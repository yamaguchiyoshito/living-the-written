# 編集・保守ガイド

[連載目次へ](../README.md)

## 原本と生成物の責務

| パス | 責務 | 編集方法 |
| --- | --- | --- |
| `chapters/*.md` | 各回の本文、図の参照とキャプション、脚注、前後リンク | [文体ルール](STYLE.md)に従って直接編集する |
| `series.json` | 連載の順序、題名、副題、概要、部（`parts`）、各回の図の一覧（`figures`）と出典の対応 | 本文変更と同じ変更で整合させる |
| `assets/illustrations/*.svg` | 本文から参照する独立した挿絵 | `draw_figures.py` を編集して再生成する |
| `scripts/draw_figures.py`、`scripts/figures/chNN.py` | 表紙（draw_figures.py）と各回の図（chNN.py の draw）を再現する図形コード | 原則としてこちらを編集する。`--chapter N` で1回分だけ描き直せる |
| `scripts/render_png.sh` | 目視確認用に SVG を PNG へ変換する（rsvg-convert が必要） | 生成物はリポジトリに入れない |
| `references/sources.json` | 作品と理論の書誌と今回の確認範囲 | 一次情報と確認状況を分けて更新する |
| `references/bibliography.md` | 読者向けの文献一覧 | `scripts/bibliography.py` で再生成する |
| `guides/STYLE.md` 以下 | 文体ルール（構成、リズム、作品への忠実さ、読者と用語、改稿チェックリスト） | 規則を変えるときに更新する |
| `scripts/check_rhythm.py` | 本文を文体ルールの数値目安と照合する | 規則の変更に合わせて保守する |
| `site-src/styles.css` | HTML閲覧用の見た目 | 本文内容を持たせない |
| `scripts/build.py` | MarkdownをHTMLへ変換 | 原本を改変しない |
| `scripts/validate.py` | 本文・参照・SVG・出典の構造検査 | 検査規則を保守する |
| `scripts/check_html.py` | HTMLの相対リンク・アンカー・外部依存を検査 | 生成後に実行する |
| `tests/` | 検査・変換の回帰試験 | 成功例と失敗例を両方持つ |
| `_site/` | ブラウザ用生成物 | 直接編集せず再生成する |

## 変更の最小手順

```sh
# Markdown、図の生成コード、出典を編集した後
python scripts/draw_figures.py
python scripts/bibliography.py
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/build.py
python scripts/check_html.py
python -I scripts/check_rhythm.py chapters/01-perception-of-time.md
```

SVGを直接修正すると次の図再生成で上書きされる。長期保守する変更は `draw_figures.py` か `scripts/figures/chNN.py` に反映する。図を直した後は `sh scripts/render_png.sh <出力先> assets/illustrations/NN-*.svg` で PNG にして目視する。回数は `series.json` の `chapters` の数で決まり、検査・ビルド・目次はそこから読む。

## 各回の型

各回の構成は[構成と結末](style-structure.md)に従う。題名は `# 第N回　題名`、副題は `## 副題`、節見出しは `###` で番号とラベルを付けない。副題の直後に `<!-- NAV:TOP -->`、末尾に `<!-- NAV:BOTTOM -->` の前後リンクを置く。本文の後に区切り線を置き、次回の題名を1行で示し（最終回は後書きに「（全8回・完）」を添える）、その下に `## 参考文献・注記` を置く。注記の先頭は連載内の注（用語、他の回への参照、概説の範囲）の段落で、その後に `[^id]: ` の脚注定義を並べる。本文側は作品や理論の初出に `[^id]` を付けるだけで、文章は変えない。

## 図の置き方と密度

図は、その内容を説明し終えた段落の直後に置く。1枚につき主張は1つ、パネルは2枚まで、ラベル文は10個前後までとする。密度は本文1,300字前後に1枚を目安とし（1回あたり4〜7枚）、冒頭と結末の語り手の場面、結末直前の段落、総括の節には置かない。読後の余韻を図で回収しない。

ファイル名は `NN-x-slug.svg`（回番号と枝番）とし、`series.json` の `figures` に本文での登場順に並べる。Markdownから `![代替テキスト](../assets/illustrations/01-a-sequential-and-simultaneous.svg)` のように相対参照し、直後に `*図N-k：前提と帰結*` というキャプションを置く。`k` は回内の通し番号で、検査は `figures` の数と順序に一致することを確かめる。SVGコードを本文へ貼り付けない。

図の中の文字は14px以上（1200px基準）とし、ラベルは16px、注記は14pxを基本にする。箱と箱の間の矢印は24px以上の長さを取る。矢じりは線と同じ色にする。色は、青＝認識・記述・知ること、青緑＝経験・行為・生きること、琥珀＝現在・いま・転機、紫＝記憶・過去・物語とし、カテゴリの区別だけに使う場合はその旨を凡例に書く。矢印は実線＝因果・流れ、破線＝解釈・言い換え・仮の対応。図の副題（`desc`）は「何を見るか」を書き、キャプションは「前提と帰結」を書いて役割を分ける。

SVGには `viewBox`、`role="img"`、`title`、`desc` を持たせる。`script`、`foreignObject`、外部画像、外部フォント、イベントハンドラは入れない。日本語の表示は閲覧環境のフォントを利用し、フォントファイルは同梱しない。

## 出典の管理

作品と理論は本文の脚注 `[^chiang-story]` と末尾の「参考文献・注記」の脚注定義でつなぐ。同じIDを `sources.json` と `series.json` の `sources` でも使う。検査は、脚注の使用と定義、`series.json` の一覧、`sources.json` の存在が一致することを確かめる。作品の結末や台詞を書きやすさのために変えないこと、作品にない場面を足さないことは[作品への忠実さ](style-fidelity.md)に従う。

## 公開前の目視確認

GitHubのPreview、HTMLのデスクトップ幅とスマートフォン幅で確認する。ページ全体の横はみ出し、欠けた日本語、切れた図の文字は修正する。
