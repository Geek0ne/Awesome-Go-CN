#!/usr/bin/env python3
"""
把 upstream_snapshot.json 更新为当前上游状态。

何时该跑：当你处理完 sync_check 报出的「新增」与「变更」，并把译文
写入 entry_translations.json 之后。快照是下一次比对的基准，不更新的话
下次仍会重复报同一批差异。

用法：
  python3 tools/update_snapshot.py            # 拉取最新上游并更新快照
  python3 tools/update_snapshot.py --file md  # 用本地 README 更新
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from parse import parse  # noqa: E402

UPSTREAM_RAW = "https://raw.githubusercontent.com/avelino/awesome-go/main/README.md"
SNAPSHOT = Path("upstream_snapshot.json")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-go-cn-sync"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--dry-run", action="store_true", help="只显示统计，不写文件")
    args = ap.parse_args()

    md = Path(args.file).read_text(encoding="utf-8") if args.file else fetch(UPSTREAM_RAW)

    snap: dict[str, dict] = {}
    for b in parse(md):
        if b["type"] == "entry" and b.get("url", "").startswith("http"):
            snap[b["url"]] = {"name": b.get("name", ""), "desc": b.get("desc", "")}

    old = json.loads(SNAPSHOT.read_text(encoding="utf-8")) if SNAPSHOT.exists() else {}
    added = len(set(snap) - set(old))
    removed = len(set(old) - set(snap))

    print(f"快照条目: {len(old)} → {len(snap)}")
    print(f"新增 {added} / 移除 {removed}")

    if args.dry_run:
        print("(dry-run，未写入)")
        return 0

    SNAPSHOT.write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    store = Path("entry_translations.json")
    n_tr = len(json.loads(store.read_text(encoding="utf-8"))) if store.exists() else 0
    untranslated = [u for u, v in snap.items() if v["desc"].strip() and u not in json.loads(
        store.read_text(encoding="utf-8"))] if store.exists() else []
    print(f"已写入 {SNAPSHOT}")
    if untranslated:
        print(f"⚠️ 仍有 {len(untranslated)} 条有描述的条目未翻译，建议先处理再更新快照")
    print(f"译文库当前 {n_tr} 条")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())