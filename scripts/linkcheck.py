#!/usr/bin/env python3
"""Check every cited source URL and report the ones that are gone.

Usage:
  python3 scripts/linkcheck.py [--out report.md] [--workers 8] [--timeout 20]

Reads the source URLs from the article frontmatter (via scripts/kg.py) and requests each one.
Only standard-library modules are used.

A URL is reported as DEAD when the server says the page does not exist (404, 410), the host
does not resolve, or the request is redirected to a different site. Everything else that is not
a clean 200 is reported as UNCERTAIN, because many documentation sites answer automated requests
with 403, 429 or a timeout while the page is fine in a browser. Note that a 200 does not prove
the page still says what the article claims: some Salesforce doc sites serve an application
shell for any path. The release refresh in CLAUDE.md step 2a is what re-verifies content; this
check only catches links that have plainly gone.

Exit code: always 0 unless the script itself fails. The workflow turns the report into an issue.
"""
from __future__ import annotations

import socket
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kg  # noqa: E402

UA = "Mozilla/5.0 (compatible; salesforce-knowledge-graph-linkcheck; +https://github.com/john1hsu/salesforce-knowledge-graph)"
DEAD_STATUS = {404, 410}


def site(host: str) -> str:
    """Registrable-ish name: last two labels, so www.salesforce.com and help.salesforce.com match."""
    return ".".join(host.lower().split(".")[-2:])


def fetch(url: str, timeout: int) -> tuple[str, str]:
    """Return (verdict, detail) where verdict is ok | dead | uncertain."""
    last = ("uncertain", "no response")
    for attempt in range(2):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*;q=0.8"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                final = resp.geturl()
                if site(urlparse(final).netloc) != site(urlparse(url).netloc):
                    return "dead", f"redirects to another site: {final}"
                return "ok", str(resp.status)
        except urllib.error.HTTPError as e:
            if e.code in DEAD_STATUS:
                return "dead", f"HTTP {e.code}"
            last = ("uncertain", f"HTTP {e.code}")
            if e.code not in (429, 500, 502, 503, 504):
                return last
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.gaierror):
                return "dead", "host does not resolve"
            last = ("uncertain", str(e.reason)[:80])
        except Exception as e:  # timeouts, TLS errors, malformed responses
            last = ("uncertain", f"{type(e).__name__}: {str(e)[:60]}")
    return last


def main() -> int:
    args = sys.argv[1:]
    out, args = kg.opt(args, "--out")
    workers, args = kg.opt(args, "--workers")
    timeout, args = kg.opt(args, "--timeout")
    arts, errs = kg.load_articles()
    if errs:
        print("\n".join(errs))
        return 1
    cited: dict[str, list[str]] = defaultdict(list)
    for a in arts:
        for s in a.get("sources") or []:
            if isinstance(s, dict) and s.get("url"):
                cited[str(s["url"])].append(a["_path"])
    urls = sorted(cited)
    with ThreadPoolExecutor(max_workers=int(workers or 8)) as pool:
        results = dict(zip(urls, pool.map(lambda u: fetch(u, int(timeout or 20)), urls)))

    dead = [(u, d) for u, (v, d) in results.items() if v == "dead"]
    unsure = [(u, d) for u, (v, d) in results.items() if v == "uncertain"]
    lines = [f"Checked {len(urls)} source URLs cited by {len(arts)} articles: "
             f"{len(urls) - len(dead) - len(unsure)} OK, {len(dead)} dead, {len(unsure)} uncertain.", ""]
    if dead:
        lines += ["## Dead links", "",
                  "Replace each with a current official page the next time the article is refreshed "
                  "(CLAUDE.md step 2a), or sooner by hand.", ""]
        for u, d in dead:
            lines += [f"- {u} ({d})"] + [f"  - `{p}`" for p in sorted(set(cited[u]))]
        lines.append("")
    if unsure:
        by_reason: dict[str, int] = defaultdict(int)
        for _, d in unsure:
            by_reason[d] += 1
        lines += ["## Uncertain", "",
                  "These did not answer cleanly. Most are sites that block automated requests, so they are "
                  "counted here and not listed as dead.", ""]
        lines += [f"- {n} x {r}" for r, n in sorted(by_reason.items(), key=lambda kv: -kv[1])]
        lines.append("")
    report = "\n".join(lines)
    print(report)
    if out:
        Path(out).write_text(report, encoding="utf-8")
        Path(out).with_suffix(".count").write_text(str(len(dead)), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
