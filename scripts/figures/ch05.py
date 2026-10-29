"""第5回「過去は終わったのに、なぜ書き換わるのか」の挿絵 7 枚。"""
from __future__ import annotations
import math

from draw_figures import Figure, person, BG, INK, MUTED, LINE, SOFT, BLUE, AMBER, TEAL, PLUM


def tag(f, x, y, w, h, s, color=BLUE, size=16):
    """小さな札。"""
    f.rect(x, y, w, h, fill='#ffffff', stroke=color, width=1.6, rx=8)
    f.text(x + w / 2, y + h / 2 + size * 0.36, s, size, color, anchor='middle', weight=700)


def ghost_person(f, x, y, color=BLUE, scale=1.0):
    """person() と同じ姿勢を破線の輪郭だけで描く。"""
    s = scale
    f.circ(x, y - 60 * s, 12 * s, color, fill=False, dash=True, width=1.6)
    f.body.append(f'<ellipse cx="{x:.1f}" cy="{y - 26 * s:.1f}" rx="{11 * s:.1f}" ry="{24 * s:.1f}" fill="none" stroke="{color}" stroke-width="1.6" stroke-dasharray="6 5"/>')
    for (x1, y1, x2, y2) in [(x, y - 4 * s, x - 22 * s, y + 34 * s), (x, y - 4 * s, x + 24 * s, y + 28 * s), (x + 4 * s, y - 38 * s, x - 22 * s, y - 20 * s), (x + 4 * s, y - 38 * s, x + 26 * s, y - 46 * s)]:
        f.line(x1, y1, x2, y2, color=color, width=1.6, dash=True)


def draw(made: set[str]) -> None:
    # ---- 図5-1 出来事は動かず、意味が動く --------------------------------------------
    f = Figure(5, '出来事は動かず、意味が動く', '過去の出来事と現在のあいだを往復する二本の矢印と、同じ出来事に付く二つの意味の札を見る。', 560, 'a')
    bx, by, bw, bh = 130, 250, 300, 110
    f.box(bx, by, bw, bh, '過去の出来事', 'ある人との出会い', PLUM)
    f.box(770, by, bw, bh, '現在', '人生を変えた相手', AMBER)
    f.line(bx + bw + 14, by + 32, 770 - 14, by + 32, color=TEAL, width=2.4, arrow=True)
    f.text(600, by + 18, '形づくる（因果）', 17, TEAL, anchor='middle', weight=700)
    f.line(770 - 14, by + bh - 28, bx + bw + 14, by + bh - 28, color=BLUE, width=2.4, arrow=True, dash=True)
    f.text(600, by + bh - 4, '意味づける（解釈）', 17, BLUE, anchor='middle', weight=700)
    # 同じ出来事に付く二つの札
    tag(f, 130, 400, 212, 42, '当時：数ある知人の一人')
    f.line(356, 421, 404, 421, color=BLUE, width=1.8, arrow=True, dash=True)
    tag(f, 418, 400, 130, 42, '十年後：転機')
    f.text(600, 508, '出来事は動かない。意味は変わる', 20, INK, anchor='middle', weight=700)
    made.add(f.save('05-a-event-and-meaning.svg'))

    # ---- 図5-2 後の作品が先の作品を読み替える ------------------------------------------
    f = Figure(5, '後の作品が先の作品を読み替える', '千年前の文章と現代の小説のあいだで往復する二本の矢印と、後続作品を先に読んだ読者の視線を見る。', 660, 'b')
    by, bh = 230, 110
    f.box(130, by, 300, bh, '『枕草子』', '先行作品', PLUM)
    f.box(770, by, 300, bh, '現代の小説', '後続作品', AMBER)
    f.line(444, by + 32, 756, by + 32, color=TEAL, width=2.4, arrow=True)
    f.text(600, by + 18, '影響（成立条件）', 17, TEAL, anchor='middle', weight=700)
    f.line(756, by + bh - 28, 444, by + bh - 28, color=BLUE, width=2.4, arrow=True, dash=True)
    f.text(600, by + bh - 4, '読み替え（新しい意味）', 17, BLUE, anchor='middle', weight=700)
    f.text(130, 376, '原文は変わらない。変わるのは解釈', 15, MUTED)
    # 読者：後続作品を先に読み、古典を後から開く
    person(f, 600, 560, BLUE, 0.95)
    f.text(600, 626, '読者', 18, BLUE, anchor='middle', weight=700)
    f.line(612, 488, 790, 356, color=BLUE, width=2, arrow=True)
    f.text(718, 440, '先に読む', 16, BLUE)
    f.line(588, 488, 420, 356, color=BLUE, width=2, arrow=True, dash=True)
    f.text(484, 440, '後から開く', 16, BLUE, anchor='end')
    made.add(f.save('05-b-later-work-rereads-earlier.svg'))

    # ---- 図5-3 先行テクストと後続テクストの往復 ------------------------------------------
    f = Figure(5, '先行テクストと後続テクストの往復', '一つのテクストから五つの関係が広がり、その一つである変換・模倣の関係で先行と後続が互いを更新する様子を見る。', 640, 'c')
    f.panel(50, 200, 550, 400)
    f.panel(640, 200, 510, 400)
    cx, cy, r = 325, 400, 165
    names = ['変換・模倣', 'ジャンル・形式', '批評・解説', '題名・序文', '引用・暗示']
    pts = []
    for i, name in enumerate(names):
        a = math.radians(72 * i)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a), name))
    for (x, y, _) in pts:
        f.line(cx, cy, x, y, color=MUTED, width=1.6)
    f.box(cx - 65, cy - 30, 130, 60, 'テクスト', '', BLUE, 21)
    for (x, y, name) in pts:
        main = name == '変換・模倣'
        f.rect(x - 80, y - 25, 160, 50, fill='#ffffff', stroke=BLUE, width=3.6 if main else 1.6, rx=10)
        f.text(x, y + 6, name, 17, BLUE, anchor='middle', weight=700)
    f.line(cx + r + 82, cy, 640, cy, color=BLUE, width=1.8, dash=True)
    # 右パネル：ハイポテクストとハイパーテクスト
    f.box(765, 240, 260, 90, '『オデュッセイア』', 'ハイポテクスト', PLUM)
    f.box(765, 470, 260, 90, '『ユリシーズ』', 'ハイパーテクスト', AMBER)
    f.line(865, 344, 865, 456, color=TEAL, width=2.4, arrow=True)
    f.text(848, 406, '成立させる', 17, TEAL, anchor='end', weight=700)
    f.line(925, 456, 925, 344, color=BLUE, width=2.4, arrow=True, dash=True)
    f.text(942, 406, '読み方が変わる', 17, BLUE, weight=700)
    made.add(f.save('05-c-genette-five-relations.svg'))

    # ---- 図5-4 書く浜崎正が、書かれる浜崎正を生む ----------------------------------------
    f = Figure(5, '書く浜崎正が、書かれる浜崎正を生む', '上は出来事から記述へ進む一方向の列、下は書く現在の浜崎正と小説の中に立つ二十歳の浜崎正が互いを成立させる輪を見る。', 790, 'd')
    f.panel(50, 200, 1100, 140, 'ふつうの順序')
    for x, name, col in [(240, '出来事', TEAL), (500, '記憶', PLUM), (760, '記述', BLUE)]:
        f.box(x, 260, 200, 60, name, '', col, 21)
    f.line(452, 290, 488, 290, color=MUTED, width=2.2, arrow=True)
    f.line(712, 290, 748, 290, color=MUTED, width=2.2, arrow=True)
    f.panel(50, 370, 1100, 390, '『ストロボライト』')
    f.text(1120, 404, '成立の向きが反転', 17, AMBER, anchor='end', weight=700)
    # 小説の中に立つ二十歳の浜崎正
    f.rect(130, 440, 400, 260, fill='#ffffff', stroke=BLUE, width=2, rx=4)
    f.text(150, 470, '小説の中', 17, BLUE, weight=700)
    person(f, 330, 600, PLUM, 1.0)
    f.text(330, 514, '書かれる浜崎正（二十歳）', 17, PLUM, anchor='middle', weight=700)
    # 現在の浜崎正（ペンを持つ）
    person(f, 900, 600, AMBER, 1.0)
    f.line(926, 554, 946, 532, color=INK, width=3)
    f.text(900, 514, '書く浜崎正（現在）', 17, AMBER, anchor='middle', weight=700)
    f.line(862, 560, 372, 560, color=AMBER, width=2.4, arrow=True)
    f.text(617, 546, '書くことで立ち上がる', 17, AMBER, anchor='middle', weight=700)
    f.path('M 330 646 L 330 724 L 900 724 L 900 652', color=PLUM, width=2.4, arrow=True)
    f.text(615, 716, '現在の自分を形成した', 17, PLUM, anchor='middle', weight=700)
    made.add(f.save('05-d-writing-and-written-hamasaki.svg'))

    # ---- 図5-5 物語が過去をつくる三つの水準 -------------------------------------------
    f = Figure(5, '物語が過去をつくる三つの水準', '事実・意味・存在の三段の帯と、意味の段から存在の段へ降りる矢印、現実とフィクションの内部を分ける仕切りを見る。', 610, 'e')
    x0, w, h = 290, 670, 90
    rows = [(220, TEAL, '第一　歴史的事実の水準', '起きたかどうか／解釈で変えられない'),
            (350, BLUE, '第二　意味の水準', '人生の中での役割／後から変わりうる'),
            (480, PLUM, '第三　物語内部の存在の水準', '記述によって成立する')]
    for y, col, title, sub in rows:
        f.rect(x0, y, w, h, fill=col, stroke='none', width=0, rx=12, opacity=0.12)
        f.rect(x0, y, w, h, fill='none', stroke=col, width=2, rx=12)
        f.text(x0 + 22, y + 38, title, 20, col, weight=700)
        f.text(x0 + 22, y + 68, sub, 16, INK)
    # 意味の段から存在の段へ
    f.line(250, 405, 250, 520, color=PLUM, width=2.4, arrow=True)
    f.lines(60, 455, ['意味の変化から', '存在の生成へ'], 16, PLUM, gap=24)
    tag(f, 60, 530, 170, 38, '『ストロボライト』', AMBER)
    # 現実とフィクションの内部
    f.line(985, 214, 985, 576, color=MUTED, width=1.6)
    f.text(1002, 338, '現実', 19, INK, weight=700)
    f.lines(1002, 520, ['フィクションの', '内部'], 17, INK, gap=24, weight=700)
    made.add(f.save('05-e-three-levels-of-narrative.svg'))

    # ---- 図5-6 書かれる自分が書く自分に追いつく ---------------------------------------
    f = Figure(5, '書かれる自分が書く自分に追いつく', '左は書く現在と書かれる過去が離れていて第三者が外から見ている図、右は両者が一点に収束し第三者の輪郭だけが残る図を見る。', 750, 'f')
    f.panel(50, 200, 540, 520, '距離がある間')
    f.panel(610, 200, 540, 520, '収束')
    # 左：距離がある間
    f.line(90, 600, 560, 600, color=MUTED, width=2, arrow=True)
    for x in (230, 300, 370):
        f.line(x, 594, x, 606, color=MUTED, width=1.5)
    f.text(300, 630, '二十一歳、二十二歳…', 15, MUTED, anchor='middle')
    person(f, 170, 520, PLUM, 1.0)
    f.text(170, 582, '書かれる浜崎正（二十歳）', 16, PLUM, anchor='middle', weight=700)
    person(f, 500, 520, AMBER, 1.0)
    f.text(500, 582, '書く浜崎正（現在）', 16, AMBER, anchor='middle', weight=700)
    f.path('M 170 612 C 170 690 500 690 500 612', color=PLUM, width=2.4, arrow=True)
    f.text(335, 700, '現在を形成', 16, PLUM, anchor='middle', weight=700)
    f.path('M 500 442 C 500 390 170 390 170 442', color=BLUE, width=2.4, arrow=True, dash=True)
    f.text(335, 390, '書く', 16, BLUE, anchor='middle', weight=700)
    person(f, 335, 330, BLUE, 0.9)
    f.text(372, 322, '美和子（外から見る）', 16, BLUE, weight=700)
    f.line(322, 350, 180, 450, color=BLUE, width=1.4, dots=True)
    f.line(348, 350, 490, 450, color=BLUE, width=1.4, dots=True)
    # 右：収束
    f.line(650, 600, 1120, 600, color=MUTED, width=2, arrow=True)
    f.line(660, 380, 1042, 456, color=MUTED, width=1.4)
    f.line(660, 540, 1042, 468, color=MUTED, width=1.4)
    person(f, 1066, 520, PLUM, 1.0)
    person(f, 1054, 520, AMBER, 1.0)
    f.text(1060, 420, '消失点', 17, INK, anchor='middle', weight=700)
    cx, cy, r = 1060, 500, 64
    a0, a1 = math.radians(-70), math.radians(-115)
    f.path(f'M {cx + r * math.cos(a0):.1f} {cy + r * math.sin(a0):.1f} A {r} {r} 0 1 1 {cx + r * math.cos(a1):.1f} {cy + r * math.sin(a1):.1f}', color=AMBER, width=2, arrow=True, dash=True)
    f.text(1060, 586, '書く行為も書かれる', 16, AMBER, anchor='middle', weight=700)
    ghost_person(f, 895, 330, BLUE, 0.9)
    f.text(932, 322, '位置が意味を失う', 16, BLUE, weight=700)
    made.add(f.save('05-f-written-self-catches-up.svg'))

    # ---- 図5-7 語る現在と形づくられる過去 ---------------------------------------------
    f = Figure(5, '語る現在と形づくられる過去', '記憶・物語・自己理解・新しい経験を結ぶ輪と、輪の外の動かない出来事の箱、中心に立つ語る現在の自分を見る。', 790, 'g')
    cx, cy, r = 790, 480, 200
    names = [('記憶', '過去の出来事の記録', PLUM), ('物語', '現在から語る', PLUM), ('自己理解', '自分が何者であるか', BLUE), ('新しい経験', '過去の意味を変える', TEAL)]
    start = math.pi  # 記憶を左に置き、時計回りに進む
    bw, bh = 200, 78
    centers = []
    for i in range(4):
        a = start + 2 * math.pi * i / 4
        centers.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    def outside(a, node):
        """円周上の角 a の点が、node の箱（余白 14px）の外にあるか。箱は横長なので上下の箱ほど外れる角が大きい。"""
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        return abs(x - node[0]) > bw / 2 + 14 or abs(y - node[1]) > bh / 2 + 14
    for i in range(4):
        a0 = start + 2 * math.pi * i / 4
        a1 = start + 2 * math.pi * (i + 1) / 4
        t0 = 0.0
        while not outside(a0 + t0, centers[i]):
            t0 += math.radians(1)
        t1 = 0.0
        while not outside(a1 - t1, centers[(i + 1) % 4]):
            t1 += math.radians(1)
        p0 = (cx + r * math.cos(a0 + t0), cy + r * math.sin(a0 + t0))
        p1 = (cx + r * math.cos(a1 - t1), cy + r * math.sin(a1 - t1))
        f.path(f'M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}', color=MUTED, width=2.2, arrow=True)
    for (x, y), (title, sub, col) in zip(centers, names):
        f.box(x - bw / 2, y - bh / 2, bw, bh, title, sub, col, 22)
    # 弧のラベル
    f.text(cx - 150, cy - 158, '語る', 17, PLUM, anchor='end', weight=700)
    f.text(cx + 150, cy - 158, '自己を形成する', 17, BLUE, weight=700)
    f.text(cx + 150, cy + 170, '生きる', 17, TEAL, weight=700)
    f.text(cx - 150, cy + 170, '語り直す', 17, PLUM, anchor='end', weight=700)
    # 輪の中心：語る現在の自分
    person(f, cx, cy + 20, AMBER, 0.9)
    f.text(cx, cy + 74, '語る現在の自分', 17, AMBER, anchor='middle', weight=700)
    # 輪の外の固定点
    ex, ey, ew, eh = 70, cy - 55, 240, 110
    f.box(ex, ey, ew, eh, '過去の出来事', '動かない（事実）', INK)
    f.line(ex + ew + 14, cy - 22, centers[0][0] - bw / 2 - 14, cy - 22, color=TEAL, width=2.4, arrow=True)
    f.text((ex + ew + centers[0][0] - bw / 2) / 2, cy - 34, '形づくる', 16, TEAL, anchor='middle', weight=700)
    f.line(centers[0][0] - bw / 2 - 14, cy + 22, ex + ew + 14, cy + 22, color=BLUE, width=2.4, arrow=True, dash=True)
    f.text((ex + ew + centers[0][0] - bw / 2) / 2, cy + 44, '意味づける', 16, BLUE, anchor='middle', weight=700)
    f.footer('事実は固定され、意味は輪の中で更新され続ける')
    made.add(f.save('05-g-narrating-present-shaping-past.svg'))
