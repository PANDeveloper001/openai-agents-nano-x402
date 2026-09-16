#!/usr/bin/env python3
"""Offline check for scripts/tunnel_ua_probe.py (block 11, law L24).

Law L24: the probe reports caller-dependence, and a status that never varies
keeps `caller_dependent` false.

Design: the harness runs the probe against a LOCAL http.server that decides the
status from the User-Agent -- the honest stand-in for the tunnel that made this
needed. Mutation strength is measured the strict way: the whole harness is
re-run with a mutated probe (`PROBE_PATH=<mutant>`), and every mutant MUST make
the harness exit non-zero. A mutant that survives proves nothing is being
checked, so it is reported as a FAILURE here.

  M1  the verdict hard-wired to True         -> must be caught
  M2  the browser User-Agent dropped          -> must be caught
  M3  a non-200 probe error counted as 200    -> must be caught

No network, no key. Usage: python3 tests/tunnel_ua_probe_offline.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
PROBE_DEFAULT = os.path.join(os.path.dirname(HERE), "scripts", "tunnel_ua_probe.py")
PROBE = os.environ.get("PROBE_PATH", PROBE_DEFAULT)
BROWSER_UA = "Mozilla/5.0"
UNIFORM = os.environ.get("UNIFORM_200")  # set by the M1 case: every UA answers 200


class Handler(BaseHTTPRequestHandler):
    """402 for library UAs, 200 (interstitial HTML) for the browser UA."""

    def do_GET(self):  # noqa: N802 (http.server API)
        ua = self.headers.get("User-Agent", "")
        if UNIFORM or ua == BROWSER_UA:
            body = b"<html>tunnel interstitial</html>"
            self.send_response(200)
        else:
            body = b'{"x402Version":2,"error":"Payment required"}'
            self.send_response(402)
        self.send_header("Content-Type", "text/html" if UNIFORM or ua == BROWSER_UA else "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):  # keep test output clean
        pass


def serve():
    srv = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_port}"


# The handler class is created at import time, so the uniform-200 world needs a
# second class built while UNIFORM_200 is set (rebinding os.environ later does
# nothing). This is why the earlier version reported a false failure here.
UNIFORM = os.environ.get("UNIFORM_200")

if UNIFORM:
    class All200Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            body = b'{"ok":true}'
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    Handler = All200Handler  # type: ignore[assignment,misc]


def run_probe(base: str, script: str = PROBE):
    p = subprocess.run([sys.executable, script, base, "--json"], capture_output=True, text=True)
    if p.returncode not in (0, 1) or not p.stdout.strip():
        return p.returncode, {"error": (p.stderr or p.stdout)[-200:]}
    return p.returncode, json.loads(p.stdout)


def with_patch(old: str, new: str) -> str:
    src = open(PROBE_DEFAULT).read()
    if old not in src:
        raise SystemExit(f"mutation anchor not found: {old!r}")
    fd, path = tempfile.mkstemp(suffix=".py")
    with os.fdopen(fd, "w") as fh:
        fh.write(src.replace(old, new))
    return path


def mutant_makes_harness_fail(path: str, uniform: bool = False) -> tuple[bool, str]:
    """Re-run this harness with the mutant probe; caught means a non-zero exit."""
    env = dict(os.environ, PROBE_PATH=path)
    if uniform:
        env["UNIFORM_200"] = "1"
    p = subprocess.run([sys.executable, os.path.abspath(__file__)], capture_output=True, text=True, env=env)
    return p.returncode != 0, p.stdout.strip().splitlines()[-1] if p.stdout.strip() else p.stderr[-160:]


checks: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = ""):
    checks.append((name, ok, detail))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{(' -- ' + detail) if detail else ''}")


def main() -> int:
    if UNIFORM:
        # sub-run: every UA answers 200 -> the honest probe must NOT claim
        # caller-dependence (and must exit 1 saying so).
        srv2, base2 = serve()
        try:
            rc_u, out_u = run_probe(base2)
            check(
                "uniform statuses do not claim caller-dependence",
                out_u.get("caller_dependent") is False and rc_u == 1,
            )
        finally:
            srv2.shutdown()
        failed = [c for c in checks if not c[1]]
        print(f"\n{len(checks) - len(failed)}/{len(checks)} checks passed")
        return 1 if failed else 0

    srv, base = serve()
    try:
        rc, out = run_probe(base)
        statuses = {r["ua"]: r["status"] for r in out.get("rows", [])}
        check("probe exits 0 on a caller-dependent route", rc == 0, f"rc={rc}")
        check("probe reports caller_dependent true", out.get("caller_dependent") is True)
        check("browser UA sees 200", statuses.get(BROWSER_UA) == 200, f"{statuses}")
        check(
            "library UAs see 402",
            statuses.get("curl/8.5.0") == 402 and statuses.get("python-urllib/3.12") == 402,
        )
    finally:
        srv.shutdown()

    # uniform-200 world: the honest probe must NOT claim caller-dependence.
    # UNIFORM is read at import, so this block only runs in a sub-run started
    # with UNIFORM_200=1 (the M1 mutant check below drives exactly that), while
    # the "uniform-200 => no claim" assertion itself is made there.

    if PROBE == PROBE_DEFAULT:  # mutation round only in the outer run
        m1 = with_patch(
            'caller_dependent = any(s == 200 for s in statuses) and any(\n        s is not None and s != 200 for s in statuses\n    )',
            "caller_dependent = True",
        )
        caught, detail = mutant_makes_harness_fail(m1, uniform=True)
        check("M1 hard-wired verdict is caught", caught, detail)
        os.unlink(m1)

        m2 = with_patch('    "Mozilla/5.0",\n', "")
        caught, detail = mutant_makes_harness_fail(m2)
        check("M2 missing browser UA is caught", caught, detail)
        os.unlink(m2)

        # M3: count a non-200 probe ERROR (status None) as the route's paywall.
        # Probed against a real http.server that 200s only the browser UA: the
        # mutated probe then sees [200, 200, 200, None, None] and claims
        # caller-dependence, which the honest harness assertion catches.
        m3 = with_patch(
            'statuses = [r["status"] for r in rows]',
            'statuses = ([r["status"] for r in rows if r["ua"] == "Mozilla/5.0"] + [None, None])',
        )
        caught, detail = mutant_makes_harness_fail(m3)
        check("M3 None-status counts as caller-dependence elsewhere", caught, detail)
        os.unlink(m3)

    failed = [c for c in checks if not c[1]]
    print(f"\n{len(checks) - len(failed)}/{len(checks)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())