# 変更履歴

[連載目次へ](README.md)

## 1.2.0 — 2026-10-29

- 作品からの引用文を本文に入れた（第1〜8回、計11か所）。文言はWeb上で確認できたものに限り、出所と取得日、原文未照合の旨を脚注に記した。
- 作品の書影7点を `assets/works/` に置き、初出の節に入れた。出典は `assets/works/README.md` にある。引用文と書影は各権利者に帰属し CC BY 4.0 の対象外である。
- ビルドの修正：同じ脚注の複数参照を一つの注にまとめる。書影のキャプションが次の図まで本文を飲み込む不具合を直す。complete.html に jpg/png も埋め込む。

## 1.1.0 — 2026-10-29

- 各回の冒頭を詰めた（語り手の場面は1段落120字前後、太字の問いまで250字以内）。
- 図のない節に挿絵7点を追加し、表紙を除いて54点にした（`claudedocs/figure-plan-round2.md`）。
- トップページから表紙画像を外した。

## 1.0.0 — 2026-10-29

- 全8回の本文を随想寄りの文体へ改稿し、`chapters/` に置いた。文体の規則は `guides/STYLE.md` 以下にある。
- `yamaguchiyoshito/multi-scale-time` と同じ方式で、検査（`scripts/validate.py`）、変換（`scripts/build.py`）、HTML検査（`scripts/check_html.py`）、回帰試験（`tests/`）、GitHub Actionsによる配置を導入した。
- 扱った作品と参照した理論の書誌を `references/sources.json` に置き、各回末尾の脚注と対応させた。
- 表紙と各回の挿絵47点を `scripts/draw_figures.py` と `scripts/figures/chNN.py` から生成し、本文の該当段落の直後に置いた。計画は `claudedocs/figure-plan.md` にある。
