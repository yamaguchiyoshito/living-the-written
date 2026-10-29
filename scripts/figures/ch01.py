"""第1回「時間は流れているのか、それとも私たちが流しているのか」の挿絵（図1-1〜図1-5）。"""
from __future__ import annotations

from draw_figures import Figure, person, BG, INK, MUTED, LINE, SOFT, BLUE, AMBER, TEAL, PLUM


def _poly(f: Figure, pts, fill, opacity=1.0, stroke='none', width=0):
    s = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    op = f' opacity="{opacity}"' if opacity < 1 else ''
    f.body.append(f'<polygon points="{s}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"{op}/>')


def _qb(p0, p1, p2, t):
    """二次ベジェ曲線上の点。"""
    a, b, c = (1 - t) ** 2, 2 * (1 - t) * t, t ** 2
    return (a * p0[0] + b * p1[0] + c * p2[0], a * p0[1] + b * p1[1] + c * p2[1])


def _fan(f: Figure, apex, a, b, color=TEAL):
    """視野を示す扇形（半透明の三角形）。"""
    _poly(f, [apex, a, b], color, opacity=0.14)


def fig_a(made: set[str]) -> None:
    """図1-1：観客の順序とフィルムの全体。"""
    f = Figure(1, '観客の順序とフィルムの全体', '観客が順に観ていく場面と、上映前から記録されているフィルムの全体を一つの帯の上で対照する。', 720, 'a')
    # 上段：フィルムの帯（6コマ）
    bx0, by0, bw, bh = 140, 240, 1010, 132
    f.text(775, 224, '上映前からすべての場面が記録されている', 16, MUTED, anchor='middle')
    f.text(1150, 224, '全体の存在のしかた', 17, INK, anchor='end', weight=700)
    f.rect(bx0, by0, bw, bh, fill=SOFT, stroke=LINE, width=2, rx=8)
    for x in range(bx0 + 14, bx0 + bw - 10, 40):  # 送り穴
        f.rect(x, by0 + 7, 12, 8, fill='#ffffff', stroke='none', width=0, rx=2)
        f.rect(x, by0 + bh - 15, 12, 8, fill='#ffffff', stroke='none', width=0, rx=2)
    f.text(50, by0 + bh / 2 + 6, 'フィルム', 18, INK, weight=700)
    fw, gap = 140, 24
    centers = []
    for i in range(6):
        x = 165 + i * (fw + gap)
        centers.append(x + fw / 2)
        f.rect(x, by0 + 22, fw, bh - 44, fill='#ffffff', stroke=INK, width=1.5, rx=4)
        label = '冒頭' if i == 0 else ('結末' if i == 5 else ('' if i == 1 else '…'))
        f.text(x + fw / 2, by0 + bh / 2 + 7, label, 19, INK, anchor='middle', weight=700 if i in (0, 5) else 400)
    # いま観ている場面（2コマ目）に琥珀の縦線
    now_x = centers[1]
    f.text(now_x, 224, 'いま観ている場面', 16, AMBER, anchor='middle', weight=700)
    f.line(now_x, 230, now_x, 392, color=AMBER, width=3)
    f.text(centers[5], 398, 'まだ来ていない結末', 16, MUTED, anchor='middle')
    # 下段左：観客と視野
    px, py = 270, 590
    _fan(f, (px + 6, 518), (bx0 + 25, by0 + bh + 2), (now_x - 2, by0 + bh + 2))
    f.line(px + 30, 505, now_x - 10, 384, color=BLUE, width=2, arrow=True)
    person(f, px, py, TEAL, 1.0)
    f.text(px, 652, '観客', 17, TEAL, anchor='middle', weight=700)
    # 下段右：順番に観る
    f.text(540, 520, '経験の順序', 17, TEAL, weight=700)
    f.line(540, 548, 1125, 548, color=TEAL, width=2, arrow=True)
    f.text(540, 582, '観客は冒頭から結末へ順番に観る（逐次的認識）', 16, MUTED)
    f.footer('フィルムにとって冒頭も結末も同じように存在する。観客にとって結末はまだ来ていない。')
    made.add(f.save('01-a-film-and-audience.svg'))


def fig_b(made: set[str]) -> None:
    """図1-2：話すヘプタポッドAと書くヘプタポッドB。"""
    f = Figure(1, '話すヘプタポッドAと書くヘプタポッドB', '順番に音を並べるヘプタポッドAと、一つの図形の全体が最初の一筆を決めるヘプタポッドBを並べる。', 650, 'b')
    py0, ph = 200, 410
    f.panel(50, py0, 540, ph, 'ヘプタポッドA・人間の言語')
    f.panel(610, py0, 540, ph, 'ヘプタポッドB')
    f.line(600, py0 + 20, 600, py0 + ph - 20, color=LINE, width=1)
    # 左：4つの箱を矢印でつなぐ
    bw, gap, by = 96, 38, 360
    labels = ['最初の音', '次の音', '…', '最後の音']
    for i, lab in enumerate(labels):
        x = 71 + i * (bw + gap)
        f.box(x, by, bw, 56, lab, '', BLUE, 18)
        if i < 3:
            f.line(x + bw + 4, by + 28, x + bw + gap - 4, by + 28, color=BLUE, width=2, arrow=True)
    f.text(71, 332, '書きながら次を考えられる', 15, MUTED)
    f.line(71, 470, 569, 470, color=AMBER, width=2, arrow=True)
    f.text(320, 500, '時間の中で発せられる', 16, AMBER, anchor='middle', weight=700)
    f.text(320, 560, '部分を順番に積み重ねて全体をつくる', 15, MUTED, anchor='middle')
    # 右：全体の輪と内部の線
    cx, cy = 880, 390
    f.circ(cx, cy, 135, BLUE, fill=False, width=10, opacity=0.16)
    f.text(cx, cy - 121, '全体', 17, BLUE, anchor='middle', weight=700)
    f.circ(cx, cy, 110, BLUE, fill=False, width=2.5)
    p1 = ((cx - 90, cy + 60), (cx - 30, cy - 75), (cx + 85, cy - 40))   # 最初の一筆
    p2 = ((cx - 80, cy + 70), (cx, cy + 15), (cx + 95, cy + 60))
    p3 = ((cx + 45, cy - 83), (cx + 20, cy + 15), (cx + 50, cy + 107))
    for p in (p2, p3):
        f.path(f'M {p[0][0]:.1f} {p[0][1]:.1f} Q {p[1][0]:.1f} {p[1][1]:.1f} {p[2][0]:.1f} {p[2][1]:.1f}', color=BLUE, width=2)
    b2 = _qb(*p2, 0.25)
    f.line(b2[0], b2[1], b2[0] - 22, b2[1] + 46, color=BLUE, width=2)
    b3 = _qb(*p3, 0.5)
    f.line(b3[0], b3[1], b3[0] + 48, b3[1] - 14, color=BLUE, width=2)
    f.path(f'M {p1[0][0]:.1f} {p1[0][1]:.1f} Q {p1[1][0]:.1f} {p1[1][1]:.1f} {p1[2][0]:.1f} {p1[2][1]:.1f}', color=BLUE, width=5.5)
    # 全体の輪から最初の一筆へ（破線）
    f.line(cx - 95, cy - 95, cx - 56, cy - 20, color=BLUE, width=2, arrow=True, dash=True)
    # 他の線から最初の一筆へ（短い破線）
    m2 = _qb(*p2, 0.5)
    t1 = _qb(*p1, 0.5)
    f.line(m2[0], m2[1] - 6, t1[0] + 3, t1[1] + 10, color=BLUE, width=1.8, arrow=True, dash=True)
    t2 = _qb(*p1, 0.85)
    f.line(b3[0] + 46, b3[1] - 20, t2[0] + 4, t2[1] + 10, color=BLUE, width=1.8, arrow=True, dash=True)
    # 最初の一筆のラベル（輪の外に置き、細い線で結ぶ）
    f.text(cx - 150, cy + 66, '最初の一筆', 16, BLUE, anchor='end', weight=700)
    f.line(cx - 144, cy + 61, cx - 94, cy + 60, color=BLUE, width=1.2)
    f.text(cx, py0 + ph - 50, '他の線との位置関係で意味が決まる', 15, MUTED, anchor='middle')
    f.text(cx, py0 + ph - 22, '書く前に全体がある', 17, BLUE, anchor='middle', weight=700)
    made.add(f.save('01-b-heptapod-a-and-b.svg'))


def fig_c(made: set[str]) -> None:
    """図1-3：逐次的認識と同時的認識。"""
    f = Figure(1, '逐次的認識と同時的認識', '過去を記憶し未来を予測する逐次的認識と、出来事の全体を既知として持つ同時的認識を、二本の時間帯で対照する。', 800, 'c')
    # 上パネル：逐次的認識
    f.panel(50, 200, 1100, 260, '逐次的認識')
    by, bh = 320, 40
    f.rect(90, by, 470, bh, fill=PLUM, stroke='none', width=0, rx=bh / 2, opacity=0.75)
    f.rect(624, by, 486, bh, fill=BLUE, stroke='none', width=0, rx=bh / 2, opacity=0.28)
    f.rect(580, by - 8, 24, bh + 16, fill=AMBER, stroke='none', width=0, rx=6)
    f.text(325, 302, '過去＝記憶の対象', 17, PLUM, anchor='middle', weight=700)
    f.text(867, 302, '未来＝予測の対象', 17, BLUE, anchor='middle', weight=700)
    person(f, 592, 294, TEAL, 0.55)
    f.text(592, 386, '現在', 17, AMBER, anchor='middle', weight=700)
    f.line(200, 406, 570, 406, color=PLUM, width=2, arrow=True)
    f.line(614, 406, 1000, 406, color=BLUE, width=2, arrow=True, dash=True)
    f.text(110, 444, '原因', 16, INK)
    f.line(150, 438, 230, 438, color=INK, width=1.8, arrow=True)
    f.text(240, 444, '結果', 16, INK)
    f.text(1110, 444, '情報は経験とともに増える', 15, MUTED, anchor='end')
    # 下パネル：同時的認識
    f.panel(50, 480, 1100, 290, '同時的認識')
    by2 = 580
    f.rect(70, 560, 1060, 80, fill='none', stroke=BLUE, width=1.5, rx=12, dash=True)
    f.rect(90, by2, 1020, bh, fill=BLUE, stroke='none', width=0, rx=bh / 2, opacity=0.55)
    f.text(70, 552, '出来事全体の関係', 15, BLUE)
    f.text(600, 552, '過去も未来も既知', 17, BLUE, anchor='middle', weight=700)
    f.line(150, 570, 560, 570, color=BLUE, width=1.8, arrow=True)
    f.line(1050, 570, 640, 570, color=BLUE, width=1.8, arrow=True)
    apex = (600, 688)
    _fan(f, apex, (90, by2), (1110, by2))
    f.line(apex[0], apex[1], 90, by2, color=TEAL, width=1.2, opacity=0.6)
    f.line(apex[0], apex[1], 1110, by2, color=TEAL, width=1.2, opacity=0.6)
    person(f, 600, 740, TEAL, 0.7)
    f.text(1110, 750, '同じ瞬間に感じることではない', 15, MUTED, anchor='end')
    made.add(f.save('01-c-sequential-and-simultaneous.svg'))


def fig_d(made: set[str]) -> None:
    """図1-4：予測と記憶、そして未来の記憶。"""
    f = Figure(1, '予測と記憶、そして未来の記憶', '人間の予測と記憶の向きの違いと、ルイーズにおいて未来の出来事が記憶の形で現れる様子を並べる。', 640, 'd')
    py0, ph = 200, 400
    f.panel(50, py0, 540, ph, '予測と記憶')
    f.panel(610, py0, 540, ph, 'ルイーズ')
    f.line(600, py0 + 20, 600, py0 + ph - 20, color=LINE, width=1)
    # 左：現在の縦線と人型、過去の箱と未来の箱
    nx = 320
    f.line(nx, 262, nx, 530, color=AMBER, width=3)
    person(f, nx, 480, TEAL, 0.8)
    f.text(nx, 556, '現在', 17, AMBER, anchor='middle', weight=700)
    f.rect(70, 330, 180, 70, fill=PLUM, stroke=PLUM, width=2, rx=14, opacity=0.14)
    f.rect(70, 330, 180, 70, fill='none', stroke=PLUM, width=2, rx=14)
    f.text(160, 371, '経験済みの出来事', 16, PLUM, anchor='middle', weight=700)
    f.line(254, 365, nx - 8, 365, color=PLUM, width=2, arrow=True)
    f.text(283, 352, '記憶', 16, PLUM, anchor='middle', weight=700)
    f.rect(364, 330, 216, 70, fill=BLUE, stroke=BLUE, width=2, rx=14, opacity=0.12)
    f.rect(364, 330, 216, 70, fill='none', stroke=BLUE, width=2, rx=14)
    f.text(472, 371, 'まだ経験していない出来事', 16, BLUE, anchor='middle', weight=700)
    f.line(nx + 8, 365, 360, 365, color=BLUE, width=2, arrow=True, dash=True)
    f.text(344, 352, '予測', 16, BLUE, anchor='middle', weight=700)
    f.text(472, 428, '将来の経験で確かめられる', 15, MUTED, anchor='middle')
    # 右：ルイーズ。未来の位置に紫の箱（輪郭は破線、塗りは紫）
    lx = 820
    f.line(lx, 262, lx, 530, color=AMBER, width=3)
    person(f, lx, 480, TEAL, 0.8)
    f.text(lx, 556, '現在', 17, AMBER, anchor='middle', weight=700)
    f.rect(930, 316, 180, 100, fill=PLUM, stroke='none', width=0, rx=14, opacity=0.2)
    f.rect(930, 316, 180, 100, fill='none', stroke=PLUM, width=2, rx=14, dash=True)
    f.text(1020, 360, '娘が生まれる', 17, PLUM, anchor='middle', weight=700)
    f.text(1020, 392, '娘を失う', 17, PLUM, anchor='middle', weight=700)
    f.line(lx + 8, 365, 926, 365, color=PLUM, width=2, arrow=True)
    f.text(877, 352, '未来の記憶', 16, PLUM, anchor='middle', weight=700)
    f.lines(1020, 446, ['まだ起きていない（破線の輪郭）', 'すでに知られている（紫の塗り）'], 15, MUTED, anchor='middle', gap=24)
    made.add(f.save('01-d-prediction-and-memory.svg'))


def fig_e(made: set[str]) -> None:
    """図1-5：知らないことと、ないこと。"""
    f = Figure(1, '知らないことと、ないこと', '未来が見えない状態と未来が存在しない状態を、同じ位置に立つ人型から見た二本の時間帯で比べる。', 740, 'e')
    nx, bh = 520, 40
    # 上パネル：未来を知らない
    f.panel(50, 200, 930, 240)
    f.text(70, 234, '未来を知らない', 23, INK, weight=700)
    by = 310
    f.rect(90, by, nx - 90, bh, fill=PLUM, stroke='none', width=0, rx=bh / 2, opacity=0.75)
    f.rect(nx, by, 940 - nx, bh, fill=MUTED, stroke='none', width=0, rx=bh / 2, opacity=0.5)
    f.text(305, 298, '過去', 17, PLUM, anchor='middle', weight=700)
    f.line(nx, 260, nx, 376, color=AMBER, width=3)
    _fan(f, (nx + 12, 243), (680, 205), (680, 281))
    person(f, nx, 285, TEAL, 0.7)
    f.rect(600, 225, 340, 158, fill=LINE, stroke='none', width=0, rx=14, opacity=0.82)
    f.text(770, 278, '見えないが続いている', 16, INK, anchor='middle', weight=700)
    f.text(770, 414, '知らない出来事', 16, MUTED, anchor='middle')
    f.text(nx, 404, '現在', 17, AMBER, anchor='middle', weight=700)
    # 下パネル：未来がない
    f.panel(50, 460, 930, 240)
    f.text(70, 494, '未来がない', 23, INK, weight=700)
    by2 = 570
    f.rect(90, by2, nx - 90, bh, fill=PLUM, stroke='none', width=0, rx=bh / 2, opacity=0.75)
    f.text(305, 558, '過去', 17, PLUM, anchor='middle', weight=700)
    f.line(nx, 520, nx, 636, color=AMBER, width=3)
    _fan(f, (nx + 12, 503), (680, 465), (680, 541))
    person(f, nx, 545, TEAL, 0.7)
    f.text(770, 596, '現在が進むにつれて生まれる', 16, INK, anchor='middle', weight=700)
    f.text(770, 674, '存在しない出来事', 16, MUTED, anchor='middle')
    f.text(nx, 664, '現在', 17, AMBER, anchor='middle', weight=700)
    # 右端：上から下へは導けない
    ax = 1065
    f.text(ax, 292, '別の状態', 17, INK, anchor='middle', weight=700)
    f.line(ax, 312, ax, 600, color=BLUE, width=2, arrow=True, dash=True)
    f.circ(ax, 455, 16, BG)
    f.line(ax - 9, 446, ax + 9, 464, color=INK, width=3)
    f.line(ax - 9, 464, ax + 9, 446, color=INK, width=3)
    f.text(ax + 20, 461, '導けない', 16, INK, weight=700)
    made.add(f.save('01-e-unknown-and-nonexistent.svg'))


def draw(made: set[str]) -> None:
    fig_a(made)
    fig_b(made)
    fig_c(made)
    fig_d(made)
    fig_e(made)
