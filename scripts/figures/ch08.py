"""第8回の挿絵（図8-1〜図8-5）。"""
from draw_figures import Figure, BG, INK, MUTED, LINE, SOFT, BLUE, AMBER, TEAL, PLUM

N = 8


def fig_a(made: set[str]) -> None:
    f = Figure(N, '一つの出来事、別々の意味', '同じ出来事が二人にとって別の順序に置かれることと、現在の書く行為が過去を物語として生むことを見る。', 600, 'a')
    # 左パネル：他者の時間
    f.panel(50, 200, 530, 360, '他者の時間')
    f.text(100, 283, 'エマノン', 17, TEAL, weight=700)
    f.line(100, 300, 520, 300, color=TEAL, width=3, arrow=True)
    f.text(100, 433, 'ヒカリ', 17, TEAL, weight=700)
    f.line(100, 450, 520, 450, color=LINE, width=3)
    # 同じ出来事をつなぐ琥珀の帯
    f.rect(300, 272, 30, 206, fill=AMBER, stroke='none', width=0, rx=6, opacity=0.2)
    f.text(315, 262, '同じ出来事', 16, AMBER, anchor='middle', weight=700)
    f.text(340, 291, '初対面', 16, INK)
    f.text(340, 478, '再会', 16, INK)
    # ヒカリが訪れる順序（時間順とは別）
    pts = {1: 450, 2: 180, 3: 315}
    for k, x in pts.items():
        f.circ(x, 450, 7, TEAL)
        f.text(x, 478, str(k), 15, MUTED, anchor='middle')
    f.path('M 440 442 Q 315 370 190 442', color=TEAL, width=2, arrow=True, dash=True)
    f.path('M 195 462 Q 247 510 300 462', color=TEAL, width=2, arrow=True, dash=True)
    f.text(315, 540, '時間順とは別の順序で訪れる（1→2→3）', 14, MUTED, anchor='middle')
    # 右パネル：過去の意味
    f.panel(620, 200, 530, 360, '過去の意味')
    f.rect(770, 262, 230, 112, fill='none', stroke=PLUM, width=2, rx=14)
    f.text(786, 286, '小説', 16, PLUM, weight=700)
    f.box(790, 298, 190, 62, '二十歳の浜崎正', '', PLUM, 19)
    f.box(770, 470, 230, 62, '現在の浜崎正（書く）', '', AMBER, 19)
    f.line(860, 378, 860, 464, color=PLUM, width=2, arrow=True)
    f.text(846, 427, '過去が書き手をつくる', 15, INK, anchor='end')
    f.line(910, 466, 910, 380, color=AMBER, width=2, arrow=True, dash=True)
    f.text(924, 427, '現在が過去を物語にする', 15, INK)
    made.add(f.save('08-a-one-event-two-meanings.svg'))


def fig_b(made: set[str]) -> None:
    f = Figure(N, '完成が残すものと終わらせるもの', '百夜の積み重ねが完成の線で切れ、作品は右へ残り、描く行為はそこで止まることを見る。', 580, 'b')
    f.text(90, 282, '描いている（未完了相）', 16, TEAL, weight=700)
    rows = [('百夜目', 578, 1.0), ('…', 430, 0.5), ('二夜目', 310, 1.0), ('一夜目', 200, 1.0)]
    for i, (lab, x1, op) in enumerate(rows):
        y = 300 + i * 48
        f.rect(90, y, x1 - 90, 36, fill=TEAL, stroke='none', width=0, rx=6, opacity=0.28 * op)
        f.text(102, y + 24, lab, 17, INK)
    f.text(325, 514, '持続：前の夜を含む', 16, MUTED, anchor='middle')
    # 完成の線
    f.line(580, 250, 580, 530, color=AMBER, width=3)
    f.text(580, 236, '描き終える', 18, AMBER, anchor='middle', weight=700)
    # 上段：残る
    f.line(586, 318, 652, 318, color=MUTED, width=2, arrow=True)
    f.text(760, 266, '残る', 16, BLUE, anchor='middle', weight=700)
    f.box(660, 282, 200, 70, '完成した絵', '', BLUE, 21)
    f.line(866, 304, 990, 304, color=BLUE, width=2, arrow=True)
    f.line(866, 332, 990, 332, color=BLUE, width=2, arrow=True)
    f.text(1000, 309, '鑑賞者が見る', 16, INK)
    f.text(1000, 337, '次の制作へ', 16, INK)
    # 下段：戻らない
    f.path('M 586 336 Q 600 462 648 462', color=MUTED, width=2, arrow=True, dash=True)
    f.rect(660, 428, 240, 68, fill='none', stroke=LINE, width=2, rx=10, dash=True)
    f.text(780, 468, '百夜は戻らない', 17, MUTED, anchor='middle')
    made.add(f.save('08-b-what-completion-ends.svg'))


def fig_c(made: set[str]) -> None:
    f = Figure(N, '七つの問いの見取り図', '七つの主題が同じ境界線の上に並び、最終回の問いがその線を一つにまとめることを見る。', 600, 'c')
    x0, x1, top, mid, bot = 70, 1130, 230, 375, 520
    f.rect(x0, top, x1 - x0, mid - top, fill=BLUE, stroke='none', width=0, rx=0, opacity=0.08)
    f.rect(x0, mid, x1 - x0, bot - mid, fill=TEAL, stroke='none', width=0, rx=0, opacity=0.08)
    f.line(x0, mid, x1, mid, color=MUTED, width=2)
    f.text(90, 264, '知ること（記述）', 18, BLUE, weight=700)
    f.text(90, 504, '生きること（経験）', 18, TEAL, weight=700)
    words = ['時間', '因果', '自由', '記憶', '物語', '虚構', '持続']
    r = 40
    xs = [150 + 115 * i for i in range(7)]
    for i, (x, w) in enumerate(zip(xs, words)):
        f.circ(x, mid, r, '#ffffff')
        f.circ(x, mid, r, MUTED, fill=False, width=2)
        f.line(x - r, mid, x - 24, mid, color=INK, width=1.6, dash=True)
        f.line(x + 24, mid, x + r, mid, color=INK, width=1.6, dash=True)
        f.text(x, mid + 7, w, 19, INK, anchor='middle', weight=700)
        f.text(x, mid + r + 22, f'第{i + 1}回', 14, MUTED, anchor='middle')
        if i < 6:
            f.line(x + r, mid, xs[i + 1] - r, mid, color=INK, width=2)
    ax, ar = 1000, 52
    f.line(xs[-1] + r, mid, ax - ar - 4, mid, color=INK, width=2, arrow=True)
    f.circ(ax, mid, ar, AMBER, opacity=0.15)
    f.circ(ax, mid, ar, AMBER, fill=False, width=2.5)
    f.text(ax, mid + 7, '生き続ける', 17, AMBER, anchor='middle', weight=700)
    f.text(ax, mid + ar + 22, '第8回', 14, MUTED, anchor='middle')
    f.text(600, 566, '知ることと生きることは同じか', 22, INK, anchor='middle', weight=700)
    made.add(f.save('08-c-map-of-seven-questions.svg'))


def fig_d(made: set[str]) -> None:
    f = Figure(N, '確定した全体と未完了の現在', '同じ人生を、上では確定した全体として、下では現在から先が未完了のものとして見る。', 590, 'd')
    L, R = 120, 1080
    # 上段：全体として捉える観点
    f.text(600, 232, '［全体として捉える観点］', 16, BLUE, anchor='middle')
    f.rect(L, 258, R - L, 32, fill=BLUE, stroke=BLUE, width=1.5, rx=6, opacity=0.22)
    f.text(600, 281, '人生の全体（確定）', 17, BLUE, anchor='middle', weight=700)
    f.text(L, 316, '始まり', 16, INK)
    f.text(R, 316, '終わり', 16, INK, anchor='end')
    # 別の水準
    f.line(600, 366, 600, 336, color=MUTED, width=1.8, arrow=True, dash=True)
    f.line(600, 366, 600, 396, color=MUTED, width=1.8, arrow=True, dash=True)
    f.text(616, 372, '別の水準', 16, MUTED)
    # 下段：現在進行形で経験する観点
    now = 440
    f.line(L, 460, R, 460, color=LINE, width=2)
    f.rect(L, 446, now - 4 - L, 28, fill=TEAL, stroke='none', width=0, rx=6, opacity=0.4)
    f.text((L + now) / 2, 465, '経験済み', 14, INK, anchor='middle')
    f.line(now, 416, now, 506, color=AMBER, width=3)
    f.text(now, 408, '現在', 18, AMBER, anchor='middle', weight=700)
    items = [('まだ出会って', 'いない人'), ('まだ交わして', 'いない言葉'), ('まだ描き終えて', 'いない作品'), ('まだ経験して', 'いない喪失')]
    bw, bh, gap = 140, 64, 12
    bx = now + 28
    for i, (a, b) in enumerate(items):
        x = bx + i * (bw + gap)
        f.rect(x, 460 - bh / 2, bw, bh, fill=BG, stroke=TEAL, width=2, rx=10, dash=True)
        f.text(x + bw / 2, 456, a, 15, INK, anchor='middle')
        f.text(x + bw / 2, 476, b, 15, INK, anchor='middle')
    f.text(600, 548, '［現在進行形で経験する観点］', 16, TEAL, anchor='middle')
    made.add(f.save('08-d-fixed-whole-unfinished-present.svg'))


def fig_e(made: set[str]) -> None:
    f = Figure(N, '知っていること、それでも生きること', '五つの人物について、知っていることの隣に、それでも省略できない行為を並べて見る。', 680, 'e')
    lx, lw, rx, rw = 215, 360, 680, 450
    f.rect(lx, 212, lw, 44, fill=BLUE, stroke='none', width=0, rx=8, opacity=0.16)
    f.text(lx + lw / 2, 241, '知っていること', 19, BLUE, anchor='middle', weight=700)
    f.rect(rx, 212, rw, 44, fill=TEAL, stroke='none', width=0, rx=8, opacity=0.16)
    f.text(rx + rw / 2, 241, 'それでも省略できないこと', 19, TEAL, anchor='middle', weight=700)
    rows = [('ルイーズ', '娘を失う日', '娘を抱き、共に生きる'), ('エレン', '既知の未来', '自分の欲望で実現する'), ('ヒカリ', '未来のエマノン', 'いまの出会いを経験する'), ('わかめとなみ', '自分たちは虚構', '物語の中で行為し続ける'), ('画家', '描き終えた絵', '百夜を描き続ける')]
    for i, (who, a, b) in enumerate(rows):
        y = 276 + i * 62
        f.text(70, y + 33, who, 14, MUTED)
        f.rect(lx, y, lw, 54, fill='#ffffff', stroke=LINE, width=1.5, rx=10)
        f.text(lx + lw / 2, y + 33, a, 18, INK, anchor='middle')
        f.line(lx + lw + 6, y + 27, rx - 8, y + 27, color=TEAL, width=2, arrow=True, dash=True)
        f.rect(rx, y, rw, 54, fill='#ffffff', stroke=LINE, width=1.5, rx=10)
        f.text(rx + rw / 2, y + 33, b, 18, INK, anchor='middle')
    f.rect(lx, 606, rx + rw - lx, 42, fill=AMBER, stroke='none', width=0, rx=8, opacity=0.15)
    f.text((lx + rx + rw) / 2, 634, '結末を知ることは結末まで生きたことではない', 19, AMBER, anchor='middle', weight=700)
    made.add(f.save('08-e-knowing-and-still-living.svg'))


def draw(made: set[str]) -> None:
    fig_a(made)
    fig_b(made)
    fig_c(made)
    fig_d(made)
    fig_e(made)
