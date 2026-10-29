"""第7回　なぜ完成させることが、失うことになるのか — 図7-1〜図7-6。"""
from __future__ import annotations
import math

from draw_figures import Figure, person, BG, INK, MUTED, LINE, SOFT, BLUE, AMBER, TEAL, PLUM


def legend(f: Figure, y: float, items: list[tuple[str, str]], x: float = 50) -> None:
    """色の凡例を一行に並べる。items は (色, 文) の列。"""
    for color, s in items:
        f.circ(x + 7, y - 6, 7, color)
        f.text(x + 22, y, s, 15, MUTED)
        x += 22 + len(s) * 15 + 34


def outline_person(f: Figure, x: float, y: float, color: str, scale: float = 1.0) -> None:
    """輪郭だけの立ち姿。(x, y) は腰。"""
    s = scale
    f.circ(x, y - 58 * s, 11 * s, color, fill=False, width=2)
    f.body.append(f'<ellipse cx="{x:.1f}" cy="{y - 20 * s:.1f}" rx="{12 * s:.1f}" ry="{24 * s:.1f}" fill="none" stroke="{color}" stroke-width="2"/>')
    for (x1, y1, x2, y2) in [(x, y + 2 * s, x - 10 * s, y + 34 * s), (x, y + 2 * s, x + 10 * s, y + 34 * s)]:
        f.body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="2" stroke-linecap="round"/>')


def open_canvas(f: Figure, x: float, y: float, w: float, h: float, color: str = TEAL, fill: str = '#ffffff') -> None:
    """右辺だけ破線にした長方形（制作中の絵）。"""
    f.rect(x, y, w, h, fill=fill, stroke='none', width=0, rx=0)
    f.path(f'M {x + w:.1f} {y:.1f} L {x:.1f} {y:.1f} L {x:.1f} {y + h:.1f} L {x + w:.1f} {y + h:.1f}', color=color, width=2)
    f.line(x + w, y, x + w, y + h, color=color, width=2, dash=True)


def draw(made: set[str]) -> None:
    fig_a(made)
    fig_b(made)
    fig_c(made)
    fig_d(made)
    fig_e(made)
    fig_f(made)


# --- 図7-1 -----------------------------------------------------------------
def fig_a(made: set[str]) -> None:
    f = Figure(7, '「描いた」と「描いている」', '同じ描く行為を、閉じた全体として外から見る場合と、進行中の内側から見る場合の違いを見る。', 600, 'a')
    f.panel(50, 200, 530, 320, '完了的な見方')
    f.panel(620, 200, 530, 320, '未完了的な見方')

    # 左：閉じた箱と外からの視点
    f.text(300, 288, '絵を描いた', 19, TEAL, anchor='middle', weight=700)
    f.rect(170, 300, 260, 120, fill='#ffffff', stroke=TEAL, width=2.5, rx=8)
    f.wave(200, 400, 360, 10, 3, TEAL, 2)
    f.circ(520, 252, 9, BLUE)
    f.text(538, 258, '視点', 14, MUTED)
    f.line(511, 260, 440, 300, color=BLUE, width=2, arrow=True)
    f.text(455, 338, '一つのまとまり', 16, BLUE)
    f.text(300, 460, '外から全体を見る', 15, MUTED, anchor='middle')

    # 右：開いたままの帯と内側の視点
    f.text(760, 310, '絵を描いている', 19, TEAL, anchor='middle', weight=700)
    f.rect(650, 330, 390, 60, fill=TEAL, stroke='none', width=0, rx=0, opacity=0.2)
    f.line(650, 330, 1040, 330, color=TEAL, width=2)
    f.line(650, 390, 1040, 390, color=TEAL, width=2)
    f.line(650, 330, 650, 390, color=TEAL, width=2)
    pts = ' '.join(f'{1040 + 6 * math.sin(k / 4):.1f},{330 + k:.1f}' for k in range(0, 61, 2))
    f.body.append(f'<polyline points="{pts}" fill="none" stroke="{TEAL}" stroke-width="2"/>')
    f.line(1052, 360, 1092, 360, color=TEAL, width=2, arrow=True, opacity=0.55)
    f.text(1075, 412, 'まだ終わらない', 15, MUTED, anchor='middle')
    f.line(860, 300, 860, 420, color=AMBER, width=3)
    f.circ(860, 360, 9, BLUE)
    f.text(876, 366, '視点', 14, MUTED)
    f.text(860, 442, 'いま', 17, AMBER, anchor='middle', weight=700)
    f.text(860, 466, '進行中に視点を置く', 15, MUTED, anchor='middle')

    legend(f, 562, [(BLUE, '青＝見方'), (TEAL, '青緑＝描く行為'), (AMBER, '琥珀＝いま')])
    made.add(f.save('07-a-perfective-and-imperfective.svg'))


# --- 図7-2 -----------------------------------------------------------------
def fig_b(made: set[str]) -> None:
    f = Figure(7, '描き終えて失われるのは、君ではなく関係', '描いているあいだと描き終えた後で、画家と君のあいだに何が残り何が消えるかを見る。', 600, 'b')
    f.panel(50, 200, 530, 370, '描いているあいだ')
    f.panel(620, 200, 530, 370, '描き終えた後')

    for dx, during in ((0, True), (570, False)):
        # 画家
        person(f, 130 + dx, 400, TEAL if during else MUTED, 0.9, 0.3)
        f.text(130 + dx, 466, '画家', 16, INK, anchor='middle', weight=700)
        # 絵
        if during:
            open_canvas(f, 250, 290, 120, 180)
            f.text(310, 278, '制作中の絵', 14, MUTED, anchor='middle')
            f.line(178, 380, 240, 380, color=TEAL, width=4, arrow=True)
            f.text(208, 366, '描く', 17, TEAL, anchor='middle', weight=700)
        else:
            f.rect(250 + dx, 290, 120, 180, fill='#ffffff', stroke=INK, width=2, rx=0)
            f.text(310 + dx, 278, '絵は残る', 16, INK, anchor='middle', weight=700)
            f.line(178 + dx, 380, 240 + dx, 380, color=MUTED, width=1.5, arrow=True, dash=True, opacity=0.7)
        # 君
        outline_person(f, 455 + dx, 400, PLUM, 0.9)
        f.text(478 + dx, 388, '君', 17, PLUM, weight=700)
        # 現在の帯
        if during:
            f.rect(90, 500, 450, 24, fill=AMBER, stroke='none', width=0, rx=4, opacity=0.25)
            f.text(96, 517, '現在', 15, AMBER, weight=700)
            for x, s in ((200, '一夜目'), (330, '十夜目'), (460, '百夜目')):
                f.line(x, 500, x, 524, color=AMBER, width=2)
                f.text(x, 548, s, 14, MUTED, anchor='middle')
            f.line(378, 372, 433, 372, color=PLUM, width=2, arrow=True, dash=True)
            f.line(455, 434, 455, 494, color=AMBER, width=2.5, arrow=True)
            f.text(467, 468, '現在に呼び出す', 15, AMBER)
        else:
            f.rect(90 + dx, 507, 450, 10, fill=AMBER, stroke='none', width=0, rx=3, opacity=0.25)
            f.text(96 + dx, 545, '現在', 15, AMBER, weight=700)
            f.line(378 + dx, 372, 433 + dx, 372, color=MUTED, width=1.5, dots=True, opacity=0.5)
            f.line(455 + dx, 434, 455 + dx, 494, color=MUTED, width=1.5, dots=True, opacity=0.5)
            f.text(467 + dx, 468, '関係が終わる', 15, MUTED, weight=700)
    made.add(f.save('07-b-relation-lost-at-completion.svg'))


# --- 図7-3 -----------------------------------------------------------------
def fig_c(made: set[str]) -> None:
    f = Figure(7, '百夜は、百個の夜ではない', '同じ百夜を、数えられる単位の列として見る場合と、過去を含んで厚くなる一つの流れとして見る場合を見る。', 790, 'c')
    f.panel(50, 200, 1100, 180, '時計時間')
    n, w, step, x0 = 16, 32, 46, 120
    for i in range(n):
        f.rect(x0 + i * step, 278, w, w, fill='#ffffff', stroke=BLUE, width=2, rx=6)
    f.text(x0 + w / 2, 340, '一夜目', 15, MUTED, anchor='middle')
    f.text(x0 + 7 * step + w / 2 + step / 2, 340, '…', 16, MUTED, anchor='middle')
    f.text(x0 + (n - 1) * step + w / 2, 340, '百夜目', 15, MUTED, anchor='middle')
    f.text(x0 + n * step + 24, 301, '百個の単位', 17, BLUE, weight=700)

    f.panel(50, 410, 1100, 290, '制作の持続')
    f.defs.append(f'<linearGradient id="g07c-band" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{PLUM}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient>')
    xl, xr = 110, 940
    f.path(f'M {xl} 565 Q 560 555 {xr} 490 L {xr} 660 Q 560 585 {xl} 575 Z', color='none', width=0, fill='url(#g07c-band)', opacity=0.5)
    for k in range(5):
        f.path(f'M {xl} 570 Q 560 {566 + k * 10} {xr} {505 + k * 36}', color=PLUM, width=1.5, opacity=0.5)
    f.text(xl, 605, '一夜目', 15, PLUM, anchor='middle')
    f.text(330, 548, '過去が残る', 16, PLUM, anchor='middle', weight=700)
    f.rect(920, 480, 40, 190, fill=AMBER, stroke='none', width=0, rx=6, opacity=0.4)
    f.text(940, 468, '百夜目', 17, AMBER, anchor='middle', weight=700)
    f.lines(972, 570, ['一夜目から九十九夜目', 'までの経験を含む'], 15, INK, gap=24)
    f.text(560, 686, '分割すると意味を失う', 15, MUTED, anchor='middle')

    legend(f, 752, [(BLUE, '青＝時計で測る時間'), (PLUM, '紫＝残る過去'), (TEAL, '青緑＝描く経験'), (AMBER, '琥珀＝現在')])
    made.add(f.save('07-c-hundred-nights-as-duration.svg'))


# --- 図7-4 -----------------------------------------------------------------
def fig_d(made: set[str]) -> None:
    f = Figure(7, '過去は現在に残り、現在が過去を成立させる', '記憶論では過去から現在へ、作品では現在から過去へと向きが逆になる二つの矢印と、両者が重なる点を見る。', 720, 'd')
    f.panel(50, 200, 530, 450, 'ベルクソン')
    f.panel(620, 200, 530, 450, '『ストロボライト』')

    # 左：純粋記憶から現在へ
    f.box(190, 260, 250, 70, '現在の知覚と行為', '', AMBER, 20)
    f.rect(110, 540, 410, 60, fill=PLUM, stroke=PLUM, width=2, rx=10, opacity=0.25)
    f.text(315, 577, '純粋記憶', 20, PLUM, anchor='middle', weight=700)
    f.text(315, 628, '過去のまま保存', 15, MUTED, anchor='middle')
    f.line(250, 538, 250, 334, color=PLUM, width=2.5, arrow=True)
    f.circ(250, 436, 10, PLUM)
    f.text(266, 442, '記憶イメージ', 16, PLUM)
    f.line(400, 334, 400, 536, color=AMBER, width=1.5, arrow=True, dash=True)
    f.text(414, 442, '意味を変える', 16, AMBER)

    # 右：書く現在が過去を立ち上げる
    f.box(760, 250, 250, 80, '書く現在', '小説家の浜崎正', AMBER, 20)
    f.path('M 720 400 L 1020 400 L 1050 430 L 1050 590 L 720 590 Z', color=LINE, width=2, fill='#ffffff')
    f.path('M 1020 400 L 1020 430 L 1050 430', color=LINE, width=2)
    f.text(745, 428, '物語の内部', 16, MUTED)
    person(f, 885, 515, PLUM, 0.9, 0.2)
    f.text(885, 575, '二十歳の浜崎正', 17, PLUM, anchor='middle', weight=700)
    f.line(885, 334, 885, 446, color=TEAL, width=2.5, arrow=True)
    f.text(900, 394, '書く', 18, TEAL, weight=700)
    f.line(700, 585, 700, 440, color=MUTED, width=1.5, arrow=True)
    f.line(691, 520, 709, 506, color=MUTED, width=1.5)
    f.text(700, 618, '通常とは逆の向き', 14, MUTED, anchor='middle')

    f.text(600, 690, '過去と現在は独立ではない', 20, INK, anchor='middle', weight=700)
    made.add(f.save('07-d-memory-and-writing-the-past.svg'))


# --- 図7-5 -----------------------------------------------------------------
def fig_e(made: set[str]) -> None:
    f = Figure(7, '生きている未完了と、止まった未完了', '同じ「完成していない」状態を、行為が続いている場合と止まっている場合に分けて見る。', 690, 'e')
    f.text(600, 224, 'どちらも完成していない', 19, INK, anchor='middle', weight=700)
    f.panel(50, 240, 530, 370, '生きている未完了')
    f.panel(620, 240, 530, 370, '止まった未完了')

    # 左：描き続ける
    person(f, 140, 430, TEAL, 0.9, 0.3)
    f.text(140, 496, '画家', 16, INK, anchor='middle', weight=700)
    f.defs.append(f'<linearGradient id="g07e-fill" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{TEAL}" stop-opacity="0.05"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0.5"/></linearGradient>')
    open_canvas(f, 330, 330, 140, 180, fill='url(#g07e-fill)')
    f.line(188, 410, 320, 410, color=TEAL, width=4, arrow=True)
    f.text(254, 440, '描き続ける', 17, TEAL, anchor='middle', weight=700)
    f.wave(196, 222, 372, 4, 1, TEAL, 2)
    f.wave(232, 268, 372, 7, 1.5, TEAL, 2)
    f.wave(278, 322, 372, 10, 2, TEAL, 2)
    f.text(258, 342, '新しい表現が生まれる', 15, TEAL, anchor='middle')
    f.text(400, 540, '関係が変わる', 16, TEAL, anchor='middle', weight=700)

    # 右：止まったまま
    person(f, 710, 430, MUTED, 0.9, -0.5)
    f.text(710, 496, '画家', 16, INK, anchor='middle', weight=700)
    open_canvas(f, 900, 330, 140, 180, color=MUTED)
    f.line(758, 410, 812, 410, color=MUTED, width=2, dots=True)
    f.text(782, 440, '制作が進まない', 15, MUTED, anchor='middle')
    f.line(842, 330, 842, 510, color=MUTED, width=2)
    f.text(842, 540, '停止', 16, MUTED, anchor='middle', weight=700)

    f.text(600, 656, '未完了が幸福なのではない', 20, INK, anchor='middle', weight=700)
    made.add(f.save('07-e-living-and-stalled-incompletion.svg'))


# --- 図7-6 -----------------------------------------------------------------
def fig_f(made: set[str]) -> None:
    f = Figure(7, '完成は、持続の停止ではない', '完成の境界を越えても経験が記憶として続き、作品は別の関係へ、経験は次の行為へ流れていく形を見る。', 650, 'f')
    # 制作の持続（左）
    f.rect(80, 300, 460, 70, fill=TEAL, stroke='none', width=0, rx=8, opacity=0.3)
    f.text(310, 342, '制作の持続', 20, TEAL, anchor='middle', weight=700)
    # 記憶として残る経験（右へ続く細い帯）
    f.rect(540, 325, 570, 20, fill=PLUM, stroke='none', width=0, rx=4, opacity=0.4)
    f.text(560, 312, '記憶として残る経験', 16, PLUM, weight=700)
    f.text(560, 372, '持続は止まらない', 15, MUTED)
    # 完成の境界
    f.line(540, 240, 540, 560, color=AMBER, width=3)
    f.text(540, 228, '完成', 20, AMBER, anchor='middle', weight=700)
    f.text(552, 264, '行為は終わる', 15, AMBER)
    # 作品と読者
    f.rect(505, 420, 70, 50, fill='#ffffff', stroke=INK, width=2, rx=0)
    f.text(540, 452, '作品', 17, INK, anchor='middle', weight=700)
    f.line(578, 455, 690, 520, color=BLUE, width=2, arrow=True)
    f.text(625, 502, '別の関係', 16, BLUE)
    person(f, 730, 555, BLUE, 0.8, 0.0)
    f.text(730, 612, '読者・鑑賞者', 16, BLUE, anchor='middle', weight=700)
    # 次の行為（右上へ立ち上がる帯）
    f.path('M 880 335 Q 980 310 1110 200', color=TEAL, width=40, opacity=0.3)
    f.text(950, 262, '次の行為', 19, TEAL, anchor='middle', weight=700)
    f.line(1060, 323, 1060, 262, color=PLUM, width=2.5, arrow=True)
    f.text(1060, 372, '次の判断を形づくる', 15, PLUM, anchor='middle')
    made.add(f.save('07-f-completion-within-duration.svg'))
