#!/usr/bin/env python3
"""
条目描述翻译的持久层 + 批次导出。

背景：build.sh 每次都从上游原始 README 重新解析生成 blocks.json。
若把译文直接写进 blocks.json，下次构建就会被抹掉。
因此译文必须存在**独立文件** entry_translations.json 里，由管道套用。

以 url 作为键：它在多次重新解析之间保持稳定。
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STORE = Path("entry_translations.json")


def load_store() -> dict[str, str]:
    if STORE.exists():
        return json.loads(STORE.read_text(encoding="utf-8"))
    return {}


def save_store(d: dict[str, str]) -> None:
    STORE.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "export"
    blocks = json.loads(Path("blocks.json").read_text(encoding="utf-8"))
    store = load_store()
    cjk = re.compile(r"[一-鿿]")

    # 待译条目：有描述、尚未含中文、且有真实外部链接
    todo = [
        b for b in blocks
        if b["type"] == "entry"
        and b.get("url", "").startswith("http")
        and b.get("desc", "").strip()
        and not cjk.search(b["desc"])
        and b["url"] not in store
    ]

    if mode == "export":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 250
        batch = todo[:n]
        out = [{"url": b["url"], "desc": b["desc"]} for b in batch]
        Path("batch_in.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"待译总数  : {len(todo)}")
        print(f"本批导出  : {len(batch)}")
        print(f"已存译文  : {len(store)}")
        print(f"批次文件  : batch_in.json")
        if batch:
            print(f"\n首条样例: {batch[0]['desc'][:100]}")
        return 0

    if mode == "apply":
        # batch_out.json: [{"url":..., "zh":...}]
        applied = skipped = 0
        for item in json.loads(Path("batch_out.json").read_text(encoding="utf-8")):
            u, zh = item.get("url"), (item.get("zh") or "").strip()
            if not u or not zh:
                skipped += 1
                continue
            if u in store:
                skipped += 1
                continue
            store[u] = zh
            applied += 1
        save_store(store)
        print(f"新存入译文: {applied}")
        print(f"跳过      : {skipped}")
        print(f"译文库总计: {len(store)}")
        return 0

    if mode == "render":
        # 把译文库套用到 blocks.json —— 这是管道里真正“生效”的一步
        n = 0
        for b in blocks:
            if b["type"] == "entry":
                zh = store.get(b.get("url", ""))
                if zh and zh != b.get("desc", ""):
                    b["desc"] = zh
                    n += 1
        Path("blocks.json").write_text(
            json.dumps(blocks, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"已套用译文: {n} 条")
        return 0

    if mode == "status":
        allent = [b for b in blocks
                  if b["type"] == "entry" and b.get("url", "").startswith("http")
                  and b.get("desc", "").strip()]
        done = len([b for b in allent if b["url"] in store])
        print(f"有描述条目 : {len(allent)}")
        print(f"已翻译     : {done}  ({done*100/max(len(allent),1):.1f}%)")
        print(f"剩余       : {len(allent)-done}")
        return 0

    print("用法: entry_store.py [export N | apply | render | status]")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())