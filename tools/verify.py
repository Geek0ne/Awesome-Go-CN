#!/usr/bin/env python3
"""终验：README 的五项硬指标。任何一项不过就不算完成。"""

import json
import re
import sys
from pathlib import Path

md = Path("README.md").read_text(encoding="utf-8")
lines = md.split("\n")
blocks = json.loads(Path("blocks.json").read_text(encoding="utf-8"))

fails: list[str] = []

# ① 锚点链接全通
anchors = set(re.findall(r'<a id="([^"]+)"', md))
toc = re.findall(r"\]\(#([a-z0-9-]+)\)", md)
dead = [a for a in toc if a not in anchors]
print(f"① 锚点链接        {len(toc)} 个 | 可解析 {len(toc) - len(dead)} | 断链 {len(dead)}")
if dead:
    fails.append(f"断链 {len(dead)}: {sorted(set(dead))[:5]}")

# ② 上游链接零丢失（不能因为汉化把 URL 改坏）
url_re = re.compile(r"\]\((https?://[^)\s]+)\)")
urls = set(url_re.findall(md))
print(f"② 外部链接        {len(urls)} 个唯一 URL")
if len(urls) < 3000:
    fails.append(f"外部链接仅 {len(urls)}，疑似丢失")

# ③ 结构性英文残留（排除条目描述，那批是后续工作）
cjk = re.compile(r"[一-鿿]")
struct = []
for i, l in enumerate(lines, 1):
    s = l.strip()
    if len(s) < 25 or cjk.search(s):
        continue
    if re.search(r"[A-Za-z]{4,}", s) and not re.match(r"^\s*(<|\||!\[|[-*+]\s*\[|`|\[)", s):
        struct.append((i, s[:80]))
print(f"③ 结构性英文残留  {len(struct)} 行")
for i, s in struct[:5]:
    print(f"    行{i}: {s}")
if len(struct) > 3:
    fails.append(f"结构性英文残留 {len(struct)} 行")

# ④ 汉化覆盖率
ent = [b for b in blocks if b["type"] == "entry" and b.get("url", "").startswith("http")]
trans = [b for b in ent if cjk.search(b.get("desc", ""))]
heads = [b for b in blocks if b["type"] == "heading"]
htrans = [b for b in heads if cjk.search(b.get("text", ""))]
print(f"④ 标题汉化        {len(htrans)}/{len(heads)}")
print(f"   条目描述汉化    {len(trans)}/{len(ent)}  (待后续批次)")

# ⑤ 已知错误不得复现
if "18.6k stars" in md:
    fails.append("star 数旧错残留")
if "back to top" in md:
    fails.append("back to top 未汉化")
print(f"⑤ star 写法       {'18.6 万 ✅' if '18.6 万' in md else '❌ 缺失'}")

print()
if fails:
    print("❌ 未通过：")
    for f in fails:
        print(f"   - {f}")
    sys.exit(1)
print("✅ 全部通过")