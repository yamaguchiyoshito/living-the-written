# 変更履歴

[連載目次へ](README.md)

## 1.0.0 — 2026-10-29

- 全8回の本文を随想寄りの文体へ改稿し、`chapters/` に置いた。文体の規則は `guides/STYLE.md` 以下にある。
- `yamaguchiyoshito/multi-scale-time` と同じ方式で、検査（`scripts/validate.py`）、変換（`scripts/build.py`）、HTML検査（`scripts/check_html.py`）、回帰試験（`tests/`）、GitHub Actionsによる配置を導入した。
- 扱った作品と参照した理論の書誌を `references/sources.json` に置き、各回末尾の脚注と対応させた。
- 表紙と各回の挿絵47点を `scripts/draw_figures.py` と `scripts/figures/chNN.py` から生成し、本文の該当段落の直後に置いた。計画は `claudedocs/figure-plan.md` にある。
