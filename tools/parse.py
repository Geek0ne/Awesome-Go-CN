#!/usr/bin/env python3
"""
awesome-go README 汉化管道 · 解析器

把 README.md 拆成"块"，只把**需要翻译的文本**抽出来，链接和格式原样保留。

设计要点：
  · 每行归为三类：heading / entry / raw
  · raw 原样保存，一个字节都不动（徽章、HTML 表格、赞助商区等）
  · entry 拆成 name / url / desc —— name 与 url **永不翻译**，只译 desc
  · 必须满足：parse → render 与原文逐字节一致（见 verify_roundtrip.py）
    这条不通过，整条管道作废，绝不进入翻译阶段。
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# 条目：`- [Name](url) - Description.`
# desc 内部可能含 [文字](链接)，必须原样保留
ENTRY_RE = re.compile(
    r"^(?P<indent>\s*)(?P<bullet>[-*+])\s+"
    r"\[(?P<name>[^\]]*)\]\((?P<url>[^)]*)\)"
    r"(?P<gap>\s*(?:-\s+|:\s+|—\s+)?)"
    r"(?P<desc>.*)$"
)

HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<text>.*?)(?P<trail>\s*#*)\s*$")


def parse(md_text: str) -> list[dict]:
    """把 Markdown 全文拆成块列表。"""
    blocks: list[dict] = []
    for lineno, line in enumerate(md_text.split("\n"), 1):
        m = ENTRY_RE.match(line)
        if m and m.group("name") and m.group("url"):
            blocks.append({
                "type": "entry",
                "lineno": lineno,
                "indent": m.group("indent"),
                "bullet": m.group("bullet"),
                "name": m.group("name"),
                "url": m.group("url"),
                "gap": m.group("gap"),
                "desc": m.group("desc"),
            })
            continue

        h = HEADING_RE.match(line)
        if h:
            blocks.append({
                "type": "heading",
                "lineno": lineno,
                "level": len(h.group("hashes")),
                "hashes": h.group("hashes"),
                "text": h.group("text"),
                "trail": h.group("trail"),
            })
            continue

        blocks.append({"type": "raw", "lineno": lineno, "text": line})
    return blocks


def render(blocks: list[dict], anchors: bool = True) -> str:
    """把块列表还原成 Markdown 全文。

    anchors=True 时，为带 anchor 字段的标题输出 `<a id="..."></a>`，
    把锚点钉在英文 slug 上 —— 标题汉化后目录的 152 个链接依然可用。
    """
    out: list[str] = []
    for b in blocks:
        if b["type"] == "entry":
            # bullet 必须原样还原：上游确实存在 * 开头的条目，
            # 统一输出 - 会改动原文，往返验证会失败。
            bl = b.get("bullet", "-")
            out.append(f'{b["indent"]}{bl} [{b["name"]}]({b["url"]}){b["gap"]}{b["desc"]}')
        elif b["type"] == "heading":
            if anchors and b.get("anchor"):
                out.append(f'<a id="{b["anchor"]}"></a>')
            out.append(f'{b["hashes"]} {b["text"]}{b["trail"]}')
        else:
            out.append(b["text"])
    return "\n".join(out)


def main() -> int:
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
    dst = Path(sys.argv[2] if len(sys.argv) > 2 else "blocks.json")

    text = src.read_text(encoding="utf-8")
    blocks = parse(text)
    dst.write_text(json.dumps(blocks, ensure_ascii=False, indent=1), encoding="utf-8")

    counts: dict[str, int] = {}
    for b in blocks:
        counts[b["type"]] = counts.get(b["type"], 0) + 1

    rebuilt = render(blocks)
    ok = rebuilt == text

    print(f"源文件      : {src} ({len(text)} 字符, {text.count(chr(10))+1} 行)")
    print(f"块统计      : heading={counts.get('heading',0)}  "
          f"entry={counts.get('entry',0)}  raw={counts.get('raw',0)}")
    print(f"往返一致    : {'✅ 是' if ok else '❌ 否 — 管道不可用'}")
    if not ok:
        a = text.split("\n")
        b = rebuilt.split("\n")
        for i, (x, y) in enumerate(zip(a, b), 1):
            if x != y:
                print(f"  首个差异 行 {i}:\n    原文: {x[:120]}\n    生成: {y[:120]}")
                break
        if len(a) != len(b):
            print(f"  行数不同: 原文 {len(a)} vs 生成 {len(b)}")
    print(f"已写出      : {dst}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())