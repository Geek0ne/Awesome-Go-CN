#!/usr/bin/env bash
# 汉化管道一键构建。每一步都是幂等的、基于同一个原始输入。
set -euo pipefail

cd "$(dirname "$0")"
SRC="${SRC:-/root/code/awesome-go/README.md}"

echo "════ 1/6 解析 + 往返验证 ════"
# 从上游原始 README 重新解析，不复用上一次的中间产物
python3 tools/parse.py "$SRC" blocks.json

echo
echo "════ 2/6 锚点复现校验 ════"
python3 tools/anchors.py

echo
echo "════ 3/6 标题 + 目录汉化 ════"
python3 tools/translate_headings.py

echo
echo "════ 4/6 分类描述汉化 ════"
python3 tools/translate_descriptions.py

echo
echo "════ 5/6 杂项汉化 ════"
python3 tools/translate_misc.py

echo
echo "════ 6/6 生成 README ════"
python3 tools/make_readme.py

echo
echo "════ 验收 ════"
python3 tools/verify.py