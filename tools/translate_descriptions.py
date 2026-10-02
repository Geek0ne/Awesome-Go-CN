#!/usr/bin/env python3
"""阶段 A-2：翻译 77 条分类描述（斜体行）。

2026-10-03 用户发现：阶段 A 只汉化了标题，分类标题下方那句斜体英文
（如 _Libraries for building actor-based programs._）仍是英文。
用户原话是「分类标题**及描述**」，这批属于漏译。
"""

import json
from pathlib import Path

TR = {
    "_Special thanks to_": "_特别感谢_",
    "_Libraries for building actor-based programs._": "_用于构建 Actor 模型的库。_",
    "_Libraries for building programs that leverage AI._": "_用于构建 AI 应用的库。_",
    "_Libraries for manipulating audio and music._": "_用于处理音频与音乐的库。_",
    "_Libraries for implementing authentication and authorization._": "_用于实现认证与授权的库。_",
    "_Tools for building blockchains._": "_用于开发区块链的工具。_",
    "_Libraries for building and working with bots._": "_用于开发和运行机器人的库。_",
    "_Libraries and tools help with build automation._": "_有助于构建自动化的库与工具。_",
    "_Libraries for building Console Applications and Console User Interfaces._": "_用于构建控制台应用与终端界面的库。_",
    "_Libraries for building standard or basic Command Line applications._": "_用于构建标准或基础命令行应用的库。_",
    "_Libraries for configuration parsing._": "_用于解析配置文件的库。_",
    "_Tools for help with continuous integration._": "_有助于持续集成的工具。_",
    "_Libraries for preprocessing CSS files._": "_用于预处理 CSS 文件的库。_",
    "_Frameworks for performing ELT / ETL_": "_用于执行 ELT / ETL 的框架_",
    "_Data stores with expiring records, in-memory distributed data stores, or in-memory subsets of file-based databases._": "_支持记录过期、内存分布式数据存储，或文件型数据库内存子集的存储。_",
    "_Libraries for building and using SQL._": "_用于构建和使用 SQL 的库。_",
    "_Libraries for working with dates and times._": "_用于处理日期与时间的库。_",
    "_Packages that help with building Distributed Systems._": "_有助于构建分布式系统的软件包。_",
    "_Tools for updating dynamic DNS records._": "_用于更新动态 DNS 记录的工具。_",
    "_Libraries and tools that implement email creation and sending._": "_实现邮件创建与发送的库与工具。_",
    "_Embedding other languages inside your go code._": "_在 Go 代码中嵌入其他语言。_",
    "_Libraries for handling errors._": "_用于错误处理的库。_",
    "_Libraries for handling files and file systems._": "_用于处理文件与文件系统的库。_",
    "_Packages for accounting and finance._": "_用于会计与金融的软件包。_",
    "_Libraries for working with forms._": "_用于处理表单的库。_",
    "_Packages to support functional programming in Go._": "_支持 Go 函数式编程的软件包。_",
    "_Awesome game development libraries._": "_优秀的游戏开发库。_",
    "_Tools that generate Go code._": "_用于生成 Go 代码的工具。_",
    "_Geographic tools and servers_": "_地理信息工具与服务_",
    "_Tools for compiling Go to other languages and vice-versa._": "_用于 Go 与其他语言互相编译的工具。_",
    "_Tools for managing and working with Goroutines._": "_用于管理和使用 Goroutine 的工具。_",
    "_Libraries for building GUI Applications._": "_用于构建 GUI 应用的库。_",
    "_Toolkits_": "_工具集_",
    "_Interaction_": "_交互_",
    "_Libraries, tools, and tutorials for interacting with hardware._": "_用于与硬件交互的库、工具与教程。_",
    "_Libraries for manipulating images._": "_用于图像处理的库。_",
    "_Libraries for programming devices of the IoT._": "_用于物联网设备编程的库。_",
    "_Libraries for scheduling jobs._": "_用于任务调度的库。_",
    "_Libraries for working with JSON._": "_用于处理 JSON 的库。_",
    "_Libraries for generating and working with log files._": "_用于生成与处理日志文件的库。_",
    "_Libraries for Machine Learning._": "_机器学习相关的库。_",
    "_Libraries that implement messaging systems._": "_实现消息系统的库。_",
    "_Libraries for working with Microsoft Excel._": "_用于处理 Microsoft Excel 的库。_",
    "_Libraries for working with Microsoft Word._": "_用于处理 Microsoft Word 的库。_",
    "_Libraries for working with dependency injection._": "_用于依赖注入的库。_",
    "_**Unofficial** set of patterns for structuring projects._": "_**非官方**的项目结构设计模式集合。_",
    "_Libraries for working with strings._": "_用于字符串处理的库。_",
    "_These libraries were placed here because none of the other categories seemed to fit._": "_这些库放在这里，是因为其他分类似乎都不太合适。_",
    "_Libraries for working with human languages._": "_用于自然语言处理的库。_",
    "_Libraries for working with various layers of the network._": "_用于处理网络各层的库。_",
    "_Libraries for making HTTP requests._": "_用于发起 HTTP 请求的库。_",
    "_Libraries for using OpenGL in Go._": "_在 Go 中使用 OpenGL 的库。_",
    "_Libraries that implement Object-Relational Mapping or datamapping techniques._": "_实现对象关系映射（ORM）或数据映射技术的库。_",
    "_Official tooling for dependency and package management_": "_官方依赖与包管理工具_",
    "_Unofficial libraries for package and dependency management._": "_非官方的包与依赖管理库。_",
    "_Libraries for scientific computing and data analyzing._": "_用于科学计算与数据分析的库。_",
    "_Libraries that are used to help make your application more secure._": "_用于提升应用安全性的库。_",
    "_Libraries and tools for binary serialization._": "_用于二进制序列化的库与工具。_",
    "_Libraries and tools for stream processing and reactive programming._": "_用于流处理与响应式编程的库与工具。_",
    "_Libraries and tools for templating and lexing._": "_用于模板与词法分析的库与工具。_",
    "_Libraries for testing codebases and generating test data._": "_用于测试代码库与生成测试数据的库。_",
    "_Libraries for parsing and manipulating texts._": "_用于解析与处理文本的库。_",
    "_Libraries for accessing third party APIs._": "_用于访问第三方 API 的库。_",
    "_General utilities and tools to make your life easier._": "_让开发更轻松的通用工具与库。_",
    "_Libraries for working with UUIDs._": "_用于处理 UUID 的库。_",
    "_Libraries for validation._": "_用于数据校验的库。_",
    "_Libraries for version control._": "_用于版本控制的库。_",
    "_Libraries for manipulating video._": "_用于视频处理的库。_",
    "_Full stack web frameworks._": "_全栈 Web 框架。_",
    "_Libraries for creating Workflows._": "_用于创建工作流的库。_",
    "_Libraries and tools for manipulating XML._": "_用于处理 XML 的库与工具。_",
    "_Libraries and tools to implement Zero Trust architectures._": "_用于实现零信任架构的库与工具。_",
    "_Source code analysis tools, also known as Static Application Security Testing (SAST) Tools._": "_源代码分析工具，也称静态应用安全测试（SAST）工具。_",
    "_Plugin for text editors and IDEs._": "_面向文本编辑器与 IDE 的插件。_",
    "_Software written in Go._": "_使用 Go 编写的软件。_",
    "_Where to discover new Go libraries._": "_发现新 Go 库的地方。_",
    "_Add the group of your city/country here (send **PR**)_": "_在这里添加你所在城市/国家的分会（请提交 **PR**）_",
}

blocks = json.loads(Path("blocks.json").read_text(encoding="utf-8"))
done = miss = 0
unmatched = []
for b in blocks:
    if b["type"] == "raw":
        t = b["text"].strip()
        if t in TR:
            b["text"] = b["text"].replace(t, TR[t])
            done += 1
        elif t.startswith("_") and t.endswith("_") and len(t) > 6 and any(c.isalpha() and ord(c) < 128 for c in t):
            miss += 1
            unmatched.append(t)

Path("blocks.json").write_text(json.dumps(blocks, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"已翻译分类描述: {done}")
print(f"未匹配        : {miss}")
for t in unmatched[:10]:
    print(f"  ⚠️ {t[:100]}")