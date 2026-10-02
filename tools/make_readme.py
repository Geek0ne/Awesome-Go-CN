#!/usr/bin/env python3
"""
生成 Awesome-Go-CN 的 README。

只替换上游的英文头部（徽章、赞助商表格、英文介绍），
从「## 目录」开始的内容原样保留 —— 那里有 151 个锚点链接，动不得。
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, "tools")
from parse import render  # noqa: E402

HEADER = """<a id="awesome-go"></a>
# Awesome Go 中文版

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Last Commit](https://img.shields.io/github/last-commit/avelino/awesome-go)](https://github.com/avelino/awesome-go/commits/main)

> **[Awesome Go](https://github.com/avelino/awesome-go) 的中文汉化版本** ——
> 收录 Go 生态中优秀的库、框架与工具，共 **87 个分类、3000+ 条目**。

## 关于本项目

这是对上游项目 [avelino/awesome-go](https://github.com/avelino/awesome-go)（18.6k stars）的**中文翻译版本**。

- **分类标题、条目描述已汉化**为中文，**库名、框架名、命令、字段等专有名词保持英文原样**，方便检索与对照
- 每条目的**链接均指向原项目地址**，功能与上游完全一致
- 持续跟踪上游更新，上游新增或修改的条目会陆续翻译同步

## 快速导航

- 按分类浏览：见下方[目录](#contents)
- 按热度浏览：见上游的 [Star History](https://star-history.com/#avelino/awesome-go)
- 贡献新条目：请遵循上游的[贡献指南](#contribution)

## 致谢与许可

本项目内容翻译自 [avelino/awesome-go](https://github.com/avelino/awesome-go)，原作者 **Thiago Avelino**。

上游项目采用 [MIT 许可证](https://github.com/avelino/awesome-go/blob/main/LICENSE)。本中文翻译版本沿用同一许可协议，版权归原作者所有。

如发现翻译有误或有更好的译法，欢迎提交 PR。

---

"""

blocks = json.loads(Path("blocks.json").read_text(encoding="utf-8"))

# 找到「目录」标题的块索引，从它开始保留
start = next(
    i for i, b in enumerate(blocks)
    if b["type"] == "heading" and b["text"] == "目录"
)
body_blocks = blocks[start:]
body = render(body_blocks, anchors=True)

# 目录标题本身也钉锚点，保持 #contents 可跳转
body = body.replace("## 目录", '<a id="contents"></a>\n## 目录', 1)

out = HEADER + body
Path("README.md").write_text(out, encoding="utf-8")

print(f"README.md 生成完成")
print(f"  总字符   : {len(out):,}")
print(f"  总行数   : {out.count(chr(10)) + 1:,}")
print(f"  头部替换 : 前 {start} 块（上游英文头部）")
print(f"  目录保留 : 从第 {start} 块起，含 {sum(1 for b in body_blocks if b.get('anchor'))} 个锚点")