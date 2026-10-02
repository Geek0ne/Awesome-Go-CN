#!/usr/bin/env python3
"""
GitHub 锚点算法复现 + 显式锚点注入

背景：awesome-go 的目录有 152 个锚点链接，且**没有**任何显式 `<a id>`，
全靠 GitHub 从标题文字自动生成。直接把标题汉化 → 锚点变中文 → 152 个链接全断。

解法：汉化后，在每个标题前插入 `<a id="原英文锚点"></a>`，
把锚点钉死在英文 slug 上，目录 152 个链接继续可用。

本脚本第一步是**验证**：能否从英文标题准确复现 GitHub 的锚点。
复现不出 152/152 就不许注入锚点。
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# GitHub 的 slug 规则：小写、去标点、空格转连字符
_PUNCT = re.compile(r"[^\w\s-]", re.UNICODE)
_SPACE = re.compile(r"[\s]+")


def gh_slug(text: str) -> str:
    """复现 GitHub 自动锚点。"""
    s = text.strip().lower()
    s = s.replace("`", "")            # 行内代码去反引号
    s = _PUNCT.sub("", s)             # 去标点
    s = _SPACE.sub("-", s)            # 空白转连字符
    return s.strip("-")


def main() -> int:
    blocks = json.loads(Path("blocks.json").read_text(encoding="utf-8"))

    # 收集目录里的锚点链接
    toc_anchors: set[str] = set()
    for b in blocks:
        if b["type"] == "entry" and b.get("url", "").startswith("#"):
            toc_anchors.add(b["url"][1:])

    # 用英文标题复现锚点
    produced = {}
    for b in blocks:
        if b["type"] == "heading" and b["level"] in (1, 2, 3, 4):
            produced.setdefault(gh_slug(b["text"]), b["text"])

    hit = toc_anchors & set(produced)
    miss = toc_anchors - set(produced)

    print(f"目录锚点总数      : {len(toc_anchors)}")
    print(f"能从标题复现      : {len(hit)}")
    print(f"复现不了          : {len(miss)}")
    if miss:
        print("  未命中样例:", sorted(miss)[:10])
    ratio = len(hit) / len(toc_anchors) * 100 if toc_anchors else 0
    print(f"复现率            : {ratio:.1f}%")

    if ratio < 100:
        print("\n❌ 未达 100%，不注入锚点（避免钉错，反而更糟）")
        return 1
    print("\n✅ 100% 复现，可以安全注入显式锚点")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())