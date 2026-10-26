#!/usr/bin/env python3
"""Gate before anything in this public repo is merged: privacy scan + opt-in link checks.

Usage: python tools/check_kits.py [--allow-unpublished]
Fails (exit 1) when:
  - any file contains private material (home paths, internal hosts/IPs, tokens, chat IDs, team names, emails);
  - a kit is missing the generated opt-in banner in README.md, START-HERE.md or SKILL.md, or the agent note;
  - a banner link lacks utm tags or points somewhere other than the kit's optin_url;
  - the opt-in page is not live (optin_live false or the URL does not return 200), unless --allow-unpublished
    (only for private review before the funnel launches; never for the public merge).
"""
import json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIVATE = [
    (r"/home/[a-z]", "home-directory path"),
    (r"asusrogai|acemagicai|asusrogwhite|heroi", "internal machine user"),
    (r"\b100\.(6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d+\.\d+\b", "Tailscale IP"),
    (r"\b(10\.(20|99)\.0|172\.16\.1)\.\d+\b", "internal network IP"),
    (r"\b(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|xox[bp]-[A-Za-z0-9-]{10,})", "secret token"),
    (r"\b1[45]\d{16,18}\b", "Discord/Telegram id"),
    (r"(?i)\b(hazel|liezel|aifleetrouter|fleet-router|hermes-agent|openclaw\.json)\b", "internal name"),
    (r"[A-Za-z0-9._%+-]+@(?!example\.)[A-Za-z0-9.-]+\.[a-z]{2,}", "email address"),
]
TEXT_EXT = {".md", ".txt", ".json", ".py", ".yaml", ".yml", ".html", ".csv"}


def scan(path):
    hits = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for pat, what in PRIVATE:
        for m in re.finditer(pat, text):
            line = text.count("\n", 0, m.start()) + 1
            hits.append(f"{path.relative_to(ROOT)}:{line}: {what}: {m.group(0)[:40]}")
    return hits


def url_ok(url):
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "amg-kits-check"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:
        return False


def main():
    allow = "--allow-unpublished" in sys.argv
    errors = []
    for f in ROOT.rglob("*"):
        if f.is_file() and ".git" not in f.parts and f.suffix in TEXT_EXT and f.parent.name != "tools":
            errors += scan(f)
    for kj in ROOT.glob("*/kit.json"):
        d, k = kj.parent, json.loads(kj.read_text(encoding="utf-8"))
        base = k["optin_url"]
        for name in ("README.md", "START-HERE.md", "SKILL.md"):
            p = d / name
            t = p.read_text(encoding="utf-8") if p.exists() else ""
            if "<!-- amg:optin-banner -->" not in t:
                errors.append(f"{d.name}/{name}: opt-in banner missing (run tools/build_kits.py)")
            links = re.findall(re.escape(base) + r"[^)\s\"]*", t)
            if not links:
                errors.append(f"{d.name}/{name}: no link to the opt-in page {base}")
            elif not all("utm_source=github" in l for l in links):
                errors.append(f"{d.name}/{name}: opt-in link without utm tags")
        if "<!-- amg:agent-note -->" not in (d / "START-HERE.md").read_text(encoding="utf-8"):
            errors.append(f"{d.name}/START-HERE.md: agent note missing")
        for rel, _ in k["files"]:
            if not (d / rel).exists():
                errors.append(f"{d.name}: listed file missing: {rel}")
        if not allow:
            if not k.get("optin_live"):
                errors.append(f"{d.name}: optin_live is false; publish the opt-in page first")
            elif not url_ok(base):
                errors.append(f"{d.name}: opt-in page {base} did not return 200")
    for e in errors:
        print("FAIL", e)
    print("PASS" if not errors else f"\n{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
