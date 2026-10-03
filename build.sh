#!/usr/bin/env bash
# 汉化管道一键构建。每一步都是幂等的、基于同一个原始输入。
set -euo pipefail

cd "$(dirname "$0")"
SRC="${SRC:-/root/code/awesome-go/README.md}"

echo "════ 1/7 解析 + 往返验证 ════"
# 从上游原始 README 重新解析，不复用上一次的中间产物
python3 tools/parse.py "$SRC" blocks.json

echo
echo "════ 2/7 锚点复现校验 ════"
python3 tools/anchors.py

echo
echo "════ 3/7 标题 + 目录汉化 ════"
python3 tools/translate_headings.py

echo
echo "════ 4/7 分类描述汉化 ════"
python3 tools/translate_descriptions.py

echo
echo "════ 5/7 杂项汉化 ════"
python3 tools/translate_misc.py

echo
echo "════ 6/7 条目描述套用 ════"
python3 tools/entry_store.py render

echo
echo "════ 7/7 生成 README ════"
python3 tools/make_readme.py

echo
echo "════ 验收 ════"
python3 tools/verify.py