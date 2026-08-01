# -*- coding: utf-8 -*-
"""Terminal-style demo GIF for AI Surface Skills README."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "demo-tool-break.gif"
POSTER = ROOT / "assets" / "demo-poster.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

W, H = 960, 540
BG = (13, 17, 23)
PANEL = (22, 27, 34)
BORDER = (48, 54, 61)
GREEN = (63, 185, 80)
RED = (248, 81, 73)
YELLOW = (210, 153, 34)
BLUE = (88, 166, 255)
MUTED = (139, 148, 158)
WHITE = (230, 237, 243)
ORANGE = (255, 166, 87)


def font(size: int, bold: bool = False):
    cands = [
        r"C:\Windows\Fonts\consolab.ttf" if bold else r"C:\Windows\Fonts\consola.ttf",
        r"C:\Windows\Fonts\CascadiaMono.ttf",
        r"C:\Windows\Fonts\cour.ttf",
    ]
    for p in cands:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


F, FT, FS = font(18), font(22, True), font(15)


def frame():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([24, 24, W - 24, H - 24], 12, fill=PANEL, outline=BORDER, width=2)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([44 + i * 22, 40, 58 + i * 22, 54], fill=c)
    d.text((130, 38), "ai-surface-skills  ·  tool-schema-breaking-review", font=FS, fill=MUTED)
    return im, d


def lines(d, items, y0=78, lh=26):
    y = y0
    for it in items:
        text, color = it if isinstance(it, tuple) else (it, WHITE)
        d.text((48, y), text, font=F, fill=color)
        y += lh


def main():
    frames, durs = [], []

    im, d = frame()
    lines(
        d,
        [
            ("$ agent", MUTED),
            "",
            ("> Compare tools.v1.json with tools.v2-bad.json", BLUE),
            ("> Follow tool-schema-breaking-review", BLUE),
            ("> Also flag permission risks", BLUE),
            "",
            ("Loading skill: tool-schema-breaking-review ...", YELLOW),
        ],
    )
    d.text((48, H - 70), "Wanbinyu/ai-surface-skills", font=FS, fill=MUTED)
    frames.append(im)
    durs.append(1400)

    im, d = frame()
    lines(
        d,
        [
            ("## Tool schema breaking review", WHITE),
            "",
            ("Before: tools.v1.json   After: tools.v2-bad.json", MUTED),
            "",
            ("Scanning tool names & params ... done", GREEN),
            ("Classifying 6 deltas ...", YELLOW),
        ],
    )
    frames.append(im)
    durs.append(1100)

    im, d = frame()
    lines(
        d,
        [
            ("### Deltas", WHITE),
            "",
            ("[BREAK] create_order -> place_order rename", RED),
            ("[BREAK] note + idempotency_key required", RED),
            ("[BREAK] status enum lost cancelled", RED),
            ("[RISK]  list_orders cross-user description", ORANGE),
            ("[RISK]  refund_order without HITL", YELLOW),
        ],
    )
    frames.append(im)
    durs.append(1800)

    im, d = frame()
    lines(
        d,
        [
            ("### Verdict", WHITE),
            "",
            ("request-changes", RED),
            "",
            ("Do not ship v2-bad tool surface.", WHITE),
            ("Keep tool names stable for agents.", WHITE),
            ("refund_order needs human-approval-gates.", WHITE),
            "",
            ("Exit criteria: checked", GREEN),
        ],
    )
    d.rounded_rectangle([48, H - 100, 420, H - 52], 8, fill=(48, 20, 20), outline=RED, width=2)
    d.text((64, H - 88), "MERGE BLOCKED", font=FT, fill=RED)
    frames.append(im)
    durs.append(2200)

    im, d = frame()
    lines(
        d,
        [
            ("AI Surface Skills", BLUE),
            ("HTTP contracts evolve. Tool contracts should too.", WHITE),
            "",
            ("9 skills  |  Tool/MCP surface  |  MIT", MUTED),
            ("Not another MCP builder.", MUTED),
            "",
            ("github.com/Wanbinyu/ai-surface-skills", GREEN),
        ],
    )
    frames.append(im)
    durs.append(2000)

    frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=durs, loop=0)
    frames[3].save(POSTER)
    print("Wrote", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
