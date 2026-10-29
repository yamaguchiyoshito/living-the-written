"""第4回「同じ時間を生きなければ、共に生きられないのか」の挿絵6枚。

凡例（この回で共通）: 歴史の年代の軸＝青、各人物の経験の順序の軸＝青緑、記憶の蓄積＝紫、「いま」＝琥珀。
歴史の年代と経験の順序は別の線として描き、同じ出来事の対応は破線で結ぶ。
"""
from __future__ import annotations

from draw_figures import Figure, person, BG, INK, MUTED, LINE, SOFT, BLUE, AMBER, TEAL, PLUM


def _cross(f: Figure, x: float, y: float, color: str, r: float = 7, width: float = 2.6) -> None:
    f.line(x - r, y - r, x + r, y + r, color=color, width=width)
    f.line(x - r, y + r, x + r, y - r, color=color, width=width)


def fig_a(made: set[str]) -> None:
    f = Figure(4, '30億年の記憶は一方向に積み重なる', '人間の記憶との長さの違いと、記憶が一方向にだけ積み重なって過去へ戻れない構造を見る。', 560, 'a', accent=PLUM)
    # 比較用の短い帯（人間の記憶）。主帯 660px に対して 1/30 ほど。
    f.rect(100, 222, 24, 14, fill=PLUM, stroke='none', width=0, rx=7, opacity=0.6)
    f.text(136, 235, '人間の記憶：数十年', 15, MUTED)
    # 「いま」
    now = 760
    f.text(now, 262, 'いま', 19, AMBER, anchor='middle', weight=700)
    f.line(now, 272, now, 462, color=AMBER, width=3)
    # 30億年の記憶の帯
    f.text(100, 298, '受け継がれた記憶', 15, MUTED)
    f.rect(100, 310, now - 100, 60, fill=PLUM, stroke='none', width=0, rx=10, opacity=0.22)
    f.text(118, 347, '30億年の記憶', 19, PLUM, weight=700)
    # 出会った人々と、いまへ持ち越される記憶
    for i, px in enumerate((330, 470, 610)):
        person(f, px, 352, INK, 0.5)
        f.line(px + 6, 318, now - 4, 300 - i * 8, color=PLUM, width=1.4)
    f.text(470, 395, '出会った人々', 16, INK, anchor='middle')
    f.text(100, 395, '生命の起源', 16, INK)
    # 戻れない（いまから過去へ戻る短い矢印に×）
    f.line(now - 6, 395, now - 60, 395, color=PLUM, width=2, arrow=True)
    _cross(f, now - 33, 395, PLUM)
    f.text(now - 33, 420, '戻れない', 15, PLUM, anchor='middle', weight=700)
    # まだ経験していない未来
    f.rect(790, 310, 330, 60, fill='none', stroke=TEAL, width=2, rx=10, dash=True)
    f.text(955, 347, 'まだ経験していない未来', 17, TEAL, anchor='middle')
    # 一方向
    f.line(100, 448, now - 10, 448, color=TEAL, width=2.4, arrow=True)
    f.text(430, 474, '一方向', 17, TEAL, anchor='middle', weight=700)
    f.footer('逐次的認識：出来事を順番に知っていく形は、記憶の長さが変わっても変わらない。')
    made.add(f.save('04-a-emanon-one-way-memory.svg'))


def fig_b(made: set[str]) -> None:
    f = Figure(4, '歴史の年代と経験の順序は別の軸である', '同じ三つの年が歴史の軸と経験の軸で異なる順に並び、対応線が交差する様子を見る。', 620, 'b')
    xs = (340, 600, 860)
    y_top, y_bot = 270, 470
    # 歴史の年代（青）
    f.text(120, 258, '歴史の年代', 19, BLUE, weight=700)
    f.line(120, y_top, 1020, y_top, color=BLUE, width=2.4, arrow=True)
    for x, yr in zip(xs, ('1960', '1985', '2020')):
        f.line(x, y_top - 7, x, y_top + 7, color=BLUE, width=2)
        f.text(x, y_top - 14, yr, 17, BLUE, anchor='middle', weight=700)
    # 対応（破線）: 1960→1番目, 1985→3番目, 2020→2番目
    for xt, xb in ((xs[0], xs[0]), (xs[1], xs[2]), (xs[2], xs[1])):
        f.line(xt, y_top + 10, xb, y_bot - 10, color=MUTED, width=1.6, dash=True)
    # ヒカリの経験の順序（青緑）
    f.text(120, y_bot - 12, 'ヒカリの経験の順序', 19, TEAL, weight=700)
    f.line(120, y_bot, 1020, y_bot, color=TEAL, width=2.4, arrow=True)
    for x, nth, yr in zip(xs, ('1番目', '2番目', '3番目'), ('1960', '2020', '1985')):
        f.line(x, y_bot - 7, x, y_bot + 7, color=TEAL, width=2)
        f.text(x, y_bot + 30, nth, 17, TEAL, anchor='middle', weight=700)
        f.text(x, y_bot + 54, yr, 15, MUTED, anchor='middle')
    # 2番目から3番目へ、記憶を持って移る（紫）
    f.rect(602, 402, 256, 26, fill=BG, stroke='none', width=0, rx=6)
    f.text(730, 421, '2020年の記憶を持って1985年へ', 15, PLUM, anchor='middle', weight=700)
    f.path(f'M {xs[1] + 12} {y_bot - 12} Q 730 400 {xs[2] - 14} {y_bot - 12}', color=PLUM, width=2, arrow=True)
    # 経験は順に積み重なる
    f.line(xs[0], 560, xs[2] + 30, 560, color=TEAL, width=2.4, arrow=True)
    f.text(615, 590, '経験は順に積み重なる', 17, TEAL, anchor='middle', weight=700)
    f.text(1150, 375, '二つの順序は一致しない', 17, INK, anchor='end', weight=700)
    made.add(f.save('04-b-years-and-order.svg'))


def fig_c(made: set[str]) -> None:
    f = Figure(4, '逆行と跳躍、どちらも経験は順に積む', '方向が反転しても連続する逆行と、離れた年代へ不連続に移る跳躍を並べ、どちらにも経験の順序があることを見る。', 630, 'c')
    f.panel(50, 200, 535, 320, '『TENET』の逆行')
    f.panel(615, 200, 535, 320, 'ヒカリの移動')
    # 左: 順行者・逆行者が同じ出来事で重なる
    f.rect(257, 270, 120, 200, fill=SOFT, stroke=BLUE, width=1.5, rx=12)
    f.text(110, 286, '順行者', 17, TEAL, weight=700)
    f.line(110, 300, 530, 300, color=TEAL, width=2.4, arrow=True)
    f.text(90, 372, '歴史の時間', 17, BLUE, weight=700)
    f.line(90, 380, 545, 380, color=BLUE, width=2.4, arrow=True)
    f.text(530, 446, '逆行者', 17, TEAL, anchor='end', weight=700)
    f.line(530, 460, 110, 460, color=TEAL, width=2.4, arrow=True)
    f.text(530, 492, '連続したまま方向が反転', 15, MUTED, anchor='end')
    f.text(317, 348, '同じ出来事', 17, BLUE, anchor='middle', weight=700)
    # 右: 1960→2020→1985 と不連続に跳ぶ
    xs = (720, 880, 1040)
    y = 380
    f.line(655, y, 1110, y, color=BLUE, width=2.4, arrow=True)
    for x, yr in zip(xs, ('1960', '1985', '2020')):
        f.line(x, y - 7, x, y + 7, color=BLUE, width=2)
        f.text(x, y + 36, yr, 16, BLUE, anchor='middle', weight=700)
    f.path(f'M {xs[0]} {y - 10} Q 880 236 {xs[2] - 6} {y - 22}', color=TEAL, width=2.4, arrow=True)
    f.text(880, 296, '①', 20, TEAL, anchor='middle', weight=700)
    f.path(f'M {xs[2] + 32} {y + 6} Q 965 492 {xs[1] + 8} {y + 8}', color=TEAL, width=2.4, arrow=True)
    f.text(962, 468, '②', 20, TEAL, anchor='middle', weight=700)
    f.text(1125, 330, '不連続に移る', 15, MUTED, anchor='end')
    # 共通の帯
    f.rect(50, 548, 1100, 50, fill=TEAL, stroke='none', width=0, rx=12, opacity=0.12)
    f.text(600, 580, '主観的な経験は順に積み重なる', 20, TEAL, anchor='middle', weight=700)
    made.add(f.save('04-c-inversion-and-leaps.svg'))


def fig_d(made: set[str]) -> None:
    f = Figure(4, '一方の初対面が、他方には再会になる', '一本の歴史の線と、それを別の順序で横切る線が二度交わり、同じ交点が一方には初対面で他方には再会になる様子を見る。', 620, 'd')
    y = 400
    ax, bx = 440, 820
    # 紫の帯: 左から右へ記憶が溜まる
    segs = 8
    for i in range(segs):
        x0 = 90 + i * (950 / segs)
        f.rect(x0, y - 12, 950 / segs + 1, 24, fill=PLUM, stroke='none', width=0, rx=0, opacity=0.05 + 0.03 * i)
    f.line(90, y, 1060, y, color=BLUE, width=2.4, arrow=True)
    f.text(90, 440, 'エマノンの時間（歴史の順序）', 17, BLUE, weight=700)
    # ヒカリの線: Bから入り、上へ抜けてAへ降りる
    f.path(f'M 900 560 L {bx} {y} C 740 300 520 300 {ax} {y} L 380 490', color=TEAL, width=2.4, arrow=True)
    f.text(630, 298, 'ヒカリの時間（経験の順序）', 17, TEAL, anchor='middle', weight=700)
    f.text(905, 516, '①', 20, TEAL, weight=700)
    f.text(350, 480, '②', 20, TEAL, anchor='end', weight=700)
    for x in (ax, bx):
        f.circ(x, y, 9, '#ffffff')
        f.circ(x, y, 9, BLUE, fill=False, width=3)
    f.text(ax, 436, '出会いA', 16, INK, anchor='middle', weight=700)
    f.text(bx, 436, '出会いB', 16, INK, anchor='middle', weight=700)
    f.text(630, 436, '同じ出来事、異なる位置', 16, INK, anchor='middle')
    f.text(ax - 18, 372, 'エマノン：初めて', 16, PLUM, anchor='end', weight=700)
    f.text(bx + 18, 372, 'エマノン：二度目', 16, PLUM, weight=700)
    f.text(ax + 22, 466, 'ヒカリ：二度目', 16, TEAL, weight=700)
    f.text(bx - 22, 466, 'ヒカリ：初めて', 16, TEAL, anchor='end', weight=700)
    f.footer('青＝歴史の順序、青緑＝経験の順序、紫の帯＝積み重なる記憶。')
    made.add(f.save('04-d-first-meeting-and-reunion.svg'))


def fig_e(made: set[str]) -> None:
    f = Figure(4, '同じ現在にいても、経験している時間は違う', '同じ現在に並ぶ二人が、それぞれ別の時間に意識を向けている様子と、それでも二人を結ぶ線を見る。', 560, 'e', accent=AMBER)
    # 同じ時計時間の帯
    f.rect(300, 220, 600, 40, fill=AMBER, stroke='none', width=0, rx=10, opacity=0.18)
    f.text(318, 246, '同じ時計時間', 17, AMBER, weight=700)
    f.text(600, 247, 'いま', 20, AMBER, anchor='middle', weight=700)
    # 帯の外側の箱
    f.box(80, 300, 220, 60, '十年前の出来事', color=PLUM, size=18)
    f.box(900, 300, 220, 60, '来週の予定', color=BLUE, size=18)
    f.text(190, 386, '相手の時間の外側', 14, MUTED, anchor='middle')
    f.text(1010, 386, '相手の時間の外側', 14, MUTED, anchor='middle')
    # 二人とベンチ
    lx, rx = 520, 690
    person(f, lx, 430, PLUM, 0.9)
    person(f, rx, 430, BLUE, 0.9)
    f.line(430, 470, 780, 470, color=MUTED, width=3)
    f.text(605, 500, '同じ景色を眺める', 16, INK, anchor='middle')
    # 意識の向く先（破線）
    f.line(lx - 12, 372, 300, 332, color=PLUM, width=1.6, dash=True)
    f.line(rx + 12, 372, 900, 332, color=BLUE, width=1.6, dash=True)
    # 関係
    f.line(lx + 30, 420, rx - 30, 420, color=TEAL, width=2.6)
    f.text(605, 408, '関係', 17, TEAL, anchor='middle', weight=700)
    f.footer('共有できない時間を持つ相手と結ぶ。')
    made.add(f.save('04-e-same-present-different-time.svg'))


def fig_f(made: set[str]) -> None:
    f = Figure(4, '日付は動かず、意味だけが動く', '歴史の一点に固定された出会いが、二人の人生の線では異なる位置に置かれ、後の出来事から意味が書き換わる構造を見る。', 650, 'f')
    dx, y_d = 560, 260
    ex, y_e = 800, 400
    hx, y_h = 320, 540
    # 歴史の日付（青）
    f.text(120, 248, '歴史の日付', 19, BLUE, weight=700)
    f.line(120, y_d, 1000, y_d, color=BLUE, width=2.4, arrow=True)
    f.text(dx, 240, '同じ出会い：日付は動かない', 17, BLUE, anchor='middle', weight=700)
    # 対応（破線）
    f.line(dx, y_d + 10, ex, y_e - 10, color=MUTED, width=1.6, dash=True)
    f.line(dx, y_d + 10, hx, y_h - 10, color=MUTED, width=1.6, dash=True)
    # エマノンの人生（紫）
    f.text(120, y_e - 12, 'エマノンの人生', 19, PLUM, weight=700)
    f.rect(150, y_e - 8, ex - 165, 16, fill=PLUM, stroke='none', width=0, rx=8, opacity=0.2)
    f.line(120, y_e, 1000, y_e, color=PLUM, width=2.4, arrow=True)
    f.text(300, y_e - 15, '長い孤独', 17, PLUM, anchor='middle', weight=700)
    f.text(300, y_e + 32, '過去の記憶として', 15, MUTED, anchor='middle')
    f.text(ex, y_e + 32, '出会い', 15, INK, anchor='middle')
    # ヒカリの人生（青緑）
    f.text(120, y_h - 12, 'ヒカリの人生', 19, TEAL, weight=700)
    f.line(120, y_h, 1000, y_h, color=TEAL, width=2.4, arrow=True)
    f.text(hx - 24, y_h + 28, '出会い', 15, INK, anchor='end')
    for x in (600, 760):
        f.circ(x, y_h, 7, TEAL)
    f.text(680, y_h - 15, '後の出来事', 17, TEAL, anchor='middle', weight=700)
    f.text(680, y_h + 32, '未来の経験として', 15, MUTED, anchor='middle')
    f.path(f'M 586 {y_h + 16} Q 460 612 {hx + 18} {y_h + 14}', color=PLUM, width=2, arrow=True, dash=True)
    f.text(470, 618, '後の出来事が意味を変える', 16, PLUM, anchor='middle', weight=700)
    # 出会いの印
    for x, yy in ((dx, y_d), (ex, y_e), (hx, y_h)):
        f.circ(x, yy, 9, '#ffffff')
        f.circ(x, yy, 9, BLUE if yy == y_d else (PLUM if yy == y_e else TEAL), fill=False, width=3)
    f.text(1150, 470, '時間的位置≠意味的位置', 17, INK, anchor='end', weight=700)
    made.add(f.save('04-f-date-fixed-meaning-moves.svg'))


def draw(made: set[str]) -> None:
    fig_a(made)
    fig_b(made)
    fig_c(made)
    fig_d(made)
    fig_e(made)
    fig_f(made)
