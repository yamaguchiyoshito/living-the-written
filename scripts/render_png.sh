#!/bin/sh
# 挿絵SVGを目視確認用のPNGに変換する（rsvg-convert が必要）。出力先は第1引数のディレクトリ。
# 使い方: sh scripts/render_png.sh /path/to/outdir assets/illustrations/01-*.svg
out="$1"; shift
mkdir -p "$out"
for f in "$@"; do rsvg-convert -w 1200 "$f" -o "$out/$(basename "$f" .svg).png"; done
