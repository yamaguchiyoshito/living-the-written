"""第3回「未来を知っていても、人は自由でいられるのか」の図3-1〜図3-6。"""
from __future__ import annotations

from draw_figures import Figure, person, BG, INK, MUTED, LINE, SOFT, BLUE, AMBER, TEAL, PLUM

GREY = '#8a9099'


def vtext(f: Figure, x: float, y: float, s: str, size: int = 18, color: str = INK, gap: float | None = None, weight: int = 400) -> None:
    """縦書きの代わりに1文字ずつ縦に積む（x は文字列の中心）。"""
    gap = gap or size * 1.3
    for i, ch in enumerate(s):
        f.text(x, y + i * gap, ch, size, color, anchor='middle', weight=weight)


def cross(f: Figure, x: float, y: float, r: float = 9, color: str = INK, width: float = 2.4) -> None:
    f.line(x - r, y - r, x + r, y + r, color=color, width=width)
    f.line(x - r, y + r, x + r, y - r, color=color, width=width)


def bubble(f: Figure, x: float, y: float, w: float, h: float, s: str, color: str, size: int = 20, tail: str = 'left') -> None:
    """吹き出し。tail='left' なら左辺の下寄りから左へ、'down' なら下辺の左寄りから下へ尾を出す。"""
    f.rect(x, y, w, h, fill='#ffffff', stroke=color, width=2, rx=18)
    if tail == 'left':
        d = f'M {x:.1f} {y + h * 0.55:.1f} L {x - 22:.1f} {y + h * 0.78:.1f} L {x:.1f} {y + h * 0.80:.1f} Z'
    else:
        d = f'M {x + 40:.1f} {y + h:.1f} L {x + 34:.1f} {y + h + 22:.1f} L {x + 62:.1f} {y + h:.1f} Z'
    f.path(d, color=color, width=2, fill='#ffffff')
    f.text(x + w / 2, y + h / 2 + size * 0.36, s, size, color, anchor='middle', weight=700)


def fig_a(made: set[str]) -> None:
    f = Figure(3, '自由の二つの意味', '別の行動を選べる自由と、自分の判断で行為する自由を左右に分け、確定した未来が閉じるのは左だけであることを見る。', 630, 'a')
    # 左パネル：別の行動を選べる自由
    f.panel(50, 200, 530, 350, '別の行動を選べる自由')
    f.rect(482, 250, 40, 290, fill=BLUE, stroke='none', width=0, rx=8, opacity=0.18)
    vtext(f, 502, 274, '一つに確定した未来', 16, BLUE, gap=26, weight=700)
    f.circ(110, 395, 10, AMBER)
    f.text(110, 428, '現在', 17, AMBER, anchor='middle', weight=700)
    f.box(240, 285, 160, 50, 'コーヒー', '', INK, 20)
    f.box(240, 455, 160, 50, '紅茶', '', INK, 20)
    f.line(122, 388, 232, 318, color=INK, width=2, arrow=True)
    f.line(122, 402, 232, 472, color=INK, width=2, arrow=True)
    f.line(400, 310, 476, 310, color=INK, width=2, arrow=True)
    f.line(400, 480, 436, 480, color=INK, width=2)
    cross(f, 452, 480, 8, INK)
    # 区切り
    f.line(600, 270, 600, 520, color=LINE, width=1.5)
    # 右パネル：自分の判断で行為する自由
    f.panel(620, 200, 530, 350, '自分の判断で行為する自由')
    f.box(650, 280, 170, 52, '他者の強制', '', GREY, 19)
    f.box(650, 440, 190, 52, '本人の欲求・判断', '', TEAL, 19)
    f.box(900, 355, 200, 64, 'コーヒーを飲む', '', TEAL, 21)
    f.line(820, 306, 896, 374, color=GREY, width=2, arrow=True)
    f.line(840, 466, 896, 404, color=TEAL, width=2.4, arrow=True)
    f.text(650, 522, '両立論が見る行為の原因', 15, TEAL)
    # 凡例
    for i, (c, s) in enumerate([(BLUE, '青＝知ること・記述'), (TEAL, '青緑＝行為'), (AMBER, '琥珀＝現在')]):
        x = 60 + i * 230
        f.circ(x, 588, 7, c)
        f.text(x + 16, 594, s, 15, MUTED)
    made.add(f.save('03-a-two-senses-of-freedom.svg'))


def fig_b(made: set[str]) -> None:
    f = Figure(3, '知ることと生きること', 'すでに知られている未来の出来事の列と、いまその一つひとつを行為として生きる列を上下に並べて見る。', 590, 'b')
    xs = [400, 650, 900]
    # 上段：知られている未来（3つが同時に見えている）
    vtext(f, 110, 262, '知ること', 18, BLUE, gap=26, weight=700)
    f.rect(170, 225, 960, 112, fill=BLUE, stroke=BLUE, width=2, rx=14, opacity=0.1)
    f.rect(170, 225, 960, 112, fill='none', stroke=BLUE, width=2, rx=14)
    f.text(190, 254, 'ルイーズが知っている未来', 18, BLUE, weight=700)
    for x, s in zip(xs, ['会話', '抱くこと', '喪失']):
        f.box(x - 70, 272, 140, 48, s, '', BLUE, 19)
    # 対応（仮の対応）
    for x in xs:
        f.line(x, 324, x, 426, color=MUTED, width=1.6, dash=True)
    # 下段：現在の行為（点が一つずつ通る）
    vtext(f, 110, 420, '生きること', 18, TEAL, gap=26, weight=700)
    f.line(170, 505, 1120, 505, color=TEAL, width=2.4, arrow=True)
    f.text(1130, 540, '現在の行為', 17, TEAL, anchor='end', weight=700)
    for i, (x, s) in enumerate(zip(xs, ['会話する', '抱く', '共に生きる'])):
        f.box(x - 70, 430, 140, 48, s, '', TEAL, 19, dash=(i > 0))
    f.circ(400, 505, 10, AMBER)
    f.text(400, 540, 'いま', 17, AMBER, anchor='middle', weight=700)
    made.add(f.save('03-b-knowing-and-living.svg'))


def fig_c(made: set[str]) -> None:
    f = Figure(3, '記述する言葉と遂行する言葉', '事実を説明する文と、発することで約束を成立させる文を左右に並べ、矢印の種類の違いで二つの働きを見る。', 600, 'c')
    # 左：記述する言葉（人型は置かず、言葉と世界の距離を示す）
    f.panel(50, 200, 530, 360, '記述する言葉')
    bubble(f, 215, 262, 200, 60, '雨が降っている', BLUE, 20, tail='down')
    f.box(225, 455, 180, 56, '世界の状態', '', BLUE, 20)
    f.line(315, 350, 315, 449, color=BLUE, width=2, arrow=True, dash=True)
    f.text(335, 405, '説明する', 16, BLUE)
    # 右：遂行する言葉
    f.panel(620, 200, 530, 360, '遂行する言葉')
    person(f, 715, 330, TEAL, 0.8)
    f.text(715, 396, '条件：権限・慣習', 15, MUTED, anchor='middle')
    bubble(f, 800, 262, 200, 60, '約束します', TEAL, 20, tail='left')
    f.box(795, 455, 210, 56, '約束が成立する', '', TEAL, 20)
    f.line(900, 326, 900, 449, color=TEAL, width=2.4, arrow=True)
    f.text(920, 395, '発言が行為になる', 16, TEAL)
    made.add(f.save('03-c-describing-and-performing.svg'))


def fig_d(made: set[str]) -> None:
    f = Figure(3, '自由への欲望が運命を実現する', '欲望から行為へ、行為から既知の未来へ、未来の記憶から欲望へと戻る環を、歴史全体の帯の内側で見る。', 610, 'd')
    # 歴史全体の帯
    f.rect(230, 210, 920, 360, fill=PLUM, stroke='none', width=0, rx=18, opacity=0.08)
    f.rect(230, 210, 920, 360, fill='none', stroke=PLUM, width=1.8, rx=18)
    f.text(1130, 552, '歴史全体', 19, PLUM, anchor='end', weight=700)
    # 欲望 → エレン
    px, py = 610, 440
    for i, s in enumerate(['壁の外へ出たい', '仲間を守りたい', '敵への憎しみ']):
        y = 300 + i * 78
        f.box(270, y, 180, 50, s, '', TEAL, 18)
        f.line(450, y + 25, 568, 425 + (i - 1) * 10, color=TEAL, width=2, arrow=True)
    person(f, px, py, TEAL, 1.0)
    f.text(px - 14, 510, 'エレン', 19, TEAL, anchor='middle', weight=700)
    # エレン → 行為 → 既知の未来
    f.line(660, 425, 826, 425, color=TEAL, width=4, arrow=True)
    f.text(743, 408, '行為', 18, TEAL, anchor='middle', weight=700)
    f.box(834, 393, 190, 64, '既知の未来', '', BLUE, 21)
    # 既知の未来 → 未来の記憶として知る → エレン（環）
    f.path(f'M 929 393 L 929 272 Q 929 258 915 258 L {px + 14} 258 Q {px} 258 {px} 272 L {px} 360', color=BLUE, width=2.2, arrow=True)
    f.text((929 + px) / 2, 246, '未来の記憶として知る', 16, BLUE, anchor='middle', weight=700)
    # 外からの強制（帯の外）
    f.box(50, 523, 150, 50, '外からの強制', '', GREY, 17)
    f.path('M 200 548 L 640 548 L 640 488', color=GREY, width=2, arrow=True, dash=True)
    cross(f, 400, 548, 9, GREY)
    made.add(f.save('03-d-desire-enacts-fate.svg'))


def fig_e(made: set[str]) -> None:
    f = Figure(3, 'ルイーズとエレン', '二人の未来の知り方と行動の中心と葛藤を左右に並べ、下の帯で共通点を見る。', 660, 'e')
    cols = [(415, 'ルイーズ'), (905, 'エレン')]
    rows = [(290, BLUE, '未来を知る経路', ('言語の習得', '巨人の記憶と「道」')),
            (380, TEAL, '行動の中心', ('娘との人生', '自由への欲望')),
            (470, AMBER, '葛藤', ('喪失を含む人生を受け入れる', '欲望と未来の確定性'))]
    f.line(660, 230, 660, 540, color=LINE, width=1.5)
    for (cx, name) in cols:
        person(f, cx - 45, 252, INK, 0.7)
        f.text(cx - 5, 260, name, 22, INK, weight=700)
    bw, bh = 300, 56
    band_y = 562
    for y, color, label, pair in rows:
        f.text(55, y + bh / 2 + 6, label, 16, MUTED)
        for (cx, _), s in zip(cols, pair):
            f.box(cx - bw / 2, y, bw, bh, s, '', color, 18)
    for (cx, _) in cols:
        # 1段目は左へ、2段目は右へ出てから帯へ下ろし、3段目は真下へ
        y1, y2, y3 = rows[0][0], rows[1][0], rows[2][0]
        f.path(f'M {cx - bw / 2} {y1 + bh / 2} L {cx - bw / 2 - 24} {y1 + bh / 2} L {cx - bw / 2 - 24} {band_y - 4}', color=MUTED, width=2, arrow=True)
        f.path(f'M {cx + bw / 2} {y2 + bh / 2} L {cx + bw / 2 + 24} {y2 + bh / 2} L {cx + bw / 2 + 24} {band_y - 4}', color=MUTED, width=2, arrow=True)
        f.line(cx, y3 + bh, cx, band_y - 4, color=MUTED, width=2, arrow=True)
    f.rect(170, band_y, 980, 54, fill=TEAL, stroke='none', width=0, rx=14, opacity=0.14)
    f.rect(170, band_y, 980, 54, fill='none', stroke=TEAL, width=2, rx=14)
    f.text(660, band_y + 34, '未来を知っても現在の行為を止めない', 21, TEAL, anchor='middle', weight=700)
    made.add(f.save('03-e-louise-and-eren.svg'))


def fig_f(made: set[str]) -> None:
    f = Figure(3, '記述と行為', '書物の一行と本人の行為の関係を左に、行為を含む未来と行為を欠いた未来の違いを右に見る。', 590, 'f')
    # 左：記述は原因ではない／記述が真なら行為が起きる
    f.panel(50, 200, 530, 350)
    f.box(165, 250, 300, 56, '書物の一行：コーヒーを飲む', '', BLUE, 19)
    f.box(165, 470, 300, 56, '本人がコーヒーを飲む', '', TEAL, 19)
    f.line(235, 318, 235, 462, color=MUTED, width=4, arrow=True)
    cross(f, 235, 390, 10, INK)
    f.text(220, 395, '記述は原因ではない', 15, INK, anchor='end')
    f.line(380, 390, 380, 318, color=BLUE, width=2, arrow=True, dash=True)
    f.line(380, 390, 380, 462, color=BLUE, width=2, arrow=True, dash=True)
    f.text(396, 395, '記述が真なら行為が起きる', 15, BLUE)
    # 右：行為を含む未来と、行為を欠いた未来
    f.panel(620, 200, 530, 350)
    f.text(650, 258, '未来（歴史）', 16, PLUM, weight=700)
    slots = [708, 823, 938, 1053]
    for top, skip in [(270, False), (420, True)]:
        f.rect(650, top, 470, 70, fill=PLUM, stroke='none', width=0, rx=12, opacity=0.1)
        f.rect(650, top, 470, 70, fill='none', stroke=PLUM, width=1.8, rx=12)
        for i, x in enumerate(slots):
            if skip and i == 2:
                continue
            f.rect(x - 52, top + 15, 104, 40, fill='#ffffff', stroke=TEAL, width=2, rx=8)
            if i == 2:
                f.text(x, top + 40, 'コーヒーを飲む', 14, TEAL, anchor='middle', weight=700)
    # 等号に×（同じ未来ではない）
    f.line(865, 372, 905, 372, color=MUTED, width=2.4, dash=True)
    f.line(865, 388, 905, 388, color=MUTED, width=2.4, dash=True)
    cross(f, 885, 380, 12, MUTED, 2)
    f.text(885, 525, '行為を取り除くと同じ未来ではない', 15, PLUM, anchor='middle')
    made.add(f.save('03-f-description-and-act.svg'))


def draw(made: set[str]) -> None:
    fig_a(made)
    fig_b(made)
    fig_c(made)
    fig_d(made)
    fig_e(made)
    fig_f(made)
