<a id="awesome-go"></a>
# Awesome Go 中文版

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Last Commit](https://img.shields.io/github/last-commit/avelino/awesome-go)](https://github.com/avelino/awesome-go/commits/main)

> **[Awesome Go](https://github.com/avelino/awesome-go) 的中文汉化版本** ——
> 收录 Go 生态中优秀的库、框架与工具，共 **87 个分类、3200+ 条目**。

## 关于本项目

这是对上游项目 [avelino/awesome-go](https://github.com/avelino/awesome-go)（**18.6 万 stars**）的**中文翻译版本**。

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

<a id="contents"></a>
<a id="contents"></a>
## 目录

<details>
<summary>展开目录</summary>

- [Awesome Go 中文版](#awesome-go)
  - [目录](#contents)
  - [Actor 模型](#actor-model)
  - [人工智能](#artificial-intelligence)
  - [音频与音乐](#audio-and-music)
  - [认证与授权](#authentication-and-authorization)
  - [区块链](#blockchain)
  - [机器人开发](#bot-building)
  - [构建自动化](#build-automation)
  - [命令行](#command-line)
    - [高级终端界面](#advanced-console-uis)
    - [标准命令行工具](#standard-cli)
  - [配置](#configuration)
  - [持续集成](#continuous-integration)
  - [CSS 预处理器](#css-preprocessors)
  - [数据集成框架](#data-integration-frameworks)
  - [数据结构与算法](#data-structures-and-algorithms)
    - [位打包与压缩](#bit-packing-and-compression)
    - [位集合](#bit-sets)
    - [布隆过滤器与布谷鸟过滤器](#bloom-and-cuckoo-filters)
    - [数据结构与算法合集](#data-structure-and-algorithm-collections)
    - [迭代器](#iterators)
    - [映射](#maps)
    - [其他数据结构与算法](#miscellaneous-data-structures-and-algorithms)
    - [可空类型](#nullable-types)
    - [队列](#queues)
    - [集合](#sets)
    - [文本分析](#text-analysis)
    - [树](#trees)
    - [管道](#pipes)
  - [数据库](#database)
    - [缓存](#caches)
    - [用 Go 实现的数据库](#databases-implemented-in-go)
    - [数据库模式迁移](#database-schema-migration)
    - [数据库工具](#database-tools)
    - [SQL 查询构造器](#sql-query-builders)
  - [数据库驱动](#database-drivers)
    - [多后端接口](#interfaces-to-multiple-backends)
    - [关系型数据库驱动](#relational-database-drivers)
    - [NoSQL 数据库驱动](#nosql-database-drivers)
    - [搜索与分析型数据库](#search-and-analytic-databases)
  - [日期与时间](#date-and-time)
  - [分布式系统](#distributed-systems)
  - [动态 DNS](#dynamic-dns)
  - [邮件](#email)
  - [可嵌入式脚本语言](#embeddable-scripting-languages)
  - [错误处理](#error-handling)
  - [文件处理](#file-handling)
  - [金融](#financial)
  - [表单](#forms)
  - [函数式](#functional)
  - [游戏开发](#game-development)
  - [代码生成器](#generators)
  - [地理信息](#geographic)
  - [Go 编译器](#go-compilers)
  - [Goroutine 并发](#goroutines)
  - [GUI](#gui)
  - [硬件](#hardware)
  - [图像处理](#images)
  - [物联网（IoT）](#iot-internet-of-things)
  - [任务调度](#job-scheduler)
  - [JSON](#json)
  - [日志](#logging)
  - [机器学习](#machine-learning)
  - [消息](#messaging)
  - [Microsoft Office](#microsoft-office)
    - [Microsoft Excel](#microsoft-excel)
    - [Microsoft Word](#microsoft-word)
  - [杂项](#miscellaneous)
    - [依赖注入](#dependency-injection)
    - [项目结构布局](#project-layout)
    - [字符串](#strings)
    - [未分类](#uncategorized)
  - [自然语言处理](#natural-language-processing)
    - [语言检测](#language-detection)
    - [形态分析器](#morphological-analyzers)
    - [Slug 生成器](#slugifiers)
    - [分词器](#tokenizers)
    - [翻译](#translation)
    - [音译](#transliteration)
  - [网络](#networking)
    - [HTTP 客户端](#http-clients)
  - [OpenGL](#opengl)
  - [ORM](#orm)
  - [包管理](#package-management)
  - [性能](#performance)
  - [查询语言](#query-language)
  - [反射](#reflection)
  - [资源嵌入](#resource-embedding)
  - [科学与数据分析](#science-and-data-analysis)
  - [安全](#security)
  - [序列化](#serialization)
  - [服务器应用](#server-applications)
  - [流处理](#stream-processing)
  - [模板引擎](#template-engines)
  - [测试](#testing)
    - [测试框架](#testing-frameworks)
    - [Mock](#mock)
    - [模糊测试与增量调试/缩减/收缩](#fuzzing-and-delta-debuggingreducingshrinking)
    - [Selenium 与浏览器控制工具](#selenium-and-browser-control-tools)
    - [故障注入](#fail-injection)
  - [文本处理](#text-processing)
    - [格式化工具](#formatters)
    - [标记语言](#markup-languages)
    - [解析器/编码器/解码器](#parsersencodersdecoders)
    - [正则表达式](#regular-expressions)
    - [数据清洗](#sanitation)
    - [爬虫](#scrapers)
    - [RSS](#rss)
    - [实用工具/杂项](#utilitymiscellaneous)
  - [第三方 API](#third-party-apis)
  - [工具](#utilities)
  - [UUID](#uuid)
  - [数据校验](#validation)
  - [版本控制](#version-control)
  - [视频](#video)
  - [Web 框架](#web-frameworks)
    - [中间件](#middlewares)
      - [实际中间件](#actual-middlewares)
      - [用于编写 HTTP 中间件的库](#libraries-for-creating-http-middlewares)
    - [路由器](#routers)
  - [WebAssembly](#webassembly)
  - [Webhook 服务](#webhooks-server)
  - [Windows](#windows)
  - [工作流框架](#workflow-frameworks)
  - [XML](#xml)
  - [零信任](#zero-trust)
  - [代码分析](#code-analysis)
  - [编辑器插件](#editor-plugins)
  - [Go Generate 工具](#go-generate-tools)
  - [Go 工具](#go-tools)
  - [软件包](#software-packages)
    - [DevOps 工具](#devops-tools)
    - [其他软件](#other-software)
- [相关资源](#resources)
  - [性能基准测试](#benchmarks)
  - [会议](#conferences)
  - [电子书](#e-books)
    - [付费电子书](#e-books-for-purchase)
    - [免费电子书](#free-e-books)
  - [Gopher 社区](#gophers)
  - [Meetup 聚会](#meetups)
  - [风格指南](#style-guides)
  - [社交媒体](#social-media)
    - [Twitter](#twitter)
    - [Reddit](#reddit)
  - [网站](#websites)
    - [教程](#tutorials)
    - [引导式学习](#guided-learning)
  - [贡献指南](#contribution)
  - [许可证](#license)

**[⬆ 回到顶部](#contents)**



</details>

<a id="actor-model"></a>
## Actor 模型

_用于构建 Actor 模型的库。_

- [asyncmachine-go/pkg/machine](https://github.com/pancsta/asyncmachine-go/tree/main/pkg/machine) - 图控制流库（支持 AOP、Actor、状态机）。
- [Ergo](https://github.com/ergo-services/ergo) - 基于 Actor 的框架，具备网络透明性，用于在 Golang 中构建事件驱动架构。灵感源自 Erlang。
- [Goakt](https://github.com/Tochemey/goakt) - 高性能分布式 Actor 框架，为 Golang 提供基于 Protocol Buffers 的消息传递。
- [Hollywood](https://github.com/anthdm/hollywood) - 用 Golang 编写的极速轻量级 Actor 引擎。
- [ProtoActor](https://github.com/asynkron/protoactor-go) - 面向 Go、C# 以及 Java/Kotlin 的分布式 Actor 库。

**[⬆ 回到顶部](#contents)**

<a id="artificial-intelligence"></a>
## 人工智能

_用于构建 AI 应用的库。_

- [AegisFlow](https://github.com/saivedant169/AegisFlow) - AI 网关，面向 10+ 服务商统一路由、加固与监控 LLM 流量。兼容 OpenAI API，支持 WASM 策略插件、金丝雀发布与实时仪表盘。
- [Aetheris](https://github.com/Colin4k1024/Aetheris) - AI Agent 执行运行时，支持事件溯源、检查点恢复，并提供 At-Most-Once 执行保证。以 Go 编写。
- [agent-sdk-go](https://github.com/agenticenv/agent-sdk-go) - 用于在 Go 中构建有状态 AI 智能体的框架。
- [agy-mcp](https://github.com/tphakala/agy-mcp) - Model Context Protocol（MCP）服务器，封装 Antigravity CLI 以运行提示词与同行评审。
- [ai](https://github.com/joakimcarlsson/ai) - Go 工具集，用于跨多家服务商构建 AI 智能体与应用，统一提供 LLM、嵌入、工具调用与 MCP 集成。
- [ai-gateway](https://github.com/ferro-labs/ai-gateway) - 兼容 OpenAI 的 LLM 网关，在 30 家服务商之间路由请求，支持降级、限流、预算、护栏与可观测性。
- [chromem-go](https://github.com/philippgille/chromem-go) - 面向 Go 的可嵌入式向量数据库，接口类似 Chroma，且零第三方依赖。内存存储，可选持久化。
- [claude-code-go](https://github.com/lancekrogers/claude-code-go) - Go 库，可从 Go 程序中以非交互方式驱动 Claude Code CLI 的提示词接口。
- [crewai-go](https://github.com/rhgs/crewai-go) - CrewAI 的惯用 Go 移植版（多智能体编排）。零依赖，仅用标准库。
- [Cynative](https://github.com/cynative/cynative) - 用于在 Go 中构建安全工程 AI 智能体的框架。默认只读、内置沙箱，并提供面向 AWS、GCP、Azure、K8s、GitHub 与 GitLab 深度调研的 45 个智能体蓝图。
- [dakera-go](https://github.com/dakera-ai/dakera-go) - Dakera 自托管智能体记忆服务器的官方 Go 客户端 SDK，为记忆存取、会话管理、命名空间操作与衰减配置提供类型化接口。
- [fun](https://gitlab.com/tozd/go/fun) - 在 Go 中使用大语言模型（LLM）最简单却强大的方式。
- [goai](https://github.com/zendev-sh/goai) - 用于构建 AI 应用的 Go SDK。一个 SDK 接入 20+ 服务商。灵感源自 Vercel AI SDK。
- [GoModel](https://github.com/ENTERPILOT/GoModel) - AI 网关，为 OpenAI、Anthropic、Gemini、Groq、xAI、Ollama 等服务商提供统一的 OpenAI 兼容 API，并支持路由、用量追踪、限流与护栏。
- [hotplex](https://github.com/hrygo/hotplex) - AI Agent 运行时引擎，为 Claude Code、OpenCode、pi-mono 等 CLI AI 工具提供长生命周期会话。支持全双工流式输出、多平台集成与安全沙箱。
- [jargo](https://github.com/gojargo/jargo) - 用于在 WebRTC 之上构建实时语音 AI 智能体的框架，将语音转文本、LLM 与文本转语音串联成流式管线。
- [keen-code](https://github.com/mochow13/keen-code) - 上下文高效的终端 AI 编码智能体。与服务商无关，支持 MCP、Agent Skills、子智能体等，并内置简洁直观的 TUI。
- [langchaingo](https://github.com/tmc/langchaingo) - LangChainGo 是一个用于开发语言模型驱动应用的框架。
- [langgraphgo](https://github.com/smallnest/langgraphgo) - 用于在 LLM 之上构建有状态多 Actor 应用的 Go 库，基于 LangGraph 理念，内置大量开箱即用的 Agent 架构。
- [llm-box](https://github.com/alib8b8/llm-box) - 终端 AI 工作流引擎，采用 YAML 驱动管线，支持 20+ LLM 服务商（DeepSeek、Qwen、GLM、Mistral 等），并提供工作流管理 TUI。
- [LocalAI](https://github.com/mudler/LocalAI) - 开源的 OpenAI 替代方案，可自托管 AI 模型。
- [localaik](https://github.com/harshaneel/localaik) - 以 LocalStack 风格在本地模拟 OpenAI 与 Gemini API；单个 Docker 容器，基于 llama.cpp + Gemma 3 后端。
- [mcp-go](https://github.com/mark3labs/mcp-go) - Model Context Protocol 的 Go 实现，用于在 Go 中构建 MCP 服务器与客户端。
- [Ollama](https://github.com/jmorganca/ollama) - 在本地运行大语言模型。
- [OllamaFarm](https://github.com/presbrey/ollamafarm) - 管理、负载均衡与故障转移 Ollama 实例组。
- [otellix](https://github.com/oluwajubelo1/otellix) - OpenTelemetry 原生的 LLM 可观测性与预算护栏，面向成本受限的生产环境。
- [routex](https://github.com/Ad3bay0c/routex) - 面向 Go 的 YAML 驱动多智能体 AI 运行时，具备 Erlang 风格的监督机制，支持 MCP 工具服务器并附带 CLI。
- [semantic-search](https://github.com/DavidBelicza/semantic-search) - 基于语义的搜索，支持 PDF、Markdown、DOCX、源代码等文件类型，利用生成式 AI 嵌入模型将文件向量化后存入向量数据库。
- [skillreaper](https://github.com/thousandflowers/skillreaper) - 命令行工具，扫描 AI 智能体会话记录，识别并安全隔离在 Claude Code、Codex CLI、Hermes、OpenCode、Cursor 与 OpenClaw 中未被使用的技能、MCP 服务器与智能体。
- [Smeldr](https://github.com/Smeldr/core) - AI 原生内容后端，具备类型化生命周期管理、为每种内容类型提供原生 MCP 工具，且零运行时依赖。
- [snip](https://github.com/edouard-claude/snip) - 命令行代理，通过声明式 YAML 过滤器将 LLM token 用量降低 60-90%。可直接用于 Claude Code、Cursor、Copilot 与 Gemini，是 Go 语言版的 rtk 替代方案。
- [thermal](https://github.com/jadmadi/thermal) - 面向 AI 编码助手的终端贡献热力图、连续打卡追踪与 token 排行榜。
- [trpc-agent-go](https://github.com/trpc-group/trpc-agent-go) - 用于构建基于 LLM 的多智能体系统的框架。
- [web-researcher-mcp](https://github.com/zoharbabin/web-researcher-mcp) - MCP 服务器，为 AI 助手提供网页搜索、内容抽取与多源调研能力。单一二进制文件，内置 5 家搜索服务商与熔断故障转移、4 级抓取管线。
- [zenflow](https://github.com/zendev-sh/zenflow) - 多智能体编排与工作流引擎。声明式 YAML 工作流，带中心辐射式邮箱的 LLM 协调器，以及竞态安全投递。仅需一个 YAML 文件、一个 Go 二进制，可在任意受 goai 支持的服务商上运行。

**[⬆ 回到顶部](#contents)**

<a id="audio-and-music"></a>
## 音频与音乐

_用于处理音频与音乐的库。_

- [beep](https://github.com/gopxl/beep) - 用于音频播放与音频处理的简单库。
- [flac](https://github.com/mewkiz/flac) - 原生 Go 实现的 FLAC 编码器/解码器，支持 FLAC 流。
- [gaad](https://github.com/Comcast/gaad) - 原生 Go AAC 比特流解析器。
- [go-aac](https://github.com/tphakala/go-aac) - 纯 Go 实现的 AAC-LC 编码器与解码器，移植自 FFmpeg。
- [go-audio-resampler](https://github.com/tphakala/go-audio-resampler) - 纯 Go 高品质音频重采样器，具备 SIMD 加速。
- [go-flac](https://github.com/tphakala/go-flac) - 原生 Go FLAC 编码器与解码器，具备 SIMD 加速。
- [go-mpris](https://github.com/leberKleber/go-mpris) - 用于访问 mpris dbus 接口的客户端。
- [go-opus](https://github.com/tphakala/go-opus) - Opus 音频编解码器（RFC 6716）的原生 Go 实现，解码器符合 RFC 规范。
- [go-resample](https://github.com/gojargo/go-resample) - 纯 Go（无 cgo）音频采样率转换器，支持 sinc、线性与零阶保持转换器。
- [go-wav](https://github.com/tphakala/go-wav) - 纯 Go 的 WAV/RIFF 读写器，支持 RF64 与 BW64，可处理超过 4 GiB 的文件。
- [GoAudio](https://github.com/DylanMeeus/GoAudio) - 原生 Go 音频处理库。
- [gocue](https://github.com/iSerganov/gocue) - 音频分析命令行工具，可检测 cue-in、cue-out 与 overlay 点，并测量 EBU R128 响度，输出 JSON 供 Liquidsoap 使用。
- [gosamplerate](https://github.com/dh1tw/gosamplerate) - libsamplerate 的 Go 绑定。
- [id3v2](https://github.com/bogem/id3v2) - 面向 Go 的 ID3 解码与编码库。
- [malgo](https://github.com/gen2brain/malgo) - 迷你音频库。
- [minimp3](https://github.com/tosone/minimp3) - 轻量级 MP3 解码库。
- [music-theory](https://github.com/go-music-theory/music-theory) - 用 Go 实现的乐理模型。
- [Oto](https://github.com/hajimehoshi/oto) - 用于在多平台播放声音的底层库。
- [PortAudio](https://github.com/gordonklaus/portaudio) - PortAudio 音频 I/O 库的 Go 绑定。
-[voxrai-ai](https://github.com/Voxray-AI/Voxray) - AI voice agents with a JSON configuration,  STT → LLM → TTS pipelines over WebSocket and WebRTC 

**[⬆ 回到顶部](#contents)**

<a id="authentication-and-authorization"></a>
## 认证与授权

_用于实现认证与授权的库。_

- [authboss](https://github.com/volatiletech/authboss) - 面向 Web 的模块化认证系统。它尽可能剔除样板代码与「困难问题」，这样每次在 Go 中开启新的 Web 项目时，只需接入、配置即可开始开发应用，而不必每次都重新构建一套认证系统。
- [authgate](https://github.com/go-authgate/authgate) - 轻量级 OAuth 2.0 授权服务器，支持设备授权许可（[RFC 8628](https://datatracker.ietf.org/doc/html/rfc8628)）、带 PKCE 的授权码流程（[RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) + [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)），以及用于机器对机器认证的客户端凭据模式。
- [branca](https://github.com/essentialkaos/branca) - 面向 Golang 1.15+ 的 branca 令牌[规范实现](https://github.com/tuupola/branca-spec)。
- [casbin](https://github.com/hsluoyz/casbin) - 授权库，支持 ACL、RBAC、ABAC 等访问控制模型。
- [cookiestxt](https://github.com/mengzhuo/cookiestxt) - 提供 cookies.txt 文件格式的解析器。
- [go-githubauth](https://github.com/jferrl/go-githubauth) - GitHub 认证工具：生成并使用 GitHub 应用令牌与安装令牌。
- [go-guardian](https://github.com/shaj13/go-guardian) - Go-Guardian 是一个 Go 库，以简单、干净、惯用的方式实现强大的现代 API 与 Web 认证，支持 LDAP、Basic、Bearer 令牌与证书认证。
- [go-iam](https://github.com/melvinodsa/go-iam) - 开发者优先的身份与访问管理系统，界面简洁。
- [go-jose](https://github.com/go-jose/go-jose) - 相当完整地实现了 JOSE 工作组的 JSON Web Token、JSON Web Signatures 与 JSON Web Encryption 规范。
- [go-jwt](https://github.com/deatil/go-jwt) - 面向 Go 的 JWT（JSON Web Token）库。
- [go-jwt](https://github.com/pardnchiu/go-jwt) - JWT 认证包，提供访问令牌与刷新令牌，附带指纹识别、Redis 存储与自动刷新能力。
- [goiabada](https://github.com/leodip/goiabada) - 支持 OAuth2 与 OpenID Connect 的开源认证与授权服务器。
- [gologin](https://github.com/dghubble/gologin) - 可通过链式调用的处理器，使用 OAuth1 与 OAuth2 认证服务商完成登录。
- [gorbac](https://github.com/mikespook/gorbac) - 在 Golang 中提供轻量级基于角色的访问控制（RBAC）实现。
- [gosession](https://github.com/Kwynto/gosession) - 这是 GoLang 中用于 net/http 的快速会话实现。这个包或许是会话机制最好的实现，至少它在努力成为最好的那个。
- [goth](https://github.com/markbates/goth) - 以简单、干净、惯用的方式使用 OAuth 与 OAuth2，开箱即支持多家服务商。
- [jeff](https://github.com/abraithwaite/jeff) - 简单、灵活、安全、惯用的 Web 会话管理，后端可插拔。
- [jwt](https://github.com/pascaldekloe/jwt) - 轻量级 JSON Web Token（JWT）库。
- [jwt](https://github.com/cristalhq/jwt) - 安全、简单、快速的 Go 版 JSON Web Token。
- [jwt-auth](https://github.com/adam-hanna/jwt-auth) - 面向 Golang HTTP 服务器的 JWT 中间件，提供丰富的配置选项。
- [jwt-go](https://github.com/golang-jwt/jwt) - 功能完备的 JSON Web Token（JWT）实现。该库同时支持 JWT 的解析与校验，以及生成与签名。
- [jwx](https://github.com/lestrrat-go/jwx) - Go 模块，实现多种 JWx（JWA/JWE/JWK/JWS/JWT，即 JOSE）技术。
- [keto](https://github.com/ory/keto) - 「Zanzibar：Google 全球一致的权限系统」的开源（Go）实现。内置 gRPC、REST API、newSQL，以及一套易用且粒度精细的权限语言。支持 ACL、RBAC 及其他访问模型。
- [loginsrv](https://github.com/tarent/loginsrv) - JWT 登录微服务，支持 OAuth2（Github）、htpasswd、osiam 等可插拔后端。
- [melange](https://github.com/pthm/melange) - 将 OpenFGA 授权 schema 编译为 PL/pgSQL 函数，在 PostgreSQL 内部执行细粒度的基于关系的访问控制检查。
- [oauth2](https://github.com/golang/oauth2) - goauth2 的继任者。通用 OAuth 2.0 包，内置 JWT、Google APIs、Compute Engine 与 App Engine 支持。
- [oidc](https://github.com/zitadel/oidc) - 易用的 OpenID Connect 客户端与服务器库，为 Go 编写并获 OpenID 基金会认证。
- [openfga](https://github.com/openfga/openfga) - 基于「Zanzibar：Google 全球一致的权限系统」论文的细粒度授权实现。由 [CNCF](https://www.cncf.io/) 背书。
- [osin](https://github.com/openshift/osin) - Golang OAuth2 服务器库。
- [otpgen](https://github.com/grijul/otpgen) - 用于生成 TOTP/HOTP 验证码的库。
- [otpgo](https://github.com/jltorresm/otpgo) - 面向 Go 的基于时间一次性密码（TOTP）与基于 HMAC 一次性密码（HOTP）库。
- [paseto](https://github.com/o1egl/paseto) - 平台无关安全令牌（PASETO）的 Golang 实现。
- [permissions](https://github.com/xyproto/permissions) - 用于跟踪用户、登录状态与权限的库。使用安全 Cookie 与 bcrypt。
- [scope](https://github.com/SonicRoshan/scope) - 轻松管理 Go 中的 OAuth2 权限范围（Scopes）。
- [scs](https://github.com/alexedwards/scs) - 面向 HTTP 服务器的会话管理器。
- [securecookie](https://github.com/chmike/securecookie) - 高效安全的 Cookie 编解码。
- [session](https://github.com/icza/session) - 面向 Web 服务器的 Go 会话管理（包含对 Google App Engine - GAE 的支持）。
- [sessions](https://github.com/adam-hanna/sessions) - 简单、高性能、高度可定制的 Go HTTP 服务器会话服务。
- [sessionup](https://github.com/swithek/sessionup) - 简单却有效的 HTTP 会话管理与身份识别包。
- [sjwt](https://github.com/brianvoe/sjwt) - 简单的 JWT 生成器与解析器。
- [spicedb](https://github.com/authzed/spicedb) - 受 Zanzibar 启发的数据库，支持细粒度授权。
- [x509proxy](https://github.com/vkuznet/x509proxy) - 用于处理 X509 代理证书的库。

**[⬆ 回到顶部](#contents)**

<a id="blockchain"></a>
## 区块链

_用于开发区块链的工具。_

- [cometbft](https://github.com/cometbft/cometbft) - 分布式的拜占庭容错确定性状态机复制引擎。它是 Tendermint Core 的分支，并实现了 Tendermint 共识算法。
- [cosmos-sdk](https://github.com/cosmos/cosmos-sdk) - 用于在 Cosmos 生态中构建公链的框架。
- [gno](https://github.com/gnolang/gno) - 使用 Golang 与 Gnolang（专为区块链打造的确定性 Go 变体）构建的全能智能合约套件。
- [go-ethereum](https://github.com/ethereum/go-ethereum) - 以太坊协议的官方 Go 实现。
- [gosemble](https://github.com/LimeChain/gosemble) - 基于 Go 的框架，用于构建兼容 Polkadot/Substrate 的运行时。
- [gossamer](https://github.com/ChainSafe/gossamer) - Polkadot Host 的 Go 实现。
- [kubo](https://github.com/ipfs/kubo) - Go 实现的 IPFS。它提供内容寻址存储，可用于 DApp 中的去中心化存储，基于 IPFS 协议。
- [lnd](https://github.com/lightningnetwork/lnd) - 闪电网络节点的完整实现。
- [nview](https://github.com/blinklabs-io/nview) - Cardano 节点的本地监控工具。它是一个 TUI（终端用户界面），设计为适配大多数屏幕尺寸。
- [pactus](https://github.com/pactus-project/pactus) - 用 Go 实现的 Pactus 区块链全节点。
- [solana-go](https://github.com/gagliardetto/solana-go) - 用于对接 Solana JSON RPC 与 WebSocket 接口的 Go 库。
- [tendermint](https://github.com/tendermint/tendermint) - 高性能中间件，可将任意编程语言编写的状态机转换为基于 Tendermint 共识与区块链协议的拜占庭容错复制状态机。
- [tronlib](https://github.com/kslamph/tronlib) - 功能完备、可用于生产环境的 Go SDK，用于与 TRON 区块链交互，并支持 TRC20 代币。

**[⬆ 回到顶部](#contents)**

<a id="bot-building"></a>
## 机器人开发

_用于开发和运行机器人的库。_

- [arikawa](https://github.com/diamondburned/arikawa) - 用于 Discord API 的库与框架。
- [bot](https://github.com/go-telegram/bot) - 零依赖的 Telegram Bot 库，附带额外的 UI 组件。
- [echotron](https://github.com/NicoNex/echotron) - Go 中优雅且并发安全的 Telegram Bot 库。
- [go-joe](https://joe-bot.net) - 受 Hubot 启发、用 Go 编写的通用机器人库。
- [go-sarah](https://github.com/oklahomer/go-sarah) - 用于为 LINE、Slack、Gitter 等聊天服务构建机器人的框架。
- [go-tg](https://github.com/mr-linch/go-tg) - 根据官方文档生成的 Telegram Bot API Go 客户端库，内置构建复杂机器人所需的「开箱即用」能力。
- [go-twitch-irc](https://github.com/gempir/go-twitch-irc) - 用于编写 twitch.tv 聊天机器人的库。
- [micha](https://github.com/onrik/micha) - 面向 Telegram bot API 的 Go 库。
- [slack-bot](https://github.com/innogames/slack-bot) - 为懒人开发者准备的开箱即用 Slack Bot：自定义命令、Jenkins、Jira、Bitbucket、Github……
- [slacker](https://github.com/slack-io/slacker) - 易于使用的 Slack 机器人创建框架。
- [telebot](https://github.com/tucnak/telebot) - 用 Go 编写的 Telegram 机器人框架。
- [teleflow](https://github.com/kslamph/teleflow) - 简单且类型安全的 Telegram 机器人框架，具备流畅的流程编排与自动状态管理。
- [telego](https://github.com/mymmrac/telego) - 面向 Golang 的 Telegram Bot API 库，完整实现一对一 API。
- [telegram-bot-api](https://github.com/go-telegram-bot-api/telegram-bot-api) - 简单干净的 Telegram 机器人客户端。
- [TG](https://github.com/enetx/tg) - 面向 Go 的 Telegram 机器人框架。
- [wayback](https://github.com/wabarc/wayback) - 一个可归档网页的机器人，支持 Telegram、Mastodon、Slack 及其他消息平台。
- [ymsdk](https://github.com/rekurt/ymsdk) - Yandex Messenger Bot API 的 Go SDK，具备类型安全模型、自动重试与限流处理。
   - [Wisp](https://github.com/wisp-trading/wisp) - 面向 Go 的事件驱动交易框架。支持现货、永续合约与预测市场，并支持多交易所（Bybit、Hyperliquid、Polymarket）。

**[⬆ 回到顶部](#contents)**

<a id="build-automation"></a>
## 构建自动化

_有助于构建自动化的库与工具。_

- [1build](https://github.com/gopinath-langote/1build) - 命令行工具，用于轻松管理项目专属命令。
- [air](https://github.com/cosmtrek/air) - Air —— Go 应用的热重载工具。
- [anko](https://github.com/GuilhermeCaruso/anko) - 支持多种编程语言的简易应用监听器。
- [gaper](https://github.com/maxclaus/gaper) - 当 Go 项目崩溃或被监听的文件发生变化时，自动构建并重启项目。
- [gilbert](https://go-gilbert.github.io) - 面向 Go 项目的构建系统与任务运行器。
- [gob](https://github.com/kcmvp/gob) - 类 [Gradle](https://docs.gradle.org/)/[Maven](https://maven.apache.org/) 的 Go 项目构建工具。
- [goyek](https://github.com/goyek/goyek) - 用 Go 创建构建流水线。
- [mage](https://github.com/magefile/mage) - Mage 是使用 Go 实现的类 make/rake 构建工具。
- [mmake](https://github.com/tj/mmake) - 现代化的 Make。
- [realize](https://github.com/tockins/realize) - 用 Go 构建带文件监听与热重载的系统。可自定义路径，运行、构建并监听文件变化。
- [rex](https://github.com/rexrun-dev/rex) - 零配置的通用项目运行器。自动识别你的技术栈（Go、Node、Python、Rust、PHP、Zig、Elixir）并执行对应命令。
- [Task](https://github.com/go-task/task) - 简单的「Make」替代品。
- [taskctl](https://github.com/taskctl/taskctl) - 并发任务运行器。
- [xc](https://github.com/joerdav/xc) - 以 README.md 定义任务的可执行 Markdown 任务运行器。

**[⬆ 回到顶部](#contents)**

<a id="command-line"></a>
## 命令行

<a id="advanced-console-uis"></a>
### 高级终端界面

_用于构建控制台应用与终端界面的库。_

- [asciigraph](https://github.com/guptarohit/asciigraph) - Go 包，可在命令行应用中零依赖地绘制轻量级 ASCII 折线图 ╭┈╯。
- [aurora](https://github.com/logrusorgru/aurora) - 支持 fmt.Printf/Sprintf 的 ANSI 终端颜色库。
- [box-cli-maker](https://github.com/box-cli-maker/box-cli-maker) - 在终端中渲染高度可定制的方框。
- [bubble-table](https://github.com/Evertras/bubble-table) - 用于 bubbletea 的交互式表格组件。
- [bubbles](https://github.com/charmbracelet/bubbles) - 用于 bubbletea 的 TUI 组件。
- [bubbletea](https://github.com/charmbracelet/bubbletea) - 基于 Elm 架构的 Go 终端应用框架。
- [chroma16](https://github.com/arceus-7/chroma16) - 从单一颜色种子或字符串生成和谐的 16 色终端调色板。
- [crab-config-files-templating](https://github.com/alfiankan/crab-config-files-templating) - 动态配置文件模板工具，适用于 kubernetes manifest 或通用配置文件。
- [ctc](https://github.com/wzshiming/ctc) - 非侵入式的跨平台终端颜色库，无需修改 Print 方法。
- [fx](https://github.com/antonmedv/fx) - 终端 JSON 查看器与处理器。
- [go-ataman](https://github.com/workanator/go-ataman) - 用于在终端中渲染 ANSI 彩色文本模板的 Go 库。
- [go-colorable](https://github.com/mattn/go-colorable) - 适用于 Windows 的彩色输出 writer。
- [go-colortext](https://github.com/daviddengcn/go-colortext) - 用于在终端中进行彩色输出的 Go 库。
- [go-isatty](https://github.com/mattn/go-isatty) - Golang 版 isatty。
- [go-palette](https://github.com/abusomani/go-palette) - Go 库，使用 ANSI 颜色提供优雅便捷的样式定义。完全兼容并封装了 [fmt 库](https://pkg.go.dev/fmt)，便于在终端中排版。
- [go-prompt](https://github.com/c-bata/go-prompt) - 用于构建强大交互式提示符的库，灵感源自 [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit)。
- [go-tui](https://github.com/grindlemire/go-tui) - 声明式终端 UI 框架，具备类 templ 模板、flexbox 布局，以及用于编辑器支持的语言服务器。
- [gocui](https://github.com/jroimartin/gocui) - 极简 Go 库，专注于创建控制台用户界面。
- [gommon/color](https://github.com/labstack/gommon/tree/master/color) - 为终端文本添加样式。
- [gookit/color](https://github.com/gookit/color) - 终端颜色渲染工具库，支持 16 色、256 色与 RGB 真彩色输出，并兼容 Windows。
- [goscaf](https://github.com/iyashjayesh/goscaf) - goscaf 通过交互式 CLI 生成强约定、生产级的 Go 项目样板代码。不用再在项目间复制粘贴骨架代码。
- [lazyenv](https://github.com/lazynop/lazyenv) - 用于浏览、对比与编辑 .env 文件的 TUI。
- [lazyteams](https://github.com/agmonetti/lazyteams) - 面向 Microsoft Teams 的键盘驱动终端用户界面。
- [lipgloss](https://github.com/charmbracelet/lipgloss) - 以声明式定义终端中的颜色、格式与布局样式。
- [loom](https://github.com/loom-go/loom) - 基于信号的响应式组件框架，用于构建 TUI。
- [marker](https://github.com/cyucelen/marker) - 匹配并标记字符串、输出彩色终端内容的最简便方式。
- [mpb](https://github.com/vbauerster/mpb) - 终端应用的多进度条。
- [phoenix](https://github.com/phoenix-tui/phoenix) - 高性能 TUI 框架，采用受 Elm 启发的架构，出色的 Unicode 渲染，零分配事件系统。
- [progressbar](https://github.com/schollz/progressbar) - 基础线程安全进度条，适用于所有操作系统。
- [pterm](https://github.com/pterm/pterm) - 通过大量可组合组件，美化各平台控制台输出的库。
- [simpletable](https://github.com/alexeyco/simpletable) - 用 Go 在终端中绘制简单表格。
- [spinner](https://github.com/briandowns/spinner) - Go 包，可便捷地提供带选项的终端加载动画。
- [tabby](https://github.com/cheynewallace/tabby) - 用于实现超级简单的 Golang 表格的小型库。
- [table](https://github.com/tomlazar/table) - 基于终端颜色表格的小型库。
- [termbox-go](https://github.com/nsf/termbox-go) - Termbox 是用于创建跨平台文本界面的库。
- [termdash](https://github.com/mum4k/termdash) - 基于 **termbox-go** 的 Go 终端仪表盘，灵感源自 [termui](https://github.com/gizak/termui)。
- [termenv](https://github.com/muesli/termenv) - 为你的终端应用提供高级 ANSI 样式与颜色支持。
- [termui](https://github.com/gizak/termui) - 基于 **termbox-go** 的 Go 终端仪表盘，灵感源自 [blessed-contrib](https://github.com/yaronn/blessed-contrib)。
- [uilive](https://github.com/gosuri/uilive) - 用于实时更新终端输出的库。
- [uiprogress](https://github.com/gosuri/uiprogress) - 用于在终端应用中渲染进度条的灵活库。
- [uitable](https://github.com/gosuri/uitable) - 通过表格化数据提升终端应用可读性的库。
- [vhs](https://github.com/charmbracelet/vhs) - 你的 CLI 家庭录像机 —— 用代码生成终端 GIF，用于文档与教程。
- [yacspin](https://github.com/theckman/yacspin) - 又一个 CLI 加载动画包，用于处理终端 spinner。

**[⬆ 回到顶部](#contents)**

<a id="standard-cli"></a>
### 标准命令行工具

_用于构建标准或基础命令行应用的库。_

- [acmd](https://github.com/cristalhq/acmd) - Go 中简单、实用且有明确主张的 CLI 包。
- [argparse](https://github.com/akamensky/argparse) - 受 Python argparse 模块启发的命令行参数解析器。
- [argv](https://github.com/cosiner/argv) - Go 库，按 bash 语法将命令行字符串切分为参数数组。
- [boa](https://github.com/GiGurra/boa) - 基于结构体标签的声明式 flag、环境变量、校验与配置文件，构建于 cobra 之上。
- [carapace](https://github.com/rsteube/carapace) - 为 spf13/cobra 生成命令参数补全。
- [carapace-bin](https://github.com/rsteube/carapace-bin) - 多 shell 多命令的参数补全工具。
- [carapace-spec](https://github.com/rsteube/carapace-spec) - 使用 spec 文件定义简单的补全规则。
- [climax](https://github.com/tucnak/climax) - 拥有「人脸」的替代 CLI，设计理念源自 Go 命令。
- [clîr](https://github.com/leaanthony/clir) - 简单清晰的 CLI 库。零依赖。
- [cmd](https://github.com/posener/cmd) - 扩展标准 `flag` 包，以惯用方式支持子命令等功能。
- [cmdr](https://github.com/hedzr/cmdr) - POSIX/GNU 风格、类 getopt 的 Go 命令行 UI 库。
- [cobra](https://github.com/spf13/cobra) - 面向现代 Go CLI 交互的 Commander 库。
- [command-chain](https://github.com/rainu/go-command-chain) - 用于配置与执行命令链的 Go 库，例如类 Unix shell 的管道。
- [commandeer](https://github.com/jaffee/commandeer) - 面向开发者的 CLI 应用：基于结构体字段与标签设置 flag、默认值与用法说明。
- [complete](https://github.com/posener/complete) - 用 Go 编写 bash 补全，并支持 Go 命令的 bash 补全。
- [console](https://github.com/reeflective/console) 面向 Cobra 命令的闭环应用库，内置 oh-my-posh 提示等能力。
- [Dnote](https://github.com/dnote/dnote) - 简单的命令行笔记本，支持多设备同步。
- [elvish](https://github.com/elves/elvish) - 一门表达力丰富的编程语言，同时是一个多功能的交互式 shell。
- [env](https://github.com/codingconcepts/env) - 基于标签的结构体环境配置。
- [flaggy](https://github.com/integrii/flaggy) - 稳健、惯用的 flag 包，具备出色的子命令支持。
- [flagvar](https://github.com/sgreben/flagvar) - 为 Go 标准 `flag` 包提供的 flag 参数类型集合。
- [flash-flags](https://github.com/agilira/flash-flags) - 极速、零依赖、符合 POSIX 的 flag 解析库，可直接作为标准库替代品，并具备安全加固。
- [Fling-CLI](https://github.com/SatyamKumarCS/Fling-CLI) - 基于自定义可靠 UDP 的终端式点对点文件与消息传输工具。
- [getopt](https://github.com/jon-codes/getopt) - 精确的 Go 版 `getopt`，已对照 GNU libc 实现进行验证。
- [go-arch](https://github.com/SalvucciFacundo/go-arch) - 用于以极简（Minimalist）、标准（Standard）与六边形（Hexagonal）架构模式搭建 Go 应用的 CLI 脚手架工具。
- [go-arg](https://github.com/alexflint/go-arg) - Go 中基于结构体的参数解析。
- [go-flags](https://github.com/jessevdk/go-flags) - Go 命令行选项解析器。
- [go-getoptions](https://github.com/DavidGamba/go-getoptions) - 受 Perl GetOpt::Long 灵活性启发的 Go 选项解析器。
- [go-readline-ny](https://github.com/nyaosorg/go-readline-ny) - 可定制的行编辑库，具备 Emacs 快捷键绑定、Unicode 支持、补全与语法高亮。用于 NYAGOS shell。
- [gocmd](https://github.com/devfacet/gocmd) - 用于构建命令行应用的 Go 库。
- [goopt](https://github.com/napalu/goopt) - 面向 Go 的声明式、基于结构体标签的 CLI 框架，功能丰富，涵盖层级化命令/flag、国际化、shell 补全与校验。
- [hashicorp/cli](https://github.com/hashicorp/cli) - 用于实现命令行界面的 Go 库。
- [hiboot cli](https://github.com/hidevopsio/hiboot/tree/master/pkg/app/cli) - 支持自动配置与依赖注入的 CLI 应用框架。
- [job](https://github.com/liujianping/job) - JOB，让你的短期命令变成长期作业。
- [kingpin](https://github.com/alecthomas/kingpin) - 支持子命令的命令行与 flag 解析器（已被下文 `kong` 取代）。
- [liner](https://github.com/peterh/liner) - 面向命令行界面的 Go readline 类库。
- [mcli](https://github.com/jxskiss/mcli) - 极简但非常强大的 Go CLI 库。
- [memsh](https://github.com/amjadjibon/memsh) - Go 版虚拟 bash shell：在内存文件系统（afero）上执行 shell 命令，支持 WASM 插件与可嵌入的 HTTP 服务器。
- [mkideal/cli](https://github.com/mkideal/cli) - 基于 Go 结构体标签、功能丰富且易用的命令行包。
- [mow.cli](https://github.com/jawher/mow.cli) - 用于构建具备精细 flag 与参数解析及校验能力的 CLI 应用的 Go 库。
- [neuron-cli](https://github.com/steevin/neuron-cli) - 本地优先、兼容 Obsidian 的终端知识管理器。
- [OpenCLI](https://github.com/bcdxn/opencli) - 面向 CLI 的 OpenAPI 风格规范；以语言无关的文档定义你的接口，据此生成文档与框架样板代码。
- [ops](https://github.com/nanovms/ops) - Unikernel 构建器 / 编排器。
- [orpheus](https://github.com/agilira/orpheus) - 具备安全加固、插件存储系统与生产级可观测性特性的 CLI 框架。
- [pflag](https://github.com/spf13/pflag) - Go flag 包的直接替代品，实现 POSIX/GNU 风格的 --flags。
- [readline](https://github.com/reeflective/readline) - 具备现代易用 UI 特性的 Shell 库。
- [sflags](https://github.com/octago/sflags) - 为 flag、urfave/cli、pflag、cobra、kingpin 等库生成基于结构体的 flag 代码。
- [structcli](https://github.com/leodido/structcli) - 消除 Cobra 样板代码：以声明式方式从 Go 结构体构建强大、功能丰富的 CLI。
- [strumt](https://github.com/antham/strumt) - 用于创建提示链的库。
- [subcmd](https://github.com/bobg/subcmd) - 另一种解析与运行子命令的方案，可与标准 `flag` 包协同工作。
- [teris-io/cli](https://github.com/teris-io/cli) - 在 Go 中构建命令行界面的简单完整 API。
- [urfave/cli](https://github.com/urfave/cli) - 简单、快速且有趣的 Go 命令行应用构建包（原 codegangsta/cli）。
- [version](https://github.com/mszostok/version) - 以多种格式收集并展示 CLI 版本信息，并附带升级提示。
- [wlog](https://github.com/dixonwille/wlog) - 简单的日志接口，支持跨平台颜色与并发。
- [wmenu](https://github.com/dixonwille/wmenu) - 易于使用的 CLI 应用菜单结构，可提示用户做出选择。

**[⬆ 回到顶部](#contents)**

<a id="configuration"></a>
## 配置

_用于解析配置文件的库。_

- [aconfig](https://github.com/cristalhq/aconfig) - 简单、实用且有明确主张的配置加载器。
- [argus](https://github.com/agilira/argus) - 文件监听与配置管理，具备 MPSC 环形缓冲区、自适应批处理策略，以及通用格式解析（JSON、YAML、TOML、INI、HCL、Properties）。
- [azureappconfiguration](https://github.com/Azure/AppConfiguration-GoProvider) - 供 Go 应用消费 Azure App Configuration 数据的配置提供程序。
- [bcl](https://github.com/wkhere/bcl) - BCL 是一门类似 HCL 的配置语言。
- [cleanenv](https://github.com/ilyakaznacheev/cleanenv) - 极简配置读取器（可从文件、ENV 以及任意来源读取）。
- [config](https://github.com/JeremyLoy/config) - 云原生应用配置。仅用两行代码即可将 ENV 绑定到结构体。
- [config](https://github.com/num30/config) - 仅用两行代码即可通过文件、环境变量或命令行参数配置你的应用。
- [config](https://github.com/andreiavrammsd/config) - 基于结构体的配置加载器，内置专用配置文件解析器，支持环境变量、flag、默认值与校验。
- [configuration](https://github.com/BoRuDar/configuration) - 用于从环境变量、文件、命令行参数及 'default' 标签初始化配置结构体的库。
- [configuro](https://github.com/sherifabdlnaby/configuro) - 强约定的配置加载与校验框架，面向符合 12-Factor 原则的应用，支持从环境变量与文件读取。
- [confiq](https://github.com/greencoda/confiq) - 面向 Go 的结构化数据格式到配置结构体的解码库，支持多种数据格式。
- [confita](https://github.com/heetch/confita) - 以级联方式从多个后端将配置加载进结构体。
- [conflate](https://github.com/the4thamigo-uk/conflate) - 用于合并来自任意 URL 的多个 JSON/YAML/TOML 文件、按 JSON Schema 校验、并套用 schema 中定义的默认值的库/工具。
- [enflag](https://github.com/atelpis/enflag) - 面向容器、零依赖的配置库，统一环境变量与 flag 解析。借助泛型实现类型安全，无需反射或结构体标签。
- [env](https://github.com/caarlos0/env) - 将环境变量解析为 Go 结构体（含默认值）。
- [env](https://github.com/junk1tm/env) - 用于将环境变量加载进结构体的轻量级包。
- [env](https://github.com/syntaqx/env) - 环境工具包，支持反序列化进结构体。
- [envconfig](https://github.com/vrischmann/envconfig) - 从环境变量读取你的配置。
- [envh](https://github.com/antham/envh) - 用于管理环境变量的辅助工具。
- [envyaml](https://github.com/yuseferi/envyaml) - 支持环境变量的 YAML 读取器。它让你把密钥放在环境变量里，却仍以结构化 YAML 的形式作为配置加载。
- [fig](https://github.com/kkyr/fig) - 用于从文件和环境变量读取配置的微型库（带校验与默认值）。
- [genv](https://github.com/sakirsensoy/genv) - 借助 dotenv 支持轻松读取环境变量。
- [go-array](https://github.com/deatil/go-array) - Go 包，可从 map、slice 或 JSON 中读取或设置数据。
- [go-aws-ssm](https://github.com/PaddleHQ/go-aws-ssm) - Go 包，用于从 AWS System Manager - Parameter Store 获取参数。
- [go-cfg](https://github.com/dsbasko/go-cfg) - 该库提供统一的方式，将配置数据从环境变量、flag 与配置文件（.json、.yaml、.toml、.env）等多种来源读入结构体。
- [go-conf](https://github.com/ThomasObenaus/go-conf) - 基于带注解结构体的简易应用配置库。支持从环境变量、配置文件与命令行参数读取配置。
- [go-config](https://github.com/MordaTeam/go-config) - 简单便捷的应用配置操作库。
- [go-external-config](https://github.com/go-external-config/go) - 受 Spring 启发的 Go 配置管理库。
- [go-external-config/aws](https://github.com/go-external-config/aws) - 为 go-external-config 提供 AWS Property Source 支持。
- [go-external-config/consul](https://github.com/go-external-config/consul) - 为 go-external-config 提供 Consul Property Source 支持。
- [go-external-config/vault](https://github.com/go-external-config/vault) - 为 go-external-config 提供 Vault Property Source 支持。
- [go-ini](https://github.com/subpop/go-ini) - Go 包，用于编解码 INI 文件。
- [go-ssm-config](https://github.com/ianlopshire/go-ssm-config) - Go 工具，用于从 AWS SSM（Parameter Store）加载配置参数。
- [go-up](https://github.com/ufoscout/go-up) - 简单配置库，支持递归占位符解析，且不耍花招。
- [go-yamlvalidator](https://github.com/Yakwilik/go-yamlvalidator) - 源码感知的 YAML 校验工具，基于原生 Go schema 并支持 JSON Schema。
- [GoCfg](https://github.com/Jagerente/gocfg) - 配置管理器，支持基于结构体标签的约定、自定义值提供程序、解析器与文档生成。可定制yet简单。
- [goconfig](https://github.com/fulldump/goconfig) - 以确定性的优先级，从 flag、环境变量、config.json 与默认值填充 Go 结构体。无额外依赖。
- [godotenv](https://github.com/joho/godotenv) - Ruby dotenv 库的 Go 移植版（从 `.env` 加载环境变量）。
- [goenv](https://github.com/psyb0t/goenv) - 读取环境变量 ENV，报告进程运行于生产还是开发环境。
- [GoLobby/Config](https://github.com/golobby/config) - GoLobby Config 是面向 Go 编程语言的轻量却强大的配置管理器。
- [gone/jconf](https://github.com/One-com/gone/tree/master/jconf) - 模块化 JSON 配置。配置结构体与它所配置的代码放在一起，并把解析委托给子模块，同时不牺牲完整的配置序列化能力。
- [gonfig](https://github.com/milad-abbasi/gonfig) - 基于标签的配置解析器，将不同提供程序的值加载进类型安全的结构体。
- [gonfiguration](https://github.com/psyb0t/gonfiguration) - 通过反射将环境变量加载进结构体，支持结构体标签默认值与必填字段。
- [gookit/config](https://github.com/gookit/config) - 应用配置管理（加载、读取、设置）。支持 JSON、YAML、TOML、INI、HCL，支持多文件加载与数据覆盖合并。
- [harvester](https://github.com/beatlabs/harvester) - Harvester，一个易用的静态与动态配置包，支持种子数据、环境变量与 Consul 集成。
- [hedzr/store](https://github.com/hedzr/store) - 可扩展的高性能配置管理库，针对层级化数据做了优化。
- [hjson](https://github.com/hjson/hjson-go) - Human JSON —— 面向人类的配置文件格式。宽松语法、更少出错、更多注释。
- [hocon](https://github.com/gurkankaymak/hocon) - 用于处理 HOCON（人类友好的 JSON 超集）格式的配置库，支持环境变量、引用其他值、注释与多文件等特性。
- [ini](https://github.com/go-ini/ini) - 用于读写 INI 文件的 Go 包。
- [ini](https://github.com/wlevene/ini) - INI 解析与写入库。支持反序列化到结构体、序列化为 JSON、写入文件，以及文件监听。
- [kelseyhightower/envconfig](https://github.com/kelseyhightower/envconfig) - 用于管理来自环境变量的配置数据的 Go 库。
- [koanf](https://github.com/knadh/koanf) - 轻量、可扩展的配置读取库。内置支持 JSON、TOML、YAML、环境变量与命令行。
- [konf](https://github.com/nil-go/konf) - 最简单的 API，用于从文件、环境变量、flag 与云平台（如 AWS、Azure、GCP）读取及监听配置。
- [konfig](https://github.com/lalamove/konfig) - 面向分布式处理时代的 Go 配置处理方案，可组合、可观测、高性能。
- [kong](https://github.com/alecthomas/kong) - 命令行解析器，支持任意复杂的命令行结构，并支持 YAML、JSON、TOML 等额外配置来源（`kingpin` 的继任者）。
- [nasermirzaei89/env](https://github.com/nasermirzaei89/env) - 简单实用的环境变量读取包。
- [nfigure](https://github.com/muir/nfigure) - 按库维度的结构体标签配置，来源包括命令行（Posix 与 Go 风格）、环境变量、JSON、YAML。
- [onion](https://github.com/goraz/onion) - 面向 Go 的分层配置，支持 JSON、TOML、YAML、properties、etcd、环境变量，以及使用 PGP 的加密。
- [piper](https://github.com/Yiling-J/piper) - 带配置继承与密钥生成的 Viper 封装。
- [sonic](https://github.com/bytedance/sonic) - 极速的 JSON 序列化与反序列化库。
- [swap](https://github.com/oblq/swap) - 基于构建环境递归实例化/配置结构体（YAML、TOML、JSON 与环境变量）。
- [typenv](https://github.com/diegomarangoni/typenv) - 极简、零依赖、类型安全的环境变量库。
- [uConfig](https://github.com/omeid/uconfig) - 轻量、零依赖、可扩展的配置管理。
- [viper](https://github.com/spf13/viper) - 带利齿的 Go 配置管理（fangs）。
- [xdg](https://github.com/adrg/xdg) - [XDG 基础目录规范](https://specifications.freedesktop.org/basedir-spec/latest/) 与 [XDG 用户目录](https://wiki.archlinux.org/index.php/XDG_user_directories)的 Go 实现。
- [yamagiconf](https://github.com/romshark/yamagiconf) - 面向 Go 配置的 YAML「安全子集」。
- [zerocfg](https://github.com/chaindead/zerocfg) - 零负担、简洁的配置管理，避免样板代码与重复代码，支持多来源与优先级覆盖。

**[⬆ 回到顶部](#contents)**

<a id="continuous-integration"></a>
## 持续集成

_有助于持续集成的工具。_

- [abstruse](https://github.com/bleenco/abstruse) - Abstruse 是一个分布式 CI 平台。
- [Bencher](https://bencher.dev/) - 一套持续基准测试工具，用于在 CI 中捕捉性能回归。
- [CDS](https://github.com/ovh/cds) - 企业级 CI/CD 与 DevOps 自动化开源平台。
- [coverage](https://github.com/jbunds/coverage) - 用于展示 Go 测试覆盖率的简易 Web UI，以及可复用的 [go-test-coverage-html-report](https://github.com/marketplace/actions/go-test-coverage-html-report) GitHub Action。
- [dot](https://github.com/opnlabs/dot) - 极简、本地优先的持续集成系统，使用 Docker 分阶段并发运行任务。
- [drone](https://github.com/drone/drone) - Drone 是基于 Docker、用 Go 编写的持续集成平台。
- [go-beautiful-html-coverage](https://github.com/gha-common/go-beautiful-html-coverage) - 在 Pull Request 中追踪代码覆盖率的 GitHub Action，附带精美的 HTML 预览，免费使用。
- [go-fuzz-action](https://github.com/jidicula/go-fuzz-action) - 在 GitHub Actions 中使用 Go 1.18 内置的模糊测试。
- [go-semver-release](https://github.com/s0ders/go-semver-release) - 自动化 Git 仓库的语义化版本管理。
- [go-test-coverage](https://github.com/marketplace/actions/go-test-coverage) - 当测试覆盖率低于设定阈值时报告问题的 GitHub Action。
- [gomason](https://github.com/nikogura/gomason) - 在干净的工作区中测试、构建、签名并发布你的 Go 二进制文件。
- [gotestfmt](https://github.com/GoTestTools/gotestfmt) - 面向人类的 go test 输出。
- [goveralls](https://github.com/mattn/goveralls) - Coveralls.io 持续代码覆盖率追踪系统的 Go 集成。
- [muffet](https://github.com/raviqqe/muffet) - 用 Go 编写的快速网站链接检查器，另见[替代方案](https://github.com/lycheeverse/lychee#features)。
- [overalls](https://github.com/go-playground/overalls) - 为 goveralls 等工具生成多包 Go 项目的 coverprofile。
- [PikoCI](https://github.com/pikoci/pikoci) - 受 Concourse 启发的自托管 CI/CD。单一二进制、任意数据库、任意队列。HCL 流水线、可插拔的资源类型与执行器。
- [roveralls](https://github.com/LawrenceWoodman/roveralls) - 递归覆盖率测试工具。
- [woodpecker](https://github.com/woodpecker-ci/woodpecker) - Woodpecker 是 Drone CI 系统的社区 fork。

**[⬆ 回到顶部](#contents)**

<a id="css-preprocessors"></a>
## CSS 预处理器

_用于预处理 CSS 文件的库。_

- [go-css](https://github.com/napsy/go-css) - 用 Go 编写的极简 CSS 解析器。
- [go-libsass](https://github.com/wellington/go-libsass) - 对 100% 兼容 Sass 的 libsass 项目的 Go 封装。

**[⬆ 回到顶部](#contents)**

<a id="data-integration-frameworks"></a>
## 数据集成框架

_用于执行 ELT / ETL 的框架_

- [Benthos](https://github.com/benthosdev/benthos) - 在多种协议之间架设的消息流式桥接。
- [CloudQuery](http://github.com/cloudquery/cloudquery) - 高性能 ELT 数据集成框架，架构可插拔。
- [confluence2md](https://github.com/gkoos/confluence2md) - Confluence 到 Markdown 的爬取与转换工具。
- [omniparser](https://github.com/jf-tech/omniparser) - 多用途 ETL 库，以流式方式解析文本输入（CSV/txt/JSON/XML/EDI/X12/EDIFACT 等），并用数据驱动的 schema 将数据转换为 JSON 输出。

**[⬆ 回到顶部](#contents)**

<a id="data-structures-and-algorithms"></a>
## 数据结构与算法

<a id="bit-packing-and-compression"></a>
### 位打包与压缩

- [bingo](https://github.com/iancmcc/bingo) - 快速、零分配、保持字典序的原生类型打包为字节流。
- [binpacker](https://github.com/zhuangsirui/binpacker) - 二进制打包与解包工具，帮助用户构建自定义二进制流。
- [bit](https://github.com/yourbasic/bit) - Golang 集合数据结构，附带若干位运算技巧函数。
- [crunch](https://github.com/superwhiskers/crunch) - Go 包，实现便于处理各种数据类型的缓冲区。
- [go-ef](https://github.com/amallia/go-ef) - Elias-Fano 编码的 Go 实现。
- [roaring](https://github.com/RoaringBitmap/roaring) - 实现压缩位集的 Go 包。

<a id="bit-sets"></a>
### 位集合

- [bitmap](https://github.com/kelindar/bitmap) - 稠密、零分配、支持 SIMD 的 Go 位图/位集。
- [bitset](https://github.com/bits-and-blooms/bitset) - 实现位集的 Go 包。

<a id="bloom-and-cuckoo-filters"></a>
### 布隆过滤器与布谷鸟过滤器

- [bloom](https://github.com/bits-and-blooms/bloom) - 实现布隆过滤器的 Go 包。
- [bloom](https://github.com/zhenjl/bloom) - 用 Go 实现的布隆过滤器。
- [bloom](https://github.com/yourbasic/bloom) - Golang 布隆过滤器实现。
- [bloomfilter](https://github.com/OldPanda/bloomfilter) - 又一个用 Go 实现的布隆过滤器，与 Java 的 Guava 库兼容。
- [boomfilters](https://github.com/tylertreat/BoomFilters) - 用于处理连续无界数据流的概率型数据结构。
- [cuckoo-filter](https://github.com/linvon/cuckoo-filter) - 布谷鸟过滤器：功能完备的布谷鸟过滤器，相较其他实现更可配置、空间更优，且原始论文中提到的全部特性均可用。
- [cuckoofilter](https://github.com/seiflotfy/cuckoofilter) - 布谷鸟过滤器：用 Go 实现，是计数布隆过滤器的一个良好替代方案。
- [ribbonGo](https://github.com/RibbonFilter/ribbonGo) - 首个纯 Go 的 Ribbon 过滤器实现（实际比 Bloom 与 Xor 更小），用于空间高效的近似集合成员查询。
- [ring](https://github.com/TheTannerRyan/ring) - 高性能、线程安全的布隆过滤器的 Go 实现。

<a id="data-structure-and-algorithm-collections"></a>
### 数据结构与算法合集

- [algorithms](https://github.com/shady831213/algorithms) - 算法与数据结构，CLRS 学习笔记。
- [go-datastructures](https://github.com/Workiva/go-datastructures) - 一批实用、高性能、线程安全的数据结构集合。
- [gods](https://github.com/emirpasic/gods) - Go 数据结构。容器、集合、列表、栈、映射、双向映射、树、哈希集合等。
- [gostl](https://github.com/liyue201/gostl) - Go 的数据结构与算法库，旨在提供类似 C++ STL 的函数。

<a id="iterators"></a>
### 迭代器

- [gloop](https://github.com/alvii147/gloop) - 借助 Go 的 range-over-func 特性实现便捷遍历。
- [goterator](https://github.com/yaa110/goterator) - 提供 map 与 reduce 功能的迭代器实现。
- [iter](https://github.com/disksing/iter) - C++ STL 迭代器与算法的 Go 实现。

<a id="maps"></a>
### 映射

更复杂的键值存储参见[数据库](#database)，
更多有序 Map 实现参见[树](#trees)。

- [cmap](https://github.com/lrita/cmap) - Go 的线程安全并发映射，支持以 `interface{}` 作为键，并能自动扩展分片。
- [concurrent-swiss-map](https://github.com/mhmtszr/concurrent-swiss-map) - 基于 Swiss Map 的高性能、线程安全、泛型并发哈希表实现。
- [dict](https://github.com/srfrog/dict) - Go 版类 Python 字典（dict）。
- [genericsyncmap](https://github.com/donomii/genericsyncmap) - 对 `sync.Map` 的类型安全泛型封装，方法完全对齐且零依赖。
- [go-shelve](https://github.com/lucmq/go-shelve) - 面向 Go 编程语言的持久化类映射对象。支持多种内嵌键值存储。
- [goradd/maps](https://github.com/goradd/maps) - 面向 Go 1.18+ 的泛型映射接口：普通 map、安全 map、有序 map、有序安全 map 等。
- [hmap](https://github.com/lyonnee/hmap) - HMap 是一个并发且安全的泛型 Map 实现，旨在提供易于使用的 API。

<a id="miscellaneous-data-structures-and-algorithms"></a>
### 其他数据结构与算法

- [combo](https://github.com/bobg/combo) - 组合运算，包括排列、组合与可重复组合。
- [concurrent-writer](https://github.com/free/concurrent-writer) - 高并发的 `bufio.Writer` 直接替代品。
- [count-min-log](https://github.com/seiflotfy/count-min-log) - Count-Min-Log 草图的 Go 实现：用近似计数器做近似计数（类似 Count-Min 草图，但占用内存更少）。
- [FSM](https://github.com/enetx/fsm) - Go 版有限状态机（FSM）。
- [fsm](https://github.com/cocoonspace/fsm) - 有限状态机包。
- [genfuncs](https://github.com/nwillc/genfuncs) - 受 Kotlin Sequence 与 Map 启发的 Go 1.18+ 泛型包。
- [go-generics](https://github.com/bobg/go-generics) - 泛型切片、映射、集合、迭代器与 goroutine 工具集。
- [go-geoindex](https://github.com/hailocab/go-geoindex) - 内存地理索引。
- [go-rampart](https://github.com/francesconi/go-rampart) - 判定区间之间的相互关系。
- [go-rquad](https://github.com/aurelien-rainone/go-rquad) - 区域四叉树，支持高效的点定位与邻域查找。
- [go-tuple](https://github.com/barweiss/go-tuple) - 面向 Go 1.18+ 的泛型元组实现。
- [go18ds](https://github.com/daichi-m/go18ds) - 使用 Go 1.18 泛型的 Go 数据结构。
- [gofal](https://github.com/xxjwxc/gofal) - 面向 Go 的分数 API。
- [gogu](https://github.com/esimov/gogu) - 一套完备、可复用、高效且并发安全的泛型工具函数与数据结构库。
- [gota](https://github.com/kniren/gota) - Go 版 dataframe、series 与数据处理方法的实现。
- [hide](https://github.com/emvi/hide) - 可与哈希互相编解码的 ID 类型，用于避免把内部 ID 发送给客户端。
- [hyperloglog](https://github.com/axiomhq/hyperloglog) - HyperLogLog 实现，带 Sparse 偏差校正与 TailCut 空间缩减。
- [quadtree](https://github.com/s0rg/quadtree) - 纯泛型的四叉树，零分配、100% 测试覆盖。
- [slices](https://github.com/twharmon/slices) - 面向切片的纯泛型函数。

<a id="nullable-types"></a>
### 可空类型

- [nan](https://github.com/kak-tus/nan) - 一个库内集成零分配的可空结构体，并提供便捷的转换函数与编解码器。
- [null](https://github.com/emvi/null) - 可与 JSON 互相编解码的 Go 可空类型。
- [typ](https://github.com/gurukami/typ) - 空值类型、安全的基础类型转换，以及从复杂结构中取值。

<a id="queues"></a>
### 队列

- [deheap](https://github.com/aalpar/deheap) - 双端堆（最小-最大堆），以 O(log n) 同时访问最小与最大元素。
- [deque](https://github.com/edwingeng/deque) - 高度优化的双端队列。
- [deque](https://github.com/gammazero/deque) - 快速环形缓冲区双端队列。
- [dqueue](https://github.com/vodolaz095/dqueue) - 简单、纯内存、零依赖、经过实战检验的线程安全延迟队列。
- [goconcurrentqueue](https://github.com/enriquebris/goconcurrentqueue) - 并发 FIFO 队列。
- [hatchet](https://github.com/hatchet-dev/hatchet) - 分布式、容错的任务队列。
- [list](https://github.com/koss-null/list) - 通用线程安全双向链表，支持完整迭代器，并提供可用于嵌入场景的侵入式单向链表；是 container/list 的功能更丰富的替代品。
- [memlog](https://github.com/embano1/memlog) - 受 Apache Kafka 启发的易用、轻量、线程安全、仅追加的内存数据结构。
- [queue](https://github.com/adrianbrad/queue) - 多种线程安全的泛型队列实现。

<a id="sets"></a>
### 集合

- [dsu](https://github.com/ihebu/dsu) - Go 版并查集数据结构实现。
- [golang-set](https://github.com/deckarep/golang-set) - 面向 Go 的线程安全与非线程安全高性能集合。
- [goset](https://github.com/zoumo/goset) - 实用的 Go Set 集合实现。
- [set](https://github.com/StudioSol/set) - 用 LinkedHashMap 实现的简易 Go 集合数据结构。

<a id="text-analysis"></a>
### 文本分析

- [bleve](https://github.com/blevesearch/bleve) - 面向 Go 的现代化文本索引库。
- [go-adaptive-radix-tree](https://github.com/plar/go-adaptive-radix-tree) - 自适应基数树（Adaptive Radix Tree）的 Go 实现。
- [go-edlib](https://github.com/hbollon/go-edlib) - Go 字符串比较与编辑距离算法库（Levenshtein、LCS、Hamming、Damerau-Levenshtein、Jaro-Winkler 等），兼容 Unicode。
- [levenshtein](https://github.com/agext/levenshtein) - Levenshtein 距离与相似度度量，支持自定义编辑代价，并为公共前缀提供类 Winkler 奖励。
- [levenshtein](https://github.com/agnivade/levenshtein) - 用于计算 Levenshtein 距离的 Go 实现。
- [mspm](https://github.com/BlackRabbitt/mspm) - 面向信息检索的多字符串模式匹配算法。
- [parsefields](https://github.com/MonaxGT/parsefields) - 解析类 JSON 日志的工具，用于采集唯一字段与事件。
- [ptrie](https://github.com/viant/ptrie) - 前缀树的实现。
- [radixtree](https://github.com/gammazero/radixtree) - 自适应基数树（prefix-tree 或 compact-trie）。
- [trie](https://github.com/derekparker/trie) - Go 版 Trie 实现。

<a id="trees"></a>
### 树

- [graphlib](https://github.com/aio-arch/graphlib) - 拓扑排序库，支持对 DAG 图排序与剪枝。
- [hashsplit](http://github.com/bobg/hashsplit) - 将字节流切分为数据块，并按内容（而非位置）确定的边界把数据块组织成树。
- [merkle](https://github.com/bobg/merkle) - 空间高效的 Merkle 根哈希与包含证明计算。
- [skiplist](https://github.com/MauriceGit/skiplist) - 非常快的 Go 跳表实现。
- [skiplist](https://github.com/gansidui/skiplist) - Go 版跳表实现。
- [skiplist](https://github.com/huandu/skiplist) - 快速易用的 Go 跳表。
- [treemap](https://github.com/igrmk/treemap) - 底层采用红黑树的按键排序泛型映射。

<a id="pipes"></a>
### 管道

- [ordered-concurrently](https://github.com/tejzpr/ordered-concurrently) - Go 模块，并发处理任务，并按输入顺序通过 channel 返回结果。
- [parapipe](https://github.com/nazar256/parapipe) - FIFO 流水线，在保持消息与结果顺序的同时让各阶段并行执行。
- [pipeline](https://github.com/hyfather/pipeline) - 支持 fan-in 与 fan-out 的流水线实现。
- [pipelines](https://github.com/nxdir-s/pipelines) - 用于并发处理的泛型流水线函数。

**[⬆ 回到顶部](#contents)**

<a id="database"></a>
## 数据库

<a id="caches"></a>
### 缓存

_支持记录过期、内存分布式数据存储，或文件型数据库内存子集的存储。_

- [bcache](https://github.com/iwanbk/bcache) - 最终一致的分布式内存缓存 Go 库。
- [BigCache](https://github.com/allegro/bigcache) - 面向 GB 级数据的高效键值缓存。
- [cache2go](https://github.com/muesli/cache2go) - 内存键值缓存，支持基于超时的自动失效。
- [cachego](https://github.com/faabiosr/cachego) - 支持多驱动的 Golang 缓存组件。
- [clusteredBigCache](https://github.com/oaStuff/clusteredBigCache) - BigCache，支持集群与单条目过期。
- [coherence-go-client](https://github.com/oracle/coherence-go-client) - 面向 Go 应用的 Oracle Coherence 缓存 API 完整实现，以 gRPC 作为网络传输。
- [couchcache](https://github.com/codingsince1985/couchcache) - 基于 Couchbase 服务器的 RESTful 缓存微服务。
- [EchoVault](https://github.com/EchoVault/EchoVault) - 可嵌入的分布式内存数据存储，兼容 Redis 客户端。
- [easycache](https://github.com/hugocarreira/easycache) - 在 Golang 中使用内存缓存的简便方式（TTL/FIFO/LRU/LFU）。
- [fastcache](https://github.com/VictoriaMetrics/fastcache) - 面向海量条目的快速线程安全内存缓存。最大限度降低 GC 开销。
- [GCache](https://github.com/bluele/gcache) - 支持可过期缓存、LFU、LRU 与 ARC 的缓存库。
- [gdcache](https://github.com/ulovecode/gdcache) - 用 Go 实现的纯非侵入式缓存库，你可以基于它实现自己的分布式缓存。
- [go-cache](https://github.com/viney-shih/go-cache) - 灵活的多层 Go 缓存库，采用 Cache-Aside 模式同时处理内存缓存与共享缓存。
- [go-freelru](https://github.com/elastic/go-freelru) 免 GC、快速且泛型的 LRU 哈希表库，支持可选加锁、分片、淘汰与过期。
- [go-gcache](https://github.com/szyhf/go-gcache) - `GCache` 的泛型版本，支持可过期缓存、LFU、LRU 与 ARC。
- [go-mcache](https://github.com/OrlovEvgeny/go-mcache) - 快速内存键值存储/缓存库。支持指针缓存。
- [gocache](https://github.com/eko/gocache) - 完整的 Go 缓存库，支持多种存储（memory、memcache、redis 等），可链式、可预加载、带指标统计等功能。
- [gocache](https://github.com/yuseferi/gocache) - 无数据竞争的 Go 缓存库，高性能并具备自动清理功能。
- [groupcache](https://github.com/golang/groupcache) - Groupcache 是一个缓存与缓存填充库，在许多场景下可替代 memcached。
- [icache](https://github.com/mdaliyan/icache) - 高性能、泛型、线程安全、零依赖的缓存包。
- [imcache](https://github.com/erni27/imcache) - 泛型内存缓存 Go 库。支持过期、滑动过期、最大条目数限制、淘汰回调与分片。
- [jetcache-go](https://github.com/mgtv-tech/jetcache-go) - 统一 Go 缓存库，支持多级缓存。
- [nscache](https://github.com/no-src/nscache) - 支持多种数据源驱动的 Go 缓存框架。
- [otter](https://github.com/maypok86/otter) - 面向 Go 的高性能无锁缓存。比 Ristretto 之流快出许多倍。
- [pocache](https://github.com/naughtygopher/pocache) - Pocache 是一个极简缓存包，专注于预判式乐观缓存策略。
- [ristretto](https://github.com/dgraph-io/ristretto) - 面向内存瓶颈场景的高性能 Go 缓存。
- [sturdyc](https://github.com/viccon/sturdyc) - 具备高级并发特性的缓存库，让 I/O 密集型应用更稳健、更高性能。
- [theine](https://github.com/Yiling-J/theine-go) - 高性能、接近最优的内存缓存，带主动 TTL 过期与泛型支持。
- [timedmap](https://github.com/zekroTJA/timedmap) - 支持键值对过期的映射。
- [ttlcache](https://github.com/jellydator/ttlcache) - 支持条目过期与泛型的内存缓存。
- [ttlcache](https://github.com/cheshir/ttlcache) - 内存键值存储，每条记录可设 TTL。

<a id="databases-implemented-in-go"></a>
### 用 Go 实现的数据库

- [badger](https://github.com/dgraph-io/badger) - Go 版快速键值存储。
- [bbolt](https://github.com/etcd-io/bbolt) - 面向 Go 的嵌入式键值数据库。
- [Bitcask](https://git.mills.io/prologic/bitcask) - Bitcask 是用纯 Go 编写的可嵌入、持久化、快速键值（KV）数据库，凭借 bitcask 磁盘布局（LSM+WAL）实现可预测的读写性能、低延迟与高吞吐。
- [buntdb](https://github.com/tidwall/buntdb) - 快速、可嵌入的 Go 内存键值数据库，支持自定义索引与空间查询。
- [clover](https://github.com/ostafen/clover) - 用纯 Golang 编写的轻量级文档型 NoSQL 数据库。
- [cockroach](https://github.com/cockroachdb/cockroach) - 可扩展、异地复制、事务型数据存储。
- [Coffer](https://github.com/claygod/coffer) - 简单且支持事务的 ACID 键值数据库。
- [column](https://github.com/kelindar/column) - 高性能列式可嵌入内存存储，具备位图索引与事务支持。
- [CovenantSQL](https://github.com/CovenantSQL/CovenantSQL) - CovenantSQL 是运行在区块链上的 SQL 数据库。
- [Databunker](https://github.com/paranoidguy/databunker) - 为符合 GDPR 与 CCPA 而构建的个人身份信息（PII）存储服务。
- [dgraph](https://github.com/dgraph-io/dgraph) - 可扩展、分布式、低延迟、高吞吐的图数据库。
- [DiceDB](https://github.com/DiceDB/dice) - 开源、快速、响应式的内存数据库，针对现代硬件优化。更高吞吐与更低中位延迟，非常适合现代工作负载。
- [diskv](https://github.com/peterbourgon/diskv) - 自研的磁盘支撑键值存储。
- [dolt](https://github.com/dolthub/dolt) - Dolt —— 数据界的 Git。
- [eliasdb](https://github.com/krotik/eliasdb) - 零依赖的事务型图数据库，提供 REST API、短语搜索与类 SQL 查询语言。
- [gedb](https://github.com/vinicius-lino-figueiredo/gedb) - 类 MongoDB 的嵌入式数据库，以纯 Go 编写。支持索引与复杂查询。
- [go-sqlite](https://github.com/glebarez/go-sqlite) 纯 Golang 实现、无需 CGO 的 SQLite 驱动。
- [godis](https://github.com/hdt3213/godis) - 用 Golang 实现的高性能 Redis 服务器与集群。
- [goleveldb](https://github.com/syndtr/goleveldb) - [LevelDB](https://github.com/google/leveldb) 键值数据库的 Go 实现。
- [hare](https://github.com/jameycribbs/hare) - 一个简单的数据库管理系统，将每张表存为按行分隔的 JSON 文本文件。
- [immudb](https://github.com/codenotary/immudb) - immudb 是面向 Go 编写的系统与应用打造的轻量、高速不可变数据库。
- [influxdb](https://github.com/influxdb/influxdb) - 面向指标、事件与实时分析的可扩展数据存储。
- [ledisdb](https://github.com/siddontang/ledisdb) - Ledisdb 是基于 LevelDB 的高性能类 Redis NoSQL 数据库。
- [levigo](https://github.com/jmhodges/levigo) - Levigo 是 LevelDB 的 Go 封装。
- [libradb](https://github.com/amit-davidson/LibraDB) - LibraDB 是一个不足 1000 行代码的简易数据库，适合学习。
- [LinDB](https://github.com/lindb/lindb) - LinDB 是可扩展、高性能、高可用的分布式时序数据库。
- [lotusdb](https://github.com/flower-corp/lotusdb) - 兼容 LSM 与 B+ 树的快速键值数据库。
- [lynxdb](https://github.com/lynxbase/lynxdb) - 轻量级列式日志分析数据库，配有受 SPL 启发的管道式查询语言。
- [MemHop](https://github.com/qyiun666/MemHop) - 面向 AI 智能体的嵌入式认知记忆数据库。六层架构（L0-L5）、Dream 整合管线、三通道 RRF 检索（BM25 + f16 向量 + 实体）、单一 .meh 文件、纯 Go、零基础设施。
- [Milvus](https://github.com/milvus-io/milvus) - Milvus 是用于嵌入管理、分析与搜索的向量数据库。
- [minisql](https://github.com/RichardKnop/minisql) - 嵌入式单文件 SQL 数据库。
- [moss](https://github.com/couchbase/moss) - Moss 是用 100% Go 编写的简易 LSM 键值存储引擎。
- [nanotdb](https://github.com/aymanhs/nanotdb) - 轻量、零依赖、仅追加的时序数据库与仪表盘，针对低功耗硬件优化。
- [NoKV](https://github.com/feichai0017/NoKV) - 面向分布式文件系统、对象存储与 AI 数据集负载的原生元数据服务。
- [NornicDB](https://github.com/orneryd/NornicDB) - 高性能图 + 向量数据库（兼容 Neo4j 与 qDrant），专注于为 AI 系统提供低延迟的 graph-rag 检索。
- [nutsdb](https://github.com/xujiajun/nutsdb) - Nutsdb 是用纯 Go 编写的简单、快速、可嵌入、持久化键值存储。支持完全可序列化事务，以及列表、集合、有序集合等多种数据结构。
- [objectbox-go](https://github.com/objectbox/objectbox-go) - 高性能嵌入式对象数据库（NoSQL），提供 Go API。
- [pebble](https://github.com/cockroachdb/pebble) - 受 RocksDB/LevelDB 启发的 Go 键值数据库。
- [piladb](https://github.com/fern4lvarez/piladb) - 基于栈式数据结构的轻量级 RESTful 数据库引擎。
- [pogreb](https://github.com/akrylysov/pogreb) - 面向读多写少负载的嵌入式键值存储。
- [prometheus](https://github.com/prometheus/prometheus) - 监控系统与时序数据库。
- [pudge](https://github.com/recoilme/pudge) - 仅使用 Go 标准库编写的快速简易键值存储。
- [redka](https://github.com/nalgeon/redka) - 用 SQLite 重新实现的 Redis。
- [rosedb](https://github.com/roseduan/rosedb) - 基于 LSM+WAL 的嵌入式键值数据库，支持 string、list、hash、set、zset。
- [rotom](https://github.com/xgzlucario/rotom) - 用 Golang 构建的迷你 Redis 服务器，兼容 RESP 协议。
- [rqlite](https://github.com/rqlite/rqlite) - 基于 SQLite 构建的轻量级分布式关系数据库。
- [tempdb](https://github.com/rafaeljesus/tempdb) - 用于临时条目的键值存储。
- [tidb](https://github.com/pingcap/tidb) - TiDB 是一个分布式 SQL 数据库，设计灵感来自 Google F1。
- [tiedot](https://github.com/HouzuoGuo/tiedot) - 由 Golang 驱动的你的 NoSQL 数据库。
- [unitdb](https://github.com/unit-io/unitdb) - 面向 IoT 与实时消息应用的快速时序数据库。通过 tcp 或 websocket 配合 pubsub 访问 unitdb，可使用 github.com/unit-io/unitd 应用。
- [Vasto](https://github.com/chrislusf/vasto) - 分布式高性能键值存储。落盘存储。最终一致性。高可用。可在服务不中断的情况下扩容或缩容。
- [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) - 快速、资源高效、可扩展的开源时序数据库。可用作 Prometheus 的长期远程存储，支持 PromQL。
- 
<a id="database-schema-migration"></a>
### 数据库模式迁移

- [atlas](https://github.com/ariga/atlas) - 一套数据库工具箱。为帮助企业更好地处理数据而设计的 CLI。
- [avro](https://github.com/khezen/avro) - 发现 SQL schema 并转换为 AVRO schema。将 SQL 记录查询为 AVRO 字节流。
- [bytebase](https://github.com/bytebase/bytebase) - 为 DevOps 团队提供安全的数据库结构变更与版本控制。
- [darwin](https://github.com/GuiaBolso/darwin) - Go 的数据库结构演进库。
- [db-migrator.go](https://github.com/raoptimus/db-migrator.go) - 面向版本化数据库结构迁移的 CLI，支持 PostgreSQL、MySQL、ClickHouse、Tarantool 与 Apache Iceberg。
- [dbmate](https://github.com/amacneil/dbmate) - 轻量级、与框架无关的数据库迁移工具。
- [go-fixtures](https://github.com/RichardKnop/go-fixtures) - 为 Golang 内置的 database/sql 库提供的 Django 风格 fixtures。
- [go-pg-migrate](https://github.com/lawzava/go-pg-migrate) - 便于 CLI 使用的 go-pg 迁移管理包。
- [go-pg-migrations](https://github.com/robinjoseph08/go-pg-migrations) - 帮助使用 go-pg/pg 编写迁移的 Go 包。
- [goavro](https://github.com/linkedin/goavro) - Avro 数据的编解码 Go 包。
- [godfish](https://github.com/rafaelespinoza/godfish) - 数据库迁移管理器，配合原生查询语言使用。支持 cassandra、mysql、postgres、sqlite3。
- [goose](https://github.com/pressly/goose) - 数据库迁移工具。你可以通过创建增量 SQL 或 Go 脚本来管理数据库的演进。
- [gorm-seeder](https://github.com/Kachit/gorm-seeder) - 面向 Gorm ORM 的简易数据库种子数据填充器。
- [gormigrate](https://github.com/go-gormigrate/gormigrate) - Gorm ORM 的数据库结构迁移辅助工具。
- [libschema](https://github.com/muir/libschema) - 在每个库中分别定义你的迁移。为开源库提供迁移。支持 MySQL 与 PostgreSQL。
- [migrate](https://github.com/golang-migrate/migrate) - 数据库迁移。提供 CLI 与 Golang 库。
- [migrator](https://github.com/lopezator/migrator) - 极简的 Go 数据库迁移库。
- [migrator](https://github.com/larapulse/migrator) - MySQL 数据库迁移器，用直观的 Go 代码执行迁移并管理数据库结构更新。
- [schema](https://github.com/adlio/schema) - 可将 schema 迁移嵌入 Go 二进制文件中、供 database/sql 兼容数据库使用的库。
- [skeema](https://github.com/skeema/skeema) - 面向 MySQL 的纯 SQL 结构管理系统，支持分片与外部在线结构变更工具。
- [soda](https://github.com/gobuffalo/pop/tree/master/soda) - 为 MySQL、PostgreSQL 与 SQLite 提供数据库迁移、创建、ORM 等能力。
- [sql-migrate](https://github.com/rubenv/sql-migrate) - 数据库迁移工具。支持使用 go-bindata 将迁移嵌入应用。
- [sqlize](https://github.com/sunary/sqlize) - 数据库迁移生成器。可通过对模型与已有 SQL 求差异来生成 SQL 迁移。

<a id="database-tools"></a>
### 数据库工具

- [chproxy](https://github.com/Vertamedia/chproxy) - ClickHouse 数据库的 HTTP 代理。
- [clickhouse-bulk](https://github.com/nikepan/clickhouse-bulk) - 收集小批量插入，向 ClickHouse 服务器发送大批量请求。
- [clickhouse-sql-parser](https://github.com/AfterShip/clickhouse-sql-parser) - ClickHouse 方言 SQL 解析器，产出类型化 AST，并提供遍历辅助、往返格式化与 CLI。
- [database-gateway](https://github.com/kazhuravlev/database-gateway) - 在生产环境运行 SQL，配备 ACL、日志与共享链接。
- [dbbench](https://github.com/sj14/dbbench) - 数据库基准测试工具，支持多种数据库与脚本。
- [dg](https://github.com/codingconcepts/dg) - 快速数据生成器，可从生成的关系型数据产出 CSV 文件。
- [filesql](https://github.com/nao1215/filesql) - 通过 database/sql API 用 SQL 查询 CSV、TSV、LTSV、JSON、JSONL、Parquet、Excel、ACH 与 Fedwire 文件，由内存 SQLite 支撑。
- [gatewayd](https://github.com/gatewayd-io/gatewayd) - 云原生数据库网关与框架，用于构建数据驱动应用。相当于数据库领域的 API 网关。
- [go-mysql](https://github.com/siddontang/go-mysql) - 用于处理 MySQL 协议与复制的 Go 工具集。
- [go-postgres-s3-backup](https://github.com/nicobistolfi/go-postgres-s3-backup) - 借助 AWS Lambda 将 PostgreSQL 无服务器备份到 S3，支持每日、每月与每年轮转。
- [gorm-multitenancy](https://github.com/bartventer/gorm-multitenancy) - 为 GORM 管理的数据库提供多租户支持。
- [GoSQLX](https://github.com/ajitpratap0/GoSQLX) - 高性能 SQL 解析器、格式化器、linter 与安全扫描器，支持多方言并附带 WASM  playground。
- [hasql](https://golang.yandex/hasql) - 用于访问多主机 SQL 数据库安装的库。
- [octillery](https://github.com/knocknote/octillery) - 数据库分片的 Go 包（支持任意 ORM 或原生 SQL）。
- [onedump](https://github.com/liweiyi88/onedump) - 用一条命令与一份配置，从不同驱动备份到不同目的地。
- [pg_timetable](https://github.com/cybertec-postgresql/pg_timetable) - 面向 PostgreSQL 的高级调度。
- [pgrwl](https://github.com/pgrwl/pgrwl) - 云原生的 PostgreSQL 持续备份方案。
- [pgwd](https://github.com/hrodrig/pgwd) - 监控 PostgreSQL 连接数（总数、活动、空闲、陈旧）的 CLI，超过阈值时经 Slack 和/或 Loki 通知。支持 Kubernetes（kubectl port-forward），并可在通知中附带运行上下文。
- [pgweb](https://github.com/sosedoff/pgweb) - 基于 Web 的 PostgreSQL 数据库浏览器。
- [pgxcli](https://github.com/Balaji01-4D/pgxcli) - 用 Go 编写的 PostgreSQL CLI 客户端，灵感源自 pgcli。
- [prep](https://github.com/hexdigest/prep) - 无需改动代码即可使用 SQL 预编译语句。
- [pREST](https://github.com/prest/prest) - 简化并加速开发，⚡ 即时、实时、高性能，可应用于任何既有或新建的 Postgres 应用。
- [rdb](https://github.com/HDT3213/rdb) - Redis RDB 文件解析器，用于二次开发与内存分析。
- [rwdb](https://github.com/andizzle/rwdb) - rwdb 为多数据库服务器部署提供只读副本能力。
- [sqly](https://github.com/nao1215/sqly) - 在交互式 shell 中对 CSV、TSV、LTSV、JSON、Parquet 与 Excel 文件执行 SQL，由内存 SQLite 支撑。
- [vitess](https://github.com/youtube/vitess) - Vitess 提供服务器与工具，便于面向大规模 Web 服务扩展 MySQL 数据库。
- [wescale](https://github.com/wesql/wescale) - WeScale 是一个数据库代理，旨在增强你的应用的可扩展性、性能、安全性与韧性。
- [xsql](https://github.com/zx06/xsql) - AI 优先的跨数据库 CLI 工具，具备只读保护与结构化 JSON 输出。

<a id="sql-query-builders"></a>
### SQL 查询构造器

_用于构建和使用 SQL 的库。_

- [bqb](https://github.com/nullism/bqb) - 轻量易学的查询构建器。
- [buildsqlx](https://github.com/arthurkushman/buildsqlx) - 面向 PostgreSQL 的 Go 数据库查询构建库。
- [builq](https://github.com/cristalhq/builq) - 在 Go 中轻松构建 SQL 查询。
- [dba](https://github.com/kran/dba) - 面向手写 SQL 的查询构建器，支持动态条件、方言感知占位符与不可变链式调用。
- [dbq](https://github.com/rocketlaunchr/dbq) - Go 的零样板数据库操作。
- [Dotsql](https://github.com/gchaincl/dotsql) - 帮你把 sql 文件集中管理并轻松使用的 Go 库。
- [gendry](https://github.com/didi/gendry) - 非侵入式 SQL 构建器与强大的数据绑定器。
- [godbal](https://github.com/xujiajun/godbal) - Go 的数据库抽象层（dbal）。支持 SQL 构建并轻松获取结果。
- [goqu](https://github.com/doug-martin/goqu) - 惯用的 SQL 构建器与查询库。
- [gosql](https://github.com/twharmon/gosql) - 对空值支持更友好的 SQL 查询构建器。
- [Hotcoal](https://github.com/motrboat/hotcoal) - 为手写 SQL 提供注入防护。
- [igor](https://github.com/galeone/igor) - 面向 PostgreSQL 的抽象层，支持高级功能并使用类 gorm 语法。
- [jet](https://github.com/go-jet/jet) - 用于在 Go 中编写类型安全 SQL 查询的框架，可轻松将数据库查询结果转换为任意目标对象结构。
- [obreron](https://github.com/profe-ajedrez/obreron) - 快速且低成本的 SQL 构建器，只专注做一件事：构建 SQL。
- [ormlite](https://github.com/pupizoid/ormlite) - 轻量包，为 sqlite 数据库提供部分类 ORM 特性与辅助工具。
- [ozzo-dbx](https://github.com/go-ozzo/ozzo-dbx) - 强大的数据获取方法，以及与数据库无关的查询构建能力。
- [patcher](https://github.com/Jacobbrewer1/patcher) - 强大的 SQL 查询构建器，可从结构体自动生成 SQL 查询。
- [qrafter](https://github.com/SennovE/qrafter) - 类型安全的 SQL 查询构建器，支持方言感知渲染、schema 自省与迁移生成。
- [qry](https://github.com/HnH/qry) - 从包含原生 SQL 查询的文件生成常量的工具。
- [relica](https://github.com/coregx/relica) - 类型安全的数据库查询构建器，零生产依赖，具备 LRU 语句缓存、批量操作，并支持 JOIN、子查询、CTE 与窗口函数。
- [sg](https://github.com/go-the-way/sg) - 用 Go 编写的标准 SQL 生成器（支持 CRUD）。
- [sq](https://github.com/bokwoon95/go-structured-query) - 面向 Go 的类型安全 SQL 构建器与结构体映射器。
- [sqlc](https://github.com/kyleconroy/sqlc) - 从 SQL 生成类型安全的代码。
- [sqlf](https://github.com/leporo/sqlf) - 快速 SQL 查询构建器。
- [sqlh](https://github.com/kirill-scherba/sqlh) - 零样板的 SQL 辅助工具，结合结构体标签与 Go 泛型（CRUD、UPSERT、JOIN、基准测试）。
- [sqlingo](https://github.com/lqs/sqlingo) - 在 Go 中构建 SQL 的轻量 DSL。
- [sqrl](https://github.com/elgris/sqrl) - SQL 查询构建器，是 Squirrel 的分支，性能更优。
- [Squalus](https://gitlab.com/qosenergy/squalus) - Go SQL 包之上的薄封装，让查询执行更轻松。
- [Squirrel](https://github.com/Masterminds/squirrel) - 帮助你构建 SQL 查询的 Go 库。
- [xo](https://github.com/knq/xo) - 基于既有 schema 定义或自定义查询生成惯用的 Go 数据库代码，支持 PostgreSQL、MySQL、SQLite、Oracle 与 Microsoft SQL Server。

**[⬆ 回到顶部](#contents)**

<a id="database-drivers"></a>
## 数据库驱动

<a id="interfaces-to-multiple-backends"></a>
### 多后端接口

- [cayley](https://github.com/google/cayley) - 支持多后端的图数据库。
- [dsc](https://github.com/viant/dsc) - 面向 SQL、NoSQL 与结构化文件的数据存储连接层。
- [dynamo](https://github.com/fogfish/dynamo) - 简单的键值抽象，用于在 AWS 存储服务（AWS DynamoDB 与 AWS S3）上存储代数数据类型与关联数据类型。
- [go-transaction-manager](https://github.com/avito-tech/go-transaction-manager) - 带多适配器（sql、sqlx、gorm、mongo 等）的事务管理器，统一控制事务边界。
- [gokv](https://github.com/philippgille/gokv) - Go 的简单键值存储抽象与实现（Redis、Consul、etcd、bbolt、BadgerDB、LevelDB、Memcached、DynamoDB、S3、PostgreSQL、MongoDB、CockroachDB 等等）。
- [transactor](https://github.com/metalfm/transactor) - 类型安全的事务边界抽象，提供 database/sql、sqlx 与 pgx 适配器。

<a id="relational-database-drivers"></a>
### 关系型数据库驱动

- [avatica](https://github.com/apache/calcite-avatica-go) - 面向 database/sql 的 Apache Avatica/Phoenix SQL 驱动。
- [bgc](https://github.com/viant/bgc) - 面向 BigQuery 的 Go 数据存储连接层。
- [firebirdsql](https://github.com/nakagami/firebirdsql) - Firebird RDBMS 的 Go SQL 驱动。
- [go-adodb](https://github.com/mattn/go-adodb) - 使用 database/sql 的 Microsoft ActiveX DataBase (ADO) 驱动。
- [go-mssqldb](https://github.com/denisenkom/go-mssqldb) - 面向 Go 的 Microsoft MSSQL 驱动。
- [go-mssqldb](https://github.com/microsoft/go-mssqldb) - 微软官方的 Go 驱动，支持 SQL Server、Azure SQL、Azure Synapse、Fabric 中的 SQL 数据库与 Fabric Data Warehouse。支持 Azure AD、Always Encrypted 与批量操作。
- [go-oci8](https://github.com/mattn/go-oci8) - 使用 database/sql 的 Go Oracle 驱动。
- [go-rqlite](https://github.com/rqlite/gorqlite) - rqlite 的 Go 客户端，为使用 rqlite API 提供易用的抽象。
- [go-sql-driver/mysql](https://github.com/go-sql-driver/mysql) - 面向 Go 的 MySQL 驱动。
- [go-sqlite3](https://github.com/mattn/go-sqlite3) - 使用 database/sql 的 Go SQLite3 驱动。
- [go-sqlite3](https://github.com/ncruces/go-sqlite3) - 该 Go 模块兼容 database/sql 驱动。它允许将 SQLite 嵌入你的应用，提供对其 C API 的直接访问，支持 SQLite VFS，并内置 GORM 驱动。
- [godror](https://github.com/godror/godror) - 面向 Go 的 Oracle 驱动，基于 ODPI-C 驱动实现。
- [gofreetds](https://github.com/minus5/gofreetds) - Microsoft MSSQL 驱动。对 [FreeTDS](https://www.freetds.org) 的 Go 封装。
- [KSQL](https://github.com/VinGarcia/ksql) - 简单而强大的 Golang SQL 库。
- [pgx](https://github.com/jackc/pgx) - PostgreSQL 驱动，支持超出 database/sql 所暴露范围的更多特性。
- [pig](https://github.com/alexeyco/pig) - 简单的 [pgx](https://github.com/jackc/pgx) 封装，便于执行查询并[扫描](https://github.com/georgysavva/scany)结果。
- [pq](https://github.com/lib/pq) - 面向 database/sql 的纯 Go Postgres 驱动。
- [Sqinn-Go](https://github.com/cvilsmeier/sqinn-go) - 以纯 Go 实现的 SQLite。
- [sqlhooks](https://github.com/qustavo/sqlhooks) - 为任意 database/sql 驱动挂载钩子。
- [sqlite](https://pkg.go.dev/modernc.org/sqlite) - sqlite 包是一个数据库驱动，基于 C SQLite3 库的无 CGO 移植版实现。
- [surrealdb.go](https://github.com/surrealdb/surrealdb.go) - SurrealDB 的 Go 驱动。
- [ydb-go-sdk](https://github.com/ydb-platform/ydb-go-sdk) - YDB（Yandex Database）的原生驱动与 database/sql 驱动。

<a id="nosql-database-drivers"></a>
### NoSQL 数据库驱动

- [aerospike-client-go](https://github.com/aerospike/aerospike-client-go) - Go 语言实现的 Aerospike 客户端。
- [arangolite](https://github.com/solher/arangolite) - 面向 ArangoDB 的轻量级 Golang 驱动。
- [asc](https://github.com/viant/asc) - 面向 Aerospike 的 Go 数据存储连接层。
- [forestdb](https://github.com/couchbase/goforestdb) - ForestDB 的 Go 绑定。
- [go-couchbase](https://github.com/couchbase/go-couchbase) - Go 语言实现的 Couchbase 客户端。
- [go-mongox](https://github.com/chenmingyong0423/go-mongox) - 基于官方驱动的 Go Mongo 库，提供精简的文档操作、结构体到集合的泛型绑定、内置 CRUD、聚合、自动字段更新、结构体校验、钩子与基于插件的编程。
- [go-pilosa](https://github.com/pilosa/go-pilosa) - 面向 Pilosa 的 Go 客户端库。
- [go-rejson](https://github.com/nitishm/go-rejson) - 使用 Redigo Golang 客户端访问 redislabs ReJSON 模块的客户端。可轻松在 Redis 中以 JSON 对象的形式存储与操作结构体。
- [gocb](https://github.com/couchbase/gocb) - 官方 Couchbase Go SDK。
- [gocosmos](https://github.com/btnguyen2k/gocosmos) - 面向 Azure Cosmos DB 的 REST 客户端与标准 `database/sql` 驱动。
- [gocql](https://gocql.github.io) - Apache Cassandra 的 Go 语言驱动。
- [godis](https://github.com/piaohao/godis) - 用 Golang 实现的 Redis 客户端，灵感源自 jedis。
- [godscache](https://github.com/defcronyke/godscache) - 对 Google Cloud Platform Go Datastore 包的封装，额外通过 memcached 增加缓存。
- [gomemcache](https://github.com/bradfitz/gomemcache/) - 面向 Go 编程语言的 memcache 客户端库。
- [gomemcached](https://github.com/aliexpressru/gomemcached) - 面向 Go 的二进制 Memcached 客户端，支持使用一致性哈希分片，并支持 SASL。
- [gorethink](https://github.com/dancannon/gorethink) - RethinkDB 的 Go 语言驱动。
- [goriak](https://github.com/zegl/goriak) - Riak KV 的 Go 语言驱动。
- [Kivik](https://github.com/go-kivik/kivik) - Kivik 为 CouchDB、PouchDB 等数据库提供统一的 Go 与 GopherJS 客户端库。
- [mgm](https://github.com/kamva/mgm) - 面向 Go 的基于模型的 MongoDB ODM（基于官方 MongoDB 驱动）。
- [mgo](https://github.com/globalsign/mgo) - （不再维护）面向 Go 语言的 MongoDB 驱动，以非常简洁的 API、遵循 Go 惯用法的方式实现了丰富且经过充分测试的特性集。
- [mongo-go-driver](https://github.com/mongodb/mongo-go-driver) - 面向 Go 语言的官方 MongoDB 驱动。
- [neo4j](https://github.com/cihangir/neo4j) - Neo4j REST API 的 Golang 绑定。
- [neoism](https://github.com/jmcvetta/neoism) - Golang 的 Neo4j 客户端。
- [qmgo](https://github.com/qiniu/qmgo) - Go 的 MongoDB 驱动。它基于官方 MongoDB 驱动，但像 Mgo 一样更易用。
- [redeo](https://github.com/bsm/redeo) - 兼容 Redis 协议的 TCP 服务器/服务。
- [redigo](https://github.com/gomodule/redigo) - Redigo 是 Redis 数据库的 Go 客户端。
- [redis](https://github.com/redis/go-redis) - Golang 的 Redis 客户端。
- [rueidis](http://github.com/rueian/rueidis) - 快速 Redis RESP3 客户端，支持自动流水线与服务端辅助的客户端侧缓存。
- [xredis](https://github.com/shomali11/xredis) - 类型安全、可自定义、干净且易用的 Redis 客户端。

<a id="search-and-analytic-databases"></a>
### 搜索与分析型数据库

- [clickhouse-go](https://github.com/ClickHouse/clickhouse-go/) - 面向 Go 的 ClickHouse SQL 客户端，兼容 `database/sql`。
- [effdsl](https://github.com/sdqri/effdsl) - 面向 Go 的 Elasticsearch 查询构建器。
- [elastic](https://github.com/olivere/elastic) - 面向 Go 的 Elasticsearch 客户端。
- [elasticsql](https://github.com/cch123/elasticsql) - 在 Go 中将 SQL 转换为 Elasticsearch DSL。
- [elastigo](https://github.com/mattbaird/elastigo) - Elasticsearch 客户端库。
- [go-elasticsearch](https://github.com/elastic/go-elasticsearch) - 面向 Go 的官方 Elasticsearch 客户端。
- [goes](https://github.com/OwnLocal/goes) - 用于与 Elasticsearch 交互的库。
- [skizze](https://github.com/skizzehq/skizze) - 一种概率型数据结构服务与存储。
- [zoekt](https://github.com/sourcegraph/zoekt) - 基于三元组的快速代码搜索。

**[⬆ 回到顶部](#contents)**

<a id="date-and-time"></a>
## 日期与时间

_用于处理日期与时间的库。_

- [approx](https://github.com/goschtalt/approx) - Duration 扩展，支持以天、周、年为单位解析与格式化时长。
- [carbon](https://github.com/dromara/carbon) - 为 Golang 打造的简单、语义化、对开发者友好的时间处理包。
- [carbon](https://github.com/uniplaces/carbon) - 简单的时间扩展，内置大量实用方法，移植自 PHP 的 Carbon 库。
- [cronrange](https://github.com/1set/cronrange) - 解析 Cron 风格的时间范围表达式，判断给定时间是否落在任一范围内。
- [date](https://github.com/rickb777/date) - 扩展 time 包，支持处理日期、日期区间、时间跨度、时间周期与一天中的时段。
- [dateparse](https://github.com/araddon/dateparse) - 无需预先了解格式即可解析日期。
- [durafmt](https://github.com/hako/durafmt) - Go 的时间时长格式化库。
- [feiertage](https://github.com/wlbr/feiertage) - 一组用于计算德国公共假期的函数，并对德国各联邦州（Bundesländer）做了专门处理。涵盖复活节、五旬节、感恩节等。
- [go-anytime](https://github.com/ijt/go-anytime) - 无需预先了解格式，即可解析「next dec 22nd at 3pm」这类日期时间，以及「from today until next thursday」这类区间。
- [go-date-fns](https://github.com/chmenegatti/go-date-fns) - 功能全面的 Go 日期工具库，灵感源自 date-fns，提供 140+ 个纯函数且不可变的函数。
- [go-datebin](https://github.com/deatil/go-datebin) - 简单的日期时间解析包。
- [go-faketime](https://github.com/harkaitz/go-faketime) - 简单的 `time.Now()`，兼容 faketime(1) 工具。
- [go-persian-calendar](https://github.com/yaa110/go-persian-calendar) - 波斯（Solar Hijri）日历在 Go (golang) 中的实现。
- [go-str2duration](https://github.com/xhit/go-str2duration) - 将字符串转换为 duration。支持由 time.Duration 返回的字符串等情况。
- [go-sunrise](https://github.com/nathan-osman/go-sunrise) - 计算给定位置的日出与日落时间。
- [go-week](https://github.com/stoewer/go-week) - 用于处理 ISO8601 周日期的高效包。
- [gostradamus](https://github.com/bykof/gostradamus) - 用于处理日期的 Go 包。
- [iso8601](https://github.com/relvacode/iso8601) - 无需正则即可高效解析 ISO8601 日期时间。
- [kair](https://github.com/GuilhermeCaruso/kair) - 日期与时间 —— Golang 格式化库。
- [now](https://github.com/jinzhu/now) - Now 是一套面向 Golang 的时间工具箱。
- [strftime](https://github.com/awoodbeck/strftime) - 兼容 C99 的 strftime 格式化器。
- [timespan](https://github.com/SaidinWoT/timespan) - 用于处理时间区间（由开始时间与时长定义）。
- [timeutil](https://github.com/leekchan/timeutil) - 对 Golang time 包的有用扩展（Timedelta、Strftime 等）。
- [tuesday](https://github.com/osteele/tuesday) - 兼容 Ruby 的 Strftime 函数。

**[⬆ 回到顶部](#contents)**

<a id="distributed-systems"></a>
## 分布式系统

_有助于构建分布式系统的软件包。_

- [arpc](https://github.com/lesismal/arpc) - 更有效的网络通信，支持双向调用、通知与广播。
- [bedrock](https://github.com/z5labs/bedrock) - 在 Go 中为快速开发服务及更多专用框架提供极简、模块化、可组合的基础设施。
- [capillaries](https://github.com/capillariesio/capillaries) - 分布式批量数据处理框架。
- [circuit](https://github.com/schigh/circuit) - 带渐进恢复（通过概率性节流）的熔断器。
- [cmd-stream-go](https://github.com/cmd-stream/cmd-stream-go) - 面向 Go 的高性能分布式命令模式库。
- [committer](https://github.com/vadiminshakov/committer) - 分布式事务管理系统（2PC/3PC 实现）。
- [consistent](https://github.com/buraksezer/consistent) - 带负载上限的一致性哈希。
- [consistenthash](https://github.com/mbrostami/consistenthash) - 副本数可配置的一致性哈希。
- [dht](https://github.com/anacrolix/dht) - BitTorrent Kademlia DHT 实现。
- [digota](https://github.com/digota/digota) - gRPC 电商微服务示例。
- [dot](https://github.com/dotchain/dot/) - 使用操作转换（OT）实现的分布式同步。
- [doublejump](https://github.com/edwingeng/doublejump) - Google Jump 一致性哈希的改良实现。
- [dragonboat](https://github.com/lni/dragonboat) - Go 中功能完整、高性能的多组 Raft 实现库。
- [Dragonfly](https://github.com/dragonflyoss/Dragonfly2) - 基于 P2P 技术提供高效、稳定、安全的文件分发与镜像加速，成为云原生架构下的最佳实践与标准方案。
- [drmaa](https://github.com/dgruber/drmaa) - 基于 DRMAA 标准的集群调度器作业提交库。
- [dynamolock](https://cirello.io/dynamolock) - 基于 DynamoDB 的分布式锁实现。
- [dynatomic](https://github.com/tylfin/dynatomic) - 用于将 DynamoDB 作为原子计数器的库。
- [emitter-io](https://github.com/emitter-io/emitter) - 基于 MQTT、WebSocket 与爱构建的高性能、分布式、安全、低延迟发布订阅平台。
- [evans](https://github.com/ktr0731/evans) - Evans：表达力更强的通用 gRPC 客户端。
- [failured](https://github.com/andy2046/failured) - 面向分布式系统的自适应时延故障检测器。
- [flowgraph](https://github.com/vectaport/flowgraph) - 基于流的编程包。
- [gleam](https://github.com/chrislusf/gleam) - 用纯 Go 与 LuaJIT 编写的快速可扩展分布式 map/reduce 系统，结合 Go 的高并发与 LuaJIT 的高性能，可独立运行也可分布式运行。
- [glow](https://github.com/chrislusf/glow) - 易用的可扩展分布式大数据处理方案，涵盖 Map-Reduce 与 DAG 执行，全部用纯 Go 实现。
- [gmsec](https://github.com/gmsec/micro) - Go 分布式系统开发框架。
- [go-doudou](https://github.com/unionj-cloud/go-doudou) - 基于 gossip 协议与 OpenAPI 3.0 规范的去中心化微服务框架。内置 go-doudou CLI，专注低代码与快速开发，能显著提升你的生产力。
- [go-eagle](https://github.com/go-eagle/eagle) - 用于构建 API 或微服务的 Go 框架，配备便捷的脚手架工具。
- [go-jump](https://github.com/dgryski/go-jump) - Google「Jump」一致性哈希函数的移植实现。
- [go-kit](https://github.com/go-kit/kit) - 微服务工具包，支持服务发现、负载均衡、可插拔传输、请求追踪等。
- [go-micro](https://github.com/micro/go-micro) - 分布式系统开发框架。
- [go-mysql-lock](https://github.com/sanketplus/go-mysql-lock) - 基于 MySQL 的分布式锁。
- [go-pdu](https://github.com/pdupub/go-pdu) - 去中心化的身份型社交网络。
- [go-sundheit](https://github.com/AppsFlyer/go-sundheit) - 为 Go 服务定义异步健康检查提供支持的库。
- [go-zero](https://github.com/tal-tech/go-zero) - Web 与 RPC 框架。它以弹性设计为保障高并发站点稳定性而生。内置 goctl，大幅提升开发效率。
- [gorpc](https://github.com/valyala/gorpc) - 简单、快速、可扩展的高负载 RPC 库。
- [grpc-go](https://github.com/grpc/grpc-go) - gRPC 的 Go 语言实现。基于 HTTP/2 的 RPC。
- [health](https://github.com/schigh/health) - 面向 Go 服务的健康检查器，支持 Kubernetes 探针。
- [hprose](https://github.com/hprose/hprose-golang) - 非常适合新手的 RPC 库，现已支持 25+ 种语言。
- [jsonrpc](https://github.com/osamingo/jsonrpc) - jsonrpc 包帮助实现 JSON-RPC 2.0。
- [jsonrpc](https://github.com/ybbus/jsonrpc) - JSON-RPC 2.0 HTTP 客户端实现。
- [K8gb](https://github.com/k8gb-io/k8gb) - 云原生的 Kubernetes 全局负载均衡器。
- [Kitex](https://github.com/cloudwego/kitex) - 高性能、高扩展性的 Golang RPC 框架，帮助开发者构建微服务。若在开发微服务时最看重性能与扩展性，Kitex 会是一个好选择。
- [Kratos](https://github.com/go-kratos/kratos) - Go 中模块化设计、易于使用的微服务框架。
- [liftbridge](https://github.com/liftbridge-io/liftbridge) - 面向 NATS 的轻量级容错消息流。
- [lock](https://github.com/ubgo/lock) - 分布式锁家族：统一 Go 接口，五种后端（filelock、flock、Redis、Postgres、etcd），支持 fencing token、信号量模式与可观测性钩子，覆盖所有后端。
- [lura](https://github.com/luraproject/lura) - 带中间件的超高性能 API 网关框架。
- [mochi mqtt](https://github.com/mochi-co/mqtt) - 完全符合规范、可嵌入的高性能 MQTT v5/v3 broker，面向 IoT、智能家居与发布订阅场景。
- [NATS](https://github.com/nats-io/nats-server) - NATS 是面向数字系统、服务与设备的简单、安全、高性能通信系统。
- [opentelemetry-go-auto-instrumentation](https://github.com/alibaba/opentelemetry-go-auto-instrumentation) - 面向 Golang 的 OpenTelemetry 编译期埋点。
- [oras](https://github.com/oras-project/oras) - 用于处理容器注册表中 OCI 制品的 CLI 与库。
- [outbox](https://github.com/oagudo/outbox) - Go 中事务性发件箱（outbox）模式的轻量库，不绑定任何特定关系型数据库或消息中间件。
- [outboxer](https://github.com/italolelis/outboxer) - Outboxer 是实现 outbox 模式的 Go 库。
- [pglock](https://cirello.io/pglock) - 基于 PostgreSQL 的分布式锁实现。
- [pjrpc](https://gitlab.com/pjrpc/pjrpc) - 采用 Protobuf 规范的 Golang JSON-RPC 服务端-客户端。
- [raft](https://github.com/hashicorp/raft) - 由 HashiCorp 提供的 Raft 共识协议 Go 实现。
- [raft](https://github.com/etcd-io/raft) - 由 CoreOS 提供的 Raft 共识协议 Go 实现。
- [rain](https://github.com/cenkalti/rain) - BitTorrent 客户端与库。
- [redis-lock](https://github.com/bsm/redislock) - 使用 Redis 的简化分布式锁实现。
- [resgate](https://resgate.io/) - 实时 API 网关，用于构建 REST、实时与 RPC API，所有客户端均可无缝同步。
- [rpcplatform](https://github.com/nexcode/rpcplatform) - 微服务框架，具备服务发现、负载均衡等相关能力。
- [rpcx](https://github.com/smallnest/rpcx) - 类似阿里 Dubbo 的分布式可插拔 RPC 服务框架。
- [Semaphore](https://github.com/jexia/semaphore) - 直观的（微）服务编排器。
- [servicepack](https://github.com/psyb0t/servicepack) - 在单个二进制中并发运行多个服务的框架，可本地运行，也可跨机器分布式运行。
- [sleuth](https://github.com/ursiform/sleuth) - 用于 HTTP 服务之间无主 P2P 自动发现与 RPC 的库（基于 [ZeroMQ](https://github.com/zeromq/libzmq)）。
- [sponge](https://github.com/zhufuyi/sponge) - 集成了代码自动生成、gin 与 grpc 框架及基础开发框架的分布式开发框架。
- [Tarmac](https://github.com/tarmac-project/tarmac) - 使用 WebAssembly 编写函数、微服务或单体应用的框架。
- [Temporal](https://github.com/temporalio/sdk-go) - 持久化执行系统，让代码具备容错能力并保持简单。
- [torrent](https://github.com/anacrolix/torrent) - BitTorrent 客户端包。
- [trpc-go](https://github.com/trpc-group/trpc-go) - tRPC 的 Go 语言实现，这是一个可插拔的高性能 RPC 框架。

**[⬆ 回到顶部](#contents)**

<a id="dynamic-dns"></a>
## 动态 DNS

_用于更新动态 DNS 记录的工具。_

- [DDNS](https://github.com/skibish/ddns) - 以 Digital Ocean Networking DNS 为后端的个人 DDNS 客户端。
- [dyndns](https://gitlab.com/alcastle/dyndns) - 后台 Go 进程，定期自动检查你的 IP 地址，并在地址变化时更新 Google 域名下（一条或多条）动态 DNS 记录。
- [GoDNS](https://github.com/timothyye/godns) - 动态 DNS 客户端工具，支持 DNSPod 与 HE.net，用 Go 编写。

**[⬆ 回到顶部](#contents)**

<a id="email"></a>
## 邮件

_实现邮件创建与发送的库与工具。_

- [chasquid](https://blitiri.com.ar/p/chasquid) - 用 Go 编写的 SMTP 服务器。
- [douceur](https://github.com/aymerick/douceur) - 为 HTML 邮件内联 CSS 的工具。
- [email](https://github.com/jordan-wright/email) - 稳健而灵活的 Go 邮件库。
- [email-verifier](https://github.com/AfterShip/email-verifier) - 一个无需实际发送邮件即可完成邮箱验证的 Go 库。
- [go-dkim](https://github.com/toorop/go-dkim) - DKIM 库，用于签名与验证邮件。
- [go-email-normalizer](https://github.com/dimuska139/go-email-normalizer) - 为邮箱地址提供规范化表示的 Golang 库。
- [go-imap](https://github.com/BrianLeishman/go-imap) - 开箱即用的 IMAP 客户端，支持自动重连、OAuth2、IDLE 与内置 MIME 解析。
- [go-imap](https://github.com/emersion/go-imap) - 面向客户端与服务器的 IMAP 库。
- [go-mail](https://github.com/wneessen/go-mail) - 用于在 Go 中发送邮件的简单库。
- [go-message](https://github.com/emersion/go-message) - 面向互联网消息格式（IMF）与邮件消息的流式处理库。
- [go-premailer](https://github.com/vanng822/go-premailer) - 在 Go 中为 HTML 邮件提供内联样式。
- [go-simple-mail](https://github.com/xhit/go-simple-mail) - 极简的邮件发送包，基于 SMTP Keep Alive，并提供连接与发送两个超时设置。
- [go-spamcheck](https://github.com/psyb0t/go-spamcheck) - Postmark SpamCheck API 客户端，依据 SpamAssassin 规则为原始邮件评分。
- [Hectane](https://github.com/hectane/hectane) - 轻量级 SMTP 客户端，提供 HTTP API。
- [hermes](https://github.com/matcornic/hermes) - 生成整洁、响应式 HTML 邮件的 Golang 包。
- [Maddy](https://github.com/foxcpp/maddy) - 一体化邮件服务器（SMTP、IMAP、DKIM、DMARC、MTA-STS、DANE）。
- [mailchain](https://github.com/mailchain/mailchain) - 用 Go 编写，向区块链地址发送加密邮件。
- [mailgun-go](https://github.com/mailgun/mailgun-go) - 通过 Mailgun API 发送邮件的 Go 库。
- [MailHog](https://github.com/mailhog/MailHog) - 带 Web 界面与 API 的邮件与 SMTP 测试工具。
- [Mailpit](https://github.com/axllent/mailpit) - 面向开发者的邮件与 SMTP 测试工具。
- [mailx](https://github.com/valord577/mailx) - Mailx 让通过 SMTP 发送邮件变得更容易。它是 Golang 标准库 `net/smtp` 的增强版。
- [mox](https://github.com/mjl-/mox) - 现代化、功能完整的安全邮件服务器，适合低维护的自托管邮件场景。
- [SendGrid](https://github.com/sendgrid/sendgrid-go) - SendGrid 的 Go 发信库。
- [smtp](https://github.com/mailhog/smtp) - SMTP 服务器协议状态机。
- [smtpmock](https://github.com/mocktools/go-smtp-mock) - 轻量级、可配置、多线程的假 SMTP 服务器。为测试环境模拟任意 SMTP 行为。
- [tickstem/verify](https://github.com/tickstem/verify) - 在邮箱进入数据库之前先做校验：语法、MX 查询、一次性域名与角色邮箱。
- [truemail-go](https://github.com/truemail-rb/truemail-go) - 可配置的 Golang 邮箱校验器。通过正则、DNS、SMTP 等多种方式验证邮箱。

**[⬆ 回到顶部](#contents)**

<a id="embeddable-scripting-languages"></a>
## 可嵌入式脚本语言

_在 Go 代码中嵌入其他语言。_

- [anko](https://github.com/mattn/anko) - 用 Go 编写的可脚本化解释器。
- [binder](https://github.com/alexeyco/binder) - Go 到 Lua 的绑定库，基于 [gopher-lua](https://github.com/yuin/gopher-lua)。
- [cel-go](https://github.com/google/cel-go) - 快速、可移植、非图灵完备的表达式求值引擎，支持渐进式类型。
- [ecal](https://github.com/krotik/ecal) - 简单可嵌入的脚本语言，支持并发事件处理。
- [expr](https://github.com/antonmedv/expr) - 面向 Go 的表达式求值引擎：快速、非图灵完备、兼具动态与静态类型。
- [FrankenPHP](https://github.com/dunglas/frankenphp) - 嵌入 Go 的 PHP，附带 `net/http` 处理器。
- [gentee](https://github.com/gentee/gentee) - 可嵌入的脚本编程语言。
- [gisp](https://github.com/jcla1/gisp) - 用 Go 实现的简易 LISP。
- [go-lua](https://github.com/Shopify/go-lua) - Lua 5.2 虚拟机到纯 Go 的移植。
- [go-lua](https://github.com/speedata/go-lua) - 用纯 Go 实现的 Lua 5.4 虚拟机。
- [go-php](https://github.com/deuill/go-php) - Go 的 PHP 绑定。
- [goal](https://codeberg.org/anaseto/goal) - 一种可嵌入的脚本化数组语言。
- [goja](https://github.com/dop251/goja) - Go 实现的 ECMAScript 5.1(+) 引擎。
- [golua](https://github.com/aarzilli/golua) - Go 对 Lua C API 的绑定。
- [gopher-lua](https://github.com/yuin/gopher-lua) - 用 Go 编写的 Lua 5.1 虚拟机与编译器。
- [gval](https://github.com/PaesslerAG/gval) - 用 Go 编写的、定制性极强的表达式语言。
- [metacall](https://github.com/metacall/core) - 跨平台多语言运行时，支持 NodeJS、JavaScript、TypeScript、Python、Ruby、C#、WebAssembly、Java、Cobol 等。
- [ngaro](https://github.com/db47h/ngaro) - 可嵌入的 Ngaro 虚拟机实现，可在 Retro 中编写脚本。
- [prolog](https://github.com/ichiban/prolog) - 可嵌入的 Prolog。
- [purl](https://github.com/ian-kent/purl) - 嵌入 Go 的 Perl 5.18.2。
- [starlark-go](https://github.com/google/starlark-go) - Starlark 的 Go 实现：一种类 Python 语言，具备确定性求值与密封式执行。
- [starlet](https://github.com/1set/starlet) - [starlark-go](https://github.com/google/starlark-go) 的 Go 封装，简化脚本执行、提供数据转换以及实用的 Starlark 库与扩展。
- [tengo](https://github.com/d5/tengo) - 面向 Go 的字节码编译型脚本语言。
- [Wa/凹语言](https://github.com/wa-lang/wa) - 嵌入 Go 的 Wa 编程语言。

**[⬆ 回到顶部](#contents)**

<a id="error-handling"></a>
## 错误处理

_用于错误处理的库。_

- [ctxerrors](https://github.com/psyb0t/ctxerrors) - 为错误包装上每个调用点的文件、行号与函数名。
- [emperror](https://github.com/emperror/emperror) - Go 库与应用的错误处理工具与最佳实践。
- [eris](https://github.com/rotisserie/eris) - 在 Go 中处理、追踪与记录错误的更好方式。兼容标准 error 库与 github.com/pkg/errors。
- [errlog](https://github.com/snwfdhmp/errlog) - 可改造的错误包，能定位引发错误的源码位置（并提供其他快速调试特性）。可即插即用接入任意日志器。
- [errors](https://github.com/emperror/errors) - 标准库 errors 包与 github.com/pkg/errors 的直接替代品。提供多种错误处理原语。
- [errors](https://github.com/neuronlabs/errors) - 带分类原语的 Golang 简易错误处理。
- [errors](https://github.com/PumpkinSeed/errors) - 最简单的错误包装器，性能出色、内存开销极小。
- [errors](https://gitlab.com/tozd/go/errors) - 为错误提供堆栈追踪与可选的结构化详情。API 兼容 github.com/pkg/errors，但内部并未使用它。
- [errors](https://github.com/naughtygopher/errors) - Go 内置 errors 的直接替代品。这是一个极简错误处理包，带自定义错误类型、友好的错误信息、Unwrap 与 Is，并配有非常易用的辅助函数。
- [errors](https://github.com/cockroachdb/errors) - Go 错误库，支持错误的网络可移植性。
- [errorx](https://github.com/joomcode/errorx) - 功能丰富的错误包，带堆栈追踪、错误组合等能力。
- [exception](https://github.com/rbrahul/exception) - 为 Golang 提供 try-catch 式异常处理的简易工具包。
- [Falcon](https://github.com/SonicRoshan/falcon) - 一个简单却非常强大的错误处理包。
- [Fault](https://github.com/Southclaws/fault) - 符合人体工学的错误包装机制，便于为错误值附加结构化元数据与上下文。
- [go-errr](https://github.com/go-errr/go) - Go 的错误处理库，具备 Catch/Recover 语义、错误链包装与堆栈追踪。
- [go-multierror](https://github.com/hashicorp/go-multierror) - Go (golang) 包，用于把一组错误表示为单个错误。
- [metaerr](https://github.com/quantumcycle/metaerr) - 用于创建自定义错误构造器的库，可从不同来源生成带元数据的结构化错误，并可选附加堆栈追踪。
- [multierr](https://github.com/uber-go/multierr) - 用于把一组错误表示为单个错误的包。
- [oops](https://github.com/samber/oops) - 带上下文、堆栈追踪与源码片段的错误处理。
- [tracerr](https://github.com/ztrue/tracerr) - 带堆栈追踪与源码片段的 Golang 错误处理。

**[⬆ 回到顶部](#contents)**

<a id="file-handling"></a>
## 文件处理

_用于处理文件与文件系统的库。_

- [afero](https://github.com/spf13/afero) - Go 的文件系统抽象体系。
- [afs](https://github.com/viant/afs) - Go 的抽象文件存储层（内存、scp、zip、tar、云端 s3、gs）。
- [baraka](https://github.com/xis/baraka) - 轻松处理 HTTP 文件上传的库。
- [checksum](https://github.com/codingsince1985/checksum) - 为大文件计算消息摘要，如 MD5、SHA256、SHA1、CRC 或 BLAKE2s。
- [copy](https://github.com/otiai10/copy) - 递归复制目录。
- [fastwalk](https://github.com/charlievieth/fastwalk) - 快速并行目录遍历库（被 [fzf](https://github.com/junegunn/fzf) 使用）。
- [flop](https://github.com/homedepot/flop) - 文件操作库，力求在功能上对齐 [GNU cp](https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html)。
- [gdu](https://github.com/dundee/gdu) - 带控制台界面的磁盘用量分析工具。
- [go-csv-tag](https://github.com/artonge/go-csv-tag) - 使用标签加载 csv 文件。
- [go-decent-copy](https://github.com/hugocarreira/go-decent-copy) - 为人类设计的文件复制工具。
- [go-exiftool](https://github.com/barasher/go-exiftool) - ExifTool 的 Go 绑定。该库以尽可能多地从文件（图片、PDF、办公文档等）中提取元数据（EXIF、IPTC 等）而闻名。
- [go-gtfs](https://github.com/artonge/go-gtfs) - 在 Go 中加载 GTFS 文件。
- [go-wkhtmltopdf](https://github.com/SebastiaanKlippert/go-wkhtmltopdf) - 将 HTML 模板转换为 PDF 文件的包。
- [gofs](https://github.com/no-src/gofs) - 开箱即用的跨平台实时文件同步工具。
- [gopdfrab](https://github.com/voidrab/gopdfrab) - Go 的 PDF/A 处理库。
- [gulter](https://github.com/adelowo/gulter) - 简易 HTTP 中间件，自动处理所有文件上传需求。
- [gut/yos](https://github.com/1set/gut) - 简单可靠的文件操作包，支持对文件、目录与符号链接进行复制/移动/比较/列举等操作。
- [gxpdf](https://github.com/coregx/gxpdf) - 现代化的 Go 全生命周期 PDF 库 —— 解析、提取表格、生成与签名文档，零 CGO 依赖。
- [higgs](https://github.com/dastoori/higgs) - 一个小型跨平台 Go 库，用于隐藏/取消隐藏文件与目录。
- [iso9660](https://github.com/kdomanski/iso9660) - 用于读取与创建 ISO9660 磁盘映像的包。
- [notify](https://github.com/rjeczalik/notify) - 文件系统事件通知库，API 简洁，类似于 os/signal。
- [opc](https://github.com/qmuntal/opc) - Go 的 Open Packaging Conventions (OPC) 文件加载支持。
- [parquet](https://github.com/parsyl/parquet) - 读写 [parquet](https://parquet.apache.org) 文件。
- [pathtype](https://github.com/jonchun/pathtype) - 把路径当作独立类型来处理，而非使用字符串。
- [pdfcpu](https://github.com/pdfcpu/pdfcpu) - PDF 处理器。
- [skywalker](https://github.com/dixonwille/skywalker) - 让人能够轻松并发遍历文件系统的包。
- [todotxt](https://github.com/1set/todotxt) - Gina Trapani 的 [_todo.txt_](http://todotxt.org/) 文件 Go 库，支持解析与操作 [_todo.txt_ 格式](https://github.com/todotxt/todo.txt)的任务列表。
- [vfs](https://github.com/C2FO/vfs) - 面向 Go 的可插拔、可扩展且有明确主张的文件系统功能集，覆盖 os、S3、GCS 等多种文件系统类型。

**[⬆ 回到顶部](#contents)**

<a id="financial"></a>
## 金融

_用于会计与金融的软件包。_

- [accounting](https://github.com/leekchan/accounting) - 面向 golang 的金额与货币格式化。
- [ach](https://github.com/moov-io/ach) - 面向自动化清算所（ACH）文件的读取器、写入器与校验器。
- [bbgo](https://github.com/c9s/bbgo) - 用 Go 编写的加密货币交易机器人框架。内置常用交易所 API、标准技术指标、回测以及众多内置策略。
- [bingx-go](https://github.com/tigusigalpa/bingx-go) - 面向 BingX API v3 的 Go 客户端，提供 260+ 方法、USDT-M/Coin-M 合约、现货、TradFi、WebSocket 行情流与跟单交易。
- [bitget-go](https://github.com/tigusigalpa/bitget-go) - 面向 Bitget UTA API v3 的 Go 客户端，带类型化模型、字符串类型价格、自动重连 WebSocket 与模拟交易。
- [bybit-go](https://github.com/tigusigalpa/bybit-go) - 面向 Bybit V5 API 的 Go 客户端，支持 HMAC/RSA 认证、WebSocket 行情流、模拟交易与 TradFi 交易品种。
- [cnn-fear-and-greed-parse](https://github.com/wildsurfer/cnn-fear-and-greed-parse) - CNN 恐惧与贪婪指数客户端，含七项成分指标与约一年的每日历史数据。
- [currency](https://github.com/bojanz/currency) - 处理货币金额，提供货币信息与格式化。
- [currency](https://github.com/naughtygopher/currency) - 高性能且精确的货币计算包。
- [dec128](https://github.com/jokruger/dec128) - 高性能的 128 位定点十进制数。
- [decimal](https://github.com/shopspring/decimal) - 任意精度定点十进制数。
- [decimal](https://github.com/aytechnet/decimal) - 高性能 64 位十进制数，部分兼容 [shopspring/decimal](https://github.com/shopspring/decimal) 与 int64，含重量与长度单位。
- [decimal](https://github.com/govalues/decimal) - 不可变十进制数，算术运算不会 panic。
- [decimal](https://github.com/klokare/decimal) - 固定大小、零分配的小数类型，适用于不需要任意精度的场景。
- [eu-vat-rates-data-go](https://github.com/vatnode/eu-vat-rates-data-go) - 内置 45 个欧洲国家的增值税率与增值税号格式，编译期嵌入并每日从欧盟委员会 TEDB 刷新。
- [fpdecimal](https://github.com/nikolaydubina/fpdecimal) - 面向小型定点十进制数的快速精确序列化与算术运算。
- [fpmoney](https://github.com/nikolaydubina/fpmoney) - 快速简洁的 ISO4217 定点金额实现。
- [glassnode-go](https://github.com/tigusigalpa/glassnode-go) - 面向 Glassnode Basic API 的 Go 客户端，含 25 类指标、类型化结构体、批量接口、时点数据，且零依赖。
- [go-finance](https://github.com/alpeb/go-finance) - 金融函数库，涵盖货币时间价值（年金）、现金流、利率换算、债券与折旧计算。
- [go-finance](https://github.com/pieterclaerhout/go-finance) - 用于获取汇率、通过 VIES 校验增值税号以及校验 IBAN 银行账号的模块。
- [go-money](https://github.com/rhymond/go-money) - Fowler's Money 模式的实现。
- [go-nowpayments](https://github.com/matm/go-nowpayments) - NOWPayments 加密货币 API 的库。
- [gobl](https://github.com/invopop/gobl) - 发票与账单文档框架。基于 JSON Schema。自动完成税额计算与校验，并提供转换为各国格式的工具。
- [indicator](https://github.com/cinar/indicator) - 技术分析库，提供金融指标、策略与回测框架。
- [kucoin-go](https://github.com/tigusigalpa/kucoin-go) - 面向 KuCoin UTA 与 Classic REST 及 WebSocket API 的 Go 客户端，支持 HMAC-SHA256 认证、字符串类型价格与类型化错误层级。
- [ledger](https://github.com/formancehq/ledger) - 可编程的财务账本，为资金流转类应用提供基础。
- [money](https://github.com/govalues/money) - 不可变金额与汇率，算术运算不会 panic。
- [ofxgo](https://github.com/aclindsa/ofxgo) - 查询 OFX 服务器并/或解析其响应（附示例命令行客户端）。
- [okx-go](https://github.com/tigusigalpa/okx-go) - 面向 OKX v5 API 的 Go 客户端，含 335 个 REST 接口、53 个 WebSocket 频道、泛型支持与自动重连。
- [orderbook](https://github.com/i25959341/orderbook) - Golang 实现的限价订单簿撮合引擎。
- [orderbook](https://github.com/intrepidkarthi/orderbook) - 可嵌入的限价订单簿与撮合引擎，具备整数精确定价、单写入者核心与预写日志崩溃恢复。
- [payme](https://github.com/jovandeginste/payme) - 面向 SEPA 支付的二维码生成器（ASCII 与 PNG）。
- [paystack-sdk-go](https://github.com/samaasi/paystack-sdk-go) - 功能完备、零依赖、完全类型化的 Paystack API Go SDK。
- [swift](https://code.pfad.fr/swift/) - 离线校验 IBAN（国际银行账号）并获取 BIC（支持部分国家）。
- [techan](https://github.com/sdcoffey/techan) - 技术分析库，提供高级市场分析与交易策略。
- [telegram-wallet-go](https://github.com/tigusigalpa/telegram-wallet-go) - 面向 Telegram Wallet Pay API 的 Go 客户端，支持 HMAC-SHA256 Webhook 验签，以及 net/http、Gin、Echo 中间件。
- [ticker](https://github.com/achannarasappa/ticker) - 终端股票监视器与持仓追踪工具。
- [transaction](https://github.com/claygod/transaction) - 账户嵌入式事务数据库，以多线程模式运行。
- [udecimal](https://github.com/quagmt/udecimal) - 面向金融应用的高性能、高精度、零分配定点十进制库。
- [vat](https://github.com/dannyvankooten/vat) - 增值税号校验与欧盟增值税率。

**[⬆ 回到顶部](#contents)**

<a id="forms"></a>
## 表单

_用于处理表单的库。_

- [bind](https://github.com/robfig/bind) - 把表单数据绑定到任意 Go 值。
- [conform](https://github.com/leebenson/conform) - 约束用户输入，依据结构体标签完成裁剪、清洗与净化。
- [form](https://github.com/go-playground/form) - 将 url.Values 解码为 Go 值，并将 Go 值编码为 url.Values。同时支持数组与完整 map。
- [formam](https://github.com/monoculum/formam) - 把表单值解码进结构体。
- [forms](https://github.com/albrow/forms) - 与框架无关的表单/JSON 数据解析与校验库，支持 multipart 表单与文件。
- [gbind](https://github.com/bdjimmy/gbind) - 把数据绑定到任意 Go 值。可使用内置与自定义的表达式绑定能力，并支持数据校验。
- [gorilla/csrf](https://github.com/gorilla/csrf) - 面向 Go Web 应用与服务的 CSRF 防护。
- [httpin](https://github.com/ggicci/httpin) - 将 HTTP 请求解码进自定义结构体，涵盖查询字符串、表单、HTTP 头部等。
- [nosurf](https://github.com/justinas/nosurf) - Go 的 CSRF 防护中间件。
- [qs](https://github.com/sonh/qs) - 把结构体编码为 URL 查询参数的 Go 模块。
- [queryparam](https://github.com/tomwright/queryparam) - 将 `url.Values` 解码为可直接使用的标准或自定义类型结构体值。
- [roamer](https://github.com/slipros/roamer) - 通过简单的标签把 Cookie、头部、查询参数、路径参数与请求体绑定到结构体等目标上，消除 HTTP 请求解析的样板代码。

**[⬆ 回到顶部](#contents)**

<a id="functional"></a>
## 函数式

_支持 Go 函数式编程的软件包。_

- [fp-go](https://github.com/repeale/fp-go) - 由 Golang 1.18+ 泛型驱动的一系列函数式编程辅助工具。
- [fpGo](https://github.com/TeaEntityLab/fpGo) - 为 Golang 带来的 Monad 与函数式编程特性。
- [fuego](https://github.com/seborama/fuego) - Go 中的函数式编程实验。
- [FuncFrog](https://github.com/koss-null/FuncFrog) - 函数式辅助库，为 Go1.18+ 泛型切片提供 Map、Filter、Reduce 等流式操作，并支持惰性求值与错误处理机制。
- [g](https://github.com/enetx/g) - 面向 Go 的函数式编程框架。
- [go-functional](https://github.com/BooleanCat/go-functional) - 用泛型在 Go 中做函数式编程。
- [go-underscore](https://github.com/tobyhede/go-underscore) - 一批实用且贴心的 Go 函数式集合工具。
- [gofp](https://github.com/rbrahul/gofp) - 类 lodash 的强大 Golang 工具库。
- [mo](https://github.com/samber/mo) - 基于 Go 1.18+ 泛型的 Monad 与常见函数式抽象（Option、Result、Either 等）。
- [underscore](https://github.com/rjNemo/underscore) - 面向 Go 1.18 及更高版本的函数式编程辅助工具。
- [valor](https://github.com/phelmkamp/valor) - 泛型 option 与 result 类型，可选地包含一个值。

**[⬆ 回到顶部](#contents)**

<a id="game-development"></a>
## 游戏开发

_优秀的游戏开发库。_

- [Ark](https://github.com/mlange-42/ark) - 基于原型的实体组件系统（ECS），用 Go 实现。
- [due](https://github.com/dobyte/due) - 分布式游戏服务器框架，采用模块化组件设计，提供 tcp、kcp、ws 与 quic 网关。
- [Ebitengine](https://github.com/hajimehoshi/ebiten) - Go 中极简的 2D 游戏引擎。
- [ecs](https://github.com/andygeiss/ecs) - 在 Golang 中基于实体组件系统（ECS）理念构建你自己的游戏引擎。
- [engo](https://github.com/EngoEngine/engo) - Engo 是用 Go 编写的开源 2D 游戏引擎，遵循实体-组件-系统范式。
- [fantasyname](https://github.com/s0rg/fantasyname) - 奇幻名字生成器。
- [g3n](https://github.com/g3n/engine) - Go 3D 游戏引擎。
- [go-astar](https://github.com/beefsack/go-astar) - A\* 寻路算法的 Go 实现。
- [go-sdl2](https://github.com/veandco/go-sdl2) - [Simple DirectMedia Layer](https://www.libsdl.org/) 的 Go 绑定。
- [go3d](https://github.com/ungerik/go3d) - 面向 Go、注重性能的 2D/3D 数学包。
- [gogpu](https://github.com/gogpu/gogpu) - 基于 WebGPU 的 GPU 应用框架，内置窗口、输入与渲染 —— 把 480 多行 GPU 代码压缩到约 20 行，零 CGO（GoGPU 生态：[gg](https://github.com/gogpu/gg)、[ui](https://github.com/gogpu/ui)、[wgpu](https://github.com/gogpu/wgpu)、[naga](https://github.com/gogpu/naga)）。
- [gogpu/wgpu](https://github.com/gogpu/wgpu) - 纯 Go 的 WebGPU 实现，带 Vulkan、DX12 与 Metal 后端，零 CGO（[GoGPU](https://github.com/gogpu) 生态的一部分）。
- [GOKe](https://github.com/kjkrol/goke) - 数据导向（DOD）、基于原型的 ECS 引擎，采用 L1 缓存对齐的分块 SoA 布局，实现可预期的无级内存增长与零分配执行路径。
- [gonet](https://github.com/xtaci/gonet) - 用 golang 实现的游戏服务器骨架。
- [goworld](https://github.com/xiaonanln/goworld) - 可扩展的游戏服务器引擎，具备 space-entity 框架与热替换能力。
- [grid](https://github.com/s0rg/grid) - 通用 2D 网格，支持光线投射、阴影投射与寻路。
- [Leaf](https://github.com/name5566/leaf) - 轻量级游戏服务器框架。
- [nano](https://github.com/lonng/nano) - 轻量级、设施完备、高性能、基于 golang 的游戏服务器框架。
- [Oak](https://github.com/oakmound/oak) - 纯 Go 游戏引擎。
- [Pi](https://github.com/elgopher/pi) - 为现代电脑打造复古游戏的游戏引擎。灵感源自 Pico-8，由 Ebitengine 驱动。
- [Pitaya](https://github.com/topfreegames/pitaya) - 可扩展的游戏服务器框架，支持集群，并可通过 C SDK 为 iOS、Android、Unity 等平台提供客户端库。
- [Pixel](https://github.com/gopxl/pixel) - Go 中手工打造的 2D 游戏库。
- [prototype](https://github.com/gonutz/prototype) - 跨平台（Windows/Linux/Mac）库，以极简 API 创建桌面游戏。
- [raylib-go](https://github.com/gen2brain/raylib-go) - [raylib](https://www.raylib.com/) 的 Go 绑定 —— 一个简单易用、适合学习游戏编程的库。
- [sceneCamera](https://github.com/donomii/sceneCamera) - 面向博物馆、FPS、RTS 与立体渲染模式的相机移动与视图/投影矩阵。
- [termloop](https://github.com/JoelOtter/termloop) - 面向 Go 的终端游戏引擎，构建于 Termbox 之上。
- [tile](https://github.com/kelindar/tile) - 数据导向、对缓存友好的 2D 网格库（TileMap），包含寻路、观察者以及导入导出。

**[⬆ 回到顶部](#contents)**

<a id="generators"></a>
## 代码生成器

_用于生成 Go 代码的工具。_

- [apispec](https://github.com/ehabterra/apispec) - 无需注解即可从 Go 代码生成 OpenAPI 3.1 规范，并附带浏览器界面用于配置、预览与探索调用图。
- [convergen](https://github.com/reedom/convergen) - 功能丰富的类型到类型代码拷贝生成器。
- [copygen](https://github.com/switchupcb/copygen) - 基于 Go 类型生成任意代码，包括默认不依赖反射的类型到类型转换器（拷贝代码）。
- [generis](https://github.com/senselogic/GENERIS) - 代码生成工具，提供泛型、自由形式宏、条件编译与 HTML 模板。
- [go-apispec](https://github.com/antst/go-apispec) - 通过静态分析从 Go 源码生成 OpenAPI 3.1 规范，并自动检测所用框架。
- [go-enum](https://github.com/abice/go-enum) - 依据代码注释生成枚举。
- [go-enum-encoding](https://github.com/nikolaydubina/go-enum-encoding) - 依据代码注释生成枚举编码逻辑。
- [go-linq](https://github.com/ahmetalpbalkan/go-linq) - 为 Go 提供的类 .NET LINQ 查询方法。
- [goderive](https://github.com/awalterschulze/goderive) - 从输入类型推导出函数。
- [goverter](https://github.com/jmattheis/goverter) - 通过定义接口来生成转换器。
- [GoWrap](https://github.com/hexdigest/gowrap) - 使用简单模板为 Go 接口生成装饰器。
- [interfaces](https://github.com/rjeczalik/interfaces) - 用于生成接口定义的命令行工具。
- [jennifer](https://github.com/dave/jennifer) - 不使用模板，生成任意 Go 代码。
- [oapi-codegen](https://github.com/deepmap/oapi-codegen) - 该包包含一组工具，可基于 OpenAPI 3.0 API 定义为服务生成 Go 样板代码。
- [protoc-gen-httpgo](https://github.com/MUlt1mate/protoc-gen-httpgo) - 从 protobuf 生成 HTTP 服务器与客户端。
- [protoc-gen-mcp](https://github.com/easyp-tech/protoc-gen-mcp) - 从 Protocol Buffers 生成类型化的 MCP 工具、提示与资源。
- [typeregistry](https://github.com/xiaoxin01/typeregistry) - 用于动态创建类型的库。

**[⬆ 回到顶部](#contents)**

<a id="geographic"></a>
## 地理信息

_地理信息工具与服务_

- [borders](https://github.com/kpfaulkner/borders) - 检测图像边界并转换为 GeoJSON，以便进行 GIS 操作。
* [geo-engine-go](https://github.com/AlexG695/geo-engine-go) - GeoEngine 的官方 Go SDK，提供高性能地理空间数据接入，延迟低至个位数毫秒。
- [geoos](https://github.com/spatial-go/geoos) - 提供空间数据与几何算法的库。
- [geoserver](https://github.com/hishamkaram/geoserver) - geoserver 是一个 Go 包，用于通过 GeoServer REST API 操作 GeoServer 实例。
- [gismanager](https://github.com/hishamkaram/gismanager) - 将你的 GIS 数据（矢量数据）发布到 PostGIS 与 Geoserver。
- [godal](https://github.com/airbusgeo/godal) - GDAL 的 Go 封装。
- [H3](https://github.com/uber/h3-go) - H3 的 Go 绑定 —— 一套层级化的六边形地理空间索引系统。
- [H3 GeoJSON](https://github.com/mmadfox/go-geojson2h3) - H3 索引与 GeoJSON 之间的转换工具。
- [H3GeoDist](https://github.com/mmadfox/go-h3geo-dist) - 通过虚拟节点分发 Uber H3 地理网格。
- [mbtileserver](https://github.com/consbio/mbtileserver) - 一个简单的 Go 服务器，用于提供以 mbtiles 格式存储的地图瓦片。
- [osm](https://github.com/paulmach/osm) - 用于读写与操作 OpenStreetMap 数据及 API 的库。
- [pbf](https://github.com/maguro/pbf) - OpenStreetMap PBF 的 golang 编码器/解码器。
- [S2 geojson](https://github.com/pantrif/s2-geojson) - 将 geojson 转换为 S2 网格单元，并在地图上演示部分 S2 几何特性。
- [S2 geometry](https://github.com/golang/geo) - Go 版 S2 几何库。
- [simplefeatures](https://github.com/peterstace/simplefeatures) - simplesfeatures 是一个 2D 几何库，提供建模几何体的 Go 类型，以及作用于这些类型的算法。
- [Tile38](https://github.com/tidwall/tile38) - 带空间索引与实时地理围栏的地理定位数据库。
- [Web-Mercator-Projection](https://github.com/jorelosorio/web-mercator-projection) 借助 Web 墨卡托投影，轻松在地图上使用并转换 LonLat、Point 与 Tile，以展示信息与标注等。
- [WGS84](https://github.com/wroge/wgs84) - 坐标转换与坐标变换库（ETRS89、OSGB36、NAD83、RGF93、Web Mercator、UTM）。

**[⬆ 回到顶部](#contents)**

<a id="go-compilers"></a>
## Go 编译器

_用于 Go 与其他语言互相编译的工具。_

- [bunster](https://github.com/yassinebenaid/bunster) - 把 Shell 脚本编译为 Go。
- [c4go](https://github.com/Konstantin8105/c4go) - 把 C 代码转译为 Go 代码。
- [cxgo](https://github.com/gotranspile/cxgo) - 把 C 代码转译为 Go 代码。
- [esp32](https://github.com/andygeiss/esp32-transpiler) - 把 Go 转译为 Arduino 代码。
- [f4go](https://github.com/Konstantin8105/f4go) - 把 FORTRAN 77 代码转译为 Go 代码。
- [go2hx](https://github.com/go2hx/go2hx) - 编译器：Go → Haxe → JavaScript/C++/Java/C#。
- [gopherjs](https://github.com/gopherjs/gopherjs) - 编译器：Go → JavaScript。

**[⬆ 回到顶部](#contents)**

<a id="goroutines"></a>
## Goroutine 并发

_用于管理和使用 Goroutine 的工具。_

- [anchor](https://github.com/kyuff/anchor) - 用于在微服务架构中管理组件生命周期的库。
- [ants](https://github.com/panjf2000/ants) - Go 中高性能、低成本的 goroutine 池。
- [artifex](https://github.com/borderstech/artifex) - 为 Golang 提供的简易内存任务队列，采用基于 worker 的分发方式。
- [async](https://github.com/yaitoo/async) - 为 Go 提供的异步任务包，采用 async/await 风格。
- [async](https://github.com/reugn/async) - Go 的替代同步库（Future、Promise、Locks）。
- [async](https://github.com/studiosol/async) - 安全地异步执行函数，并在 panic 时将其恢复。
- [async-job](https://github.com/lab210-dev/async-job) - AsyncJob 是一个轻量、清晰且快速的异步队列任务管理器。
- [autopool](https://github.com/AshvinBambhaniya/autopool) - 零配置、自动扩缩的 Go worker 池，支持优先级感知调度。
- [breaker](https://github.com/kamilsk/breaker) - 使执行流可中断的灵活机制。
- [channelify](https://github.com/ddelizia/channelify) - 把你的函数改写为返回 channel，以便轻松而强大地并行处理。
- [conc](https://github.com/sourcegraph/conc) - `conc` 是你在 Go 中做结构化并发的工具箱，让常见任务更简单、更安全。
- [concurrency-limiter](https://github.com/vivek-ng/concurrency-limiter) - 并发限流器，支持超时、动态优先级与 goroutine 的上下文取消。
- [conexec](https://github.com/ITcathyh/conexec) - 并发工具包，帮助你高效且安全地并发执行函数。支持指定整体超时以避免阻塞，并使用 goroutine 池提升效率。
- [cyclicbarrier](https://github.com/marusama/cyclicbarrier) - Golang 的 CyclicBarrier（循环栅栏）。
- [execpool](https://github.com/hexdigest/execpool) - 围绕 exec.Cmd 构建的进程池，会预先启动指定数量的进程，并在需要时为其接入 stdin 与 stdout。非常类似于 FastCGI 或 Apache Prefork MPM，但适用于任意命令。
- [flowmatic](https://github.com/carlmjohnson/flowmatic) - 让结构化并发变得简单。
- [go-accumulator](https://github.com/nar10z/go-accumulator) - 事件累积及其后续处理的解决方案。
- [go-actor](https://github.com/vladopajic/go-actor) - 用 Actor 模型编写并发程序的微型库。
- [go-floc](https://github.com/workanator/go-floc) - 轻松编排 goroutine。
- [go-flow](https://github.com/kamildrazkiewicz/go-flow) - 控制 goroutine 的执行顺序。
- [go-future](https://github.com/jizhuozhi/go-future) - Future/Promise 库，带泛型组合子与 DAG 执行引擎。
- [go-tools/multithreading](https://github.com/nikhilsaraf/go-tools) - 用这个轻量库以简洁的 API 管理 goroutine 池。
- [go-trylock](https://github.com/subchen/go-trylock) - 为 Golang 读写锁提供 TryLock 支持。
- [go-waitgroup](https://github.com/pieterclaerhout/go-waitgroup) - 类 `sync.WaitGroup`，附带错误处理与并发控制。
- [go-workerpool](https://github.com/zenthangplus/go-workerpool) - 受 Java 线程池启发，Go WorkerPool 旨在控制重量级 goroutine。
- [goccm](https://github.com/zenthangplus/goccm) - Go 并发管理器包，限制允许并发运行的 goroutine 数量。
- [gohive](https://github.com/loveleshsharma/gohive) - 为 Go 打造的高性能、易用 goroutine 池。
- [gollback](https://github.com/vardius/gollback) - 简单的异步函数工具，用于管理闭包与回调的执行。
- [goscade](https://github.com/ognick/goscade) - 极简的 Go 组件生命周期编排器，具备依赖图、启动时序、就绪协调与优雅停机。
- [gowl](https://github.com/hamed-yousefi/gowl) - Gowl 既是进程管理工具，也是进程监控工具。无限 worker 池让你既能控制进程池与进程，又能监控其状态。
- [goworker](https://github.com/benmanns/goworker) - goworker 是一个基于 Go 的后台 worker。
- [gowp](https://github.com/xxjwxc/gowp) - gowp 是带并发限制的 goroutine 池。
- [gpool](https://github.com/Sherifabdlnaby/gpool) - 管理一组可动态调整大小的、感知上下文的 goroutine，以约束并发度。
- [grpool](https://github.com/ivpusic/grpool) - 轻量级 goroutine 池。
- [hands](https://github.com/duanckham/hands) - 用于控制多个 goroutine 执行与返回策略的进程控制器。
- [Hunch](https://github.com/AaronJan/Hunch) - Hunch 提供 `All`、`First`、`Retry`、`Waterfall` 等函数，让异步流程控制更直观。
- [kyoo](https://github.com/dirkaholic/kyoo) - 提供无限任务队列与并发 worker 池。
- [neilotoole/errgroup](https://github.com/neilotoole/errgroup) - `sync/errgroup` 的直接替代品，限制在 N 个 worker goroutine 的池内。
- [nursery](https://github.com/arunsworld/nursery) - Go 中的结构化并发。
- [oversight](https://pkg.go.dev/cirello.io/oversight) - Oversight 是 Erlang 监管树的完整实现。
- [parallel-fn](https://github.com/rafaeljesus/parallel-fn) - 并行运行函数。
- [pond](https://github.com/alitto/pond) - 用 Go 编写的极简高性能 goroutine worker 池。
- [pool](https://github.com/go-playground/pool) - 有限消费者 goroutine 或无限 goroutine 池，让 goroutine 处理与取消更轻松。
- [powerlock](https://github.com/donomii/powerlock) - 具名 FIFO 互斥锁，支持上下文取消、有界等待队列、看门狗诊断、pprof 性能剖析与 Prometheus 指标。
- [rill](https://github.com/destel/rill) - 为 Go 提供简洁、可组合、基于 channel 的并发工具包。
- [routine](https://github.com/timandy/routine) - `routine` 是 Go 库的 `ThreadLocal`。它封装并提供若干易用、无竞争、高性能的 `goroutine` 上下文访问接口，帮助你更优雅地获取协程上下文信息。
- [routine](https://github.com/x-mod/routine) - 带上下文的 goroutine 控制，支持 Main、Go、Pool 以及若干实用的执行器。
- [semaphore](https://github.com/kamilsk/semaphore) - 基于 channel 与 context 的信号量模式实现，带锁/解锁操作的超时控制。
- [semaphore](https://github.com/marusama/semaphore) - 基于 CAS 的快速可调整大小信号量实现（比基于 channel 的实现更快）。
- [stl](https://github.com/ssgreg/stl) - 基于软件事务内存（STM）并发控制机制的软件事务锁。
- [threadpool](https://github.com/shettyh/threadpool) - Golang 线程池实现。
- [tunny](https://github.com/Jeffail/tunny) - 面向 golang 的 goroutine 池。
- [worker-pool](https://github.com/vardius/worker-pool) - goworker 是一个简单的 Go 异步 worker 池。
- [workerpool](https://github.com/gammazero/workerpool) - 限制任务执行并发度（而非排队任务数量）的 goroutine 池。

**[⬆ 回到顶部](#contents)**

<a id="gui"></a>
## GUI

_用于构建 GUI 应用的库。_

_工具集_

- [app](https://github.com/murlokswarm/app) - 用 Go、HTML 与 CSS 构建应用的包。支持 macOS，Windows 开发中。
- [cimgui-go](https://github.com/AllenDang/cimgui-go) - 通过 [cimgui](https://github.com/cimgui/cimgui) 为 [Dear ImGui](https://github.com/ocornut/imgui) 自动生成的 Go 封装。
- [Cogent Core](https://github.com/cogentcore/core) - 用于构建可在 macOS、Windows、Linux、iOS、Android 与 Web 上运行的 2D 与 3D 应用的框架。
- [DarwinKit](https://github.com/progrium/darwinkit) - 用 Go 构建原生 macOS 应用。
- [energy](https://github.com/energye/energy) - 基于 LCL（原生系统 UI 控件库）与 CEF（Chromium 嵌入式框架）的跨平台方案（Windows/macOS/Linux）。
- [fyne](https://github.com/fyne-io/fyne) - 基于 Material Design、面向 Go 设计的跨平台原生 GUI。支持 Linux、macOS、Windows、BSD、iOS 与 Android。
- [gio](https://gioui.org) - Gio 是一个用 Go 编写跨平台即时模式 GUI 的库。Gio 支持所有主流平台：Linux、macOS、Windows、Android、iOS、FreeBSD、OpenBSD 与 WebAssembly。
- [go-gtk](https://mattn.github.io/go-gtk/) - GTK 的 Go 绑定。
- [go-sciter](https://github.com/sciter-sdk/go-sciter) - Sciter 的 Go 绑定 —— 面向现代桌面 UI 开发的可嵌入 HTML/CSS/脚本引擎。跨平台。
- [Goey](https://bitbucket.org/rj/goey/src/master/) - 面向 Windows/Linux/Mac 的跨平台 UI 工具包聚合层，涵盖 GTK、Cocoa 与 Windows API。
- [gogpu/ui](https://github.com/gogpu/ui) - GPU 加速的 GUI 工具包，含 22 个控件、3 套设计体系（Material、Fluent、Cupertino）、响应式信号，零 CGO（[GoGPU](https://github.com/gogpu) 生态的一部分）。
- [goradd/html5tag](https://github.com/goradd/html5tag) - 用于输出 HTML5 标签的库。
- [gotk3](https://github.com/gotk3/gotk3) - GTK3 的 Go 绑定。
- [gowd](https://github.com/dtylman/gowd) - 借助 Go、HTML、CSS 与 NW.js 快速简便地开发桌面 UI。跨平台。
- [proton](https://github.com/CzaxStudio/proton) - 基于 Gio 构建的纯 Go 即时模式 GUI 框架，零 Cgo 依赖。
- [qt](https://github.com/therecipe/qt) - Go 的 Qt 绑定（支持 Windows/macOS/Linux/Android/iOS/Sailfish OS/树莓派）。
- [Spot](https://github.com/roblillack/spot) - 响应式跨平台桌面 GUI 工具包。
- [ui](https://github.com/andlabs/ui) - 面向 Go 的平台原生 GUI 库。跨平台。
- [unison](https://github.com/richardwilkes/unison) - 面向 Go 桌面应用的一体化图形用户体验工具包，支持 macOS、Windows 与 Linux。
- [Wails](https://wails.io) - 借助内置操作系统 HTML 渲染器、用 HTML 做 UI 的 Mac/Windows/Linux 桌面应用方案。
- [walk](https://github.com/lxn/walk) - 面向 Go 的 Windows 应用开发工具包。
- [webview](https://github.com/zserge/webview) - 跨平台 webview 窗口，带简洁的双向 JavaScript 绑定（Windows/macOS/Linux）。

_交互_

- [AppIndicator Go](https://github.com/gopherlibs/appindicator) - libappindicator3 C 库的 Go 绑定。
- [gogpu/systray](https://github.com/gogpu/systray) - 面向 Windows、macOS 与 Linux 的纯 Go 系统托盘库，零 CGO（[GoGPU](https://github.com/gogpu) 生态的一部分）。
- [gosx-notifier](https://github.com/deckarep/gosx-notifier) - Go 的 macOS 桌面通知库。
- [mac-activity-tracker](https://github.com/prashantgupta24/activity-tracker) - macOS 库，用于通知机器上发生的任意（可插拔的）活动。
- [mac-sleep-notifier](https://github.com/prashantgupta24/mac-sleep-notifier) - golang 中的 macOS 睡眠/唤醒通知。
- [robotgo](https://github.com/go-vgo/robotgo) - Go 原生跨平台 GUI 系统自动化，可控制鼠标、键盘等。
- [systray](https://github.com/getlantern/systray) - 跨平台 Go 库，在通知区域放置图标与菜单。
- [trayhost](https://github.com/shurcooL/trayhost) - 跨平台 Go 库，在宿主操作系统的任务栏中放置图标。
- [zenity](https://github.com/ncruces/zenity) - 跨平台 Go 库与 CLI，用于创建与用户图形化交互的简单对话框。

**[⬆ 回到顶部](#contents)**

<a id="hardware"></a>
## 硬件

_用于与硬件交互的库、工具与教程。_

- [arduino-cli](https://github.com/arduino/arduino-cli) - 官方 Arduino CLI 与库。既可独立运行，也可集成进更大的 Go 项目。
- [emgo](https://github.com/ziutek/emgo) - 类 Go 的嵌入式系统编程语言（如 STM32 MCU）。
- [ghw](https://github.com/jaypipes/ghw) - Golang 硬件发现/检测库。
- [go-osc](https://github.com/hypebeast/go-osc) - Go 的 Open Sound Control (OSC) 绑定。
- [go-rpio](https://github.com/stianeikeland/go-rpio) - Go 的 GPIO 支持，无需 cgo。
- [goroslib](https://github.com/aler9/goroslib) - Go 的机器人操作系统（ROS）库。
- [joystick](https://github.com/0xcafed00d/joystick) - 轮询式 API，用于读取已连接游戏手柄的状态。
- [moody](https://github.com/dinakars777/moody) - macOS 硬件事件人格化守护进程。监控 USB、充电器、合盖等硬件事件，并以可自定义的「人格」作出响应。
- [sysinfo](https://github.com/zcalusic/sysinfo) - 提供 Linux 操作系统/内核/硬件系统信息的纯 Go 库。

**[⬆ 回到顶部](#contents)**

<a id="images"></a>
## 图像处理

_用于图像处理的库。_

- [bild](https://github.com/anthonynsimon/bild) - 纯 Go 实现的图像处理算法集合。
- [bimg](https://github.com/h2non/bimg) - 使用 libvips 进行快速高效图像处理的小型包。
- [cameron](https://github.com/aofei/cameron) - Go 的头像生成器。
- [canvas](https://github.com/tdewolff/canvas) - 矢量图形转 PDF、SVG 或栅格化图像。
- [color-extractor](https://github.com/marekm4/color-extractor) - 主色提取器，无外部依赖。
- [darkroom](https://github.com/gojek/darkroom) - 图像代理，具备可更换的存储后端与图像处理引擎，注重速度与韧性。
- [eagle-image-api](https://github.com/nicobistolfi/eagle-image-api) - 基于 libvips 的图像优化与转换 API，可部署到 AWS Lambda 与 CloudFront。
- [geopattern](https://github.com/pravj/geopattern) - 从字符串生成美观的生成式图像图案。
- [gg](https://github.com/fogleman/gg) - 纯 Go 的 2D 渲染。
- [gift](https://github.com/disintegration/gift) - 图像处理滤镜包。
- [gltf](https://github.com/qmuntal/gltf) - 高效稳健的 glTF 2.0 读取器、写入器与校验器。
- [go-cairo](https://github.com/ungerik/go-cairo) - cairo 图形库的 Go 绑定。
- [go-gd](https://github.com/bolknote/go-gd) - GD 库的 Go 绑定。
- [go-nude](https://github.com/koyachi/go-nude) - 用 Go 实现的裸露内容检测。
- [go-qrcode](https://github.com/yeqown/go-qrcode) - 生成个性化样式的二维码，可调整颜色、模块大小、形状与图标。
- [go-webcolors](https://github.com/jyotiska/go-webcolors) - 把 Python 的 webcolors 库移植到 Go。
- [go-webp](https://github.com/kolesa-team/go-webp) - 使用 libwebp 编解码 webp 图片的库。
- [gocv](https://github.com/hybridgroup/gocv) - 基于 OpenCV 3.3+ 的 Go 计算机视觉包。
- [gogpu/gg](https://github.com/gogpu/gg) - GPU 加速的 2D 渲染，提供类 Canvas 的 API，零 CGO（[GoGPU](https://github.com/gogpu) 纯 Go 图形生态的一部分）。
- [goimagehash](https://github.com/corona10/goimagehash) - Go 的感知哈希（perceptual image hashing）包。
- [goimghdr](https://github.com/corona10/goimghdr) - imghdr 模块用于判定 Go 文件中所含图像的类型。
- [govatar](https://github.com/o1egl/govatar) - 用于生成趣味头像的库与命令行工具。
- [govips](https://github.com/davidbyttow/govips) - 为 Go 打造的闪电般快速的图像处理与缩放库。
- [gowitness](https://github.com/sensepost/gowitness) - 用 Go 配合命令行无头 Chrome 对网页截图。
- [gridder](https://github.com/shomali11/gridder) - 基于网格的 2D 图形库。
- [image2ascii](https://github.com/qeesung/image2ascii) - 把图像转换为 ASCII 字符画。
- [imagick](https://github.com/gographics/imagick) - ImageMagick MagickWand C API 的 Go 绑定。
- [imaginary](https://github.com/h2non/imaginary) - 快速简便的图像缩放 HTTP 微服务。
- [imaging](https://github.com/disintegration/imaging) - 简易 Go 图像处理包。
- [imagor](https://github.com/cshum/imagor) - 基于 libvips 的快速安全图像处理服务器与 Go 库。
- [img](https://github.com/hawx/img) - 一组图像操作工具。
- [ln](https://github.com/fogleman/ln) - Go 中的 3D 线稿渲染。
- [mergi](https://github.com/noelyahan/mergi) - 图像操作工具与 Go 库（合并、裁剪、缩放、水印、动效）。
- [mort](https://github.com/aldor007/mort) - 用 Go 编写的存储与图像处理服务器。
- [mpo](https://github.com/donatj/mpo) - MPO 3D 照片的解码与转换工具。
- [nativewebp](https://github.com/HugoSmits86/nativewebp) - Go 原生 WebP 编码器，零外部依赖。
- [picfit](https://github.com/thoas/picfit) - 用 Go 编写的图像缩放服务器。
- [pt](https://github.com/fogleman/pt) - 用 Go 编写的路径追踪引擎。
- [scout](https://github.com/jonoton/scout) - Scout 是面向 DIY 视频监控的独立开源软件解决方案。
- [smartcrop](https://github.com/muesli/smartcrop) - 为任意图像与裁剪尺寸寻找优质裁剪区域。
- [steganography](https://github.com/auyer/steganography) - 用于 LSB 隐写的纯 Go 库。
- [stegify](https://github.com/DimitarPetrov/stegify) - LSB 隐写 Go 工具，能够把任意文件隐藏在图片中。
- [svgo](https://github.com/ajstarks/svgo) - 用于 SVG 生成的 Go 语言库。
- [transformimgs](https://github.com/Pixboost/transformimgs) - Transformimgs 使用新一代格式为 Web 缩放与优化图片。
- [webp-server](https://github.com/mehdipourfar/webp-server) - 简单极简的图片服务器，支持存储、缩放、转换与缓存图片。

**[⬆ 回到顶部](#contents)**

<a id="iot-internet-of-things"></a>
## 物联网（IoT）

_用于物联网设备编程的库。_

- [connectordb](https://github.com/connectordb/connectordb) - 面向量化自我与物联网的开源平台。
- [devices](https://github.com/goiot/devices) - 面向物联网设备的一组库，属于实验性的 x/exp/io。
- [ekuiper](https://github.com/lf-edge/ekuiper) - 面向物联网边缘的轻量级数据流处理引擎。
- [eywa](https://github.com/xcodersun/eywa) - Eywa 项目本质上是一个连接管理器，用于跟踪已连接的设备。
- [flogo](https://github.com/tibcosoftware/flogo) - Flogo 项目是面向物联网边缘应用与集成的开源框架。
- [gatt](https://github.com/paypal/gatt) - Gatt 是用于构建蓝牙低功耗外设的 Go 包。
- [gobot](https://github.com/hybridgroup/gobot/) - Gobot 是面向机器人、物联网与实体计算的框架。
- [huego](https://github.com/amimof/huego) - 功能完备的 Philips Hue Go 客户端库。
- [iot](https://github.com/vaelen/iot/) - IoT 是一个用于实现 Google IoT Core 设备的简易框架。
- [periph](https://periph.io/) - 外设 I/O，用于对接底层板级设施。
- [rulego](https://github.com/rulego/rulego) - RuleGo 是面向物联网边缘的轻量、高性能、可嵌入、可编排的组件化规则引擎。
- [sensorbee](https://github.com/sensorbee/sensorbee) - 面向物联网的轻量级流处理引擎。
- [shifu](https://github.com/Edgenesis/shifu) - Kubernetes 原生的物联网开发框架。
- [smart-home](https://github.com/e154/smart-home) - 用于物联网自动化的软件包。

**[⬆ 回到顶部](#contents)**

<a id="job-scheduler"></a>
## 任务调度

_用于任务调度的库。_

- [cdule](https://github.com/deepaksinghvi/cdule) - 带数据库支持的作业调度库。
- [cheek](https://github.com/bart6114/cheek) - 类 crontab 的简易调度器，力求以 KISS 理念搞定作业调度。
- [clockwerk](https://github.com/onatm/clockwerk) - 用简单流畅的语法调度周期作业的 Go 包。
- [cronticker](https://github.com/krayzpipes/cronticker) - 支持 cron 表达式的 ticker 实现。
- [go-cron](https://github.com/rk/go-cron) - Go 的简易 Cron 库，可按从每秒一次到每年某月某日某时一次的不同间隔执行闭包或函数。主要面向 Web 应用与长期运行的守护进程。
- [go-cron](https://github.com/netresearch/go-cron) - Cron 作业调度器，支持运行时更新排程、按条目隔离上下文、弹性中间件（重试、熔断、限流）与可观测性钩子；是 robfig/cron 的继任者。
- [go-job](https://github.com/cybergarage/go-job) - 灵活可扩展的 Go 作业调度与执行库。
- [go-quartz](https://github.com/reugn/go-quartz) - 简单、零依赖的 Go 调度库。
- [go-scheduler](https://github.com/pardnchiu/go-scheduler) - 支持标准 cron 表达式、自定义描述符、时间间隔与任务依赖的作业调度器。
- [gocron](https://github.com/go-co-op/gocron) - 简单易用的 Go 作业调度。这是 [jasonlvhit/gocron](https://github.com/jasonlvhit/gocron) 的活跃维护分支。
- [goflow](https://github.com/fieldryand/goflow) - 简单却强大的 DAG 调度器与仪表盘。
- [gron](https://github.com/roylee0704/gron) - 用简洁的 Go API 定义基于时间的任务，Gron 的调度器会据此执行。
- [gronx](https://github.com/adhocore/gronx) - Cron 表达式解析器、任务运行器与守护进程，读取类 crontab 的任务列表。
- [JobRunner](https://github.com/bamzi/jobrunner) - 智能且功能丰富的 cron 作业调度器，内置作业队列与实时监控。
- [leprechaun](https://github.com/kilgaloon/leprechaun) - 支持 webhook、cron 与传统调度的作业调度器。
- [ofelia](https://github.com/netresearch/ofelia) - Docker 作业调度器（Docker 版 crontab）；是 mcuadros/ofelia 的分支，新增 Web 界面、作业依赖、重试与作业持久化。
- [pending](https://github.com/kahoon/pending) - 基于 ID 的防抖任务调度器，用于延迟任务，支持取消、优雅停机与可选的并发上限。
- [sched](https://github.com/romshark/sched) - 具备时间快进能力的作业调度器。
- [scheduler](https://github.com/carlescere/scheduler) - 让 cronjob 调度变得简单。
- [scheduler](https://github.com/yuseferi/scheduler) - Go 原生的分布式作业调度器，支持延迟任务、批量 Redis 协调、重试、基于租约的恢复与带版本隔离的队列分区。
- [tasks](https://github.com/madflojo/tasks) - 易于使用的 Go 进程内调度器，用于周期性任务。
- [tickstem/cron](https://github.com/tickstem/cron) - 用于调度 HTTP cron 作业的 Go 客户端，带执行历史、失败告警，并提供 tsk-local 让你无需真实凭据即可测试处理器。
- [tickstem/heartbeat](https://github.com/tickstem/heartbeat) - 用于「死人开关」心跳监控的 Go 客户端：每次作业运行后 ping 一个 URL，若心跳中断则通过邮件告警。

**[⬆ 回到顶部](#contents)**

<a id="json"></a>
## JSON

_用于处理 JSON 的库。_

- [ajson](https://github.com/spyzhov/ajson) - 支持 JSONPath 的 Go 抽象 JSON 处理。
- [ask](https://github.com/simonnilsson/ask) - 便捷访问 map 与 slice 中的嵌套值。可与 encoding/json 等把任意数据「反序列化」为 Go 类型的包配合使用。
- [dynjson](https://github.com/cocoonspace/dynjson) - 面向动态 API、格式可由客户端定制的 JSON 方案。
- [ej](https://github.com/lucassscaravelli/ej) - 简洁地从不同来源读写 JSON。
- [epoch](https://github.com/vtopc/epoch) - 包含在 JSON 中将 Unix 时间戳/纪元时间与内置 time.Time 类型互相编解码的原语。
- [fastjson](https://github.com/valyala/fastjson) - 快速 JSON 解析器与校验器，用 Go 编写。无需自定义结构体、无需代码生成、无需反射。
- [gabs](https://github.com/Jeffail/gabs) - 用于在 Go 中解析、创建与编辑未知或动态 JSON。
- [gjo](https://github.com/skanehira/gjo) - 创建 JSON 对象的小工具。
- [GJSON](https://github.com/tidwall/gjson) - 一行代码获取一个 JSON 值。
- [go-jsonerror](https://github.com/ddymko/go-jsonerror) - Go-JsonError 让我们能轻松创建符合 JsonApi 规范的 JSON 响应错误。
- [go-respond](https://github.com/nicklaw5/go-respond) - 用于处理常见 HTTP JSON 响应的 Go 包。
- [gojmapr](https://github.com/limiu82214/gojmapr) - 按 JSON 路径从复杂 JSON 中取出简单结构体。
- [gojq](https://github.com/elgs/gojq) - Golang 中的 JSON 查询。
- [gojson](https://github.com/ChimeraCoder/gojson) - 从示例 JSON 自动生成 Go (golang) 结构体定义。
- [htmljson](https://github.com/nikolaydubina/htmljson) - 在 Go 中把 JSON 丰富地渲染为 HTML。
- [JayDiff](https://github.com/yazgazan/jaydiff) - 用 Go 编写的 JSON diff 工具。
- [jettison](https://github.com/wI2L/jettison) - 快速灵活的 Go JSON 编码器。
- [jscan](https://github.com/romshark/jscan) - 高性能零分配 JSON 迭代器。
- [JSON-to-Go](https://mholt.github.io/json-to-go/) - 将 JSON 转换为 Go 结构体。
- [JSON-to-Proto](https://json-to-proto.github.io/) - 在线将 JSON 转换为 Protobuf。
- [json2go](https://github.com/m-zajac/json2go) - 高级 JSON 到 Go 结构体转换。提供的包可解析多个 JSON 文档，并生成能同时容纳它们的结构体。
- [jsonapi-errors](https://github.com/AmuzaTkts/jsonapi-errors) - 基于 JSON API 错误规范的 Go 绑定。
- [jsoncolor](https://github.com/neilotoole/jsoncolor) - `encoding/json` 的直接替代品，输出带颜色的 JSON。
- [jsondiff](https://github.com/wI2L/jsondiff) - 基于 RFC6902（JSON Patch）的 Go JSON diff 库。
- [jsonf](https://github.com/miolini/jsonf) - 控制台工具，提供高亮格式化与按结构体查询获取 JSON。
- [jsongo](https://github.com/ricardolonga/jsongo) - 流畅的 API，让创建 JSON 对象更轻松。
- [jsonhal](https://github.com/RichardKnop/jsonhal) - 简易 Go 包，让自定义结构体可序列化为兼容 HAL 的 JSON 响应。
- [jsonhandlers](https://github.com/abusomani/jsonhandlers) - JSON 库，提供简洁的处理器，便于从各种来源读写 JSON。
- [jsonic](https://github.com/sinhashubham95/jsonic) - 无需以类型安全方式定义结构体，即可处理与查询 JSON 的工具集。
- [jsonvalue](https://github.com/Andrew-M-C/go.jsonvalue) - 面向非结构化 JSON 数据的快速便捷库，可替代 `encoding/json`。
- [jzon](https://github.com/zerosnake0/jzon) - API/行为与标准兼容的 JSON 库。
- [kazaam](https://github.com/Qntfy/kazaam) - 用于对 JSON 文档做任意变换的 API。
- [mapslice-json](https://github.com/mickep76/mapslice-json) - Go 版 MapSlice，用于 JSON 中 map 的有序编解码。
- [marshmallow](https://github.com/PerimeterX/marshmallow) - 面向灵活场景的高性能 JSON 反序列化。
- [mp](https://github.com/sanbornm/mp) - 简易命令行邮件解析器。当前从 stdin 读取并输出 JSON。
- [OjG](https://github.com/ohler55/ojg) - 面向 Go 的优化版 JSON 是一个高性能解析器，并内置 JSONPath 等多种 JSON 辅助工具。
- [omg.jsonparser](https://github.com/dedalqq/omg.jsonparser) - 简易 JSON 解析器，支持通过 Go 结构体字段标签按条件校验。
- [silentjson](https://github.com/GenshIv/silentjson) - 利用 AVX2 SIMD 指令实现的零分配 JSON 边界扫描与切分器。
- [SJSON](https://github.com/tidwall/sjson) - 一行代码设置一个 JSON 值。
- [ujson](https://github.com/olvrng/ujson) - 快速极简的 JSON 解析与转换器，可作用于非结构化 JSON。
- [vjson](https://github.com/miladibra10/vjson) - 用于校验 JSON 对象的 Go 包，可用流畅 API 声明 JSON schema。

**[⬆ 回到顶部](#contents)**

<a id="logging"></a>
## 日志

_用于生成与处理日志文件的库。_

- [caarlos0/log](https://github.com/caarlos0/log) - 彩色命令行日志工具。
- [distillog](https://github.com/amoghe/distillog) - 提炼的分级日志（可以理解为标准库 + 日志级别）。
- [glg](https://github.com/kpango/glg) - glg 是简单快速的 Go 分级日志库。
- [glo](https://github.com/lajosbencz/glo) - 受 PHP Monolog 启发的日志设施，严重级别完全一致。
- [glog](https://github.com/golang/glog) - 面向 Go 的分级执行日志。
- [go-cronowriter](https://github.com/utahta/go-cronowriter) - 简单的写入器，可依据当前日期时间自动轮转日志文件，类似 cronolog。
- [go-log](https://github.com/pieterclaerhout/go-log) - 带堆栈追踪、对象转储与可选时间戳的日志库。
- [go-log](https://github.com/subchen/go-log) - Go 中简单可配置的日志方案，支持级别、格式化器与写入器。
- [go-log](https://github.com/siddontang/go-log) - 支持级别与多处理器的日志库。
- [go-log](https://github.com/ian-kent/go-log) - 用 Go 实现的 Log4j。
- [go-log4g](https://github.com/go-log4g/core) - Log4g 为 Go 的标准 log/slog 日志门面提供 Log4j 风格的配置与模式布局。
- [go-logger](https://github.com/apsdehal/go-logger) - Go 程序的简易日志器，带级别处理器。
- [GoLogX](https://github.com/AyoubTadlaoui/GoLogX) - 仅追加、哈希链式、可选 Ed25519 签名的 slog 处理器，支持离线校验是否被篡改。
- [gone/log](https://github.com/One-com/gone/tree/master/log) - 快速可扩展、功能完整、与标准库源码兼容的日志库。
- [gslog](https://github.com/maguro/gslog) - 面向 log/slog 的 Google Cloud Logging 处理器，集成 OpenTelemetry trace 与 baggage，以及 Kubernetes podinfo 标签。
- [httpretty](https://github.com/henvic/httpretty) - 在终端上美化打印常规 HTTP 请求以便调试（类似 http.DumpRequest）。
- [journald](https://github.com/ssgreg/journald) - Go 实现的 systemd Journal 原生日志 API。
- [kemba](https://github.com/clok/kemba) - 受 [debug](https://github.com/visionmedia/debug) 启发的迷你调试日志工具，非常适合 CLI 工具与应用。
- [lazyjournal](https://github.com/Lifailon/lazyjournal) - TUI，用于读取并过滤来自 journalctl、文件系统、Docker 与 Podman 容器以及 Kubernetes Pod 的日志。
- [log](https://github.com/aerogo/log) - O(1) 日志系统，可将一条日志同时接入多个写入器（如标准输出、文件与 TCP 连接）。
- [log](https://github.com/apex/log) - 面向 Go 的结构化日志包。
- [log](https://github.com/go-playground/log) - 简单、可配置、可扩展的 Go 结构化日志方案。
- [log](https://github.com/teris-io/log) - Go 的结构化日志接口，清晰地分离了日志门面与其实现。
- [log](https://github.com/heartwilltell/log) - 对标准 log 包的简单分级封装。
- [log](https://github.com/no-src/log) - 开箱即用的简易日志框架。
- [log15](https://github.com/inconshreveable/log15) - 简单、强大的 Go 日志方案。
- [logdump](https://github.com/ewwwwwqm/logdump) - 多级日志包。
- [logex](https://github.com/chzyer/logex) - Golang 日志库，支持跟踪与级别控制，基于标准 log 库封装。
- [logger](https://github.com/azer/logger) - 极简的 Go 日志库。
- [logo](https://github.com/mbndr/logo) - 面向不同可配置写入器的 Golang 日志器。
- [logrus](https://github.com/Sirupsen/logrus) - 面向 Go 的结构化日志器。
- [logrusiowriter](https://github.com/cabify/logrusiowriter) - 使用 [logrus](https://github.com/sirupsen/logrus) 日志器实现的 `io.Writer`。
- [logrusly](https://github.com/sebest/logrusly) - [logrus](https://github.com/sirupsen/logrus) 插件，将错误发送到 [Loggly](https://www.loggly.com/)。
- [logutils](https://github.com/hashicorp/logutils) - 为改进 Go (Golang) 日志体验的工具集，扩展了标准日志器。
- [logxi](https://github.com/mgutz/logxi) - 符合 12-factor 的应用日志器，快速且让人愉悦。
- [lumberjack](https://github.com/natefinch/lumberjack) - 简单的滚动日志器，实现 io.WriteCloser。
- [mlog](https://github.com/jbrodriguez/mlog) - 简单的 Go 日志模块，含 5 个级别、可选的日志轮转功能以及标准输出/错误输出。
- [noodlog](https://github.com/gyozatech/noodlog) - 参数化的 JSON 日志库，可对敏感数据脱敏并封送任意类型的内容。不再出现打印指针而非值，也不再有 JSON 字符串的转义字符。
- [onelog](https://github.com/francoispqt/onelog) - Onelog 是极简但极为高效的 JSON 日志器，在所有场景下都是最快的 JSON 日志器之一，同时也是分配开销最低的日志器之一。
- [ozzo-log](https://github.com/go-ozzo/ozzo-log) - 高性能日志，支持日志严重级别、分类与过滤。可将过滤后的日志消息发往各类目标（如控制台、网络、邮件）。
- [phuslu/log](https://github.com/phuslu/log) - 高性能结构化日志。
- [pp](https://github.com/k0kubun/pp) - Go 语言的彩色格式化打印工具。
- [rollingwriter](https://github.com/arthurkiller/rollingWriter) - RollingWriter 是自动轮转的 `io.Writer` 实现，支持多种策略以实现日志文件轮转。
- [seelog](https://github.com/cihub/seelog) - 具备灵活分发、过滤与格式化能力的日志方案。
- [sentry-go](https://github.com/getsentry/sentry-go) - Go 的 Sentry SDK。帮助你实时告警并监控追踪错误，附带性能监控。
- [slf4g](https://github.com/echocat/slf4g) - Golang 的简易日志门面：简单的结构化日志，但强大、可扩展、可定制，融汇了数十年来历代日志框架的心血。
- [slog](https://github.com/gookit/slog) - 轻量、可配置、可扩展的 Go 日志器。
- [slog-configurator](https://github.com/psyb0t/slog-configurator) - 通过环境变量配置标准库 log/slog 日志器：级别、格式、源码位置以及标准输出/错误输出分流。
- [slog-datadog](https://github.com/samber/slog-datadog) - 面向 Datadog 的 slog 处理器。
- [slog-formatter](https://github.com/samber/slog-formatter) - 面向 slog 的常用格式化器，以及构建自定义处理器的辅助工具。
- [slog-logrus](https://github.com/samber/slog-logrus) - 面向 Logrus 的 slog 处理器。
- [slog-loki](https://github.com/samber/slog-loki) - 面向 Grafana Loki 的 slog 处理器。
- [slog-multi](https://github.com/samber/slog-multi) - slog.Handler 链（管线、扇出等）。
- [slog-sentry](https://github.com/samber/slog-sentry) - 面向 Sentry 的 slog 处理器。
- [slog-slack](https://github.com/samber/slog-slack) - 面向 Slack 的 slog 处理器。
- [slog-zap](https://github.com/samber/slog-zap) - 面向 Zap 的 slog 处理器。
- [slog-zerolog](https://github.com/samber/slog-zerolog) - 面向 Zerolog 的 slog 处理器。
- [slogor](https://gitlab.com/greyxor/slogor) - 彩色的 slog 处理器。
- [spew](https://github.com/davecgh/go-spew) - 为 Go 数据结构实现深度美化打印器，辅助调试。
- [sqldb-logger](https://github.com/simukti/sqldb-logger) - 面向 Go SQL 数据库驱动的日志器，无需改动现有 \*sql.DB 标准库用法。
- [stdlog](https://github.com/alexcesaro/log) - Stdlog 是一个提供分级日志的面向对象库，对定时任务非常有用。
- [structy/log](https://github.com/structy/log) - 易于使用的日志系统，极简但具备调试与消息区分所需的特性。
- [tail](https://github.com/hpcloud/tail) - 力求模拟 BSD tail 程序特性的 Go 包。
- [timberjack](https://github.com/DeRuina/timberjack) - 滚动日志器，支持基于大小、基于时间与基于定时时钟的轮转，并支持压缩与清理。
- [tint](https://github.com/lmittmann/tint) - 写入着色日志的 slog.Handler。
- [xlog](https://github.com/xfxdev/xlog) - 面向 Go 的插件化架构与灵活日志系统，支持级别控制、多日志目标与自定义日志格式。
- [xlog](https://github.com/rs/xlog) - 面向 `net/context` 感知型 HTTP 处理器的结构化日志器，支持灵活分发。
- [xylog](https://github.com/xybor-x/xylog) - 分级且结构化的日志，支持动态字段、高性能、zone 管理、简易配置与可读语法。
- [yell](https://github.com/jfcg/yell) - 又一个极简日志库。
- [zap](https://github.com/uber-go/zap) - Go 中快速、结构化、分级的日志方案。
- [zax](https://github.com/yuseferi/zax) - 把 Context 与 Zap 日志器集成，让 Go 日志具备更多灵活性。
- [zerolog](https://github.com/rs/zerolog) - 零分配 JSON 日志器。
- [zkits-logger](https://github.com/edoger/zkits-logger) - 强大的零依赖 JSON 日志器。
- [zl](https://github.com/nkmr-jp/zl) - 开发者体验出色的基于 zap 的日志器。功能丰富却易于配置。

**[⬆ 回到顶部](#contents)**

<a id="machine-learning"></a>
## 机器学习

_机器学习相关的库。_

- [Anneal](https://github.com/georgebuilds/anneal) - 用 Go 编写的机器学习编译器，是从零实现的 tinygrad 移植版，带 WebGPU 后端。
- [bayesian](https://github.com/jbrukh/bayesian) - Golang 的朴素贝叶斯分类。
- [born](https://github.com/born-ml/born) - 受 Burn（Rust）启发的深度学习框架，具备自动微分、类型安全张量与零 CGO GPU 加速。
- [catboost-cgo](https://github.com/mirecl/catboost-cgo) - 快速、可扩展、高性能的决策树梯度提升库。用 Golang 通过 Cgo 加速推理速度极快的 CatBoost 模型。
- [CloudForest](https://github.com/ryanbressler/CloudForest) - 纯 Go 实现的快速、灵活、多线程决策树集成模型，用于机器学习。
- [datatrax](https://github.com/rbmuller/datatrax) - 纯 Go 零依赖的数据工程与经典机器学习工具包，含批处理、类型转换与 7 种算法。
- [ddt](https://github.com/sgrodriguez/ddt) - 动态决策树，可创建带有自定义规则的树。
- [eaopt](https://github.com/MaxHalford/eaopt) - 演化优化库。
- [evoli](https://github.com/khezen/evoli) - 遗传算法与粒子群优化库。
- [fonet](https://github.com/Fontinalis/fonet) - 用 Go 编写的深度神经网络库。
- [go-cluster](https://github.com/e-XpertSolutions/go-cluster) - k-modes 与 k-prototypes 聚类算法的 Go 实现。
- [go-deep](https://github.com/patrikeh/go-deep) - Go 中功能丰富的神经网络库。
- [go-fann](https://github.com/white-pony/go-fann) - Fast Artificial Neural Networks（FANN）库的 Go 绑定。
- [go-galib](https://github.com/thoj/go-galib) - 用 Go / golang 编写的遗传算法库。
- [go-pr](https://github.com/daviddengcn/go-pr) - Go 语言中的模式识别包。
- [gobrain](https://github.com/goml/gobrain) - 用 Go 编写的神经网络。
- [godist](https://github.com/e-dard/godist) - 各类概率分布及其相关方法。
- [goga](https://github.com/tomcraven/goga) - Go 的遗传算法库。
- [GoLearn](https://github.com/sjwhitworth/golearn) - Go 的通用机器学习库。
- [GoMind](https://github.com/surenderthakran/gomind) - Go 中极简的神经网络库。
- [goml](https://github.com/cdipaolo/goml) - Go 中的在线机器学习。
- [GoMLX](https://github.com/gomlx/gomlx) - 面向 Go 的加速机器学习框架。
- [gonet](https://github.com/dathoangnd/gonet) - 面向 Go 的神经网络。
- [Goptuna](https://github.com/c-bata/goptuna) - 用 Go 编写的黑箱函数贝叶斯优化框架。一切都将被优化。
- [goRecommend](https://github.com/timkaye11/goRecommend) - 用 Go 编写的推荐算法库。
- [gorgonia](https://github.com/gorgonia/gorgonia) - 类 Theano 的 Go 图计算库，为构建各类机器学习与神经网络算法提供原语。
- [gorse](https://github.com/zhenghaoz/gorse) - 用 Go 编写的、基于协同过滤的离线推荐系统后端。
- [goscore](https://github.com/asafschers/goscore) - 面向 PMML 的 Go 评分 API。
- [gosseract](https://github.com/otiai10/gosseract) - 通过调用 Tesseract C++ 库实现的 Go OCR（光学字符识别）包。
- [hugot](https://github.com/knights-analytics/hugot) - 面向 Golang 的 Huggingface transformer 管线，基于 onnxruntime。
- [libsvm](https://github.com/datastream/libsvm) - 基于 LIBSVM 3.14 衍生移植的 golang 版 libsvm。
- [m2cgen](https://github.com/BayesWitnesses/m2cgen) - 命令行工具，把训练好的经典机器学习模型转译为零依赖的原生 Go 代码；用 Python 编写，支持 Go 语言。
- [neural-go](https://github.com/schuyler/neural-go) - 用 Go 实现的多层感知机网络，通过反向传播训练。
- [ocrserver](https://github.com/otiai10/ocrserver) - 简易 OCR API 服务器，用 Docker 与 Heroku 部署非常方便。
- [onnx-go](https://github.com/owulveryck/onnx-go) - Go 对 Open Neural Network Exchange（ONNX）的接口。
- [probab](https://github.com/ThePaw/probab) - 概率分布函数与贝叶斯推断。纯 Go 编写。
- [randomforest](https://github.com/malaschitz/randomForest) - 易用的 Go 随机森林库。
- [regommend](https://github.com/muesli/regommend) - 推荐与协同过滤引擎。
- [shield](https://github.com/eaigner/shield) - 贝叶斯文本分类器，为 Go 提供灵活的分词器与存储后端。
- [tfgo](https://github.com/galeone/tfgo) - 易用的 Tensorflow 绑定：简化官方 Tensorflow Go 绑定的使用。可在 Go 中定义计算图，加载并执行在 Python 中训练的模型。
- [Varis](https://github.com/Xamber/Varis) - Golang 神经网络。

**[⬆ 回到顶部](#contents)**

<a id="messaging"></a>
## 消息

_实现消息系统的库。_

- [ami](https://github.com/kak-tus/ami) - 基于 Redis Cluster Streams 的可靠队列 Go 客户端。
- [amqp](https://github.com/rabbitmq/amqp091-go) - Go RabbitMQ 客户端库。
- [APNs2](https://github.com/sideshow/apns2) - 面向 Go 的 HTTP/2 Apple 推送通知服务提供器 —— 向 iOS、tvOS、Safari 与 macOS 应用发送推送通知。
- [Asynq](https://github.com/hibiken/asynq) - 基于 Redis 构建的简单、可靠、高效的 Go 分布式任务队列。
- [backlite](https://github.com/mikestefanello/backlite) - 类型安全、持久化、嵌入式的任务队列与后台作业运行器，基于 SQLite。
- [Beaver](https://github.com/Clivern/Beaver) - 实时消息服务器，用于在 Web 与移动应用中构建可扩展的应用内通知、多人游戏与聊天应用。
- [broker](https://github.com/qvcloud/broker) - 生产级消息抽象，为各类消息中间件提供统一 API，并内置 OpenTelemetry 集成。
- [Bus](https://github.com/mustafaturan/bus) - 用于内部通信的极简消息总线实现。
- [Centrifugo](https://github.com/centrifugal/centrifugo) - Go 中的实时消息（Websockets 或 SockJS）服务器。
- [Chanify](https://github.com/chanify/chanify) - 推送通知服务器，向你的 iOS 设备发送消息。
- [Commander](https://github.com/jeroenrinzema/commander) - 高级事件驱动的生产者/消费者，支持 Apache Kafka 等多种「方言」。
- [Confluent Kafka Golang Client](https://github.com/confluentinc/confluent-kafka-go) - confluent-kafka-go 是 Confluent 面向 Apache Kafka 与 Confluent Platform 的 Golang 客户端。
- [dbus](https://github.com/godbus/dbus) - D-Bus 的原生 Go 绑定。
- [drone-line](https://github.com/appleboy/drone-line) - 通过 binary、docker 或 Drone CI 发送 [Line](https://at.line.me/en) 通知。
- [emitter](https://github.com/olebedev/emitter) - 以 Go 的方式发出事件，支持通配符、断言、可取消以及诸多其他优点。
- [event](https://github.com/agoalofalife/event) - 观察者模式的实现。
- [EventBus](https://github.com/asaskevich/EventBus) - 轻量事件总线，兼容异步。
- [gaurun-client](https://github.com/osamingo/gaurun-client) - 用 Go 编写的 Gaurun 客户端。
- [Glue](https://github.com/desertbit/glue) - 稳健的 Go 与 JavaScript Socket 库（Socket.io 的替代方案）。
- [go-eventbus](https://github.com/stanipetrosyan/go-eventbus) - Go 的简易事件总线包。
- [Go-MediatR](https://github.com/mehdihadeli/Go-MediatR) - 用于在事件驱动架构中处理中介者模式与简化 CQRS 模式的库，灵感源自 C# 的 MediatR 库。
- [go-mq](https://github.com/cheshir/go-mq) - 支持声明式配置的 RabbitMQ 客户端。
- [go-notify](https://github.com/TheCreeper/go-notify) - freedesktop 通知规范的原生实现。
- [go-nsq](https://github.com/nsqio/go-nsq) - NSQ 的官方 Go 包。
- [go-res](https://github.com/jirenius/go-res) - 用于构建 REST/实时服务的包，基于 NATS 与 Resgate，让客户端无缝同步。
- [go-vitotrol](https://github.com/maxatome/go-vitotrol) - Viessmann Vitotrol web 服务的客户端库。
- [GoEventBus](https://github.com/Raezil/GoEventBus) - 闪电般快速的内存无锁事件总线库。
- [Gollum](https://github.com/trivago/gollum) - 一个 n:m 多路复用器，从不同来源汇聚消息并广播到一组目标。
- [golongpoll](https://github.com/jcuga/golongpoll) - HTTP 长轮询服务器库，让 web 发布订阅变得简单。
- [gopush-cluster](https://github.com/Terry-Mao/gopush-cluster) - gopush-cluster 是一个 Go 推送服务器集群。
- [gorush](https://github.com/appleboy/gorush) - 使用 [APNs2](https://github.com/sideshow/apns2) 与 Google [GCM](https://github.com/google/go-gcm) 的推送通知服务器。
- [gosd](https://github.com/alexsniffin/gosd) - 用于调度何时向 channel 派发消息的库。
- [guble](https://github.com/smancke/guble) - 消息服务器，使用推送通知（Google Firebase Cloud Messaging、Apple Push Notification 服务、短信）以及 WebSocket，提供 REST API，并具备分布式运行与消息持久化能力。
- [hare](https://github.com/leozz37/hare) - 易于使用的库，用于发送消息与监听 TCP socket。
- [hub](https://github.com/leandro-lugaresi/hub) - 面向 Go 应用的消息/事件中心，采用发布/订阅模式，并支持类似 RabbitMQ exchange 的别名机制。
- [hypermatch](https://github.com/SchwarzDigits/hypermatch) - 依据大量规则匹配事件，规则可用 Go 编写或以 JSON 表达。
- [jazz](https://github.com/socifi/jazz) - 简易 RabbitMQ 抽象层，用于队列管理以及消息的发布与消费。
- [machinery](https://github.com/RichardKnop/machinery) - 基于分布式消息传递的异步任务队列/作业队列。
- [mangos](https://github.com/nanomsg/mangos) - 纯 Go 实现的 Nanomsg（可扩展性协议），支持传输层互操作。
- [melody](https://github.com/olahol/melody) - 处理 WebSocket 会话的极简框架，内置广播与自动 ping/pong 处理。
- [Mercure](https://github.com/dunglas/mercure) - 使用 Mercure 协议（构建于 Server-Sent Events 之上）派发服务器推送更新的服务器与库。
- [messagebus](https://github.com/vardius/message-bus) - messagebus 是一个简单异步的 Go 消息总线，在做事件溯源、CQRS、DDD 时非常适合用作事件总线。
- [NATS Go Client](https://github.com/nats-io/nats.go) - NATS 的 Go 客户端。
  messaging system.
- [nsq-event-bus](https://github.com/rafaeljesus/nsq-event-bus) - NSQ topic 与 channel 的极简封装。
- [oplog](https://github.com/dailymotion/oplog) - 面向 REST API 的通用 oplog/复制系统。
- [pubsub](https://github.com/tuxychandru/pubsub) - Go 的简易发布订阅包。
- [Quamina](https://github.com/timbray/quamina) - 用于过滤消息与事件的快速模式匹配。
- [rabbitroutine](https://github.com/furdarius/rabbitroutine) - 轻量库，处理 RabbitMQ 自动重连与发布重试。该库考虑了重连后需要在 RabbitMQ 中重新声明实体的需求。
- [rabbus](https://github.com/rafaeljesus/rabbus) - amqp exchange 与 queue 的极简封装。
- [rabtap](https://github.com/jandelgado/rabtap) - RabbitMQ 瑞士军刀式命令行应用。
- [RapidMQ](https://github.com/sybrexsys/RapidMQ) - RapidMQ 是用于管理本地消息队列的轻量可靠库。
- [Ratus](https://github.com/hyperonym/ratus) - Ratus 是一个 RESTful 异步任务队列服务器。
- [redisqueue](https://github.com/robinjoseph08/redisqueue) - redisqueue 提供了一个使用 Redis streams 的队列生产者与消费者。
- [rmqconn](https://github.com/sbabiv/rmqconn) - RabbitMQ 重连。对 amqp.Connection 与 amqp.Dial 的封装，允许在连接断开时重连，而非强制调用 Close() 方法关闭。
- [sarama](https://github.com/Shopify/sarama) - 面向 Apache Kafka 的 Go 库。
- [Uniqush-Push](https://github.com/uniqush/uniqush-push) - 基于 Redis 的统一推送服务，用于向移动设备发送服务端通知。
- [varmq](https://github.com/goptics/varmq) - 与存储无关的消息队列与 worker 池，面向并发 Go 程序。
- [Watermill](https://github.com/ThreeDotsLabs/watermill) - 高效处理消息流。构建事件驱动应用，支持事件溯源、基于消息的 RPC、Saga。可使用 Kafka 或 RabbitMQ 等传统发布订阅实现，也可用 HTTP 或 MySQL binlog。
- [zmq4](https://github.com/pebbe/zmq4) - Go 对 ZeroMQ 4.x 版本的接口。同时也提供 [version 3](https://github.com/pebbe/zmq3) 与 [version 2](https://github.com/pebbe/zmq2) 版本。

**[⬆ 回到顶部](#contents)**

<a id="microsoft-office"></a>
## Microsoft Office

- [unioffice](https://github.com/unidoc/unioffice) - 纯 Go 库，用于创建与处理 Office Word（.docx）、Excel（.xlsx）与 Powerpoint（.pptx）文档。

<a id="microsoft-excel"></a>
### Microsoft Excel

_用于处理 Microsoft Excel 的库。_

- [cellwalker](https://github.com/chonla/cellwalker) - 以单元格名为路径在 Excel 中遍历。
- [excelize](https://github.com/xuri/excelize) - 读写 Microsoft Excel&trade;（XLSX）文件的 Golang 库。
- [exl](https://github.com/go-the-way/exl) - Excel 到 Go 结构体的绑定。（仅支持 Go1.18+）
- [go-excel](https://github.com/szyhf/go-excel) - 简单轻量的读取器，把类似关系型数据库的 Excel 当作表格读取。
- [xlsx](https://github.com/tealeg/xlsx) - 在 Go 程序中简化读取新版 Microsoft Excel 所用 XML 格式的库。
- [xlsx](https://github.com/plandem/xlsx) - 在 Go 程序中快速且安全地读写既有 Microsoft Excel 文件的方式。

<a id="microsoft-word"></a>
### Microsoft Word

_用于处理 Microsoft Word 的库。_

- [godocx](https://github.com/gomutex/godocx) - 用于读写 Microsoft Word（Docx）文件的库。

**[⬆ 回到顶部](#contents)**

<a id="miscellaneous"></a>
## 杂项

<a id="dependency-injection"></a>
### 依赖注入

_用于依赖注入的库。_

- [alice](https://github.com/magic003/alice) - 面向 Golang 的可加式依赖注入容器。
- [autowire](https://github.com/tiendc/autowire) - 使用泛型与反射实现的依赖注入。
- [boot-go](http://github.com/boot-go/boot) - 面向 Go 开发者的基于组件的依赖注入开发方式（使用反射）。
- [componego](https://github.com/componego/componego) - 基于组件的依赖注入框架，允许动态替换依赖而无需在测试中重复代码。
- [cosban/di](https://gitlab.com/cosban/di) - 基于代码生成的依赖注入接线工具。
- [dig](https://github.com/uber-go/dig) - 面向 Go 的基于反射的依赖注入工具集。
- [dingo](https://github.com/i-love-flamingo/dingo) - 面向 Go 的依赖注入工具集，基于 Guice。
- [do](https://github.com/samber/do) - 基于泛型的依赖注入框架。
- [floatdrop/di](https://github.com/floatdrop/di) - 基于泛型方法构建的依赖注入容器，具备子作用域、生命周期钩子，并在构建任何对象之前进行图校验。
- [fx](https://github.com/uber-go/fx) - 面向 Go 的基于依赖注入的应用框架（构建于 dig 之上）。
- [go-beans](https://github.com/go-beans/go) - 受 Spring 启发的 Go 依赖注入与应用生命周期框架。
- [Go-Spring](https://github.com/go-spring/spring-core) - 受 Spring Boot 启发的高性能 Go 框架，提供依赖注入、自动配置与生命周期管理，同时保持 Go 的简洁与高效。
- [gocontainer](https://github.com/vardius/gocontainer) - 简易依赖注入容器。
- [godi](https://github.com/junioryono/godi) - 微软风格的 Go 依赖注入，支持作用域生命周期与泛型。
- [goioc/di](https://github.com/goioc/di) - 受 Spring 启发的依赖注入容器。
- [GoLobby/Container](https://github.com/golobby/container) - GoLobby Container 是面向 Go 编程语言的轻量却强大的 IoC 依赖注入容器。
- [gontainer](https://github.com/NVIDIA/gontainer) - 面向 Go 项目的依赖注入服务容器。
- [gontainer/gontainer](https://github.com/gontainer/gontainer) - 基于 YAML 的 Go 依赖注入容器。支持依赖作用域，并能自动检测循环依赖。Gontainer 是并发安全的。
- [HnH/di](https://github.com/HnH/di) - 专注于整洁 API 与灵活性的依赖注入容器库。
- [kinit](https://github.com/go-kata/kinit) - 可定制的依赖注入容器，具备全局模式、级联初始化与 panic 安全的终结处理。
- [kod](https://github.com/go-kod/kod) - 基于泛型的 Go 依赖注入框架。
- [linker](https://github.com/logrange/linker) - 基于反射的依赖注入与控制反转库，支持组件生命周期。
- [nject](https://github.com/muir/nject) - 类型安全、基于反射的框架，面向库、测试、HTTP 端点与服务启动。
- [ore](https://github.com/firasdarwish/ore) - 轻量、泛型且简单的依赖注入（DI）容器。
- [parsley](https://github.com/matzefriedrich/parsley) - 灵活、模块化、基于反射的 DI 库，具备作用域上下文与代理生成等高级特性，面向大规模 Go 应用设计。
- [wire](https://github.com/Fs02/wire) - 面向 Golang 的严格运行时依赖注入。
- [yama](https://github.com/livetribe/yama) - 编译期依赖注入与生命周期框架，为 Google Wire 依赖图生成 start、quiesce 与 stop 代码。

**[⬆ 回到顶部](#contents)**

<a id="project-layout"></a>
### 项目结构布局

_**非官方**的项目结构设计模式集合。_

- [ardanlabs/service](https://github.com/ardanlabs/service) - 用于构建生产级可扩展 Web 服务应用的[启动套件](https://github.com/ardanlabs/service/wiki)。
- [cookiecutter-golang](https://github.com/lacion/cookiecutter-golang) - Go 应用样板模板，帮助项目快速起步并遵循生产环境最佳实践。
- [go-blueprint](https://github.com/Melkeydev/go-blueprint) - 让用户能够借助流行框架快速搭建 Go 项目。
- [go-ddd](https://github.com/sklinkert/go-ddd) - 领域驱动设计模板，含 CQRS、值对象、幂等命令与事务性发件箱。
- [go-grpc-bazel-example](https://github.com/esurdam/go-grpc-bazel-example) - Go gRPC 微服务 monorepo 示例，集成 Bazel、grpc-gateway、OpenAPI 与 Kubernetes。
- [go-module](https://github.com/octomation/go-module) - Go 编写的典型模块的项目模板。
- [go-rest-api-boilerplate](https://github.com/vahiiiid/go-rest-api-boilerplate) - 对 AI 友好、可直接用于生产的 Go REST API 骨架，内置整洁架构、JWT 认证、RBAC、PostgreSQL、Docker 热重载与 Swagger 文档。
- [go-sample](https://github.com/zitryss/go-sample) - Go 应用项目的示例布局，附带真实代码。
- [go-starter](https://github.com/allaboutapps/go-starter) - 有明确主张、可直接用于生产的 RESTful JSON 后端模板，与 VSCode DevContainers 深度集成。
- [go-todo-backend](https://github.com/Fs02/go-todo-backend) - 使用模块化项目布局构建产品微服务的 Go Todo 后端示例。
- [goapp](https://github.com/naughtygopher/goapp) - 用于组织与开发 Go Web 应用/服务的实践指南。
- [gobase](https://github.com/wajox/gobase) - golang 应用的简易骨架，包含真实 Go 应用的基础搭建。
- [golang-standards/project-layout](https://github.com/golang-standards/project-layout) - Go 生态中常见与新兴项目布局模式的合集。注意：尽管以组织名命名，它们并不代表 Go 官方标准，详见 [该 issue](https://github.com/golang-standards/project-layout/issues/117)。尽管如此，其中一些布局或许对你有用。
- [golang-templates/seed](https://github.com/golang-templates/seed) - Go 应用 GitHub 仓库模板。
- [goxygen](https://github.com/shpota/goxygen) - 几秒钟内生成使用 Go 与 Angular、React 或 Vue 的现代 Web 项目。
- [insidieux/inizio](https://github.com/insidieux/inizio) - 带插件的 Golang 项目布局生成器。
- [kickstart.go](https://github.com/raeperd/kickstart.go) - 极简单文件 Go HTTP 服务器模板，无第三方依赖。
- [modern-go-application](https://github.com/sagikazarmark/modern-go-application) - 应用现代实践的 Go 应用骨架与示例。
- [nunu](https://github.com/go-nunu/nunu) - Nunu 是用于构建 Go 应用的脚手架工具。
- [pagoda](https://github.com/mikestefanello/pagoda) - 用 Go 构建的快速、易用全栈 Web 开发启动套件。
- [scaffold](https://github.com/catchplay/scaffold) - 脚手架可生成 Go 项目起始布局，让你专注于业务逻辑的实现。
- [wangyoucao577/go-project-layout](https://github.com/wangyoucao577/go-project-layout) - 关于如何组织 Go 项目布局的实践与讨论合集。

**[⬆ 回到顶部](#contents)**

<a id="strings"></a>
### 字符串

_用于字符串处理的库。_

- [bexp](https://github.com/happy-sdk/happy/tree/main/pkg/strings/bexp) - Brace Expansion 机制的 Go 实现，用于生成任意字符串。
- [caps](https://github.com/chanced/caps) - 大小写转换库。
- [go-formatter](https://gitlab.com/tymonx/go-formatter) - 实现由花括号 `{}` 包裹的**替换字段**格式化字符串。
- [gobeam/Stringy](https://github.com/gobeam/Stringy) - 字符串处理库，可转换为驼峰、下划线、短横线/slugify 等形式。
- [str](https://github.com/schigh/str) - 以管线优先的字符串工具集，用于组合各类转换。
- [strcase](https://github.com/charlievieth/strcase) - 标准库 strings/bytes 包的case-insensitive（忽略大小写）实现。
- [stringFormatter](https://github.com/Wissance/stringFormatter) - 以 Python 或 C# 风格进行字符串格式化，并附带额外的文本格式化特性。
- [strutil](https://github.com/ozgio/strutil) - 字符串工具集。
- [sttr](https://github.com/abhimanyu003/sttr) - 跨平台命令行应用，对字符串执行各类操作。
- [xstrings](https://github.com/huandu/xstrings) - 从其他语言移植而来的实用字符串函数合集。

**[⬆ 回到顶部](#contents)**

<a id="uncategorized"></a>
### 未分类

_这些库放在这里，是因为其他分类似乎都不太合适。_

- [anagent](https://github.com/mudler/anagent) - 极简、可插拔、支持依赖注入的 Golang 事件循环/定时器处理方案。
- [antch](https://github.com/antchfx/antch) - 快速、强大、可扩展的网页爬取与抓取框架。
- [archives](https://github.com/mholt/archives) - 跨平台、多格式的 Go 库，统一 API 处理各类归档与压缩格式，并提供兼容 io/fs 的虚拟文件系统。
- [autoflags](https://github.com/artyom/autoflags) - Go 包，自动从结构体字段定义命令行 flag。
- [avgRating](https://github.com/kirillDanshin/avgRating) - 基于威尔逊评分公式计算平均分与评分。
- [banner](https://github.com/dimiro1/banner) - 为你的 Go 应用添加漂亮的 banner 横幅。
- [base64Captcha](https://github.com/mojocn/base64Captcha) - Base64captch 支持数字、数字字母组合、字母、算术、音频与数字-字母混合验证码。
- [basexx](https://github.com/bobg/basexx) - 在各种进制之间进行数字字符串的转换。
- [battery](https://github.com/distatus/battery) - 跨平台、标准化的电池信息库。
- [bitio](https://github.com/icza/bitio) - 高度优化的 Go 位级 Reader 与 Writer。
- [browscap_go](https://github.com/digitalcrab/browscap_go) - 面向 [Browser Capabilities Project](https://browscap.org/) 的 GoLang 库。
- [captcha](https://github.com/steambap/captcha) - captcha 包为验证码生成提供易用且不预设立场的 API。
- [common](https://github.com/kubeservice-stack/common) - 服务器框架库。
- [conv](https://github.com/cstockton/go-conv) - conv 包提供跨 Go 类型的快速直观转换。
- [datacounter](https://github.com/miolini/datacounter) - 面向 Reader/Writer/http.ResponseWriter 的 Go 计数器。
- [fake-useragent](https://github.com/lib4u/fake-useragent) - 基于真实世界数据库的 Go 简易 useragent 生成器，保持数据更新。
- [faker](https://github.com/pioz/faker) - Go 的随机假数据与结构体生成器。
- [ffmt](https://github.com/go-ffmt/ffmt) - 为人类美化数据展示。
- [gatus](https://github.com/TwinProduction/gatus) - 自动化服务健康仪表盘。
- [go-commandbus](https://github.com/lana/go-commandbus) - 轻量且可插拔的 Go 命令总线。
- [go-commons-pool](https://github.com/jolestar/go-commons-pool) - 面向 Golang 的通用对象池。
- [go-openapi](https://github.com/go-openapi) - 用于解析与使用 OpenAPI schema 的包合集。
- [go-resiliency](https://github.com/eapache/go-resiliency) - Golang 的弹性（韧性）设计模式。
- [go-unarr](https://github.com/gen2brain/go-unarr) - RAR、TAR、ZIP 与 7z 归档的解压库。
- [gofakeit](https://github.com/brianvoe/gofakeit) - 用 Go 编写的随机数据生成器。
- [goffi](https://github.com/go-webgpu/goffi) - 纯 Go 的 FFI，采用 libffi 风格的类型化调用接口与结构化错误处理，无需 CGO 即可调用 C 库。
- [gommit](https://github.com/antham/gommit) - 分析 git 提交信息，确保其符合既定模式。
- [gopsutil](https://github.com/shirou/gopsutil) - 跨平台库，用于获取进程与系统占用情况（CPU、内存、磁盘等）。
- [gosh](https://github.com/osamingo/gosh) - 提供 Go 统计处理器、结构体与测量方法。
- [gosms](https://github.com/haxpax/gosms) - 用 Go 实现的本地短信网关，可用于发送短信。
- [gotoprom](https://github.com/cabify/gotoprom) - 面向官方 Prometheus 客户端的类型安全指标构建器封装库。
- [gountries](https://github.com/pariz/gountries) - 提供国家与行政区划数据的包。
- [gtree](https://github.com/ddddddO/gtree) - 提供 CLI、包与网页工具，可从 Markdown 或通过编程方式生成树状输出与目录。
- [health](https://github.com/alexliesenfeld/health) - Go 的简单灵活健康检查库。
- [health](https://github.com/dimiro1/health) - 易用、可扩展的健康检查库。
- [healthcheck](https://github.com/etherlabsio/healthcheck) - 面向 RESTful 服务、有明确主张且并发安全的健康检查 HTTP 处理器。
- [hostutils](https://github.com/Wing924/hostutils) - 用于打包与解包 FQDN 列表的 Go 库。
- [indigo](https://github.com/osamingo/indigo) - 基于 Sonyflake 生成并经 Base58 编码的分布式唯一 ID 生成器。
- [lk](https://github.com/hyperboloide/lk) - golang 的简易授权库。
- [llvm](https://github.com/llir/llvm) - 用于以纯 Go 与 LLVM IR 交互的库。
- [metrics](https://github.com/pascaldekloe/metrics) - 用于指标埋点与 Prometheus 暴露的库。
- [morse](https://github.com/alwindoss/morse) - 摩尔斯电码双向转换库。
- [numa](https://github.com/lrita/numa) - NUMA 是一个用 Go 编写的工具库，帮助我们编写 NUMA 感知的代码。
- [pdfgen](https://github.com/hyperboloide/pdfgen) - 根据 JSON 请求生成 PDF 的 HTTP 服务。
- [persian](https://github.com/mavihq/persian) - Go 中面向波斯语的一些工具。
- [purego](https://github.com/ebitengine/purego) - 无需 Cgo 即可从 Go 调用 C 函数的库。
- [sandid](https://github.com/aofei/sandid) - 地球上每一粒沙子都有自己的 ID。
- [shellwords](https://github.com/Wing924/shellwords) - 按 UNIX Bourne shell 的分词规则操作字符串的 Golang 库。
- [shortid](https://github.com/teris-io/shortid) - 分布式生成超短、唯一、非顺序、对 URL 友好的 ID。
- [shoutrrr](https://github.com/containrrr/shoutrrr) - 通知库，便捷接入 slack、mattermost、gotify、smtp 等各类消息服务。
- [sitemap-format](https://github.com/mingard/sitemap-format) - 简易站点地图生成器，附带一点语法糖。
- [stateless](https://github.com/qmuntal/stateless) - 用于创建状态机的流畅式库。
- [stats](https://github.com/go-playground/stats) - 监控 Go MemStats 与内存、Swap、CPU 等系统指标，并通过 UDP 发送到你指定的任意位置，用于日志等用途……
- [turtle](https://github.com/hackebrot/turtle) - Go 版表情符号库。
- [url-shortener](https://github.com/pantrif/url-shortener) - 现代化、强大且稳健的 URL 短链微服务，支持 mysql。
- [VarHandler](https://github.com/azr/generators/tree/master/varhandler) - 生成 HTTP 输入与输出处理的样板代码。
- [varint](https://github.com/chmike/varint) - 比标准库提供的实现更快的变长整数编解码器。
- [xdg](https://github.com/rkoesters/xdg) - 用 Go 实现的 FreeDesktop.org（xdg）规范。
- [xkg](https://github.com/go-xkg/xkg) - X 键盘捕获工具。
- [xz](https://github.com/ulikunitz/xz) - 用于读写 xz 压缩文件的纯 golang 包。
**[⬆ 回到顶部](#contents)**

<a id="natural-language-processing"></a>
## 自然语言处理

_用于自然语言处理的库。_

另见[文本处理](#text-processing)与[文本分析](#text-analysis)。

<a id="language-detection"></a>
### 语言检测

- [detectlanguage](https://github.com/detectlanguage/detectlanguage-go) - 语言检测 API 的 Go 客户端。支持批量请求、短语或单词级语言检测。
- [getlang](https://github.com/rylans/getlang) - 快速的自然语言检测包。
- [guesslanguage](https://github.com/endeveit/guesslanguage) - 用于判定 Unicode 文本自然语言的函数。
- [lingua-go](https://github.com/pemistahl/lingua-go) - 精确的自然语言检测库，长短文本皆适用。支持检测混合语言文本中的多种语言。
- [whatlanggo](https://github.com/abadojack/whatlanggo) - Go 的自然语言检测包。支持 84 种语言与 24 种文字系统（如拉丁文、西里尔文等）。

<a id="morphological-analyzers"></a>
### 形态分析器

- [go-propisyu](https://github.com/rekurt/go-propisyu) - 将数字转换为俄语单词，语法性数与名词变格均正确。
- [go-stem](https://github.com/agonopol/go-stem) - porter 词干提取算法的实现。
- [go2vec](https://github.com/danieldk/go2vec) - 用于读取 word2vec 嵌入的读取器与工具函数。
- [golibstemmer](https://github.com/rjohnsondev/golibstemmer) - Snowball libstemmer 库的 Go 绑定，包含 porter 2。
- [gosentiwordnet](https://github.com/dinopuguh/gosentiwordnet) - 用 Go 基于 sentiwordnet 词典实现的情感分析器。
- [govader](https://github.com/jonreiter/govader) - [VADER 情感分析](https://github.com/cjhutto/vaderSentiment)的 Go 实现。
- [govader-backend](https://github.com/PIMPfiction/govader_backend) - [GoVader](https://github.com/jonreiter/govader) 的微服务实现。
- [kagome](https://github.com/ikawaha/kagome) - 用纯 Go 编写的日语形态分析器。
- [libtextcat](https://github.com/goodsign/libtextcat) - libtextcat C 库的 Cgo 绑定，担保与 2.2 版本兼容。
- [nlp](https://github.com/james-bowman/nlp) - Go 自然语言处理库，支持 LSA（潜在语义分析）。
- [paicehusk](https://github.com/rookii/paicehusk) - Paice/Husk 词干提取算法的 Golang 实现。
- [porter](https://github.com/a2800276/porter) - 这是 Martin Porter 词干提取算法 C 实现的相当直接的移植。
- [porter2](https://github.com/zhenjl/porter2) - 极快的 Porter 2 词干提取器。
- [RAKE.go](https://github.com/afjoseph/RAKE.Go) - 快速自动关键词提取算法（RAKE）的 Go 移植。
- [snowball](https://github.com/goodsign/snowball) - Snowball 词干提取器的 Go 移植（cgo 封装），提供词干提取功能，对应 [Snowball 原生实现](http://snowball.tartarus.org/)。
- [spaGO](https://github.com/nlpodyssey/spago) - Go 中自包含的机器学习与自然语言处理库。
- [spelling-corrector](https://github.com/jorelosorio/spellingcorrector) - 西班牙语拼写纠正器，或用来创建你自己的。

<a id="slugifiers"></a>
### Slug 生成器

- [go-slugify](https://github.com/mozillazg/go-slugify) - 生成漂亮 slug，支持多语言。
- [slug](https://github.com/gosimple/slug) - 对 URL 友好的 slugify，支持多语言。
- [Slugify](https://github.com/avelino/slugify) - 处理字符串的 Go slugify 应用。

<a id="tokenizers"></a>
### 分词器

- [gojieba](https://github.com/yanyiwu/gojieba) - [jieba](https://github.com/fxsjy/jieba) 的 Go 实现 —— 一个中文分词算法。
- [gotokenizer](https://github.com/xujiajun/gotokenizer) - 基于词典与 Bigram 语言模型的 Golang 分词器。（目前仅支持中文分词）
- [gse](https://github.com/go-ego/gse) - Go 的高效文本分词，支持英文、中文、日文及其他语言。
- [MMSEGO](https://github.com/awsong/MMSEGO) - [MMSEG](http://technology.chtsai.org/mmseg/) 的 Go 实现 —— 一个中文分词算法。
- [segment](https://github.com/blevesearch/segment) - Go 库，用于按 [Unicode 标准附录 #29](https://www.unicode.org/reports/tr29/) 描述的方式执行 Unicode 文本分段。
- [sentences](https://github.com/neurosnap/sentences) - 句子分词器：把文本转换为句子列表。
- [shamoji](https://github.com/osamingo/shamoji) - shamoji 是用 Go 编写的词语过滤包。
- [stemmer](https://github.com/dchest/stemmer) - Go 编程语言的词干提取器包集合，包含英语与德语词干提取器。
- [textcat](https://github.com/pebbe/textcat) - 基于 n-gram 的 Go 文本分类包，支持 utf-8 与原始文本。

<a id="translation"></a>
### 翻译

- [ctxi18n](https://github.com/invopop/ctxi18n/) - 上下文感知的国际化方案，API 简短精炼，支持复数、插值与 `fs.FS`。YAML 语言包定义基于 [Rails i18n](https://guides.rubyonrails.org/i18n.html)。
- [go-i18n](https://github.com/nicksnyder/go-i18n/) - 用于处理本地化文本的包及配套工具。
- [go-mystem](https://github.com/dveselov/mystem) - Yandex.Mystem（俄语形态分析器）的 CGo 绑定。
- [go-pinyin](https://github.com/mozillazg/go-pinyin) - 汉字转汉语拼音转换器。
- [go-words](https://github.com/saleh-rahimzadeh/go-words) - 面向 Golang 项目的词表与文本资源库。
- [gotext](https://github.com/leonelquinteros/gotext) - Go 的 GNU gettext 工具。
- [iuliia-go](https://github.com/mehanizm/iuliia-go) - 以所有可能的方式完成西里尔文 → 拉丁文转写。
- [spreak](https://github.com/vorlif/spreak) - Go 的灵活翻译与本地化库，基于 gettext 背后的设计理念。
- [t](https://github.com/youthlin/t) - 另一个 golang 国际化包，遵循 GNU gettext 风格并支持 .po/.mo 文件：`t.T`（gettext）、`t.N`（ngettext）等。并内置命令行工具 [xtemplate](https://github.com/youthlin/t/blob/main/cmd/xtemplate)，可从 text/html 模板中提取消息生成 pot 文件。

<a id="transliteration"></a>
### 音译

- [enca](https://github.com/endeveit/enca) - [libenca](https://cihar.com/software/enca/) 的极简 cgo 绑定，用于检测字符编码。
- [go-unidecode](https://github.com/mozillazg/go-unidecode) - Unicode 文本的 ASCII 转写。
- [gounidecode](https://github.com/fiam/gounidecode) - Go 的 Unicode 转写器（亦称 unidecode）。
- [transliterator](https://github.com/alexsergivan/transliterator) - 提供单向字符串转写，并支持语言特定的转写规则。

**[⬆ 回到顶部](#contents)**

<a id="networking"></a>
## 网络

_用于处理网络各层的库。_

- [arp](https://github.com/mdlayher/arp) - arp 包实现 RFC 826 描述的 ARP 协议。
- [bart](https://github.com/gaissmai/bart) - bart 包提供平衡路由表（BART），用于极快的 IP 到 CIDR 查询等。
- [buffstreams](https://github.com/stabbycutyou/buffstreams) - 让基于 TCP 流式传输 protobuf 数据变得简单。
- [canopus](https://github.com/zubairhamed/canopus) - CoAP 客户端/服务器实现（RFC 7252）。
- [cdns](https://github.com/junevm/cdns) - 在终端中轻松切换 DNS 服务器。
- [chicha-ip-proxy](https://github.com/matveynator/chicha-ip-proxy) - 零配置的 TCP/UDP 端口代理，支持自启动、基于 IP 的访问控制与操作系统级网络栈调优。
- [cidranger](https://github.com/yl2chen/cidranger) - Go 的快速 IP 到 CIDR 查询。
- [cloudflared](https://github.com/cloudflare/cloudflared) - Cloudflare Tunnel 客户端（原 Argo Tunnel）。
- [dhcp6](https://github.com/mdlayher/dhcp6) - dhcp6 包实现 RFC 3315 描述的 DHCPv6 服务器。
- [dns](https://github.com/miekg/dns) - 用于处理 DNS 的 Go 库。
- [dnsmonster](https://github.com/mosajjal/dnsmonster) - 被动 DNS 抓取/监控框架。
- [drainwatch](https://github.com/jaynirmal15/drainwatch) - 度量 Kubernetes Pod 终止时，已建立的 TCP 与 UDP 连接实际发生了什么。
- [easytcp](https://github.com/DarthPestilane/easytcp) - 用 Go (Golang) 编写的轻量级 TCP 框架，内置消息路由器。EasyTCP 帮助你轻松、快速、少痛苦地构建 TCP 服务器。
- [ether](https://github.com/songgao/ether) - 跨平台的 Go 包，用于收发以太网帧。
- [ethernet](https://github.com/mdlayher/ethernet) - ethernet 包实现 IEEE 802.3 以太网 II 帧与 IEEE 802.1Q VLAN 标签的编解码。
- [event](https://github.com/cheng-zhongliang/event) - 用 Golang 编写的简单 I/O 事件通知库。
- [expose](https://github.com/kernelshard/expose) - 轻量级开源安全隧道工具，将本地服务器暴露到互联网。
- [fasthttp](https://github.com/valyala/fasthttp) - fasthttp 包是 Go 的快速 HTTP 实现，比 net/http 最快可达 10 倍。
- [fibersse](https://github.com/vinod-morya/fibersse) - 面向 Fiber v3 的生产级 Server-Sent Events（SSE），支持事件合并、优先级通道、主题通配符、自适应节流与内置认证。
- [fortio](https://github.com/fortio/fortio) - 负载测试库与命令行工具，配备高级 echo 服务器与 Web 界面。可指定一组每秒查询数负载，记录延迟直方图与其他有用统计并绘图。支持 TCP、HTTP、gRPC。
- [ftp](https://github.com/jlaffaye/ftp) - ftp 包实现 [RFC 959](https://tools.ietf.org/html/rfc959) 描述的 FTP 客户端。
- [ftpserverlib](https://github.com/fclairamb/ftpserverlib) - 功能完备的 FTP 服务器库。
- [fullproxy](https://github.com/shoriwe/fullproxy) - 功能完备、可脚本化、可作为守护进程配置的代理与枢轴工具包，支持 SOCKS5、HTTP、原始端口与反向代理协议。
- [fwdctl](https://github.com/alegrey91/fwdctl) - 在 Linux 服务器上管理 IPTables 转发规则的简单直观 CLI。
- [gaio](https://github.com/xtaci/gaio) - 面向 Golang 的高性能异步 IO 网络，proactor 模式。
- [gev](https://github.com/Allenxuxu/gev) - gev 是基于 Reactor 模式的轻量快速非阻塞 TCP 网络库。
- [gldap](https://github.com/jimlambrt/gldap) - gldap 提供 LDAP 服务器实现，由你为它的 LDAP 操作提供处理器。
- [gmqtt](https://github.com/DrmagicE/gmqtt) - Gmqtt 是灵活的高性能 MQTT broker 库，完整实现 MQTT 协议 V3.1.1。
- [gnet](https://github.com/panjf2000/gnet) - `gnet` 是用纯 Go 编写的高性能、轻量、非阻塞、事件驱动的网络框架。
- [gnet](https://github.com/fish-tennis/gnet) - `gnet` 是高性能网络框架，尤其适合游戏服务器。
- [gNxI](https://github.com/google/gnxi) - 一组使用 gNMI 与 gNOI 协议的网络管理工具。
- [go-getter](https://github.com/hashicorp/go-getter) - Go 库，用于通过 URL 从各种来源下载文件或目录。
- [go-multiproxy](https://github.com/presbrey/go-multiproxy) - 通过代理池发起 HTTP 请求的库，提供容错、负载均衡、自动重试、Cookie 管理等能力，可作为 http.Get/Post 的替代或 http.Client RoundTripper 直接替换。
- [go-pcaplite](https://github.com/alexcfv/go-pcaplite) - 轻量级实时抓包库，支持提取 HTTPS SNI。
- [go-powerdns](https://github.com/joeig/go-powerdns) - Golang 的 PowerDNS API 绑定。
- [go-sse](https://github.com/lampctl/go-sse) - HTML 服务器推送事件的 Go 客户端与服务器实现。
- [go-stun](https://github.com/ccding/go-stun) - STUN 客户端（RFC 3489 与 RFC 5389）的 Go 实现。
- [gobgp](https://github.com/osrg/gobgp) - 用 Go 编程语言实现的 BGP。
- [gopacket](https://github.com/google/gopacket) - 基于 libpcap 绑定、用于数据包处理的 Go 库。
- [gopcap](https://github.com/akrennmair/gopcap) - libpcap 的 Go 封装。
- [GoProxy](https://github.com/elazarl/goproxy) - 用 Go 创建定制化 HTTP/HTTPS 代理服务器的库。
- [goshark](https://github.com/sunwxg/goshark) - goshark 包使用 tshark 解码 IP 数据包并创建数据结构以供分析。
- [gosnmp](https://github.com/soniah/gosnmp) - 执行 SNMP 操作的原生 Go 库。
- [gotcp](https://github.com/gansidui/gotcp) - 用于快速编写 TCP 应用程序的 Go 包。
- [grab](https://github.com/cavaliercoder/grab) - 用于管理文件下载的 Go 包。
- [graval](https://github.com/koofr/graval) - 实验性的 FTP 服务器框架。
- [gws](https://github.com/lxzan/gws) - 基于 AsyncIO 的高性能 WebSocket 服务器与客户端。
- [HTTPLab](https://github.com/gchaincl/httplab) - HTTPLabs 让你检查 HTTP 请求并伪造响应。
- [httpproxy](https://github.com/wzshiming/httpproxy) - HTTP 代理处理器与拨号器。
- [iplib](https://github.com/c-robinson/iplib) - 用于处理 IP 地址（net.IP、net.IPNet）的库，灵感来自 python 的 [ipaddress](https://docs.python.org/3/library/ipaddress.html) 与 ruby 的 [ipaddr](https://ruby-doc.org/stdlib-2.5.1/libdoc/ipaddr/rdoc/IPAddr.html)
- [jazigo](https://github.com/udhos/jazigo) - Jazigo 是用 Go 编写的工具，用于批量获取多台网络设备的配置。
- [kcp-go](https://github.com/xtaci/kcp-go) - KCP —— 快速可靠 ARQ 协议。
- [lhttp](https://github.com/fanux/lhttp) - 强大的 WebSocket 框架，让构建 IM 服务器更轻松。
- [linkio](https://github.com/ian-kent/linkio) - 面向 Reader/Writer 接口的网络链路速度模拟。
- [llb](https://github.com/kirillDanshin/llb) - 这是一个非常简单但迅捷的代理服务器后端。可用于零内存分配、快速响应地重定向到预定义域名。
- [macwifi](https://github.com/jaisonerick/macwifi) - 面向 macOS 13+ 的 Wi-Fi 扫描与钥匙串密码获取。
- [mdns](https://github.com/hashicorp/mdns) - Golang 中简单的 mDNS（组播 DNS）客户端/服务器库。
- [mqttPaho](https://eclipse.org/paho/clients/golang/) - Paho Go 客户端提供 MQTT 客户端库，可通过 TCP、TLS 或 WebSocket 连接 MQTT broker。
- [natiu-mqtt](https://github.com/soypat/natiu-mqtt) - 极简、零分配、低层次的 MQTT 实现，非常适合嵌入式系统。
- [nbio](https://github.com/lesismal/nbio) - 纯 Go 的 100 万+ 连接方案，支持 tls/http1.x/websocket，与 net/http 高度兼容，性能高、内存开销小，非阻塞、事件驱动、易于使用。
- [net](https://golang.org/x/net) - 本仓库收录补充性的 Go 网络类库。
- [netchan](https://github.com/matveynator/netchan) - Golang 的网络通道（netchan）：安全、可集群、支持嵌套通道与任意数据类型。灵感来自 Rob Pike。
- [nethawk](https://github.com/Flowtriq/nethawk) - 用于实时网络流量抓取、分析与攻击检测的终端 UI，支持 JSON 输出模式。
- [netpoll](https://github.com/cloudwego/netpoll) - 高性能非阻塞 IO 网络框架，聚焦 RPC 场景，由字节跳动开发。
- [NFF-Go](https://github.com/intel-go/nff-go) - 用于快速开发云与裸金属环境高性能网络功能的框架（原 YANFF）。
- [nodepass](https://github.com/NodePassProject/nodepass) - 安全高效的 TCP/UDP 隧道方案，借助预建立的 TCP/QUIC/WebSocket 或 HTTP/2 连接，突破网络限制实现快速可靠访问。
- [peerdiscovery](https://github.com/schollz/peerdiscovery) - 纯 Go 库，使用 UDP 组播实现跨平台局域网对等发现。
- [portproxy](https://github.com/aybabtme/portproxy) - 简单 TCP 代理，为不支持 CORS 的 API 补上 CORS 支持。
- [proxq](https://github.com/psyb0t/docker-proxq) - 异步反向代理，将每个请求排入 Redis 队列并返回 job ID 供轮询响应，支持路径前缀路由、重试与缓存。
- [psql-wire](https://github.com/jeroenrinzema/psql-wire) - PostgreSQL 服务端线路协议。构建你自己的服务器并开始提供连接服务……
- [publicip](https://github.com/polera/publicip) - publicip 包返回你的公网 IPv4 地址（互联网出口）。
- [quic-go](https://github.com/lucas-clemente/quic-go) - QUIC 协议的纯 Go 实现。
- [roamr](https://github.com/sourabh-khot65/roamr) - CLI 对附近已保存的 WiFi 网络进行评分，告诉你该用哪个以及原因。
- [sdns](https://github.com/semihalev/sdns) - 高性能递归 DNS 解析服务器，支持 DNSSEC，注重隐私保护。
- [sftp](https://github.com/pkg/sftp) - sftp 包实现 <https://filezilla-project.org/specs/draft-ietf-secsh-filexfer-02.txt> 描述的 SSH 文件传输协议。
- [ssh](https://github.com/gliderlabs/ssh) - 构建 SSH 服务器的更高层 API（封装 crypto/ssh）。
- [sslb](https://github.com/eduardonunesp/sslb) - 这是一个超级简单的负载均衡器，只是个小项目，用于达成某种性能目标。
- [stun](https://github.com/go-rtc/stun) - RFC 5389 STUN 协议的 Go 实现。
- [tcpack](https://github.com/lim-yoona/tcpack) - tcpack 是基于 TCP 的应用协议，用于在 Go 程序中打包与解包字节流。
- [tspool](https://github.com/two/tspool) - 使用 worker 池提升性能、保护服务器的 TCP 库。
- [tun2socks](https://github.com/xjasonlyu/tun2socks) - 由 [gVisor](https://gvisor.dev/) TCP/IP 栈驱动的纯 Go 版 tun2socks 实现。
- [utp](https://github.com/anacrolix/utp) - Go 的 uTP 微型传输协议实现。
- [vssh](https://github.com/yahoo/vssh) - 用于在 SSH 协议之上构建网络与服务器自动化的 Go 库。
- [water](https://github.com/songgao/water) - 简易 TUN/TAP 库。
- [webrtc](https://github.com/pions/webrtc) - WebRTC API 的纯 Go 实现。
- [winrm](https://github.com/masterzen/winrm) - Go 版 WinRM 客户端，用于在 Windows 机器上远程执行命令。
- [ws-reconnect](https://github.com/sing198/ws-reconnect) - 弹性 WebSocket 客户端，具备自动重连、指数退避与心跳管理。
- [xtcp](https://github.com/xfxdev/xtcp) - TCP 服务器框架，支持同时全双工通信、优雅停机与自定义协议。

**[⬆ 回到顶部](#contents)**

<a id="http-clients"></a>
### HTTP 客户端

_用于发起 HTTP 请求的库。_

- [axios4go](https://github.com/rezmoss/axios4go) - 受 Axios 启发的 Go HTTP 客户端库，提供简单直观的 API 来发起 HTTP 请求。
- [azuretls-client](https://github.com/Noooste/azuretls-client) - 易于使用的 HTTP 客户端，100% 由 Go 实现，可伪装 TLS/JA3 与 HTTP2 指纹。
- [fast-shot](https://github.com/opus-domini/fast-shot) - 用 Go 最快最简的 HTTP 客户端，以连珠炮般的精准命中你的 API 目标。
- [gentleman](https://github.com/h2non/gentleman) - 功能完备、插件驱动的 HTTP 客户端库。
- [go-cleanhttp](https://github.com/hashicorp/go-cleanhttp) - 轻松获取标准库 HTTP 客户端，且不与其它客户端共享任何状态。
- [go-http-client](https://github.com/bozd4g/go-http-client) - 简单轻松地发起 http 调用。
- [go-ipmux](https://github.com/optimus-hft/go-ipmux) - 基于多个源 IP 对 HTTP 请求进行多路复用的库。
- [go-otelroundtripper](https://github.com/NdoleStudio/go-otelroundtripper) - 为 HTTP 请求发出 OpenTelemetry 指标的 Go http.RoundTripper。
- [go-req](https://github.com/wenerme/go-req) - 声明式 Golang HTTP 客户端。
- [go-retryablehttp](https://github.com/hashicorp/go-retryablehttp) - Go 的可重试 HTTP 客户端。
- [go-zoox/fetch](https://github.com/go-zoox/fetch) - 强大、轻量、易用的 HTTP 客户端，受 Web Fetch API 启发。
- [Grequest](https://github.com/lib4u/grequest)  - 简单轻量的 golang http 请求包，基于强大的 net/http。
- [grequests](https://github.com/levigross/grequests) - Go 版的 Requests 库「克隆」。
- [hedge](https://github.com/bhope/hedge) - Go 的自适应对冲请求（hedged requests）。基于 Google《The Tail at Scale》论文，零配置即可削减 p99 延迟。
- [heimdall](https://github.com/gojektech/heimdall) - 增强版 HTTP 客户端，具备重试与熔断能力。
- [httpretry](https://github.com/ybbus/httpretry) - 为 Go 默认 HTTP 客户端增添重试功能。
 - [impersonate-http](https://github.com/North-web-dev/impersonate-http) - 直接替换 net/http.Client，字节级精确的浏览器 TLS（JA3/JA4）与 HTTP/2（Akamai）指纹。
- [pester](https://github.com/sethgrid/pester) - 具备重试、退避与并发能力的 Go HTTP 客户端调用。
- [req](https://github.com/imroc/req) - 简单带「黑魔法」的 Go HTTP 客户端（更少代码，更高效率）。
- [request](https://github.com/monaco-io/request) - golang 的 HTTP 客户端。若你用过 axios 或 requests，你会喜欢它。无第三方依赖。
- [requests](https://github.com/carlmjohnson/requests) - 为 Go 程序员打造的 HTTP 请求库。使用 context.Context 且不隐藏底层 net/http.Client，与 Go 标准 API 兼容，并附带测试工具。
- [resty](https://github.com/go-resty/resty) - 受 Ruby rest-client 启发的 Go 简易 HTTP 与 REST 客户端。
- [rq](https://github.com/ddo/rq) - 为 golang 标准库 HTTP 客户端提供更友好的接口。
- [sling](https://github.com/dghubble/sling) - Sling 是用于创建与发送 API 请求的 Go HTTP 客户端库。
- [surf](https://github.com/enetx/surf) - 高级 HTTP 客户端，支持 HTTP/1.1、HTTP/2、HTTP/3（QUIC）、SOCKS5 代理以及浏览器级 TLS 指纹。
- [tls-client](https://github.com/bogdanfinn/tls-client) - 类 net/http.Client 的 HTTP 客户端，可选项选择用于请求的特定客户端 TLS 指纹。

**[⬆ 回到顶部](#contents)**

<a id="opengl"></a>
## OpenGL

_在 Go 中使用 OpenGL 的库。_

- [gl](https://github.com/go-gl/gl) - OpenGL 的 Go 绑定（由 glow 生成）。
- [glfw](https://github.com/go-gl/glfw) - GLFW 3 的 Go 绑定。
- [go-glmatrix](https://github.com/technohippy/go-glmatrix) - [glMatrix](https://glmatrix.net/) 库的 Go 移植。
- [goxjs/gl](https://github.com/goxjs/gl) - Go 跨平台 OpenGL 绑定（OS X、Linux、Windows、浏览器、iOS、Android）。
- [goxjs/glfw](https://github.com/goxjs/glfw) - Go 跨平台 GLFW 库，用于创建 OpenGL 上下文并接收事件。
- [mathgl](https://github.com/go-gl/mathgl) - 专为 3D 数学优化的纯 Go 数学包，灵感源自 GLM。

**[⬆ 回到顶部](#contents)**

<a id="orm"></a>
## ORM

_实现对象关系映射（ORM）或数据映射技术的库。_

- [bob](https://github.com/stephenafamo/bob) - Go 的 SQL 查询构建器与 ORM/Factory 生成器。SQLBoiler 的继任者。
- [bun](https://github.com/uptrace/bun) - SQL-first 的 Golang ORM。go-pg 的继任者。
- [cacheme](https://github.com/Yiling-J/cacheme-go) - 基于 schema 的类型安全 Go Redis 缓存/记忆化框架。
- [CQL](https://github.com/FrancoLiberali/cql) - 构建于 GORM 之上，基于自动生成代码提供编译期校验的查询。
- [ent](https://github.com/facebook/ent) - Go 的实体框架。简单却强大的 ORM，用于建模与查询数据。
- [go-dbw](https://github.com/hashicorp/go-dbw) - 封装数据库操作的简单包。
- [go-firestorm](https://github.com/jschoedt/go-firestorm) - 面向 Google/Firebase Cloud Firestore 的简易 ORM。
- [go-sql](https://github.com/rushteam/gosql) - 易于使用的 mysql ORM。
- [go-sqlbuilder](https://github.com/huandu/go-sqlbuilder) - 灵活强大的 SQL 字符串构建库，外加零配置 ORM。
- [go-store](https://github.com/gosuri/go-store) - Go 的简易快速 Redis 支撑键值存储库。
- [golobby/orm](https://github.com/golobby/orm) - 简单、快速、类型安全的泛型 ORM，为开发者幸福感而生。
- [GoooQo](https://github.com/doytowin/goooqo) - 基于声明式查询模型的数据库访问框架。
- [GORM](https://github.com/go-gorm/gorm) - Golang 的 ORM 神库，致力于对开发者友好。
- [gormt](https://github.com/xxjwxc/gormt) - 把 MySQL 数据库映射到 golang gorm 结构体。
- [gorp](https://github.com/go-gorp/gorp) - Go Relational Persistence —— Go 的类 ORM 库。
- [grimoire](https://github.com/Fs02/grimoire) - Grimoire 是 golang 的数据库访问层与校验库。（支持 MySQL、PostgreSQL 与 SQLite3）。
- [lore](https://github.com/abrahambotros/lore) - Go 的简单轻量伪 ORM/伪结构体映射环境。
- [marlow](https://github.com/marlow/marlow) - 由项目结构体生成的 ORM，提供编译期安全保障。
- [pop/soda](https://github.com/gobuffalo/pop) - 为 MySQL、PostgreSQL 与 SQLite 提供数据库迁移、创建、ORM 等能力。
- [Prisma](https://github.com/prisma/prisma-client-go) - Prisma Client Go，为 Go 提供类型安全的数据库访问。
- [reform](https://github.com/go-reform/reform) - 更好的 Go ORM，基于非空接口与代码生成。
- [rel](https://github.com/go-rel/rel) - 现代化的 Golang 数据库访问层 —— 可测试、可扩展，打磨成干净优雅的 API。
- [SQLBoiler](https://github.com/volatiletech/sqlboiler) - ORM 生成器。生成功能丰富、疾速飞快、完全贴合你数据库 schema 的 ORM。
- [upper.io/db](https://github.com/upper/db) - 通过使用封装成熟数据库驱动的适配器，以单一接口与不同数据源交互。
- [XORM](https://gitea.com/xorm/xorm) - Go 的简单强大 ORM。（支持 MySQL、MyMysql、PostgreSQL、Tidb、SQLite3、MsSql 与 Oracle）。
- [Zoom](https://github.com/albrow/zoom) - 构建于 Redis 之上的疾速数据存储与查询引擎。

**[⬆ 回到顶部](#contents)**

<a id="package-management"></a>
## 包管理

_官方依赖与包管理工具_

- [go modules](https://golang.org/cmd/go/#hdr-Modules__module_versions__and_more) - 模块是源代码交换与版本管理的基本单元。go 命令直接支持模块的使用，包括记录与解析对其他模块的依赖。

_非官方的包与依赖管理库。_

- [gup](https://github.com/nao1215/gup) - 更新通过 `go install` 安装的二进制文件。
- [modup](https://github.com/chaindead/modup) - Go 依赖更新的终端 UI，可检测过期模块并选择性升级。
- [syft](https://github.com/anchore/syft) - 用于从容器镜像与文件系统生成软件物料清单（SBOM）的 CLI 工具与 Go 库。

**[⬆ 回到顶部](#contents)**

<a id="performance"></a>
## 性能

- [ebpf-go](https://github.com/cilium/ebpf) - 提供加载、编译与调试 eBPF 程序的工具。
- [go-instrument](https://github.com/nikolaydubina/go-instrument) - 自动为所有方法与函数添加 span。
- [go-perfstat](https://github.com/go-perfstat/go) - Go 的轻量性能统计与执行耗时聚合。
- [jaeger](https://github.com/jaegertracing/jaeger) - 分布式追踪系统。
- [mm-go](https://github.com/joetifa2003/mm-go) - 面向 golang 的泛型手动内存管理。
- [otelinji](https://github.com/hedhyw/otelinji) - OpenTelemetry 自动埋点工具，为函数添加 span。
- [pixie](https://github.com/pixie-labs/pixie) - 通过 eBPF 为 Golang 应用实现免埋点追踪。
- [profile](https://github.com/pkg/profile) - Go 的简易性能剖析支持包。
- [statsviz](https://github.com/arl/statsviz) - Go 应用程序运行时统计信息的实时可视化。
- [tracer](https://github.com/kamilsk/tracer) - 简单轻量的追踪方案。

**[⬆ 回到顶部](#contents)**

<a id="query-language"></a>
## 查询语言

- [api-fu](https://github.com/ccbrown/api-fu) - 完备的 GraphQL 实现。
- [dasel](https://github.com/tomwright/dasel) - 在命令行中用选择器查询与更新数据结构。可与 jq/yq 媲美，但支持 JSON、YAML、TOML 与 XML，且零运行时依赖。
- [gnata](https://github.com/RecoLabs/gnata) - JSONata 2.x 查询与转换语言的纯 Go 实现。
- [gojsonq](https://github.com/thedevsaddam/gojsonq) - 用于对 JSON 数据进行查询的简易 Go 包。
- [goven](https://github.com/SeldonIO/goven) - 适用于任意数据库 schema 的即插即用查询语言。
- [gqlgen](https://github.com/99designs/gqlgen) - 基于 go generate 的 GraphQL 服务器库。
- [grapher](https://github.com/reaganiwadha/grapher) - 利用 Go 泛型的 GraphQL 字段构建器，附带额外工具与特性。
- [graphql](https://github.com/neelance/graphql-go) - 专注于易用性的 GraphQL 服务器。
- [graphql-go](https://github.com/graphql-go/graphql) - Go 的 GraphQL 实现。
- [gws](https://github.com/Zaba505/gws) - Apollo 的「GraphQL over WebSocket」客户端与服务器实现。
- [jsonpath](https://github.com/AsaiYusuke/jsonpath) - 依据 JSONPath 语法检索 JSON 部分的查询库。
- [jsonql](https://github.com/elgs/jsonql) - Golang 中的 JSON 查询表达式库。
- [jsonslice](https://github.com/bhmj/jsonslice) - 带高级过滤器的 Jsonpath 查询。
- [mql](https://github.com/hashicorp/mql) - Model Query Language (mql) 是面向数据库模型的查询语言。
- [play](https://github.com/paololazzari/play) - TUI 试验场，可摆弄你喜欢的 grep、sed、awk、jq 与 yq 等程序。
- [rql](https://github.com/a8m/rql) - 面向 REST API 的资源查询语言。
- [rqp](https://github.com/timsolov/rest-query-parser) - REST API 的查询解析器。过滤与校验开箱即用，查询中直接支持 `AND`、`OR` 运算。
- [straf](https://github.com/SonicRoshan/straf) - 轻松将 Golang 结构体转换为 GraphQL 对象。

**[⬆ 回到顶部](#contents)**

<a id="reflection"></a>
## 反射

- [copy](https://github.com/gotidy/copy) - 用于快速复制不同类型结构体的包。
- [Deepcopier](https://github.com/ulule/deepcopier) - Go 的简易结构体复制。
- [go-deepcopy](https://github.com/tiendc/go-deepcopy) - 快速的深拷贝库。
- [goenum](https://github.com/lvyahui8/goenum) - 基于泛型与反射的通用枚举结构体，让你快速定义枚举并使用一组实用的默认方法。
- [gotype](https://github.com/wzshiming/gotype) - Golang 源码解析，用法类似 reflect 包。
- [gpath](https://github.com/tenntenn/gpath) - 简化在反射中用 Go 表达式访问结构体字段的库。
- [objwalker](https://github.com/rekby/objwalker) - 通过反射遍历 Go 对象。
- [reflectpro](https://github.com/gontainer/reflectpro) - Go 的调用者、复制器、getter 与 setter。
- [reflectutils](https://github.com/muir/reflectutils) - 反射辅助工具：结构体标签解析、递归遍历、从字符串填充值。

**[⬆ 回到顶部](#contents)**

<a id="resource-embedding"></a>
## 资源嵌入

- [debme](https://github.com/leaanthony/debme) - 从现有的 `embed.FS` 子目录创建一个 `embed.FS`。
- [embed](https://pkg.go.dev/embed) - embed 包提供对嵌入在运行中的 Go 程序里的文件的访问。
- [rebed](https://github.com/soypat/rebed) - 从 Go 1.16 的 `embed.FS` 类型重建目录结构与文件。
- [vfsgen](https://github.com/shurcooL/vfsgen) - 生成 vfsdata.go 文件，静态实现给定的虚拟文件系统。

**[⬆ 回到顶部](#contents)**

<a id="science-and-data-analysis"></a>
## 科学与数据分析

_用于科学计算与数据分析的库。_

- [bradleyterry](https://github.com/seanhagen/bradleyterry) - 为成对比较提供 Bradley-Terry 模型。
- [calendarheatmap](https://github.com/nikolaydubina/calendarheatmap) - 受 GitHub 贡献活跃度启发的纯 Go 日历热力图。
- [chart](https://github.com/vdobler/chart) - Go 的简易图表绘制库，支持多种图形类型。
- [dataframe-go](https://github.com/rocketlaunchr/dataframe-go) - 面向机器学习与统计的 dataframe（类似 pandas）。
- [decimal](https://github.com/db47h/decimal) - decimal 包实现任意精度的十进制浮点运算。
- [entitydebs](https://github.com/ndabAP/entitydebs) - 社会科学工具，内置依存句法分析器，可编程分析非虚构文本中的实体。
- [evaler](https://github.com/soniah/evaler) - 浮点算术表达式求值器。
- [ewma](https://github.com/VividCortex/ewma) - 指数加权移动平均。
- [geom](https://github.com/skelterjohn/geom) - 面向 golang 的 2D 几何库。
- [go-dsp](https://github.com/mjibson/go-dsp) - Go 的数字信号处理。
- [go-estimate](https://github.com/milosgajdos/go-estimate) - Go 中的状态估计与滤波算法。
- [go-gt](https://github.com/ThePaw/go-gt) - 用「Go」语言编写的图论算法。
- [go-hep](https://github.com/go-hep/hep) - 一组用于轻松开展高能物理分析的库与工具。
- [godesim](https://github.com/soypat/godesim) - 面向基于事件仿真的扩展/多变量 ODE 求解器框架，API 简单。
- [goent](https://github.com/kzahedi/goent) - 熵度量的 Go 实现。
- [gograph](https://github.com/hmdsefi/gograph) - Go 的泛型图库，提供数学图论理论与算法。
- [gonum](https://github.com/gonum/gonum) - Gonum is a set of numeric libraries for the Go programming language. It contains libraries for matrices, statistics, optimization, and more.
- [gonum/plot](https://github.com/gonum/plot) - gonum/plot provides an API for building and drawing plots in Go.
- [goraph](https://github.com/gyuho/goraph) - Pure Go graph theory library(data structure, algorithm visualization).
- [gosl](https://github.com/cpmech/gosl) - Go scientific library for linear algebra, FFT, geometry, NURBS, numerical methods, probabilities, optimisation, differential equations, and more.
- [GoStats](https://github.com/OGFris/GoStats) - GoStats is an Open Source GoLang library for math statistics mostly used in Machine Learning domains, it covers most of the Statistical measures functions.
- [graph](https://github.com/yourbasic/graph) - Library of basic graph algorithms.
- [hdf5](https://github.com/scigolib/hdf5) - Pure Go implementation of the HDF5 file format for scientific data storage and exchange.
- [insyra](https://github.com/HazelnutParadise/insyra) - Data analysis library with statistics, visualization, Parquet support, and Python integration.
- [jsonl-graph](https://github.com/nikolaydubina/jsonl-graph) - Tool to manipulate JSONL graphs with graphviz support.
- [matlab](https://github.com/scigolib/matlab) - Pure Go library for reading and writing MATLAB .mat files (v5-v7.3) without CGO.
- [MatProInterface.go](https://github.com/MatProGo-dev/MatProInterface.go) - MatProInterface.go is an open source package for defining mathematical programs (e.g., convex optimization problems) in Go.
- [matrix](https://github.com/Arceus-7/matrix) - A clean, generic, zero-dependency matrix math package for Go with support for arithmetic, decompositions, and linear system solving.
- [ode](https://github.com/ChristopherRabotin/ode) - Ordinary differential equation (ODE) solver which supports extended states and channel-based iteration stop conditions.
- [orb](https://github.com/paulmach/orb) - 2D geometry types with clipping, GeoJSON and Mapbox Vector Tile support.
- [pagerank](https://github.com/alixaxel/pagerank) - Weighted PageRank algorithm implemented in Go.
- [piecewiselinear](https://github.com/sgreben/piecewiselinear) - Tiny linear interpolation library.
- [PiHex](https://github.com/claygod/PiHex) - Implementation of the "Bailey-Borwein-Plouffe" algorithm for the hexadecimal number Pi.
- [Poly](https://github.com/bebop/poly) - A Go package for engineering organisms.
- [rootfinding](https://github.com/khezen/rootfinding) - root-finding algorithms library for finding roots of quadratic functions.
- [simd](https://github.com/tphakala/simd) - Native Go vector and SIMD operations on slices with multi-architecture assembly acceleration.
- [sparse](https://github.com/james-bowman/sparse) - Go Sparse matrix formats for linear algebra supporting scientific and machine learning applications, compatible with gonum matrix libraries.
- [stats](https://github.com/montanaflynn/stats) - Statistics package with common functions missing from the Golang standard library.
- [streamtools](https://github.com/nytlabs/streamtools) - general purpose, graphical tool for dealing with streams of data.
- [taxonkit](https://github.com/shenwei356/taxonkit) - A practical and efficient NCBI taxonomy toolkit; supports querying lineage, reformatting, filtering, and creating custom taxdump files.
- [TextRank](https://github.com/DavidBelicza/TextRank) - TextRank implementation in Golang with extendable features (summarization, weighting, phrase extraction) and multithreading (goroutine) support.
- [topk](https://github.com/keilerkonzept/topk) - Sliding-window and regular top-K sketches, based on the HeavyKeeper algorithm.
- [triangolatte](https://github.com/tchayen/triangolatte) - 2D triangulation library. Allows translating lines and polygons (both based on points) to the language of GPUs.

**[⬆ 回到顶部](#contents)**

<a id="security"></a>
## 安全

_用于提升应用安全性的库。_

- [acmetool](https://github.com/hlandau/acme) - ACME (Let's Encrypt) client tool with automatic renewal.
- [acme-proxy](https://github.com/esnet/acme-proxy) - Solve ACME http-01 challenge without opening port 80 to the internet, obtain certs from an external certificate authority.
- [acopw-go](https://sr.ht/~jamesponddotco/acopw-go/) - Small cryptographically secure password generator package for Go.
- [acra](https://github.com/cossacklabs/acra) - Network encryption proxy to protect database-based applications from data leaks: strong selective encryption, SQL injections prevention, intrusion detection system.
- [aes-ctr-drbg](https://github.com/sixafter/aes-ctr-drbg) - A Deterministic Random Bit Generator based on AES in Counter mode (AES-CTR-DRBG) as specified in NIST SP 800-90A.
- [age](https://github.com/FiloSottile/age) - A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability.
- [argon2-hashing](https://github.com/andskur/argon2-hashing) - light wrapper around Go's argon2 package that closely mirrors with Go's standard library Bcrypt and simple-scrypt package.
- [autocert](https://pkg.go.dev/golang.org/x/crypto/acme/autocert) - Auto provision Let's Encrypt certificates and start a TLS server.
- [BadActor](https://github.com/jaredfolkins/badactor) - In-memory, application-driven jailer built in the spirit of fail2ban.
- [beelzebub](https://github.com/mariocandela/beelzebub) - A secure low code honeypot framework, leveraging AI for System Virtualization.
- [booster](https://github.com/anatol/booster) - Fast initramfs generator with full-disk encryption support.
- [caddy-waf](https://github.com/fabriziosalmi/caddy-waf) - Web Application Firewall middleware for the Caddy server, with a regex rule engine, anomaly scoring, IP/DNS/ASN/country blacklists and rate limiting.
- [Cameradar](https://github.com/Ullaakut/cameradar) - Tool and library to remotely hack RTSP streams from surveillance cameras.
- [canery](https://github.com/rluders/canery) - Minimal, stateless authorization engine with a pluggable evaluation model.
- [certificates](https://github.com/mvmaasakkers/certificates) - An opinionated tool for generating tls certificates.
- [CertMagic](https://github.com/caddyserver/certmagic) - Mature, robust, and powerful ACME client integration for fully-managed TLS certificate issuance and renewal.
- [Coraza](https://github.com/corazawaf/coraza) - Enterprise-ready, modsecurity and OWASP CRS compatible WAF library.
- [coraza-rule-validator](https://github.com/stardothosting/coraza-rule-validator) - Standalone CLI tool to validate ModSecurity and Coraza SecLang WAF rules before production deployment.
- [Crenox](https://github.com/crenoxhq/crenox) - Zero-dependency pre-commit secret scanner using Aho-Corasick for high-performance credentials leak detection.
- [deidentify](https://github.com/aliengiraffe/deidentify) - Deterministic, format-preserving removal of personally identifiable information from text and structured data.
- [dongle](https://github.com/golang-module/dongle) - A simple, semantic and developer-friendly golang package for encoding&decoding and encryption&decryption.
- [dotlock](https://github.com/ahmadraza100/dotlock) - Encrypted .env vault manager with interactive TUI for managing secrets across multiple environments and profiles.
- [encid](https://github.com/bobg/encid) - Encode and decode encrypted integer IDs.
- [entpassgen](https://github.com/andreimerlescu/entpassgen) - Entropy Password Generator with extensive command line arguments to generate random strings securely including digits, passwords, and passwords built using obscure dictionary words mixed with symbols and digits.
- [firewalld-rest](https://github.com/prashantgupta24/firewalld-rest) - A rest application to dynamically update firewalld rules on a linux server.
- [fort](https://github.com/djadmin/fort) - Audits macOS security settings across 16 checks, reports a score, and fixes issues where it safely can. Single binary, installable via Homebrew.
- [go-generate-password](https://github.com/m1/go-generate-password) - Password generator that can be used on the cli or as a library.
- [go-htpasswd](https://github.com/tg123/go-htpasswd) - Apache htpasswd Parser for Go.
- [go-password-validator](https://github.com/lane-c-wagner/go-password-validator) - Password validator based on raw cryptographic entropy values.
- [go-peer](https://github.com/number571/go-peer) - A software library for creating secure and anonymous decentralized systems.
- [go-yara](https://github.com/hillu/go-yara) - Go Bindings for [YARA](https://github.com/plusvic/yara), the "pattern matching swiss knife for malware researchers (and everyone else)".
- [goArgonPass](https://github.com/dwin/goArgonPass) - Argon2 password hash and verification designed to be compatible with existing Python and PHP implementations.
- [goSecretBoxPassword](https://github.com/dwin/goSecretBoxPassword) - A probably paranoid package for securely hashing and encrypting passwords.
- [gost-crypto](https://github.com/rekurt/gost-crypto) - Go library for Russian GOST cryptographic standards (digital signatures, Streebog hash, Kuznechik cipher, MGM AEAD) backed by OpenSSL gost-engine.
- [grim](https://github.com/ijin82/grim) - Fast and secure CLI tool for managing encrypted Markdown note vaults in volatile memory.
- [gspy](https://github.com/Mutasem-mk4/gspy) - Forensic goroutine-to-syscall inspector for live Go processes.
- [Interpol](https://github.com/avahidi/interpol) - Rule-based data generator for fuzzing and penetration testing.
- [leakhound](https://github.com/nilpoona/leakhound) - Static analysis tool to detect accidental logging of sensitive struct fields, preventing data leaks in logs.
- [lego](https://github.com/go-acme/lego) - Pure Go ACME client library and CLI tool (for use with Let's Encrypt).
- [luks.go](https://github.com/anatol/luks.go) - Pure Golang library to manage LUKS partitions.
- [mcprobe](https://github.com/tamish560/mcprobe) - Security scanner for MCP servers with prompt injection detection, tool shadowing, and SARIF output.
- [memguard](https://github.com/awnumar/memguard) - A pure Go library for handling sensitive values in memory.
- [mist](https://github.com/iSerganov/mist) - Asymmetric-key audio steganography library that hides encrypted messages inside compressed audio using X25519 and ChaCha20-Poly1305.
- [multikey](https://github.com/adrianosela/multikey) - An n-out-of-N keys encryption/decryption framework based on Shamir's Secret Sharing algorithm.
- [nacl](https://github.com/kevinburke/nacl) - Go implementation of the NaCL set of API's.
- [optimus-go](https://github.com/pjebs/optimus-go) - ID hashing and Obfuscation using Knuth's Algorithm.
- [passlib](https://github.com/hlandau/passlib) - Futureproof password hashing library.
- [passwap](https://github.com/zitadel/passwap) - Provides a unified implementation between different password hashing algorithms
- [pii-shield](https://github.com/pii-shield/pii-shield) - Zero-code log sanitization sidecar for Kubernetes that redacts PII from logs.
- [pm](https://github.com/nicola-strappazzon/password-manager) - Unix-style password manager written in Go to save your data with OpenPGP encryption.
- [procscope](https://github.com/Mutasem-mk4/procscope) - Process-scoped runtime investigator using eBPF to trace process lifecycle, file activity, and network connections.
- [qrand](https://github.com/bitfield/qrand) - Client for the ANU Quantum Numbers (AQN) API, providing quantum-mechanically secure random data.
- [Razify](https://github.com/Hossiy21/razify) - CLI to scan, validate and audit .env files for leaked secrets and environment drift.
- [redact](https://github.com/alesr/redact) - Redact sensitive information from slog-based logs using a configurable pipeline.
- [SafeDep/vet](https://github.com/safedep/vet) - Protect against malicious open source packages.
- [secret](https://github.com/rsjethani/secret) - Prevent your secrets from leaking into logs, std\* etc.
- [secretgenerator](https://github.com/rafaelperoco/secretgenerator) - CSPRNG-backed credential generator with a versioned JSON schema for passwords, passphrases, secrets, API keys, and PINs.
- [secure](https://github.com/unrolled/secure) - HTTP middleware for Go that facilitates some quick security wins.
- [secureio](https://github.com/xaionaro-go/secureio) - An keyexchanging+authenticating+encrypting wrapper and multiplexer for `io.ReadWriteCloser` based on XChaCha20-poly1305, ECDH and ED25519.
- [simple-scrypt](https://github.com/elithrar/simple-scrypt) - Scrypt package with a simple, obvious API and automatic cost calibration built-in.
- [ssh-vault](https://github.com/ssh-vault/ssh-vault) - encrypt/decrypt using ssh keys.
- [sslmgr](https://github.com/adrianosela/sslmgr) - SSL certificates made easy with a high level wrapper around acme/autocert.
- [teler-waf](https://github.com/kitabisa/teler-waf) - teler-waf is a Go HTTP middleware that provide teler IDS functionality to protect against web-based attacks and improve the security of Go-based web applications. It is highly configurable and easy to integrate into existing Go applications.
- [themis](https://github.com/cossacklabs/themis) - high-level cryptographic library for solving typical data security tasks (secure data storage, secure messaging, zero-knowledge proof authentication), available for 14 languages, best fit for multi-platform apps.
- [urusai](https://github.com/calpa/urusai) - Urusai ("noisy" in Japanese) is a Go implementation of a random HTTP/DNS traffic noise generator that helps protect privacy by creating digital smokescreens while browsing.
- [veil](https://github.com/getveil/veil) - Local HTTPS proxy that hides API credentials from AI coding agents. OS keychain integration, format-aware placeholders, SQLite audit log.
- [y509](https://github.com/kanywst/y509) - TUI for X.509 certificate chains that reports whether a chain verifies and, separately, whether a server served it correctly.


**[⬆ 回到顶部](#contents)**

<a id="serialization"></a>
## 序列化

_用于二进制序列化的库与工具。_

- [bambam](https://github.com/glycerine/bambam) - generator for Cap'n Proto schemas from go.
- [bel](https://github.com/32leaves/bel) - Generate TypeScript interfaces from Go structs/interfaces. Useful for JSON RPC.
- [binstruct](https://github.com/ghostiam/binstruct) - Golang binary decoder for mapping data into the structure.
- [cbor](https://github.com/fxamacker/cbor) - Small, safe, and easy CBOR encoding and decoding library.
- [colfer](https://github.com/pascaldekloe/colfer) - Code generation for the Colfer binary format.
- [csvutil](https://github.com/jszwec/csvutil) - High Performance, idiomatic CSV record encoding and decoding to native Go structures.
- [elastic](https://github.com/epiclabs-io/elastic) - Convert slices, maps or any other unknown value across different types at run-time, no matter what.
- [fixedwidth](https://github.com/huydang284/fixedwidth) - Fixed-width text formatting (UTF-8 supported).
- [fwencoder](https://github.com/o1egl/fwencoder) - Fixed width file parser (encoding and decoding library) for Go.
- [go-capnproto](https://github.com/glycerine/go-capnproto) - Cap'n Proto library and parser for go.
- [go-codec](https://github.com/ugorji/go) - High Performance, feature-Rich, idiomatic encode, decode and rpc library for msgpack, cbor and json, with runtime-based OR code-generation support.
- [go-csvlib](https://github.com/tiendc/go-csvlib) - High level and rich functionalities CSV serialization/deserialization library.
- [goprotobuf](https://github.com/golang/protobuf) - Go support, in the form of a library and protocol compiler plugin, for Google's protocol buffers.
- [gotiny](https://github.com/raszia/gotiny) - Efficient Go serialization library, gotiny is almost as fast as serialization libraries that generate code.
- [jsoniter](https://github.com/json-iterator/go) - High-performance 100% compatible drop-in replacement of "encoding/json".
- [mus-go](https://github.com/mus-format/mus-go) - MUS format serializer for Go.
- [php_session_decoder](https://github.com/yvasiyarov/php_session_decoder) - GoLang library for working with PHP session format and PHP Serialize/Unserialize functions.
- [pletter](https://github.com/vimeda/pletter) - A standard way to wrap a proto message for message brokers.
- [proto](https://github.com/emicklei/proto) - Parser and writer for Google ProtocolBuffers .proto files.
- [structomap](https://github.com/tuvistavie/structomap) - Library to easily and dynamically generate maps from static structures.
- [unitpacking](https://github.com/recolude/unitpacking) - Library to pack unit vectors into as fewest bytes as possible.

**[⬆ 回到顶部](#contents)**

<a id="server-applications"></a>
## 服务器应用

- [algernon](https://github.com/xyproto/algernon) - HTTP/2 web server with built-in support for Lua, Markdown, GCSS and Amber.
- [Caddy](https://github.com/caddyserver/caddy) - Caddy is an alternative, HTTP/2 web server that's easy to configure and use.
- [Casdoor](https://github.com/casdoor/casdoor) - Identity and access management (IAM) and single sign-on (SSO) server with a web UI, supporting OAuth 2.0, OIDC, SAML, CAS and LDAP.
- [consul](https://www.consul.io/) - Consul is a tool for service discovery, monitoring and configuration.
- [cortex-tenant](https://github.com/blind-oracle/cortex-tenant) - Prometheus remote write proxy that adds add Cortex tenant ID header based on metric labels.
- [devd](https://github.com/cortesi/devd) - Local webserver for developers.
- [discovery](https://github.com/Bilibili/discovery) - A registry for resilient mid-tier load balancing and failover.
- [dudeldu](https://github.com/krotik/dudeldu) - A simple SHOUTcast server.
- [Easegress](https://github.com/megaease/easegress) - A cloud native high availability/performance traffic orchestration system with observability and extensibility.
- [Engity's Bifröst](https://bifroest.engity.org/) - Highly customizable SSH server with several ways to authorize a user how to execute its session (local or in containers).
- [etcd](https://github.com/etcd-io/etcd) - Highly-available key value store for shared configuration and service discovery.
- [Euterpe](https://github.com/ironsmile/euterpe) - Self-hosted music streaming server with built-in web UI and REST API.
- [Fider](https://github.com/getfider/fider) - Fider is an open platform to collect and organize customer feedback.
- [Flagr](https://github.com/checkr/flagr) - Flagr is an open-source feature flagging and A/B testing service.
- [flipt](https://github.com/markphelps/flipt) - A self contained feature flag solution written in Go and Vue.js
- [flue](https://github.com/karnstack/flue) - Self-hosted daemon that serves terminal sessions to a browser tab. Sessions keep running after the tab is closed.
- [go-feature-flag](https://github.com/thomaspoignant/go-feature-flag) - A simple, complete and lightweight self-hosted feature flag solution 100% Open Source.
- [go-proxy-cache](https://github.com/fabiocicerchia/go-proxy-cache) - Simple Reverse Proxy with Caching, written in Go, using Redis.
- [gondola](https://github.com/bmf-san/gondola) - A YAML based golang reverse proxy.
- [goshs](https://github.com/patrickhener/goshs) - SimpleHTTPServer replacement with file upload/download, WebDAV, SFTP, SMB, TLS, authentication, and share links.
- [Kono](https://github.com/starwalkn/kono) - lightweight extendable API Gateway in Go - parallel fan-out, flexible aggregation, and zero configuration magic.
- [lets-proxy2](https://github.com/rekby/lets-proxy2) - Reverse proxy for handle https with issue certificates in fly from lets-encrypt.
- [minio](https://github.com/pgsty/minio) - Community Maintained Fork of minio (Object Storage Service).
- [Moxy](https://github.com/sinhashubham95/moxy) - Moxy is a simple mocker and proxy application server, you can create mock endpoints as well as proxy requests in case no mock exists for the endpoint.
- [nginx-prometheus](https://github.com/blind-oracle/nginx-prometheus) - Nginx log parser and exporter to Prometheus.
- [nsq](https://nsq.io/) - A realtime distributed messaging platform.
- [OpenRun](https://github.com/openrundev/openrun) - Open-source alternative to Google Cloud Run and AWS App Runner. Easily deploy internal tools across a team.
- [pocketbase](https://github.com/pocketbase/pocketbase) - PocketBase is a realtime backend in 1 file consisting of embedded database (SQLite) with realtime subscriptions, built-in auth management and much more.
- [protoxy](https://github.com/camgraff/protoxy) - A proxy server that converts JSON request bodies to Protocol Buffers.
- [psql-streamer](https://github.com/blind-oracle/psql-streamer) - Stream database events from PostgreSQL to Kafka.
- [relay](https://github.com/valtors/relay) - MCP server with 40+ tools for AI agents. File operations, web search, screenshots, multi-agent coordination. Single Go binary.
- [riemann-relay](https://github.com/blind-oracle/riemann-relay) - Relay to load-balance Riemann events and/or convert them to Carbon.
- [RoadRunner](https://github.com/spiral/roadrunner) - High-performance PHP application server, load-balancer and process manager.
- [SFTPGo](https://github.com/drakkan/sftpgo) - Fully featured and highly configurable SFTP server with optional FTP/S and WebDAV support. It can serve local filesystem and Cloud Storage backends such as S3 and Google Cloud Storage.
- [simpleconf](https://github.com/shaunlee/simpleconf) - Configuration server holding one JSON document, read and written by key path over HTTP and TCP, with optional Raft clustering.
- [Trickster](https://github.com/tricksterproxy/trickster) - HTTP reverse proxy cache and time series accelerator.
- [wd-41](https://github.com/baalimago/wd-41) - A (w)eb (d)evelopment server with automatic live-reload on file changes.
- [whois](https://github.com/KincaidYang/whois) - Self-hosted WHOIS/RDAP query service and MCP server for domains, IPv4/IPv6 addresses, CIDRs and ASNs.
- [Wish](https://github.com/charmbracelet/wish) - Make SSH apps, just like that!

**[⬆ 回到顶部](#contents)**

<a id="stream-processing"></a>
## 流处理

_用于流处理与响应式编程的库与工具。_

- [go-etl](https://github.com/Breeze0806/go-etl) - A lightweight toolkit for data source extraction, transformation, and loading (ETL).
- [go-streams](https://github.com/reugn/go-streams) - Go stream processing library.
- [goio](https://github.com/primetalk/goio) - An implementation of IO, Stream, Fiber for Golang, inspired by awesome Scala libraries cats and fs2.
- [gostream](https://github.com/mariomac/gostream) - Type-safe stream processing library inspired by the Java Streams API.
- [machine](https://github.com/whitaker-io/machine) - Go library for writing and generating stream workers with built in metrics and traceability.
- [nibbler](https://github.com/naughtygopher/nibbler) - A lightweight package for micro batch processing.
- [ro](https://github.com/samber/ro) - Reactive Programming: declarative and composable API for event-driven applications.
- [signals](https://github.com/coregx/signals) - Type-safe reactive state management inspired by Angular Signals with computed values, effects, and dependency tracking.
- [stream](https://github.com/youthlin/stream) - Go Stream, like Java 8 Stream: Filter/Map/FlatMap/Peek/Sorted/ForEach/Reduce...
- [StreamSQL](https://github.com/rulego/streamsql) - A lightweight streaming SQL engine for real-time data processing.

**[⬆ 回到顶部](#contents)**

<a id="template-engines"></a>
## 模板引擎

_用于模板与词法分析的库与工具。_

- [bagme](https://github.com/boxesandglue/bagme) - HTML/CSS to PDF rendering with TeX-quality typesetting in pure Go.
- [ego](https://github.com/benbjohnson/ego) - Lightweight templating language that lets you write templates in Go. Templates are translated into Go and compiled.
- [fasttemplate](https://github.com/valyala/fasttemplate) - Simple and fast template engine. Substitutes template placeholders up to 10x faster than [text/template](https://golang.org/pkg/text/template/).
- [gomponents](https://www.gomponents.com) - HTML 5 components in pure Go, that look something like this: `func(name string) g.Node { return Div(Class("headline"), g.Textf("Hi %v!", name)) }`.
- [got](https://github.com/goradd/got) - A Go code generator inspired by Hero and Fasttemplate. Has include files, custom tag definitions, injected Go code, language translation, and more.
- [goview](https://github.com/foolin/goview) - Goview is a lightweight, minimalist and idiomatic template library based on golang html/template for building Go web application.
- [gox](https://github.com/doors-dev/gox) - HTML templates as first-class Go expressions, with seamless editor support.
- [htmgo](https://htmgo.dev) - build simple and scalable systems with go + htmx
- [jet](https://github.com/CloudyKit/jet) - Jet template engine.
- [liquid](https://github.com/osteele/liquid) - Go implementation of Shopify Liquid templates.
- [maroto](https://github.com/johnfercher/maroto) - A maroto way to create PDFs. Maroto is inspired in Bootstrap and uses gofpdf. Fast and simple.
- [pongo2](https://github.com/flosch/pongo2) - Django-like template-engine for Go.
- [quicktemplate](https://github.com/valyala/quicktemplate) - Fast, powerful, yet easy to use template engine. Converts templates into Go code and then compiles it.
- [Razor](https://github.com/sipin/gorazor) - Razor view engine for Golang.
- [Soy](https://github.com/robfig/soy) - Closure templates (aka Soy templates) for Go, following the [official spec](https://developers.google.com/closure/templates/).
- [sprout](https://github.com/go-sprout/sprout) - Useful template functions for Go templates.
- [tbd](https://github.com/lucasepe/tbd) - A really simple way to create text templates with placeholders - exposes extra builtin Git repo metadata.
- [templ](https://github.com/a-h/templ) - A HTML templating language that has great developer tooling.
- [templator](https://github.com/alesr/templator) - A type-safe HTML template rendering engine for Go.

**[⬆ 回到顶部](#contents)**

<a id="testing"></a>
## 测试

_用于测试代码库与生成测试数据的库。_

<a id="testing-frameworks"></a>
### 测试框架

- [apitest](https://apitest.dev) - Simple and extensible behavioural testing library for REST based services or HTTP handlers that supports mocking external http calls and rendering of sequence diagrams.
- [arch-go](https://github.com/arch-go/arch-go) - Architecture testing tool for Go projects.
- [assay](https://github.com/tushariitr-19/assay) - Framework-agnostic evaluation library for testing Go agents and MCP servers with deterministic checks, CI-ready exit codes, and zero-code YAML-based testing.
- [assert](https://github.com/go-playground/assert) - Basic Assertion Library used along side native go testing, with building blocks for custom assertions.
- [baloo](https://github.com/h2non/baloo) - Expressive and versatile end-to-end HTTP API testing made easy.
- [be](https://github.com/carlmjohnson/be) - The minimalist generic test assertion library.
- [biff](https://github.com/fulldump/biff) - Bifurcation testing framework, BDD compatible.
- [charlatan](https://github.com/percolate/charlatan) - Tool to generate fake interface implementations for tests.
- [commander](https://github.com/SimonBaeumer/commander) - Tool for testing cli applications on windows, linux and osx.
- [coverage](https://github.com/jbunds/coverage) - 用于展示 Go 测试覆盖率的简易 Web UI，以及可复用的 [go-test-coverage-html-report](https://github.com/marketplace/actions/go-test-coverage-html-report) GitHub Action。
- [cupaloy](https://github.com/bradleyjkemp/cupaloy) - Simple snapshot testing addon for your test framework.
- [dbcleaner](https://github.com/khaiql/dbcleaner) - Clean database for testing purpose, inspired by `database_cleaner` in Ruby.
- [dft](https://github.com/abecodes/dft) - Lightweight, zero dependency docker containers for testing (or more).
- [dsunit](https://github.com/viant/dsunit) - Datastore testing for SQL, NoSQL, structured files.
- [embedded-postgres](https://github.com/fergusstrange/embedded-postgres) - Run a real Postgres database locally on Linux, OSX or Windows as part of another Go application or test.
- [endly](https://github.com/viant/endly) - Declarative end to end functional testing.
- [envite](https://github.com/PerimeterX/envite) - Dev and testing environment management framework.
- [fixenv](https://github.com/rekby/fixenv) - Fixture manage engine, inspired by pytest fixtures.
- [flute](https://github.com/suzuki-shunsuke/flute) - HTTP client testing framework.
- [frisby](https://github.com/verdverm/frisby) - REST API testing framework.
- [gherkingen](https://github.com/hedhyw/gherkingen) - BDD boilerplate generator and framework.
- [ginkgo](https://onsi.github.io/ginkgo/) - BDD Testing Framework for Go.
- [gnomock](https://github.com/orlangure/gnomock) - integration testing with real dependencies (database, cache, even Kubernetes or AWS) running in Docker, without mocks.
- [go-carpet](https://github.com/msoap/go-carpet) - Tool for viewing test coverage in terminal.
- [go-cmp](https://github.com/google/go-cmp) - Package for comparing Go values in tests.
- [go-hit](https://github.com/Eun/go-hit) - Hit is an http integration test framework written in golang.
- [go-httpbin](https://github.com/mccutchen/go-httpbin) - HTTP testing and debugging tool with various endpoints for client testing.
- [go-mutesting](https://github.com/jonbaldie/go-mutesting) - Mutation testing for Go with CI quality gates, coverage-aware MSI, baseline tracking, and git-diff filtering.
- [go-mysql-test-container](https://github.com/arikama/go-mysql-test-container) - Golang MySQL testcontainer to help with MySQL integration testing.
- [go-snaps](http://github.com/gkampitakis/go-snaps) - Jest-like snapshot testing in Golang.
- [go-test-coverage](https://github.com/vladopajic/go-test-coverage) - Tool that reports coverage of files below set threshold.
- [go-testdeep](https://github.com/maxatome/go-testdeep) - Extremely flexible golang deep comparison, extends the go testing package.
- [go-testing](https://github.com/tkrop/go-testing) - Go testing extension, that allows a simple setup of strongly isolated unit, component, and integration test providing advanced mock support extending gomock and gock.
- [go-testpredicate](https://github.com/maargenton/go-testpredicate) - Test predicate style assertions library with extensive diagnostics output.
- [go-vcr](https://github.com/dnaeon/go-vcr) - Record and replay your HTTP interactions for fast, deterministic and accurate tests.
- [goblin](https://github.com/franela/goblin) - Mocha like testing framework of Go.
- [goc](https://github.com/qiniu/goc) - Goc is a comprehensive coverage testing system for The Go Programming Language.
- [gocheck](https://labix.org/gocheck) - More advanced testing framework alternative to gotest.
- [GoConvey](https://github.com/smartystreets/goconvey/) - BDD-style framework with web UI and live reload.
- [gocrest](https://github.com/corbym/gocrest) - Composable hamcrest-like matchers for Go assertions.
- [godog](https://github.com/cucumber/godog) - Cucumber BDD framework for Go.
- [gofight](https://github.com/appleboy/gofight) - API Handler Testing for Golang Router framework.
- [gogiven](https://github.com/corbym/gogiven) - YATSPEC-like BDD testing framework for Go.
- [gomatch](https://github.com/jfilipczyk/gomatch) - library created for testing JSON against patterns.
- [gomega](https://onsi.github.io/gomega/) - Rspec like matcher/assertion library.
- [gospecify](https://github.com/stesla/gospecify) - This provides a BDD syntax for testing your Go code. It should be familiar to anybody who has used libraries such as rspec.
- [gosuite](https://github.com/pavlo/gosuite) - Brings lightweight test suites with setup/teardown facilities to `testing` by leveraging Go1.7's Subtests.
- [got](https://github.com/ysmood/got) - An enjoyable golang test framework.
- [gotest.tools](https://github.com/gotestyourself/gotest.tools) - A collection of packages to augment the go testing package and support common patterns.
- [Hamcrest](https://github.com/rdrdr/hamcrest) - fluent framework for declarative Matcher objects that, when applied to input values, produce self-describing results.
- [httper](https://github.com/gustofarbi/httper) - CLI runner for JetBrains .http files with scripting, assertions, gRPC, and load testing.
- [httpexpect](https://github.com/gavv/httpexpect) - Concise, declarative, and easy to use end-to-end HTTP and REST API testing.
- [is](https://github.com/matryer/is) - Professional lightweight testing mini-framework for Go.
- [jsonassert](https://github.com/kinbiko/jsonassert) - Package for verifying that your JSON payloads are serialized correctly.
- [keploy](https://github.com/keploy/keploy) - Generate Testcase and Data Mocks from API calls automatically.
- [omg.testingtools](https://github.com/dedalqq/omg.testingtools) - The simple library for change a values of private fields for testing.
- [restit](https://github.com/yookoala/restit) - Go micro framework to help writing RESTful API integration test.
- [schema](https://github.com/jgroeneveld/schema) - Quick and easy expression matching for JSON schemas used in requests and responses.
- [should](https://github.com/Kairum-Labs/should) - Testing library with zero dependencies, detailed struct diffs and human-readable error messages.
- [stop-and-go](https://github.com/elgohr/stop-and-go) - Testing helper for concurrency.
- [testcase](https://github.com/adamluzsi/testcase) - Idiomatic testing framework for Behavior Driven Development.
- [testcerts](https://github.com/madflojo/testcerts) - Dynamically generate self-signed certificates and certificate authorities within your test functions.
- [testcontainers-go](https://github.com/testcontainers/testcontainers-go) - A Go package that makes it simple to create and clean up container-based dependencies for automated integration/smoke tests. The clean, easy-to-use API enables developers to programmatically define containers that should be run as part of a test and clean up those resources when the test is done.
- [testfixtures](https://github.com/go-testfixtures/testfixtures) - A helper for Rails' like test fixtures to test database applications.
- [Testify](https://github.com/stretchr/testify) - Sacred extension to the standard go testing package.
- [Testo](https://github.com/ozontech/testo) - Plugin-based testing framework with suites, parallel tests, hooks and parametrization. Inspired by Pytest.
- [testsql](https://github.com/zhulongcheng/testsql) - Generate test data from SQL files before testing and clear it after finished.
- [testza](https://github.com/MarvinJWendt/testza) - Full-featured test framework with nice colorized output.
- [tparse](https://github.com/mfridman/tparse) - CLI tool for summarizing go test output. Pipe friendly. Compatible with go test flags.
- [trial](https://github.com/jgroeneveld/trial) - Quick and easy extendable assertions without introducing much boilerplate.
- [Tt](https://github.com/vcaesar/tt) - Simple and colorful test tools.
- [wstest](https://github.com/posener/wstest) - Websocket client for unit-testing a websocket http.Handler.

<a id="mock"></a>
### Mock

- [counterfeiter](https://github.com/maxbrunsfeld/counterfeiter) - Tool for generating self-contained mock objects.
- [fabricator](https://github.com/Goldziher/fabricator) - Type-safe factories for generating mock and fake data in Go, inspired by factory_boy and interface-forge.
- [genmock](https://gitlab.com/so_literate/genmock) - Go mocking system with code generator for building calls of the interface methods.
- [go-localstack](https://github.com/elgohr/go-localstack) - Tool for using localstack in AWS testing.
- [go-sqlmock](https://github.com/DATA-DOG/go-sqlmock) - Mock SQL driver for testing database interactions.
- [go-txdb](https://github.com/DATA-DOG/go-txdb) - Single transaction based database driver mainly for testing purposes.
- [gomock](https://github.com/uber-go/mock) - Mocking framework for the Go programming language.
- [gomock](https://github.com/vibridi/gomock) - CLI tool to generate typed and framework-agnostic interface mocks, with support for generics.
- [govcr](https://github.com/seborama/govcr) - HTTP mock for Golang: record and replay HTTP interactions for offline testing.
- [hoverfly](https://github.com/SpectoLabs/hoverfly) - HTTP(S) proxy for recording and simulating REST/SOAP APIs with extensible middleware and easy-to-use CLI.
- [httpmock](https://github.com/jarcoal/httpmock) - Easy mocking of HTTP responses from external resources.
- [minimock](https://github.com/gojuno/minimock) - Mock generator for Go interfaces.
- [mockery](https://github.com/vektra/mockery) - Tool to generate Go interfaces.
- [mockfs](https://github.com/balinomad/go-mockfs) - Mock filesystem for Go testing with error injection and latency simulation, built on `testing/fstest.MapFS`.
- [mockhttp](https://github.com/tv42/mockhttp) - Mock object for Go http.ResponseWriter.
- [mooncake](https://github.com/GuilhermeCaruso/mooncake) - A simple way to generate mocks for multiple purposes.
- [moq](https://github.com/matryer/moq) - Utility that generates a struct from any interface. The struct can be used in test code as a mock of the interface.
- [moxie](https://lesiw.io/moxie) - Generate mock methods on embedded structs.
- [pgxmock](https://github.com/pashagolub/pgxmock) - A mock library implementing [pgx - PostgreSQL Driver and Toolkit](https://github.com/jackc/pgx/).
- [timex](https://github.com/cabify/timex) - A test-friendly replacement for the native `time` package.
- [wsmock](https://github.com/sing198/wsmock) - Expressive, zero-boilerplate WebSocket mock server for testing with fault injection and assertions.
- [xgo](https://github.com/xhd2015/xgo) - A general pureposed function mocking library.

<a id="fuzzing-and-delta-debuggingreducingshrinking"></a>
### 模糊测试与增量调试/缩减/收缩

- [go-fuzz](https://github.com/dvyukov/go-fuzz) - Randomized testing system.
- [Tavor](https://github.com/zimmski/tavor) - Generic fuzzing and delta-debugging framework.

<a id="selenium-and-browser-control-tools"></a>
### Selenium 与浏览器控制工具

- [bonk](https://github.com/joakimcarlsson/bonk) - Fast, stealth-first browser automation library using Chrome DevTools Protocol over WebSocket with no external dependencies.
- [cdp](https://github.com/mafredri/cdp) - Type-safe bindings for the Chrome Debugging Protocol that can be used with browsers or other debug targets that implement it.
- [chromedp](https://github.com/knq/chromedp) - a way to drive/test Chrome, Safari, Edge, Android Webviews, and other browsers supporting the Chrome Debugging Protocol.
- [playwright-go](https://github.com/mxschmitt/playwright-go) - browser automation library to control Chromium, Firefox and WebKit with a single API.
- [rod](https://github.com/go-rod/rod) - A Devtools driver to make web automation and scraping easy.
- [selenosis](https://github.com/alcounit/selenosis) - Stateless Kubernetes-native hub that routes Selenium, Playwright, and MCP sessions to on-demand browser pods via custom resources.

<a id="fail-injection"></a>
### 故障注入

- [failpoint](https://github.com/pingcap/failpoint) - An implementation of [failpoints](https://www.freebsd.org/cgi/man.cgi?query=fail) for Golang.

**[⬆ 回到顶部](#contents)**

<a id="text-processing"></a>
## 文本处理

_用于解析与处理文本的库。_

另见[自然语言处理](#natural-language-processing)与[文本分析](#text-analysis)。

<a id="formatters"></a>
### 格式化工具

- [address](https://github.com/bojanz/address) - Handles address representation, validation and formatting.
- [align](https://github.com/Guitarbum722/align) - A general purpose application that aligns text.
- [bytes](https://github.com/labstack/gommon/tree/master/bytes) - Formats and parses numeric byte values (10K, 2M, 3G, etc.).
- [go-fixedwidth](https://github.com/ianlopshire/go-fixedwidth) - Fixed-width text formatting (encoder/decoder with reflection).
- [go-humanize](https://github.com/dustin/go-humanize) - Formatters for time, numbers, and memory size to human readable format.
- [gotabulate](https://github.com/bndr/gotabulate) - Easily pretty-print your tabular data with Go.
- [sq](https://github.com/neilotoole/sq) - Convert data from SQL databases or document formats like CSV or Excel into formats such as JSON, Excel, CSV, HTML, Markdown, XML, and YAML.
- [textwrap](https://github.com/isbm/textwrap) - Wraps text at end of lines. Implementation of `textwrap` module from Python.

<a id="markup-languages"></a>
### 标记语言

- [bafi](https://github.com/mmalcek/bafi) - Universal JSON, BSON, YAML, XML translator to ANY format using templates.
- [bbConvert](https://github.com/CalebQ42/bbConvert) - Converts bbCode to HTML that allows you to add support for custom bbCode tags.
- [blackfriday](https://github.com/russross/blackfriday) - Markdown processor in Go.
- [go-output-format](https://github.com/drewstinnett/go-output-format) - Output go structures into multiple formats (YAML/JSON/etc) in your command line app.
- [go-toml](https://github.com/pelletier/go-toml) - Go library for the TOML format with query support and handy cli tools.
- [goldmark](https://github.com/yuin/goldmark) - A Markdown parser written in Go. Easy to extend, standard (CommonMark) compliant, well structured.
- [goq](https://github.com/andrewstuart/goq) - Declarative unmarshalling of HTML using struct tags with jQuery syntax (uses GoQuery).
- [html-to-markdown](https://github.com/JohannesKaufmann/html-to-markdown) - Convert HTML to Markdown. Even works with entire websites and can be extended through rules.
- [htmlquery](https://github.com/antchfx/htmlquery) - An XPath query package for HTML, lets you extract data or evaluate from HTML documents by an XPath expression.
- [htmlyaml](https://github.com/nikolaydubina/htmlyaml) - Rich rendering of YAML as HTML in Go.
- [htree](https://github.com/bobg/htree) - Traverse, navigate, filter, and otherwise process trees of [html.Node](https://pkg.go.dev/golang.org/x/net/html#Node) objects.
- [markdown](https://github.com/nao1215/markdown) - Markdown builder that generates GitHub Flavored Markdown and mermaid diagrams through method chaining.
- [mdsmith](https://github.com/jeduden/mdsmith) - fast, auto-fixing Markdown linter and formatter. Checks style, readability, structure, and cross-file integrity.
- [mxj](https://github.com/clbanning/mxj) - Encode / decode XML as JSON or map[string]interface{}; extract values with dot-notation paths and wildcards. Replaces x2j and j2x packages.
- [picoloom](https://github.com/alnah/picoloom) - Markdown-to-PDF converter with CLI and Go library APIs.
- [toml](https://github.com/BurntSushi/toml) - TOML configuration format (encoder/decoder with reflection).

<a id="parsersencodersdecoders"></a>
### 解析器/编码器/解码器

- [allot](https://github.com/sbstjn/allot) - Placeholder and wildcard text parsing for CLI tools and bots.
- [codetree](https://github.com/aerogo/codetree) - Parses indented code (python, pixy, scarlet, etc.) and returns a tree structure.
- [commonregex](https://github.com/mingrammer/commonregex) - A collection of common regular expressions for Go.
- [did](https://github.com/ockam-network/did) - DID (Decentralized Identifiers) Parser and Stringer in Go.
- [doi](https://github.com/hscells/doi) - Document object identifier (doi) parser in Go.
- [editorconfig-core-go](https://github.com/editorconfig/editorconfig-core-go) - Editorconfig file parser and manipulator for Go.
- [go-fasttld](https://github.com/elliotwutingfeng/go-fasttld) - High performance effective top level domains (eTLD) extraction module.
- [go-nmea](https://github.com/adrianmo/go-nmea) - NMEA parser library for the Go language.
- [go-querystring](https://github.com/google/go-querystring) - Go library for encoding structs into URL query parameters.
- [go-vcard](https://github.com/emersion/go-vcard) - Parse and format vCard.
- [godump](https://github.com/yassinebenaid/godump) - Pretty print any GO variable with ease, an alternative to Go's `fmt.Printf("%#v")`.
- [godump (goforj)](https://github.com/goforj/godump) - Pretty-print Go structs with Laravel/Symfony-style dumps, full type info, colorized CLI output, cycle detection, and private field access.
- [gofeed](https://github.com/mmcdole/gofeed) - Parse RSS and Atom feeds in Go.
- [gographviz](https://github.com/awalterschulze/gographviz) - Parses the Graphviz DOT language.
- [gonameparts](https://github.com/polera/gonameparts) - Parses human names into individual name parts.
- [ltsv](https://github.com/Wing924/ltsv) - High performance [LTSV (Labeled Tab Separated Value)](http://ltsv.org/) reader for Go.
- [normalize](https://github.com/avito-tech/normalize) - Sanitize, normalize and compare fuzzy text.
- [parseargs-go](https://github.com/nproc/parseargs-go) - string argument parser that understands quotes and backslashes.
- [prattle](https://github.com/askeladdk/prattle) - Scan and parse LL(1) grammars simply and efficiently.
- [sh](https://github.com/mvdan/sh) - Shell parser and formatter.
- [tokenizer](https://github.com/bzick/tokenizer) - Parse any string, slice or infinite buffer to any tokens.
- [vdf](https://github.com/andygrunwald/vdf) - A Lexer and Parser for Valves Data Format (known as vdf) written in Go.
- [when](https://github.com/olebedev/when) - Natural EN and RU language date/time parser with pluggable rules.
- [xj2go](https://github.com/stackerzzq/xj2go) - Convert xml or json to go struct.

<a id="regular-expressions"></a>
### 正则表达式

- [coregex](https://github.com/coregx/coregex) - Production regex engine with Rust regex-crate architecture: multi-engine DFA/NFA, SIMD prefilters, drop-in stdlib replacement.
- [genex](https://github.com/alixaxel/genex) - Count and expand Regular Expressions into all matching Strings.
- [go-wildcard](https://github.com/IGLOU-EU/go-wildcard) - Simple and lightweight wildcard pattern matching.
- [goregen](https://github.com/zach-klippenstein/goregen) - Library for generating random strings from regular expressions.
- [regroup](https://github.com/oriser/regroup) - Match regex expression named groups into go struct using struct tags and automatic parsing.
- [rex](https://github.com/hedhyw/rex) - Regular expressions builder.

<a id="sanitation"></a>
### 数据清洗

- [bluemonday](https://github.com/microcosm-cc/bluemonday) - HTML Sanitizer.
- [gofuckyourself](https://github.com/JoshuaDoes/gofuckyourself) - A sanitization-based swear filter for Go.

<a id="scrapers"></a>
### 爬虫

- [colly](https://github.com/asciimoo/colly) - Fast and Elegant Scraping Framework for Gophers.
- [dataflowkit](https://github.com/slotix/dataflowkit) - Web scraping Framework to turn websites into structured data.
- [doc-scraper](https://github.com/Sriram-PR/doc-scraper) - Web crawler that converts documentation sites to clean Markdown and JSONL for LLM ingestion (RAG, training data).
- [go-recipe](https://github.com/kkyr/go-recipe) - A package for scraping recipes from websites.
- [go-sitemap-parser](https://github.com/aafeher/go-sitemap-parser) - Go language library for parsing Sitemaps.
- [GoQuery](https://github.com/PuerkitoBio/goquery) - GoQuery brings a syntax and a set of features similar to jQuery to the Go language.
- [pagser](https://github.com/foolin/pagser) - Pagser is a simple, extensible, configurable parse and deserialize html page to struct based on goquery and struct tags for golang crawler.
- [Tagify](https://github.com/zoomio/tagify) - Produces a set of tags from given source.
- [walker](https://github.com/cyucelen/walker) - Seamlessly fetch paginated data from any source. Simple and high performance API scraping included.
- [xurls](https://github.com/mvdan/xurls) - Extract urls from text.

<a id="rss"></a>
### RSS

- [podcast](https://github.com/eduncan911/podcast) - iTunes Compliant and RSS 2.0 Podcast Generator in Golang

<a id="utilitymiscellaneous"></a>
### 实用工具/杂项

- [ahocorasick](https://github.com/coregx/ahocorasick) - High-performance Aho-Corasick multi-pattern string matching with DFA compilation and SIMD prefilter, up to 7 GB/s throughput (part of [coregx](https://github.com/coregx) ecosystem).
- [go-runewidth](https://github.com/mattn/go-runewidth) - Functions to get fixed width of the character or string.
- [kace](https://github.com/codemodus/kace) - Common case conversions covering common initialisms.
- [lancet](https://github.com/duke-git/lancet) - A comprehensive, Lodash-like utility library for Go
- [petrovich](https://github.com/striker2000/petrovich) - Petrovich is the library which inflects Russian names to given grammatical case.
- [radix](https://github.com/yourbasic/radix) - Fast string sorting algorithm.
- [TySug](https://github.com/Dynom/TySug) - Alternative suggestions with respect to keyboard layouts.
- [uniwidth](https://github.com/unilibs/uniwidth) - High-performance Unicode character width calculation with SWAR optimization, O(1) lookup tables, and ZWJ emoji support.
- [w2vgrep](https://github.com/arunsupe/semantic-grep) - A semantic grep tool using word embeddings to find semantically similar matches. For example, searching for "death" will find "dead", "killing", "murder".

**[⬆ 回到顶部](#contents)**

<a id="third-party-apis"></a>
## 第三方 API

_用于访问第三方 API 的库。_

- [airtable](https://github.com/mehanizm/airtable) - Go client library for the [Airtable API](https://airtable.com/api).
- [anaconda](https://github.com/ChimeraCoder/anaconda) - Go client library for the Twitter 1.1 API.
- [appstore-sdk-go](https://github.com/Kachit/appstore-sdk-go) - Unofficial Golang SDK for AppStore Connect API.
- [aws-encryption-sdk-go](https://github.com/chainifynet/aws-encryption-sdk-go) - Unofficial Go SDK implementation of the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/index.html).
- [aws-sdk-go](https://github.com/aws/aws-sdk-go-v2) - The official AWS SDK for the Go programming language.
- [bqwriter](https://github.com/OTA-Insight/bqwriter) - High Level Go Library to write data into [Google BigQuery](https://cloud.google.com/bigquery) at a high throughout.
- [birdeye-go](https://github.com/tigusigalpa/birdeye-go) - Go client for Birdeye DeFi API with typed spot prices, OHLCV candles, historical data, and raw request escape hatch.
- [brewerydb](https://github.com/naegelejd/brewerydb) - Go library for accessing the BreweryDB API.
- [cachet](https://github.com/andygrunwald/cachet) - Go client library for [Cachet (open source status page system)](https://cachethq.io/).
- [circleci](https://github.com/jszwedko/go-circleci) - Go client library for interacting with CircleCI's API.
- [codeship-go](https://github.com/codeship/codeship-go) - Go client library for interacting with Codeship's API v2.
- [coinglass-go](https://github.com/tigusigalpa/coinglass-go) - Go client for Coinglass API v4 with zero dependencies, WebSocket streams, and typed endpoints for futures, spot, options, ETF, and indicators.
- [coinpaprika-go](https://github.com/coinpaprika/coinpaprika-api-go-client) - Go client library for interacting with Coinpaprika's API.
- [colony-sdk-go](https://github.com/TheColonyCC/colony-sdk-go) - Go client library for [The Colony](https://thecolony.cc) — a public social network whose users are AI agents.
- [device-check-go](https://github.com/rinchsan/device-check-go) - Go client library for interacting with [iOS DeviceCheck API](https://developer.apple.com/documentation/devicecheck) v1.
- [discordgo](https://github.com/bwmarrin/discordgo) - Go bindings for the Discord Chat API.
- [disgo](https://github.com/switchupcb/disgo) - Go API Wrapper for the Discord API.
- [dusupay-sdk-go](https://github.com/Kachit/dusupay-sdk-go) - Unofficial Dusupay payment gateway API Client for Go
- [ethrpc](https://github.com/onrik/ethrpc) - Go bindings for Ethereum JSON RPC API.
- [facebook](https://github.com/huandu/facebook) - Go Library that supports the Facebook Graph API.
- [fasapay-sdk-go](https://github.com/Kachit/fasapay-sdk-go) - Unofficial Fasapay payment gateway XML API Client for Golang.
- [fcm](https://github.com/maddevsio/fcm) - Go library for Firebase Cloud Messaging.
- [featureflip-go](https://github.com/canopy-labs/featureflip-go) - Go SDK for [Featureflip](https://featureflip.io/) feature flags, with local evaluation and streaming updates.
- [gads](https://github.com/emiddleton/gads) - Google Adwords Unofficial API.
- [gcm](https://github.com/Aorioli/gcm) - Go library for Google Cloud Messaging.
- [geo-golang](https://github.com/codingsince1985/geo-golang) - Go Library to access [Google Maps](https://developers.google.com/maps/documentation/geocoding/intro), [MapQuest](https://developer.mapquest.com/documentation/api/geocoding/), [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/), [OpenCage](https://opencagedata.com/api), [Bing](https://msdn.microsoft.com/en-us/library/ff701715.aspx), [Mapbox](https://www.mapbox.com/developers/api/geocoding/), and [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Nominatim) geocoding / reverse geocoding APIs.
- [github](https://github.com/google/go-github) - Go library for accessing the GitHub REST API v3.
- [githubql](https://github.com/shurcooL/githubql) - Go library for accessing the GitHub GraphQL API v4.
- [go-atlassian](https://github.com/ctreminiom/go-atlassian) - Go library for accessing the [Atlassian Cloud](https://www.atlassian.com/enterprise/cloud) services (Jira, Jira Service Management, Jira Agile, Confluence, Admin Cloud)
- [go-aws-news](https://github.com/circa10a/go-aws-news) - Go application and library to fetch what's new from AWS.
- [go-chronos](https://github.com/axelspringer/go-chronos) - Go library for interacting with the [Chronos](https://mesos.github.io/chronos/) Job Scheduler
- [go-gerrit](https://github.com/andygrunwald/go-gerrit) - Go client library for [Gerrit Code Review](https://www.gerritcodereview.com/).
- [go-hacknews](https://github.com/PaulRosset/go-hacknews) - Tiny Go client for HackerNews API.
- [go-here](https://github.com/abdullahselek/go-here) - Go client library around the HERE location based APIs.
- [go-hibp](https://github.com/wneessen/go-hibp) - Simple Go binding to the "Have I Been Pwned" APIs.
- [go-imgur](https://github.com/koffeinsource/go-imgur) - Go client library for [imgur](https://imgur.com)
- [go-jira](https://github.com/andygrunwald/go-jira) - Go client library for [Atlassian JIRA](https://www.atlassian.com/software/jira)
- [go-lark](https://github.com/go-lark/lark) - An easy-to-use unofficial SDK for [Feishu](https://open.feishu.cn/) and [Lark](https://open.larksuite.com/) Open Platform.
- [go-marathon](https://github.com/gambol99/go-marathon) - Go library for interacting with Mesosphere's Marathon PAAS.
- [go-myanimelist](https://github.com/nstratos/go-myanimelist) - Go client library for accessing the [MyAnimeList API](https://myanimelist.net/apiconfig/references/api/v2).
- [go-openai](https://github.com/sashabaranov/go-openai) - OpenAI ChatGPT, DALL·E, Whisper API library for Go.
- [go-openproject](https://github.com/manuelbcd/go-openproject) - Go client library for interacting with [OpenProject](https://docs.openproject.org/api/) API.
- [go-postman-collection](https://github.com/rbretecher/go-postman-collection) - Go module to work with [Postman Collections](https://learning.getpostman.com/docs/postman/collections/creating-collections/) (compatible with Insomnia).
- [go-redoc](https://github.com/mvrilo/go-redoc) - Embedded OpenAPI/Swagger documentation ui for Go using [ReDoc](https://redocly.com/).
- [go-restcountries](https://github.com/chriscross0/go-restcountries) - Go library for the [REST Countries API](https://countrylayer.com/).
- [go-salesforce](https://github.com/k-capehart/go-salesforce) - Go client library for interacting with the [Salesforce REST API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm).
- [go-sophos](https://github.com/esurdam/go-sophos) - Go client library for the [Sophos UTM REST API](https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en) with zero dependencies.
- [go-swagger-ui](https://github.com/esurdam/go-swagger-ui) - Go library containing precompiled [Swagger UI](https://swagger.io/tools/swagger-ui/) for serving swagger json.
- [go-telegraph](https://gitlab.com/toby3d/telegraph) - Telegraph publishing platform API client.
- [go-trending](https://github.com/andygrunwald/go-trending) - Go library for accessing [trending repositories](https://github.com/trending) and [developers](https://github.com/trending/developers) at Github.
- [go-unsplash](https://github.com/hbagdi/go-unsplash) - Go client library for the [Unsplash.com](https://unsplash.com) API.
- [go-xkcd](https://github.com/nishanths/go-xkcd) - Go client for the xkcd API.
- [go-yapla](https://gitlab.com/adrienK/go-yapla) - Go client library for the Yapla v2.0 API.
- [goagi](https://github.com/staskobzar/goagi) - Go library to build Asterisk PBX agi/fastagi applications.
- [goami2](https://github.com/staskobzar/goami2) - AMI v2 library for Asterisk PBX.
- [GoFreeDB](https://github.com/FreeLeh/GoFreeDB) - Golang library providing common and simple database abstractions on top of Google Sheets.
- [gogtrends](https://github.com/groovili/gogtrends) - Google Trends Unofficial API.
- [golang-tmdb](https://github.com/cyruzin/golang-tmdb) - Golang wrapper for The Movie Database API v3.
- [golyrics](https://github.com/mamal72/golyrics) - Golyrics is a Go library to fetch music lyrics data from the Wikia website.
- [gomalshare](https://github.com/MonaxGT/gomalshare) - Go library MalShare API [malshare.com](https://www.malshare.com/)
- [GoMusicBrainz](https://github.com/michiwend/gomusicbrainz) - Go MusicBrainz WS2 client library.
- [google](https://github.com/google/google-api-go-client) - Auto-generated Google APIs for Go.
- [google-analytics](https://github.com/chonthu/go-google-analytics) - Simple wrapper for easy google analytics reporting.
- [google-cloud](https://github.com/GoogleCloudPlatform/gcloud-golang) - Google Cloud APIs Go Client Library.
- [gopaapi5](https://github.com/utekaravinash/gopaapi5) - Go Client Library for [Amazon Product Advertising API 5.0](https://webservices.amazon.com/paapi5/documentation/).
- [gopensky](https://github.com/navidys/gopensky) - Go client implementation for [OpenSKY Network](https://opensky-network.org/) live's API (airspace ADS-B and Mode S data).
- [gosip](https://github.com/koltyakov/gosip) - Client library for SharePoint.
- [gostorm](https://github.com/jsgilmore/gostorm) - GoStorm is a Go library that implements the communications protocol required to write Storm spouts and Bolts in Go that communicate with the Storm shells.
- [hipchat](https://github.com/andybons/hipchat) - This project implements a golang client library for the Hipchat API.
- [hipchat (xmpp)](https://github.com/daneharrigan/hipchat) - A golang package to communicate with HipChat over XMPP.
- [httpsms-go](https://github.com/NdoleStudio/httpsms-go) - Go client for the httpSMS API.
- [igdb](https://github.com/Henry-Sarabia/igdb) - Go client for the [Internet Game Database API](https://api.igdb.com/).
- [ip2location-io-go](https://github.com/ip2location/ip2location-io-go) - Go wrapper for the IP2Location.io API [IP2Location.io](https://www.ip2location.io/).
- [jokeapi-go](https://github.com/icelain/jokeapi) - Go client for [JokeAPI](https://sv443.net/jokeapi/v2/).
- [lark](https://github.com/chyroc/lark) - [Feishu](https://open.feishu.cn/)/[Lark](https://open.larksuite.com/) Open API Go SDK, Support ALL Open API and Event Callback.
- [lastpass-go](https://github.com/ansd/lastpass-go) - Go client library for the [LastPass](https://www.lastpass.com/) API.
- [lemonsqueezy-go](https://github.com/NdoleStudio/lemonsqueezy-go) - Go client for the Lemon Squeezy API.
- [libgoffi](https://github.com/clevabit/libgoffi) - Library adapter toolbox for native [libffi](https://sourceware.org/libffi/) integration
- [libopenapi](https://github.com/pb33f/libopenapi) - Parse, validate, and work with OpenAPI, Swagger, Overlays, and Arazzo specifications.
- [manus-ai-go](https://github.com/tigusigalpa/manus-ai-go) - Go client for Manus AI API v2 with task automation, file management, webhooks, and type-safe models.
- [Medium](https://github.com/Medium/medium-sdk-go) - Golang SDK for Medium's OAuth2 API.
- [megos](https://github.com/andygrunwald/megos) - Client library for accessing an [Apache Mesos](https://mesos.apache.org/) cluster.
- [minio-go](https://github.com/minio/minio-go) - Minio Go Library for Amazon S3 compatible cloud storage.
- [mixpanel](https://github.com/dukex/mixpanel) - Mixpanel is a library for tracking events and sending Mixpanel profile updates to Mixpanel from your go applications.
- [nansen-go](https://github.com/tigusigalpa/nansen-go) - Go client for Nansen AI API with Smart Money analytics, token screener, profiler, and zero dependencies.
- [newsapi-go](https://github.com/jellydator/newsapi-go) - Go client for [NewsAPI](https://newsapi.org/).
- [openaigo](https://github.com/otiai10/openaigo) - OpenAI GPT3/GPT3.5 ChatGPT API client library for Go.
- [patreon-go](https://github.com/mxpv/patreon-go) - Go library for Patreon API.
- [paypal](https://github.com/logpacker/PayPal-Go-SDK) - Wrapper for PayPal payment API.
- [playlyfe](https://github.com/playlyfe/playlyfe-go-sdk) - The Playlyfe Rest API Go SDK.
- [pushover](https://github.com/gregdel/pushover) - Go wrapper for the Pushover API.
- [rawg-sdk-go](https://github.com/dimuska139/rawg-sdk-go) - Go library for the [RAWG Video Games Database](https://rawg.io/) API
- [shopify](https://github.com/rapito/go-shopify) - Go Library to make CRUD request to the Shopify API.
- [simples3](https://github.com/rhnvrm/simples3) - Simple no frills AWS S3 Library using REST with V4 Signing written in Go.
- [slack](https://github.com/slack-go/slack) - Slack API in Go.
- [smite](https://github.com/sergiotapia/smitego) - Go package to wraps access to the Smite game API.
- [sonarqube-client-go](https://github.com/BoxBoxJason/sonarqube-client-go) - Go client library and command-line client for the SonarQube Web API.
- [spec](https://github.com/oaswrap/spec) - Lightweight OpenAPI 3.x builder supporting static generation and popular frameworks like chi, echo, gin, fiber, mux and more.
- [spotify](https://github.com/rapito/go-spotify) - Go Library to access Spotify WEB API.
- [steam](https://github.com/sostronk/go-steam) - Go Library to interact with Steam game servers.
- [stripe](https://github.com/stripe/stripe-go) - Go client for the Stripe API.
- [swag](https://github.com/zc2638/swag) - No comments, simple go wrapper to create swagger 2.0 compatible APIs. Support most routing frameworks, such as built-in, gin, chi, mux, echo, httprouter, fasthttp and more.
- [textbelt](https://github.com/dietsche/textbelt) - Go client for the textbelt.com txt messaging API.
- [threads-go](https://github.com/tirthpatell/threads-go) - Go client library for the Meta Threads API with OAuth 2.0, rate limiting, and type-safe error handling.
- [Trello](https://github.com/adlio/trello) - Go wrapper for the Trello API.
- [TripAdvisor](https://github.com/mrbenosborne/tripadvisor-golang) - Go wrapper for the TripAdvisor API.
- [tumblr](https://github.com/mattcunningham/gumblr) - Go wrapper for the Tumblr v2 API.
- [uptimerobot](https://github.com/bitfield/uptimerobot) - Go wrapper and command-line client for the Uptime Robot v2 API.
- [vl-go](https://github.com/verifid/vl-go) - Go client library around the VerifID identity verification layer API.
- [webhooks](https://github.com/go-playground/webhooks) - Webhook receiver for GitHub and Bitbucket.
- [wit-go](https://github.com/wit-ai/wit-go) - Go client for wit.ai HTTP API.
- [ynab](https://github.com/brunomvsouza/ynab.go) - Go wrapper for the YNAB API.
- [zooz](https://github.com/gojuno/go-zooz) - Go client for the Zooz API.

**[⬆ 回到顶部](#contents)**

<a id="utilities"></a>
## 工具

_让开发更轻松的通用工具与库。_

- [abstract](https://github.com/maxbolgarin/abstract) - Abstractions and utilities to get rid of boilerplate code in business logic.
- [apm](https://github.com/topfreegames/apm) - Process manager for Golang applications with an HTTP API.
- [backscanner](https://github.com/icza/backscanner) - A scanner similar to bufio.Scanner, but it reads and returns lines in reverse order, starting at a given position and going backward.
- [bed](https://github.com/itchyny/bed) - A Vim-like binary editor written in Go.
- [blank](https://github.com/Henry-Sarabia/blank) - Verify or remove blanks and whitespace from strings.
- [bleep](https://github.com/sinhashubham95/bleep) - Perform any number of actions on any set of OS signals in Go.
- [boilr](https://github.com/tmrts/boilr) - Blazingly fast CLI tool for creating projects from boilerplate templates.
- [boring](https://github.com/alebeck/boring) - Simple command-line SSH tunnel manager.
- [changie](https://github.com/miniscruff/changie) - Automated changelog tool for preparing releases with lots of customization options.
- [chyle](https://github.com/antham/chyle) - Changelog generator using a git repository with multiple configuration possibilities.
- [circuit](https://github.com/cep21/circuit) - An efficient and feature complete Hystrix like Go implementation of the circuit breaker pattern.
- [circuitbreaker](https://github.com/rubyist/circuitbreaker) - Circuit Breakers in Go.
- [clipboard](https://github.com/golang-design/clipboard) - 📋 cross-platform clipboard package in Go.
- [clockwork](https://github.com/jonboulle/clockwork) - A simple fake clock for golang.
- [cmd](https://github.com/SimonBaeumer/cmd) - Library for executing shell commands on osx, windows and linux.
- [config-file-validator](https://github.com/Boeing/config-file-validator) - Cross Platform tool to validate configuration files.
- [contem](https://github.com/maxbolgarin/contem) - Drop-in context.Context replacement for graceful shutdown Go applications.
- [cookie](https://github.com/syntaqx/cookie) - Cookie struct parsing and helper package.
- [copy-pasta](https://github.com/jutkko/copy-pasta) - Universal multi-workstation clipboard that uses S3 like backend for the storage.
- [countries](https://github.com/biter777/countries) - Full implementation of ISO-3166-1, ISO-4217, ITU-T E.164, Unicode CLDR and IANA ccTLD standards.
- [countries](https://github.com/pioz/countries) - All you need when you are working with countries in Go.
- [create-go-app](https://github.com/create-go-app/cli) - A powerful CLI for create a new production-ready project with backend (Golang), frontend (JavaScript, TypeScript) & deploy automation (Ansible, Docker) by running one command.
- [cryptgo](https://github.com/Gituser143/cryptgo) - Crytpgo is a TUI based application written purely in Go to monitor and observe cryptocurrency prices in real time!
- [ctop](https://github.com/bcicen/ctop) - [Top-like](https://ctop.sh) interface (e.g. htop) for container metrics.
- [ctxutil](https://github.com/posener/ctxutil) - A collection of utility functions for contexts.
- [cvt](https://github.com/shockerli/cvt) - Easy and safe convert any value to another type.
- [dbt](https://github.com/nikogura/dbt) - A framework for running self-updating signed binaries from a central, trusted repository.
- [Death](https://github.com/vrecan/death) - Managing go application shutdown with signals.
- [debounce](https://github.com/floatdrop/debounce) - A zero-allocation debouncer written in Go.
- [delve](https://github.com/derekparker/delve) - Go debugger.
- [dive](https://github.com/wagoodman/dive) - A tool for exploring each layer in a Docker image.
- [dlog](https://github.com/kirillDanshin/dlog) - Compile-time controlled logger to make your release smaller without removing debug calls.
- [EaseProbe](https://github.com/megaease/easeprobe) - A simple, standalone, and lightWeight tool that can do health/status checking daemon, support HTTP/TCP/SSH/Shell/Client/... probes, and Slack/Discord/Telegram/SMS... notification.
- [equalizer](https://github.com/reugn/equalizer) - Quota manager and rate limiter collection for Go.
- [ergo](https://github.com/cristianoliveira/ergo) - The management of multiple local services running over different ports made easy.
- [evaluator](https://github.com/nullne/evaluator) - Evaluate an expression dynamically based on s-expression. It's simple and easy to extend.
- [Failsafe-go](https://github.com/failsafe-go/failsafe-go) - Fault tolerance and resilience patterns for Go.
- [filetype](https://github.com/h2non/filetype) - Small package to infer the file type checking the magic numbers signature.
- [filler](https://github.com/yaronsumel/filler) - small utility to fill structs using "fill" tag.
- [filter](https://github.com/gookit/filter) - provide filtering, sanitizing, and conversion of Go data.
- [fzf](https://github.com/junegunn/fzf) - Command-line fuzzy finder written in Go.
- [generate](https://github.com/go-playground/generate) - runs go generate recursively on a specified path or environment variable and can filter by regex.
- [gh-image](https://github.com/drogers0/gh-image) - A gh CLI extension that uploads images to GitHub issues, PRs, and READMEs from the command line, producing user-attachments URLs that respect repository visibility.
- [ghokin](https://github.com/antham/ghokin) - Parallelized formatter with no external dependencies for gherkin (cucumber, behat...).
- [git-time-metric](https://github.com/git-time-metric/gtm) - Simple, seamless, lightweight time tracking for Git.
- [git-tools](https://github.com/kazhuravlev/git-tools) - Tool to help manage git tags.
- [gitbatch](https://github.com/isacikgoz/gitbatch) - manage your git repositories in one place.
- [gitcs](https://github.com/knbr13/gitcs/) - Git Commits Visualizer, CLI tool to visualize your Git commits on your local machine.
- [go-actuator](https://github.com/sinhashubham95/go-actuator) - Production ready features for Go based web frameworks.
- [go-astitodo](https://github.com/asticode/go-astitodo) - Parse TODOs in your GO code.
- [go-bind-plugin](https://github.com/wendigo/go-bind-plugin) - go:generate tool for wrapping symbols exported by golang plugins (1.8 only).
- [go-bsdiff](https://github.com/gabstv/go-bsdiff) - Pure Go bsdiff and bspatch libraries and CLI tools.
- [go-clip](https://github.com/prashantgupta24/go-clip) - A minimalistic clipboard manager for Mac.
- [Go-Constant](https://github.com/sajjadrabiee/go-constant) - Generic typed constant sets with safe string parsing for Go's missing enum type.
- [go-convert](https://github.com/Eun/go-convert) - Package go-convert enables you to convert a value into another type.
- [go-countries](https://github.com/mikekonan/go-countries) - Lightweight lookup over ISO-3166 codes.
- [go-dry](https://github.com/ungerik/go-dry) - DRY (don't repeat yourself) package for Go.
- [go-events](https://github.com/deatil/go-events) - A go event and event'subscribe package, like wordpress hook functions.
- [go-funk](https://github.com/thoas/go-funk) - Modern Go utility library which provides helpers (map, find, contains, filter, chunk, reverse, ...).
- [go-health](https://github.com/Talento90/go-health) - Health package simplifies the way you add health check to your services.
- [go-httpheader](https://github.com/mozillazg/go-httpheader) - Go library for encoding structs into Header fields.
- [go-lambda-cleanup](https://github.com/karl-cardenas-coding/go-lambda-cleanup) - A CLI for removing unused or previous versions of AWS Lambdas.
- [go-lock](https://github.com/viney-shih/go-lock) - go-lock is a lock library implementing read-write mutex and read-write trylock without starvation.
- [go-pattern-match](https://github.com/PhakornKiong/go-pattern-match) - A Pattern matching library inspired by ts-pattern.
- [go-pkg](https://github.com/chenquan/go-pkg) - A go toolkit.
- [go-problemdetails](https://github.com/mvmaasakkers/go-problemdetails) - Go package for working with Problem Details.
- [go-qr](https://github.com/piglig/go-qr) - A native, high-quality and minimalistic QR code generator.
- [go-rate](https://github.com/beefsack/go-rate) - Timed rate limiter for Go.
- [go-safecast](https://github.com/ccoVeille/go-safecast) - Safe number type conversion library that prevents integer overflow and underflow (addresses gosec G115 and CWE-190).
- [go-sitemap-generator](https://github.com/ikeikeikeike/go-sitemap-generator) - XML Sitemap generator written in Go.
- [go-snk](https://github.com/SharkByteSoftware/go-snk) - Type-safe generic helpers for slices, maps, strings, errors, JSON, HTTP, and containers, organized as small independently adoptable packages.
- [go-trigger](https://github.com/sadlil/go-trigger) - Go-lang global event triggerer, Register Events with an id and trigger the event from anywhere from your project.
- [go-tripper](https://github.com/rajnandan1/go-tripper) - Tripper is a circuit breaker package for Go that allows you to circuit and control the status of circuits.
- [go-type](https://github.com/mikekonan/go-types) - Library providing Go types for store/validation and transfer of ISO-4217, ISO-3166, and other types.
- [go-utils](https://github.com/Goldziher/go-utils) - Simple, performant generic utilities for Go inspired by JavaScript and Python (map, filter, reduce, and more).
- [goback](https://github.com/carlescere/goback) - Go simple exponential backoff package.
- [goctx](https://github.com/zerosnake0/goctx) - Get your context value with high performance.
- [godaemon](https://github.com/VividCortex/godaemon) - Utility to write daemons.
- [godoclive](https://github.com/syst3mctl/godoclive) - Generates interactive API documentation from Go HTTP handlers using static analysis of chi, gin, and net/http routers.
- [godropbox](https://github.com/dropbox/godropbox) - Common libraries for writing Go services/applications from Dropbox.
- [gofn](https://github.com/tiendc/gofn) - High performance utility functions written using Generics for Go 1.18+.
- [golarm](https://github.com/msempere/golarm) - Fire alarms with system events.
- [golog](https://github.com/mlimaloureiro/golog) - Easy and lightweight CLI tool to time track your tasks.
- [gopencils](https://github.com/bndr/gopencils) - Small and simple package to easily consume REST APIs.
- [goplaceholder](https://github.com/michiwend/goplaceholder) - a small golang lib to generate placeholder images.
- [goreadability](https://github.com/philipjkim/goreadability) - Webpage summary extractor using Facebook Open Graph and arc90's readability.
- [goreleaser](https://github.com/goreleaser/goreleaser) - Deliver Go binaries as fast and easily as possible.
- [goreporter](https://github.com/wgliang/goreporter) - Golang tool that does static analysis, unit testing, code review and generate code quality report.
- [goseaweedfs](https://github.com/linxGnu/goseaweedfs) - SeaweedFS client library with almost full features.
- [gostrutils](https://github.com/ik5/gostrutils) - Collections of string manipulation and conversion functions.
- [gotenv](https://github.com/subosito/gotenv) - Load environment variables from `.env` or any `io.Reader` in Go.
- [goval](https://github.com/maja42/goval) - Evaluate arbitrary expressions in Go.
- [graterm](https://github.com/skovtunenko/graterm) - Provides primitives to perform ordered (sequential/concurrent) GRAceful TERMination (aka shutdown) in Go application.
- [grofer](https://github.com/pesos/grofer) - A system and resource monitoring tool written in Golang!
- [gubrak](https://github.com/novalagung/gubrak) - Golang utility library with syntactic sugar. It's like lodash, but for golang.
- [handy](https://github.com/miguelpragier/handy) - Many utilities and helpers like string handlers/formatters and validators.
- [healthcheck](https://github.com/kazhuravlev/healthcheck) - A simple yet powerful readiness test for Kubernetes.
- [hostctl](https://github.com/guumaster/hostctl) - A CLI tool to manage /etc/hosts with easy commands.
- [htcat](https://github.com/htcat/htcat) - Parallel and Pipelined HTTP GET Utility.
- [hub](https://github.com/github/hub) - wrap git commands with additional functionality to interact with github from the terminal.
- [immortal](https://github.com/immortal/immortal) - \*nix cross-platform (OS agnostic) supervisor.
- [jet](https://github.com/NicoNex/jet) - Just Edit Text: a fast and powerful tool for finding and replacing file content and names using regular expressions.
- [jsend](https://github.com/clevergo/jsend) - JSend's implementation written in Go.
- [json-log-viewer](https://github.com/hedhyw/json-log-viewer) - Interactive viewer for JSON logs.
- [jump](https://github.com/gsamokovarov/jump) - Jump helps you navigate faster by learning your habits.
- [just](https://github.com/kazhuravlev/just) - Just a collection of useful functions for working with generic data structures.
- [koazee](https://github.com/wesovilabs/koazee) - Library inspired in Lazy evaluation and functional programming that takes the hassle out of working with arrays.
- [LAN Orangutan](https://github.com/291-Group/LAN-Orangutan) - Network device discovery and inventory with persistent labeling, multi-network scanning, and Tailscale integration.
- [lang](https://github.com/maxbolgarin/lang) - Generic one-liners to work with variables, slices and maps without boilerplate code.
- [lets-go](https://github.com/aplescia-chwy/lets-go) - Go module that provides common utilities for Cloud Native REST API development. Also contains AWS Specific utilities.
- [limiters](https://github.com/mennanov/limiters) - Rate limiters for distributed applications in Golang with configurable back-ends and distributed locks.
- [lo](https://github.com/samber/lo) - A Lodash like Go library based on Go 1.18+ Generics (map, filter, contains, find...)
- [loncha](https://github.com/kazu/loncha) - A high-performance slice Utilities.
- [lrserver](https://github.com/jaschaephraim/lrserver) - LiveReload server for Go.
- [mani](https://github.com/alajmo/mani) - CLI tool to help you manage multiple repositories.
- [mc](https://github.com/minio/mc) - Minio Client provides minimal tools to work with Amazon S3 compatible cloud storage and filesystems.
- [mergo](https://github.com/imdario/mergo) - Helper to merge structs and maps in Golang. Useful for configuration default values, avoiding messy if-statements.
- [mimemagic](https://github.com/zRedShift/mimemagic) - Pure Go ultra performant MIME sniffing library/utility.
- [mimetype](https://github.com/gabriel-vasile/mimetype) - Package for MIME type detection based on magic numbers.
- [minify](https://github.com/tdewolff/minify) - Fast minifiers for HTML, CSS, JS, XML, JSON and SVG file formats.
- [minquery](https://github.com/icza/minquery) - MongoDB / mgo.v2 query that supports efficient pagination (cursors to continue listing documents where we left off).
- [moldova](https://github.com/StabbyCutyou/moldova) - Utility for generating random data based on an input template.
- [mole](https://github.com/davrodpin/mole) - cli app to easily create ssh tunnels.
- [mongo-go-pagination](https://github.com/gobeam/mongo-go-pagination) - Mongodb Pagination for official mongodb/mongo-go-driver package which supports both normal queries and Aggregation pipelines.
- [mssqlx](https://github.com/linxGnu/mssqlx) - Database client library, proxy for any master slave, master master structures. Lightweight and auto balancing in mind.
- [multitick](https://github.com/VividCortex/multitick) - Multiplexor for aligned tickers.
- [netbug](https://github.com/e-dard/netbug) - Easy remote profiling of your services.
- [nfdump](https://github.com/chrispassas/nfdump) - Read nfdump netflow files.
- [nostromo](https://github.com/pokanop/nostromo) - CLI for building powerful aliases.
- [okrun](https://github.com/xta/okrun) - go run error steamroller.
- [olaf](https://github.com/btnguyen2k/olaf) - Twitter Snowflake implemented in Go.
- [onecache](https://github.com/adelowo/onecache) - Caching library with support for multiple backend stores (Redis, Memcached, filesystem etc).
- [optional](https://github.com/kazhuravlev/optional) - Optional struct fields and vars.
- [panicparse](https://github.com/maruel/panicparse) - Groups similar goroutines and colorizes stack dump.
- [pattern-match](https://github.com/alexpantyukhin/go-pattern-match) - Pattern matching library.
- [peco](https://github.com/peco/peco) - Simplistic interactive filtering tool.
- [pgo](https://github.com/arthurkushman/pgo) - Convenient functions for PHP community.
- [pm](https://github.com/VividCortex/pm) - Process (i.e. goroutine) manager with an HTTP API.
- [pointer](https://github.com/xorcare/pointer) - Package pointer contains helper routines for simplifying the creation of optional fields of basic type.
- [ptr](https://github.com/gotidy/ptr) - Package that provide functions for simplified creation of pointers from constants of basic types.
- [rate](https://github.com/webriots/rate) - High-performance rate limiting library with token bucket and AIMD strategies.
- [rclient](https://github.com/zpatrick/rclient) - Readable, flexible, simple-to-use client for REST APIs.
- [release](https://github.com/tomodian/release) - CLI for Keep-a-changelog formatted changelogs.
- [relimpact](https://github.com/hashmap-kz/relimpact) - Fast API compatibility reports for Go projects.
- [remote-touchpad](https://github.com/Unrud/remote-touchpad) - Control mouse and keyboard from a smartphone.
- [repeat](https://github.com/ssgreg/repeat) - Go implementation of different backoff strategies useful for retrying operations and heartbeating.
- [request](https://github.com/mozillazg/request) - Go HTTP Requests for Humans™.
- [rerun](https://github.com/ivpusic/rerun) - Recompiling and rerunning go apps when source changes.
- [rest-go](https://github.com/edermanoel94/rest-go) - A package that provide many helpful methods for working with rest api.
- [retro](https://github.com/goioc/retro) - Handy retry-on-error library with extensive flexibility (backoff strategies, caps, etc).
- [retry](https://github.com/kamilsk/retry) - The most advanced functional mechanism to perform actions repetitively until successful.
- [retry](https://github.com/percolate/retry) - A simple but highly configurable retry package for Go.
- [retry](https://github.com/thedevsaddam/retry) - Simple and easy retry mechanism package for Go.
- [retry](https://github.com/shafreeck/retry) - A pretty simple library to ensure your work to be done.
- [retry-go](https://github.com/avast/retry-go) - Simple library for retry mechanism.
- [retry-go](https://github.com/rafaeljesus/retry-go) - Retrying made simple and easy for golang.
- [robustly](https://github.com/VividCortex/robustly) - Runs functions resiliently, catching and restarting panics.
- [rospo](https://github.com/ferama/rospo) - Simple and reliable ssh tunnels with embedded ssh server in Golang.
- [scan](https://github.com/blockloop/scan) - Scan golang `sql.Rows` directly to structs, slices, or primitive types.
- [scan](https://github.com/wroge/scan) - Scan sql rows into any type powered by generics.
- [scany](https://github.com/georgysavva/scany) - Library for scanning data from a database into Go structs and more.
- [serve](https://github.com/syntaqx/serve) - A static http server anywhere you need.
- [sesh](https://github.com/joshmedeski/sesh) - Sesh is a CLI that helps you create and manage tmux sessions quickly and easily using zoxide.
- [set](https://github.com/nofeaturesonlybugs/set) - Performant and flexible struct mapping and loose type conversion.
- [shutdown](https://github.com/ztrue/shutdown) - App shutdown hooks for `os.Signal` handling.
- [silk](https://github.com/chrispassas/silk) - Read silk netflow files.
- [slice](https://github.com/psampaz/slice) - Type-safe functions for common Go slice operations.
- [sliceconv](https://github.com/Henry-Sarabia/sliceconv) - Slice conversion between primitive types.
- [slicer](https://github.com/leaanthony/slicer) - Makes working with slices easier.
- [sorty](https://github.com/jfcg/sorty) - Fast Concurrent / Parallel Sorting.
- [sqlex](https://github.com/go-sqlex/sqlex) - Drop-in modernization of jmoiron/sqlx with fixed SQL lexer bugs, automatic IN-clause expansion, pluggable hooks, and unified DB/Tx/Conn interfaces.
- [sqlx](https://github.com/jmoiron/sqlx) - provides a set of extensions on top of the excellent built-in database/sql package.
- [sqlz](https://github.com/rfberaldo/sqlz) - Extension for the database/sql package, adding named queries, struct scanning, and batch operations.
- [sshman](https://github.com/shoobyban/sshman) - SSH Manager for authorized_keys files on multiple remote servers.
- [stacktower](https://github.com/stacktower-io/stacktower) - Visualize dependency graphs as physical tower structures, inspired by XKCD #2347.
- [statiks](https://github.com/janiltonmaciel/statiks) - Fast, zero-configuration, static HTTP filer server.
- [Storm](https://github.com/asdine/storm) - Simple and powerful toolkit for BoltDB.
- [structs](https://github.com/PumpkinSeed/structs) - Implement simple functions to manipulate structs.
- [throttle](https://github.com/yudppp/throttle) - Throttle is an object that will perform exactly one action per duration.
- [tik](https://github.com/andy2046/tik) - Simple and easy timing wheel package for Go.
- [tome](https://github.com/cyruzin/tome) - Tome was designed to paginate simple RESTful APIs.
- [toolbox](https://github.com/viant/toolbox) - Slice, map, multimap, struct, function, data conversion utilities. Service router, macro evaluator, tokenizer.
- [UNIS](https://github.com/esemplastic/unis) - Common Architecture™ for String Utilities in Go.
- [upterm](https://github.com/owenthereal/upterm) - A tool for developers to share terminal/tmux sessions securely over the web. It’s perfect for remote pair programming, accessing computers behind NATs/firewalls, remote debugging, and more.
- [usql](https://github.com/knq/usql) - usql is a universal command-line interface for SQL databases.
- [util](https://github.com/shomali11/util) - Collection of useful utility functions. (strings, concurrency, manipulations, ...).
- [watchhttp](https://github.com/nikolaydubina/watchhttp) - Run command periodically and expose latest STDOUT or its rich delta as HTTP endpoint.
- [wifiqr](https://github.com/reugn/wifiqr) - Wi-Fi QR Code Generator.
- [wuzz](https://github.com/asciimoo/wuzz) - Interactive cli tool for HTTP inspection.
- [xferspdy](https://github.com/monmohan/xferspdy) - Xferspdy provides binary diff and patch library in golang.
- [xpool](https://github.com/peczenyj/xpool) - Yet another golang type safe object pool using generics.
- [yogo](https://github.com/antham/yogo) - Check yopmail mails from command line.

**[⬆ 回到顶部](#contents)**

<a id="uuid"></a>
## UUID

_用于处理 UUID 的库。_

- [fastuuid](https://github.com/rekby/fastuuid) - Fast generate UUIDv4 as string or bytes.
- [goid](https://github.com/jakehl/goid) - Generate and Parse RFC4122 compliant V4 UUIDs.
- [gouid](https://github.com/twharmon/gouid) - Generate cryptographically secure random string IDs with just one allocation.
- [guid](https://github.com/sdrapkin/guid) - Fast cryptographically safe Guid generator for Go (~10x faster than `uuid`).
- [nanoid](https://github.com/aidarkhanov/nanoid) - A tiny and efficient Go unique string ID generator.
- [sno](https://github.com/muyo/sno) - Compact, sortable and fast unique IDs with embedded metadata.
- [ulid](https://github.com/oklog/ulid) - Go implementation of ULID (Universally Unique Lexicographically Sortable Identifier).
- [uniq](https://gitlab.com/skilstak/code/go/uniq) - No hassle safe, fast unique identifiers with commands.
- [uuid](https://github.com/agext/uuid) - Generate, encode, and decode UUIDs v1 with fast or cryptographic-quality random node identifier.
- [uuid](https://github.com/gofrs/uuid) - Implementation of Universally Unique Identifier (UUID). Supports both creation and parsing of UUIDs. Actively maintained fork of satori uuid.
- [uuid](https://github.com/google/uuid) - Go package for UUIDs based on RFC 4122 and DCE 1.1: Authentication and Security Services.
- [uuidcheck](https://github.com/ashwingopalsamy/uuidcheck) - A tiny, dependency-free Go library that validates UUIDs against standard RFC 4122 formatting, converts UUIDv7() into UTC timestamps.
- [wuid](https://github.com/edwingeng/wuid) - An extremely fast globally unique number generator.
- [xid](https://github.com/rs/xid) - Xid is a globally unique id generator library, ready to be safely used directly in your server code.

**[⬆ 回到顶部](#contents)**

<a id="validation"></a>
## 数据校验

_用于数据校验的库。_

- [checkdigit](https://github.com/osamingo/checkdigit) - Provide check digit algorithms (Luhn, Verhoeff, Damm) and calculators (ISBN, EAN, JAN, UPC, etc.).
- [checker](https://github.com/cinar/checker) - Zero-dependency input validation and in-place normalization with struct tags, 23 locales, and JSON Schema generation.
- [go-validator](https://github.com/tiendc/go-validator) - Validation library using Generics.
- [gody](https://github.com/guiferpa/gody) - :balloon: A lightweight struct validator for Go.
- [govalid](https://github.com/twharmon/govalid) - Fast, tag-based validation for structs.
- [govalidator](https://github.com/asaskevich/govalidator) - Validators and sanitizers for strings, numerics, slices and structs.
- [govalidator](https://github.com/thedevsaddam/govalidator) - Validate Golang request data with simple rules. Highly inspired by Laravel's request validation.
- [govy](https://github.com/nobl9/govy) - strongly-typed validation rules over functional interface, powered by generics and reflection free with heavy focus on crafting clear and information-rich error messages.
- [hvalid](https://github.com/lyonnee/hvalid) hvalid is a lightweight validation library written in Go language. It provides a custom validator interface and a series of common validation functions to help developers quickly implement data validation.
- [jio](https://github.com/faceair/jio) - jio is a json schema validator similar to [joi](https://github.com/hapijs/joi).
- [ozzo-validation](https://github.com/go-ozzo/ozzo-validation) - Supports validation of various data types (structs, strings, maps, slices, etc.) with configurable and extensible validation rules specified in usual code constructs instead of struct tags.
- [validate](https://github.com/gookit/validate) - Go package for data validation and filtering. support validate Map, Struct, Request(Form, JSON, url.Values, Uploaded Files) data and more features.
- [validate](https://github.com/gobuffalo/validate) - This package provides a framework for writing validations for Go applications.
- [validator](https://github.com/go-playground/validator) - Go Struct and Field validation, including Cross Field, Cross Struct, Map, Slice and Array diving.
- [Validator](https://github.com/go-the-way/validator) - A lightweight model validator written in Go.Contains VFs:Min, Max, MinLength, MaxLength, Length, Enum, Regex.
- [valix](https://github.com/marrow16/valix) Go package for validating requests
- [Zog](https://github.com/Oudwins/zog) - A [Zod](https://github.com/colinhacks/zod) inspired schema builder for runtime value parsing and validation.
- [vx](https://github.com/sevlyar/vx) - Validation built from small, composable checks with zero dependencies and a reconstructable error path.
  **[⬆ 回到顶部](#contents)**

<a id="version-control"></a>
## 版本控制

_用于版本控制的库。_

- [cli](https://gitlab.com/gitlab-org/cli) - An open-source GitLab command line tool bringing GitLab's cool features to your command line.
- [froggit-go](https://github.com/jfrog/froggit-go) - Froggit-Go is a Go library, allowing to perform actions on VCS providers.
- [ggc](https://github.com/bmf-san/ggc) - A Git CLI tool with both traditional command-line and interactive incremental-search UI, workflow support, and configurable keybindings.
- [git-courer](https://github.com/Alejandro-M-P/git-courer) - Local MCP server for Git operations using Ollama to save tokens and prevent secret leakage.
- [git2go](https://github.com/libgit2/git2go) - Go bindings for libgit2.
- [githooks](https://github.com/gabyx/githooks) - Per-repo and shared Git hooks with version control and auto update.
- [gitty](https://github.com/Omibranch/gitty) - Single-binary Git/GitHub CLI that replaces add→commit→push with one command; human-readable syntax, no external dependencies.
- [go-git](https://github.com/go-git/go-git) - highly extensible Git implementation in pure Go.
- [go-vcs](https://github.com/sourcegraph/go-vcs) - manipulate and inspect VCS repositories in Go.
- [hercules](https://github.com/src-d/hercules) - gaining advanced insights from Git repository history.
- [hgo](https://github.com/beyang/hgo) - Hgo is a collection of Go packages providing read-access to local Mercurial repositories.

**[⬆ 回到顶部](#contents)**

<a id="video"></a>
## 视频

_用于视频处理的库。_

- [gmf](https://github.com/3d0c/gmf) - Go bindings for FFmpeg av\* libraries.
- [go-astiav](https://github.com/asticode/go-astiav) - Better C bindings for ffmpeg in GO.
- [go-astisub](https://github.com/asticode/go-astisub) - Manipulate subtitles in GO (.srt, .stl, .ttml, .webvtt, .ssa/.ass, teletext, .smi, etc.).
- [go-astits](https://github.com/asticode/go-astits) - Parse and demux MPEG Transport Streams (.ts) natively in GO.
- [go-mpd](https://github.com/unki2aut/go-mpd) - Parser and generator library for MPEG-DASH manifest files.
- [goav](https://github.com/giorgisio/goav) - Comprehensive Go bindings for FFmpeg.
- [gortsplib](https://github.com/aler9/gortsplib) - Pure Go RTSP server and client library.
- [hls-m3u8](https://github.com/Eyevinn/hls-m3u8) - Parser and generator for HLS (M3U8) playlists; kept up to date with the spec.
- [libvlc-go](https://github.com/adrg/libvlc-go) - Go bindings for libvlc 2.X/3.X/4.X (used by the VLC media player).
- [manifestor](https://github.com/alanzng/manifestor) - Zero-dependency library for parsing, filtering, transforming, and building HLS and DASH manifests.
* [mosaic](https://github.com/farshidrezaei/mosaic) - Predictable, production-ready Adaptive Bitrate (ABR) video packaging for Go (HLS & DASH CMAF).
- [mp4ff](https://github.com/Eyevinn/mp4ff) - Library and tools for working with MP4 files containing video, audio, subtitles, or metadata.
- [mpeg-ts-analyzer](https://github.com/small-teton/mpeg-ts-analyzer) - Analyzer for MPEG-2 Transport Streams that checks PCR timing compliance and dumps low-level TS, PSI, and PES structures.
- [v4l](https://github.com/korandiz/v4l) - Video capture library for Linux, written in Go.

**[⬆ 回到顶部](#contents)**

<a id="web-frameworks"></a>
## Web 框架

_全栈 Web 框架。_

- [aichteeteapee](https://github.com/psyb0t/aichteeteapee) - Batteries-included HTTP server library with a router, middleware stack, WebSocket hubs, file uploads, and OpenAPI validation.
- [Andurel](https://github.com/mbvlabs/andurel) - Rails-inspired full-stack Go web framework with scaffolding, database tooling, and server-rendered or Inertia frontends.
- [Atreugo](https://github.com/savsgio/atreugo) - High performance and extensible micro web framework with zero memory allocations in hot paths.
- [Barf](https://github.com/opensaucerer/barf) - Basically, A Remarkable Framework for building JSON-based web APIs. It is entirely unobtrusive and re-invents no wheel. It is crafted such that getting started is easy and quick while being flexible enough for more complex use cases.
- [Beego](https://github.com/beego/beego) - beego is an open-source, high-performance web framework for the Go programming language.
- [Confetti Framework](https://confetti-framework.github.io/docs/) - Confetti is a Go web application framework with an expressive, elegant syntax. Confetti combines the elegance of Laravel and the simplicity of Go.
- [Don](https://github.com/abemedia/go-don) - A highly performant and simple to use API framework.
- [doors](https://github.com/doors-dev/doors) - Server-driven framework for building stateful, reactive web applications entirely in Go.
- [Echo](https://github.com/labstack/echo) - High performance, minimalist Go web framework.
- [Fastschema](https://github.com/fastschema/fastschema) - A flexible Go web framework and Headless CMS.
- [Fiber](https://github.com/gofiber/fiber) - An Express.js inspired web framework build on Fasthttp.
- [Flamingo](https://github.com/i-love-flamingo/flamingo) - Framework for pluggable web projects. Including a concept for modules and offering features for DI, Configareas, i18n, template engines, graphql, observability, security, events, routing & reverse routing etc.
- [Flamingo Commerce](https://github.com/i-love-flamingo/flamingo-commerce) - Providing e-commerce features using clean architecture like DDD and ports and adapters, that you can use to build flexible e-commerce applications.
- [Fuego](https://github.com/go-fuego/fuego) - The framework for busy Go developers! Web framework generating OpenAPI 3 spec from source code.
- [Gin](https://github.com/gin-gonic/gin) - Gin is a web framework written in Go! It features a martini-like API with much better performance, up to 40 times faster. If you need performance and good productivity.
- [Ginrpc](https://github.com/xxjwxc/ginrpc) - Gin parameter automatic binding tool,gin rpc tools.
- [go-api-boot](https://github.com/SaiNageswarS/go-api-boot) - A gRpc-first micro-service framework. Features include ODM support for Mongo, cloud resource support (AWS/Azure/Google), and a fluent dependency injection which is customized for gRpc. Additionally, grpc-web is supported directly, enabling browser access to all gRpc APIs without a proxy.
- [Goa](https://github.com/goadesign/goa) - Goa provides a holistic approach for developing remote APIs and microservices in Go.
- [GoFr](https://github.com/gofr-dev/gofr) - Gofr is an opinionated microservice development framework.
- [GoFrame](https://github.com/gogf/gf) - GoFrame is a modular, powerful, high-performance and enterprise-class application development framework of Golang.
- [Gone](https://github.com/gone-io/gone) - A lightweight dependency injection and web framework inspired by Spring.
- [goravel](https://github.com/goravel/goravel) - A Laravel-inspired web framework with ORM, authentication, queue, task scheduling, and more built-in features.
- [Goshtoso](https://github.com/araihu/goshtoso) - Server-rendered UI components for Go applications, built with templ, Tailwind CSS, HTMX, and Alpine.js.
- [Goyave](https://github.com/go-goyave/goyave) - Feature-complete REST API framework aimed at clean code and fast development, with powerful built-in functionalities.
- [Hertz](https://github.com/cloudwego/hertz) - A high-performance and strong-extensibility Go HTTP framework that helps developers build microservices.
- [hiboot](https://github.com/hidevopsio/hiboot) - hiboot is a high performance web application framework with auto configuration and dependency injection support.
- [httpsuite](https://github.com/rluders/httpsuite) - HTTP request parsing and RFC 9457 problem responses for Go, with a stdlib-only core and optional validation.
- [Huma](https://github.com/danielgtaylor/huma/) - Framework for modern REST/GraphQL APIs with built-in OpenAPI 3, generated documentation, and a CLI.
- [iWF](https://github.com/indeedeng/iwf) - iWF is an all-in-one platform for developing long-running business processes. It offers a convenient abstraction for utilizing databases, ElasticSearch, message queues, durable timers, and more, with a clean, simple, and user-friendly interface.
- [Lit](https://github.com/jvcoutinho/lit) - Highly performant declarative web framework for Golang, aiming for simplicity and quality of life.
- [Microservice](https://github.com/claygod/microservice) - The framework for the creation of microservices, written in Golang.
- [NotNet](https://github.com/nottechdm/notnet) - A lightweight Go framework for building fast, ergonomic RESTful APIs with middleware and flexible routing.
- [patron](https://github.com/beatlabs/patron) - Patron is a microservice framework following best cloud practices with a focus on productivity.
- [Pnutmux](https://gitlab.com/fruitygo/pnutmux) - Pnutmux is a powerful Go web framework that uses regex for matching and handling HTTP requests. It offers features such as CORS handling, structured logging, URL parameters extraction, middlewares, and concurrency limiting.
- [Revel](https://github.com/revel/revel) - High-productivity web framework for the Go language.
- [rk-boot](https://github.com/rookie-ninja/rk-boot) - A bootstrapper library for building enterprise go microservice with Gin and gRPC quickly and easily.
- [Ronykit](https://github.com/clubpay/ronykit) - Web framework with pluggable architecture and very performant.
- [rux](https://github.com/gookit/rux) - Simple and fast web framework for build golang HTTP applications.
- [templui](https://github.com/axzilla/templui) - Modern UI Components for Go & Templ.
- [togo](https://github.com/togo-framework/togo) - Full-stack framework that ships your Go backend and React frontend as a single binary; a Laravel-artisan-grade CLI.
- [uAdmin](https://github.com/uadmin/uadmin) - Fully featured web framework for Golang, inspired by Django.
- [WebGo](https://github.com/naughtygopher/webgo) - A micro-framework to build web apps with handler chaining, middleware, and context injection. With standard library-compliant HTTP handlers (i.e., `http.HandlerFunc`)..
- [Xun](https://github.com/yaitoo/xun) - Web framework built on Go's built-in html/template and net/http package’s router. It is designed to be lightweight, fast, and easy to use while providing a simple and intuitive API for building web applications with advanced features such as middleware, routing, and template rendering.
- [Yokai](https://github.com/ankorstore/yokai) - Simple, modular, and observable Go framework for backend applications.

**[⬆ 回到顶部](#contents)**

<a id="middlewares"></a>
### 中间件

<a id="actual-middlewares"></a>
#### 实际中间件

- [client-timing](https://github.com/posener/client-timing) - An HTTP client for Server-Timing header.
- [CORS](https://github.com/rs/cors) - Easily add CORS capabilities to your API.
- [echo-middleware](https://github.com/faabiosr/echo-middleware) - Middleware for Echo framework with logging and metrics.
- [formjson](https://github.com/rs/formjson) - Transparently handle JSON input as a standard form POST.
- [go-fault](https://github.com/github/go-fault) - Fault injection middleware for Go.
- [Limiter](https://github.com/ulule/limiter) - Dead simple rate limit middleware for Go.
- [ln-paywall](https://github.com/philippgille/ln-paywall) - Go middleware for monetizing APIs on a per-request basis with the Lightning Network (Bitcoin).
- [mid](https://github.com/bobg/mid) - Miscellaneous HTTP middleware features: idiomatic error return from handlers; receive/respond with JSON data; request tracing; and more.
- [rk-gin](https://github.com/rookie-ninja/rk-gin) - Middleware for Gin framework with logging, metrics, auth, tracing etc.
- [rk-grpc](https://github.com/rookie-ninja/rk-grpc) - Middleware for gRPC with logging, metrics, auth, tracing etc.
- [Tollbooth](https://github.com/didip/tollbooth) - Rate limit HTTP request handler.
- [XFF](https://github.com/sebest/xff) - Handle `X-Forwarded-For` header and friends.

<a id="libraries-for-creating-http-middlewares"></a>
#### 用于编写 HTTP 中间件的库

- [alice](https://github.com/justinas/alice) - Painless middleware chaining for Go.
- [catena](https://github.com/codemodus/catena) - http.Handler wrapper catenation (same API as "chain").
- [chain](https://github.com/codemodus/chain) - Handler wrapper chaining with scoped data (net/context-based "middleware").
- [gores](https://github.com/alioygur/gores) - Go package that handles HTML, JSON, XML and etc. responses. Useful for RESTful APIs.
- [interpose](https://github.com/carbocation/interpose) - Minimalist net/http middleware for golang.
- [mediary](https://github.com/HereMobilityDevelopers/mediary) - add interceptors to `http.Client` to allow dumping/shaping/tracing/... of requests/responses.
- [muxchain](https://github.com/stephens2424/muxchain) - Lightweight middleware for net/http.
- [negroni](https://github.com/urfave/negroni) - Idiomatic HTTP middleware for Golang.
- [render](https://github.com/unrolled/render) - Go package for easily rendering JSON, XML, and HTML template responses.
- [renderer](https://github.com/thedevsaddam/renderer) - Simple, lightweight and faster response (JSON, JSONP, XML, YAML, HTML, File) rendering package for Go.
- [stats](https://github.com/thoas/stats) - Go middleware that stores various information about your web application.

**[⬆ 回到顶部](#contents)**

<a id="routers"></a>
### 路由器

- [alien](https://github.com/gernest/alien) - Lightweight and fast http router from outer space.
- [bellt](https://github.com/GuilhermeCaruso/bellt) - A simple Go HTTP router.
- [Bone](https://github.com/go-zoo/bone) - Lightning Fast HTTP Multiplexer.
- [Bxog](https://github.com/claygod/Bxog) - Simple and fast HTTP router for Go. It works with routes of varying difficulty, length and nesting. And he knows how to create a URL from the received parameters.
- [chi](https://github.com/go-chi/chi) - Small, fast and expressive HTTP router built on net/context.
- [fasthttprouter](https://github.com/buaazp/fasthttprouter) - High performance router forked from `httprouter`. The first router fit for `fasthttp`.
- [FastRouter](https://github.com/razonyang/fastrouter) - a fast, flexible HTTP router written in Go.
- [Fox](https://github.com/fox-toolkit/fox) - A high-performance HTTP router for building reverse proxies and API gateways, with first-class support for mutating routes at runtime.
- [fursy](https://github.com/coregx/fursy) - HTTP router with type-safe generic handlers, automatic OpenAPI 3.1 generation from code, and RFC 9457 error responses.
- [goblin](https://github.com/bmf-san/goblin) - A golang http router based on trie tree.
- [gocraft/web](https://github.com/gocraft/web) - Mux and middleware package in Go.
- [Goji](https://github.com/goji/goji) - Goji is a minimalistic and flexible HTTP request multiplexer with support for `net/context`.
- [GoLobby/Router](https://github.com/golobby/router) - GoLobby Router is a lightweight yet powerful HTTP router for the Go programming language.
- [goroute](https://github.com/goroute/route) - Simple yet powerful HTTP request multiplexer.
- [GoRouter](https://github.com/vardius/gorouter) - GoRouter is a Server/API micro framework, HTTP request router, multiplexer, mux that provides request router with middleware supporting `net/context`.
- [gowww/router](https://github.com/gowww/router) - Lightning fast HTTP router fully compatible with the net/http.Handler interface.
- [httprouter](https://github.com/julienschmidt/httprouter) - High performance router. Use this and the standard http handlers to form a very high performance web framework.
- [httptreemux](https://github.com/dimfeld/httptreemux) - High-speed, flexible tree-based HTTP router for Go. Inspiration from httprouter.
- [lars](https://github.com/go-playground/lars) - Is a lightweight, fast and extensible zero allocation HTTP router for Go used to create customizable frameworks.
- [mux](https://github.com/gorilla/mux) - Powerful URL router and dispatcher for golang.
- [nchi](https://github.com/muir/nchi) - chi-like router built on httprouter with dependency injection based middleware wrappers
- [ngamux](https://github.com/ngamux/ngamux) - Simple HTTP router for Go.
- [ozzo-routing](https://github.com/go-ozzo/ozzo-routing) - An extremely fast Go (golang) HTTP router that supports regular expression route matching. Comes with full support for building RESTful APIs.
- [pure](https://github.com/go-playground/pure) - Is a lightweight HTTP router that sticks to the std "net/http" implementation.
- [Siesta](https://github.com/VividCortex/siesta) - Composable framework to write middleware and handlers.
- [vestigo](https://github.com/husobee/vestigo) - Performant, stand-alone, HTTP compliant URL Router for go web applications.
- [violetear](https://github.com/nbari/violetear) - Go HTTP router.
- [xmux](https://github.com/rs/xmux) - High performance muxer based on `httprouter` with `net/context` support.
- [xujiajun/gorouter](https://github.com/xujiajun/gorouter) - A simple and fast HTTP router for Go.

**[⬆ 回到顶部](#contents)**

<a id="webassembly"></a>
## WebAssembly

- [dom](https://github.com/dennwc/dom) - DOM library.
- [Extism Go SDK](https://github.com/extism/go-sdk) - Universal, cross-language WebAssembly framework for building plug-in systems and polyglot apps.
- [go-canvas](https://github.com/markfarnan/go-canvas) - Library to use HTML5 Canvas, with all drawing within go code.
- [tinygo](https://github.com/tinygo-org/tinygo) - Go compiler for small places. Microcontrollers, WebAssembly, and command-line tools. Based on LLVM.
- [vert](https://github.com/norunners/vert) - Interop between Go and JS values.
- [wasmbrowsertest](https://github.com/agnivade/wasmbrowsertest) - Run Go WASM tests in your browser.
- [webapi](https://github.com/gowebapi/webapi) - Bindings for DOM and HTML generated from WebIDL.

**[⬆ 回到顶部](#contents)**

<a id="webhooks-server"></a>
## Webhook 服务

- [HookRun](https://github.com/bluvenr/hookrun) - Lightweight webhook action engine (~3MB single binary, zero deps) that executes commands and scripts from YAML rules with token/HMAC/IP auth and hot reload.
- [webhook](https://github.com/adnanh/webhook) - Tool which allows user to create HTTP endpoints (hooks) that execute commands on the server.
- [webhooked](https://github.com/42Atomys/webhooked) - A webhook receiver on steroids: handle, secure, format and store a Webhook payload has never been easier.
- [WebhookX](https://github.com/webhookx-io/webhookx) - A webhooks gateway for message receiving, processing, and reliable delivering.

**[⬆ 回到顶部](#contents)**

<a id="windows"></a>
## Windows

- [d3d9](https://github.com/gonutz/d3d9) - Go bindings for Direct3D9.
- [go-ole](https://github.com/go-ole/go-ole) - Win32 OLE implementation for golang.
- [gosddl](https://github.com/MonaxGT/gosddl) - Converter from SDDL-string to user-friendly JSON. SDDL consist of four part: Owner, Primary Group, DACL, SACL.
- [windowsupdate](https://github.com/ceshihao/windowsupdate) - A Golang binding for Windows Update Agent API using go-ole.

**[⬆ 回到顶部](#contents)**

<a id="workflow-frameworks"></a>
## 工作流框架

_用于创建工作流的库。_

- [Cadence-client](https://github.com/uber-go/cadence-client) - A framework for authoring workflows and activities running on top of the Cadence orchestration engine made by Uber.
- [Dagu](https://github.com/dagu-go/dagu) - No-code workflow executor. it executes DAGs defined in a simple YAML format.
- [durable-go](https://github.com/agenticenv/durable-go) - Durable execution engine for single-process Go apps and AI agents, with zero dependencies.
- [Flowbaker](https://github.com/flowbaker/flowbaker) - Self-hosted execution engine for building, connecting, and automating no-code workflows.
- [go-dag](https://github.com/rhosocial/go-dag) - A framework developed in Go that manages the execution of workflows described by directed acyclic graphs.
- [go-taskflow](https://github.com/noneback/go-taskflow) - A taskflow-like General-purpose Task-parallel Programming Framework with integrated visualizer and profiler.
- [GopherFlow](https://github.com/RealZimboGuy/gopherflow) - Durable workflow engine with a built-in web console, backed by Postgres, MySQL or SQLite.
- [workflow](https://github.com/luno/workflow) - A tech stack agnostic Event Driven Workflow framework.

**[⬆ 回到顶部](#contents)**

<a id="xml"></a>
## XML

_用于处理 XML 的库与工具。_

- [XML-Comp](https://github.com/xml-comp/xml-comp) - Simple command line XML comparer that generates diffs of folders, files and tags.
- [xml2map](https://github.com/sbabiv/xml2map) - XML to MAP converter written Golang.
- [xmlquery](https://github.com/antchfx/xmlquery) - xmlquery is Golang XPath package for XML query.
- [xmlwriter](https://github.com/shabbyrobe/xmlwriter) - Procedural XML generation API based on libxml2's xmlwriter module.
- [xpath](https://github.com/antchfx/xpath) - XPath package for Go.
- [zek](https://github.com/miku/zek) - Generate a Go struct from XML.

<a id="zero-trust"></a>
## 零信任

_用于实现零信任架构的库与工具。_

- [Cosign](https://github.com/sigstore/cosign) - Container Signing, Verification and Storage in an OCI registry.
- [in-toto](https://github.com/in-toto/in-toto-golang) - Go implementation of the in-toto (provides a framework to protect the integrity of the software supply chain) python reference implementation.
- [OpenZiti](https://github.com/openziti/ziti) - A full, open source zero trust overlay network. Including numerous SDKs for numerous languages such as [golang](https://github.com/openziti/sdk-golang) allowing you to embed zero trust principles directly into your applications. The [OpenZiti Test Kitchen](https://github.com/openziti-test-kitchen) has numerous examples to draw inspiration from including a [zero trust ssh client - zssh](https://github.com/openziti-test-kitchen/zssh)
- [Spiffe-Vault](https://github.com/philips-labs/spiffe-vault) - Utilizes Spiffe JWT authentication with Hashicorp Vault for secretless authentication.
- [Spire](https://github.com/spiffe/spire) - SPIRE (the SPIFFE Runtime Environment) is a toolchain of APIs for establishing trust between software systems across a wide variety of hosting platforms.

<a id="code-analysis"></a>
## 代码分析

_源代码分析工具，也称静态应用安全测试（SAST）工具。_

- [apicompat](https://github.com/bradleyfalzon/apicompat) - Checks recent changes to a Go project for backwards incompatible changes.
- [ast-metrics](https://github.com/ast-metrics/ast-metrics) - Static code analyzer for Go and other languages: complexity, coupling, cohesion and maintainability metrics, with HTML, JSON, Markdown and SARIF reports.
- [asty](https://github.com/asty-org/asty) - Converts golang AST to JSON and JSON to AST.
- [blanket](https://gitlab.com/verygoodsoftwarenotvirus/blanket) - blanket is a tool that helps you catch functions which don't have direct unit tests in your Go packages.
- [ChainJacking](https://github.com/Checkmarx/chainjacking) - Find which of your Go lang direct GitHub dependencies is susceptible to ChainJacking attack.
- [Chronos](https://github.com/amit-davidson/Chronos) - Detects race conditions statically
- [deadmono](https://github.com/arxeiss/deadmono) - Wrapper around deadcode for detection of dead code in Go monorepo.
- [dupl](https://github.com/mibk/dupl) - Tool for code clone detection.
- [errcheck](https://github.com/kisielk/errcheck) - Errcheck is a program for checking for unchecked errors in Go programs.
- [fatcontext](https://github.com/Crocmagnon/fatcontext) - Fatcontext detects nested contexts in loops or function literals.
- [go-checkstyle](https://github.com/qiniu/checkstyle) - checkstyle is a style check tool like java checkstyle. This tool inspired by java checkstyle, golint. The style referred to some points in Go Code Review Comments.
- [go-cleanarch](https://github.com/roblaszczak/go-cleanarch) - go-cleanarch was created to validate Clean Architecture rules, like a The Dependency Rule and interaction between packages in your Go projects.
- [go-critic](https://github.com/go-critic/go-critic) - source code linter that brings checks that are currently not implemented in other linters.
- [go-mod-outdated](https://github.com/psampaz/go-mod-outdated) - An easy way to find outdated dependencies of your Go projects.
- [goast-viewer](https://github.com/yuroyoro/goast-viewer) - Web based Golang AST visualizer.
- [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports) - Tool to fix (add, remove) your Go imports automatically.
- [golang-ifood-sdk](https://github.com/arxdsilva/golang-ifood-sdk) - iFood API SDK.
- [golangci-lint](https://github.com/golangci/golangci-lint) – A fast Go linters runner. It runs linters in parallel, uses caching, supports `yaml` config, has integrations with all major IDE and has dozens of linters included.
- [golines](https://github.com/segmentio/golines) - Formatter that automatically shortens long lines in Go code.
- [gomarklint](https://github.com/shinagawa-web/gomarklint) - Markdown linter with built-in HTTP link validation, single binary, no Node.js required.
- [GoPlantUML](https://github.com/jfeliu007/goplantuml) - Library and CLI that generates text plantump class diagram containing information about structures and interfaces with the relationship among them.
- [goreturns](https://github.com/sqs/goreturns) - Adds zero-value return statements to match the func return types.
- [gostatus](https://github.com/shurcooL/gostatus) - Command line tool, shows the status of repositories that contain Go packages.
- [lint](https://github.com/surullabs/lint) - Run linters as part of go test.
- [php-parser](https://github.com/z7zmey/php-parser) - A Parser for PHP written in Go.
- [revive](https://github.com/mgechev/revive) – ~6x faster, stricter, configurable, extensible, and beautiful drop-in replacement for `golint`.
- [staticcheck](https://github.com/dominikh/go-tools/tree/master/cmd/staticcheck) - staticcheck is `go vet` on steroids, applying a ton of static analysis checks you might be used to from tools like ReSharper for C#.
- [structalign](https://github.com/peczenyj/structalign) - Shows how a struct's fields could be reordered to use less memory, printing a diff instead of rewriting files.
- [stto](https://github.com/mainak55512/stto) - A light-weight superfast line of code counter written in pure Go.
- [testifylint](https://github.com/Antonboom/testifylint) – A linter that checks usage of [github.com/stretchr/testify](https://github.com/stretchr/testify).
- [tickgit](https://github.com/augmentable-dev/tickgit) - CLI and go package for surfacing code comment TODOs (in any language) and applying a `git blame`to identify the author.
- [todocheck](https://github.com/preslavmihaylov/todocheck) - Static code analyser which links TODO comments in code with issues in your issue tracker.
- [unconvert](https://github.com/mdempsky/unconvert) - Remove unnecessary type conversions from Go source.
- [usestdlibvars](https://github.com/sashamelentyev/usestdlibvars) - A linter that detect the possibility to use variables/constants from the Go standard library.
- [vacuum](https://github.com/daveshanley/vacuum) - An ultra-super-fast, lightweight OpenAPI linter and quality checking tool.
- [validate](https://github.com/mccoyst/validate) - Automatically validates struct fields with tags.
- [wrapcheck](https://github.com/tomarrell/wrapcheck) - A linter to check that errors from external packages are wrapped.

**[⬆ 回到顶部](#contents)**

<a id="editor-plugins"></a>
## 编辑器插件

_面向文本编辑器与 IDE 的插件。_

- [coc-go language server extension for Vim/Neovim](https://github.com/josa42/coc-go) - This plugin adds [gopls](https://github.com/golang/tools/blob/master/gopls/README.md) features to Vim/Neovim.
- [Go Doc](https://github.com/msyrus/vscode-go-doc) - A Visual Studio Code extension for showing definition in output and generating go doc.
- [Go plugin for JetBrains IDEs](https://plugins.jetbrains.com/plugin/9568-go) - Go plugin for JetBrains IDEs.
- [go-mode](https://github.com/dominikh/go-mode.el) - Go mode for GNU/Emacs.
- [gocode](https://github.com/nsf/gocode) - Autocompletion daemon for the Go programming language.
- [goimports-reviser](https://github.com/incu6us/goimports-reviser) - Formatting tool for imports.
- [goprofiling](https://marketplace.visualstudio.com/items?itemName=MaxMedia.go-prof) - This extension adds benchmark profiling support for the Go language to VS Code.
- [GoSublime](https://github.com/DisposaBoy/GoSublime) - Golang plugin collection for the text editor SublimeText 3 providing code completion and other IDE-like features.
- [gounit-vim](https://github.com/hexdigest/gounit-vim) - Vim plugin for generating Go tests based on the function's or method's signature.
- [vim-compiler-go](https://github.com/rjohnsondev/vim-compiler-go) - Vim plugin to highlight syntax errors on save.
- [vim-go](https://github.com/fatih/vim-go) - Go development plugin for Vim.
- [vscode-go](https://github.com/golang/vscode-go) - Extension for Visual Studio Code (VS Code) which provides support for the Go language.
- [Watch](https://github.com/eaburns/Watch) - Runs a command in an acme win on file changes.

**[⬆ 回到顶部](#contents)**

<a id="go-generate-tools"></a>
## Go Generate 工具

- [envdoc](https://github.com/g4s8/envdoc) - generate documentation for environment variables from Go source files.
- [generic](https://github.com/usk81/generic) - flexible data type for Go.
- [gocontracts](https://github.com/Parquery/gocontracts) - brings design-by-contract to Go by synchronizing the code with the documentation.
- [godal](https://github.com/mafulong/godal) - Generate orm models corresponding to golang by specifying sql ddl file, which can be used by gorm.
- [gonerics](https://github.com/bouk/gonerics) - Idiomatic Generics in Go.
- [gotests](https://github.com/cweill/gotests) - Generate Go tests from your source code.
- [gounit](https://github.com/hexdigest/gounit) - Generate Go tests using your own templates.
- [hasgo](https://github.com/DylanMeeus/hasgo) - Generate Haskell inspired functions for your slices.
- [oapixconstgen](https://github.com/psyb0t/oapixconstgen) - Generate typed Go constants from an OpenAPI spec's x-constants extension.
- [options-gen](https://github.com/kazhuravlev/options-gen) - Functional options described by Dave Cheney's post "Functional options for friendly APIs".
- [re2dfa](https://gitlab.com/opennota/re2dfa) - Transform regular expressions into finite state machines and output Go source code.
- [sqlgen](https://github.com/anqiansong/sqlgen) - Generate gorm, xorm, sqlx, bun, sql code from SQL file or DSN.
- [TOML-to-Go](https://xuri.me/toml-to-go) - Translates TOML into a Go type in the browser instantly.
- [xgen](https://github.com/xuri/xgen) - XSD (XML Schema Definition) parser and Go/C/Java/Rust/TypeScript code generator.

**[⬆ 回到顶部](#contents)**

<a id="go-tools"></a>
## Go 工具

- [decouple](https://github.com/bobg/decouple) - Find “overspecified” function parameters that could be generalized with interface types.
- [docs](https://github.com/go-oas/docs) - Automatically generate RESTful API documentation for GO projects - aligned with Open API Specification standard.
- [go-callvis](https://github.com/TrueFurby/go-callvis) - Visualize call graph of your Go program using dot format.
- [go-size-analyzer](https://github.com/Zxilly/go-size-analyzer) - Analyze and visualize the size of dependencies in compiled Golang binaries, providing insight into their impact on the final build.
- [go-swagger](https://github.com/go-swagger/go-swagger) - Swagger 2.0 implementation for go. Swagger is a simple yet powerful representation of your RESTful API.
- [go-template-playground](https://bartventer.github.io/go-template-playground/) - An interactive environment to create and test Go templates.
- [godbg](https://github.com/tylerwince/godbg) - Implementation of Rusts `dbg!` macro for quick and easy debugging during development.
- [gofindimpl](https://github.com/psyb0t/gofindimpl) - Find all structs that implement a given Go interface across a codebase.
- [gomodrun](https://github.com/dustinblackman/gomodrun/) - Go tool that executes and caches binaries included in go.mod files.
- [gotemplate.io](https://gotemplate.io/) - Online tool to preview `text/template` templates live.
- [gotestdox](https://github.com/bitfield/gotestdox) - Show Go test results as readable sentences.
- [gothanks](https://github.com/psampaz/gothanks) - GoThanks automatically stars your go.mod github dependencies, sending this way some love to their maintainers.
- [gotutor](https://github.com/ahmedakef/gotutor) - Online Go Debugger & Visualizer.
- [govisual](https://github.com/doganarif/govisual) - Zero-config, pure-Go HTTP request visualizer & debugger for local Go web development.
- [igo](https://github.com/rocketlaunchr/igo) - An igo to go transpiler (new language features for Go language!)
- [lensm](https://github.com/loov/lensm) - Go assembly and source viewer.
- [modver](https://github.com/bobg/modver) - Compare two versions of a Go module to check the version-number change required (major, minor, or patchlevel), according to [semver](https://semver.org/) rules.
- [MoniGO](https://github.com/iyashjayesh/monigo) - A performance monitoring library for Go applications. It provides real-time insights into application performance! 🚀
- [OctoLinker](https://github.com/OctoLinker/browser-extension) - Navigate through go files efficiently with the OctoLinker browser extension for GitHub.
- [richgo](https://github.com/kyoh86/richgo) - Enrich `go test` outputs with text decorations.
- [roumon](https://github.com/becheran/roumon) - Monitor current state of all active goroutines via a command line interface.
- [rts](https://github.com/galeone/rts) - RTS: response to struct. Generates Go structs from server responses.
- [textra](https://github.com/ravsii/textra) - Extract Go struct field names, types and tags for filtering and exporting.
- [typex](https://github.com/dtgorski/typex) - Examine Go types and their transitive dependencies, alternatively export results as TypeScript value objects (or types) declaration.

**[⬆ 回到顶部](#contents)**

<a id="software-packages"></a>
## 软件包

_使用 Go 编写的软件。_

**[⬆ 回到顶部](#contents)**

<a id="devops-tools"></a>
### DevOps 工具

- [abbreviate](https://github.com/dnnrly/abbreviate) - abbreviate is a tool turning long strings in to shorter ones with configurable separators, for example to embed branch names in to deployment stack IDs.
- [alaz](https://github.com/ddosify/alaz) - Effortless, Low-Overhead, eBPF-based Kubernetes Monitoring.
- [aptly](https://github.com/aptly-dev/aptly) - aptly is a Debian repository management tool.
- [aurora](https://github.com/xuri/aurora) - Cross-platform web-based Beanstalkd queue server console.
- [aws-doctor](https://github.com/elC0mpa/aws-doctor) - Diagnose AWS costs, detect idle resources, and optimize cloud spending directly from your terminal 🩺 ☁️.
- [awsenv](https://github.com/soniah/awsenv) - Small binary that loads Amazon (AWS) environment variables for a profile.
- [Balerter](https://github.com/balerter/balerter) - A self-hosted script-based alerting manager.
- [Blast](https://github.com/dave/blast) - A simple tool for API load testing and batch jobs.
- [bombardier](https://github.com/codesenberg/bombardier) - Fast cross-platform HTTP benchmarking tool.
- [cassowary](https://github.com/rogerwelin/cassowary) - Modern cross-platform HTTP load-testing tool written in Go.
- [chaosmonkey](https://github.com/Netflix/chaosmonkey) - A resiliency tool that helps applications tolerate random instance failures.
- [colima](https://github.com/abiosoft/colima) - Container runtimes on macOS (and Linux) with minimal setup.
- [Ddosify](https://github.com/ddosify/ddosify) - High-performance load testing tool, written in Golang.
- [decompose](https://github.com/s0rg/decompose) - tool to generate and process Docker containers connections graphs.
- [Den](https://github.com/us/den) - Self-hosted sandbox runtime for AI agents. Open-source E2B alternative.
- [DepCharge](https://github.com/centerorbit/depcharge) - Helps orchestrating the execution of commands across the many dependencies in larger projects.
- [dish](https://github.com/thevxn/dish) - A lightweight, remotely configurable monitoring service.
- [Docker](https://www.docker.com/) - Open platform for distributed applications for developers and sysadmins.
- [docker-go-mingw](https://github.com/x1unix/docker-go-mingw) - Docker image for building Go binaries for Windows with MinGW toolchain.
- [docker-volume-backup](https://github.com/offen/docker-volume-backup) - Backup Docker volumes locally or to any S3, WebDAV, Azure Blob Storage, Dropbox or SSH compatible storage.
- [Dockerfile-Generator](https://github.com/ozankasikci/dockerfile-generator) - A go library and an executable that produces valid Dockerfiles using various input channels.
- [docklite](https://github.com/benzjeremy/docklite) - Lightweight Portainer alternative for Docker container management with real-time SSE metrics.
- [dogo](https://github.com/liudng/dogo) - Monitoring changes in the source file and automatically compile and run (restart).
- [drone-jenkins](https://github.com/appleboy/drone-jenkins) - Trigger downstream Jenkins jobs using a binary, docker or Drone CI.
- [drone-scp](https://github.com/appleboy/drone-scp) - Copy files and artifacts via SSH using a binary, docker or Drone CI.
- [Dropship](https://github.com/chrismckenzie/dropship) - Tool for deploying code via cdn.
- [easyssh-proxy](https://github.com/appleboy/easyssh-proxy) - Golang package for easy remote execution through SSH and SCP downloading via `ProxyCommand`.
- [fac](https://github.com/mkchoi212/fac) - Command-line user interface to fix git merge conflicts.
- [Flannel](https://github.com/flannel-io/flannel) - Flannel is a network fabric for containers, designed for Kubernetes.
- [Fleet device management](https://github.com/fleetdm/fleet) - Lightweight, programmable telemetry for servers and workstations.
- [gaia](https://github.com/gaia-pipeline/gaia) - Build powerful pipelines in any programming language.
- [ghorg](https://github.com/gabrie30/ghorg) - Quickly clone an entire org/users repositories into one directory - Supports GitHub, GitLab, Gitea, and Bitbucket.
- [Gitea](https://github.com/go-gitea/gitea) - Fork of Gogs, entirely community driven.
- [gitea-github-migrator](https://git.jonasfranz.software/JonasFranzDEV/gitea-github-migrator) - Migrate all your GitHub repositories, issues, milestones and labels to your Gitea instance.
- [gitl](https://github.com/akomyagin/gitl) - AI review of git commit ranges with risk scoring (low/medium/high), changelog generation, and multi-repo activity digest. GitHub Action included.
- [go-furnace](https://github.com/go-furnace/go-furnace) - Hosting solution written in Go. Deploy your Application with ease on AWS, GCP or DigitalOcean.
- [go-rocket-update](https://github.com/mouuff/go-rocket-update) - A simple way to make self updating Go applications - Supports Github and Gitlab.
- [go-selfupdate](https://github.com/sanbornm/go-selfupdate) - Enable your Go applications to self update.
- [gobrew](https://github.com/cryptojuice/gobrew) - gobrew lets you easily switch between multiple versions of go.
- [gobrew](https://github.com/kevincobain2000/gobrew) - Go version manager. Super simple tool to install and manage Go versions. Install go without root. Gobrew doesn't require shell rehash.
- [godbg](https://github.com/sirnewton01/godbg) - Web-based gdb front-end application.
- [Gogs](https://gogs.io/) - A Self Hosted Git Service in the Go Programming Language.
- [goma-gateway](https://github.com/jkaninda/goma-gateway) - A Lightweight API Gateway and Reverse Proxy with declarative config, robust middleware, and support for REST, GraphQL, TCP, UDP, and gRPC.
- [gonative](https://github.com/inconshreveable/gonative) - Tool which creates a build of Go that can cross compile to all platforms while still using the Cgo-enabled versions of the stdlib packages.
- [govvv](https://github.com/ahmetalpbalkan/govvv) - “go build” wrapper to easily add version information into Go binaries.
- [grapes](https://github.com/yaronsumel/grapes) - Lightweight tool designed to distribute commands over ssh with ease.
- [GVM](https://github.com/moovweb/gvm) - GVM provides an interface to manage Go versions.
- [Hey](https://github.com/rakyll/hey) - Hey is a tiny program that sends some load to a web application.
- [httpref](https://github.com/dnnrly/httpref) - httpref is a handy CLI reference for HTTP methods, status codes, headers, and TCP and UDP ports.
- [jcli](https://github.com/jenkins-zh/jenkins-cli) - Jenkins CLI allows you manage your Jenkins as an easy way.
- [k0s](https://github.com/k0sproject/k0s) - Zero Friction Kubernetes distribution.
- [k3d](https://github.com/k3d-io/k3d) - Little helper to run CNCF's k3s in Docker.
- [k3s](https://github.com/k3s-io/k3s) - Lightweight Kubernetes.
- [k6](https://github.com/grafana/k6) - A modern load testing tool, using Go and JavaScript.
- [k9s](https://github.com/derailed/k9s) - Kubernetes CLI to manage your clusters in style.
- [kala](https://github.com/ajvb/kala) - Simplistic, modern, and performant job scheduler.
- [kcli](https://github.com/cswank/kcli) - Command line tool for inspecting kafka topics/partitions/messages.
- [kepfi](https://github.com/Knuspii/kepfi) - A smart alternative to rm with a recovery bin and storage tracking.
- [kind](https://github.com/kubernetes-sigs/kind) - Kubernetes IN Docker - local clusters for testing Kubernetes.
- [ko](https://github.com/google/ko) - Command line tool for building and deploying Go applications on Kubernetes
- [kool](https://github.com/kool-dev/kool) - Command line tool for managing Docker environments as an easy way.
- [kubeblocks](https://github.com/apecloud/kubeblocks) - KubeBlocks is an open-source control plane that runs and manages databases, message queues and other data infrastructure on K8s.
- [kubefwd](https://github.com/txn2/kubefwd) - Bulk Kubernetes port forwarding with unique IPs per service for local development.
- [kubernetes](https://github.com/kubernetes/kubernetes) - Container Cluster Manager from Google.
- [kubeshark](https://github.com/kubeshark/kubeshark) - API traffic analyzer for Kubernetes, inspired by Wireshark, purposely built for Kubernetes.
- [KubeVela](https://github.com/kubevela/kubevela) - Cloud native application delivery.
- [KubeVPN](https://github.com/kubenetworks/kubevpn) - KubeVPN offers a Cloud-Native Dev Environment that seamlessly connects to your Kubernetes cluster network.
- [KusionStack](https://github.com/KusionStack/kusion) - A unified programmable configuration techstack to deliver modern app in 'platform as code' and 'infra as code' approach.
- [kwatch](https://github.com/abahmed/kwatch) - Monitor & detect crashes in your Kubernetes(K8s) cluster instantly.
- [lstags](https://github.com/ivanilves/lstags) - Tool and API to sync Docker images across different registries.
- [lwc](https://github.com/timdp/lwc) - A live-updating version of the UNIX wc command.
- [manssh](https://github.com/xwjdsh/manssh) - manssh is a command line tool for managing your ssh alias config easily.
- [Mantil](https://github.com/mantil-io/mantil) - Go specific framework for building serverless applications on AWS that enables you to focus on pure Go code while Mantil takes care of the infrastructure.
- [minikube](https://github.com/kubernetes/minikube) - Run Kubernetes locally.
- [Moby](https://github.com/moby/moby) - Collaborative project for the container ecosystem to assemble container-based systems.
- [Mora](https://github.com/emicklei/mora) - REST server for accessing MongoDB documents and meta data.
- [mq-studio](https://github.com/amigoer/mq-studio) - Cross-platform desktop client for managing and monitoring RocketMQ, RabbitMQ, Kafka, Pulsar, Redis Stream, MQTT, NATS, and ActiveMQ clusters.
- [ostent](https://github.com/ostrost/ostent) - collects and displays system metrics and optionally relays to Graphite and/or InfluxDB.
- [Packer](https://github.com/mitchellh/packer) - Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.
- [Pewpew](https://github.com/bengadbois/pewpew) - Flexible HTTP command line stress tester.
- [pingtower](https://github.com/crleonard/pingtower) - Lightweight self-hosted uptime monitor for websites and APIs.
- [PipeCD](https://github.com/pipe-cd/pipecd) - A GitOps-style continuous delivery platform that provides consistent deployment and operations experience for any applications.
- [podinfo](https://github.com/stefanprodan/podinfo) - Podinfo is a tiny web application made with Go that showcases best practices of running microservices in Kubernetes. Podinfo is used by CNCF projects like Flux and Flagger for end-to-end testing and workshops.
- [podman-tui](https://github.com/containers/podman-tui) - Terminal UI for Podman management.
- [Pomerium](https://github.com/pomerium/pomerium) - Pomerium is an identity-aware access proxy.
- [Rodent](https://github.com/alouche/rodent) - Rodent helps you manage Go versions, projects and track dependencies.
- [s3-proxy](https://github.com/oxyno-zeta/s3-proxy) - S3 Proxy with GET, PUT and DELETE methods and authentication (OpenID Connect and Basic Auth).
- [s3gof3r](https://github.com/rlmcpherson/s3gof3r) - Small utility/library optimized for high speed transfer of large objects into and out of Amazon S3.
- [s5cmd](https://github.com/peak/s5cmd) - Blazing fast S3 and local filesystem execution tool.
- [Scaleway-cli](https://github.com/scaleway/scaleway-cli) - Manage BareMetal Servers from Command Line (as easily as with Docker).
- [script](https://github.com/bitfield/script) - Making it easy to write shell-like scripts in Go for DevOps and system administration tasks.
- [sg](https://github.com/ChristopherRabotin/sg) - Benchmarks a set of HTTP endpoints (like ab), with possibility to use the response code and data between each call for specific server stress based on its previous response.
- [sigma](https://github.com/go-sigma/sigma) - OCI-native container image registry, support OCI-native artifact, scan artifact, image build etc.
- [skm](https://github.com/TimothyYe/skm) - SKM is a simple and powerful SSH Keys Manager, it helps you to manage your multiple SSH keys easily!
- [sortie](https://github.com/sortie-ai/sortie) - Turn tracker tickets into autonomous coding agent sessions.
- [StatusOK](https://github.com/sanathp/statusok) - Monitor your Website and REST APIs.Get Notified through Slack, E-mail when your server is down or response time is more than expected.
- [tau](https://github.com/taubyte/tau) - Easily build Cloud Computing Platforms with features like Serverless WebAssembly Functions, Frontend Hosting, CI/CD, Object Storage, K/V Database, and Pub-Sub Messaging.
- [terraform-provider-openapi](https://github.com/dikhan/terraform-provider-openapi) - Terraform provider plugin that dynamically configures itself at runtime based on an OpenAPI document (formerly known as swagger file) containing the definitions of the APIs exposed.
- [tf-profile](https://github.com/datarootsio/tf-profile) - Profiler for Terraform runs. Generate global stats, resource-level stats or visualizations.
- [tickstem/uptime](https://github.com/tickstem/uptime) - Go client for HTTP uptime monitoring with SSL expiry alerts and configurable response assertions.
- [tlm](https://github.com/yusufcanb/tlm) - Local cli copilot, powered by CodeLLaMa
- [traefik](https://github.com/containous/traefik) - Reverse proxy and load balancer with support for multiple backends.
- [trubka](https://github.com/xitonix/trubka) - A CLI tool to manage and troubleshoot Apache Kafka clusters with the ability of generically publishing/consuming protocol buffer and plain text events to/from Kafka.
- [Updatecli](https://github.com/updatecli/updatecli) - A universal declarative update policy engine.
- [uTask](https://github.com/ovh/utask) - Automation engine that models and executes business processes declared in yaml.
- [Vegeta](https://github.com/tsenart/vegeta) - HTTP load testing tool and library. It's over 9000!
- [wait-for](https://github.com/dnnrly/wait-for) - Wait for something to happen (from the command line) before continuing. Easy orchestration of Docker services and other things.
- [Wide](https://wide.b3log.org/login) - Web-based IDE for Teams using Golang.
- [winrm-cli](https://github.com/masterzen/winrm-cli) - Cli tool to remotely execute commands on Windows machines.
- [zerohand](https://github.com/nilpoona/zerohand) - A simple and efficient load testing tool for Web APIs.

**[⬆ 回到顶部](#contents)**

<a id="other-software"></a>
### 其他软件

- [Backrest](https://github.com/garethgeorge/backrest) - Web-based UI and orchestrator for restic backup.
- [Better Go Playground](https://goplay.tools) - Go playground with syntax highlight, code completion and other features.
- [blocky](https://github.com/0xERR0R/blocky) - Fast and lightweight DNS proxy as ad-blocker for local network with many features.
- [bluetuith](https://github.com/bluetuith-org/bluetuith) - TUI Bluetooth manager for Linux.
- [borg](https://github.com/crufter/borg) - Terminal based search engine for bash snippets.
- [boxed](https://github.com/tejo/boxed) - Dropbox based blog engine.
- [Chapar](https://github.com/chapar-rest/chapar) - Chapar is a cross-platform Postman alternative built with go, aims to help developers to test their api endpoints. it support http and grpc protocols.
- [Cherry](https://github.com/rafael-santiago/cherry) - Tiny webchat server in Go.
- [chicha-isotope-map](https://github.com/matveynator/chicha-isotope-map) - Self-hosted public radiation map for importing, analyzing, and visualizing measurement tracks.
- [Circuit](https://github.com/gocircuit/circuit) - Circuit is a programmable platform-as-a-service (PaaS) and/or Infrastructure-as-a-Service (IaaS), for management, discovery, synchronization and orchestration of services and hosts comprising cloud applications.
- [Comcast](https://github.com/tylertreat/Comcast) - Simulate bad network connections.
- [confd](https://github.com/kelseyhightower/confd) - Manage local application configuration files using templates and data from etcd or consul.
- [crawley](https://github.com/s0rg/crawley) - Web scraper/crawler for cli.
- [croc](https://github.com/schollz/croc) - Easily and securely send files or folders from one computer to another.
- [CrunchyCleaner](https://github.com/Knuspii/CrunchyCleaner) - A lightweight, software cache cleanup tool for Windows & Linux.
- [dispositio](https://github.com/tsraveling/dispositio) - Terminal tool for planning large projects in simple markdown.
- [Documize](https://github.com/documize/community) - Modern wiki software that integrates data from SaaS tools.
- [dp](https://github.com/scryinfo/dp) - Through SDK for data exchange with blockchain, developers can get easy access to DAPP development.
- [drive](https://github.com/odeke-em/drive) - Google Drive client for the commandline.
- [Duplicacy](https://github.com/gilbertchen/duplicacy) - A cross-platform network and cloud backup tool based on the idea of lock-free deduplication.
- [fjira](https://github.com/mk-5/fjira) - A fuzzy-search based terminal UI application for Attlasian Jira
- [Gebug](https://github.com/moshebe/gebug) - A tool that makes debugging of Dockerized Go applications super easy by enabling Debugger and Hot-Reload features, seamlessly.
- [gfile](https://github.com/Antonito/gfile) - Securely transfer files between two computers, without any third party, over WebRTC.
- [Go Package Store](https://github.com/shurcooL/Go-Package-Store) - App that displays updates for the Go packages in your GOPATH.
- [go-peerflix](https://github.com/Sioro-Neoku/go-peerflix) - Video streaming torrent client.
- [goblin](https://goblin.run) - Cloud builder for CLI's written in go lang
- [GoBoy](https://github.com/Humpheh/goboy) - Nintendo Game Boy Color emulator written in Go.
- [gocc](https://github.com/goccmack/gocc) - Gocc is a compiler kit for Go written in Go.
- [GoDocTooltip](https://github.com/diankong/GoDocTooltip) - Chrome extension for Go Doc sites, which shows function description as tooltip at function list.
- [Gokapi](https://github.com/Forceu/gokapi) - Lightweight server to share files, which expire after a set amount of downloads or days. Similar to Firefox Send, but without public upload.
- [GoLand](https://jetbrains.com/go) - Full featured cross-platform Go IDE.
- [GoNB](https://github.com/janpfeifer/gonb) - Interactive Go programming with Jupyter Notebooks (also works in VSCode, Binder and Google's Colab).
- [GooseForum](https://github.com/leancodebox/GooseForum) - Self-hosted forum platform built with Go, Vue, and Tailwind CSS.
- [Gor](https://github.com/buger/gor) - Http traffic replication tool, for replaying traffic from production to stage/dev environments in real-time.
- [Guora](https://github.com/meloalright/guora) - A self-hosted Quora like web application written in Go.
- [GURL](https://github.com/matveynator/gurl) - When CURL says your SSL library is too old — use GURL. One file. Zero SSL dependencies.
- [hoofli](https://github.com/dnnrly/hoofli) - Generate PlantUML diagrams from Chrome or Firefox network inspections.
- [hotswap](https://github.com/edwingeng/hotswap) - A complete solution to reload your go code without restarting your server, interrupting or blocking any ongoing procedure.
- [hugo](https://gohugo.io/) - Fast and Modern Static Website Engine.
- [ide](https://github.com/thestrukture/ide) - Browser accessible IDE. Designed for Go with Go.
- [joincap](https://github.com/assafmo/joincap) - Command-line utility for merging multiple pcap files together.
- [JuiceFS](https://github.com/juicedata/juicefs) - Distributed POSIX file system built on top of Redis and AWS S3.
- [Juju](https://jujucharms.com/) - Cloud-agnostic service deployment and orchestration - supports EC2, Azure, Openstack, MAAS and more.
- [KeibiDrop](https://github.com/KeibiSoft/KeibiDrop) - On-demand peer-to-peer filesystem that mounts a remote folder and hides link latency with read-ahead, end-to-end encrypted with hybrid X25519 and ML-KEM-1024.
- [Layli](https://layli.app) - Draw pretty layout diagrams as code.
- [Leaps](https://github.com/jeffail/leaps) - Pair programming service using Operational Transforms.
- [lgo](https://github.com/yunabe/lgo) - Interactive Go programming with Jupyter. It supports code completion, code inspection and 100% Go compatibility.
- [LightCMS](https://github.com/jonradoff/lightcms) - Self-hosted content management system with static page generation, role-based access control, and an MCP server for agent-driven content operations.
- [limetext](https://limetext.github.io) - Lime Text is a powerful and elegant text editor primarily developed in Go that aims to be a Free and open-source software successor to Sublime Text.
- [LiteIDE](https://github.com/visualfc/liteide) - LiteIDE is a simple, open source, cross-platform Go IDE.
- [mac-cleanup-go](https://github.com/2ykwang/mac-cleanup-go) - Preview-first TUI for cleaning macOS caches, logs, and temporary files.
- [mdv](https://github.com/Allra-Fintech/mdv) - CLI tool that renders Markdown files in the browser with live reload, GFM, syntax highlighting, Mermaid diagrams, and PDF export.
- [mockingjay](https://github.com/quii/mockingjay-server) - Fake HTTP servers and consumer driven contracts from one configuration file. You can also make the server randomly misbehave to help do more realistic performance tests.
- [myLG](https://github.com/mehrdadrad/mylg) - Command Line Network Diagnostic tool written in Go.
- [naclpipe](https://github.com/unix4fun/naclpipe) - Simple NaCL EC25519 based crypto pipe tool written in Go.
- [Neo-cowsay](https://github.com/Code-Hex/Neo-cowsay) - 🐮 cowsay is reborn. for a New Era.
- [nes](https://github.com/fogleman/nes) - Nintendo Entertainment System (NES) emulator written in Go.
- [onWatch](https://github.com/onllm-dev/onWatch) - Monitor AI API quotas across providers locally with historical tracking, alerts, and a web dashboard to avoid surprise throttling and budget overruns.
- [Orbit](https://github.com/gulien/orbit) - A simple tool for running commands and generating files from templates.
- [peg](https://github.com/pointlander/peg) - Peg, Parsing Expression Grammar, is an implementation of a Packrat parser generator.
- [Plakar](https://github.com/PlakarKorp/plakar) - An encrypted, deduplicated, verifiable, and scalable backup engine with no vendor lock-in.
- [Plik](https://github.com/root-gg/plik) - Plik is a temporary file upload system (Wetransfer like) in Go.
- [portal](https://github.com/SpatiumPortae/portal) - Portal is a quick and easy command-line file transfer utility from any computer to another.
- [restic](https://github.com/restic/restic) - De-duplicating backup program.
- [sake](https://github.com/alajmo/sake) - sake is a command runner for local and remote hosts.
- [scc](https://github.com/boyter/scc) - Sloc Cloc and Code, a very fast accurate code counter with complexity calculations and COCOMO estimates.
- [ScheduleGate](https://github.com/gjunqueira-sys/ScheduleGate) - DCMA 14-point schedule assessment CLI for MS Project Excel/CSV exports.
- [Seaweed File System](https://github.com/chrislusf/seaweedfs) - Fast, Simple and Scalable Distributed File System with O(1) disk seek.
- [shell2http](https://github.com/msoap/shell2http) - Executing shell commands via http server (for prototyping or remote control).
- [Snitch](https://github.com/lucasgomide/snitch) - Simple way to notify your team and many tools when someone has deployed any application via Tsuru.
- [sonic](https://github.com/go-sonic/sonic) - Sonic is a Go Blogging Platform. Simple and Powerful.
- [spotify-screensaver](https://github.com/benzjeremy/spotify-screensaver) - Desktop screensaver for Spotify with digital OLED clock, canvas audio visualizer, and MPRIS controls.
- [Stack Up](https://github.com/pressly/sup) - Stack Up, a super simple deployment tool - just Unix - think of it like 'make' for a network of servers.
- [stew](https://github.com/marwanhawari/stew) - An independent package manager for compiled binaries.
- [syncthing](https://syncthing.net/) - Open, decentralized file synchronization tool and protocol.
- [tcpdog](https://github.com/mehrdadrad/tcpdog) - eBPF based TCP observability.
- [tinycare-tui](https://github.com/DMcP89/tinycare-tui) - Small terminal app that shows git commits from the last 24 hours and week, current weather, some self care advice, a joke, and you current todo list tasks.
- [tldx](https://github.com/brandonyoungdev/tldx) - Bulk domain availability checker using RDAP, DNS, and WHOIS fallback with keyword permutation generation.
- [toxiproxy](https://github.com/shopify/toxiproxy) - Proxy to simulate network and system conditions for automated tests.
- [tsuru](https://tsuru.io/) - Extensible and open source Platform as a Service software.
- [vaku](https://github.com/lingrino/vaku) - CLI & API for folder-based functions in Vault like copy, move, and search.
- [vFlow](https://github.com/VerizonDigital/vflow) - High-performance, scalable and reliable IPFIX, sFlow and Netflow collector.
- [untis-go](https://github.com/benzjeremy/untis-go) - Fast, native WebUntis desktop client for students and teachers. Sidebar navigation, timetables, homework, absences & messages. AES-256-GCM encrypted credentials, SQLite cache-first, random port security.
- [Wave Terminal](https://waveterm.dev) - Wave is an open-source, AI-native terminal built for seamless developer workflows with inline rendering, a modern UI, and persistent sessions.
- [wellington](https://github.com/wellington/wellington) - Sass project management tool, extends the language with sprite functions (like Compass).
- [woke](https://github.com/get-woke/woke) - Detect non-inclusive language in your source code.
- [yai](https://github.com/ekkinox/yai) - AI powered terminal assistant.
- [zs](https://git.mills.io/prologic/zs) - an extremely minimal static site generator.

**[⬆ 回到顶部](#contents)**

<a id="resources"></a>
# 相关资源

_发现新 Go 库的地方。_

**[⬆ 回到顶部](#contents)**

<a id="benchmarks"></a>
## 性能基准测试

- [autobench](https://github.com/davecheney/autobench) - Framework to compare the performance between different Go versions.
- [go-benchmark-app](https://github.com/mrLSD/go-benchmark-app) - Powerful HTTP-benchmark tool mixed with Аb, Wrk, Siege tools. Gathering statistics and various parameters for benchmarks and comparison results.
- [go-benchmarks](https://github.com/tylertreat/go-benchmarks) - Few miscellaneous Go microbenchmarks. Compare some language features to alternative approaches.
- [go-http-routing-benchmark](https://github.com/julienschmidt/go-http-routing-benchmark) - Go HTTP request router benchmark and comparison.
- [go-json-benchmark](https://github.com/zerosnake0/go-json-benchmark) - Go JSON benchmark.
- [go-ml-benchmarks](https://github.com/nikolaydubina/go-ml-benchmarks) - benchmarks for machine learning inference in Go.
- [go-web-framework-benchmark](https://github.com/smallnest/go-web-framework-benchmark) - Go web framework benchmark.
- [go_serialization_benchmarks](https://github.com/alecthomas/go_serialization_benchmarks) - Benchmarks of Go serialization methods.
- [gocostmodel](https://github.com/PuerkitoBio/gocostmodel) - Benchmarks of common basic operations for the Go language.
- [golang-benchmarks](https://github.com/SimonWaldherr/golang-benchmarks) - a collection of golang benchmarks.
- [gospeed](https://github.com/feyeleanor/GoSpeed) - Go micro-benchmarks for calculating the speed of language constructs.
- [kvbench](https://github.com/jimrobinson/kvbench) - Key/Value database benchmark.
- [skynet](https://github.com/atemerev/skynet) - Skynet 1M threads microbenchmark.
- [speedtest-resize](https://github.com/fawick/speedtest-resize) - Compare various Image resize algorithms for the Go language.
- [vizb](https://github.com/goptics/vizb) - A CLI tool to visualize Go benchmark data in 4D.

**[⬆ 回到顶部](#contents)**

<a id="conferences"></a>
## 会议

- [GoCon](https://gocon.connpass.com/) - Tokyo, Japan.
- [GoDays](https://www.godays.io/) - Berlin, Germany.
- [GoLab](https://golab.io/) - Florence, Italy.
- [GopherCon](https://www.gophercon.com/) - Varied Locations Each Year, USA.
- [GopherCon Africa](https://gophercon.africa/) - Nairobi, Kenya.
- [GopherCon Australia](https://gophercon.com.au/) - Sydney, Australia.
- [GopherCon Brazil](https://gopherconbr.org) - Florianópolis, Brazil.
- [GopherCon China](https://gophercon.com.cn) - Shanghai, China.
- [GopherCon Europe](https://gophercon.eu/) - Berlin, Germany.
- [GopherCon India](https://gopherconindia.org/) - Pune, India.
- [GopherCon Israel](https://www.gophercon.org.il/) - Tel Aviv, Israel.
- [GopherCon Russia](https://www.gophercon-russia.ru) - Moscow, Russia.
- [GopherCon Singapore](https://gophercon.sg) - Mapletree Business City, Singapore.
- [GopherCon UK](https://www.gophercon.co.uk/) - London, UK.
- [GopherCon Vietnam](https://gophercon.vn/) - Ho Chi Minh City, Vietnam.
- [GoWest Conference](https://www.gowestconf.com/) - Lehi, USA.

**[⬆ 回到顶部](#contents)**

<a id="e-books"></a>
## 电子书

<a id="e-books-for-purchase"></a>
### 付费电子书

- [100 Go Mistakes: How to Avoid Them](https://www.manning.com/books/100-go-mistakes-how-to-avoid-them)
- [Black Hat Go](https://nostarch.com/blackhatgo) - Go programming for hackers and pentesters.
- [Build an Orchestrator in Go](https://www.manning.com/books/build-an-orchestrator-in-go)
- [Continuous Delivery in Go](https://www.manning.com/books/continuous-delivery-in-go) - This practical guide to continuous delivery shows you how to rapidly establish an automated pipeline that will improve your testing, code quality, and final product.
- [Creative DIY Microcontroller Project With TinyGo and WebAssembly](https://www.packtpub.com/product/creative-diy-microcontroller-projects-with-tinygo-and-webassembly/9781800560208) - An introduction into the TinyGo compiler with projects involving Arduino and WebAssembly.
- [Effective Go: Elegant, efficient, and testable code](https://www.manning.com/books/effective-go) - Unlock Go’s unique perspective on program design, and start writing simple, maintainable, and testable Go code.
- [For the Love of Go](https://bitfieldconsulting.com/books/love) - An introductory book for Go beginners.
- [Go in Practice, Second Edition](https://www.manning.com/books/go-in-practice-second-edition) - Your practical guide on the ins-and-outs of Go development, covering the standard library and the most important tools from Go’s powerful ecosystem.
- [Know Go: Generics](https://bitfieldconsulting.com/books/generics) - A guide to understanding and using generics in Go.
- [Lets-Go](https://lets-go.alexedwards.net) - A step-by-step guide to creating fast, secure and maintanable web applications with Go.
- [Lets-Go-Further](https://lets-go-further.alexedwards.net) - Advanced patterns for building APIs and web applications in Go.
- [The Power of Go: Tests](https://bitfieldconsulting.com/books/tests) - A guide to testing in Go.
- [The Power of Go: Tools](https://bitfieldconsulting.com/books/tools) - A guide to writing command-line tools in Go.
- [Writing A Compiler In Go](https://compilerbook.com)
- [Writing An Interpreter In Go](https://interpreterbook.com) - Book that introduces dozens of techniques for writing idiomatic, expressive, and efficient Go code that avoids common pitfalls.

<a id="free-e-books"></a>
### 免费电子书

- [A Go Developer's Notebook](https://leanpub.com/GoNotebook/read)
- [An Introduction to Programming in Go](http://www.golang-book.com/)
- [Build a blockchain from scratch in Go with gRPC](https://github.com/volodymyrprokopyuk/go-blockchain) - The foundational and practical guide for effectively learning and progressively building a blockchain from scratch in Go with gRPC.
- [Build Web Application with Golang](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/)
- [Building Web Apps With Go](https://codegangsta.gitbooks.io/building-web-apps-with-go/content/)
- [Go 101](https://go101.org) - A book focusing on Go syntax/semantics and all kinds of details.
- [Go AST Book (Chinese)](https://github.com/chai2010/go-ast-book) - A book focusing on Go `go/*` packages.
- [Go Faster](https://leanpub.com/gofaster) - This book seeks to shorten your learning curve and help you become a proficient Go programmer, faster.
- [Go Succinctly](https://github.com/thedevsir/gosuccinctly) - in Persian.
- [Go with the domain](https://threedots.tech/go-with-the-domain/) - A book showing how to apply DDD, Clean Architecture, and CQRS by practical refactoring.
- [GoBooks](https://github.com/dariubs/GoBooks) - A curated list of Go books.
- [How To Code in Go eBook](https://www.digitalocean.com/community/books/how-to-code-in-go-ebook) - A 600 page introduction to Go aimed at first time developers.
- [Learning Go](https://www.miek.nl/downloads/Go/Learning-Go-latest.pdf)
- [Network Programming With Go](https://jan.newmarch.name/golang/)
- [Practical Go Lessons](https://www.practical-go-lessons.com/)
- [Spaceship Go A Journey to the Standard Library](https://blasrodri.github.io/spaceship-go-gh-pages/)
- [The Go Programming Language](https://www.gopl.io/)
- [The Golang Standard Library by Example (Chinese)](https://github.com/polaris1119/The-Golang-Standard-Library-by-Example)
- [The Little Go Book](https://github.com/karlseguin/the-little-go-book)
- [Web Application with Go the Anti-Textbook](https://github.com/thewhitetulip/web-dev-golang-anti-textbook/)

**[⬆ 回到顶部](#contents)**

<a id="gophers"></a>
## Gopher 社区

- [Free Gophers Pack](https://github.com/MariaLetta/free-gophers-pack) - Gopher graphics pack by Maria Letta with illustrations and emotional characters in vector and raster.
- [Go-gopher-Vector](https://github.com/keygx/Go-gopher-Vector) - Go gopher Vector Data [.ai, .svg].
- [gopher-logos](https://github.com/GolangUA/gopher-logos) - adorable gopher logos.
- [gopher-stickers](https://github.com/tenntenn/gopher-stickers)
- [gophericons](https://github.com/shalakhin/gophericons)
- [gopherize.me](https://github.com/matryer/gopherize.me) - Gopherize yourself.
- [gophers](https://github.com/ashleymcnamara/gophers) - Gopher artworks by Ashley McNamara.
- [gophers](https://github.com/egonelbre/gophers) - Free gophers.
- [gophers](https://github.com/rogeralsing/gophers) - random gopher graphics.
- [gophers](https://github.com/sillecelik/go-gopher) - Gopher amigurumi toy pattern.
- [gophers](https://github.com/scraly/gophers) - Gophers by Aurélie Vache.

**[⬆ 回到顶部](#contents)**

<a id="meetups"></a>
## Meetup 聚会

- [Basel Go Meetup](https://www.meetup.com/Basel-Go-Meetup/)
- [Belfast Gophers](https://www.meetup.com/Belfast-Gophers/)
- [Belgrade Golang Meetup](https://www.meetup.com/golang-serbia/)
- [Berlin Golang](https://www.meetup.com/golang-users-berlin/)
- [Brisbane Gophers](https://www.meetup.com/Brisbane-Golang-Meetup/)
- [Bärner Go Meetup - Berne, Switzerland](https://www.meetup.com/berner-go-meetup/)
- [Go Ireland - Dublin](https://www.meetup.com/goireland/)
- [Go Language NYC](https://www.meetup.com/golanguagenewyork/)
- [Go London User Group](https://www.meetup.com/Go-London-User-Group/)
- [Go Remote Meetup](https://www.meetup.com/Go-Remote-Meetup/)
- [Go Toronto](https://www.meetup.com/go-toronto/)
- [Go User Group Atlanta](https://www.meetup.com/Go-Users-Group-Atlanta/)
- [GoBandung](https://www.meetup.com/GoBandung/)
- [GoBridge, San Francisco, CA](https://www.meetup.com/gobridge/)
- [GoCracow - Krakow, Poland](https://www.meetup.com/GoCracow/)
- [GoJakarta](https://www.meetup.com/GoJakarta/)
- [Golang Amsterdam](https://www.meetup.com/golang-amsterdam/)
- [Golang Argentina](https://www.meetup.com/Golang-Argentina/)
- [Golang Athens](https://www.meetup.com/Athens-Gophers/)
- [Golang Baltimore, MD](https://www.meetup.com/BaltimoreGolang/)
- [Golang Bangalore](https://www.meetup.com/Golang-Bangalore/)
- [Golang Belo Horizonte - Brazil](https://www.meetup.com/go-belo-horizonte/)
- [Golang Boston](https://www.meetup.com/bostongo/)
- [Golang Bulgaria](https://www.meetup.com/Golang-Bulgaria/)
- [Golang Cardiff, UK](https://www.meetup.com/Cardiff-Go-Meetup/)
- [Golang Copenhagen](https://www.meetup.com/Go-Cph/)
- [Golang Curitiba - Brazil](https://www.meetup.com/GolangCWB/)
- [Golang DC, Arlington, VA](https://www.meetup.com/Golang-DC/)
- [Golang Dorset, UK](https://www.meetup.com/golang-dorset/)
- [Golang Estonia](https://www.meetup.com/Golang-Estonia/)
- [Golang Gurgaon, India](https://www.meetup.com/Gurgaon-Go-Meetup/)
- [Golang Hamburg - Germany](https://www.meetup.com/Go-User-Group-Hamburg/)
- [Golang Israel](https://www.meetup.com/Go-Israel/)
- [Golang Kathmandu](https://www.meetup.com/Golang-Kathmandu/)
- [Golang Lima - Peru](https://www.meetup.com/Golang-Peru/)
- [Golang Lyon](https://www.meetup.com/Golang-Lyon/)
- [Golang Marseille](https://www.meetup.com/fr-FR/Golang-Marseille/)
- [Golang Melbourne](https://www.meetup.com/golang-mel/)
- [Golang Milano](https://www.meetup.com/golang-milano/)
- [Golang North East](https://www.meetup.com/en-AU/Golang-North-East/)
- [Golang Paris](https://www.meetup.com/Golang-Paris/)
- [Golang Poland](https://www.meetup.com/Golang-Poland/)
- [Golang Pune](https://www.meetup.com/Golang-Pune/)
- [Golang Roma](https://www.meetup.com/golangroma/)
- [Golang Rotterdam](https://www.meetup.com/golang-rotterdam/)
- [Golang Singapore](https://www.meetup.com/golangsg/)
- [Golang Stockholm](https://www.meetup.com/Go-Stockholm/)
- [Golang Sydney, AU](https://www.meetup.com/golang-syd/)
- [Golang São Paulo - Brazil](https://www.meetup.com/golangbr/)
- [Golang Taipei](https://www.meetup.com/golang-taipei-meetup/)
- [Golang Thessaloniki](https://www.meetup.com/thessaloniki-golang-meetup/)
- [Golang Torino](https://www.meetup.com/golang-torino/)
- [Golang Turkey](https://kommunity.com/goturkiye)
- [Golang Vancouver, BC](https://www.meetup.com/golangvan/)
- [Golang Vienna, Austria](https://www.meetup.com/viennago/)
- [Golang Москва](https://www.meetup.com/Golang-Moscow/)
- [GoSF - San Francisco, CA](https://www.meetup.com/golangsf)
- [Istanbul Golang](https://www.meetup.com/Istanbul-Golang/)
- [Lagos Gophers](https://www.meetup.com/GolangNigeria/)
- [Nairobi Gophers](https://www.meetup.com/nairobi-gophers/)
- [Seattle Go Programmers](https://www.meetup.com/golang/)
- [Ukrainian Golang User Groups](https://www.meetup.com/uagolang/)
- [Utah Go User Group](https://www.meetup.com/utahgophers/)
- [Women Who Go - San Francisco, CA](https://www.meetup.com/Women-Who-Go/)
- [Zürich Gophers - Zurich, Switzerland](https://www.meetup.com/zurich-gophers/)

_在这里添加你所在城市/国家的分会（请提交 **PR**）_

**[⬆ 回到顶部](#contents)**

<a id="style-guides"></a>
## 风格指南

- [CockroachDB](https://github.com/cockroachdb/cockroach/blob/master/docs/style.md)
- [enra/go-styleguide](https://codeberg.org/enra/go-styleguide)
- [GitLab](https://docs.gitlab.com/ee/development/go_guide/)
- [Google](https://google.github.io/styleguide/go/)
- [Hyperledger](https://github.com/hyperledger/fabric/blob/release-1.4/docs/source/style-guides/go-style.rst)
- [Thanos](https://thanos.io/tip/contributing/coding-style-guide.md/)
- [Trybe](https://github.com/betrybe/playbook-go/blob/main/README_EN.md)
- [Uber](https://github.com/uber-go/guide/blob/master/style.md)

**[⬆ 回到顶部](#contents)**

<a id="social-media"></a>
## 社交媒体

<a id="twitter"></a>
### Twitter

- [@GoDiscussions](https://twitter.com/GoDiscussions)
- [@golang](https://twitter.com/golang)
- [@golang_news](https://twitter.com/golang_news)
- [@golangch](https://twitter.com/golangch)
- [@golangweekly](https://twitter.com/golangweekly)

**[⬆ 回到顶部](#contents)**

<a id="reddit"></a>
### Reddit

- [r/golang](https://www.reddit.com/r/golang/)

**[⬆ 回到顶部](#contents)**

<a id="websites"></a>
## 网站

- [Awesome Go @LibHunt](https://go.libhunt.com) - Your go-to Go Toolbox.
- [Awesome Golang Workshops](https://github.com/amit-davidson/awesome-golang-workshops) - A curated list of awesome golang workshops.
- [Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job) - Curated list of awesome remote jobs. A lot of them are looking for Go hackers.
- [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) - List of other amazingly awesome lists.
- [awesome-go-extra](https://github.com/xwjdsh/awesome-go-extra) - Parse awesome-go README file and generate a new README file with repo info.
- [Code with Mukesh](https://codewithmukesh.com/categories/golang) - Software Engineer and Blogs @ codewithmukesh.com.
- [Coding Mystery](https://codingmystery.com) - Solve exciting escape-room-inspired programming challenges using Go.
- [CodinGame](https://www.codingame.com/) - Learn Go by solving interactive tasks using small games as practical examples.
- [Go Blog](https://blog.golang.org) - The official Go blog.
- [Go Code Club](https://www.youtube.com/watch?v=nvoIPQYdx9g&list=PLEcwzBXTPUE_YQR7R0BRtHBYJ0LN3Y0i3) - A group of Gophers read and discuss a different Go project every week.
- [Go Community on Hashnode](https://hashnode.com/n/go) - Community of Gophers on Hashnode.
- [Go Forum](https://forum.golangbridge.org) - Forum to discuss Go.
- [Go Projects](https://github.com/golang/go/wiki/Projects) - List of projects on the Go community wiki.
- [Go Proverbs](https://go-proverbs.github.io/) - Go Proverbs by Rob Pike.
- [Go Report Card](https://goreportcard.com) - A report card for your Go package.
- [go.dev](https://go.dev/) - A hub for Go developers.
- [gocryforhelp](https://github.com/ninedraft/gocryforhelp) - Collection of Go projects that needs help. Good place to start your open-source way in Go.
- [Golang Developer Jobs](https://golangjob.xyz) - Developer Jobs exclusively for Golang related Roles.
- [Golang News](https://golangnews.com) - Links and news about Go programming.
- [Golang Nugget](https://golangnugget.com) - A weekly roundup of the best Go content, delivered to your inbox every Monday.
- [Golang Weekly](https://discu.eu/weekly/golang/) - Each monday projects, tutorials and articles about Go.
- [golang-nuts](https://groups.google.com/forum/#!forum/golang-nuts) - Go mailing list.
- [Gopher Community Chat](https://invite.slack.golangbridge.org) - Join Our New Slack Community For Gophers ([Understand how it came](https://blog.gopheracademy.com/gophers-slack-community/)).
- [Gophercises](https://gophercises.com/) - Free coding exercises for budding gophers.
- [json2go](https://m-zajac.github.io/json2go) - Advanced JSON to Go struct conversion - online tool.
- [justforfunc](https://www.youtube.com/c/justforfunc) - Youtube channel dedicated to Go programming language tips and tricks, hosted by Francesc Campoy [@francesc](https://twitter.com/francesc).
- [Learn Go Programming](https://blog.learngoprogramming.com) - Learn Go concepts with illustrations.
- [Libs.tech](https://libs.tech/go) – Awesome Go libraries and hidden gems
- [Made with Golang](https://madewithgolang.com/?ref=awesome-go)
- [pkg.go.dev](https://pkg.go.dev/) - Documentation for open source Go packages.
- [studygolang](https://studygolang.com) - The community of studygolang in China.
- [Trending Go repositories on GitHub today](https://github.com/trending?l=go) - Good place to find new Go libraries.
- [TutorialEdge - Golang](https://tutorialedge.net/course/golang/)

**[⬆ 回到顶部](#contents)**

<a id="tutorials"></a>
### 教程

- [50 Shades of Go](https://golang50shades.github.io/) - Traps, Gotchas, and Common Mistakes for New Golang Devs.
- [A Comprehensive Guide to Structured Logging in Go](https://betterstack.com/community/guides/logging/logging-in-go/) - Delve deep into the world of structured logging in Go with a specific focus on recently accepted slog proposal which aims to bring high performance structured logging with levels to the standard library.
- [A Guide to Golang E-Commerce](https://snipcart.com/blog/golang-ecommerce-ponzu-cms-demo?utm_term=golang-ecommerce-ponzu-cms-demo) - Building a Golang site for e-commerce (demo included).
- [A Tour of Go](https://tour.golang.org/) - Interactive tour of Go.
- [Build a Database in 1000 lines of code](https://link.medium.com/O9YQlx89Htb) - Build a NoSQL Database From Zero in 1000 Lines of Code.
- [Build web application with Golang](https://github.com/astaxie/build-web-application-with-golang) - Golang ebook intro how to build a web app with golang.
- [Building and Testing a REST API in Go with Gorilla Mux and PostgreSQL](https://semaphoreci.com/community/tutorials/building-and-testing-a-rest-api-in-go-with-gorilla-mux-and-postgresql) - We’ll write an API with the help of the powerful Gorilla Mux.
- [Building Go Web Applications and Microservices Using Gin](https://semaphoreci.com/community/tutorials/building-go-web-applications-and-microservices-using-gin) - Get familiar with Gin and find out how it can help you reduce boilerplate code and build a request handling pipeline.
- [Caching Slow Database Queries](https://medium.com/@rocketlaunchr.cloud/caching-slow-database-queries-1085d308a0c9) - How to cache slow database queries.
- [Canceling MySQL](https://medium.com/@rocketlaunchr.cloud/canceling-mysql-in-go-827ed8f83b30) - How to cancel MySQL queries.
- [CodeCrafters Golang Track](https://app.codecrafters.io/tracks/go) - Achieve mastery in advanced Go by building your own Redis, Docker, Git, and SQLite. Featuring goroutines, systems programming, file I/O, and more.
- [Design Patterns in Go](https://github.com/shubhamzanwar/design-patterns) - Collection of programming design patterns implemented in Go.
- [Games With Go](https://www.youtube.com/watch?v=9D4yH7e_ea8&list=PLDZujg-VgQlZUy1iCqBbe5faZLMkA3g2x) - A video series teaching programming and game development.
- [Go By Example](https://gobyexample.com/) - Hands-on introduction to Go using annotated example programs.
- [Go Cheat Sheet](https://github.com/a8m/go-lang-cheat-sheet) - Go's reference card.
- [Go database/sql tutorial](http://go-database-sql.org/) - Introduction to database/sql.
- [Go in 7 days](https://github.com/harrytran103/7_days_of_go) - Learn everything about Go in 7 days (from a Nodejs developer).
- [Go Language Tutorial](https://www.javatpoint.com/go-tutorial) - Learn Go language Tutorial.
- [Go Tutorial](https://www.tutorialspoint.com/go/index.htm) - Learn Go programming.
- [Go WebAssembly Tutorial - Building a Simple Calculator](https://tutorialedge.net/golang/go-webassembly-tutorial/)
- [go-clean-template](https://github.com/evrone/go-clean-template) - Clean Architecture template for Golang services.
- [go-patterns](https://github.com/tmrts/go-patterns) - Curated list of Go design patterns, recipes and idioms.
- [Golang for Node.js Developers](https://github.com/miguelmota/golang-for-nodejs-developers) - Examples of Golang compared to Node.js for learning.
- [Golang Tutorial Guide](https://www.freecodecamp.org/news/golang-tutorial-list-free-courses-learn-go-programming-language/) - A List of Free Courses to Learn the Go Programming Language.
- [golang-examples](https://github.com/SimonWaldherr/golang-examples) - Many examples to learn Golang.
- [Golangbot](https://golangbot.com/learn-golang-series/) - Tutorials to get started with programming in Go.
- [GopherCoding](https://gophercoding.com/) - Collection of code snippets and tutorials to help tackle every day issues.
- [GopherSnippets](https://gophersnippets.com/) - Code snippets with tests and testable examples for the Go programming language.
- [Gosamples](https://gosamples.dev/) - Collection of code snippets that let you solve everyday code problems.
- [GraphQL with Go](https://hasura.io/learn/graphql/backend-stack/languages/go/) - Learn how to create a Go GraphQL server and client with code generation. Also includes creating REST endpoints.
- [Hackr.io](https://hackr.io/tutorials/learn-golang) - Learn Go from the best online golang tutorials submitted & voted by the golang programming community.
- [Hex Monscape](https://github.com/Haraj-backend/hex-monscape) - Getting started guidelines in writing maintainable code using Hexagonal Architecture.
- [How to Benchmark: dbq vs sqlx vs GORM](https://medium.com/@rocketlaunchr.cloud/how-to-benchmark-dbq-vs-sqlx-vs-gorm-e814caacecb5) - Learn how to benchmark in Go. As a case-study, we will benchmark dbq, sqlx and GORM.
- [How To Deploy a Go Web Application with Docker](https://semaphoreci.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker) - Learn how to use Docker for Go development and how to build production Docker images.
- [How to Implement Role-Based Access Control (RBAC) Authorization in Golang](https://www.permit.io/blog/role-based-access-control-rbac-authorization-in-golang) - A guide to implementing Role-Based Access Control (RBAC) in Golang, including code examples, covering various methods to secure app endpoints with role-based authorization.
- [How to Use Godog for Behavior-driven Development in Go](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go) - Get started with Godog - a Behavior-driven development framework for building and testing Go applications.
- [Learn Go with 1000+ Exercises](https://github.com/inancgumus/learngo) - Learn Go with thousands of examples, exercises, and quizzes.
- [Learn Go with TDD](https://github.com/quii/learn-go-with-tests) - Learn Go with test-driven development.
- [Learning Go by examples](https://dev.to/aurelievache/learning-go-by-examples-introduction-448n) - Series of articles in order to learn Golang language by concrete applications as example.
- [Microservices with Go](https://www.youtube.com/playlist?list=PLmD8u-IFdreyh6EUfevBcbiuCKzFk0EW_) - Dive deep into building microservices using Go, including gRPC.
- [package main](https://www.youtube.com/packagemain) - YouTube channel about Programming in Go.
- [Programming with Google Go](https://www.coursera.org/specializations/google-golang) - Coursera Specialization to learn about Go from scratch.
- [Scaling Go Applications](https://betterstack.com/community/guides/scaling-go/) - Everything about building, deploying and scaling Go applications in production.
- [The world’s easiest introduction to WebAssembly with Golang](https://medium.com/@martinolsansky/webassembly-with-golang-is-fun-b243c0e34f02)
- [Understanding Go in a visual way](https://dev.to/aurelievache/series/26234) - Learn Go visually
- [W3basic Go Tutorials](https://www.w3basic.com/golang/) - W3Basic provides an in-depth tutorial and well-organized content to learn Golang programming.
- [Your basic Go](https://yourbasic.org/golang) - Huge collection of tutorials and how to's.

**[⬆ 回到顶部](#contents)**

<a id="guided-learning"></a>
### 引导式学习

- [The Go Developer Roadmap](https://roadmap.sh/golang) - A visual roadmap that new Go developers can follow through to help them learn Go.
- [The Go Interview Practice](https://github.com/RezaSi/go-interview-practice) - A GitHub repository offering coding challenges for Go technical interview preparation.
- [The Go Learning Path](https://tutorialedge.net/paths/golang/) - A guided learning path containing a mix of free and premium resources.
- [The Go Skill Tree](https://labex.io/skilltrees/go) - A structured learning path that combines both free and premium resources.

**[⬆ 回到顶部](#contents)**

<a id="contribution"></a>
## 贡献指南

欢迎贡献！请阅读上游的[贡献指南](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md)了解具体规范。

<a id="license"></a>
## 许可证

本项目采用 [MIT 许可证](https://github.com/avelino/awesome-go/blob/main/LICENSE) 发布，详见 LICENSE 文件。
