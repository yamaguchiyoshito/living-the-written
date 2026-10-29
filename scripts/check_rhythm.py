# 改稿版の記事を references/checklist.md の数値目安と照合する。
# 使い方: python3 -I scripts/check_rhythm.py chapters/NN-xxx.md
import re, sys
text = open(sys.argv[1], encoding='utf-8').read()
body = text.split('\n---\n')[0]
chapters = re.split(r'\n#{2,3} ', body)
tot_q = 0; tot_bold = len(re.findall(r'\*\*', body))//2
print(f"bold={tot_bold}")
# 冒頭: 副題の直後から太字の問いまで（「私」の場面と一般論）
opening = chapters[1].partition('\n')[2] if len(chapters) > 1 else ''
opening = opening.split('<!-- /NAV -->', 1)[-1]
lead = [p.strip() for p in opening.split('**')[0].split('\n\n') if p.strip() and not p.strip().startswith('<!--')]
lead_chars = sum(len(re.sub(r'\s', '', p)) for p in lead)
me_chars = len(re.sub(r'\s', '', lead[0])) if lead else 0
print(f"冒頭: 太字の問いまで={lead_chars}字 「私」の場面={me_chars}字")
if lead_chars > 250: print("  ! 冒頭: 太字の問いまでが250字を超える")
if me_chars > 150: print("  ! 冒頭: 「私」の場面が150字を超える")
for ch in chapters[1:]:
    title, _, rest = ch.partition('\n')
    paras = [p.strip() for p in rest.split('\n\n') if p.strip() and not p.strip().startswith(('![', '*図', '*書影', '*場面', '<!--', '[', '## 参考文献', '> '))]
    sents_all=[]; issues=[]
    one=0; nocomma_bad=0
    for pi,p in enumerate(paras):
        p = p.replace('**','')
        p = re.sub(r'「[^」]*」', '「」', p)  # 引用文の中は数えない（文言を変えられないため）
        sents = [s for s in re.split(r'(?<=。)', p) if s.strip()]
        if len(sents)<=1: one+=1
        if len(sents)>6: issues.append(f"P{pi+1}: {len(sents)}文")
        nc = sum(1 for s in sents if '、' not in s)
        if len(sents)>1 and nc*2 < len(sents): issues.append(f"P{pi+1}: 読点なし文が半数未満 ({nc}/{len(sents)})")
        for s in sents:
            L=len(s); c=s.count('、')
            if (L<=40 and c>1) or c>2: issues.append(f"読点過多({c},{L}字): {s[:30]}")
        sents_all += sents
        # paragraph-start connectives
        if re.match(r'^(つまり|したがって|そして|ここで)', p): issues.append(f"P{pi+1}: 段落先頭接続詞")
    # consecutive endings
    ends=[re.sub(r'.*?(\S{3})。$', r'\1', s.strip()) for s in sents_all]
    run=1
    for i in range(1,len(ends)):
        run = run+1 if ends[i]==ends[i-1] else 1
        if run==3: issues.append(f"同じ文末3連続: …{ends[i]}。 ({sents_all[i][:20]})")
    # subject-start runs
    run=0
    for s in sents_all:
        if re.match(r'^\s*\S{1,8}は', s): run+=1
        else: run=0
        if run==4: issues.append(f"主語始まり4連続: {s[:20]}")
    q = sum(1 for s in sents_all if s.strip().endswith('か。')); tot_q+=q
    shikashi = rest.count('しかし')
    short = sum(1 for s in sents_all if len(s)<=15); long = sum(1 for s in sents_all if 60<=len(s)<=90); over=sum(1 for s in sents_all if len(s)>90)
    mid = [25<=len(s)<=45 for s in sents_all]; midrun=0
    for m in mid:
        midrun = midrun+1 if m else 0
        if midrun==4: issues.append("中間の長さ4文連続")
    work = len(re.findall(r'『[^』]*』(は|の独創性は)|テッド・チャンは', rest))
    print(f"\n## {title}\n  段落={len(paras)} 文={len(sents_all)} 一文段落={one} 疑問={q} しかし={shikashi} 短文(<=15)={short} 長文(60-90)={long} 90超={over} 作品主語={work}")
    for i in issues: print("  !", i)
print(f"\n疑問文合計={tot_q}")
