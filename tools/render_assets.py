#!/usr/bin/env python3
"""Render the branded README images (AI Money Group: paper #fff9ee, ink #171717, orange #e65b25).

Usage:
  python tools/render_assets.py hub
  python tools/render_assets.py kit <slug> [--pdf GUIDE.pdf --pages 2,4,7]

hub  -> assets/hub-banner.png, assets/cta-guide.png, assets/cta-amg.png
kit  -> <slug>/assets/cover.png, how-it-works.png, cta-guide.png, (with --pdf) preview.png
Kit art: <slug>/assets/art.jpg (generated chapter art, no text in the image). Text is rendered as HTML so it
is always crisp; never put words inside generated images. Needs Chrome/Chromium (CHROME env to override).
"""
import base64, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = """*{box-sizing:border-box;margin:0}html,body{width:100%;height:100%;overflow:hidden}
body{background:#fff9ee;color:#171717;font-family:Arial,"Liberation Sans",Helvetica,sans-serif}
.serif{font-family:Georgia,"Liberation Serif",serif}em{font-style:normal;color:#e65b25}
.kick{font:700 15px Arial,"Liberation Sans";letter-spacing:3px;color:#bd471d;text-transform:uppercase}
.chip{display:inline-flex;align-items:center;gap:8px;background:#171717;color:#fff9ee;border-radius:30px;
  padding:9px 16px;font:700 14px Arial,"Liberation Sans";margin:0 8px 8px 0}
.chip i{width:8px;height:8px;border-radius:50%;background:#e65b25;display:inline-block}
svg.i{width:30px;height:30px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}"""
ICON = {
    "paste": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "map": '<path d="M9 3 3 6v15l6-3 6 3 6-3V3l-6 3z"/><path d="M9 3v15M15 6v15"/>',
    "book": '<path d="M2 4h7a3 3 0 0 1 3 3v14a2 2 0 0 0-2-2H2zM22 4h-7a3 3 0 0 0-3 3v14a2 2 0 0 1 2-2h8z"/>',
}


def b64(p):
    ext = p.suffix.lstrip(".").replace("jpg", "jpeg")
    return f"data:image/{ext};base64," + base64.b64encode(p.read_bytes()).decode()


def chrome():
    for c in [os.environ.get("CHROME"), r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              "google-chrome", "chromium", "chromium-browser"]:
        if c and (Path(c).exists() or shutil.which(c)):
            return c
    raise SystemExit("Chrome not found; set CHROME")


def shoot(html, out, w, h, transparent=False):
    with tempfile.TemporaryDirectory() as t:
        f = Path(t) / "x.html"
        f.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{html}", encoding="utf-8")
        extra = ["--default-background-color=00000000"] if transparent else []
        subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2", *extra,
                        f"--window-size={w},{h}", f"--screenshot={Path(out).resolve()}", f.as_uri()],
                       check=True, capture_output=True)
    if transparent:
        from PIL import Image
        im = Image.open(out).convert("RGBA")
        im.crop(im.getbbox()).save(out, optimize=True)
    print("wrote", out)


def logo():
    return f'<img src="{b64(ROOT / "assets/amg-logo.png")}" style="width:44px;height:44px;border-radius:50%">'


def banner(out, kicker, title, sub, art, chips, w=1280, h=440):
    art_html = (f'<div style="position:absolute;right:0;top:0;bottom:0;width:46%;background:url({b64(art)}) center/cover">'
                f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,#fff9ee 0%,rgba(255,249,238,0) 28%)"></div></div>'
                if art else "")
    chips_html = "".join(f'<span class="chip"><i></i>{c}</span>' for c in chips)
    shoot(f"""<div style="position:relative;width:{w}px;height:{h}px;border-bottom:10px solid #e65b25">{art_html}
      <div style="position:absolute;left:64px;top:52px;width:{'58%' if art else '85%'}">
        <div style="display:flex;align-items:center;gap:14px;margin-bottom:26px">{logo()}
          <span class="kick" style="color:#171717">AI Money Group</span></div>
        <div class="kick">{kicker}</div>
        <h1 class="serif" style="font-size:58px;line-height:1.04;margin:10px 0 16px;letter-spacing:-1px">{title}</h1>
        <p class="serif" style="font-size:22px;line-height:1.35;color:#3a3631;margin-bottom:22px">{sub}</p>
        <div>{chips_html}</div></div></div>""", out, w, h)


def cta(out, label, dark=False):
    bg, fg = ("#171717", "#fff9ee") if dark else ("#e65b25", "#171717")
    shoot(f"""<div style="padding:10px 14px 18px 10px;background:transparent">
      <div style="display:inline-flex;align-items:center;gap:14px;background:{bg};color:{fg};border:3px solid #171717;
        box-shadow:7px 7px 0 #171717;border-radius:12px;padding:20px 34px;font:800 24px Arial,'Liberation Sans';letter-spacing:.5px">
        {label}<span style="font-size:28px">→</span></div></div>
      <style>html,body{{background:transparent}}</style>""", out, 620, 110, transparent=True)


def how(out, steps):
    cells = "".join(
        f"""<div style="flex:1;text-align:center;position:relative">
          <div style="width:74px;height:74px;border-radius:50%;margin:0 auto 14px;display:flex;align-items:center;justify-content:center;
            background:{'#e65b25' if i == len(steps) - 1 else '#171717'};color:#fff">
            <svg class="i" viewBox="0 0 24 24">{ICON[ic]}</svg></div>
          <div style="font:800 15px Arial,'Liberation Sans';letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px">{t}</div>
          <div class="serif" style="font-size:17px;color:#3a3631;line-height:1.3;padding:0 10px">{d}</div>
          {'' if i == len(steps) - 1 else '<div style="position:absolute;top:36px;left:calc(50% + 46px);right:calc(-50% + 46px);border-top:3px dashed #e65b25"></div>'}
        </div>""" for i, (ic, t, d) in enumerate(steps))
    shoot(f"""<div style="padding:40px 40px 34px;width:1280px;height:300px">
        <div class="kick" style="text-align:center;margin-bottom:26px">How it works</div>
        <div style="display:flex">{cells}</div></div>""", out, 1280, 300)


def preview(pdf, pages, out):
    import pymupdf
    from PIL import Image, ImageDraw, ImageFilter
    doc = pymupdf.open(pdf)
    W, H = 2560, 1180
    sheet = Image.new("RGB", (W, H), "#171717")
    d = ImageDraw.Draw(sheet)
    d.rectangle([0, H - 16, W, H], fill="#e65b25")
    ph = 1000
    imgs = []
    for n in pages:
        pix = doc[n - 1].get_pixmap(dpi=200)
        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        imgs.append(im.resize((int(im.width * ph / im.height), ph)))
    gap = 70
    x = (W - sum(i.width for i in imgs) - gap * (len(imgs) - 1)) // 2
    for i, im in enumerate(imgs):
        y = 80 + (0 if i == len(imgs) // 2 else 30)
        sh = Image.new("RGBA", (im.width + 60, im.height + 60), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle([30, 30, im.width + 30, im.height + 30], fill=(0, 0, 0, 170))
        sheet.paste(sh.filter(ImageFilter.GaussianBlur(18)), (x - 10, y), sh.filter(ImageFilter.GaussianBlur(18)))
        sheet.paste(im, (x, y))
        x += im.width + gap
    sheet.save(out, optimize=True)
    print("wrote", out)


def main():
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == "hub":
        (ROOT / "assets").mkdir(exist_ok=True)
        art = ROOT / "assets/hub-art.jpg"
        banner(ROOT / "assets/hub-banner.png", "Free AI-ready kits",
               "Paste one line.<br><em>Your AI does the work.</em>",
               "Practical kits for marketers and business owners, built to run in the AI you already use.",
               art if art.exists() else None, ["Claude", "ChatGPT", "Claude Code", "Codex", "Hermes", "OpenClaw"])
        cta(ROOT / "assets/cta-amg.png", "JOIN AI MONEY GROUP", dark=True)
        return
    slug = a[1]
    d = ROOT / slug
    k = json.loads((d / "kit.json").read_text(encoding="utf-8"))
    (d / "assets").mkdir(exist_ok=True)
    words = k["title"].replace("The ", "").split()
    title = " ".join(words[:-2]) + f"<br><em>{' '.join(words[-2:])}</em>"
    banner(d / "assets/cover.png", "Free AI kit · " + k.get("kicker", "AI Money Group"), title, k["tagline"],
           d / "assets/art.jpg", k.get("chips", ["Copy-paste prompt", "Installable skill", "Free guide"]))
    how(d / "assets/how-it-works.png", [tuple(s) for s in k["how_it_works"]])
    cta(d / "assets/cta-guide.png", "GET THE FREE GUIDE")
    if "--pdf" in a:
        pdf = a[a.index("--pdf") + 1]
        pages = [int(p) for p in a[a.index("--pages") + 1].split(",")] if "--pages" in a else [2, 4, 7]
        preview(pdf, pages, d / "assets/preview.png")


if __name__ == "__main__":
    main()
