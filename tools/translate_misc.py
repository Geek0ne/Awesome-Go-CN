#!/usr/bin/env python3
"""阶段 A-3：杂项汉化 —— 返回顶部链接 + 分类交叉引用句。"""

import json
from pathlib import Path

# 交叉引用句（跨行，已按 blocks 里的实际存储形式匹配）
SEE_ALSO = {
    "See also [Database](#database) for more complex key-value stores, and [Trees](#trees) for additional ordered map implementations.":
        "更复杂的键值存储参见 [数据库](#database)，更多有序 Map 实现参见 [树](#trees)。",
    "See also [Text Processing](#text-processing) and [Text Analysis](#text-analysis).":
        "另见[文本处理](#text-processing)与[文本分析](#text-analysis)。",
    "See also [Natural Language Processing](#natural-language-processing) and [Text Analysis](#text-analysis).":
        "另见[自然语言处理](#natural-language-processing)与[文本分析](#text-analysis)。",
    # 上游这句是硬换行成两行存放的，需分别匹配
    "See also [Database](#database) for more complex key-value stores, and [Trees](#trees) for":
        "更复杂的键值存储参见[数据库](#database)，",
    "additional ordered map implementations.":
        "更多有序 Map 实现参见[树](#trees)。",
}

blocks = json.loads(Path("blocks.json").read_text(encoding="utf-8"))

top = see_done = see_miss = 0
for b in blocks:
    if b["type"] != "raw":
        continue
    if "back to top" in b["text"]:
        b["text"] = b["text"].replace("[⬆ back to top]", "[⬆ 回到顶部]")
        top += 1
    s = b["text"].strip()
    if s in SEE_ALSO:
        b["text"] = b["text"].replace(s, SEE_ALSO[s])
        see_done += 1
    elif s.startswith("See also "):
        see_miss += 1
        print(f"  ⚠️ 未匹配: {s[:100]}")

Path("blocks.json").write_text(json.dumps(blocks, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"已汉化「回到顶部」: {top}")
print(f"已汉化交叉引用句  : {see_done}")
print(f"未匹配交叉引用句  : {see_miss}")