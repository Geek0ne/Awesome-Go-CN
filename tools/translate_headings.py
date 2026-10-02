#!/usr/bin/env python3
"""阶段 A：翻译全部标题，并注入显式锚点钉住 152 个目录链接。"""

import json
import re
from pathlib import Path

TR = {
    # L1
    "Awesome Go": "Awesome Go 中文版",
    "Resources": "相关资源",
    # L2
    "Contents": "目录",
    "Actor Model": "Actor 模型",
    "Artificial Intelligence": "人工智能",
    "Audio and Music": "音频与音乐",
    "Authentication and Authorization": "认证与授权",
    "Blockchain": "区块链",
    "Bot Building": "机器人开发",
    "Build Automation": "构建自动化",
    "Command Line": "命令行",
    "Configuration": "配置",
    "Continuous Integration": "持续集成",
    "CSS Preprocessors": "CSS 预处理器",
    "Data Integration Frameworks": "数据集成框架",
    "Data Structures and Algorithms": "数据结构与算法",
    "Database": "数据库",
    "Database Drivers": "数据库驱动",
    "Date and Time": "日期与时间",
    "Distributed Systems": "分布式系统",
    "Dynamic DNS": "动态 DNS",
    "Email": "邮件",
    "Embeddable Scripting Languages": "可嵌入式脚本语言",
    "Error Handling": "错误处理",
    "File Handling": "文件处理",
    "Financial": "金融",
    "Forms": "表单",
    "Functional": "函数式",
    "Game Development": "游戏开发",
    "Generators": "代码生成器",
    "Geographic": "地理信息",
    "Go Compilers": "Go 编译器",
    "Goroutines": "Goroutine 并发",
    "GUI": "GUI",
    "Hardware": "硬件",
    "Images": "图像处理",
    "IoT (Internet of Things)": "物联网（IoT）",
    "Job Scheduler": "任务调度",
    "JSON": "JSON",
    "Logging": "日志",
    "Machine Learning": "机器学习",
    "Messaging": "消息",
    "Microsoft Office": "Microsoft Office",
    "Miscellaneous": "杂项",
    "Natural Language Processing": "自然语言处理",
    "Networking": "网络",
    "OpenGL": "OpenGL",
    "ORM": "ORM",
    "Package Management": "包管理",
    "Performance": "性能",
    "Query Language": "查询语言",
    "Reflection": "反射",
    "Resource Embedding": "资源嵌入",
    "Science and Data Analysis": "科学与数据分析",
    "Security": "安全",
    "Serialization": "序列化",
    "Server Applications": "服务器应用",
    "Stream Processing": "流处理",
    "Template Engines": "模板引擎",
    "Testing": "测试",
    "Text Processing": "文本处理",
    "Third-party APIs": "第三方 API",
    "Utilities": "工具",
    "UUID": "UUID",
    "Validation": "数据校验",
    "Version Control": "版本控制",
    "Video": "视频",
    "Web Frameworks": "Web 框架",
    "WebAssembly": "WebAssembly",
    "Webhooks Server": "Webhook 服务",
    "Windows": "Windows",
    "Workflow Frameworks": "工作流框架",
    "XML": "XML",
    "Zero Trust": "零信任",
    "Code Analysis": "代码分析",
    "Editor Plugins": "编辑器插件",
    "Go Generate Tools": "Go Generate 工具",
    "Go Tools": "Go 工具",
    "Software Packages": "软件包",
    "Benchmarks": "性能基准测试",
    "Conferences": "会议",
    "E-Books": "电子书",
    "Gophers": "Gopher 社区",
    "Meetups": "Meetup 聚会",
    "Style Guides": "风格指南",
    "Social Media": "社交媒体",
    "Websites": "网站",
    "Contribution": "贡献指南",
    "License": "许可证",
    # L3
    "Advanced Console UIs": "高级终端界面",
    "Standard CLI": "标准命令行工具",
    "Bit-packing and Compression": "位打包与压缩",
    "Bit Sets": "位集合",
    "Bloom and Cuckoo Filters": "布隆过滤器与布谷鸟过滤器",
    "Data Structure and Algorithm Collections": "数据结构与算法合集",
    "Iterators": "迭代器",
    "Maps": "映射",
    "Miscellaneous Data Structures and Algorithms": "其他数据结构与算法",
    "Nullable Types": "可空类型",
    "Queues": "队列",
    "Sets": "集合",
    "Text Analysis": "文本分析",
    "Trees": "树",
    "Pipes": "管道",
    "Caches": "缓存",
    "Databases Implemented in Go": "用 Go 实现的数据库",
    "Database Schema Migration": "数据库模式迁移",
    "Database Tools": "数据库工具",
    "SQL Query Builders": "SQL 查询构造器",
    "Interfaces to Multiple Backends": "多后端接口",
    "Relational Database Drivers": "关系型数据库驱动",
    "NoSQL Database Drivers": "NoSQL 数据库驱动",
    "Search and Analytic Databases": "搜索与分析型数据库",
    "Microsoft Excel": "Microsoft Excel",
    "Microsoft Word": "Microsoft Word",
    "Dependency Injection": "依赖注入",
    "Project Layout": "项目结构布局",
    "Strings": "字符串",
    "Uncategorized": "未分类",
    "Language Detection": "语言检测",
    "Morphological Analyzers": "形态分析器",
    "Slugifiers": "Slug 生成器",
    "Tokenizers": "分词器",
    "Translation": "翻译",
    "Transliteration": "音译",
    "HTTP Clients": "HTTP 客户端",
    "Testing Frameworks": "测试框架",
    "Mock": "Mock",
    "Fuzzing and delta-debugging/reducing/shrinking": "模糊测试与增量调试/缩减/收缩",
    "Selenium and browser control tools": "Selenium 与浏览器控制工具",
    "Fail injection": "故障注入",
    "Formatters": "格式化工具",
    "Markup Languages": "标记语言",
    "Parsers/Encoders/Decoders": "解析器/编码器/解码器",
    "Regular Expressions": "正则表达式",
    "Sanitation": "数据清洗",
    "Scrapers": "爬虫",
    "RSS": "RSS",
    "Utility/Miscellaneous": "实用工具/杂项",
    "Middlewares": "中间件",
    "Routers": "路由器",
    "DevOps Tools": "DevOps 工具",
    "Other Software": "其他软件",
    "E-books for purchase": "付费电子书",
    "Free e-books": "免费电子书",
    "Twitter": "Twitter",
    "Reddit": "Reddit",
    "Tutorials": "教程",
    "Guided Learning": "引导式学习",
    # L4
    "Actual middlewares": "实际中间件",
    "Libraries for creating HTTP middlewares": "用于编写 HTTP 中间件的库",
}

# 目录里非标题但也要汉化的短句
RAW_TR = {
    "<summary>Expand contents</summary>": "<summary>展开目录</summary>",
}

_PUNCT = re.compile(r"[^\w\s-]", re.UNICODE)
_SPACE = re.compile(r"[\s]+")


def gh_slug(t: str) -> str:
    s = t.strip().lower().replace("`", "")
    s = _PUNCT.sub("", s)
    return _SPACE.sub("-", s).strip("-")


blocks = json.loads(Path("blocks.json").read_text(encoding="utf-8"))

translated = untranslated = 0
out: list[dict] = []

for b in blocks:
    if b["type"] == "heading":
        en = b["text"]
        zh = TR.get(en)
        if zh:
            slug = gh_slug(en)
            # 钉锚点：标题文字改了，但锚点仍是英文 slug，目录 152 链接照常可用
            b["anchor"] = slug
            b["text"] = zh
            translated += 1
        else:
            untranslated += 1
            print(f"  ⚠️ 未翻译标题: {en!r}")
    elif b["type"] == "raw" and b["text"] in RAW_TR:
        b["text"] = RAW_TR[b["text"]]
        translated += 1
    out.append(b)

Path("blocks.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"已翻译标题/文本: {translated}")
print(f"未翻译        : {untranslated}")
print(f"已钉锚点      : {sum(1 for b in out if b.get('anchor'))}")