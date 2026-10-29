"""第6回「虚構だと知れば、その世界から自由になれるのか」の図 6-1〜6-7。"""
from __future__ import annotations

from draw_figures import Figure, person, BG, INK, MUTED, LINE, SOFT, BLUE, AMBER, TEAL, PLUM


def _double_arrow(f, x0, x1, y, color, width=2):
    m = (x0 + x1) / 2
    f.line(m, y, x0, y, color=color, width=width, arrow=True)
    f.line(m, y, x1, y, color=color, width=width, arrow=True)


def _vertical_text(f, x, y0, s, size=17, color=INK, gap=None):
    gap = gap or size * 1.25
    for i, ch in enumerate(s):
        f.text(x, y0 + i * gap, ch, size, color, anchor='middle')


def _cycle(f, x, y0, labels, color=PLUM, w=100, h=36, step=70, size=15):
    """箱を縦に並べ、上から下へ矢印でつなぎ、最後の箱から右側を回って最初の箱へ戻る輪。"""
    ys = [y0 + i * step for i in range(len(labels))]
    for yy, lab in zip(ys, labels):
        f.box(x, yy, w, h, lab, '', color, size)
    for a, b in zip(ys, ys[1:]):
        f.line(x + w / 2, a + h, x + w / 2, b, color=color, width=2, arrow=True)
    right = x + w + 16
    f.path(f'M {x + w:.1f} {ys[-1] + h / 2:.1f} L {right:.1f} {ys[-1] + h / 2:.1f} L {right:.1f} {ys[0] + h / 2:.1f} L {x + w + 6:.1f} {ys[0] + h / 2:.1f}', color=color, width=2, arrow=True)
    return ys


def draw(made: set[str]) -> None:
    # ---------------------------------------------------------------- 6-1
    f = Figure(6, '存在の三つの水準', 'りんご、数、虚数、探偵が、存在のどの水準に置かれるかを見る。', 680, 'a')
    x0, x1 = 150, 1050
    bands = [(200, 110, TEAL, '物理的な存在'), (350, 120, BLUE, '抽象的・文化的な存在'), (510, 120, PLUM, '虚構内部の存在')]
    f.line(110, 200, 110, 630, color=MUTED, width=2)
    for (y, h, col, lab), num in zip(bands, ['第一', '第二', '第三']):
        f.rect(x0, y, x1 - x0, h, fill=col, stroke='none', width=0, rx=14, opacity=0.09)
        f.rect(x0, y, x1 - x0, h, fill='none', stroke=col, width=2, rx=14)
        f.text(x0 + 20, y + 30, lab, 19, col, weight=700)
        f.line(104, y + h / 2, 116, y + h / 2, color=MUTED, width=2)
        f.text(76, y + h / 2 + 6, num, 18, MUTED, anchor='middle', weight=700)
    # 第一：りんご
    for i in range(3):
        f.circ(200 + i * 40, 272, 14, TEAL)
    f.text(310, 279, 'りんご×3', 17, INK)
    f.text(700, 279, '手で取れる。かじれば減る', 15, MUTED)
    # 第一→第二
    f.line(600, 312, 600, 348, color=MUTED, width=2, arrow=True)
    f.text(614, 336, '数の3はりんごから取り出せない', 15, MUTED)
    # 第二：数の3、虚数 i、実数
    f.box(190, 395, 130, 52, '数の3', '', BLUE, 18)
    f.box(430, 395, 130, 52, '虚数 i', '', BLUE, 18)
    f.box(680, 395, 130, 52, '実数', '', BLUE, 18)
    f.line(562, 421, 678, 421, color=BLUE, width=2, dash=True)
    f.text(620, 466, '構造が違う', 15, BLUE, anchor='middle')
    f.text(860, 427, 'どちらも物体ではない', 15, MUTED)
    # 第三：ホームズ
    f.rect(190, 552, 150, 68, fill='#ffffff', stroke=PLUM, width=2, rx=12)
    f.rect(196, 558, 138, 56, fill='none', stroke=PLUM, width=1.2, rx=9)
    person(f, 258, 598, INK, 0.42)
    f.text(362, 582, 'ホームズ', 18, INK)
    f.text(362, 607, '職業も住所も人間関係もある', 15, MUTED)
    # 右端の縦書き風の注記（第二・第三の帯に沿わせる）
    _vertical_text(f, 1105, 388, '第二も第三も物体ではない', 17, MUTED, gap=21)
    made.add(f.save('06-a-three-levels-of-being.svg'))

    # ---------------------------------------------------------------- 6-2
    f = Figure(6, '出口も画面の内側にある', '物語の世界から実写の風景までの移動が、どの枠の中で起きているかを見る。', 680, 'b')
    f.rect(80, 210, 820, 430, fill='none', stroke=PLUM, width=4, rx=18)
    f.text(100, 240, '映画として提示された映像', 19, PLUM, weight=700)
    f.rect(110, 255, 760, 355, fill=AMBER, stroke=AMBER, width=2, rx=14, opacity=0.06)
    f.rect(110, 255, 760, 355, fill='none', stroke=AMBER, width=2, rx=14)
    f.text(126, 283, '実写の風景', 18, AMBER, weight=700)
    f.rect(140, 298, 560, 280, fill=BG, stroke=PLUM, width=2, rx=14, dash=True)
    f.text(156, 326, '制作を思わせる空間', 18, PLUM, weight=700)
    for i in range(4):
        f.rect(160 + i * 24, 536, 18, 18, fill='none', stroke=PLUM, width=1.5, rx=3)
    f.text(262, 551, 'セット・絵コンテ', 15, PLUM)
    f.rect(170, 342, 300, 180, fill='#ffffff', stroke=PLUM, width=2, rx=12)
    f.text(186, 370, '物語の世界', 18, PLUM, weight=700)
    person(f, 300, 460, INK, 0.75, lean=0.4)
    f.text(300, 512, 'シンジ', 16, INK, anchor='middle')
    f.line(345, 440, 850, 440, color=TEAL, width=2.5, arrow=True)
    f.text(585, 468, '物語を終わらせる方向へ', 15, TEAL, anchor='middle')
    f.text(780, 468, 'アニメーション→実写', 14, AMBER, anchor='middle')
    f.lines(930, 240, ['画面の外には', '出ていない', '', '実写もまた', '提示された映像'], 17, MUTED, gap=26)
    made.add(f.save('06-b-exit-inside-the-screen.svg'))

    # ---------------------------------------------------------------- 6-3
    f = Figure(6, '世界が増えても、自由は増えない', '世界の数が増えたとき、関係の輪が変わるかどうかを見る。', 690, 'c')
    f.panel(50, 200, 430, 455, 'ふだんの考え')
    f.text(345, 268, '可能性が開く', 16, TEAL, anchor='middle')
    f.circ(92, 430, 7, INK)
    for i, lab in enumerate(['出会った世界', '出会わなかった世界', '別れた世界', '別れなかった世界']):
        y = 290 + i * 90
        f.line(100, 430, 236, y + 22, color=TEAL, width=2, arrow=True)
        f.box(240, y, 210, 44, lab, '', TEAL, 16)
    f.panel(510, 200, 640, 455, 'わかめとなみ')
    f.text(830, 262, '出来事は世界ごとに異なる', 15, MUTED, anchor='middle')
    for i, lab in enumerate(['世界1', '世界2', '世界3', '世界…']):
        bx = 530 + i * 150
        f.rect(bx, 272, 142, 335, fill=PLUM, stroke='none', width=0, rx=12, opacity=0.05 + 0.04 * i)
        f.text(bx + 71, 298, lab, 16, PLUM, anchor='middle', weight=700)
        _cycle(f, bx + 12, 318, ['出会う', '愛し合う', '傷つけ合う', '殺し合う'])
    f.line(520, 585, 1140, 585, color=INK, width=1.8, dash=True)
    f.text(830, 636, '関係の構造は同じ', 16, INK, anchor='middle', weight=700)
    made.add(f.save('06-c-worlds-multiply-structure-repeats.svg'))

    # ---------------------------------------------------------------- 6-4
    f = Figure(6, '運命を知ることと、作者を知ること', '二組の登場人物が知る内容が、物語の内側に向くか、外側の作者に向くかを見る。', 700, 'd')
    f.panel(50, 200, 530, 455, 'エレン')
    f.rect(80, 330, 470, 300, fill='#ffffff', stroke=PLUM, width=2, rx=14)
    f.text(96, 358, '物語', 18, PLUM, weight=700)
    person(f, 170, 470, INK, 0.9, lean=0.2)
    f.rect(118, 508, 120, 10, fill=TEAL, stroke='none', width=0, rx=5)
    f.text(178, 540, '行為は続く', 15, TEAL, anchor='middle')
    f.line(232, 450, 372, 450, color=MUTED, width=2, arrow=True)
    f.text(300, 474, '時間', 14, MUTED, anchor='middle')
    f.box(378, 420, 150, 56, '未来の出来事', '', INK, 18)
    f.path('M 198 402 Q 300 352 440 416', color=BLUE, width=2.4, arrow=True)
    f.text(300, 362, '知る', 17, BLUE, anchor='middle', weight=700)
    f.text(315, 612, '枠の中に留まる', 15, MUTED, anchor='middle')
    f.panel(620, 200, 530, 455, 'わかめとなみ')
    f.box(790, 252, 190, 48, '作者・シナリオ', '', PLUM, 18)
    f.rect(650, 330, 470, 300, fill='#ffffff', stroke=PLUM, width=2, rx=14)
    f.text(666, 358, '物語', 18, PLUM, weight=700)
    person(f, 820, 470, INK, 0.9, lean=0.1)
    person(f, 900, 470, INK, 0.9, lean=-0.1)
    f.rect(768, 508, 180, 10, fill=TEAL, stroke='none', width=0, rx=5)
    f.text(858, 540, '行為は続く', 15, TEAL, anchor='middle')
    f.line(860, 302, 860, 404, color=PLUM, width=2.4, arrow=True)
    f.text(846, 358, '描く', 17, PLUM, anchor='end', weight=700)
    f.line(930, 408, 930, 306, color=BLUE, width=2.4, arrow=True, dash=True)
    f.text(944, 358, '知る', 17, BLUE, weight=700)
    f.text(885, 612, '枠の中に留まる', 15, MUTED, anchor='middle')
    f.footer('知識の向く先が違う。エレンは物語の内側の未来へ、わかめとなみは物語の外側の作者へ向く。')
    made.add(f.save('06-d-knowing-fate-knowing-author.svg'))

    # ---------------------------------------------------------------- 6-5
    f = Figure(6, '虚構の苦痛は消えない', '描かれた苦痛が物語の内側と外側でそれぞれ何を動かすかを見る。', 680, 'e')
    # 右側：現実のもの
    f.rect(820, 220, 330, 410, fill=TEAL, stroke='none', width=0, rx=16, opacity=0.07)
    f.text(985, 252, '現実のもの', 18, TEAL, anchor='middle', weight=700)
    # 中央：物語の内部
    f.rect(330, 220, 460, 380, fill='#ffffff', stroke=PLUM, width=2, rx=14)
    f.text(345, 250, '物語の内部', 18, PLUM, weight=700)
    person(f, 430, 430, INK, 1.0)
    f.circ(430, 404, 10, AMBER)
    f.circ(408, 485, 6, AMBER)
    f.text(420, 491, '苦痛', 16, AMBER, weight=700)
    f.box(560, 330, 220, 50, '行動・関係', '', PLUM, 16)
    f.box(560, 470, 220, 50, '別の人物を傷つける・救う', '', PLUM, 16)
    f.line(442, 400, 556, 358, color=PLUM, width=2.2, arrow=True)
    f.line(442, 408, 556, 492, color=PLUM, width=2.2, arrow=True)
    f.text(560, 570, '登場人物の行動や関係を動かす', 15, MUTED, anchor='middle')
    # 左側：現実の人間
    person(f, 150, 430, TEAL, 1.0)
    f.circ(150, 404, 10, AMBER)
    f.text(150, 491, '現実の人間', 16, TEAL, anchor='middle', weight=700)
    f.text(150, 516, '身体の苦痛', 15, AMBER, anchor='middle')
    f.line(166, 404, 418, 404, color=MUTED, width=1.8, dash=True)
    f.text(292, 386, '同じ地位ではない', 15, MUTED, anchor='middle')
    # 読者
    person(f, 900, 400, TEAL, 0.9)
    f.text(924, 352, '読者', 16, TEAL, weight=700)
    f.line(792, 384, 868, 384, color=BLUE, width=2.2, arrow=True)
    f.text(830, 366, '読み取る', 15, BLUE, anchor='middle')
    f.box(860, 486, 180, 48, '感情・判断', '', TEAL, 16)
    f.line(906, 436, 930, 482, color=TEAL, width=2.2, arrow=True)
    f.box(860, 562, 220, 48, '作品が社会に与える影響', '', BLUE, 16)
    f.line(792, 586, 856, 586, color=BLUE, width=2.2, arrow=True)
    made.add(f.save('06-e-fictional-pain-persists.svg'))

    # ---------------------------------------------------------------- 6-6
    f = Figure(6, '虚構の薬と毒', '読者と虚構の距離があるときとないときで、同じ虚構が何をもたらすかを見る。', 660, 'f')

    def fiction_frame(x):
        f.rect(x, 270, 200, 250, fill='#ffffff', stroke=PLUM, width=2, rx=14)
        f.text(x + 15, 298, '虚構', 18, PLUM, weight=700)
        person(f, x + 60, 430, INK, 0.7, lean=0.1)
        person(f, x + 120, 430, INK, 0.7, lean=-0.1)
        f.circ(x + 90, 400, 8, AMBER)
        f.text(x + 90, 375, '苦痛', 14, AMBER, anchor='middle', weight=700)
        f.text(x + 100, 500, '二人には自分の世界の出来事', 14, MUTED, anchor='middle')

    f.panel(50, 200, 530, 430, '薬：距離がある')
    fiction_frame(80)
    person(f, 470, 380, TEAL, 0.85)
    f.text(492, 336, '読者', 16, TEAL, weight=700)
    f.text(470, 450, '読者には物語の中の出来事', 14, MUTED, anchor='middle')
    _double_arrow(f, 296, 430, 330, AMBER, 2.2)
    f.text(363, 316, '距離', 17, AMBER, anchor='middle', weight=700)
    f.box(380, 476, 190, 50, '現実の構造が見える', '', BLUE, 16)
    f.line(282, 501, 376, 501, color=BLUE, width=2.2, arrow=True)

    f.panel(620, 200, 530, 430, '毒：距離を忘れる')
    fiction_frame(650)
    person(f, 885, 380, TEAL, 0.85)
    f.text(907, 336, '読者', 16, TEAL, weight=700)
    f.text(866, 450, '読者には物語の中の出来事', 14, MUTED)
    f.box(900, 476, 200, 50, '苦痛を物語として消費', '', BLUE, 16)
    f.line(852, 501, 896, 501, color=BLUE, width=2.2, arrow=True)
    f.box(655, 545, 190, 50, '不条理・偶然が隠れる', '', PLUM, 15, dash=True)
    made.add(f.save('06-f-fiction-as-remedy-and-poison.svg'))

    # ---------------------------------------------------------------- 6-7
    f = Figure(6, '知ることもまた、物語の内側にある', '登場人物が自分の虚構性を知る認識が、物語の枠のどちら側に置かれるかを見る。', 760, 'g')
    f.box(540, 200, 120, 48, '作者', '', PLUM, 18)
    f.line(600, 250, 600, 296, color=PLUM, width=2.4, arrow=True)
    f.text(615, 280, '描く', 17, PLUM, weight=700)
    f.rect(200, 300, 800, 275, fill='#ffffff', stroke=PLUM, width=2, rx=14)
    f.text(216, 328, '物語', 18, PLUM, weight=700)
    f.rect(466, 316, 268, 78, fill='none', stroke=PLUM, width=1.5, rx=14, dash=True)
    f.box(480, 330, 240, 50, '自分たちは描かれた存在だ', '', BLUE, 17)
    f.text(750, 360, 'この認識も描かれる', 15, PLUM)
    person(f, 560, 510, INK, 0.9, lean=0.1)
    person(f, 640, 510, INK, 0.9, lean=-0.1)
    f.text(600, 565, 'わかめとなみ', 16, INK, anchor='middle')
    f.line(600, 448, 600, 400, color=BLUE, width=2.4, arrow=True)
    f.text(614, 430, '知る', 17, BLUE, weight=700)
    f.line(690, 530, 975, 530, color=TEAL, width=2.4, arrow=True)
    f.text(832, 518, '生き続ける', 16, TEAL, anchor='middle', weight=700)
    f.rect(200, 605, 800, 44, fill=BLUE, stroke='none', width=0, rx=10, opacity=0.12)
    f.text(600, 634, '知ること：認識を変える', 18, BLUE, anchor='middle', weight=700)
    f.text(600, 683, '≠', 28, INK, anchor='middle', weight=700)
    f.rect(200, 695, 800, 44, fill=TEAL, stroke='none', width=0, rx=10, opacity=0.12)
    f.text(600, 724, '生きること：行為は続く', 18, TEAL, anchor='middle', weight=700)
    made.add(f.save('06-g-knowing-inside-the-story.svg'))
