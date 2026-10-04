#!/usr/bin/env python3
"""
上游同步检查 —— 生成「可执行的翻译待办清单」。

⚠️ 设计要点（2026-10-04 修正）
早先版本拿「上游英文」去比「我方中文」，两者永远不相等，
导致每条都被误报为「变更」（3029 条），报告等于没用。

正确逻辑：**上游英文 vs 我方翻译时那会儿的上游英文**（同语言对同语言）。
upstream_snapshot.json 存的就是翻译当时的上游描述，作为比对基准。
译文只用于「展示我方现译」，不参与差异判定。
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
STORE = Path("entry_translations.json")
SNAPSHOT = Path("upstream_snapshot.json")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-go-cn-sync"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def entries_of(md_text: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for b in parse(md_text):
        if b["type"] == "entry" and b.get("url", "").startswith("http"):
            out[b["url"]] = {"name": b.get("name", ""), "desc": b.get("desc", "").strip()}
    return out


def build(upstream_md: str) -> dict:
    up = entries_of(upstream_md)
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8")) if SNAPSHOT.exists() else {}
    store = json.loads(STORE.read_text(encoding="utf-8")) if STORE.exists() else {}

    def translatable(u: str) -> bool:
        return bool(up[u]["desc"])

    # 只看有描述的条目：无描述的（纯链接）不存在翻译需求
    added = sorted(u for u in up if translatable(u) and u not in snap)
    removed = sorted(u for u in snap if u in up and translatable(u))
    # removed 语义修正：快照里有、上游已经删掉的
    removed = sorted(u for u in snap if u not in up)
    changed = sorted(
        u for u in up
        if translatable(u) and u in snap
        and snap[u]["desc"].strip() != up[u]["desc"]
    )

    return {
        "统计": {
            "上游条目总数": len(up),
            "其中有描述_可译": sum(1 for u in up if translatable(u)),
            "已翻译": len(store),
            "新增_待翻译": len(added),
            "变更_待重译": len(changed),
            "删除_待处理": len(removed),
        },
        "明细": {
            "新增": [
                {"name": up[u]["name"], "url": u, "上游英文": up[u]["desc"],
                 "状态": "待翻译" if u not in store else "已有译文待确认"}
                for u in added
            ],
            "变更": [
                {"name": up[u]["name"], "url": u,
                 "上游英文_新": up[u]["desc"],
                 "上游英文_旧": snap[u]["desc"],
                 "我方现译": store.get(u, "(未翻译)"),
                 "状态": "待重译" if u in store else "待翻译"}
                for u in changed
            ],
            "删除": [
                {"name": snap[u].get("name", ""), "url": u,
                 "我方现译": store.get(u, "(未翻译)")}
                for u in removed
            ],
        },
    }


def to_text(r: dict) -> str:
    s = r["统计"]
    L = ["=" * 70, "Awesome-Go-CN 上游同步检查报告", "=" * 70]
    for k, v in s.items():
        L.append(f"{k:<16}: {v}")
    total = s["新增_待翻译"] + s["变更_待重译"] + s["删除_待处理"]
    L.append("")
    if total == 0:
        L.append("✅ 与上游完全一致，无需处理。")
        return "\n".join(L)

    for kind, title in (("新增", "新增 · 待翻译"), ("变更", "变更 · 待重译"), ("删除", "删除 · 待处理")):
        items = r["明细"][kind]
        if not items:
            continue
        L.append(f"── {title} ({len(items)}) " + "─" * 30)
        for it in items:
            L.append(f"[{it['name']}] {it['url']}")
            if kind == "新增":
                L.append(f"    上游英文: {it['上游英文']}")
            elif kind == "变更":
                L.append(f"    上游英文(新): {it['上游英文_新']}")
                L.append(f"    上游英文(旧): {it['上游英文_旧']}")
                L.append(f"    我方现译    : {it['我方现译']}")
            else:
                L.append(f"    我方现译: {it['我方现译']}")
            L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="比对本地的上游 README（不联网）")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    ap.add_argument("--out")
    args = ap.parse_args()

    md = Path(args.file).read_text(encoding="utf-8") if args.file else fetch(UPSTREAM_RAW)
    r = build(md)

    if args.out:
        Path(args.out).write_text(
            json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(r, ensure_ascii=False, indent=1) if args.format == "json" else to_text(r))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())