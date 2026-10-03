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
- [config](https://github.com/num30/config) - configure your app using file, environment variables, or flags in two lines of code.
- [config](https://github.com/andreiavrammsd/config) - Struct-based configuration loader with a dedicated config file parser, supporting env vars, flags, defaults, and validation.
- [configuration](https://github.com/BoRuDar/configuration) - Library for initializing configuration structs from env variables, files, flags and 'default' tag.
- [configuro](https://github.com/sherifabdlnaby/configuro) - opinionated configuration loading & validation framework from ENV and Files focused towards 12-Factor compliant applications.
- [confiq](https://github.com/greencoda/confiq) - Structured data format to config struct decoder library for Go - supporting multiple data formats.
- [confita](https://github.com/heetch/confita) - Load configuration in cascade from multiple backends into a struct.
- [conflate](https://github.com/the4thamigo-uk/conflate) - Library/tool to merge multiple JSON/YAML/TOML files from arbitrary URLs, validation against a JSON schema, and application of default values defined in the schema.
- [enflag](https://github.com/atelpis/enflag) - Container-oriented, zero-dependency configuration library that unifies Env variable and Flag parsing. Uses generics for type safety, without reflection or struct tags.
- [env](https://github.com/caarlos0/env) - Parse environment variables to Go structs (with defaults).
- [env](https://github.com/junk1tm/env) - A lightweight package for loading environment variables into structs.
- [env](https://github.com/syntaqx/env) - An environment utility package with support for unmarshaling into structs.
- [envconfig](https://github.com/vrischmann/envconfig) - Read your configuration from environment variables.
- [envh](https://github.com/antham/envh) - Helpers to manage environment variables.
- [envyaml](https://github.com/yuseferi/envyaml) - Yaml with environment variables reader. it helps to have secrets as environment variable but load them configs as structured Yaml.
- [fig](https://github.com/kkyr/fig) - Tiny library for reading configuration from a file and from environment variables (with validation & defaults).
- [genv](https://github.com/sakirsensoy/genv) - Read environment variables easily with dotenv support.
- [go-array](https://github.com/deatil/go-array) - A Go package that read or set data from map, slice or json.
- [go-aws-ssm](https://github.com/PaddleHQ/go-aws-ssm) - Go package that fetches parameters from AWS System Manager - Parameter Store.
- [go-cfg](https://github.com/dsbasko/go-cfg) - The library provides a unified way to read configuration data into a structure from various sources, such as env, flags, and configuration files (.json, .yaml, .toml, .env).
- [go-conf](https://github.com/ThomasObenaus/go-conf) - Simple library for application configuration based on annotated structs. It supports reading the configuration from environment variables, config files and command line parameters.
- [go-config](https://github.com/MordaTeam/go-config) - Simple and convenient library for working with app configurations.
- [go-external-config](https://github.com/go-external-config/go) - Spring-inspired configuration management library for Go.
- [go-external-config/aws](https://github.com/go-external-config/aws) - AWS property source support for go-external-config.
- [go-external-config/consul](https://github.com/go-external-config/consul) - Consul property source support for go-external-config.
- [go-external-config/vault](https://github.com/go-external-config/vault) - Vault property source support for go-external-config.
- [go-ini](https://github.com/subpop/go-ini) - A Go package that marshals and unmarshals INI-files.
- [go-ssm-config](https://github.com/ianlopshire/go-ssm-config) - Go utility for loading configuration parameters from AWS SSM (Parameter Store).
- [go-up](https://github.com/ufoscout/go-up) - A simple configuration library with recursive placeholders resolution and no magic.
- [go-yamlvalidator](https://github.com/Yakwilik/go-yamlvalidator) - Source-aware YAML validation with native Go schemas and JSON Schema support.
- [GoCfg](https://github.com/Jagerente/gocfg) - Config manager with Struct Tags based contracts, custom value providers, parsers, and documentation generation. Customizable yet simple.
- [goconfig](https://github.com/fulldump/goconfig) - Populate Go structs from flags, environment variables, config.json and defaults with deterministic precedence. No extra dependencies.
- [godotenv](https://github.com/joho/godotenv) - Go port of Ruby's dotenv library (Loads environment variables from `.env`).
- [goenv](https://github.com/psyb0t/goenv) - Reads the ENV environment variable and reports whether the process is running in production or development.
- [GoLobby/Config](https://github.com/golobby/config) - GoLobby Config is a lightweight yet powerful configuration manager for the Go programming language.
- [gone/jconf](https://github.com/One-com/gone/tree/master/jconf) - Modular JSON configuration. Keep your config structs along with the code they configure and delegate parsing to submodules without sacrificing full config serialization.
- [gonfig](https://github.com/milad-abbasi/gonfig) - Tag-based configuration parser which loads values from different providers into typesafe struct.
- [gonfiguration](https://github.com/psyb0t/gonfiguration) - Loads configuration from environment variables into structs via reflection, with struct-tag defaults and required fields.
- [gookit/config](https://github.com/gookit/config) - application config manage(load,get,set). support JSON, YAML, TOML, INI, HCL. multi file load, data override merge.
- [harvester](https://github.com/beatlabs/harvester) - Harvester, a easy to use static and dynamic configuration package supporting seeding, env vars and Consul integration.
- [hedzr/store](https://github.com/hedzr/store) - Extensible, high-performance configuration management library, optimized for hierarchical data.
- [hjson](https://github.com/hjson/hjson-go) - Human JSON, a configuration file format for humans. Relaxed syntax, fewer mistakes, more comments.
- [hocon](https://github.com/gurkankaymak/hocon) - Configuration library for working with the HOCON(a human-friendly JSON superset) format, supports features like environment variables, referencing other values, comments and multiple files.
- [ini](https://github.com/go-ini/ini) - Go package to read and write INI files.
- [ini](https://github.com/wlevene/ini) - INI Parser & Write Library, Unmarshal to Struct, Marshal to Json, Write File, watch file.
- [kelseyhightower/envconfig](https://github.com/kelseyhightower/envconfig) - Go library for managing configuration data from environment variables.
- [koanf](https://github.com/knadh/koanf) - Light weight, extensible library for reading config in Go applications. Built in support for JSON, TOML, YAML, env, command line.
- [konf](https://github.com/nil-go/konf) - The simplest API for reading/watching config from file, env, flag and clouds (e.g. AWS, Azure, GCP).
- [konfig](https://github.com/lalamove/konfig) - Composable, observable and performant config handling for Go for the distributed processing era.
- [kong](https://github.com/alecthomas/kong) - Command-line parser with support for arbitrarily complex command-line structures and additional sources of configuration such as YAML, JSON, TOML, etc (successor to `kingpin`).
- [nasermirzaei89/env](https://github.com/nasermirzaei89/env) - Simple useful package for read environment variables.
- [nfigure](https://github.com/muir/nfigure) - Per-library struct-tag based configuration from command lines (Posix & Go-style); environment, JSON, YAML
- [onion](https://github.com/goraz/onion) - Layer based configuration for Go, Supports JSON, TOML, YAML, properties, etcd, env, and encryption using PGP.
- [piper](https://github.com/Yiling-J/piper) - Viper wrapper with config inheritance and key generation.
- [sonic](https://github.com/bytedance/sonic) - A blazingly fast JSON serializing & deserializing library.
- [swap](https://github.com/oblq/swap) - Instantiate/configure structs recursively, based on build environment. (YAML, TOML, JSON and env).
- [typenv](https://github.com/diegomarangoni/typenv) - Minimalistic, zero dependency, typed environment variables library.
- [uConfig](https://github.com/omeid/uconfig) - Lightweight, zero-dependency, and extendable configuration management.
- [viper](https://github.com/spf13/viper) - Go configuration with fangs.
- [xdg](https://github.com/adrg/xdg) - Go implementation of the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/) and [XDG user directories](https://wiki.archlinux.org/index.php/XDG_user_directories).
- [yamagiconf](https://github.com/romshark/yamagiconf) - The "safe subset" of YAML for Go configs.
- [zerocfg](https://github.com/chaindead/zerocfg) - Zero-effort, concise configuration management that avoids boilerplate and repetitive code, supports multiple sources with priority overrides.

**[⬆ 回到顶部](#contents)**

<a id="continuous-integration"></a>
## 持续集成

_有助于持续集成的工具。_

- [abstruse](https://github.com/bleenco/abstruse) - Abstruse is a distributed CI platform.
- [Bencher](https://bencher.dev/) - A suite of continuous benchmarking tools designed to catch performance regressions in CI.
- [CDS](https://github.com/ovh/cds) - Enterprise-Grade CI/CD and DevOps Automation Open Source Platform.
- [coverage](https://github.com/jbunds/coverage) - A simple Web UI for Go test coverage, and the [go-test-coverage-html-report](https://github.com/marketplace/actions/go-test-coverage-html-report) reusable GitHub Action.
- [dot](https://github.com/opnlabs/dot) - A minimal, local first continuous integration system that uses Docker to run jobs concurrently in stages.
- [drone](https://github.com/drone/drone) - Drone is a Continuous Integration platform built on Docker, written in Go.
- [go-beautiful-html-coverage](https://github.com/gha-common/go-beautiful-html-coverage) - A GitHub Action to track code coverage in your pull requests, with a beautiful HTML preview, for free.
- [go-fuzz-action](https://github.com/jidicula/go-fuzz-action) - Use Go 1.18's built-in fuzz testing in GitHub Actions.
- [go-semver-release](https://github.com/s0ders/go-semver-release) - Automate the semantic versioning of Git repositories.
- [go-test-coverage](https://github.com/marketplace/actions/go-test-coverage) - A GitHub Action which reports issues when test coverage is below set threshold.
- [gomason](https://github.com/nikogura/gomason) - Test, Build, Sign, and Publish your go binaries from a clean workspace.
- [gotestfmt](https://github.com/GoTestTools/gotestfmt) - go test output for humans.
- [goveralls](https://github.com/mattn/goveralls) - Go integration for Coveralls.io continuous code coverage tracking system.
- [muffet](https://github.com/raviqqe/muffet) - Fast website link checker in Go, see [alternatives](https://github.com/lycheeverse/lychee#features).
- [overalls](https://github.com/go-playground/overalls) - Multi-Package go project coverprofile for tools like goveralls.
- [PikoCI](https://github.com/pikoci/pikoci) - Self-hosted CI/CD inspired by Concourse. Single binary, any database, any queue. HCL pipelines, pluggable resource types and runners.
- [roveralls](https://github.com/LawrenceWoodman/roveralls) - Recursive coverage testing tool.
- [woodpecker](https://github.com/woodpecker-ci/woodpecker) - Woodpecker is a community fork of the Drone CI system.

**[⬆ 回到顶部](#contents)**

<a id="css-preprocessors"></a>
## CSS 预处理器

_用于预处理 CSS 文件的库。_

- [go-css](https://github.com/napsy/go-css) - A very simple CSS parser, written in Go.
- [go-libsass](https://github.com/wellington/go-libsass) - Go wrapper to the 100% Sass compatible libsass project.

**[⬆ 回到顶部](#contents)**

<a id="data-integration-frameworks"></a>
## 数据集成框架

_用于执行 ELT / ETL 的框架_

- [Benthos](https://github.com/benthosdev/benthos) - A message streaming bridge between a range of protocols.
- [CloudQuery](http://github.com/cloudquery/cloudquery) - A high-performance ELT data integration framework with pluggable architecture.
- [confluence2md](https://github.com/gkoos/confluence2md) - Confluence to Markdown crawler and converter.
- [omniparser](https://github.com/jf-tech/omniparser) - A versatile ETL library that parses text input (CSV/txt/JSON/XML/EDI/X12/EDIFACT/etc) in streaming fashion and transforms data into JSON output using data-driven schema.

**[⬆ 回到顶部](#contents)**

<a id="data-structures-and-algorithms"></a>
## 数据结构与算法

<a id="bit-packing-and-compression"></a>
### 位打包与压缩

- [bingo](https://github.com/iancmcc/bingo) - Fast, zero-allocation, lexicographical-order-preserving packing of native types to bytes.
- [binpacker](https://github.com/zhuangsirui/binpacker) - Binary packer and unpacker helps user build custom binary stream.
- [bit](https://github.com/yourbasic/bit) - Golang set data structure with bonus bit-twiddling functions.
- [crunch](https://github.com/superwhiskers/crunch) - Go package implementing buffers for handling various datatypes easily.
- [go-ef](https://github.com/amallia/go-ef) - A Go implementation of the Elias-Fano encoding.
- [roaring](https://github.com/RoaringBitmap/roaring) - Go package implementing compressed bitsets.

<a id="bit-sets"></a>
### 位集合

- [bitmap](https://github.com/kelindar/bitmap) - Dense, zero-allocation, SIMD-enabled bitmap/bitset in Go.
- [bitset](https://github.com/bits-and-blooms/bitset) - Go package implementing bitsets.

<a id="bloom-and-cuckoo-filters"></a>
### 布隆过滤器与布谷鸟过滤器

- [bloom](https://github.com/bits-and-blooms/bloom) - Go package implementing Bloom filters.
- [bloom](https://github.com/zhenjl/bloom) - Bloom filters implemented in Go.
- [bloom](https://github.com/yourbasic/bloom) - Golang Bloom filter implementation.
- [bloomfilter](https://github.com/OldPanda/bloomfilter) - Yet another Bloomfilter implementation in Go, compatible with Java's Guava library.
- [boomfilters](https://github.com/tylertreat/BoomFilters) - Probabilistic data structures for processing continuous, unbounded streams.
- [cuckoo-filter](https://github.com/linvon/cuckoo-filter) - Cuckoo filter: a comprehensive cuckoo filter, which is configurable and space optimized compared with other implements, and all features mentioned in original paper are available.
- [cuckoofilter](https://github.com/seiflotfy/cuckoofilter) - Cuckoo filter: a good alternative to a counting bloom filter implemented in Go.
- [ribbonGo](https://github.com/RibbonFilter/ribbonGo) - First pure Go implementation of Ribbon filters (practically smaller than Bloom and Xor) for space-efficient approximate set membership queries.
- [ring](https://github.com/TheTannerRyan/ring) - Go implementation of a high performance, thread safe bloom filter.

<a id="data-structure-and-algorithm-collections"></a>
### 数据结构与算法合集

- [algorithms](https://github.com/shady831213/algorithms) - Algorithms and data structures.CLRS study.
- [go-datastructures](https://github.com/Workiva/go-datastructures) - Collection of useful, performant, and thread-safe data structures.
- [gods](https://github.com/emirpasic/gods) - Go Data Structures. Containers, Sets, Lists, Stacks, Maps, BidiMaps, Trees, HashSet etc.
- [gostl](https://github.com/liyue201/gostl) - Data structure and algorithm library for go, designed to provide functions similar to C++ STL.

<a id="iterators"></a>
### 迭代器

- [gloop](https://github.com/alvii147/gloop) - Convenient looping using Go's range-over-func feature.
- [goterator](https://github.com/yaa110/goterator) - Iterator implementation to provide map and reduce functionalities.
- [iter](https://github.com/disksing/iter) - Go implementation of C++ STL iterators and algorithms.

<a id="maps"></a>
### 映射

更复杂的键值存储参见[数据库](#database)，
更多有序 Map 实现参见[树](#trees)。

- [cmap](https://github.com/lrita/cmap) - a thread-safe concurrent map for go, support using `interface{}` as key and auto scale up shards.
- [concurrent-swiss-map](https://github.com/mhmtszr/concurrent-swiss-map) - A high-performance, thread-safe generic concurrent hash map implementation with Swiss Map.
- [dict](https://github.com/srfrog/dict) - Python-like dictionaries (dict) for Go.
- [genericsyncmap](https://github.com/donomii/genericsyncmap) - Type-safe generic wrapper for `sync.Map` with full method parity and zero dependencies.
- [go-shelve](https://github.com/lucmq/go-shelve) - A persistent, map-like object for the Go programming language. Supports multiple embedded key-value stores.
- [goradd/maps](https://github.com/goradd/maps) - Go 1.18+ generic map interface for maps; safe maps; ordered maps; ordered, safe maps; etc.
- [hmap](https://github.com/lyonnee/hmap) - HMap is a concurrent and secure, generic support Map implementation designed to provide an easy-to-use API.

<a id="miscellaneous-data-structures-and-algorithms"></a>
### 其他数据结构与算法

- [combo](https://github.com/bobg/combo) - Combinatorial operations including permutations, combinations, and combinations-with-replacement.
- [concurrent-writer](https://github.com/free/concurrent-writer) - Highly concurrent drop-in replacement for `bufio.Writer`.
- [count-min-log](https://github.com/seiflotfy/count-min-log) - Go implementation Count-Min-Log sketch: Approximately counting with approximate counters (Like Count-Min sketch but using less memory).
- [FSM](https://github.com/enetx/fsm) - FSM for Go.
- [fsm](https://github.com/cocoonspace/fsm) - Finite-State Machine package.
- [genfuncs](https://github.com/nwillc/genfuncs) - Go 1.18+ generics package inspired by Kotlin's Sequence and Map.
- [go-generics](https://github.com/bobg/go-generics) - Generic slice, map, set, iterator, and goroutine utilities.
- [go-geoindex](https://github.com/hailocab/go-geoindex) - In-memory geo index.
- [go-rampart](https://github.com/francesconi/go-rampart) - Determine how intervals relate to each other.
- [go-rquad](https://github.com/aurelien-rainone/go-rquad) - Region quadtrees with efficient point location and neighbour finding.
- [go-tuple](https://github.com/barweiss/go-tuple) - Generic tuple implementation for Go 1.18+.
- [go18ds](https://github.com/daichi-m/go18ds) - Go Data Structures using Go 1.18 generics.
- [gofal](https://github.com/xxjwxc/gofal) - fractional api for Go.
- [gogu](https://github.com/esimov/gogu) - A comprehensive, reusable and efficient concurrent-safe generics utility functions and data structures library.
- [gota](https://github.com/kniren/gota) - Implementation of dataframes, series, and data wrangling methods for Go.
- [hide](https://github.com/emvi/hide) - ID type with marshalling to/from hash to prevent sending IDs to clients.
- [hyperloglog](https://github.com/axiomhq/hyperloglog) - HyperLogLog implementation with Sparse, LogLog-Beta bias correction and TailCut space reduction.
- [quadtree](https://github.com/s0rg/quadtree) - Generic, zero-alloc, 100%-test covered quadtree.
- [slices](https://github.com/twharmon/slices) - Pure, generic functions for slices.

<a id="nullable-types"></a>
### 可空类型

- [nan](https://github.com/kak-tus/nan) - Zero allocation Nullable structures in one library with handy conversion functions, marshallers and unmarshallers.
- [null](https://github.com/emvi/null) - Nullable Go types that can be marshalled/unmarshalled to/from JSON.
- [typ](https://github.com/gurukami/typ) - Null Types, Safe primitive type conversion and fetching value from complex structures.

<a id="queues"></a>
### 队列

- [deheap](https://github.com/aalpar/deheap) - Doubly-ended heap (min-max heap) with O(log n) access to both minimum and maximum elements.
- [deque](https://github.com/edwingeng/deque) - A highly optimized double-ended queue.
- [deque](https://github.com/gammazero/deque) - Fast ring-buffer deque (double-ended queue).
- [dqueue](https://github.com/vodolaz095/dqueue) - Simple, in memory, zero dependency and battle tested, thread-safe deferred queue.
- [goconcurrentqueue](https://github.com/enriquebris/goconcurrentqueue) - Concurrent FIFO queue.
- [hatchet](https://github.com/hatchet-dev/hatchet) - Distributed, Fault-tolerant task queue.
- [list](https://github.com/koss-null/list) - A generic, thread-safe doubly linked list with full iterator support and an intrusive singly linked list for embedded use; a feature-rich replacement for container/list.
- [memlog](https://github.com/embano1/memlog) - An easy to use, lightweight, thread-safe and append-only in-memory data structure inspired by Apache Kafka.
- [queue](https://github.com/adrianbrad/queue) - Multiple thread-safe, generic queue implementations for Go.

<a id="sets"></a>
### 集合

- [dsu](https://github.com/ihebu/dsu) - Disjoint Set data structure implementation in Go.
- [golang-set](https://github.com/deckarep/golang-set) - Thread-Safe and Non-Thread-Safe high-performance sets for Go.
- [goset](https://github.com/zoumo/goset) - A useful Set collection implementation for Go.
- [set](https://github.com/StudioSol/set) - Simple set data structure implementation in Go using LinkedHashMap.

<a id="text-analysis"></a>
### 文本分析

- [bleve](https://github.com/blevesearch/bleve) - Modern text indexing library for go.
- [go-adaptive-radix-tree](https://github.com/plar/go-adaptive-radix-tree) - Go implementation of Adaptive Radix Tree.
- [go-edlib](https://github.com/hbollon/go-edlib) - Go string comparison and edit distance algorithms library (Levenshtein, LCS, Hamming, Damerau levenshtein, Jaro-Winkler, etc.) compatible with Unicode.
- [levenshtein](https://github.com/agext/levenshtein) - Levenshtein distance and similarity metrics with customizable edit costs and Winkler-like bonus for common prefix.
- [levenshtein](https://github.com/agnivade/levenshtein) - Implementation to calculate levenshtein distance in Go.
- [mspm](https://github.com/BlackRabbitt/mspm) - Multi-String Pattern Matching Algorithm for information retrieval.
- [parsefields](https://github.com/MonaxGT/parsefields) - Tools for parse JSON-like logs for collecting unique fields and events.
- [ptrie](https://github.com/viant/ptrie) - An implementation of prefix tree.
- [radixtree](https://github.com/gammazero/radixtree) - Adaptive radix tree (prefix-tree or compact-trie).
- [trie](https://github.com/derekparker/trie) - Trie implementation in Go.

<a id="trees"></a>
### 树

- [graphlib](https://github.com/aio-arch/graphlib) - Topological sort lib,Sorting and pruning of DAG graphs.
- [hashsplit](http://github.com/bobg/hashsplit) - Split byte streams into chunks, and arrange chunks into trees, with boundaries determined by content, not position.
- [merkle](https://github.com/bobg/merkle) - Space-efficient computation of Merkle root hashes and inclusion proofs.
- [skiplist](https://github.com/MauriceGit/skiplist) - Very fast Go Skiplist implementation.
- [skiplist](https://github.com/gansidui/skiplist) - Skiplist implementation in Go.
- [skiplist](https://github.com/huandu/skiplist) - Fast and easy-to-use skip list for Go.
- [treemap](https://github.com/igrmk/treemap) - Generic key-sorted map using a red-black tree under the hood.

<a id="pipes"></a>
### 管道

- [ordered-concurrently](https://github.com/tejzpr/ordered-concurrently) - Go module that processes work concurrently and returns output in a channel in the order of input.
- [parapipe](https://github.com/nazar256/parapipe) - FIFO Pipeline which parallels execution on each stage while maintaining the order of messages and results.
- [pipeline](https://github.com/hyfather/pipeline) - An implementation of pipelines with fan-in and fan-out.
- [pipelines](https://github.com/nxdir-s/pipelines) - Generic pipeline functions for concurrent processing.

**[⬆ 回到顶部](#contents)**

<a id="database"></a>
## 数据库

<a id="caches"></a>
### 缓存

_支持记录过期、内存分布式数据存储，或文件型数据库内存子集的存储。_

- [bcache](https://github.com/iwanbk/bcache) - Eventually consistent distributed in-memory cache Go library.
- [BigCache](https://github.com/allegro/bigcache) - Efficient key/value cache for gigabytes of data.
- [cache2go](https://github.com/muesli/cache2go) - In-memory key:value cache which supports automatic invalidation based on timeouts.
- [cachego](https://github.com/faabiosr/cachego) - Golang Cache component for multiple drivers.
- [clusteredBigCache](https://github.com/oaStuff/clusteredBigCache) - BigCache with clustering support and individual item expiration.
- [coherence-go-client](https://github.com/oracle/coherence-go-client) - Full implementation of Oracle Coherence cache API for Go applications using gRPC as network transport.
- [couchcache](https://github.com/codingsince1985/couchcache) - RESTful caching micro-service backed by Couchbase server.
- [EchoVault](https://github.com/EchoVault/EchoVault) - Embeddable Distributed in-memory data store compatible with Redis clients.
- [easycache](https://github.com/hugocarreira/easycache) - A simple way to use in-memory cache in Golang (TTL/FIFO/LRU/LFU).
- [fastcache](https://github.com/VictoriaMetrics/fastcache) - fast thread-safe inmemory cache for big number of entries. Minimizes GC overhead.
- [GCache](https://github.com/bluele/gcache) - Cache library with support for expirable Cache, LFU, LRU and ARC.
- [gdcache](https://github.com/ulovecode/gdcache) - A pure non-intrusive cache library implemented by golang, you can use it to implement your own distributed cache.
- [go-cache](https://github.com/viney-shih/go-cache) - A flexible multi-layer Go caching library to deal with in-memory and shared cache by adopting Cache-Aside pattern.
- [go-freelru](https://github.com/elastic/go-freelru) A GC-less, fast and generic LRU hashmap library with optional locking, sharding, eviction and expiration.
- [go-gcache](https://github.com/szyhf/go-gcache) - The generic version of `GCache`, cache support for expirable Cache, LFU, LRU and ARC.
- [go-mcache](https://github.com/OrlovEvgeny/go-mcache) - Fast in-memory key:value store/cache library. Pointer caches.
- [gocache](https://github.com/eko/gocache) - A complete Go cache library with multiple stores (memory, memcache, redis, ...), chainable, loadable, metrics cache and more.
- [gocache](https://github.com/yuseferi/gocache) - A data race free Go ache library with high performance and auto pruge functionality
- [groupcache](https://github.com/golang/groupcache) - Groupcache is a caching and cache-filling library, intended as a replacement for memcached in many cases.
- [icache](https://github.com/mdaliyan/icache) - A High Performance, Generic, thread-safe, zero-dependency cache package.
- [imcache](https://github.com/erni27/imcache) - A generic in-memory cache Go library. It supports expiration, sliding expiration, max entries limit, eviction callbacks and sharding.
- [jetcache-go](https://github.com/mgtv-tech/jetcache-go) - Unified Go cache library supporting multi-level caching.
- [nscache](https://github.com/no-src/nscache) - A Go caching framework that supports multiple data source drivers.
- [otter](https://github.com/maypok86/otter) - A high performance lockless cache for Go. Many times faster than Ristretto and friends.
- [pocache](https://github.com/naughtygopher/pocache) - Pocache is a minimal cache package which focuses on a preemptive optimistic caching strategy.
- [ristretto](https://github.com/dgraph-io/ristretto) - A high performance memory-bound Go cache.
- [sturdyc](https://github.com/viccon/sturdyc) - A caching library with advanced concurrency features designed to make I/O heavy applications robust and highly performant.
- [theine](https://github.com/Yiling-J/theine-go) - High performance, near optimal in-memory cache with proactive TTL expiration and generics.
- [timedmap](https://github.com/zekroTJA/timedmap) - Map with expiring key-value pairs.
- [ttlcache](https://github.com/jellydator/ttlcache) - An in-memory cache with item expiration and generics.
- [ttlcache](https://github.com/cheshir/ttlcache) - In-memory key value storage with TTL for each record.

<a id="databases-implemented-in-go"></a>
### 用 Go 实现的数据库

- [badger](https://github.com/dgraph-io/badger) - Fast key-value store in Go.
- [bbolt](https://github.com/etcd-io/bbolt) - An embedded key/value database for Go.
- [Bitcask](https://git.mills.io/prologic/bitcask) - Bitcask is an embeddable, persistent and fast key-value (KV) database written in pure Go with predictable read/write performance, low latency and high throughput thanks to the bitcask on-disk layout (LSM+WAL).
- [buntdb](https://github.com/tidwall/buntdb) - Fast, embeddable, in-memory key/value database for Go with custom indexing and spatial support.
- [clover](https://github.com/ostafen/clover) - A lightweight document-oriented NoSQL database written in pure Golang.
- [cockroach](https://github.com/cockroachdb/cockroach) - Scalable, Geo-Replicated, Transactional Datastore.
- [Coffer](https://github.com/claygod/coffer) - Simple ACID key-value database that supports transactions.
- [column](https://github.com/kelindar/column) - High-performance, columnar, embeddable in-memory store with bitmap indexing and transactions.
- [CovenantSQL](https://github.com/CovenantSQL/CovenantSQL) - CovenantSQL is a SQL database on blockchain.
- [Databunker](https://github.com/paranoidguy/databunker) - Personally identifiable information (PII) storage service built to comply with GDPR and CCPA.
- [dgraph](https://github.com/dgraph-io/dgraph) - Scalable, Distributed, Low Latency, High Throughput Graph Database.
- [DiceDB](https://github.com/DiceDB/dice) - An open-source, fast, reactive, in-memory database optimized for modern hardware. Higher throughput and lower median latencies, making it ideal for modern workloads.
- [diskv](https://github.com/peterbourgon/diskv) - Home-grown disk-backed key-value store.
- [dolt](https://github.com/dolthub/dolt) - Dolt – It's Git for Data.
- [eliasdb](https://github.com/krotik/eliasdb) - Dependency-free, transactional graph database with REST API, phrase search and SQL-like query language.
- [gedb](https://github.com/vinicius-lino-figueiredo/gedb) - MongoDB-like embedded database, written in pure-go. Supports indexing and complex queries.
- [go-sqlite](https://github.com/glebarez/go-sqlite) – A Pure Golang implemented SQLite driver without CGO.
- [godis](https://github.com/hdt3213/godis) - A Golang implemented high-performance Redis server and cluster.
- [goleveldb](https://github.com/syndtr/goleveldb) - Implementation of the [LevelDB](https://github.com/google/leveldb) key/value database in Go.
- [hare](https://github.com/jameycribbs/hare) - A simple database management system that stores each table as a text file of line-delimited JSON.
- [immudb](https://github.com/codenotary/immudb) - immudb is a lightweight, high-speed immutable database for systems and applications written in Go.
- [influxdb](https://github.com/influxdb/influxdb) - Scalable datastore for metrics, events, and real-time analytics.
- [ledisdb](https://github.com/siddontang/ledisdb) - Ledisdb is a high performance NoSQL like Redis based on LevelDB.
- [levigo](https://github.com/jmhodges/levigo) - Levigo is a Go wrapper for LevelDB.
- [libradb](https://github.com/amit-davidson/LibraDB) - LibraDB is a simple database with less than 1000 lines of code for learning.
- [LinDB](https://github.com/lindb/lindb) - LinDB is a scalable, high performance, high availability distributed time series database.
- [lotusdb](https://github.com/flower-corp/lotusdb) - Fast k/v database compatible with lsm and b+tree.
- [lynxdb](https://github.com/lynxbase/lynxdb) - Lightweight columnar log analytics database with a pipe-style query language inspired by SPL.
- [MemHop](https://github.com/qyiun666/MemHop) - Embedded cognitive memory database for AI agents. Six-layer architecture (L0-L5), Dream consolidation pipeline, three-channel RRF retrieval (BM25 + f16 vector + entity), single .meh file, pure Go, zero infrastructure.
- [Milvus](https://github.com/milvus-io/milvus) - Milvus is a vector database for embedding management, analytics and search.
- [minisql](https://github.com/RichardKnop/minisql) - Embedded single file SQL database.
- [moss](https://github.com/couchbase/moss) - Moss is a simple LSM key-value storage engine written in 100% Go.
- [nanotdb](https://github.com/aymanhs/nanotdb) - A lightweight, zero-dependency, append-only Time-Series Database and Dashboard optimized for low-power hardware.
- [NoKV](https://github.com/feichai0017/NoKV) - Native metadata service for distributed filesystems, object storage, and AI dataset workloads.
- [NornicDB](https://github.com/orneryd/NornicDB) - High performance graph + vector database (Neo4j and qDrant compatible), focused on low latency graph-rag retreival for AI systems. 
- [nutsdb](https://github.com/xujiajun/nutsdb) - Nutsdb is a simple, fast, embeddable, persistent key/value store written in pure Go. It supports fully serializable transactions and many data structures such as list, set, sorted set.
- [objectbox-go](https://github.com/objectbox/objectbox-go) - High-performance embedded Object Database (NoSQL) with Go API.
- [pebble](https://github.com/cockroachdb/pebble) - RocksDB/LevelDB inspired key-value database in Go.
- [piladb](https://github.com/fern4lvarez/piladb) - Lightweight RESTful database engine based on stack data structures.
- [pogreb](https://github.com/akrylysov/pogreb) - Embedded key-value store for read-heavy workloads.
- [prometheus](https://github.com/prometheus/prometheus) - Monitoring system and time series database.
- [pudge](https://github.com/recoilme/pudge) - Fast and simple key/value store written using Go's standard library.
- [redka](https://github.com/nalgeon/redka) - Redis re-implemented with SQLite.
- [rosedb](https://github.com/roseduan/rosedb) - An embedded k-v database based on LSM+WAL, supports string, list, hash, set, zset.
- [rotom](https://github.com/xgzlucario/rotom) - A tiny Redis server built with Golang, compatible with RESP protocols.
- [rqlite](https://github.com/rqlite/rqlite) - The lightweight, distributed, relational database built on SQLite.
- [tempdb](https://github.com/rafaeljesus/tempdb) - Key-value store for temporary items.
- [tidb](https://github.com/pingcap/tidb) - TiDB is a distributed SQL database. Inspired by the design of Google F1.
- [tiedot](https://github.com/HouzuoGuo/tiedot) - Your NoSQL database powered by Golang.
- [unitdb](https://github.com/unit-io/unitdb) - Fast timeseries database for IoT, realtime messaging applications. Access unitdb with pubsub over tcp or websocket using github.com/unit-io/unitd application.
- [Vasto](https://github.com/chrislusf/vasto) - A distributed high-performance key-value store. On Disk. Eventual consistent. HA. Able to grow or shrink without service interruption.
- [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) - fast, resource-effective and scalable open source time series database. May be used as long-term remote storage for Prometheus. Supports PromQL.
- 
<a id="database-schema-migration"></a>
### 数据库模式迁移

- [atlas](https://github.com/ariga/atlas) - A Database Toolkit. A CLI designed to help companies better work with their data.
- [avro](https://github.com/khezen/avro) - Discover SQL schemas and convert them to AVRO schemas. Query SQL records into AVRO bytes.
- [bytebase](https://github.com/bytebase/bytebase) - Safe database schema change and version control for DevOps teams.
- [darwin](https://github.com/GuiaBolso/darwin) - Database schema evolution library for Go.
- [db-migrator.go](https://github.com/raoptimus/db-migrator.go) - CLI for versioned database schema migrations with support for PostgreSQL, MySQL, ClickHouse, Tarantool, and Apache Iceberg.
- [dbmate](https://github.com/amacneil/dbmate) - A lightweight, framework-agnostic database migration tool.
- [go-fixtures](https://github.com/RichardKnop/go-fixtures) - Django style fixtures for Golang's excellent built-in database/sql library.
- [go-pg-migrate](https://github.com/lawzava/go-pg-migrate) - CLI-friendly package for go-pg migrations management.
- [go-pg-migrations](https://github.com/robinjoseph08/go-pg-migrations) - A Go package to help write migrations with go-pg/pg.
- [goavro](https://github.com/linkedin/goavro) - A Go package that encodes and decodes Avro data.
- [godfish](https://github.com/rafaelespinoza/godfish) - Database migration manager, works with native query language. Support for cassandra, mysql, postgres, sqlite3.
- [goose](https://github.com/pressly/goose) - Database migration tool. You can manage your database's evolution by creating incremental SQL or Go scripts.
- [gorm-seeder](https://github.com/Kachit/gorm-seeder) - Simple database seeder for Gorm ORM.
- [gormigrate](https://github.com/go-gormigrate/gormigrate) - Database schema migration helper for Gorm ORM.
- [libschema](https://github.com/muir/libschema) - Define your migrations separately in each library. Migrations for open source libraries. MySQL & PostgreSQL.
- [migrate](https://github.com/golang-migrate/migrate) - Database migrations. CLI and Golang library.
- [migrator](https://github.com/lopezator/migrator) - Dead simple Go database migration library.
- [migrator](https://github.com/larapulse/migrator) - MySQL database migrator designed to run migrations to your features and manage database schema update with intuitive go code.
- [schema](https://github.com/adlio/schema) - Library to embed schema migrations for database/sql-compatible databases inside your Go binaries.
- [skeema](https://github.com/skeema/skeema) - Pure-SQL schema management system for MySQL, with support for sharding and external online schema change tools.
- [soda](https://github.com/gobuffalo/pop/tree/master/soda) - Database migration, creation, ORM, etc... for MySQL, PostgreSQL, and SQLite.
- [sql-migrate](https://github.com/rubenv/sql-migrate) - Database migration tool. Allows embedding migrations into the application using go-bindata.
- [sqlize](https://github.com/sunary/sqlize) - Database migration generator. Allows generate sql migration from model and existing sql by differ them.

<a id="database-tools"></a>
### 数据库工具

- [chproxy](https://github.com/Vertamedia/chproxy) - HTTP proxy for ClickHouse database.
- [clickhouse-bulk](https://github.com/nikepan/clickhouse-bulk) - Collects small inserts and sends big requests to ClickHouse servers.
- [clickhouse-sql-parser](https://github.com/AfterShip/clickhouse-sql-parser) - Parser for ClickHouse-dialect SQL that produces a typed AST, with traversal helpers, round-trip formatting, and a CLI.
- [database-gateway](https://github.com/kazhuravlev/database-gateway) - Running SQL in production with ACLs, logs, and shared links.
- [dbbench](https://github.com/sj14/dbbench) - Database benchmarking tool with support for several databases and scripts.
- [dg](https://github.com/codingconcepts/dg) - A fast data generator that produces CSV files from generated relational data.
- [filesql](https://github.com/nao1215/filesql) - Query CSV, TSV, LTSV, JSON, JSONL, Parquet, Excel, ACH, and Fedwire files with SQL through the database/sql API, backed by in-memory SQLite.
- [gatewayd](https://github.com/gatewayd-io/gatewayd) - Cloud-native database gateway and framework for building data-driven applications. Like API gateways, for databases.
- [go-mysql](https://github.com/siddontang/go-mysql) - Go toolset to handle MySQL protocol and replication.
- [go-postgres-s3-backup](https://github.com/nicobistolfi/go-postgres-s3-backup) - Serverless PostgreSQL backups to S3 using AWS Lambda, with daily, monthly, and yearly rotation.
- [gorm-multitenancy](https://github.com/bartventer/gorm-multitenancy) - Multi-tenancy support for GORM managed databases.
- [GoSQLX](https://github.com/ajitpratap0/GoSQLX) - High-performance SQL parser, formatter, linter, and security scanner with multi-dialect support and WASM playground.
- [hasql](https://golang.yandex/hasql) - Library for accessing multi-host SQL database installations.
- [octillery](https://github.com/knocknote/octillery) - Go package for sharding databases ( Supports every ORM or raw SQL ).
- [onedump](https://github.com/liweiyi88/onedump) - Database backup from different drivers to different destinations with one command and configuration.
- [pg_timetable](https://github.com/cybertec-postgresql/pg_timetable) - Advanced scheduling for PostgreSQL.
- [pgrwl](https://github.com/pgrwl/pgrwl) - Cloud-native continuous backup for PostgreSQL.
- [pgwd](https://github.com/hrodrig/pgwd) - CLI that monitors PostgreSQL connection counts (total, active, idle, stale) and notifies via Slack and/or Loki when thresholds are exceeded. Supports Kubernetes (kubectl port-forward) and optional run context in notifications.
- [pgweb](https://github.com/sosedoff/pgweb) - Web-based PostgreSQL database browser.
- [pgxcli](https://github.com/Balaji01-4D/pgxcli) - PostgreSQL CLI client written in Go, inspired by pgcli.
- [prep](https://github.com/hexdigest/prep) - Use prepared SQL statements without changing your code.
- [pREST](https://github.com/prest/prest) - Simplify and accelerate development, ⚡ instant, realtime, high-performance on any Postgres application, existing or new.
- [rdb](https://github.com/HDT3213/rdb) - Redis RDB file parser for secondary development and memory analysis.
- [rwdb](https://github.com/andizzle/rwdb) - rwdb provides read replica capability for multiple database servers setup.
- [sqly](https://github.com/nao1215/sqly) - Execute SQL against CSV, TSV, LTSV, JSON, Parquet, and Excel files in an interactive shell, backed by in-memory SQLite.
- [vitess](https://github.com/youtube/vitess) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.
- [wescale](https://github.com/wesql/wescale) - WeScale is a database proxy designed to enhance the scalability, performance, security, and resilience of your applications.
- [xsql](https://github.com/zx06/xsql) - AI-first cross-database CLI tool with read-only protection and structured JSON output.

<a id="sql-query-builders"></a>
### SQL 查询构造器

_用于构建和使用 SQL 的库。_

- [bqb](https://github.com/nullism/bqb) - Lightweight and easy to learn query builder.
- [buildsqlx](https://github.com/arthurkushman/buildsqlx) - Go database query builder library for PostgreSQL.
- [builq](https://github.com/cristalhq/builq) - Easily build SQL queries in Go.
- [dba](https://github.com/kran/dba) - SQL query builder for hand-written SQL, adding dynamic conditions, dialect-aware placeholders, and immutable chaining.
- [dbq](https://github.com/rocketlaunchr/dbq) - Zero boilerplate database operations for Go.
- [Dotsql](https://github.com/gchaincl/dotsql) - Go library that helps you keep sql files in one place and use them with ease.
- [gendry](https://github.com/didi/gendry) - Non-invasive SQL builder and powerful data binder.
- [godbal](https://github.com/xujiajun/godbal) - Database Abstraction Layer (dbal) for go. Support SQL builder and get result easily.
- [goqu](https://github.com/doug-martin/goqu) - Idiomatic SQL builder and query library.
- [gosql](https://github.com/twharmon/gosql) - SQL Query builder with better null values support.
- [Hotcoal](https://github.com/motrboat/hotcoal) - Secure your handcrafted SQL against injection.
- [igor](https://github.com/galeone/igor) - Abstraction layer for PostgreSQL that supports advanced functionality and uses gorm-like syntax.
- [jet](https://github.com/go-jet/jet) - Framework for writing type-safe SQL queries in Go, with ability to easily convert database query result into desired arbitrary object structure.
- [obreron](https://github.com/profe-ajedrez/obreron) - Fast and cheap SQL builder which does only one thing, SQL building.
- [ormlite](https://github.com/pupizoid/ormlite) - Lightweight package containing some ORM-like features and helpers for sqlite databases.
- [ozzo-dbx](https://github.com/go-ozzo/ozzo-dbx) - Powerful data retrieval methods as well as DB-agnostic query building capabilities.
- [patcher](https://github.com/Jacobbrewer1/patcher) - Powerful SQL Query builder that automatically generates SQL queries from structs.
- [qrafter](https://github.com/SennovE/qrafter) - Type-safe SQL query builder with dialect-aware rendering, schema introspection, and migration generation.
- [qry](https://github.com/HnH/qry) - Tool that generates constants from files with raw SQL queries.
- [relica](https://github.com/coregx/relica) - Type-safe database query builder with zero production dependencies, LRU statement cache, batch operations, and support for JOINs, subqueries, CTEs, and window functions.
- [sg](https://github.com/go-the-way/sg) - A SQL Gen for generating standard SQLs(supports: CRUD) written in Go.
- [sq](https://github.com/bokwoon95/go-structured-query) - Type-safe SQL builder and struct mapper for Go.
- [sqlc](https://github.com/kyleconroy/sqlc) - Generate type-safe code from SQL.
- [sqlf](https://github.com/leporo/sqlf) - Fast SQL query builder.
- [sqlh](https://github.com/kirill-scherba/sqlh) - Zero-boilerplate SQL helper with struct tags and Go generics (CRUD, UPSERT, JOIN, benchmarks).
- [sqlingo](https://github.com/lqs/sqlingo) - A lightweight DSL to build SQL in Go.
- [sqrl](https://github.com/elgris/sqrl) - SQL query builder, fork of Squirrel with improved performance.
- [Squalus](https://gitlab.com/qosenergy/squalus) - Thin layer over the Go SQL package that makes it easier to perform queries.
- [Squirrel](https://github.com/Masterminds/squirrel) - Go library that helps you build SQL queries.
- [xo](https://github.com/knq/xo) - Generate idiomatic Go code for databases based on existing schema definitions or custom queries supporting PostgreSQL, MySQL, SQLite, Oracle, and Microsoft SQL Server.

**[⬆ 回到顶部](#contents)**

<a id="database-drivers"></a>
## 数据库驱动

<a id="interfaces-to-multiple-backends"></a>
### 多后端接口

- [cayley](https://github.com/google/cayley) - Graph database with support for multiple backends.
- [dsc](https://github.com/viant/dsc) - Datastore connectivity for SQL, NoSQL, structured files.
- [dynamo](https://github.com/fogfish/dynamo) - A simple key-value abstraction to store algebraic and linked-data data types at AWS storage services: AWS DynamoDB and AWS S3.
- [go-transaction-manager](https://github.com/avito-tech/go-transaction-manager) - Transaction manager with multiple adapters (sql, sqlx, gorm, mongo, ...) controls transaction boundaries.
- [gokv](https://github.com/philippgille/gokv) - Simple key-value store abstraction and implementations for Go (Redis, Consul, etcd, bbolt, BadgerDB, LevelDB, Memcached, DynamoDB, S3, PostgreSQL, MongoDB, CockroachDB and many more).
- [transactor](https://github.com/metalfm/transactor) - Type-safe transaction boundary abstraction with adapters for database/sql, sqlx, and pgx.

<a id="relational-database-drivers"></a>
### 关系型数据库驱动

- [avatica](https://github.com/apache/calcite-avatica-go) - Apache Avatica/Phoenix SQL driver for database/sql.
- [bgc](https://github.com/viant/bgc) - Datastore Connectivity for BigQuery for go.
- [firebirdsql](https://github.com/nakagami/firebirdsql) - Firebird RDBMS SQL driver for Go.
- [go-adodb](https://github.com/mattn/go-adodb) - Microsoft ActiveX Object DataBase driver for go that uses database/sql.
- [go-mssqldb](https://github.com/denisenkom/go-mssqldb) - Microsoft MSSQL driver for Go.
- [go-mssqldb](https://github.com/microsoft/go-mssqldb) - Microsoft's official Go driver for SQL Server, Azure SQL, Azure Synapse, SQL database in Fabric, and Fabric Data Warehouse. Supports Azure AD, Always Encrypted, bulk operations.
- [go-oci8](https://github.com/mattn/go-oci8) - Oracle driver for go that uses database/sql.
- [go-rqlite](https://github.com/rqlite/gorqlite) - A Go client for rqlite, providing easy-to-use abstractions for working with the rqlite API.
- [go-sql-driver/mysql](https://github.com/go-sql-driver/mysql) - MySQL driver for Go.
- [go-sqlite3](https://github.com/mattn/go-sqlite3) - SQLite3 driver for go that uses database/sql.
- [go-sqlite3](https://github.com/ncruces/go-sqlite3) - This Go module is compatible with the database/sql driver. It allows embedding SQLite into your application, provides direct access to its C API, supports SQLite VFS, and also includes a GORM driver.
- [godror](https://github.com/godror/godror) - Oracle driver for Go, using the ODPI-C driver.
- [gofreetds](https://github.com/minus5/gofreetds) - Microsoft MSSQL driver. Go wrapper over [FreeTDS](https://www.freetds.org).
- [KSQL](https://github.com/VinGarcia/ksql) - A Simple and Powerful Golang SQL Library.
- [pgx](https://github.com/jackc/pgx) - PostgreSQL driver supporting features beyond those exposed by database/sql.
- [pig](https://github.com/alexeyco/pig) - Simple [pgx](https://github.com/jackc/pgx) wrapper to execute and [scan](https://github.com/georgysavva/scany) query results easily.
- [pq](https://github.com/lib/pq) - Pure Go Postgres driver for database/sql.
- [Sqinn-Go](https://github.com/cvilsmeier/sqinn-go) - SQLite with pure Go.
- [sqlhooks](https://github.com/qustavo/sqlhooks) - Attach hooks to any database/sql driver.
- [sqlite](https://pkg.go.dev/modernc.org/sqlite) - Package sqlite is a sql/database driver using a CGo-free port of the C SQLite3 library.
- [surrealdb.go](https://github.com/surrealdb/surrealdb.go) - SurrealDB Driver for Go.
- [ydb-go-sdk](https://github.com/ydb-platform/ydb-go-sdk) - native and database/sql driver YDB (Yandex Database).

<a id="nosql-database-drivers"></a>
### NoSQL 数据库驱动

- [aerospike-client-go](https://github.com/aerospike/aerospike-client-go) - Aerospike client in Go language.
- [arangolite](https://github.com/solher/arangolite) - Lightweight golang driver for ArangoDB.
- [asc](https://github.com/viant/asc) - Datastore Connectivity for Aerospike for go.
- [forestdb](https://github.com/couchbase/goforestdb) - Go bindings for ForestDB.
- [go-couchbase](https://github.com/couchbase/go-couchbase) - Couchbase client in Go.
- [go-mongox](https://github.com/chenmingyong0423/go-mongox) - A Go Mongo library based on the official driver, featuring streamlined document operations, generic binding of structs to collections, built-in CRUD, aggregation, automated field updates, struct validation, hooks, and plugin-based programming.
- [go-pilosa](https://github.com/pilosa/go-pilosa) - Go client library for Pilosa.
- [go-rejson](https://github.com/nitishm/go-rejson) - Golang client for redislabs' ReJSON module using Redigo golang client. Store and manipulate structs as JSON objects in redis with ease.
- [gocb](https://github.com/couchbase/gocb) - Official Couchbase Go SDK.
- [gocosmos](https://github.com/btnguyen2k/gocosmos) - REST client and standard `database/sql` driver for Azure Cosmos DB.
- [gocql](https://gocql.github.io) - Go language driver for Apache Cassandra.
- [godis](https://github.com/piaohao/godis) - redis client implement by golang, inspired by jedis.
- [godscache](https://github.com/defcronyke/godscache) - A wrapper for the Google Cloud Platform Go Datastore package that adds caching using memcached.
- [gomemcache](https://github.com/bradfitz/gomemcache/) - memcache client library for the Go programming language.
- [gomemcached](https://github.com/aliexpressru/gomemcached) - A binary Memcached client for Go with support for sharding using consistent hashing, along with SASL.
- [gorethink](https://github.com/dancannon/gorethink) - Go language driver for RethinkDB.
- [goriak](https://github.com/zegl/goriak) - Go language driver for Riak KV.
- [Kivik](https://github.com/go-kivik/kivik) - Kivik provides a common Go and GopherJS client library for CouchDB, PouchDB, and similar databases.
- [mgm](https://github.com/kamva/mgm) - MongoDB model-based ODM for Go (based on official MongoDB driver).
- [mgo](https://github.com/globalsign/mgo) - (unmaintained) MongoDB driver for the Go language that implements a rich and well tested selection of features under a very simple API following standard Go idioms.
- [mongo-go-driver](https://github.com/mongodb/mongo-go-driver) - Official MongoDB driver for the Go language.
- [neo4j](https://github.com/cihangir/neo4j) - Neo4j Rest API Bindings for Golang.
- [neoism](https://github.com/jmcvetta/neoism) - Neo4j client for Golang.
- [qmgo](https://github.com/qiniu/qmgo) - The MongoDB driver for Go. It‘s based on official MongoDB driver but easier to use like Mgo.
- [redeo](https://github.com/bsm/redeo) - Redis-protocol compatible TCP servers/services.
- [redigo](https://github.com/gomodule/redigo) - Redigo is a Go client for the Redis database.
- [redis](https://github.com/redis/go-redis) - Redis client for Golang.
- [rueidis](http://github.com/rueian/rueidis) - Fast Redis RESP3 client with auto pipelining and server-assisted client side caching.
- [xredis](https://github.com/shomali11/xredis) - Typesafe, customizable, clean & easy to use Redis client.

<a id="search-and-analytic-databases"></a>
### 搜索与分析型数据库

- [clickhouse-go](https://github.com/ClickHouse/clickhouse-go/) - ClickHouse SQL client for Go with a `database/sql` compatibility.
- [effdsl](https://github.com/sdqri/effdsl) - Elasticsearch query builder for Go.
- [elastic](https://github.com/olivere/elastic) - Elasticsearch client for Go.
- [elasticsql](https://github.com/cch123/elasticsql) - Convert sql to elasticsearch dsl in Go.
- [elastigo](https://github.com/mattbaird/elastigo) - Elasticsearch client library.
- [go-elasticsearch](https://github.com/elastic/go-elasticsearch) - Official Elasticsearch client for Go.
- [goes](https://github.com/OwnLocal/goes) - Library to interact with Elasticsearch.
- [skizze](https://github.com/skizzehq/skizze) - A probabilistic data structure service and storage.
- [zoekt](https://github.com/sourcegraph/zoekt) - Fast trigram based code search.

**[⬆ 回到顶部](#contents)**

<a id="date-and-time"></a>
## 日期与时间

_用于处理日期与时间的库。_

- [approx](https://github.com/goschtalt/approx) - A Duration extension supporting parsing/printing durations in days, weeks and years.
- [carbon](https://github.com/dromara/carbon) - A simple, semantic and developer-friendly time package for golang.
- [carbon](https://github.com/uniplaces/carbon) - Simple Time extension with a lot of util methods, ported from PHP Carbon library.
- [cronrange](https://github.com/1set/cronrange) - Parses Cron-style time range expressions, checks if the given time is within any ranges.
- [date](https://github.com/rickb777/date) - Augments Time for working with dates, date ranges, time spans, periods, and time-of-day.
- [dateparse](https://github.com/araddon/dateparse) - Parse date's without knowing format in advance.
- [durafmt](https://github.com/hako/durafmt) - Time duration formatting library for Go.
- [feiertage](https://github.com/wlbr/feiertage) - Set of functions to calculate public holidays in Germany, incl. specialization on the states of Germany (Bundesländer). Things like Easter, Pentecost, Thanksgiving...
- [go-anytime](https://github.com/ijt/go-anytime) - Parse dates/times like "next dec 22nd at 3pm" and ranges like "from today until next thursday" without knowing the format in advance.
- [go-date-fns](https://github.com/chmenegatti/go-date-fns) - A comprehensive date utility library for Go, inspired by date-fns, with 140+ pure and immutable functions.
- [go-datebin](https://github.com/deatil/go-datebin) - A simple datetime parse pkg.
- [go-faketime](https://github.com/harkaitz/go-faketime) - A simple `time.Now()` that honors the faketime(1) utility.
- [go-persian-calendar](https://github.com/yaa110/go-persian-calendar) - The implementation of the Persian (Solar Hijri) Calendar in Go (golang).
- [go-str2duration](https://github.com/xhit/go-str2duration) - Convert string to duration. Support time.Duration returned string and more.
- [go-sunrise](https://github.com/nathan-osman/go-sunrise) - Calculate the sunrise and sunset times for a given location.
- [go-week](https://github.com/stoewer/go-week) - An efficient package to work with ISO8601 week dates.
- [gostradamus](https://github.com/bykof/gostradamus) - A Go package for working with dates.
- [iso8601](https://github.com/relvacode/iso8601) - Efficiently parse ISO8601 date-times without regex.
- [kair](https://github.com/GuilhermeCaruso/kair) - Date and Time - Golang Formatting Library.
- [now](https://github.com/jinzhu/now) - Now is a time toolkit for golang.
- [strftime](https://github.com/awoodbeck/strftime) - C99-compatible strftime formatter.
- [timespan](https://github.com/SaidinWoT/timespan) - For interacting with intervals of time, defined as a start time and a duration.
- [timeutil](https://github.com/leekchan/timeutil) - Useful extensions (Timedelta, Strftime, ...) to the golang's time package.
- [tuesday](https://github.com/osteele/tuesday) - Ruby-compatible Strftime function.

**[⬆ 回到顶部](#contents)**

<a id="distributed-systems"></a>
## 分布式系统

_有助于构建分布式系统的软件包。_

- [arpc](https://github.com/lesismal/arpc) - More effective network communication, support two-way-calling, notify, broadcast.
- [bedrock](https://github.com/z5labs/bedrock) - Provides a minimal, modular and composable foundation for quickly developing services and more use case specific frameworks in Go.
- [capillaries](https://github.com/capillariesio/capillaries) - distributed batch data processing framework.
- [circuit](https://github.com/schigh/circuit) - Circuit breaker with gradual recovery via probabilistic throttling.
- [cmd-stream-go](https://github.com/cmd-stream/cmd-stream-go) - High-performance distributed command pattern library for Go.
- [committer](https://github.com/vadiminshakov/committer) - A distributed transactions management system (2PC/3PC implementation).
- [consistent](https://github.com/buraksezer/consistent) - Consistent hashing with bounded loads.
- [consistenthash](https://github.com/mbrostami/consistenthash) - Consistent hashing with configurable replicas.
- [dht](https://github.com/anacrolix/dht) - BitTorrent Kademlia DHT implementation.
- [digota](https://github.com/digota/digota) - grpc ecommerce microservice.
- [dot](https://github.com/dotchain/dot/) - distributed sync using operational transformation/OT.
- [doublejump](https://github.com/edwingeng/doublejump) - A revamped Google's jump consistent hash.
- [dragonboat](https://github.com/lni/dragonboat) - A feature complete and high performance multi-group Raft library in Go.
- [Dragonfly](https://github.com/dragonflyoss/Dragonfly2) - Provide efficient, stable and secure file distribution and image acceleration based on p2p technology to be the best practice and standard solution in cloud native architectures.
- [drmaa](https://github.com/dgruber/drmaa) - Job submission library for cluster schedulers based on the DRMAA standard.
- [dynamolock](https://cirello.io/dynamolock) - DynamoDB-backed distributed locking implementation.
- [dynatomic](https://github.com/tylfin/dynatomic) - A library for using DynamoDB as an atomic counter.
- [emitter-io](https://github.com/emitter-io/emitter) - High performance, distributed, secure and low latency publish-subscribe platform built with MQTT, Websockets and love.
- [evans](https://github.com/ktr0731/evans) - Evans: more expressive universal gRPC client.
- [failured](https://github.com/andy2046/failured) - adaptive accrual failure detector for distributed systems.
- [flowgraph](https://github.com/vectaport/flowgraph) - flow-based programming package.
- [gleam](https://github.com/chrislusf/gleam) - Fast and scalable distributed map/reduce system written in pure Go and Luajit, combining Go's high concurrency with Luajit's high performance, runs standalone or distributed.
- [glow](https://github.com/chrislusf/glow) - Easy-to-Use scalable distributed big data processing, Map-Reduce, DAG execution, all in pure Go.
- [gmsec](https://github.com/gmsec/micro) - A Go distributed systems development framework.
- [go-doudou](https://github.com/unionj-cloud/go-doudou) - A gossip protocol and OpenAPI 3.0 spec based decentralized microservice framework. Built-in go-doudou cli focusing on low-code and rapid dev can power up your productivity.
- [go-eagle](https://github.com/go-eagle/eagle) - A Go framework for the API or Microservice with handy scaffolding tools.
- [go-jump](https://github.com/dgryski/go-jump) - Port of Google's "Jump" Consistent Hash function.
- [go-kit](https://github.com/go-kit/kit) - Microservice toolkit with support for service discovery, load balancing, pluggable transports, request tracking, etc.
- [go-micro](https://github.com/micro/go-micro) - A distributed systems development framework.
- [go-mysql-lock](https://github.com/sanketplus/go-mysql-lock) - MySQL based distributed lock.
- [go-pdu](https://github.com/pdupub/go-pdu) - A decentralized identity-based social network.
- [go-sundheit](https://github.com/AppsFlyer/go-sundheit) - A library built to provide support for defining async service health checks for golang services.
- [go-zero](https://github.com/tal-tech/go-zero) - A web and rpc framework. It's born to ensure the stability of the busy sites with resilient design. Builtin goctl greatly improves the development productivity.
- [gorpc](https://github.com/valyala/gorpc) - Simple, fast and scalable RPC library for high load.
- [grpc-go](https://github.com/grpc/grpc-go) - The Go language implementation of gRPC. HTTP/2 based RPC.
- [health](https://github.com/schigh/health) - Health checker for Go services with Kubernetes probe support.
- [hprose](https://github.com/hprose/hprose-golang) - Very newbility RPC Library, support 25+ languages now.
- [jsonrpc](https://github.com/osamingo/jsonrpc) - The jsonrpc package helps implement of JSON-RPC 2.0.
- [jsonrpc](https://github.com/ybbus/jsonrpc) - JSON-RPC 2.0 HTTP client implementation.
- [K8gb](https://github.com/k8gb-io/k8gb) - A cloud native Kubernetes Global Balancer.
- [Kitex](https://github.com/cloudwego/kitex) - A high-performance and strong-extensibility Golang RPC framework that helps developers build microservices. If the performance and extensibility are the main concerns when you develop microservices, Kitex can be a good choice.
- [Kratos](https://github.com/go-kratos/kratos) - A modular-designed and easy-to-use microservices framework in Go.
- [liftbridge](https://github.com/liftbridge-io/liftbridge) - Lightweight, fault-tolerant message streams for NATS.
- [lock](https://github.com/ubgo/lock) - Distributed lock family with one Go interface and five backends (filelock, flock, Redis, Postgres, etcd) — fencing tokens, semaphore mode, and observability hooks across all backends.
- [lura](https://github.com/luraproject/lura) - Ultra performant API Gateway framework with middlewares.
- [mochi mqtt](https://github.com/mochi-co/mqtt) - Fully spec compliant, embeddable high-performance MQTT v5/v3 broker for IoT, smarthome, and pubsub.
- [NATS](https://github.com/nats-io/nats-server) - NATS is a simple, secure, and performant communications system for digital systems, services, and devices.
- [opentelemetry-go-auto-instrumentation](https://github.com/alibaba/opentelemetry-go-auto-instrumentation) - OpenTelemetry Compile-Time Instrumentation for Golang.
- [oras](https://github.com/oras-project/oras) - CLI and library for OCI Artifacts in container registries.
- [outbox](https://github.com/oagudo/outbox) - Lightweight library for the transactional outbox pattern in Go, not tied to any specific relational database or broker.
- [outboxer](https://github.com/italolelis/outboxer) - Outboxer is a go library that implements the outbox pattern.
- [pglock](https://cirello.io/pglock) - PostgreSQL-backed distributed locking implementation.
- [pjrpc](https://gitlab.com/pjrpc/pjrpc) - Golang JSON-RPC Server-Client with Protobuf spec.
- [raft](https://github.com/hashicorp/raft) - Golang implementation of the Raft consensus protocol, by HashiCorp.
- [raft](https://github.com/etcd-io/raft) - Go implementation of the Raft consensus protocol, by CoreOS.
- [rain](https://github.com/cenkalti/rain) - BitTorrent client and library.
- [redis-lock](https://github.com/bsm/redislock) - Simplified distributed locking implementation using Redis.
- [resgate](https://resgate.io/) - Realtime API Gateway for building REST, real time, and RPC APIs, where all clients are synchronized seamlessly.
- [rpcplatform](https://github.com/nexcode/rpcplatform) - Framework for microservices with service discovery, load balancing, and related features.
- [rpcx](https://github.com/smallnest/rpcx) - Distributed pluggable RPC service framework like alibaba Dubbo.
- [Semaphore](https://github.com/jexia/semaphore) - A straightforward (micro) service orchestrator.
- [servicepack](https://github.com/psyb0t/servicepack) - Framework for running multiple services concurrently in a single binary, locally or distributed across machines.
- [sleuth](https://github.com/ursiform/sleuth) - Library for master-less p2p auto-discovery and RPC between HTTP services (using [ZeroMQ](https://github.com/zeromq/libzmq)).
- [sponge](https://github.com/zhufuyi/sponge) - A distributed development framework that integrates automatic code generation, gin and grpc frameworks, base development frameworks.
- [Tarmac](https://github.com/tarmac-project/tarmac) - Framework for writing functions, microservices, or monoliths with WebAssembly
- [Temporal](https://github.com/temporalio/sdk-go) - Durable execution system for making code fault-tolerant and simple.
- [torrent](https://github.com/anacrolix/torrent) - BitTorrent client package.
- [trpc-go](https://github.com/trpc-group/trpc-go) - The Go language implementation of tRPC, which is a pluggable, high-performance RPC framework.

**[⬆ 回到顶部](#contents)**

<a id="dynamic-dns"></a>
## 动态 DNS

_用于更新动态 DNS 记录的工具。_

- [DDNS](https://github.com/skibish/ddns) - Personal DDNS client with Digital Ocean Networking DNS as backend.
- [dyndns](https://gitlab.com/alcastle/dyndns) - Background Go process to regularly and automatically check your IP Address and make updates to (one or many) Dynamic DNS records for Google domains whenever your address changes.
- [GoDNS](https://github.com/timothyye/godns) - A dynamic DNS client tool, supports DNSPod & HE.net, written in Go.

**[⬆ 回到顶部](#contents)**

<a id="email"></a>
## 邮件

_实现邮件创建与发送的库与工具。_

- [chasquid](https://blitiri.com.ar/p/chasquid) - SMTP server written in Go.
- [douceur](https://github.com/aymerick/douceur) - CSS inliner for your HTML emails.
- [email](https://github.com/jordan-wright/email) - A robust and flexible email library for Go.
- [email-verifier](https://github.com/AfterShip/email-verifier) - A Go library for email verification without sending any emails.
- [go-dkim](https://github.com/toorop/go-dkim) - DKIM library, to sign & verify email.
- [go-email-normalizer](https://github.com/dimuska139/go-email-normalizer) - Golang library for providing a canonical representation of email address.
- [go-imap](https://github.com/BrianLeishman/go-imap) - Batteries-included IMAP client with auto-reconnect, OAuth2, IDLE support, and built-in MIME parsing.
- [go-imap](https://github.com/emersion/go-imap) - IMAP library for clients and servers.
- [go-mail](https://github.com/wneessen/go-mail) - A simple Go library for sending mails in Go.
- [go-message](https://github.com/emersion/go-message) - Streaming library for the Internet Message Format and mail messages.
- [go-premailer](https://github.com/vanng822/go-premailer) - Inline styling for HTML mail in Go.
- [go-simple-mail](https://github.com/xhit/go-simple-mail) - Very simple package to send emails with SMTP Keep Alive and two timeouts: Connect and Send.
- [go-spamcheck](https://github.com/psyb0t/go-spamcheck) - Client for Postmark's SpamCheck API that scores a raw email against SpamAssassin rules.
- [Hectane](https://github.com/hectane/hectane) - Lightweight SMTP client providing an HTTP API.
- [hermes](https://github.com/matcornic/hermes) - Golang package that generates clean, responsive HTML e-mails.
- [Maddy](https://github.com/foxcpp/maddy) - All-in-one (SMTP, IMAP, DKIM, DMARC, MTA-STS, DANE) email server
- [mailchain](https://github.com/mailchain/mailchain) - Send encrypted emails to blockchain addresses written in Go.
- [mailgun-go](https://github.com/mailgun/mailgun-go) - Go library for sending mail with the Mailgun API.
- [MailHog](https://github.com/mailhog/MailHog) - Email and SMTP testing with web and API interface.
- [Mailpit](https://github.com/axllent/mailpit) - Email and SMTP testing tool for developers.
- [mailx](https://github.com/valord577/mailx) - Mailx is a library that makes it easier to send email via SMTP. It is an enhancement of the golang standard library `net/smtp`.
- [mox](https://github.com/mjl-/mox) - Modern full-featured secure mail server for low-maintenance, self-hosted email.
- [SendGrid](https://github.com/sendgrid/sendgrid-go) - SendGrid's Go library for sending email.
- [smtp](https://github.com/mailhog/smtp) - SMTP server protocol state machine.
- [smtpmock](https://github.com/mocktools/go-smtp-mock) - Lightweight configurable multithreaded fake SMTP server. Mimic any SMTP behaviour for your test environment.
- [tickstem/verify](https://github.com/tickstem/verify) - Validate email addresses before they hit your database: syntax, MX lookup, disposable domains, and role-based inboxes.
- [truemail-go](https://github.com/truemail-rb/truemail-go) - Configurable Golang email validator/verifier. Verify email via Regex, DNS, SMTP and even more.

**[⬆ 回到顶部](#contents)**

<a id="embeddable-scripting-languages"></a>
## 可嵌入式脚本语言

_在 Go 代码中嵌入其他语言。_

- [anko](https://github.com/mattn/anko) - Scriptable interpreter written in Go.
- [binder](https://github.com/alexeyco/binder) - Go to Lua binding library, based on [gopher-lua](https://github.com/yuin/gopher-lua).
- [cel-go](https://github.com/google/cel-go) - Fast, portable, non-Turing complete expression evaluation with gradual typing.
- [ecal](https://github.com/krotik/ecal) - A simple embeddable scripting language which supports concurrent event processing.
- [expr](https://github.com/antonmedv/expr) - Expression evaluation engine for Go: fast, non-Turing complete, dynamic typing, static typing.
- [FrankenPHP](https://github.com/dunglas/frankenphp) - PHP embedded in Go, with a `net/http` handler.
- [gentee](https://github.com/gentee/gentee) - Embeddable scripting programming language.
- [gisp](https://github.com/jcla1/gisp) - Simple LISP in Go.
- [go-lua](https://github.com/Shopify/go-lua) - Port of the Lua 5.2 VM to pure Go.
- [go-lua](https://github.com/speedata/go-lua) - Lua 5.4 VM implemented in pure Go.
- [go-php](https://github.com/deuill/go-php) - PHP bindings for Go.
- [goal](https://codeberg.org/anaseto/goal) - An embeddable scripting array language.
- [goja](https://github.com/dop251/goja) - ECMAScript 5.1(+) implementation in Go.
- [golua](https://github.com/aarzilli/golua) - Go bindings for Lua C API.
- [gopher-lua](https://github.com/yuin/gopher-lua) - Lua 5.1 VM and compiler written in Go.
- [gval](https://github.com/PaesslerAG/gval) - A highly customizable expression language written in Go.
- [metacall](https://github.com/metacall/core) - Cross-platform Polyglot Runtime which supports NodeJS, JavaScript, TypeScript, Python, Ruby, C#, WebAssembly, Java, Cobol and more.
- [ngaro](https://github.com/db47h/ngaro) - Embeddable Ngaro VM implementation enabling scripting in Retro.
- [prolog](https://github.com/ichiban/prolog) - Embeddable Prolog.
- [purl](https://github.com/ian-kent/purl) - Perl 5.18.2 embedded in Go.
- [starlark-go](https://github.com/google/starlark-go) - Go implementation of Starlark: Python-like language with deterministic evaluation and hermetic execution.
- [starlet](https://github.com/1set/starlet) - Go wrapper for [starlark-go](https://github.com/google/starlark-go) that simplifies script execution, offers data conversion, and useful Starlark libraries and extensions.
- [tengo](https://github.com/d5/tengo) - Bytecode compiled script language for Go.
- [Wa/凹语言](https://github.com/wa-lang/wa) - The Wa Programming Language embedded in Go.

**[⬆ 回到顶部](#contents)**

<a id="error-handling"></a>
## 错误处理

_用于错误处理的库。_

- [ctxerrors](https://github.com/psyb0t/ctxerrors) - Wrap errors with the file, line, and function name of each call site.
- [emperror](https://github.com/emperror/emperror) - Error handling tools and best practices for Go libraries and applications.
- [eris](https://github.com/rotisserie/eris) - A better way to handle, trace, and log errors in Go. Compatible with the standard error library and github.com/pkg/errors.
- [errlog](https://github.com/snwfdhmp/errlog) - Hackable package that determines responsible source code for an error (and some other fast-debugging features). Pluggable to any logger in-place.
- [errors](https://github.com/emperror/errors) - Drop-in replacement for the standard library errors package and github.com/pkg/errors. Provides various error handling primitives.
- [errors](https://github.com/neuronlabs/errors) - Simple golang error handling with classification primitives.
- [errors](https://github.com/PumpkinSeed/errors) - The most simple error wrapper with awesome performance and minimal memory overhead.
- [errors](https://gitlab.com/tozd/go/errors) - Providing errors with a stack trace and optional structured details. Compatible with github.com/pkg/errors API but does not use it internally.
- [errors](https://github.com/naughtygopher/errors) - Drop-in replacement for builtin Go errors. This is a minimal error handling package with custom error types, user friendly messages, Unwrap & Is. With very easy to use and straightforward helper functions.
- [errors](https://github.com/cockroachdb/errors) - Go error library with error portability over the network.
- [errorx](https://github.com/joomcode/errorx) - A feature rich error package with stack traces, composition of errors and more.
- [exception](https://github.com/rbrahul/exception) - A simple utility package for exception handling with try-catch in Golang.
- [Falcon](https://github.com/SonicRoshan/falcon) - A Simple Yet Highly Powerful Package For Error Handling.
- [Fault](https://github.com/Southclaws/fault) - An ergonomic mechanism for wrapping errors in order to facilitate structured metadata and context for error values.
- [go-errr](https://github.com/go-errr/go) - Error handling library with Catch/Recover semantics, wrapped error chains, and stack traces for Go.
- [go-multierror](https://github.com/hashicorp/go-multierror) - Go (golang) package for representing a list of errors as a single error.
- [metaerr](https://github.com/quantumcycle/metaerr) - A library to create your custom error builders producing structured errors with metadata from different sources and optional stacktraces.
- [multierr](https://github.com/uber-go/multierr) - Package for representing a list of errors as a single error.
- [oops](https://github.com/samber/oops) - Error handling with context, stack trace and source fragments.
- [tracerr](https://github.com/ztrue/tracerr) - Golang errors with stack trace and source fragments.

**[⬆ 回到顶部](#contents)**

<a id="file-handling"></a>
## 文件处理

_用于处理文件与文件系统的库。_

- [afero](https://github.com/spf13/afero) - FileSystem Abstraction System for Go.
- [afs](https://github.com/viant/afs) - Abstract File Storage (mem, scp, zip, tar, cloud: s3, gs) for Go.
- [baraka](https://github.com/xis/baraka) - A library to process http file uploads easily.
- [checksum](https://github.com/codingsince1985/checksum) - Compute message digest, like MD5, SHA256, SHA1, CRC or BLAKE2s, for large files.
- [copy](https://github.com/otiai10/copy) - Copy directory recursively.
- [fastwalk](https://github.com/charlievieth/fastwalk) - Fast parallel directory traversal library (used by [fzf](https://github.com/junegunn/fzf)).
- [flop](https://github.com/homedepot/flop) - File operations library which aims to mirror feature parity with [GNU cp](https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html).
- [gdu](https://github.com/dundee/gdu) - Disk usage analyzer with console interface.
- [go-csv-tag](https://github.com/artonge/go-csv-tag) - Load csv file using tag.
- [go-decent-copy](https://github.com/hugocarreira/go-decent-copy) - Copy files for humans.
- [go-exiftool](https://github.com/barasher/go-exiftool) - Go bindings for ExifTool, the well-known library used to extract as much metadata as possible (EXIF, IPTC, ...) from files (pictures, PDF, office, ...).
- [go-gtfs](https://github.com/artonge/go-gtfs) - Load gtfs files in go.
- [go-wkhtmltopdf](https://github.com/SebastiaanKlippert/go-wkhtmltopdf) - A package to convert an HTML template to a PDF file.
- [gofs](https://github.com/no-src/gofs) - A cross-platform real-time file synchronization tool out of the box.
- [gopdfrab](https://github.com/voidrab/gopdfrab) - PDF/A processing for Go.
- [gulter](https://github.com/adelowo/gulter) - A simple HTTP middleware to automatically handle all your file upload needs
- [gut/yos](https://github.com/1set/gut) - Simple and reliable package for file operations like copy/move/diff/list on files, directories and symbolic links.
- [gxpdf](https://github.com/coregx/gxpdf) - Modern full-lifecycle PDF library for Go — parse, extract tables, generate, and sign documents with zero CGO dependencies.
- [higgs](https://github.com/dastoori/higgs) - A tiny cross-platform Go library to hide/unhide files and directories.
- [iso9660](https://github.com/kdomanski/iso9660) - A package for reading and creating ISO9660 disk images
- [notify](https://github.com/rjeczalik/notify) - File system event notification library with simple API, similar to os/signal.
- [opc](https://github.com/qmuntal/opc) - Load Open Packaging Conventions (OPC) files for Go.
- [parquet](https://github.com/parsyl/parquet) - Read and write [parquet](https://parquet.apache.org) files.
- [pathtype](https://github.com/jonchun/pathtype) - Treat paths as their own type instead of using strings.
- [pdfcpu](https://github.com/pdfcpu/pdfcpu) - PDF processor.
- [skywalker](https://github.com/dixonwille/skywalker) - Package to allow one to concurrently go through a filesystem with ease.
- [todotxt](https://github.com/1set/todotxt) - Go library for Gina Trapani's [_todo.txt_](http://todotxt.org/) files, supports parsing and manipulating of task lists in the [_todo.txt_ format](https://github.com/todotxt/todo.txt).
- [vfs](https://github.com/C2FO/vfs) - A pluggable, extensible, and opinionated set of filesystem functionality for Go across a number of filesystem types such as os, S3, and GCS.

**[⬆ 回到顶部](#contents)**

<a id="financial"></a>
## 金融

_用于会计与金融的软件包。_

- [accounting](https://github.com/leekchan/accounting) - money and currency formatting for golang.
- [ach](https://github.com/moov-io/ach) - A reader, writer, and validator for Automated Clearing House (ACH) files.
- [bbgo](https://github.com/c9s/bbgo) - A crypto trading bot framework written in Go. Including common crypto exchange API, standard indicators, back-testing and many built-in strategies.
- [bingx-go](https://github.com/tigusigalpa/bingx-go) - Go client for BingX API v3 with 260+ methods, USDT-M/Coin-M futures, spot, TradFi, WebSocket streams, and copy trading.
- [bitget-go](https://github.com/tigusigalpa/bitget-go) - Go client for Bitget UTA API v3 with typed models, string-based prices, auto-reconnecting WebSocket, and demo trading.
- [bybit-go](https://github.com/tigusigalpa/bybit-go) - Go client for Bybit V5 API with HMAC/RSA authentication, WebSocket streams, demo trading, and TradFi instruments.
- [cnn-fear-and-greed-parse](https://github.com/wildsurfer/cnn-fear-and-greed-parse) - Client for CNN's Fear & Greed Index with the seven component indicators and about a year of daily history.
- [currency](https://github.com/bojanz/currency) - Handles currency amounts, provides currency information and formatting.
- [currency](https://github.com/naughtygopher/currency) - High performant & accurate currency computation package.
- [dec128](https://github.com/jokruger/dec128) - High performance 128-bit fixed-point decimal numbers.
- [decimal](https://github.com/shopspring/decimal) - Arbitrary-precision fixed-point decimal numbers.
- [decimal](https://github.com/aytechnet/decimal) - High performance 64-bit decimal partially compatible with [shopspring/decimal](https://github.com/shopspring/decimal) and int64, including Weight and Length.
- [decimal](https://github.com/govalues/decimal) - Immutable decimal numbers with panic-free arithmetic.
- [decimal](https://github.com/klokare/decimal) - A fixed-size, no allocation decimal type for when you don't need arbitrary precision.
- [eu-vat-rates-data-go](https://github.com/vatnode/eu-vat-rates-data-go) - VAT rates and VAT number formats for 45 European countries, embedded at compile time and refreshed daily from the European Commission TEDB.
- [fpdecimal](https://github.com/nikolaydubina/fpdecimal) - Fast and precise serialization and arithmetic for small fixed-point decimals
- [fpmoney](https://github.com/nikolaydubina/fpmoney) - Fast and simple ISO4217 fixed-point decimal money.
- [glassnode-go](https://github.com/tigusigalpa/glassnode-go) - Go client for Glassnode Basic API with 25 metric categories, typed structs, bulk endpoints, Point-in-Time data, and zero dependencies.
- [go-finance](https://github.com/alpeb/go-finance) - Library of financial functions for time value of money (annuities), cash flow, interest rate conversions, bonds and depreciation calculations.
- [go-finance](https://github.com/pieterclaerhout/go-finance) - Module to fetch exchange rates, check VAT numbers via VIES and check IBAN bank account numbers.
- [go-money](https://github.com/rhymond/go-money) - Implementation of Fowler's Money pattern.
- [go-nowpayments](https://github.com/matm/go-nowpayments) - Library for the crypto NOWPayments API.
- [gobl](https://github.com/invopop/gobl) - Invoice and billing document framework. JSON Schema based. Automates tax calculations and validation, with tooling to convert into global formats.
- [indicator](https://github.com/cinar/indicator) - Technical analysis library providing financial indicators, strategies, and backtesting framework.
- [kucoin-go](https://github.com/tigusigalpa/kucoin-go) - Go client for KuCoin UTA and Classic REST & WebSocket APIs with HMAC-SHA256 auth, string-typed prices, and typed error hierarchy.
- [ledger](https://github.com/formancehq/ledger) - A programmable financial ledger that provides a foundation for money-moving applications.
- [money](https://github.com/govalues/money) - Immutable monetary amounts and exchange rates with panic-free arithmetic.
- [ofxgo](https://github.com/aclindsa/ofxgo) - Query OFX servers and/or parse the responses (with example command-line client).
- [okx-go](https://github.com/tigusigalpa/okx-go) - Go client for OKX v5 API with 335 REST endpoints, 53 WebSocket channels, generics support and auto-reconnect.
- [orderbook](https://github.com/i25959341/orderbook) - Matching Engine for Limit Order Book in Golang.
- [orderbook](https://github.com/intrepidkarthi/orderbook) - Embeddable limit order book and matching engine with integer-exact pricing, a single-writer core, and write-ahead-log crash recovery.
- [payme](https://github.com/jovandeginste/payme) - QR code generator (ASCII & PNG) for SEPA payments.
- [paystack-sdk-go](https://github.com/samaasi/paystack-sdk-go) - A comprehensive, zero-dependency, and fully typed Go SDK for the Paystack API.
- [swift](https://code.pfad.fr/swift/) - Offline validity check of IBAN (International Bank Account Number) and retrieval of BIC (for some countries).
- [techan](https://github.com/sdcoffey/techan) - Technical analysis library with advanced market analysis and trading strategies.
- [telegram-wallet-go](https://github.com/tigusigalpa/telegram-wallet-go) - Go client for Telegram Wallet Pay API with HMAC-SHA256 webhook verification, middleware for net/http, Gin, and Echo.
- [ticker](https://github.com/achannarasappa/ticker) - Terminal stock watcher and stock position tracker.
- [transaction](https://github.com/claygod/transaction) - Embedded transactional database of accounts, running in multithreaded mode.
- [udecimal](https://github.com/quagmt/udecimal) - High performance, high precision, zero allocation fixed-point decimal library for financial applications.
- [vat](https://github.com/dannyvankooten/vat) - VAT number validation & EU VAT rates.

**[⬆ 回到顶部](#contents)**

<a id="forms"></a>
## 表单

_用于处理表单的库。_

- [bind](https://github.com/robfig/bind) - Bind form data to any Go values.
- [conform](https://github.com/leebenson/conform) - Keeps user input in check. Trims, sanitizes & scrubs data based on struct tags.
- [form](https://github.com/go-playground/form) - Decodes url.Values into Go value(s) and Encodes Go value(s) into url.Values. Dual Array and Full map support.
- [formam](https://github.com/monoculum/formam) - decode form's values into a struct.
- [forms](https://github.com/albrow/forms) - Framework-agnostic library for parsing and validating form/JSON data which supports multipart forms and files.
- [gbind](https://github.com/bdjimmy/gbind) - Bind data to any Go value. Can use built-in and custom expression binding capabilities; supports data validation
- [gorilla/csrf](https://github.com/gorilla/csrf) - CSRF protection for Go web applications & services.
- [httpin](https://github.com/ggicci/httpin) - Decode an HTTP request into a custom struct, including querystring, forms, HTTP headers, etc.
- [nosurf](https://github.com/justinas/nosurf) - CSRF protection middleware for Go.
- [qs](https://github.com/sonh/qs) - Go module for encoding structs into URL query parameters.
- [queryparam](https://github.com/tomwright/queryparam) - Decode `url.Values` into usable struct values of standard or custom types.
- [roamer](https://github.com/slipros/roamer) - Eliminates boilerplate code for parsing HTTP requests by binding cookies, headers, query params, path params, body to structs and more by using simple tags.

**[⬆ 回到顶部](#contents)**

<a id="functional"></a>
## 函数式

_支持 Go 函数式编程的软件包。_

- [fp-go](https://github.com/repeale/fp-go) - Collection of Functional Programming helpers powered by Golang 1.18+ generics.
- [fpGo](https://github.com/TeaEntityLab/fpGo) - Monad, Functional Programming features for Golang.
- [fuego](https://github.com/seborama/fuego) - Functional Experiment in Go.
- [FuncFrog](https://github.com/koss-null/FuncFrog) - Functional helpers library providing Map, Filter, Reduce and other stream operations on generic slices Go1.18+ with lazy evaluation and error handling mechanisms.
- [g](https://github.com/enetx/g) - Functional programming framework for Go.
- [go-functional](https://github.com/BooleanCat/go-functional) - Functional programming in Go using generics
- [go-underscore](https://github.com/tobyhede/go-underscore) - Useful collection of helpfully functional Go collection utilities.
- [gofp](https://github.com/rbrahul/gofp) - A lodash like powerful utility library for Golang.
- [mo](https://github.com/samber/mo) - Monads and popular FP abstractions, based on Go 1.18+ Generics (Option, Result, Either...).
- [underscore](https://github.com/rjNemo/underscore) - Functional programming helpers for Go 1.18 and beyond.
- [valor](https://github.com/phelmkamp/valor) - Generic option and result types that optionally contain a value.

**[⬆ 回到顶部](#contents)**

<a id="game-development"></a>
## 游戏开发

_优秀的游戏开发库。_

- [Ark](https://github.com/mlange-42/ark) - Archetype-based Entity Component System (ECS) for Go.
- [due](https://github.com/dobyte/due) - Distributed game server framework with a modular component design, providing tcp, kcp, ws and quic gateways.
- [Ebitengine](https://github.com/hajimehoshi/ebiten) - dead simple 2D game engine in Go.
- [ecs](https://github.com/andygeiss/ecs) - Build your own Game-Engine based on the Entity Component System concept in Golang.
- [engo](https://github.com/EngoEngine/engo) - Engo is an open-source 2D game engine written in Go. It follows the Entity-Component-System paradigm.
- [fantasyname](https://github.com/s0rg/fantasyname) - Fantasy names generator.
- [g3n](https://github.com/g3n/engine) - Go 3D Game Engine.
- [go-astar](https://github.com/beefsack/go-astar) - Go implementation of the A\* path finding algorithm.
- [go-sdl2](https://github.com/veandco/go-sdl2) - Go bindings for the [Simple DirectMedia Layer](https://www.libsdl.org/).
- [go3d](https://github.com/ungerik/go3d) - Performance oriented 2D/3D math package for Go.
- [gogpu](https://github.com/gogpu/gogpu) - GPU application framework with windowing, input, and rendering built on WebGPU — reduces 480+ lines of GPU code to ~20, zero CGO (GoGPU ecosystem: [gg](https://github.com/gogpu/gg), [ui](https://github.com/gogpu/ui), [wgpu](https://github.com/gogpu/wgpu), [naga](https://github.com/gogpu/naga)).
- [gogpu/wgpu](https://github.com/gogpu/wgpu) - Pure Go WebGPU implementation with Vulkan, DX12, and Metal backends, zero CGO (part of [GoGPU](https://github.com/gogpu) ecosystem).
- [GOKe](https://github.com/kjkrol/goke) - Data-Oriented (DOD), archetype-based ECS engine utilizing an L1 cache-aligned chunked SoA layout for predictable, stepless memory growth and zero-allocation execution paths.
- [gonet](https://github.com/xtaci/gonet) - Game server skeleton implemented with golang.
- [goworld](https://github.com/xiaonanln/goworld) - Scalable game server engine, featuring space-entity framework and hot-swapping.
- [grid](https://github.com/s0rg/grid) - Generic 2D grid with ray-casting, shadow-casting and path finding.
- [Leaf](https://github.com/name5566/leaf) - Lightweight game server framework.
- [nano](https://github.com/lonng/nano) - Lightweight, facility, high performance golang based game server framework.
- [Oak](https://github.com/oakmound/oak) - Pure Go game engine.
- [Pi](https://github.com/elgopher/pi) - Game engine for creating retro games for modern computers. Inspired by Pico-8 and powered by Ebitengine.
- [Pitaya](https://github.com/topfreegames/pitaya) - Scalable game server framework with clustering support and client libraries for iOS, Android, Unity and others through the C SDK.
- [Pixel](https://github.com/gopxl/pixel) - Hand-crafted 2D game library in Go.
- [prototype](https://github.com/gonutz/prototype) - Cross-platform (Windows/Linux/Mac) library for creating desktop games using a minimal API.
- [raylib-go](https://github.com/gen2brain/raylib-go) - Go bindings for [raylib](https://www.raylib.com/), a simple and easy-to-use library to learn videogames programming.
- [sceneCamera](https://github.com/donomii/sceneCamera) - Camera movement and view/projection matrices for museum, FPS, RTS, and stereo rendering modes.
- [termloop](https://github.com/JoelOtter/termloop) - Terminal-based game engine for Go, built on top of Termbox.
- [tile](https://github.com/kelindar/tile) - Data-oriented and cache-friendly 2D Grid library (TileMap), includes pathfinding, observers and import/export.

**[⬆ 回到顶部](#contents)**

<a id="generators"></a>
## 代码生成器

_用于生成 Go 代码的工具。_

- [apispec](https://github.com/ehabterra/apispec) - Generate OpenAPI 3.1 specs from Go code without annotations, plus a browser UI to configure, preview, and explore the call graph.
- [convergen](https://github.com/reedom/convergen) - Feature rich type-to-type copy code generator.
- [copygen](https://github.com/switchupcb/copygen) - Generate any code based on Go types, including type-to-type converters (copy code) without reflection by default.
- [generis](https://github.com/senselogic/GENERIS) - Code generation tool providing generics, free-form macros, conditional compilation and HTML templating.
- [go-apispec](https://github.com/antst/go-apispec) - Generate OpenAPI 3.1 specs from Go source code via static analysis with automatic framework detection.
- [go-enum](https://github.com/abice/go-enum) - Code generation for enums from code comments.
- [go-enum-encoding](https://github.com/nikolaydubina/go-enum-encoding) - Code generation for enum encoding from code comments.
- [go-linq](https://github.com/ahmetalpbalkan/go-linq) - .NET LINQ-like query methods for Go.
- [goderive](https://github.com/awalterschulze/goderive) - Derives functions from input types
- [goverter](https://github.com/jmattheis/goverter) - Generate converters by defining an interface.
- [GoWrap](https://github.com/hexdigest/gowrap) - Generate decorators for Go interfaces using simple templates.
- [interfaces](https://github.com/rjeczalik/interfaces) - Command line tool for generating interface definitions.
- [jennifer](https://github.com/dave/jennifer) - Generate arbitrary Go code without templates.
- [oapi-codegen](https://github.com/deepmap/oapi-codegen) - This package contains a set of utilities for generating Go boilerplate code for services based on OpenAPI 3.0 API definitions.
- [protoc-gen-httpgo](https://github.com/MUlt1mate/protoc-gen-httpgo) - Generate HTTP server and client from protobuf.
- [protoc-gen-mcp](https://github.com/easyp-tech/protoc-gen-mcp) - Generate typed MCP tools, prompts, and resources from Protocol Buffers.
- [typeregistry](https://github.com/xiaoxin01/typeregistry) - A library to create type dynamically.

**[⬆ 回到顶部](#contents)**

<a id="geographic"></a>
## 地理信息

_地理信息工具与服务_

- [borders](https://github.com/kpfaulkner/borders) - Detects image borders and converts to GeoJSON for GIS operations.
* [geo-engine-go](https://github.com/AlexG695/geo-engine-go) - Official Go SDK for GeoEngine, offering high-performance geospatial data ingestion with single-digit millisecond latency.
- [geoos](https://github.com/spatial-go/geoos) - A library provides spatial data and geometric algorithms.
- [geoserver](https://github.com/hishamkaram/geoserver) - geoserver Is a Go Package For Manipulating a GeoServer Instance via the GeoServer REST API.
- [gismanager](https://github.com/hishamkaram/gismanager) - Publish Your GIS Data(Vector Data) to PostGIS and Geoserver.
- [godal](https://github.com/airbusgeo/godal) - Go wrapper for GDAL.
- [H3](https://github.com/uber/h3-go) - Go bindings for H3, a hierarchical hexagonal geospatial indexing system.
- [H3 GeoJSON](https://github.com/mmadfox/go-geojson2h3) - Conversion utilities between H3 indexes and GeoJSON.
- [H3GeoDist](https://github.com/mmadfox/go-h3geo-dist) - Distribution of Uber H3geo cells by virtual nodes.
- [mbtileserver](https://github.com/consbio/mbtileserver) - A simple Go-based server for map tiles stored in mbtiles format.
- [osm](https://github.com/paulmach/osm) - Library for reading, writing and working with OpenStreetMap data and APIs.
- [pbf](https://github.com/maguro/pbf) - OpenStreetMap PBF golang encoder/decoder.
- [S2 geojson](https://github.com/pantrif/s2-geojson) - Convert geojson to s2 cells & demonstrating some S2 geometry features on map.
- [S2 geometry](https://github.com/golang/geo) - S2 geometry library in Go.
- [simplefeatures](https://github.com/peterstace/simplefeatures) - simplesfeatures is a 2D geometry library that provides Go types that model geometries, as well as algorithms that operate on them.
- [Tile38](https://github.com/tidwall/tile38) - Geolocation DB with spatial index and realtime geofencing.
- [Web-Mercator-Projection](https://github.com/jorelosorio/web-mercator-projection) A project to easily use and convert LonLat, Point and Tile to display info, markers, etc, in a map using the Web Mercator Projection.
- [WGS84](https://github.com/wroge/wgs84) - Library for Coordinate Conversion and Transformation (ETRS89, OSGB36, NAD83, RGF93, Web Mercator, UTM).

**[⬆ 回到顶部](#contents)**

<a id="go-compilers"></a>
## Go 编译器

_用于 Go 与其他语言互相编译的工具。_

- [bunster](https://github.com/yassinebenaid/bunster) - Compile shell scripts to Go.
- [c4go](https://github.com/Konstantin8105/c4go) - Transpile C code to Go code.
- [cxgo](https://github.com/gotranspile/cxgo) - Transpile C code to Go code.
- [esp32](https://github.com/andygeiss/esp32-transpiler) - Transpile Go into Arduino code.
- [f4go](https://github.com/Konstantin8105/f4go) - Transpile FORTRAN 77 code to Go code.
- [go2hx](https://github.com/go2hx/go2hx) - Compiler from Go to Haxe to Javascript/C++/Java/C#.
- [gopherjs](https://github.com/gopherjs/gopherjs) - Compiler from Go to JavaScript.

**[⬆ 回到顶部](#contents)**

<a id="goroutines"></a>
## Goroutine 并发

_用于管理和使用 Goroutine 的工具。_

- [anchor](https://github.com/kyuff/anchor) - Library to manage component lifecycle in microservice architectures.
- [ants](https://github.com/panjf2000/ants) - A high-performance and low-cost goroutine pool in Go.
- [artifex](https://github.com/borderstech/artifex) - Simple in-memory job queue for Golang using worker-based dispatching.
- [async](https://github.com/yaitoo/async) - An asynchronous task package with async/await style for Go.
- [async](https://github.com/reugn/async) - An alternative sync library for Go (Future, Promise, Locks).
- [async](https://github.com/studiosol/async) - A safe way to execute functions asynchronously, recovering them in case of panic.
- [async-job](https://github.com/lab210-dev/async-job) - AsyncJob is an asynchronous queue job manager with light code, clear and speed.
- [autopool](https://github.com/AshvinBambhaniya/autopool) - Zero-config, auto-scaling worker pool for Go with priority-aware scheduling.
- [breaker](https://github.com/kamilsk/breaker) - Flexible mechanism to make execution flow interruptible.
- [channelify](https://github.com/ddelizia/channelify) - Transform your function to return channels for easy and powerful parallel processing.
- [conc](https://github.com/sourcegraph/conc) - `conc` is your toolbelt for structured concurrency in go, making common tasks easier and safer.
- [concurrency-limiter](https://github.com/vivek-ng/concurrency-limiter) - Concurrency limiter with support for timeouts, dynamic priority and context cancellation of goroutines.
- [conexec](https://github.com/ITcathyh/conexec) - A concurrent toolkit to help execute funcs concurrently in an efficient and safe way. It supports specifying the overall timeout to avoid blocking and uses goroutine pool to improve efficiency.
- [cyclicbarrier](https://github.com/marusama/cyclicbarrier) - CyclicBarrier for golang.
- [execpool](https://github.com/hexdigest/execpool) - A pool built around exec.Cmd that spins up a given number of processes in advance and attaches stdin and stdout to them when needed. Very similar to FastCGI or Apache Prefork MPM but works for any command.
- [flowmatic](https://github.com/carlmjohnson/flowmatic) - Structured concurrency made easy.
- [go-accumulator](https://github.com/nar10z/go-accumulator) - Solution for accumulation of events and their subsequent processing.
- [go-actor](https://github.com/vladopajic/go-actor) - A tiny library for writing concurrent programs using actor model.
- [go-floc](https://github.com/workanator/go-floc) - Orchestrate goroutines with ease.
- [go-flow](https://github.com/kamildrazkiewicz/go-flow) - Control goroutines execution order.
- [go-future](https://github.com/jizhuozhi/go-future) - A Future/Promise library with generic combinators and a DAG execution engine.
- [go-tools/multithreading](https://github.com/nikhilsaraf/go-tools) - Manage a pool of goroutines using this lightweight library with a simple API.
- [go-trylock](https://github.com/subchen/go-trylock) - TryLock support on read-write lock for Golang.
- [go-waitgroup](https://github.com/pieterclaerhout/go-waitgroup) - Like `sync.WaitGroup` with error handling and concurrency control.
- [go-workerpool](https://github.com/zenthangplus/go-workerpool) - Inspired from Java Thread Pool, Go WorkerPool aims to control heavy Go Routines.
- [goccm](https://github.com/zenthangplus/goccm) - Go Concurrency Manager package limits the number of goroutines that allowed to run concurrently.
- [gohive](https://github.com/loveleshsharma/gohive) - A highly performant and easy to use Goroutine pool for Go.
- [gollback](https://github.com/vardius/gollback) - asynchronous simple function utilities, for managing execution of closures and callbacks.
- [goscade](https://github.com/ognick/goscade) - Minimalistic lifecycle orchestrator for Go components with dependency graphs, startup sequencing, readiness coordination, and graceful shutdown.
- [gowl](https://github.com/hamed-yousefi/gowl) - Gowl is a process management and process monitoring tool at once. An infinite worker pool gives you the ability to control the pool and processes and monitor their status.
- [goworker](https://github.com/benmanns/goworker) - goworker is a Go-based background worker.
- [gowp](https://github.com/xxjwxc/gowp) - gowp is concurrency limiting goroutine pool.
- [gpool](https://github.com/Sherifabdlnaby/gpool) - manages a resizeable pool of context-aware goroutines to bound concurrency.
- [grpool](https://github.com/ivpusic/grpool) - Lightweight Goroutine pool.
- [hands](https://github.com/duanckham/hands) - A process controller used to control the execution and return strategies of multiple goroutines.
- [Hunch](https://github.com/AaronJan/Hunch) - Hunch provides functions like: `All`, `First`, `Retry`, `Waterfall` etc., that makes asynchronous flow control more intuitive.
- [kyoo](https://github.com/dirkaholic/kyoo) - Provides an unlimited job queue and concurrent worker pools.
- [neilotoole/errgroup](https://github.com/neilotoole/errgroup) - Drop-in alternative to `sync/errgroup`, limited to a pool of N worker goroutines.
- [nursery](https://github.com/arunsworld/nursery) - Structured concurrency in Go.
- [oversight](https://pkg.go.dev/cirello.io/oversight) - Oversight is a complete implementation of the Erlang supervision trees.
- [parallel-fn](https://github.com/rafaeljesus/parallel-fn) - Run functions in parallel.
- [pond](https://github.com/alitto/pond) - Minimalistic and High-performance goroutine worker pool written in Go.
- [pool](https://github.com/go-playground/pool) - Limited consumer goroutine or unlimited goroutine pool for easier goroutine handling and cancellation.
- [powerlock](https://github.com/donomii/powerlock) - Named FIFO mutexes with context cancellation, bounded wait queues, watchdog diagnostics, pprof profiles, and Prometheus metrics.
- [rill](https://github.com/destel/rill) - Go toolkit for clean, composable, channel-based concurrency.
- [routine](https://github.com/timandy/routine) - `routine` is a `ThreadLocal` for go library. It encapsulates and provides some easy-to-use, non-competitive, high-performance `goroutine` context access interfaces, which can help you access coroutine context information more gracefully.
- [routine](https://github.com/x-mod/routine) - go routine control with context, support: Main, Go, Pool and some useful Executors.
- [semaphore](https://github.com/kamilsk/semaphore) - Semaphore pattern implementation with timeout of lock/unlock operations based on channel and context.
- [semaphore](https://github.com/marusama/semaphore) - Fast resizable semaphore implementation based on CAS (faster than channel-based semaphore implementations).
- [stl](https://github.com/ssgreg/stl) - Software transactional locks based on Software Transactional Memory (STM) concurrency control mechanism.
- [threadpool](https://github.com/shettyh/threadpool) - Golang threadpool implementation.
- [tunny](https://github.com/Jeffail/tunny) - Goroutine pool for golang.
- [worker-pool](https://github.com/vardius/worker-pool) - goworker is a Go simple async worker pool.
- [workerpool](https://github.com/gammazero/workerpool) - Goroutine pool that limits the concurrency of task execution, not the number of tasks queued.

**[⬆ 回到顶部](#contents)**

<a id="gui"></a>
## GUI

_用于构建 GUI 应用的库。_

_工具集_

- [app](https://github.com/murlokswarm/app) - Package to create apps with GO, HTML and CSS. Supports: MacOS, Windows in progress.
- [cimgui-go](https://github.com/AllenDang/cimgui-go) - Auto generated Go wrapper for [Dear ImGui](https://github.com/ocornut/imgui) via [cimgui](https://github.com/cimgui/cimgui).
- [Cogent Core](https://github.com/cogentcore/core) - A framework for building 2D and 3D apps that run on macOS, Windows, Linux, iOS, Android, and the web.
- [DarwinKit](https://github.com/progrium/darwinkit) - Build native macOS applications using Go.
- [energy](https://github.com/energye/energy) - Cross-platform based on LCL(Native System UI Control Library) and CEF(Chromium Embedded Framework) (Windows/ macOS / Linux)
- [fyne](https://github.com/fyne-io/fyne) - Cross platform native GUIs designed for Go based on Material Design. Supports: Linux, macOS, Windows, BSD, iOS and Android.
- [gio](https://gioui.org) - Gio is a library for writing cross-platform immediate mode GUI-s in Go. Gio supports all the major platforms: Linux, macOS, Windows, Android, iOS, FreeBSD, OpenBSD and WebAssembly.
- [go-gtk](https://mattn.github.io/go-gtk/) - Go bindings for GTK.
- [go-sciter](https://github.com/sciter-sdk/go-sciter) - Go bindings for Sciter: the Embeddable HTML/CSS/script engine for modern desktop UI development. Cross platform.
- [Goey](https://bitbucket.org/rj/goey/src/master/) - Cross platform UI toolkit aggregator for Windows / Linux / Mac. GTK, Cocoa, Windows API
- [gogpu/ui](https://github.com/gogpu/ui) - GPU-accelerated GUI toolkit with 22 widgets, 3 design systems (Material, Fluent, Cupertino), reactive signals, and zero CGO (part of [GoGPU](https://github.com/gogpu) ecosystem).
- [goradd/html5tag](https://github.com/goradd/html5tag) - Library for outputting HTML5 tags.
- [gotk3](https://github.com/gotk3/gotk3) - Go bindings for GTK3.
- [gowd](https://github.com/dtylman/gowd) - Rapid and simple desktop UI development with GO, HTML, CSS and NW.js. Cross platform.
- [proton](https://github.com/CzaxStudio/proton) - Pure Go immediate-mode GUI framework built on Gio with zero Cgo dependencies.
- [qt](https://github.com/therecipe/qt) - Qt binding for Go (support for Windows / macOS / Linux / Android / iOS / Sailfish OS / Raspberry Pi).
- [Spot](https://github.com/roblillack/spot) - Reactive, cross-platform desktop GUI toolkit.
- [ui](https://github.com/andlabs/ui) - Platform-native GUI library for Go. Cross platform.
- [unison](https://github.com/richardwilkes/unison) - A unified graphical user experience toolkit for Go desktop applications. macOS, Windows, and Linux are supported.
- [Wails](https://wails.io) - Mac, Windows, Linux desktop apps with HTML UI using built-in OS HTML renderer.
- [walk](https://github.com/lxn/walk) - Windows application library kit for Go.
- [webview](https://github.com/zserge/webview) - Cross-platform webview window with simple two-way JavaScript bindings (Windows / macOS / Linux).

_交互_

- [AppIndicator Go](https://github.com/gopherlibs/appindicator) - Go bindings for libappindicator3 C library.
- [gogpu/systray](https://github.com/gogpu/systray) - Pure Go system tray library for Windows, macOS, and Linux with zero CGO (part of [GoGPU](https://github.com/gogpu) ecosystem).
- [gosx-notifier](https://github.com/deckarep/gosx-notifier) - OSX Desktop Notifications library for Go.
- [mac-activity-tracker](https://github.com/prashantgupta24/activity-tracker) - OSX library to notify about any (pluggable) activity on your machine.
- [mac-sleep-notifier](https://github.com/prashantgupta24/mac-sleep-notifier) - OSX Sleep/Wake notifications in golang.
- [robotgo](https://github.com/go-vgo/robotgo) - Go Native cross-platform GUI system automation. Control the mouse, keyboard and other.
- [systray](https://github.com/getlantern/systray) - Cross platform Go library to place an icon and menu in the notification area.
- [trayhost](https://github.com/shurcooL/trayhost) - Cross-platform Go library to place an icon in the host operating system's taskbar.
- [zenity](https://github.com/ncruces/zenity) - Cross-platform Go library and CLI to create simple dialogs that interact graphically with the user.

**[⬆ 回到顶部](#contents)**

<a id="hardware"></a>
## 硬件

_用于与硬件交互的库、工具与教程。_

- [arduino-cli](https://github.com/arduino/arduino-cli) - Official Arduino CLI and library. Can run standalone, or be incorporated into larger Go projects.
- [emgo](https://github.com/ziutek/emgo) - Go-like language for programming embedded systems (e.g. STM32 MCU).
- [ghw](https://github.com/jaypipes/ghw) - Golang hardware discovery/inspection library.
- [go-osc](https://github.com/hypebeast/go-osc) - Open Sound Control (OSC) bindings for Go.
- [go-rpio](https://github.com/stianeikeland/go-rpio) - GPIO for Go, doesn't require cgo.
- [goroslib](https://github.com/aler9/goroslib) - Robot Operating System (ROS) library for Go.
- [joystick](https://github.com/0xcafed00d/joystick) - a polled API to read the state of an attached joystick.
- [moody](https://github.com/dinakars777/moody) - Hardware event personality daemon for macOS. Monitors USB, charger, lid, and other hardware events and responds with customizable personalities.
- [sysinfo](https://github.com/zcalusic/sysinfo) - A pure Go library providing Linux OS / kernel / hardware system information.

**[⬆ 回到顶部](#contents)**

<a id="images"></a>
## 图像处理

_用于图像处理的库。_

- [bild](https://github.com/anthonynsimon/bild) - Collection of image processing algorithms in pure Go.
- [bimg](https://github.com/h2non/bimg) - Small package for fast and efficient image processing using libvips.
- [cameron](https://github.com/aofei/cameron) - An avatar generator for Go.
- [canvas](https://github.com/tdewolff/canvas) - Vector graphics to PDF, SVG or rasterized image.
- [color-extractor](https://github.com/marekm4/color-extractor) - Dominant color extractor with no external dependencies.
- [darkroom](https://github.com/gojek/darkroom) - An image proxy with changeable storage backends and image processing engines with focus on speed and resiliency.
- [eagle-image-api](https://github.com/nicobistolfi/eagle-image-api) - Image optimization and transformation API using libvips, deployable to AWS Lambda and CloudFront.
- [geopattern](https://github.com/pravj/geopattern) - Create beautiful generative image patterns from a string.
- [gg](https://github.com/fogleman/gg) - 2D rendering in pure Go.
- [gift](https://github.com/disintegration/gift) - Package of image processing filters.
- [gltf](https://github.com/qmuntal/gltf) - Efficient and robust glTF 2.0 reader, writer and validator.
- [go-cairo](https://github.com/ungerik/go-cairo) - Go binding for the cairo graphics library.
- [go-gd](https://github.com/bolknote/go-gd) - Go binding for GD library.
- [go-nude](https://github.com/koyachi/go-nude) - Nudity detection with Go.
- [go-qrcode](https://github.com/yeqown/go-qrcode) - Generate QR codes with personalized styles, allowing adjustments to color, block size, shape, and icons.
- [go-webcolors](https://github.com/jyotiska/go-webcolors) - Port of webcolors library from Python to Go.
- [go-webp](https://github.com/kolesa-team/go-webp) - Library for encode and decode webp pictures, using libwebp.
- [gocv](https://github.com/hybridgroup/gocv) - Go package for computer vision using OpenCV 3.3+.
- [gogpu/gg](https://github.com/gogpu/gg) - GPU-accelerated 2D rendering with Canvas-like API, zero CGO (part of [GoGPU](https://github.com/gogpu) pure Go graphics ecosystem).
- [goimagehash](https://github.com/corona10/goimagehash) - Go Perceptual image hashing package.
- [goimghdr](https://github.com/corona10/goimghdr) - The imghdr module determines the type of image contained in a file for Go.
- [govatar](https://github.com/o1egl/govatar) - Library and CMD tool for generating funny avatars.
- [govips](https://github.com/davidbyttow/govips) - A lightning fast image processing and resizing library for Go.
- [gowitness](https://github.com/sensepost/gowitness) - Screenshoting webpages using go and headless chrome on command line.
- [gridder](https://github.com/shomali11/gridder) - A Grid based 2D Graphics library.
- [image2ascii](https://github.com/qeesung/image2ascii) - Convert image to ASCII.
- [imagick](https://github.com/gographics/imagick) - Go binding to ImageMagick's MagickWand C API.
- [imaginary](https://github.com/h2non/imaginary) - Fast and simple HTTP microservice for image resizing.
- [imaging](https://github.com/disintegration/imaging) - Simple Go image processing package.
- [imagor](https://github.com/cshum/imagor) - Fast, secure image processing server and Go library, using libvips.
- [img](https://github.com/hawx/img) - Selection of image manipulation tools.
- [ln](https://github.com/fogleman/ln) - 3D line art rendering in Go.
- [mergi](https://github.com/noelyahan/mergi) - Tool & Go library for image manipulation (Merge, Crop, Resize, Watermark, Animate).
- [mort](https://github.com/aldor007/mort) - Storage and image processing server written in Go.
- [mpo](https://github.com/donatj/mpo) - Decoder and conversion tool for MPO 3D Photos.
- [nativewebp](https://github.com/HugoSmits86/nativewebp) - Go native WebP encoder with zero external dependencies.
- [picfit](https://github.com/thoas/picfit) - An image resizing server written in Go.
- [pt](https://github.com/fogleman/pt) - Path tracing engine written in Go.
- [scout](https://github.com/jonoton/scout) - Scout is a standalone open source software solution for DIY video security.
- [smartcrop](https://github.com/muesli/smartcrop) - Finds good crops for arbitrary images and crop sizes.
- [steganography](https://github.com/auyer/steganography) - Pure Go Library for LSB steganography.
- [stegify](https://github.com/DimitarPetrov/stegify) - Go tool for LSB steganography, capable of hiding any file within an image.
- [svgo](https://github.com/ajstarks/svgo) - Go Language Library for SVG generation.
- [transformimgs](https://github.com/Pixboost/transformimgs) - Transformimgs resizes and optimises images for Web using next-generation formats.
- [webp-server](https://github.com/mehdipourfar/webp-server) - Simple and minimal image server capable of storing, resizing, converting and caching images.

**[⬆ 回到顶部](#contents)**

<a id="iot-internet-of-things"></a>
## 物联网（IoT）

_用于物联网设备编程的库。_

- [connectordb](https://github.com/connectordb/connectordb) - Open-Source Platform for Quantified Self & IoT.
- [devices](https://github.com/goiot/devices) - Suite of libraries for IoT devices, experimental for x/exp/io.
- [ekuiper](https://github.com/lf-edge/ekuiper) - Lightweight data stream processing engine for IoT edge.
- [eywa](https://github.com/xcodersun/eywa) - Project Eywa is essentially a connection manager that keeps track of connected devices.
- [flogo](https://github.com/tibcosoftware/flogo) - Project Flogo is an Open Source Framework for IoT Edge Apps & Integration.
- [gatt](https://github.com/paypal/gatt) - Gatt is a Go package for building Bluetooth Low Energy peripherals.
- [gobot](https://github.com/hybridgroup/gobot/) - Gobot is a framework for robotics, physical computing, and the Internet of Things.
- [huego](https://github.com/amimof/huego) - An extensive Philips Hue client library for Go.
- [iot](https://github.com/vaelen/iot/) - IoT is a simple framework for implementing a Google IoT Core device.
- [periph](https://periph.io/) - Peripherals I/O to interface with low-level board facilities.
- [rulego](https://github.com/rulego/rulego) - RuleGo is a lightweight, high-performance, embedded, orchestrable component-based rule engine for IoT edge.
- [sensorbee](https://github.com/sensorbee/sensorbee) - Lightweight stream processing engine for IoT.
- [shifu](https://github.com/Edgenesis/shifu) - Kubernetes native IoT development framework.
- [smart-home](https://github.com/e154/smart-home) - Software package for IoT automation.

**[⬆ 回到顶部](#contents)**

<a id="job-scheduler"></a>
## 任务调度

_用于任务调度的库。_

- [cdule](https://github.com/deepaksinghvi/cdule) - Job scheduler library with database support
- [cheek](https://github.com/bart6114/cheek) - A simple crontab like scheduler that aims to offer a KISS approach to job scheduling.
- [clockwerk](https://github.com/onatm/clockwerk) - Go package to schedule periodic jobs using a simple, fluent syntax.
- [cronticker](https://github.com/krayzpipes/cronticker) - A ticker implementation to support cron schedules.
- [go-cron](https://github.com/rk/go-cron) - Simple Cron library for go that can execute closures or functions at varying intervals, from once a second to once a year on a specific date and time. Primarily for web applications and long running daemons.
- [go-cron](https://github.com/netresearch/go-cron) - Cron job scheduler with runtime schedule updates, per-entry context, resilience middleware (retry, circuit breaker, rate limiting), and observability hooks; successor to robfig/cron.
- [go-job](https://github.com/cybergarage/go-job) - A flexible and extensible job scheduling and execution library for Go.
- [go-quartz](https://github.com/reugn/go-quartz) - Simple, zero-dependency scheduling library for Go.
- [go-scheduler](https://github.com/pardnchiu/go-scheduler) - Job scheduler supporting standard cron expressions, custom descriptors, intervals, and task dependencies.
- [gocron](https://github.com/go-co-op/gocron) - Easy and fluent Go job scheduling. This is an actively maintained fork of [jasonlvhit/gocron](https://github.com/jasonlvhit/gocron).
- [goflow](https://github.com/fieldryand/goflow) - A simple but powerful DAG scheduler and dashboard.
- [gron](https://github.com/roylee0704/gron) - Define time-based tasks using a simple Go API and Gron’s scheduler will run them accordingly.
- [gronx](https://github.com/adhocore/gronx) - Cron expression parser, task runner and daemon consuming crontab like task list.
- [JobRunner](https://github.com/bamzi/jobrunner) - Smart and featureful cron job scheduler with job queuing and live monitoring built in.
- [leprechaun](https://github.com/kilgaloon/leprechaun) - Job scheduler that supports webhooks, crons and classic scheduling.
- [ofelia](https://github.com/netresearch/ofelia) - Docker job scheduler (crontab for Docker); fork of mcuadros/ofelia that adds a web UI, job dependencies, retries, and job persistence.
- [pending](https://github.com/kahoon/pending) - ID-based debounced task scheduler for deferred tasks with cancellation, graceful shutdown, and optional concurrency limits.
- [sched](https://github.com/romshark/sched) - A job scheduler with the ability to fast-forward time.
- [scheduler](https://github.com/carlescere/scheduler) - Cronjobs scheduling made easy.
- [scheduler](https://github.com/yuseferi/scheduler) - Go-native distributed job scheduler with delayed tasks, batched Redis coordination, retries, lease-based recovery, and versioned queue partitioning.
- [tasks](https://github.com/madflojo/tasks) - An easy to use in-process scheduler for recurring tasks in Go.
- [tickstem/cron](https://github.com/tickstem/cron) - Go client for scheduling HTTP cron jobs, with execution history, failure alerts, and tsk-local for testing handlers without live credentials.
- [tickstem/heartbeat](https://github.com/tickstem/heartbeat) - Go client for dead-man's switch heartbeat monitoring: ping a URL after each job run and get alerted by email if pings stop arriving.

**[⬆ 回到顶部](#contents)**

<a id="json"></a>
## JSON

_用于处理 JSON 的库。_

- [ajson](https://github.com/spyzhov/ajson) - Abstract JSON for golang with JSONPath support.
- [ask](https://github.com/simonnilsson/ask) - Easy access to nested values in maps and slices. Works in combination with encoding/json and other packages that "Unmarshal" arbitrary data into Go data-types.
- [dynjson](https://github.com/cocoonspace/dynjson) - Client-customizable JSON formats for dynamic APIs.
- [ej](https://github.com/lucassscaravelli/ej) - Write and read JSON from different sources succinctly.
- [epoch](https://github.com/vtopc/epoch) - Contains primitives for marshaling/unmarshalling Unix timestamp/epoch to/from build-in time.Time type in JSON.
- [fastjson](https://github.com/valyala/fastjson) - Fast JSON parser and validator for Go. No custom structs, no code generation, no reflection.
- [gabs](https://github.com/Jeffail/gabs) - For parsing, creating and editing unknown or dynamic JSON in Go.
- [gjo](https://github.com/skanehira/gjo) - Small utility to create JSON objects.
- [GJSON](https://github.com/tidwall/gjson) - Get a JSON value with one line of code.
- [go-jsonerror](https://github.com/ddymko/go-jsonerror) - Go-JsonError is meant to allow us to easily create json response errors that follow the JsonApi spec.
- [go-respond](https://github.com/nicklaw5/go-respond) - Go package for handling common HTTP JSON responses.
- [gojmapr](https://github.com/limiu82214/gojmapr) - Get simple struct from complex json by json path.
- [gojq](https://github.com/elgs/gojq) - JSON query in Golang.
- [gojson](https://github.com/ChimeraCoder/gojson) - Automatically generate Go (golang) struct definitions from example JSON.
- [htmljson](https://github.com/nikolaydubina/htmljson) - Rich rendering of JSON as HTML in Go.
- [JayDiff](https://github.com/yazgazan/jaydiff) - JSON diff utility written in Go.
- [jettison](https://github.com/wI2L/jettison) - Fast and flexible JSON encoder for Go.
- [jscan](https://github.com/romshark/jscan) - High performance zero-allocation JSON iterator.
- [JSON-to-Go](https://mholt.github.io/json-to-go/) - Convert JSON to Go struct.
- [JSON-to-Proto](https://json-to-proto.github.io/) - Convert JSON to Protobuf online.
- [json2go](https://github.com/m-zajac/json2go) - Advanced JSON to Go struct conversion. Provides package that can parse multiple JSON documents and create struct to fit them all.
- [jsonapi-errors](https://github.com/AmuzaTkts/jsonapi-errors) - Go bindings based on the JSON API errors reference.
- [jsoncolor](https://github.com/neilotoole/jsoncolor) - Drop-in replacement for `encoding/json` that outputs colorized JSON.
- [jsondiff](https://github.com/wI2L/jsondiff) - JSON diff library for Go based on RFC6902 (JSON Patch).
- [jsonf](https://github.com/miolini/jsonf) - Console tool for highlighted formatting and struct query fetching JSON.
- [jsongo](https://github.com/ricardolonga/jsongo) - Fluent API to make it easier to create Json objects.
- [jsonhal](https://github.com/RichardKnop/jsonhal) - Simple Go package to make custom structs marshal into HAL compatible JSON responses.
- [jsonhandlers](https://github.com/abusomani/jsonhandlers) - JSON library to expose simple handlers that lets you easily read and write json from various sources.
- [jsonic](https://github.com/sinhashubham95/jsonic) - Utilities to handle and query JSON without defining structs in a type safe manner.
- [jsonvalue](https://github.com/Andrew-M-C/go.jsonvalue) - A fast and convenient library for unstructured JSON data, replacing `encoding/json`.
- [jzon](https://github.com/zerosnake0/jzon) - JSON library with standard compatible API/behavior.
- [kazaam](https://github.com/Qntfy/kazaam) - API for arbitrary transformation of JSON documents.
- [mapslice-json](https://github.com/mickep76/mapslice-json) - Go MapSlice for ordered marshal/ unmarshal of maps in JSON.
- [marshmallow](https://github.com/PerimeterX/marshmallow) - Performant JSON unmarshalling for flexible use cases.
- [mp](https://github.com/sanbornm/mp) - Simple cli email parser. It currently takes stdin and outputs JSON.
- [OjG](https://github.com/ohler55/ojg) - Optimized JSON for Go is a high performance parser with a variety of additional JSON tools including JSONPath.
- [omg.jsonparser](https://github.com/dedalqq/omg.jsonparser) - Simple JSON parser with validation by condition via golang struct fields tags.
- [silentjson](https://github.com/GenshIv/silentjson) - Zero-allocation JSON boundary scanner and splitter utilizing AVX2 SIMD instructions.
- [SJSON](https://github.com/tidwall/sjson) - Set a JSON value with one line of code.  
- [ujson](https://github.com/olvrng/ujson) - Fast and minimal JSON parser and transformer that works on unstructured JSON.
- [vjson](https://github.com/miladibra10/vjson) - Go package for validating JSON objects with declaring a JSON schema with fluent API.

**[⬆ 回到顶部](#contents)**

<a id="logging"></a>
## 日志

_用于生成与处理日志文件的库。_

- [caarlos0/log](https://github.com/caarlos0/log) - Colorful CLI logger.
- [distillog](https://github.com/amoghe/distillog) - distilled levelled logging (think of it as stdlib + log levels).
- [glg](https://github.com/kpango/glg) - glg is simple and fast leveled logging library for Go.
- [glo](https://github.com/lajosbencz/glo) - PHP Monolog inspired logging facility with identical severity levels.
- [glog](https://github.com/golang/glog) - Leveled execution logs for Go.
- [go-cronowriter](https://github.com/utahta/go-cronowriter) - Simple writer that rotate log files automatically based on current date and time, like cronolog.
- [go-log](https://github.com/pieterclaerhout/go-log) - A logging library with stack traces, object dumping and optional timestamps.
- [go-log](https://github.com/subchen/go-log) - Simple and configurable Logging in Go, with level, formatters and writers.
- [go-log](https://github.com/siddontang/go-log) - Log lib supports level and multi handlers.
- [go-log](https://github.com/ian-kent/go-log) - Log4j implementation in Go.
- [go-log4g](https://github.com/go-log4g/core) - Log4g provides Log4j-style configuration and pattern layouts for Go's standard log/slog logging facade.
- [go-logger](https://github.com/apsdehal/go-logger) - Simple logger of Go Programs, with level handlers.
- [GoLogX](https://github.com/AyoubTadlaoui/GoLogX) - Append-only, hash-chained, optionally Ed25519-signed slog handler with offline verification of tampering.
- [gone/log](https://github.com/One-com/gone/tree/master/log) - Fast, extendable, full-featured, std-lib source compatible log library.
- [gslog](https://github.com/maguro/gslog) - Google Cloud Logging handler for log/slog, with OpenTelemetry trace and baggage, and Kubernetes podinfo labels.
- [httpretty](https://github.com/henvic/httpretty) - Pretty-prints your regular HTTP requests on your terminal for debugging (similar to http.DumpRequest).
- [journald](https://github.com/ssgreg/journald) - Go implementation of systemd Journal's native API for logging.
- [kemba](https://github.com/clok/kemba) - A tiny debug logging tool inspired by [debug](https://github.com/visionmedia/debug), great for CLI tools and applications.
- [lazyjournal](https://github.com/Lifailon/lazyjournal) - A TUI for reading and filtering logs from journalctl, file system, Docker and Podman containers, as well Kubernetes pods.
- [log](https://github.com/aerogo/log) - An O(1) logging system that allows you to connect one log to multiple writers (e.g. stdout, a file and a TCP connection).
- [log](https://github.com/apex/log) - Structured logging package for Go.
- [log](https://github.com/go-playground/log) - Simple, configurable and scalable Structured Logging for Go.
- [log](https://github.com/teris-io/log) - Structured log interface for Go cleanly separates logging facade from its implementation.
- [log](https://github.com/heartwilltell/log) - Simple leveled logging wrapper around standard log package.
- [log](https://github.com/no-src/log) - A simple logging framework out of the box.
- [log15](https://github.com/inconshreveable/log15) - Simple, powerful logging for Go.
- [logdump](https://github.com/ewwwwwqm/logdump) - Package for multi-level logging.
- [logex](https://github.com/chzyer/logex) - Golang log lib, supports tracking and level, wrap by standard log lib.
- [logger](https://github.com/azer/logger) - Minimalistic logging library for Go.
- [logo](https://github.com/mbndr/logo) - Golang logger to different configurable writers.
- [logrus](https://github.com/Sirupsen/logrus) - Structured logger for Go.
- [logrusiowriter](https://github.com/cabify/logrusiowriter) - `io.Writer` implementation using [logrus](https://github.com/sirupsen/logrus) logger.
- [logrusly](https://github.com/sebest/logrusly) - [logrus](https://github.com/sirupsen/logrus) plug-in to send errors to a [Loggly](https://www.loggly.com/).
- [logutils](https://github.com/hashicorp/logutils) - Utilities for slightly better logging in Go (Golang) extending the standard logger.
- [logxi](https://github.com/mgutz/logxi) - 12-factor app logger that is fast and makes you happy.
- [lumberjack](https://github.com/natefinch/lumberjack) - Simple rolling logger, implements io.WriteCloser.
- [mlog](https://github.com/jbrodriguez/mlog) - Simple logging module for go, with 5 levels, an optional rotating logfile feature and stdout/stderr output.
- [noodlog](https://github.com/gyozatech/noodlog) - Parametrized JSON logging library which lets you obfuscate sensitive data and marshal any kind of content. No more printed pointers instead of values, nor escape chars for the JSON strings.
- [onelog](https://github.com/francoispqt/onelog) - Onelog is a dead simple but very efficient JSON logger. It is the fastest JSON logger out there in all scenarios. Also, it is one of the logger with the lowest allocation.
- [ozzo-log](https://github.com/go-ozzo/ozzo-log) - High performance logging supporting log severity, categorization, and filtering. Can send filtered log messages to various targets (e.g. console, network, mail).
- [phuslu/log](https://github.com/phuslu/log) - High performance structured logging.
- [pp](https://github.com/k0kubun/pp) - Colored pretty printer for Go language.
- [rollingwriter](https://github.com/arthurkiller/rollingWriter) - RollingWriter is an auto-rotate `io.Writer` implementation with multi policies to provide log file rotation.
- [seelog](https://github.com/cihub/seelog) - Logging functionality with flexible dispatching, filtering, and formatting.
- [sentry-go](https://github.com/getsentry/sentry-go) - Sentry SDK for Go. Helps monitor and track errors with real-time alerts and performance monitoring.
- [slf4g](https://github.com/echocat/slf4g) - Simple Logging Facade for Golang: Simple structured logging; but powerful, extendable and customizable, with huge amount of learnings from decades of past logging frameworks.
- [slog](https://github.com/gookit/slog) - Lightweight, configurable, extensible logger for Go.
- [slog-configurator](https://github.com/psyb0t/slog-configurator) - Configures the standard library log/slog logger from environment variables: level, format, source location, and stdout/stderr split.
- [slog-datadog](https://github.com/samber/slog-datadog) - A slog handler for Datadog.
- [slog-formatter](https://github.com/samber/slog-formatter) - Common formatters for slog and helpers to build your own.
- [slog-logrus](https://github.com/samber/slog-logrus) - A slog handler for Logrus.
- [slog-loki](https://github.com/samber/slog-loki) - A slog handler for Grafana Loki.
- [slog-multi](https://github.com/samber/slog-multi) - Chain of slog.Handler (pipeline, fanout...).
- [slog-sentry](https://github.com/samber/slog-sentry) - A slog handler for Sentry.
- [slog-slack](https://github.com/samber/slog-slack) - A slog handler for Slack.
- [slog-zap](https://github.com/samber/slog-zap) - A slog handler for Zap.
- [slog-zerolog](https://github.com/samber/slog-zerolog) - A slog handler for Zerolog.
- [slogor](https://gitlab.com/greyxor/slogor) - A colorful slog handler.
- [spew](https://github.com/davecgh/go-spew) - Implements a deep pretty printer for Go data structures to aid in debugging.
- [sqldb-logger](https://github.com/simukti/sqldb-logger) - A logger for Go SQL database driver without modify existing \*sql.DB stdlib usage.
- [stdlog](https://github.com/alexcesaro/log) - Stdlog is an object-oriented library providing leveled logging. It is very useful for cron jobs.
- [structy/log](https://github.com/structy/log) - A simple to use log system, minimalist but with features for debugging and differentiation of messages.
- [tail](https://github.com/hpcloud/tail) - Go package striving to emulate the features of the BSD tail program.
- [timberjack](https://github.com/DeRuina/timberjack) - Rolling logger with size-based, time-based, and scheduled clock-based rotation, supporting compression and cleanup.
- [tint](https://github.com/lmittmann/tint) - A slog.Handler that writes tinted logs.
- [xlog](https://github.com/xfxdev/xlog) - Plugin architecture and flexible log system for Go, with level ctrl, multiple log target and custom log format.
- [xlog](https://github.com/rs/xlog) - Structured logger for `net/context` aware HTTP handlers with flexible dispatching.
- [xylog](https://github.com/xybor-x/xylog) - Leveled and structured logging, dynamic fields, high performance, zone management, simple configuration, and readable syntax.
- [yell](https://github.com/jfcg/yell) - Yet another minimalistic logging library.
- [zap](https://github.com/uber-go/zap) - Fast, structured, leveled logging in Go.
- [zax](https://github.com/yuseferi/zax) - Integrate Context with Zap logger, which leads to more flexibility in Go logging.
- [zerolog](https://github.com/rs/zerolog) - Zero-allocation JSON logger.
- [zkits-logger](https://github.com/edoger/zkits-logger) - A powerful zero-dependency JSON logger.
- [zl](https://github.com/nkmr-jp/zl) - High Developer Experience, zap based logger. It offers rich functionality but is easy to configure.

**[⬆ 回到顶部](#contents)**

<a id="machine-learning"></a>
## 机器学习

_机器学习相关的库。_

- [Anneal](https://github.com/georgebuilds/anneal) - Machine learning compiler in Go, a from-scratch tinygrad port with a WebGPU backend.
- [bayesian](https://github.com/jbrukh/bayesian) - Naive Bayesian Classification for Golang.
- [born](https://github.com/born-ml/born) - Deep learning framework inspired by Burn (Rust), with autograd, type-safe tensors, and zero-CGO GPU acceleration.
- [catboost-cgo](https://github.com/mirecl/catboost-cgo) - Fast, scalable, high performance Gradient Boosting on Decision Trees library. Golang using Cgo for blazing fast inference CatBoost Model.
- [CloudForest](https://github.com/ryanbressler/CloudForest) - Fast, flexible, multi-threaded ensembles of decision trees for machine learning in pure Go.
- [datatrax](https://github.com/rbmuller/datatrax) - Data engineering and classic ML toolkit with batch processing, type coercion, and 7 algorithms in pure Go with zero dependencies.
- [ddt](https://github.com/sgrodriguez/ddt) - Dynamic decision tree, create trees defining customizable rules.
- [eaopt](https://github.com/MaxHalford/eaopt) - An evolutionary optimization library.
- [evoli](https://github.com/khezen/evoli) - Genetic Algorithm and Particle Swarm Optimization library.
- [fonet](https://github.com/Fontinalis/fonet) - A Deep Neural Network library written in Go.
- [go-cluster](https://github.com/e-XpertSolutions/go-cluster) - Go implementation of the k-modes and k-prototypes clustering algorithms.
- [go-deep](https://github.com/patrikeh/go-deep) - A feature-rich neural network library in Go.
- [go-fann](https://github.com/white-pony/go-fann) - Go bindings for Fast Artificial Neural Networks(FANN) library.
- [go-galib](https://github.com/thoj/go-galib) - Genetic Algorithms library written in Go / golang.
- [go-pr](https://github.com/daviddengcn/go-pr) - Pattern recognition package in Go lang.
- [gobrain](https://github.com/goml/gobrain) - Neural Networks written in go.
- [godist](https://github.com/e-dard/godist) - Various probability distributions, and associated methods.
- [goga](https://github.com/tomcraven/goga) - Genetic algorithm library for Go.
- [GoLearn](https://github.com/sjwhitworth/golearn) - General Machine Learning library for Go.
- [GoMind](https://github.com/surenderthakran/gomind) - A simplistic Neural Network Library in Go.
- [goml](https://github.com/cdipaolo/goml) - On-line Machine Learning in Go.
- [GoMLX](https://github.com/gomlx/gomlx) - An accelerated Machine Learning framework for Go.
- [gonet](https://github.com/dathoangnd/gonet) - Neural Network for Go.
- [Goptuna](https://github.com/c-bata/goptuna) - Bayesian optimization framework for black-box functions written in Go. Everything will be optimized.
- [goRecommend](https://github.com/timkaye11/goRecommend) - Recommendation Algorithms library written in Go.
- [gorgonia](https://github.com/gorgonia/gorgonia) - graph-based computational library like Theano for Go that provides primitives for building various machine learning and neural network algorithms.
- [gorse](https://github.com/zhenghaoz/gorse) - An offline recommender system backend based on collaborative filtering written in Go.
- [goscore](https://github.com/asafschers/goscore) - Go Scoring API for PMML.
- [gosseract](https://github.com/otiai10/gosseract) - Go package for OCR (Optical Character Recognition), by using Tesseract C++ library.
- [hugot](https://github.com/knights-analytics/hugot) - Huggingface transformer pipelines for golang with onnxruntime.
- [libsvm](https://github.com/datastream/libsvm) - libsvm golang version derived work based on LIBSVM 3.14.
- [m2cgen](https://github.com/BayesWitnesses/m2cgen) - A CLI tool to transpile trained classic ML models into a native Go code with zero dependencies, written in Python with Go language support.
- [neural-go](https://github.com/schuyler/neural-go) - Multilayer perceptron network implemented in Go, with training via backpropagation.
- [ocrserver](https://github.com/otiai10/ocrserver) - A simple OCR API server, seriously easy to be deployed by Docker and Heroku.
- [onnx-go](https://github.com/owulveryck/onnx-go) - Go Interface to Open Neural Network Exchange (ONNX).
- [probab](https://github.com/ThePaw/probab) - Probability distribution functions. Bayesian inference. Written in pure Go.
- [randomforest](https://github.com/malaschitz/randomForest) - Easy to use Random Forest library for Go.
- [regommend](https://github.com/muesli/regommend) - Recommendation & collaborative filtering engine.
- [shield](https://github.com/eaigner/shield) - Bayesian text classifier with flexible tokenizers and storage backends for Go.
- [tfgo](https://github.com/galeone/tfgo) - Easy to use Tensorflow bindings: simplifies the usage of the official Tensorflow Go bindings. Define computational graphs in Go, load and execute models trained in Python.
- [Varis](https://github.com/Xamber/Varis) - Golang Neural Network.

**[⬆ 回到顶部](#contents)**

<a id="messaging"></a>
## 消息

_实现消息系统的库。_

- [ami](https://github.com/kak-tus/ami) - Go client to reliable queues based on Redis Cluster Streams.
- [amqp](https://github.com/rabbitmq/amqp091-go) - Go RabbitMQ Client Library.
- [APNs2](https://github.com/sideshow/apns2) - HTTP/2 Apple Push Notification provider for Go - Send push notifications to iOS, tvOS, Safari and OSX apps.
- [Asynq](https://github.com/hibiken/asynq) - A simple, reliable, and efficient distributed task queue for Go built on top of Redis.
- [backlite](https://github.com/mikestefanello/backlite) - Type-safe, persistent, embedded task queues and background job runner w/ SQLite.
- [Beaver](https://github.com/Clivern/Beaver) - A real time messaging server to build a scalable in-app notifications, multiplayer games, chat apps in web and mobile apps.
- [broker](https://github.com/qvcloud/broker) - Production-grade messaging abstraction with a unified API for various brokers and built-in OpenTelemetry integration.
- [Bus](https://github.com/mustafaturan/bus) - Minimalist message bus implementation for internal communication.
- [Centrifugo](https://github.com/centrifugal/centrifugo) - Real-time messaging (Websockets or SockJS) server in Go.
- [Chanify](https://github.com/chanify/chanify) - A push notification server send message to your iOS devices.
- [Commander](https://github.com/jeroenrinzema/commander) - A high-level event driven consumer/producer supporting various "dialects" such as Apache Kafka.
- [Confluent Kafka Golang Client](https://github.com/confluentinc/confluent-kafka-go) - confluent-kafka-go is Confluent's Golang client for Apache Kafka and the Confluent Platform.
- [dbus](https://github.com/godbus/dbus) - Native Go bindings for D-Bus.
- [drone-line](https://github.com/appleboy/drone-line) - Sending [Line](https://at.line.me/en) notifications using a binary, docker or Drone CI.
- [emitter](https://github.com/olebedev/emitter) - Emits events using Go way, with wildcard, predicates, cancellation possibilities and many other good wins.
- [event](https://github.com/agoalofalife/event) - Implementation of the pattern observer.
- [EventBus](https://github.com/asaskevich/EventBus) - The lightweight event bus with async compatibility.
- [gaurun-client](https://github.com/osamingo/gaurun-client) - Gaurun Client written in Go.
- [Glue](https://github.com/desertbit/glue) - Robust Go and Javascript Socket Library (Alternative to Socket.io).
- [go-eventbus](https://github.com/stanipetrosyan/go-eventbus) - Simple Event Bus package for Go.
- [Go-MediatR](https://github.com/mehdihadeli/Go-MediatR) - A library for handling mediator patterns and simplified CQRS patterns within an event-driven architecture, inspired by csharp MediatR library.
- [go-mq](https://github.com/cheshir/go-mq) - RabbitMQ client with declarative configuration.
- [go-notify](https://github.com/TheCreeper/go-notify) - Native implementation of the freedesktop notification spec.
- [go-nsq](https://github.com/nsqio/go-nsq) - the official Go package for NSQ.
- [go-res](https://github.com/jirenius/go-res) - Package for building REST/real-time services where clients are synchronized seamlessly, using NATS and Resgate.
- [go-vitotrol](https://github.com/maxatome/go-vitotrol) - Client library to Viessmann Vitotrol web service.
- [GoEventBus](https://github.com/Raezil/GoEventBus) - A blazing‑fast, in‑memory, lock‑free event bus library
- [Gollum](https://github.com/trivago/gollum) - A n:m multiplexer that gathers messages from different sources and broadcasts them to a set of destinations.
- [golongpoll](https://github.com/jcuga/golongpoll) - HTTP longpoll server library that makes web pub-sub simple.
- [gopush-cluster](https://github.com/Terry-Mao/gopush-cluster) - gopush-cluster is a go push server cluster.
- [gorush](https://github.com/appleboy/gorush) - Push notification server using [APNs2](https://github.com/sideshow/apns2) and google [GCM](https://github.com/google/go-gcm).
- [gosd](https://github.com/alexsniffin/gosd) - A library for scheduling when to dispatch a message to a channel.
- [guble](https://github.com/smancke/guble) - Messaging server using push notifications (Google Firebase Cloud Messaging, Apple Push Notification services, SMS) as well as websockets, a REST API, featuring distributed operation and message-persistence.
- [hare](https://github.com/leozz37/hare) - A user friendly library for sending messages and listening to TCP sockets.
- [hub](https://github.com/leandro-lugaresi/hub) - A Message/Event Hub for Go applications, using publish/subscribe pattern with support for alias like rabbitMQ exchanges.
- [hypermatch](https://github.com/SchwarzDigits/hypermatch) - Matches events against large sets of rules, with rules written in Go or as JSON.
- [jazz](https://github.com/socifi/jazz) - A simple RabbitMQ abstraction layer for queue administration and publishing and consuming of messages.
- [machinery](https://github.com/RichardKnop/machinery) - Asynchronous task queue/job queue based on distributed message passing.
- [mangos](https://github.com/nanomsg/mangos) - Pure go implementation of the Nanomsg ("Scalability Protocols") with transport interoperability.
- [melody](https://github.com/olahol/melody) - Minimalist framework for dealing with websocket sessions, includes broadcasting and automatic ping/pong handling.
- [Mercure](https://github.com/dunglas/mercure) - Server and library to dispatch server-sent updates using the Mercure protocol (built on top of Server-Sent Events).
- [messagebus](https://github.com/vardius/message-bus) - messagebus is a Go simple async message bus, perfect for using as event bus when doing event sourcing, CQRS, DDD.
- [NATS Go Client](https://github.com/nats-io/nats.go) - Go client for the NATS
  messaging system.
- [nsq-event-bus](https://github.com/rafaeljesus/nsq-event-bus) - A tiny wrapper around NSQ topic and channel.
- [oplog](https://github.com/dailymotion/oplog) - Generic oplog/replication system for REST APIs.
- [pubsub](https://github.com/tuxychandru/pubsub) - Simple pubsub package for go.
- [Quamina](https://github.com/timbray/quamina) - Fast pattern-matching for filtering messages and events.
- [rabbitroutine](https://github.com/furdarius/rabbitroutine) - Lightweight library that handles RabbitMQ auto-reconnect and publishing retries. The library takes into account the need to re-declare entities in RabbitMQ after reconnection.
- [rabbus](https://github.com/rafaeljesus/rabbus) - A tiny wrapper over amqp exchanges and queues.
- [rabtap](https://github.com/jandelgado/rabtap) - RabbitMQ swiss army knife cli app.
- [RapidMQ](https://github.com/sybrexsys/RapidMQ) - RapidMQ is a lightweight and reliable library for managing of the local messages queue.
- [Ratus](https://github.com/hyperonym/ratus) - Ratus is a RESTful asynchronous task queue server.
- [redisqueue](https://github.com/robinjoseph08/redisqueue) - redisqueue provides a producer and consumer of a queue that uses Redis streams.
- [rmqconn](https://github.com/sbabiv/rmqconn) - RabbitMQ Reconnection. Wrapper over amqp.Connection and amqp.Dial. Allowing to do a reconnection when the connection is broken before forcing the call to the Close () method to be closed.
- [sarama](https://github.com/Shopify/sarama) - Go library for Apache Kafka.
- [Uniqush-Push](https://github.com/uniqush/uniqush-push) - Redis backed unified push service for server-side notifications to mobile devices.
- [varmq](https://github.com/goptics/varmq) - A storage-agnostic message queue and worker pool for concurrent Go programs.
- [Watermill](https://github.com/ThreeDotsLabs/watermill) - Working efficiently with message streams. Building event driven applications, enabling event sourcing, RPC over messages, sagas. Can use conventional pub/sub implementations like Kafka or RabbitMQ, but also HTTP or MySQL binlog.
- [zmq4](https://github.com/pebbe/zmq4) - Go interface to ZeroMQ version 4. Also available for [version 3](https://github.com/pebbe/zmq3) and [version 2](https://github.com/pebbe/zmq2).

**[⬆ 回到顶部](#contents)**

<a id="microsoft-office"></a>
## Microsoft Office

- [unioffice](https://github.com/unidoc/unioffice) - Pure go library for creating and processing Office Word (.docx), Excel (.xlsx) and Powerpoint (.pptx) documents.

<a id="microsoft-excel"></a>
### Microsoft Excel

_用于处理 Microsoft Excel 的库。_

- [cellwalker](https://github.com/chonla/cellwalker) - Virtually traverse Excel cell by cell's name.
- [excelize](https://github.com/xuri/excelize) - Golang library for reading and writing Microsoft Excel&trade; (XLSX) files.
- [exl](https://github.com/go-the-way/exl) - Excel binding to struct written in Go.(Only supports Go1.18+)
- [go-excel](https://github.com/szyhf/go-excel) - A simple and light reader to read a relate-db-like excel as a table.
- [xlsx](https://github.com/tealeg/xlsx) - Library to simplify reading the XML format used by recent version of Microsoft Excel in Go programs.
- [xlsx](https://github.com/plandem/xlsx) - Fast and safe way to read/update your existing Microsoft Excel files in Go programs.

<a id="microsoft-word"></a>
### Microsoft Word

_用于处理 Microsoft Word 的库。_

- [godocx](https://github.com/gomutex/godocx) - Library for reading and writing Microsoft Word (Docx) files.

**[⬆ 回到顶部](#contents)**

<a id="miscellaneous"></a>
## 杂项

<a id="dependency-injection"></a>
### 依赖注入

_用于依赖注入的库。_

- [alice](https://github.com/magic003/alice) - Additive dependency injection container for Golang.
- [autowire](https://github.com/tiendc/autowire) - Dependency injection using Generics and reflection.
- [boot-go](http://github.com/boot-go/boot) - Component-based development with dependency injection using reflections for Go developers.
- [componego](https://github.com/componego/componego) - A dependency injection framework based on components, allowing dynamic dependency replacement without duplicating code in tests.
- [cosban/di](https://gitlab.com/cosban/di) - A code generation based dependency injection wiring tool.
- [dig](https://github.com/uber-go/dig) - A reflection based dependency injection toolkit for Go.
- [dingo](https://github.com/i-love-flamingo/dingo) - A dependency injection toolkit for Go, based on Guice.
- [do](https://github.com/samber/do) - A dependency injection framework based on Generics.
- [floatdrop/di](https://github.com/floatdrop/di) - Dependency injection container built on generic methods, with child scopes, lifecycle hooks and graph validation before anything is built.
- [fx](https://github.com/uber-go/fx) - A dependency injection based application framework for Go (built on top of dig).
- [go-beans](https://github.com/go-beans/go) - Spring-inspired dependency injection and application lifecycle framework for Go.
- [Go-Spring](https://github.com/go-spring/spring-core) - A high-performance Go framework inspired by Spring Boot, offering DI, auto-configuration, and lifecycle management while maintaining Go's simplicity and efficiency.
- [gocontainer](https://github.com/vardius/gocontainer) - Simple Dependency Injection Container.
- [godi](https://github.com/junioryono/godi) - Microsoft-style dependency injection for Go with scoped lifetimes and generics.
- [goioc/di](https://github.com/goioc/di) - Spring-inspired Dependency Injection Container.
- [GoLobby/Container](https://github.com/golobby/container) - GoLobby Container is a lightweight yet powerful IoC dependency injection container for the Go programming language.
- [gontainer](https://github.com/NVIDIA/gontainer) - A dependency injection service container for Go projects.
- [gontainer/gontainer](https://github.com/gontainer/gontainer) - A YAML-based Dependency Injection container for GO. It supports dependencies' scopes, and auto-detection of circular dependencies. Gontainer is concurrent-safe.
- [HnH/di](https://github.com/HnH/di) - DI container library that is focused on clean API and flexibility.
- [kinit](https://github.com/go-kata/kinit) - Customizable dependency injection container with the global mode, cascade initialization and panic-safe finalization.
- [kod](https://github.com/go-kod/kod) - A generics based dependency injection framework for Go.
- [linker](https://github.com/logrange/linker) - A reflection based dependency injection and inversion of control library with components lifecycle support.
- [nject](https://github.com/muir/nject) - A type safe, reflective framework for libraries, tests, http endpoints, and service startup.
- [ore](https://github.com/firasdarwish/ore) - Lightweight, generic & simple dependency injection (DI) container.
- [parsley](https://github.com/matzefriedrich/parsley) - A flexible and modular reflection-based DI library with advanced features like scoped contexts and proxy generation, designed for large-scale Go applications.
- [wire](https://github.com/Fs02/wire) - Strict Runtime Dependency Injection for Golang.
- [yama](https://github.com/livetribe/yama) - Compile-time dependency injection and lifecycle framework that generates start, quiesce, and stop code for Google Wire graphs.

**[⬆ 回到顶部](#contents)**

<a id="project-layout"></a>
### 项目结构布局

_**非官方**的项目结构设计模式集合。_

- [ardanlabs/service](https://github.com/ardanlabs/service) - A [starter kit](https://github.com/ardanlabs/service/wiki) for building production grade scalable web service applications.
- [cookiecutter-golang](https://github.com/lacion/cookiecutter-golang) - A Go application boilerplate template for quick starting projects following production best practices.
- [go-blueprint](https://github.com/Melkeydev/go-blueprint) - Allows users to spin up a quick Go project using a popular framework.
- [go-ddd](https://github.com/sklinkert/go-ddd) - Domain-Driven Design template with CQRS, value objects, idempotent commands, and a transactional outbox.
- [go-grpc-bazel-example](https://github.com/esurdam/go-grpc-bazel-example) - Example monorepo for Go gRPC microservices with Bazel, grpc-gateway, OpenAPI, and Kubernetes.
- [go-module](https://github.com/octomation/go-module) - Template for a typical module written on Go.
- [go-rest-api-boilerplate](https://github.com/vahiiiid/go-rest-api-boilerplate) - AI-friendly, production-ready Go REST API boilerplate with clean architecture, JWT authentication, RBAC, PostgreSQL, Docker hot-reload, and Swagger documentation.
- [go-sample](https://github.com/zitryss/go-sample) - A sample layout for Go application projects with the real code.
- [go-starter](https://github.com/allaboutapps/go-starter) - An opinionated production-ready RESTful JSON backend template, highly integrated with VSCode DevContainers.
- [go-todo-backend](https://github.com/Fs02/go-todo-backend) - Go Todo Backend example using modular project layout for product microservice.
- [goapp](https://github.com/naughtygopher/goapp) - An opinionated guideline to structure & develop a Go web application/service.
- [gobase](https://github.com/wajox/gobase) - A simple skeleton for golang application with basic setup for real golang application.
- [golang-standards/project-layout](https://github.com/golang-standards/project-layout) - Set of common historical and emerging project layout patterns in the Go ecosystem. Note: despite the org-name they do not represent official golang standards, see [this issue](https://github.com/golang-standards/project-layout/issues/117) for more information. Nonetheless, some may find the layout useful.
- [golang-templates/seed](https://github.com/golang-templates/seed) - Go application GitHub repository template.
- [goxygen](https://github.com/shpota/goxygen) - Generate a modern Web project with Go and Angular, React, or Vue in seconds.
- [insidieux/inizio](https://github.com/insidieux/inizio) - Golang project layout generator with plugins.
- [kickstart.go](https://github.com/raeperd/kickstart.go) - Minimalistic single-file Go HTTP server template without third-party dependencies.
- [modern-go-application](https://github.com/sagikazarmark/modern-go-application) - Go application boilerplate and example applying modern practices.
- [nunu](https://github.com/go-nunu/nunu) - Nunu is a scaffolding tool for building Go applications.
- [pagoda](https://github.com/mikestefanello/pagoda) - Rapid, easy full-stack web development starter kit built in Go.
- [scaffold](https://github.com/catchplay/scaffold) - Scaffold generates a starter Go project layout. Lets you focus on business logic implemented.
- [wangyoucao577/go-project-layout](https://github.com/wangyoucao577/go-project-layout) - Set of practices and discussions on how to structure Go project layout.

**[⬆ 回到顶部](#contents)**

<a id="strings"></a>
### 字符串

_用于字符串处理的库。_

- [bexp](https://github.com/happy-sdk/happy/tree/main/pkg/strings/bexp) - Go implementation of Brace Expansion mechanism to generate arbitrary strings.
- [caps](https://github.com/chanced/caps) - A case conversion library.
- [go-formatter](https://gitlab.com/tymonx/go-formatter) - Implements **replacement fields** surrounded by curly braces `{}` format strings.
- [gobeam/Stringy](https://github.com/gobeam/Stringy) - String manipulation library to convert string to camel case, snake case, kebab case / slugify etc.
- [str](https://github.com/schigh/str) - Pipeline-first string toolkit for composing transformations.
- [strcase](https://github.com/charlievieth/strcase) - Case-insensitive implementation of the standard library's strings/bytes packages.
- [stringFormatter](https://github.com/Wissance/stringFormatter) - String formatting like in Python or C# manner with the additional text formatting features.
- [strutil](https://github.com/ozgio/strutil) - String utilities.
- [sttr](https://github.com/abhimanyu003/sttr) - cross-platform, cli app to perform various operations on string.
- [xstrings](https://github.com/huandu/xstrings) - Collection of useful string functions ported from other languages.

**[⬆ 回到顶部](#contents)**

<a id="uncategorized"></a>
### 未分类

_这些库放在这里，是因为其他分类似乎都不太合适。_

- [anagent](https://github.com/mudler/anagent) - Minimalistic, pluggable Golang evloop/timer handler with dependency-injection.
- [antch](https://github.com/antchfx/antch) - A fast, powerful and extensible web crawling & scraping framework.
- [archives](https://github.com/mholt/archives) - a cross-platform, multi-format Go library for working with archives and compression formats with a unified API and as virtual file systems compatible with io/fs.
- [autoflags](https://github.com/artyom/autoflags) - Go package to automatically define command line flags from struct fields.
- [avgRating](https://github.com/kirillDanshin/avgRating) - Calculate average score and rating based on Wilson Score Equation.
- [banner](https://github.com/dimiro1/banner) - Add beautiful banners into your Go applications.
- [base64Captcha](https://github.com/mojocn/base64Captcha) - Base64captch supports digit, number, alphabet, arithmetic, audio and digit-alphabet captcha.
- [basexx](https://github.com/bobg/basexx) - Convert to, from, and between digit strings in various number bases.
- [battery](https://github.com/distatus/battery) - Cross-platform, normalized battery information library.
- [bitio](https://github.com/icza/bitio) - Highly optimized bit-level Reader and Writer for Go.
- [browscap_go](https://github.com/digitalcrab/browscap_go) - GoLang Library for [Browser Capabilities Project](https://browscap.org/).
- [captcha](https://github.com/steambap/captcha) - Package captcha provides an easy to use, unopinionated API for captcha generation.
- [common](https://github.com/kubeservice-stack/common) - A library for server framework.
- [conv](https://github.com/cstockton/go-conv) - Package conv provides fast and intuitive conversions across Go types.
- [datacounter](https://github.com/miolini/datacounter) - Go counters for readers/writer/http.ResponseWriter.
- [fake-useragent](https://github.com/lib4u/fake-useragent) - Up-to-date simple useragent faker with real world database in Golang
- [faker](https://github.com/pioz/faker) - Random fake data and struct generator for Go.
- [ffmt](https://github.com/go-ffmt/ffmt) - Beautify data display for Humans.
- [gatus](https://github.com/TwinProduction/gatus) - Automated service health dashboard.
- [go-commandbus](https://github.com/lana/go-commandbus) - A slight and pluggable command-bus for Go.
- [go-commons-pool](https://github.com/jolestar/go-commons-pool) - Generic object pool for Golang.
- [go-openapi](https://github.com/go-openapi) - Collection of packages to parse and utilize open-api schemas.
- [go-resiliency](https://github.com/eapache/go-resiliency) - Resiliency patterns for golang.
- [go-unarr](https://github.com/gen2brain/go-unarr) - Decompression library for RAR, TAR, ZIP and 7z archives.
- [gofakeit](https://github.com/brianvoe/gofakeit) - Random data generator written in go.
- [goffi](https://github.com/go-webgpu/goffi) - Pure Go FFI with libffi-style typed call interface and structured error handling for calling C libraries without CGO.
- [gommit](https://github.com/antham/gommit) - Analyze git commit messages to ensure they follow defined patterns.
- [gopsutil](https://github.com/shirou/gopsutil) - Cross-platform library for retrieving process and system utilization(CPU, Memory, Disks, etc).
- [gosh](https://github.com/osamingo/gosh) - Provide Go Statistics Handler, Struct, Measure Method.
- [gosms](https://github.com/haxpax/gosms) - Your own local SMS gateway in Go that can be used to send SMS.
- [gotoprom](https://github.com/cabify/gotoprom) - Type-safe metrics builder wrapper library for the official Prometheus client.
- [gountries](https://github.com/pariz/gountries) - Package that exposes country and subdivision data.
- [gtree](https://github.com/ddddddO/gtree) - Provide CLI, Package and Web for tree output and directories creation from Markdown or programmatically.
- [health](https://github.com/alexliesenfeld/health) - A simple and flexible health check library for Go.
- [health](https://github.com/dimiro1/health) - Easy to use, extensible health check library.
- [healthcheck](https://github.com/etherlabsio/healthcheck) - An opinionated and concurrent health-check HTTP handler for RESTful services.
- [hostutils](https://github.com/Wing924/hostutils) - A golang library for packing and unpacking FQDNs list.
- [indigo](https://github.com/osamingo/indigo) - Distributed unique ID generator of using Sonyflake and encoded by Base58.
- [lk](https://github.com/hyperboloide/lk) - A simple licensing library for golang.
- [llvm](https://github.com/llir/llvm) - Library for interacting with LLVM IR in pure Go.
- [metrics](https://github.com/pascaldekloe/metrics) - Library for metrics instrumentation and Prometheus exposition.
- [morse](https://github.com/alwindoss/morse) - Library to convert to and from morse code.
- [numa](https://github.com/lrita/numa) - NUMA is a utility library, which is written in go. It help us to write some NUMA-AWARED code.
- [pdfgen](https://github.com/hyperboloide/pdfgen) - HTTP service to generate PDF from Json requests.
- [persian](https://github.com/mavihq/persian) - Some utilities for Persian language in go.
- [purego](https://github.com/ebitengine/purego) - A library for calling C functions from Go without Cgo.
- [sandid](https://github.com/aofei/sandid) - Every grain of sand on earth has its own ID.
- [shellwords](https://github.com/Wing924/shellwords) - A Golang library to manipulate strings according to the word parsing rules of the UNIX Bourne shell.
- [shortid](https://github.com/teris-io/shortid) - Distributed generation of super short, unique, non-sequential, URL friendly IDs.
- [shoutrrr](https://github.com/containrrr/shoutrrr) - Notification library providing easy access to various messaging services like slack, mattermost, gotify and smtp among others.
- [sitemap-format](https://github.com/mingard/sitemap-format) - A simple sitemap generator, with a little syntactic sugar.
- [stateless](https://github.com/qmuntal/stateless) - A fluent library for creating state machines.
- [stats](https://github.com/go-playground/stats) - Monitors Go MemStats + System stats such as Memory, Swap and CPU and sends via UDP anywhere you want for logging etc...
- [turtle](https://github.com/hackebrot/turtle) - Emojis for Go.
- [url-shortener](https://github.com/pantrif/url-shortener) - A modern, powerful, and robust URL shortener microservice with mysql support.
- [VarHandler](https://github.com/azr/generators/tree/master/varhandler) - Generate boilerplate http input and output handling.
- [varint](https://github.com/chmike/varint) - A faster varying length integer encoder/decoder than the one provided in the standard library.
- [xdg](https://github.com/rkoesters/xdg) - FreeDesktop.org (xdg) Specs implemented in Go.
- [xkg](https://github.com/go-xkg/xkg) - X Keyboard Grabber.
- [xz](https://github.com/ulikunitz/xz) - Pure golang package for reading and writing xz-compressed files.
**[⬆ 回到顶部](#contents)**

<a id="natural-language-processing"></a>
## 自然语言处理

_用于自然语言处理的库。_

另见[文本处理](#text-processing)与[文本分析](#text-analysis)。

<a id="language-detection"></a>
### 语言检测

- [detectlanguage](https://github.com/detectlanguage/detectlanguage-go) - Language Detection API Go Client. Supports batch requests, short phrase or single word language detection.
- [getlang](https://github.com/rylans/getlang) - Fast natural language detection package.
- [guesslanguage](https://github.com/endeveit/guesslanguage) - Functions to determine the natural language of a unicode text.
- [lingua-go](https://github.com/pemistahl/lingua-go) - An accurate natural language detection library, suitable for long and short text alike. Supports detecting multiple languages in mixed-language text.
- [whatlanggo](https://github.com/abadojack/whatlanggo) - Natural language detection package for Go. Supports 84 languages and 24 scripts (writing systems e.g. Latin, Cyrillic, etc).

<a id="morphological-analyzers"></a>
### 形态分析器

- [go-propisyu](https://github.com/rekurt/go-propisyu) - Convert numbers to Russian words with correct grammatical gender and noun declension.
- [go-stem](https://github.com/agonopol/go-stem) - Implementation of the porter stemming algorithm.
- [go2vec](https://github.com/danieldk/go2vec) - Reader and utility functions for word2vec embeddings.
- [golibstemmer](https://github.com/rjohnsondev/golibstemmer) - Go bindings for the snowball libstemmer library including porter 2.
- [gosentiwordnet](https://github.com/dinopuguh/gosentiwordnet) - Sentiment analyzer using sentiwordnet lexicon in Go.
- [govader](https://github.com/jonreiter/govader) - Go implementation of [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment).
- [govader-backend](https://github.com/PIMPfiction/govader_backend) - Microservice implementation of [GoVader](https://github.com/jonreiter/govader).
- [kagome](https://github.com/ikawaha/kagome) - JP morphological analyzer written in pure Go.
- [libtextcat](https://github.com/goodsign/libtextcat) - Cgo binding for libtextcat C library. Guaranteed compatibility with version 2.2.
- [nlp](https://github.com/james-bowman/nlp) - Go Natural Language Processing library supporting LSA (Latent Semantic Analysis).
- [paicehusk](https://github.com/rookii/paicehusk) - Golang implementation of the Paice/Husk Stemming Algorithm.
- [porter](https://github.com/a2800276/porter) - This is a fairly straightforward port of Martin Porter's C implementation of the Porter stemming algorithm.
- [porter2](https://github.com/zhenjl/porter2) - Really fast Porter 2 stemmer.
- [RAKE.go](https://github.com/afjoseph/RAKE.Go) - Go port of the Rapid Automatic Keyword Extraction Algorithm (RAKE).
- [snowball](https://github.com/goodsign/snowball) - Snowball stemmer port (cgo wrapper) for Go. Provides word stem extraction functionality [Snowball native](http://snowball.tartarus.org/).
- [spaGO](https://github.com/nlpodyssey/spago) - Self-contained Machine Learning and Natural Language Processing library in Go.
- [spelling-corrector](https://github.com/jorelosorio/spellingcorrector) - A spelling corrector for the Spanish language or create your own.

<a id="slugifiers"></a>
### Slug 生成器

- [go-slugify](https://github.com/mozillazg/go-slugify) - Make pretty slug with multiple languages support.
- [slug](https://github.com/gosimple/slug) - URL-friendly slugify with multiple languages support.
- [Slugify](https://github.com/avelino/slugify) - Go slugify application that handles string.

<a id="tokenizers"></a>
### 分词器

- [gojieba](https://github.com/yanyiwu/gojieba) - This is a Go implementation of [jieba](https://github.com/fxsjy/jieba) which a Chinese word splitting algorithm.
- [gotokenizer](https://github.com/xujiajun/gotokenizer) - A tokenizer based on the dictionary and Bigram language models for Golang. (Now only support chinese segmentation)
- [gse](https://github.com/go-ego/gse) - Go efficient text segmentation; support english, chinese, japanese and other.
- [MMSEGO](https://github.com/awsong/MMSEGO) - This is a GO implementation of [MMSEG](http://technology.chtsai.org/mmseg/) which a Chinese word splitting algorithm.
- [segment](https://github.com/blevesearch/segment) - Go library for performing Unicode Text Segmentation as described in [Unicode Standard Annex #29](https://www.unicode.org/reports/tr29/)
- [sentences](https://github.com/neurosnap/sentences) - Sentence tokenizer: converts text into a list of sentences.
- [shamoji](https://github.com/osamingo/shamoji) - The shamoji is word filtering package written in Go.
- [stemmer](https://github.com/dchest/stemmer) - Stemmer packages for Go programming language. Includes English and German stemmers.
- [textcat](https://github.com/pebbe/textcat) - Go package for n-gram based text categorization, with support for utf-8 and raw text.

<a id="translation"></a>
### 翻译

- [ctxi18n](https://github.com/invopop/ctxi18n/) - Context aware i18n with a short and consise API, pluralization, interpolation, and `fs.FS` support. YAML locale definitions are based on [Rails i18n](https://guides.rubyonrails.org/i18n.html).
- [go-i18n](https://github.com/nicksnyder/go-i18n/) - Package and an accompanying tool to work with localized text.
- [go-mystem](https://github.com/dveselov/mystem) - CGo bindings to Yandex.Mystem - russian morphology analyzer.
- [go-pinyin](https://github.com/mozillazg/go-pinyin) - CN Hanzi to Hanyu Pinyin converter.
- [go-words](https://github.com/saleh-rahimzadeh/go-words) - A words table and text resource library for Golang projects.
- [gotext](https://github.com/leonelquinteros/gotext) - GNU gettext utilities for Go.
- [iuliia-go](https://github.com/mehanizm/iuliia-go) - Transliterate Cyrillic → Latin in every possible way.
- [spreak](https://github.com/vorlif/spreak) - Flexible translation and humanization library for Go, based on the concepts behind gettext.
- [t](https://github.com/youthlin/t) - Another i18n pkg for golang, which follows GNU gettext style and supports .po/.mo files: `t.T (gettext)`, `t.N (ngettext)`, etc. And it contains a cmd tool [xtemplate](https://github.com/youthlin/t/blob/main/cmd/xtemplate), which can extract messages as a pot file from text/html template.

<a id="transliteration"></a>
### 音译

- [enca](https://github.com/endeveit/enca) - Minimal cgo bindings for [libenca](https://cihar.com/software/enca/), which detects character encodings.
- [go-unidecode](https://github.com/mozillazg/go-unidecode) - ASCII transliterations of Unicode text.
- [gounidecode](https://github.com/fiam/gounidecode) - Unicode transliterator (also known as unidecode) for Go.
- [transliterator](https://github.com/alexsergivan/transliterator) - Provides one-way string transliteration with supporting of language-specific transliteration rules.

**[⬆ 回到顶部](#contents)**

<a id="networking"></a>
## 网络

_用于处理网络各层的库。_

- [arp](https://github.com/mdlayher/arp) - Package arp implements the ARP protocol, as described in RFC 826.
- [bart](https://github.com/gaissmai/bart) - Package bart provides a Balanced-Routing-Table (BART) for very fast IP to CIDR lookups and more.
- [buffstreams](https://github.com/stabbycutyou/buffstreams) - Streaming protocolbuffer data over TCP made easy.
- [canopus](https://github.com/zubairhamed/canopus) - CoAP Client/Server implementation (RFC 7252).
- [cdns](https://github.com/junevm/cdns) - Change DNS servers effortlessly via terminal.
- [chicha-ip-proxy](https://github.com/matveynator/chicha-ip-proxy) - Zero-configuration TCP/UDP port proxy with autostart, IP-based access control, and OS-level network stack tuning.
- [cidranger](https://github.com/yl2chen/cidranger) - Fast IP to CIDR lookup for Go.
- [cloudflared](https://github.com/cloudflare/cloudflared) - Cloudflare Tunnel client (formerly Argo Tunnel).
- [dhcp6](https://github.com/mdlayher/dhcp6) - Package dhcp6 implements a DHCPv6 server, as described in RFC 3315.
- [dns](https://github.com/miekg/dns) - Go library for working with DNS.
- [dnsmonster](https://github.com/mosajjal/dnsmonster) - Passive DNS Capture/Monitoring Framework.
- [drainwatch](https://github.com/jaynirmal15/drainwatch) - Measures what actually happens to established TCP and UDP connections when a Kubernetes pod terminates.
- [easytcp](https://github.com/DarthPestilane/easytcp) - A light-weight TCP framework written in Go (Golang), built with message router. EasyTCP helps you build a TCP server easily fast and less painful.
- [ether](https://github.com/songgao/ether) - Cross-platform Go package for sending and receiving ethernet frames.
- [ethernet](https://github.com/mdlayher/ethernet) - Package ethernet implements marshaling and unmarshalling of IEEE 802.3 Ethernet II frames and IEEE 802.1Q VLAN tags.
- [event](https://github.com/cheng-zhongliang/event) - Simple I/O event notification library written in Golang.
- [expose](https://github.com/kernelshard/expose) - Lightweight, open-source secure tunneling tool to expose local servers to the internet.
- [fasthttp](https://github.com/valyala/fasthttp) - Package fasthttp is a fast HTTP implementation for Go, up to 10 times faster than net/http.
- [fibersse](https://github.com/vinod-morya/fibersse) - Production-grade Server-Sent Events (SSE) for Fiber v3 with event coalescing, priority lanes, topic wildcards, adaptive throttling, and built-in auth.
- [fortio](https://github.com/fortio/fortio) - Load testing library and command line tool, advanced echo server and web UI. Allows to specify a set query-per-second load and record latency histograms and other useful stats and graph them. Tcp, Http, gRPC.
- [ftp](https://github.com/jlaffaye/ftp) - Package ftp implements a FTP client as described in [RFC 959](https://tools.ietf.org/html/rfc959).
- [ftpserverlib](https://github.com/fclairamb/ftpserverlib) - Fully featured FTP server library.
- [fullproxy](https://github.com/shoriwe/fullproxy) - A fully featured scriptable and daemon configurable proxy and pivoting toolkit with SOCKS5, HTTP, raw ports and reverse proxy protocols.
- [fwdctl](https://github.com/alegrey91/fwdctl) - A simple and intuitive CLI to manage IPTables forwards in your Linux server.
- [gaio](https://github.com/xtaci/gaio) - High performance async-io networking for Golang in proactor mode.
- [gev](https://github.com/Allenxuxu/gev) - gev is a lightweight, fast non-blocking TCP network library based on Reactor mode.
- [gldap](https://github.com/jimlambrt/gldap) - gldap provides an ldap server implementation and you provide handlers for its ldap operations.
- [gmqtt](https://github.com/DrmagicE/gmqtt) - Gmqtt is a flexible, high-performance MQTT broker library that fully implements the MQTT protocol V3.1.1.
- [gnet](https://github.com/panjf2000/gnet) - `gnet` is a high-performance, lightweight, non-blocking, event-driven networking framework written in pure Go.
- [gnet](https://github.com/fish-tennis/gnet) - `gnet` is a high-performance networking framework,especially for game servers.
- [gNxI](https://github.com/google/gnxi) - A collection of tools for Network Management that use the gNMI and gNOI protocols.
- [go-getter](https://github.com/hashicorp/go-getter) - Go library for downloading files or directories from various sources using a URL.
- [go-multiproxy](https://github.com/presbrey/go-multiproxy) - Library for making HTTP requests through a pool of proxies offering fault tolerance, load balancing, automatic retries, cookie management, and more, via http.Get/Post replacement or http.Client RoundTripper drop-in
- [go-pcaplite](https://github.com/alexcfv/go-pcaplite) - Lightweight live packet capture library with HTTPS SNI extraction.
- [go-powerdns](https://github.com/joeig/go-powerdns) - PowerDNS API bindings for Golang.
- [go-sse](https://github.com/lampctl/go-sse) - Go client and server implementation of HTML server-sent events.
- [go-stun](https://github.com/ccding/go-stun) - Go implementation of the STUN client (RFC 3489 and RFC 5389).
- [gobgp](https://github.com/osrg/gobgp) - BGP implemented in the Go Programming Language.
- [gopacket](https://github.com/google/gopacket) - Go library for packet processing with libpcap bindings.
- [gopcap](https://github.com/akrennmair/gopcap) - Go wrapper for libpcap.
- [GoProxy](https://github.com/elazarl/goproxy) - A library to create a customized HTTP/HTTPS proxy server using Go.
- [goshark](https://github.com/sunwxg/goshark) - Package goshark use tshark to decode IP packet and create data struct to analyse packet.
- [gosnmp](https://github.com/soniah/gosnmp) - Native Go library for performing SNMP actions.
- [gotcp](https://github.com/gansidui/gotcp) - Go package for quickly writing tcp applications.
- [grab](https://github.com/cavaliercoder/grab) - Go package for managing file downloads.
- [graval](https://github.com/koofr/graval) - Experimental FTP server framework.
- [gws](https://github.com/lxzan/gws) - High-Performance WebSocket Server & Client With AsyncIO Supporting .
- [HTTPLab](https://github.com/gchaincl/httplab) - HTTPLabs let you inspect HTTP requests and forge responses.
- [httpproxy](https://github.com/wzshiming/httpproxy) - HTTP proxy handler and dialer.
- [iplib](https://github.com/c-robinson/iplib) - Library for working with IP addresses (net.IP, net.IPNet), inspired by python [ipaddress](https://docs.python.org/3/library/ipaddress.html) and ruby [ipaddr](https://ruby-doc.org/stdlib-2.5.1/libdoc/ipaddr/rdoc/IPAddr.html)
- [jazigo](https://github.com/udhos/jazigo) - Jazigo is a tool written in Go for retrieving configuration for multiple network devices.
- [kcp-go](https://github.com/xtaci/kcp-go) - KCP - Fast and Reliable ARQ Protocol.
- [lhttp](https://github.com/fanux/lhttp) - Powerful websocket framework, build your IM server more easily.
- [linkio](https://github.com/ian-kent/linkio) - Network link speed simulation for Reader/Writer interfaces.
- [llb](https://github.com/kirillDanshin/llb) - It's a very simple but quick backend for proxy servers. Can be useful for fast redirection to predefined domain with zero memory allocation and fast response.
- [macwifi](https://github.com/jaisonerick/macwifi) - Wi-Fi scanning and Keychain password retrieval for macOS 13+.
- [mdns](https://github.com/hashicorp/mdns) - Simple mDNS (Multicast DNS) client/server library in Golang.
- [mqttPaho](https://eclipse.org/paho/clients/golang/) - The Paho Go Client provides an MQTT client library for connection to MQTT brokers via TCP, TLS or WebSockets.
- [natiu-mqtt](https://github.com/soypat/natiu-mqtt) - A dead-simple, non-allocating, low level implementation of MQTT well suited for embedded systems.
- [nbio](https://github.com/lesismal/nbio) - Pure Go 1000k+ connections solution, support tls/http1.x/websocket and basically compatible with net/http, with high-performance and low memory cost, non-blocking, event-driven, easy-to-use.
- [net](https://golang.org/x/net) - This repository holds supplementary Go networking libraries.
- [netchan](https://github.com/matveynator/netchan) - Network Channels (netchan) for Golang: Secure, cluster-ready, supports nested channels & any data type. Inspired by Rob Pike.
- [nethawk](https://github.com/Flowtriq/nethawk) - Terminal UI for real-time network traffic capture, analysis, and attack detection with JSON output mode.
- [netpoll](https://github.com/cloudwego/netpoll) - A high-performance non-blocking I/O networking framework, which focused on RPC scenarios, developed by ByteDance.
- [NFF-Go](https://github.com/intel-go/nff-go) - Framework for rapid development of performant network functions for cloud and bare-metal (former YANFF).
- [nodepass](https://github.com/NodePassProject/nodepass) - A secure, efficient TCP/UDP tunneling solution that delivers fast, reliable access across network restrictions using pre-established TCP/QUIC/WebSocket or HTTP/2 connections.
- [peerdiscovery](https://github.com/schollz/peerdiscovery) - Pure Go library for cross-platform local peer discovery using UDP multicast.
- [portproxy](https://github.com/aybabtme/portproxy) - Simple TCP proxy which adds CORS support to API's which don't support it.
- [proxq](https://github.com/psyb0t/docker-proxq) - Asynchronous reverse proxy that queues each request in Redis and returns a job ID to poll for the response, with path-prefix routing, retries, and caching.
- [psql-wire](https://github.com/jeroenrinzema/psql-wire) - PostgreSQL server wire protocol. Build your own server and start serving connections..
- [publicip](https://github.com/polera/publicip) - Package publicip returns your public facing IPv4 address (internet egress).
- [quic-go](https://github.com/lucas-clemente/quic-go) - An implementation of the QUIC protocol in pure Go.
- [roamr](https://github.com/sourabh-khot65/roamr) - CLI that scores nearby saved WiFi networks and tells you which to use, and why.
- [sdns](https://github.com/semihalev/sdns) - A high-performance, recursive DNS resolver server with DNSSEC support, focused on preserving privacy.
- [sftp](https://github.com/pkg/sftp) - Package sftp implements the SSH File Transfer Protocol as described in <https://filezilla-project.org/specs/draft-ietf-secsh-filexfer-02.txt>.
- [ssh](https://github.com/gliderlabs/ssh) - Higher-level API for building SSH servers (wraps crypto/ssh).
- [sslb](https://github.com/eduardonunesp/sslb) - It's a Super Simples Load Balancer, just a little project to achieve some kind of performance.
- [stun](https://github.com/go-rtc/stun) - Go implementation of RFC 5389 STUN protocol.
- [tcpack](https://github.com/lim-yoona/tcpack) - tcpack is an application protocol based on TCP to Pack and Unpack bytes stream in go program.
- [tspool](https://github.com/two/tspool) - A TCP Library use worker pool to improve performance and protect your server.
- [tun2socks](https://github.com/xjasonlyu/tun2socks) - A pure go implementation of tun2socks powered by [gVisor](https://gvisor.dev/) TCP/IP stack.
- [utp](https://github.com/anacrolix/utp) - Go uTP micro transport protocol implementation.
- [vssh](https://github.com/yahoo/vssh) - Go library for building network and server automation over SSH protocol.
- [water](https://github.com/songgao/water) - Simple TUN/TAP library.
- [webrtc](https://github.com/pions/webrtc) - A pure Go implementation of the WebRTC API.
- [winrm](https://github.com/masterzen/winrm) - Go WinRM client to remotely execute commands on Windows machines.
- [ws-reconnect](https://github.com/sing198/ws-reconnect) - Resilient WebSocket client with automatic reconnection, exponential backoff, and heartbeat management.
- [xtcp](https://github.com/xfxdev/xtcp) - TCP Server Framework with simultaneous full duplex communication, graceful shutdown, and custom protocol.

**[⬆ 回到顶部](#contents)**

<a id="http-clients"></a>
### HTTP 客户端

_用于发起 HTTP 请求的库。_

- [axios4go](https://github.com/rezmoss/axios4go) - A Go HTTP client library inspired by Axios, providing a simple and intuitive API for making HTTP requests.
- [azuretls-client](https://github.com/Noooste/azuretls-client) - An easy-to-use HTTP client 100% in Go to spoof TLS/JA3 and HTTP2 fingerprint.
- [fast-shot](https://github.com/opus-domini/fast-shot) - Hit your API targets with rapid-fire precision using Go's fastest and simple HTTP Client.
- [gentleman](https://github.com/h2non/gentleman) - Full-featured plugin-driven HTTP client library.
- [go-cleanhttp](https://github.com/hashicorp/go-cleanhttp) - Get easily stdlib HTTP client, which does not share any state with other clients.
- [go-http-client](https://github.com/bozd4g/go-http-client) - Make http calls simply and easily.
- [go-ipmux](https://github.com/optimus-hft/go-ipmux) - A library for Multiplexing HTTP requests based on multiple Source IPs.
- [go-otelroundtripper](https://github.com/NdoleStudio/go-otelroundtripper) - Go http.RoundTripper that emits open telemetry metrics for HTTP requests.
- [go-req](https://github.com/wenerme/go-req) - Declarative golang HTTP client.
- [go-retryablehttp](https://github.com/hashicorp/go-retryablehttp) - Retryable HTTP client in Go.
- [go-zoox/fetch](https://github.com/go-zoox/fetch) - A Powerful, Lightweight, Easy Http Client, inspired by Web Fetch API.
- [Grequest](https://github.com/lib4u/grequest)  - Simple and lightweight golang package for http requests. based on powerful net/http
- [grequests](https://github.com/levigross/grequests) - A Go "clone" of the great and famous Requests library.
- [hedge](https://github.com/bhope/hedge) - Adaptive hedged requests for Go. Cuts p99 latency with zero configuration, based on Google's "The Tail at Scale" paper.
- [heimdall](https://github.com/gojektech/heimdall) - An enhanced http client with retry and hystrix capabilities.
- [httpretry](https://github.com/ybbus/httpretry) - Enriches the default go HTTP client with retry functionality.
 - [impersonate-http](https://github.com/North-web-dev/impersonate-http) - Drop-in net/http.Client with a byte-exact browser TLS (JA3/JA4) and HTTP/2 (Akamai) fingerprint.
- [pester](https://github.com/sethgrid/pester) - Go HTTP client calls with retries, backoff, and concurrency.
- [req](https://github.com/imroc/req) - Simple Go HTTP client with Black Magic (Less code and More efficiency).
- [request](https://github.com/monaco-io/request) - HTTP client for golang. If you have experience about axios or requests, you will love it. No 3rd dependency.
- [requests](https://github.com/carlmjohnson/requests) - HTTP requests for Gophers. Uses context.Context and doesn't hide the underlying net/http.Client, making it compatible with standard Go APIs. Also includes testing tools.
- [resty](https://github.com/go-resty/resty) - Simple HTTP and REST client for Go inspired by Ruby rest-client.
- [rq](https://github.com/ddo/rq) - A nicer interface for golang stdlib HTTP client.
- [sling](https://github.com/dghubble/sling) - Sling is a Go HTTP client library for creating and sending API requests.
- [surf](https://github.com/enetx/surf) - Advanced HTTP client with HTTP/1.1, HTTP/2, HTTP/3 (QUIC), SOCKS5 proxy support and browser-grade TLS fingerprinting.
- [tls-client](https://github.com/bogdanfinn/tls-client) - net/http.Client like HTTP Client with options to select specific client TLS Fingerprints to use for requests.

**[⬆ 回到顶部](#contents)**

<a id="opengl"></a>
## OpenGL

_在 Go 中使用 OpenGL 的库。_

- [gl](https://github.com/go-gl/gl) - Go bindings for OpenGL (generated via glow).
- [glfw](https://github.com/go-gl/glfw) - Go bindings for GLFW 3.
- [go-glmatrix](https://github.com/technohippy/go-glmatrix) - Go port of [glMatrix](https://glmatrix.net/) library.
- [goxjs/gl](https://github.com/goxjs/gl) - Go cross-platform OpenGL bindings (OS X, Linux, Windows, browsers, iOS, Android).
- [goxjs/glfw](https://github.com/goxjs/glfw) - Go cross-platform glfw library for creating an OpenGL context and receiving events.
- [mathgl](https://github.com/go-gl/mathgl) - Pure Go math package specialized for 3D math, with inspiration from GLM.

**[⬆ 回到顶部](#contents)**

<a id="orm"></a>
## ORM

_实现对象关系映射（ORM）或数据映射技术的库。_

- [bob](https://github.com/stephenafamo/bob) - SQL query builder and ORM/Factory generator for Go. Successor of SQLBoiler.
- [bun](https://github.com/uptrace/bun) - SQL-first Golang ORM. Successor of go-pg.
- [cacheme](https://github.com/Yiling-J/cacheme-go) - Schema based, typed Redis caching/memoize framework for Go.
- [CQL](https://github.com/FrancoLiberali/cql) - Built on top of GORM, adds compile-time verified queries based on auto-generated code.
- [ent](https://github.com/facebook/ent) - An entity framework for Go. Simple, yet powerful ORM for modeling and querying data.
- [go-dbw](https://github.com/hashicorp/go-dbw) - A simple package that encapsulates database operations.
- [go-firestorm](https://github.com/jschoedt/go-firestorm) - A simple ORM for Google/Firebase Cloud Firestore.
- [go-sql](https://github.com/rushteam/gosql) - A easy ORM for mysql.
- [go-sqlbuilder](https://github.com/huandu/go-sqlbuilder) - A flexible and powerful SQL string builder library plus a zero-config ORM.
- [go-store](https://github.com/gosuri/go-store) - Simple and fast Redis backed key-value store library for Go.
- [golobby/orm](https://github.com/golobby/orm) - Simple, fast, type-safe, generic orm for developer happiness.
- [GoooQo](https://github.com/doytowin/goooqo) - A database access framework based on declarative query model.
- [GORM](https://github.com/go-gorm/gorm) - The fantastic ORM library for Golang, aims to be developer friendly.
- [gormt](https://github.com/xxjwxc/gormt) - Mysql database to golang gorm struct.
- [gorp](https://github.com/go-gorp/gorp) - Go Relational Persistence, ORM-ish library for Go.
- [grimoire](https://github.com/Fs02/grimoire) - Grimoire is a database access layer and validation for golang. (Support: MySQL, PostgreSQL and SQLite3).
- [lore](https://github.com/abrahambotros/lore) - Simple and lightweight pseudo-ORM/pseudo-struct-mapping environment for Go.
- [marlow](https://github.com/marlow/marlow) - Generated ORM from project structs for compile time safety assurances.
- [pop/soda](https://github.com/gobuffalo/pop) - Database migration, creation, ORM, etc... for MySQL, PostgreSQL, and SQLite.
- [Prisma](https://github.com/prisma/prisma-client-go) - Prisma Client Go, Typesafe database access for Go.
- [reform](https://github.com/go-reform/reform) - Better ORM for Go, based on non-empty interfaces and code generation.
- [rel](https://github.com/go-rel/rel) - Modern Database Access Layer for Golang - Testable, Extendable and Crafted Into a Clean and Elegant API.
- [SQLBoiler](https://github.com/volatiletech/sqlboiler) - ORM generator. Generate a featureful and blazing-fast ORM tailored to your database schema.
- [upper.io/db](https://github.com/upper/db) - Single interface for interacting with different data sources through the use of adapters that wrap mature database drivers.
- [XORM](https://gitea.com/xorm/xorm) - Simple and powerful ORM for Go. (Support: MySQL, MyMysql, PostgreSQL, Tidb, SQLite3, MsSql and Oracle).
- [Zoom](https://github.com/albrow/zoom) - Blazing-fast datastore and querying engine built on Redis.

**[⬆ 回到顶部](#contents)**

<a id="package-management"></a>
## 包管理

_官方依赖与包管理工具_

- [go modules](https://golang.org/cmd/go/#hdr-Modules__module_versions__and_more) - Modules are the unit of source code interchange and versioning. The go command has direct support for working with modules, including recording and resolving dependencies on other modules.

_非官方的包与依赖管理库。_

- [gup](https://github.com/nao1215/gup) - Update binaries installed by "go install".
- [modup](https://github.com/chaindead/modup) - Terminal UI for Go dependency updates with outdated module detection and selective upgrading.
- [syft](https://github.com/anchore/syft) - A CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems.

**[⬆ 回到顶部](#contents)**

<a id="performance"></a>
## 性能

- [ebpf-go](https://github.com/cilium/ebpf) - Provides utilities for loading, compiling, and debugging eBPF programs.
- [go-instrument](https://github.com/nikolaydubina/go-instrument) - Automatically add spans to all methods and functions.
- [go-perfstat](https://github.com/go-perfstat/go) - Lightweight performance statistics and execution time aggregation for Go.
- [jaeger](https://github.com/jaegertracing/jaeger) - A distributed tracing system.
- [mm-go](https://github.com/joetifa2003/mm-go) - Generic manual memory management for golang.
- [otelinji](https://github.com/hedhyw/otelinji) - OpenTelemetry auto-instrumentation tool for adding spans to functions.
- [pixie](https://github.com/pixie-labs/pixie) - No instrumentation tracing for Golang applications via eBPF.
- [profile](https://github.com/pkg/profile) - Simple profiling support package for Go.
- [statsviz](https://github.com/arl/statsviz) - Live visualization of your Go application runtime statistics.
- [tracer](https://github.com/kamilsk/tracer) - Simple, lightweight tracing.

**[⬆ 回到顶部](#contents)**

<a id="query-language"></a>
## 查询语言

- [api-fu](https://github.com/ccbrown/api-fu) - Comprehensive GraphQL implementation.
- [dasel](https://github.com/tomwright/dasel) - Query and update data structures using selectors from the command line. Comparable to jq/yq but supports JSON, YAML, TOML and XML with zero runtime dependencies.
- [gnata](https://github.com/RecoLabs/gnata) - Pure-Go implementation of the JSONata 2.x query and transformation language.
- [gojsonq](https://github.com/thedevsaddam/gojsonq) - A simple Go package to Query over JSON Data.
- [goven](https://github.com/SeldonIO/goven) - A drop-in query language for any database schema.
- [gqlgen](https://github.com/99designs/gqlgen) - go generate based graphql server library.
- [grapher](https://github.com/reaganiwadha/grapher) - A GraphQL field builder utilizing Go generics with extra utilities and features.
- [graphql](https://github.com/neelance/graphql-go) - GraphQL server with a focus on ease of use.
- [graphql-go](https://github.com/graphql-go/graphql) - Implementation of GraphQL for Go.
- [gws](https://github.com/Zaba505/gws) - Apollos' "GraphQL over Websocket" client and server implementation.
- [jsonpath](https://github.com/AsaiYusuke/jsonpath) - A query library for retrieving part of JSON based on JSONPath syntax.
- [jsonql](https://github.com/elgs/jsonql) - JSON query expression library in Golang.
- [jsonslice](https://github.com/bhmj/jsonslice) - Jsonpath queries with advanced filters.
- [mql](https://github.com/hashicorp/mql) - Model Query Language (mql) is a query language for your database models.
- [play](https://github.com/paololazzari/play) - A TUI playground to experiment with your favorite programs, such as grep, sed, awk, jq and yq.
- [rql](https://github.com/a8m/rql) - Resource Query Language for REST API.
- [rqp](https://github.com/timsolov/rest-query-parser) - Query Parser for REST API. Filtering, validations, both `AND`, `OR` operations are supported directly in the query.
- [straf](https://github.com/SonicRoshan/straf) - Easily Convert Golang structs to GraphQL objects.

**[⬆ 回到顶部](#contents)**

<a id="reflection"></a>
## 反射

- [copy](https://github.com/gotidy/copy) - Package for fast copying structs of different types.
- [Deepcopier](https://github.com/ulule/deepcopier) - Simple struct copying for Go.
- [go-deepcopy](https://github.com/tiendc/go-deepcopy) - Fast deep copy library.
- [goenum](https://github.com/lvyahui8/goenum) - A common enumeration struct based on generics and reflection that allows you to quickly define enumerations and use a set of useful default methods.
- [gotype](https://github.com/wzshiming/gotype) - Golang source code parsing, usage like reflect package.
- [gpath](https://github.com/tenntenn/gpath) - Library to simplify access struct fields with Go's expression in reflection.
- [objwalker](https://github.com/rekby/objwalker) - Walk by go objects with reflection.
- [reflectpro](https://github.com/gontainer/reflectpro) - Callers, copiers, getters and setters for go.
- [reflectutils](https://github.com/muir/reflectutils) - Helpers for working with reflection: struct tag parsing; recursive walking; fill value from string.

**[⬆ 回到顶部](#contents)**

<a id="resource-embedding"></a>
## 资源嵌入

- [debme](https://github.com/leaanthony/debme) - Create an `embed.FS` from an existing `embed.FS` subdirectory.
- [embed](https://pkg.go.dev/embed) - Package embed provides access to files embedded in the running Go program.
- [rebed](https://github.com/soypat/rebed) - Recreate folder structures and files from Go 1.16's `embed.FS` type
- [vfsgen](https://github.com/shurcooL/vfsgen) - Generates a vfsdata.go file that statically implements the given virtual filesystem.

**[⬆ 回到顶部](#contents)**

<a id="science-and-data-analysis"></a>
## 科学与数据分析

_用于科学计算与数据分析的库。_

- [bradleyterry](https://github.com/seanhagen/bradleyterry) - Provides a Bradley-Terry Model for pairwise comparisons.
- [calendarheatmap](https://github.com/nikolaydubina/calendarheatmap) - Calendar heatmap in plain Go inspired by Github contribution activity.
- [chart](https://github.com/vdobler/chart) - Simple Chart Plotting library for Go. Supports many graphs types.
- [dataframe-go](https://github.com/rocketlaunchr/dataframe-go) - Dataframes for machine-learning and statistics (similar to pandas).
- [decimal](https://github.com/db47h/decimal) - Package decimal implements arbitrary-precision decimal floating-point arithmetic.
- [entitydebs](https://github.com/ndabAP/entitydebs) - A social science tool to programmatically analyze entities in non-fictional texts with a built-in dependency parser.
- [evaler](https://github.com/soniah/evaler) - Simple floating point arithmetic expression evaluator.
- [ewma](https://github.com/VividCortex/ewma) - Exponentially-weighted moving averages.
- [geom](https://github.com/skelterjohn/geom) - 2D geometry for golang.
- [go-dsp](https://github.com/mjibson/go-dsp) - Digital Signal Processing for Go.
- [go-estimate](https://github.com/milosgajdos/go-estimate) - State estimation and filtering algorithms in Go.
- [go-gt](https://github.com/ThePaw/go-gt) - Graph theory algorithms written in "Go" language.
- [go-hep](https://github.com/go-hep/hep) - A set of libraries and tools for performing High Energy Physics analyses with ease.
- [godesim](https://github.com/soypat/godesim) - Extended/multivariable ODE solver framework for event-based simulations with simple API.
- [goent](https://github.com/kzahedi/goent) - GO Implementation of Entropy Measures.
- [gograph](https://github.com/hmdsefi/gograph) - A golang generic graph library that provides mathematical graph-theory and algorithms.
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
- [coverage](https://github.com/jbunds/coverage) - A simple Web UI for Go test coverage, and the [go-test-coverage-html-report](https://github.com/marketplace/actions/go-test-coverage-html-report) reusable GitHub Action.
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
