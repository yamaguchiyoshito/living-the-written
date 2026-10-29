#!/usr/bin/env python3
"""Generate every SVG illustration (cover + per-chapter figures) deterministically. Stdlib only.

各回の図は scripts/figures/chNN.py の draw(made) に置く。`python scripts/draw_figures.py` で全図を再生成し、
`python scripts/draw_figures.py --chapter 3` で第3回だけを描き直す（この場合は図の集合の照合と不要SVGの削除をしない）。

図の方針: 1枚につき主張は1つ、パネルは2枚まで、ラベルは10個前後。矢印や色だけに意味を依存させず、ラベルでも区別する。
SVGには viewBox / role="img" / title / desc を持たせ、script・外部参照・フォントファイルは入れない。
"""
from __future__ import annotations
from html import escape
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'illustrations'
BG, INK, MUTED, LINE, SOFT = '#f7f5ef', '#232a33', '#5d6873', '#d8d4c8', '#ece9e0'
BLUE, AMBER, TEAL, PLUM = '#2b5f9e', '#c7792b', '#2f8f83', '#8a4f9e'
FONT = 'system-ui, -apple-system, "Hiragino Kaku Gothic ProN", "Noto Sans CJK JP", Meiryo, sans-serif'
CODE = 'LIVING THE WRITTEN'


class Figure:
    def __init__(self, number: int, title: str, subtitle: str, height: int = 620, part: str = '', accent: str = BLUE):
        self.h = height
        self.n = number
        self.part = part
        self.accent = accent
        self.defs: list[str] = []
        self._markers: dict[str, str] = {}
        self.body: list[str] = []
        self.title = title
        self.subtitle = subtitle
        self.gradients = 0
        shown = str(ord(part) - 96) if part.isalpha() and len(part) == 1 else part
        label = CODE if number == 0 else f'{CODE}     {number:02d}' + (f'     図{number}-{shown}' if part else '')
        self.text(50, 52, label, 18, accent, weight=700)
        self.text(50, 103, title, 34, weight=700)
        self.text(50, 141, subtitle, 21, MUTED)
        self.line(50, 166, 1150, 166, color=LINE, width=1)

    # --- primitives -------------------------------------------------------
    MIN_TEXT = 14

    def text(self, x, y, s, size=24, color=INK, anchor='start', weight=400, opacity=1.0):
        size = max(size, self.MIN_TEXT)
        op = f' opacity="{opacity}"' if opacity < 1 else ''
        self.body.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}"{op}>{escape(str(s))}</text>')

    def lines(self, x, y, items, size=19, color=INK, anchor='start', gap=None, weight=400):
        gap = gap or size * 1.45
        for i, s in enumerate(items):
            self.text(x, y + i * gap, s, size, color, anchor, weight)

    def _marker(self, color):
        """One arrowhead marker per stroke colour, so heads always match their lines."""
        if color not in self._markers:
            mid = f'arrow-{color.lstrip("#")}'
            self._markers[color] = mid
            self.defs.append(f'<marker id="{mid}" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto-start-reverse"><path d="M1,1 L9,5 L1,9" fill="none" stroke="{color}" stroke-width="1.4"/></marker>')
        return self._markers[color]

    def line(self, x1, y1, x2, y2, color=MUTED, width=2, arrow=False, dash=False, dots=False, opacity=1.0):
        extra = (f' marker-end="url(#{self._marker(color)})"' if arrow else '') + (' stroke-dasharray="8 7"' if dash else '') + (' stroke-dasharray="2 9" stroke-linecap="round"' if dots else '') + (f' opacity="{opacity}"' if opacity < 1 else '')
        self.body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}"{extra}/>')

    def path(self, d, color=MUTED, width=2, arrow=False, dash=False, fill='none', opacity=1.0):
        extra = (f' marker-end="url(#{self._marker(color)})"' if arrow else '') + (' stroke-dasharray="8 7"' if dash else '') + (f' opacity="{opacity}"' if opacity < 1 else '')
        self.body.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}"{extra}/>')

    def rect(self, x, y, w, h, fill='#ffffff', stroke=LINE, width=2, rx=12, dash=False, opacity=1.0):
        extra = (' stroke-dasharray="8 7"' if dash else '') + (f' opacity="{opacity}"' if opacity < 1 else '')
        self.body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"{extra}/>')

    def box(self, x, y, w, h, title, subtitle='', color=BLUE, size=22, dash=False, fill='#ffffff'):
        self.rect(x, y, w, h, fill=fill, stroke=color, width=2, rx=14, dash=dash)
        self.text(x + w / 2, y + (h / 2 + 8 if not subtitle else h / 2 - 4), title, size, color, anchor='middle', weight=700)
        if subtitle:
            self.text(x + w / 2, y + h / 2 + 26, subtitle, 17, MUTED, anchor='middle')

    def circ(self, x, y, r=10, color=BLUE, fill=True, dash=False, width=2, opacity=1.0):
        op = f' opacity="{opacity}"' if opacity < 1 else ''
        if fill:
            self.body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"{op}/>')
        else:
            extra = ' stroke-dasharray="7 6"' if dash else ''
            self.body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}"{extra}{op}/>')

    def panel(self, x, y, w, h, label=''):
        self.rect(x, y, w, h, fill='none', stroke='#c9c4b6', width=2, rx=16, dash=True)
        if label:
            self.text(x + w / 2, y + 34, label, 23, INK, anchor='middle', weight=700)

    def blob(self, cx, cy, r, color, opacity=0.55):
        self.gradients += 1
        gid = f'g{self.n:02d}{self.part}-{self.gradients}'
        self.defs.append(f'<radialGradient id="{gid}"><stop offset="0" stop-color="{color}" stop-opacity="{opacity}"/><stop offset="0.55" stop-color="{color}" stop-opacity="{opacity*0.45:.2f}"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>')
        self.body.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="url(#{gid})"/>')

    def wave(self, x0, x1, y, amp, periods, color=BLUE, width=2, steps=240, phase=0.0, opacity=1.0):
        pts = []
        for i in range(steps + 1):
            t = i / steps
            pts.append(f'{x0 + (x1 - x0) * t:.1f},{y - amp * math.sin(2 * math.pi * periods * t + phase):.1f}')
        op = f' opacity="{opacity}"' if opacity < 1 else ''
        self.body.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"{op}/>')

    def square_wave(self, x0, x1, y, amp, periods, color=BLUE, width=2):
        pts = [f'{x0:.1f},{y + amp:.1f}']
        seg = (x1 - x0) / periods
        for k in range(periods):
            a, b = x0 + k * seg, x0 + (k + 0.5) * seg
            pts += [f'{a:.1f},{y - amp:.1f}', f'{b:.1f},{y - amp:.1f}', f'{b:.1f},{y + amp:.1f}', f'{a + seg:.1f},{y + amp:.1f}']
        self.body.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}"/>')

    def brace(self, x0, x1, y, down=True, color=MUTED):
        """A horizontal brace spanning x0..x1 with its point at y (pointing down if down)."""
        m = (x0 + x1) / 2
        s = 10 if down else -10
        d = f'M {x0:.1f} {y - s:.1f} Q {x0:.1f} {y:.1f} {x0 + 12:.1f} {y:.1f} L {m - 12:.1f} {y:.1f} Q {m:.1f} {y:.1f} {m:.1f} {y + s:.1f} Q {m:.1f} {y:.1f} {m + 12:.1f} {y:.1f} L {x1 - 12:.1f} {y:.1f} Q {x1:.1f} {y:.1f} {x1:.1f} {y - s:.1f}'
        self.path(d, color=color, width=1.6)

    def footer(self, s):
        if s:
            self.text(50, self.h - 28, s, 19, MUTED)

    def save(self, name: str):
        OUT.mkdir(parents=True, exist_ok=True)
        head = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{self.h}" viewBox="0 0 1200 {self.h}" role="img" aria-labelledby="title desc">',
                f'<title id="title">{escape(self.title)}</title>', f'<desc id="desc">{escape(self.subtitle)}</desc>',
                '<defs>' + ''.join(self.defs) + '</defs>', f'<rect width="1200" height="{self.h}" rx="20" fill="{BG}"/>',
                f'<g font-family=\'{FONT}\'>']
        (OUT / name).write_text('\n'.join(head + self.body + ['</g>', '</svg>']) + '\n', encoding='utf-8')
        return name


def log_axis(f, x0, x1, y, lo, hi, ticks, label='', color=MUTED):
    """A log10 axis from lo..hi (in the same unit) mapped to x0..x1. ticks: list of (value, label)."""
    def X(v):
        return x0 + (math.log10(v) - math.log10(lo)) / (math.log10(hi) - math.log10(lo)) * (x1 - x0)
    f.line(x0, y, x1 + 30, y, color=color, width=2, arrow=True)
    for v, t in ticks:
        x = X(v)
        f.line(x, y - 6, x, y + 6, color=color, width=1.5)
        f.text(x, y + 28, t, 16, MUTED, anchor='middle')
    if label:
        f.text(x1 + 36, y + 6, label, 16, MUTED)
    return X


def band(f, X, lo, hi, y, h, color, label='', sub='', text_color=None, min_w=10):
    x0, x1 = X(lo), X(hi)
    if x1 - x0 < min_w:
        x0, x1 = (x0 + x1) / 2 - min_w / 2, (x0 + x1) / 2 + min_w / 2
    f.rect(x0, y, x1 - x0, h, fill=color, stroke='none', width=0, rx=h / 2, opacity=0.78)
    if label:
        f.text(x0 - 14, y + h / 2 + 6, label, 17, text_color or INK, anchor='end')
    if sub:
        f.text(x1 + 12, y + h / 2 + 6, sub, 15, MUTED)


def person(f, x, y, color=INK, scale=1.0, lean=0.0):
    """A running silhouette: head, leaning torso, limbs with round caps. (x, y) is the hip."""
    s = scale
    f.circ(x + 10 * s * lean, y - 60 * s, 12 * s, color)
    f.body.append(f'<ellipse cx="{x + 5 * s * lean:.1f}" cy="{y - 26 * s:.1f}" rx="{11 * s:.1f}" ry="{24 * s:.1f}" transform="rotate({-18 * lean:.0f} {x + 5 * s * lean:.1f} {y - 26 * s:.1f})" fill="{color}"/>')
    for (x1, y1, x2, y2, w) in [(x, y - 4 * s, x - 22 * s, y + 34 * s, 8), (x, y - 4 * s, x + 24 * s, y + 28 * s, 8), (x + 4 * s, y - 38 * s, x - 22 * s, y - 20 * s, 6.5), (x + 4 * s, y - 38 * s, x + 26 * s, y - 46 * s, 6.5)]:
        f.body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{w * s:.1f}" stroke-linecap="round"/>')


def loop_nodes(f, cx, cy, r, labels, color=BLUE, box_w=190, box_h=58, size=18, start=-math.pi / 2):
    """Nodes placed on a circle, connected clockwise with arrows. Returns the node centers."""
    n = len(labels)
    centers = []
    for i in range(n):
        a = start + 2 * math.pi * i / n
        centers.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    for i in range(n):
        a0 = start + 2 * math.pi * i / n
        a1 = start + 2 * math.pi * (i + 1) / n
        pad = 0.42 * (box_w / 2) / r + 0.08
        p0 = (cx + r * math.cos(a0 + pad), cy + r * math.sin(a0 + pad))
        p1 = (cx + r * math.cos(a1 - pad), cy + r * math.sin(a1 - pad))
        f.path(f'M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}', color=color, width=2.2, arrow=True)
    for (x, y), lab in zip(centers, labels):
        title, sub = (lab if isinstance(lab, tuple) else (lab, ''))
        f.box(x - box_w / 2, y - box_h / 2, box_w, box_h, title, sub, color, size)
    return centers


def draw_cover(made: set[str]) -> None:
    f = Figure(0, '書かれたものを生きる', '時間・因果・自由・記憶・物語・虚構・持続の哲学、全8回', 700)
    # 一枚の長いページ。行はすべて書かれている。「いま」より左は読まれた行、右はまだ読まれていない行。
    f.rect(70, 196, 760, 290, fill='#ffffff', stroke=LINE, width=2, rx=10)
    now_x = 420
    f.rect(now_x - 26, 180, 52, 420, fill=AMBER, stroke='none', width=0, rx=8, opacity=0.14)
    f.text(now_x, 176, 'いま', 20, AMBER, anchor='middle', weight=700)
    widths = [0.92, 0.78, 0.88, 0.7, 0.95, 0.82, 0.74]
    for i, w in enumerate(widths):
        y = 232 + i * 31
        x0, x1 = 110, 110 + 690 * w
        if x1 <= now_x:
            f.line(x0, y, x1, y, color=INK, width=5)
        elif x0 >= now_x:
            f.line(x0, y, x1, y, color=LINE, width=5)
        else:
            f.line(x0, y, now_x, y, color=INK, width=5)
            f.line(now_x, y, x1, y, color=LINE, width=5)
    f.text(250, 466, '読まれた行', 15, MUTED, anchor='middle')
    f.text(620, 466, '書かれているが、まだ読まれていない行', 15, MUTED, anchor='middle')
    person(f, now_x, 560, INK, 0.95)
    f.lines(880, 262, ['結末まで書かれていても、', '読む行為は省略できない。', '', '未来が決まっていても、', 'その未来はまだ', '経験されていない。'], 22, INK, gap=34)
    f.text(600, 634, 'すべてが決まっていたとしても、すべてはまだ生きられていない。', 28, BLUE, anchor='middle', weight=700)
    f.footer('時間、因果、自由、記憶、物語、虚構、持続。七つの問いを八回でたどる。')
    made.add(f.save('00-cover.svg'))


def chapter_module(n: int):
    import importlib
    import sys
    sys.path.insert(0, str(ROOT / 'scripts'))
    try:
        return importlib.import_module(f'figures.ch{n:02d}')
    except ModuleNotFoundError:
        return None


def main(argv: list[str] | None = None) -> None:
    import argparse
    parser = argparse.ArgumentParser(description='挿絵SVGを生成する')
    parser.add_argument('--chapter', type=int, action='append', help='この回だけ描き直す（照合と不要SVGの削除をしない）')
    args = parser.parse_args(argv)
    series = json.loads((ROOT / 'series.json').read_text(encoding='utf-8'))
    made: set[str] = set()
    if args.chapter:
        for n in args.chapter:
            module = chapter_module(n)
            if module is None:
                raise SystemExit(f'scripts/figures/ch{n:02d}.py がない')
            module.draw(made)
        print(f'wrote {len(made)} SVG files for chapters {args.chapter}: {sorted(made)}')
        return
    draw_cover(made)
    for c in series['chapters']:
        module = chapter_module(c['number'])
        if module is not None:
            module.draw(made)
    expected = {'00-cover.svg'} | {Path(p).name for c in series['chapters'] for p in c['figures']}
    missing = expected - made
    extra = made - expected
    if missing or extra:
        raise SystemExit(f'figure set mismatch with series.json: missing={sorted(missing)} extra={sorted(extra)}')
    for stale in OUT.glob('*.svg'):
        if stale.name not in made:
            stale.unlink()
    print(f'wrote {len(made)} SVG files to {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
