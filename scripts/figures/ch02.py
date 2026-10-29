"""第2回「原因は本当に結果より先にあるのか」の挿絵7枚。"""
from __future__ import annotations
import math

from draw_figures import Figure, BG, INK, MUTED, LINE, SOFT, BLUE, AMBER, TEAL, PLUM

PALE_BLUE = '#9db6d4'


def _arc(f, cx, cy, r, x_from, y_from, x_to, y_to, color, sweep=0):
    """Small angle arc about (cx, cy) from the direction of (x_from, y_from) to that of (x_to, y_to)."""
    a0 = math.atan2(y_from - cy, x_from - cx)
    a1 = math.atan2(y_to - cy, x_to - cx)
    p0 = (cx + r * math.cos(a0), cy + r * math.sin(a0))
    p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
    f.path(f'M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 {sweep} {p1[0]:.1f} {p1[1]:.1f}', color=color, width=1.8)


def _refraction_scene(f, ox, label):
    """空気と水の境界、点A・点B。ox はパネルの左端。戻り値は A, P(境界上の実際の点), B の座標。"""
    a = (ox + 90, 285)
    p = (ox + 280, 465)
    b = (ox + 400, 645)
    f.rect(ox + 30, 465, 470, 215, fill=SOFT, stroke='none', width=0, rx=0)
    f.line(ox + 30, 465, ox + 500, 465, color=MUTED, width=1.6)
    f.text(ox + 40, 450, '空気', 16, MUTED)
    f.text(ox + 40, 492, '水', 16, MUTED)
    f.text(ox + 495, 452, '境界面', 15, MUTED, anchor='end')
    f.circ(a[0], a[1], 7, INK)
    f.circ(b[0], b[1], 7, INK)
    f.text(a[0] - 16, a[1] + 7, 'A', 18, INK, anchor='end', weight=700)
    f.text(b[0] + 16, b[1] + 7, 'B', 18, INK, weight=700)
    return a, p, b


def fig_a(made):
    f = Figure(2, '屈折の二つの説明', '空気から水へ入る光の経路を、境界での角度で説明する図と、始点から終点までの経路全体の所要時間で説明する図を並べて見る。', 740, 'a')
    # 左パネル：境界での条件（局所）
    f.panel(50, 200, 530, 490, '境界での条件（局所）')
    a, p, b = _refraction_scene(f, 50, 'left')
    f.line(a[0], a[1], p[0], p[1], color=BLUE, width=3)
    f.line(p[0], p[1], b[0], b[1], color=BLUE, width=3, arrow=True)
    f.line(p[0], p[1] - 75, p[0], p[1] + 75, color=MUTED, width=1.4, dash=True)
    f.text(p[0] + 8, p[1] - 62, '垂線', 15, MUTED)
    _arc(f, p[0], p[1], 52, p[0], p[1] - 100, a[0], a[1], BLUE, sweep=0)
    _arc(f, p[0], p[1], 52, p[0], p[1] + 100, b[0], b[1], BLUE, sweep=0)
    f.text(p[0] - 30, p[1] - 60, '入射側の角度', 15, BLUE, anchor='end')
    f.text(p[0] + 66, p[1] + 66, '屈折側の角度', 15, BLUE)
    f.circ(p[0], p[1], 9, AMBER)
    f.text(p[0] - 18, p[1] + 36, '手前の状況だけを見る', 15, AMBER, anchor='end')
    # 右パネル：経路全体の条件（全体）
    f.panel(620, 200, 530, 490, '経路全体の条件（全体）')
    a, p, b = _refraction_scene(f, 620, 'right')
    for px in (p[0] - 120, p[0] - 35, p[0] + 100):
        f.line(a[0], a[1], px, 465, color=PALE_BLUE, width=1.5)
        f.line(px, 465, b[0], b[1], color=PALE_BLUE, width=1.5)
    f.line(a[0], a[1], p[0], p[1], color=BLUE, width=3.4)
    f.line(p[0], p[1], b[0], b[1], color=BLUE, width=3.4, arrow=True)
    # パネル内の小さな凡例
    f.line(930, 300, 968, 300, color=BLUE, width=3.4)
    f.text(978, 306, '実際の経路', 16, BLUE, weight=700)
    f.text(978, 330, '所要時間が停留する経路', 15, BLUE)
    f.line(930, 360, 968, 360, color=PALE_BLUE, width=1.5)
    f.text(978, 366, '候補の経路', 16, MUTED)
    f.text(b[0] - 30, b[1] + 32, '終点まで含めて決まる', 15, BLUE, anchor='middle')
    f.footer('青＝記述、琥珀＝いま手前にある状況')
    made.add(f.save('02-a-fermat-two-descriptions.svg'))


def fig_b(made):
    f = Figure(2, '各時点の法則と経路全体の条件', '運動を時点ごとに決める記述と、出発から到着までの経路全体に条件を課す記述を並べ、両者が対応することを見る。', 640, 'b')
    # 左パネル：各時点で成り立つ法則
    f.panel(50, 200, 490, 380, '各時点で成り立つ法則')
    bw, bh, gap, y = 100, 58, 50, 335
    xs = [85, 85 + bw + gap, 85 + 2 * (bw + gap)]
    for x, lab in zip(xs, ['ある時点', '次の時点', 'その次']):
        f.box(x, y, bw, bh, lab, '', BLUE, 18)
    for x in xs[:2]:
        f.line(x + bw + 4, y + bh / 2, x + bw + gap - 4, y + bh / 2, color=BLUE, width=2.2, arrow=True)
    f.line(xs[2] + bw + 4, y + bh / 2, xs[2] + bw + 42, y + bh / 2, color=BLUE, width=2.2, arrow=True)
    f.text(xs[0] + bw / 2, y - 18, '位置と速度と力', 16, BLUE, anchor='middle')
    f.text((xs[0] + bw + xs[1]) / 2, y + bh + 26, '次の時点を決める', 15, MUTED, anchor='middle')
    f.line(100, 500, 490, 500, color=LINE, width=2)
    f.circ(100, 500, 6, INK)
    f.circ(490, 500, 6, INK)
    f.text(100, 530, '出発の時刻', 15, MUTED, anchor='middle')
    f.text(490, 530, '到着の時刻', 15, MUTED, anchor='middle')
    # 中央：数学的に対応する
    f.line(600, 445, 552, 445, color=BLUE, width=2, arrow=True, dash=True)
    f.line(600, 445, 648, 445, color=BLUE, width=2, arrow=True, dash=True)
    f.text(600, 420, '数学的に', 15, BLUE, anchor='middle')
    f.text(600, 475, '対応する', 15, BLUE, anchor='middle')
    # 右パネル：経路全体に課した条件
    f.panel(660, 200, 490, 380, '経路全体に課した条件')
    x0, x1, y0, y1 = 710, 1100, 440, 400
    f.rect(x0, 270, x1 - x0, 36, fill=BLUE, stroke='none', width=0, rx=8, opacity=0.14)
    f.text((x0 + x1) / 2, 294, '出発から到着まで足し合わせた量　→　一次変分がゼロ', 15, BLUE, anchor='middle')
    f.path(f'M {x0} {y0} C 820 330, 980 520, {x1} {y1}', color=BLUE, width=3)
    f.path(f'M {x0} {y0} C 800 355, 1010 480, {x1} {y1}', color=BLUE, width=1.6, dash=True)
    f.text(820, 362, '実際の経路', 16, BLUE, weight=700, anchor='middle')
    f.text(1000, 478, 'わずかにずらした経路', 15, MUTED, anchor='middle')
    f.line(x0, 500, x1, 500, color=LINE, width=2)
    f.circ(x0, y0, 6, INK)
    f.circ(x1, y1, 6, INK)
    f.line(x0, y0 + 8, x0, 500, color=LINE, width=1.2, dash=True)
    f.line(x1, y1 + 8, x1, 500, color=LINE, width=1.2, dash=True)
    f.text(x0, 530, '出発の時刻', 15, MUTED, anchor='middle')
    f.text(x1, 530, '到着の時刻', 15, MUTED, anchor='middle')
    f.footer('黒丸＝固定した端点。実線＝実際の経路、破線＝わずかにずらした経路')
    made.add(f.save('02-b-local-law-and-whole-path.svg'))


def _bezier_poly(f, x0, x1, yc, d, wobble, color, width, opacity=1.0, steps=160):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        y = yc + 3 * t * (1 - t) * d + wobble * math.sin(2 * math.pi * 4 * t) * math.sin(math.pi * t)
        pts.append(f'{x0 + (x1 - x0) * t:.1f},{y:.1f}')
    op = f' opacity="{opacity}"' if opacity < 1 else ''
    f.body.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"{op}/>')


def fig_c(made):
    f = Figure(2, 'すべての経路の寄与を重ねる', '始点から終点へ至る多数の経路と、そのうち古典的な極限で寄与が効く停留する経路の近くの帯を見る。', 740, 'c')
    x0, x1, yc = 150, 1050, 460
    f.rect(150, 210, 900, 40, fill=BLUE, stroke='none', width=0, rx=8, opacity=0.14)
    f.text(600, 236, '寄与の重ね合わせ：経路ごとの寄与が位相を持って干渉する', 17, BLUE, anchor='middle')
    # 可能な経路すべて（薄い青）
    for d, w in [(-215, 0), (-150, 0), (-115, 16), (130, 0), (165, 14), (205, 0)]:
        _bezier_poly(f, x0, x1, yc, d, w, PALE_BLUE, 1.5)
    # 停留する経路の近くの帯
    pts_a = [(x0 + (x1 - x0) * t, yc + 3 * t * (1 - t) * -70) for t in [i / 80 for i in range(81)]]
    pts_b = [(x0 + (x1 - x0) * t, yc + 3 * t * (1 - t) * 50) for t in [i / 80 for i in range(81)]]
    d = 'M ' + ' L '.join(f'{x:.1f} {y:.1f}' for x, y in pts_a) + ' L ' + ' L '.join(f'{x:.1f} {y:.1f}' for x, y in reversed(pts_b)) + ' Z'
    f.path(d, color='none', width=0, fill=BLUE, opacity=0.10)
    _bezier_poly(f, x0, x1, yc, -70, 0, BLUE, 2.2, opacity=0.7)
    _bezier_poly(f, x0, x1, yc, 50, 0, BLUE, 2.2, opacity=0.7)
    _bezier_poly(f, x0, x1, yc, -10, 0, BLUE, 3.6)
    f.circ(x0, yc, 8, INK)
    f.circ(x1, yc, 8, INK)
    f.text(x0, yc + 36, '始点', 17, INK, anchor='middle', weight=700)
    f.text(x1, yc + 36, '終点', 17, INK, anchor='middle', weight=700)
    f.text(175, 300, '可能な経路すべて', 16, MUTED)
    f.text(600, 438, '停留する経路', 17, BLUE, anchor='middle', weight=700)
    f.text(600, 527, 'その近くの経路　古典的な極限で効く', 15, BLUE, anchor='middle')
    f.rect(150, 660, 900, 40, fill=SOFT, stroke='none', width=0, rx=8)
    f.text(600, 686, '計算のための数学的な表現。粒子が経路を試して選ぶのではない', 17, INK, anchor='middle')
    made.add(f.save('02-c-path-integral-superposition.svg'))


def fig_d(made):
    f = Figure(2, '未来のエレンと過去のグリシャの輪', '過去から未来へ一方向に進む因果の連鎖と、グリシャの行動とエレンの働きかけが互いに依存して閉じる輪を並べて見る。', 740, 'd')

    def axis(x, w):
        f.line(x + 24, 615, x + w - 30, 615, color=MUTED, width=1.6, arrow=True)
        f.text(x + 24, 600, '過去', 15, MUTED)
        f.text(x + w - 24, 600, '未来', 15, MUTED, anchor='end')

    # 左パネル：通常の因果
    f.panel(50, 200, 470, 440, '通常の因果')
    axis(50, 470)
    bw, bh, gap, y = 100, 64, 46, 408
    xs = [80, 80 + bw + gap, 80 + 2 * (bw + gap)]
    for x in xs:
        f.box(x, y, bw, bh, '出来事', '', PLUM, 18)
    for x in xs:
        f.line(x + bw + 4, y + bh / 2, x + bw + gap - 2, y + bh / 2, color=PLUM, width=2.2, arrow=True)
    f.text(285, 530, '一方向に進む', 16, PLUM, anchor='middle')
    # 右パネル：因果ループ
    f.panel(560, 200, 590, 440, '因果ループ')
    axis(560, 590)
    lx, rx, by, bh = 600, 900, 400, 80
    f.box(lx, by, 230, bh, 'グリシャ（過去）', 'レイス家と対峙する', PLUM, 20)
    f.box(rx, by, 210, bh, '未来のエレン', '', PLUM, 20)
    f.path(f'M {lx + 115} {by - 6} C 740 300, 960 300, {rx + 105} {by - 6}', color=PLUM, width=2.4, arrow=True)
    f.path(f'M {rx + 105} {by + bh + 6} C 960 580, 740 580, {lx + 115} {by + bh + 6}', color=PLUM, width=2.4, arrow=True)
    f.text(860, 308, '行動が未来の状況を成立させる', 15, PLUM, anchor='middle')
    f.text(860, 588, '働きかけが過去の行動を促す', 15, PLUM, anchor='middle')
    f.text(865, 445, '閉じた輪', 15, MUTED, anchor='middle')
    f.text(855, 672, '過去の書き換えではなく、働きかけを含めて成立した歴史', 15, INK, anchor='middle')
    f.footer('紫＝物語の出来事、実線＝因果')
    made.add(f.save('02-d-causal-loop.svg'))


def fig_e(made):
    f = Figure(2, '「道」は時間の外にある', '過去から未来へ並ぶ人物や出来事の列と、その順序の外で全員を結ぶ「道」の面を見る。', 700, 'e')
    # 上段：時間の軸と平行でない面「道」
    plane = 'M 250 235 L 1030 205 L 950 395 L 170 425 Z'
    f.path(plane, color=PLUM, width=2, fill=PLUM, opacity=0.10)
    f.path(plane, color=PLUM, width=2)
    f.text(300, 270, '「道」　時間の秩序の外', 20, PLUM, weight=700)
    f.text(60, 318, '時間の外', 15, PLUM)
    f.text(60, 342, '相互に結ぶ', 15, PLUM)
    xs = [220, 380, 540, 700, 860]
    nodes = [(300, 335), (430, 305), (600, 325), (740, 285), (870, 315)]
    named = {1: 'グリシャ', 3: 'エレン'}
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            f.line(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1], color=PLUM, width=1.6, opacity=0.5)
    for i, (nx, ny) in enumerate(nodes):
        f.circ(nx, ny, 9 if i in named else 6, PLUM if i in named else MUTED)
    f.text(1000, 255, '離れた人物や出来事が結びつく', 15, PLUM, anchor='end')
    # 各時点から面への対応（破線）
    y = 560
    for x, (nx, ny) in zip(xs, nodes):
        f.line(x, y - 14, nx, ny + 12, color=PLUM, width=1.6, dash=True)
    f.text(900, 470, '各時点が「道」に現れる', 15, PLUM)
    # 下段：通常の時間の軸
    f.line(180, y, 1080, y, color=MUTED, width=2, arrow=True)
    f.text(60, 548, '通常の時間', 15, MUTED)
    f.text(60, 572, '先後に並ぶ', 15, MUTED)
    f.text(180, 594, '過去', 15, MUTED)
    f.text(1080, 594, '未来', 15, MUTED, anchor='end')
    for i, x in enumerate(xs):
        if i in named:
            f.circ(x, y, 11, PLUM)
            f.text(x, 596, named[i], 17, PLUM, anchor='middle', weight=700)
        else:
            f.circ(x, y, 7, MUTED)
    f.text(600, 638, '順序の外から全体を見る　出来事は先後の関係だけでなく相互の関係でも理解される', 17, INK, anchor='middle')
    f.footer('紫＝物語の人物と「道」、灰＝ほかの人物や出来事、破線＝「道」での対応')
    made.add(f.save('02-e-path-outside-time.svg'))


def fig_f(made):
    f = Figure(2, '同じ退職に二つの意味', '一つの退職から二つの結末へ進む経過と、それぞれの結末から退職へ戻って与えられる意味の違いを見る。', 740, 'f')
    f.box(330, 400, 190, 70, '仕事を辞めた', '', AMBER, 20)
    f.box(760, 300, 240, 70, '新しい仕事で成功した', '', TEAL, 19)
    f.box(760, 500, 240, 70, 'うまくいかなかった', '', TEAL, 19)
    f.line(524, 425, 752, 340, color=TEAL, width=2.4, arrow=True)
    f.line(524, 445, 752, 530, color=TEAL, width=2.4, arrow=True)
    f.text(640, 362, '後の出来事', 15, TEAL, anchor='middle')
    f.path('M 800 294 C 700 230, 490 230, 400 394', color=BLUE, width=2, arrow=True, dash=True)
    f.path('M 800 576 C 700 640, 490 640, 400 476', color=BLUE, width=2, arrow=True, dash=True)
    f.text(610, 246, '転機として語られる', 16, BLUE, anchor='middle')
    f.text(610, 642, '失敗の原因として語られる', 16, BLUE, anchor='middle')
    f.text(316, 442, '出来事そのものは変わらない', 15, INK, anchor='end')
    f.text(880, 442, '変わるのは全体の中での意味', 15, INK, anchor='middle')
    f.line(100, 668, 1090, 668, color=MUTED, width=1.6, arrow=True)
    f.text(1104, 674, '時間', 15, MUTED)
    f.footer('琥珀＝転機とされる出来事、青緑＝その後の経験、青の破線＝後から与える意味')
    made.add(f.save('02-f-resignation-meaning-from-outcome.svg'))


def fig_g(made):
    f = Figure(2, '経験の方向と解釈の方向', '人生の線の上を過去から未来へ進む経験の矢印と、現在から過去へ戻る解釈の矢印を見る。', 630, 'g')
    y = 385
    f.line(120, y, 1080, y, color=MUTED, width=2)
    f.text(1092, y + 6, '人生', 16, MUTED)
    events = [250, 420, 590, 760]
    for x in events:
        f.circ(x, y, 12, TEAL)
        f.text(x, y - 24, '出来事', 15, TEAL, anchor='middle')
    f.circ(960, y, 14, AMBER)
    f.text(960, y - 26, '現在', 16, AMBER, anchor='middle', weight=700)
    f.line(180, 285, 1020, 285, color=TEAL, width=3, arrow=True)
    f.text(600, 260, '経験の方向　出来事が順番に生じる', 18, TEAL, anchor='middle', weight=700)
    f.line(960, y + 20, 960, 503, color=BLUE, width=1.6, dash=True)
    f.line(960, 505, 180, 505, color=BLUE, width=2.4, arrow=True, dash=True)
    for x in events:
        f.line(x, 503, x, y + 24, color=BLUE, width=1.4, arrow=True, dash=True)
    f.text(505, 470, '振り返る', 15, BLUE, anchor='middle')
    f.text(600, 540, '解釈の方向　後の出来事に照らして意味を改める', 18, BLUE, anchor='middle', weight=700)
    f.text(1130, 578, '順番に生きる。意味は順番どおりに決まらない', 15, INK, anchor='end')
    f.footer('青緑＝経験・生きること、青＝認識・知ること、琥珀＝現在')
    made.add(f.save('02-g-living-forward-understanding-backward.svg'))


def draw(made: set[str]) -> None:
    fig_a(made)
    fig_b(made)
    fig_c(made)
    fig_d(made)
    fig_e(made)
    fig_f(made)
    fig_g(made)
