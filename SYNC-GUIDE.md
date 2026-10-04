# 上游同步指南

本文档记录**如何把上游 [avelino/awesome-go](https://github.com/avelino/awesome-go) 的更新同步到这个汉化仓库**。

这套流程在 2026-10-04 完整走过一遍（上游 3129 → 3145 条，新增 18 / 删除 2），不是纸上谈兵。

---

## 一、自动监控：什么都不用做

`.github/workflows/sync-check.yml` 每天 **06:30 (UTC+8)** 自动跑一次比对：

| 情况 | 发生什么 |
|:---|:---|
| 上游有差异 | 自动开/更新一个带 `上游同步` 标签的 Issue，标题形如「🔔 awesome-go 上游有更新」 |
| 上游无差异 | 完全静默，并把上次的 Issue 自动关掉 |

**你平时只需要扫一眼仓库的 Issues 列表。** 没 Issue = 上游没变化，不用管。

想立刻检查也可以在 Actions 页���手动点 `Workflow dispatch`。

---

## 二、看到 Issue 后怎么处理

Issue 里已经列好了完整待办清单，但你本地跑一遍更方便：

```bash
cd /root/code/awesome-go-cn
python3 tools/sync_check.py
```

输出分三类：

```
新增_待翻译   上游有、我们没有   → 附「上游英文」原文
变更_待重译   描述被上游改了    → 附「上游英文(新)」+「上游英文(旧)」+「我方现译」三行对照
删除_待处理   上游删了、我们还有 → 附我方现译，你决定删不删
```

---

## 三、同步步骤

### 第 1 步：更新上游 README（**最容易漏，别跳**）

```bash
curl -sL -o /root/code/awesome-go/README.md \
  https://raw.githubusercontent.com/avelino/awesome-go/main/README.md
```

> ⚠️ **必须先做这步。** `build.sh` 默认从 `/root/code/awesome-go/README.md` 读取上游内容。
> 如果它还是旧版本，构建出来的 README 会比同步前**更差**——新增条目一条都进不来，
> 已删除的条目反而会变成英文。
>
> 2026-10-04 就踩过这个坑：第一次构建验收报 `3027/3130`，比同步前的 3029 还少 2 条。

### 第 2 步：翻译新增与变更的条目

把译文写进 `entry_translations.json`，**键是条目的 URL**：

```json
{
  "https://github.com/CreateLab/glinq": "类 LINQ 的惰性求值库，具备类型安全的泛型、性能优化与零依赖。",
  "https://github.com/bytecodealliance/wasmtime-go": "Wasmtime WebAssembly 运行时的 Go 绑定（支持 WASI、JIT/AOT，嵌入安全且快速）。"
}
```

- `新增` 的条目：新增一个键值对
- `变更` 的条目：把旧译文替换掉
- `删除` 的条目：把整个键值对删掉

**注意**：本文件是译文库，**必须提交到 git**。它是全部翻译成果的唯一载体。

### 第 3 步：更新比对基准快照

```bash
python3 tools/update_snapshot.py
```

**必须在翻译完成之后跑。** `upstream_snapshot.json` 记录的是「我翻译时上游长什么样」，
下次比对时用它作基准。不更新的话，下次还会重复报同一批差异。

> `entry_translations.json`（我的译文）和 `upstream_snapshot.json`（上游原文快照）
> 是**两个不同的文件**，不要混为一谈。前者是我写的，后者是上游的。

### 第 4 步：重新生成 README 并验收

```bash
bash build.sh
```

必须五项全绿才能提交：

```
① 锚点链接        255 个 | 可解析 255 | 断链 0
② 外部链接        3265 个唯一 URL      ← 同步后这个数应该上涨
③ 结构性英文残留  0 行
④ 标题汉化        136/151
   条目描述汉化    3044/3145
⑤ star 写法       18.6 万 ✅
```

**任何一项数字异常，先查清楚再提交。** 特别是：
- 「条目描述汉化」比同步前**变少** → 第 1 步没做，或有译文被误删
- 「外部链接」没上涨 → 新增条目根本没进来
- 「断链」不为 0 → 锚点或 URL 被改坏了

### 第 5 步：复检

```bash
python3 tools/sync_check.py
```

**必须输出「新增 0 / 变更 0 / 删除 0」**。这才叫真正同步完成。

### 第 6 步：提交推送

```bash
git add -A && git commit -m "feat: 与上游同步至 N 条" && git push origin main
```

---

## 四、译名约定（务必保持一致）

| 类型 | 处理方式 | 例子 |
|:---|:---|:---|
| 库名 / 框架名 / API 名 | **保留英文** | Gin、gRPC、MQTT、WebRTC、JWT |
| 技术专名 | **保留英文** | SHA256、SSE、NACl、token bucket |
| 产品/品牌名 | **保留英文** | Shopify、GitHub、Cocos2d |
| 项目本身的玩笑名 | **保留英文** | `Go HTTP Requests for Humans™` |
| 分类标题 / 描述 | **译成中文** | 「Audio and Music」→「音频与音乐」 |
| 条目内嵌的 Markdown 链接 | **原样保留，一个字都不动** | `([RFC 8628](https://...))` |

最后一条尤其重要：链接由程序搬运，手工编辑极易破坏，验收会直接报断链。

---

## 五、文件职责

| 文件 | 作用 | 是否入库 |
|:---|:---|:---|
| `entry_translations.json` | **译文库**，全部翻译成果的载体 | ✅ 必须 |
| `upstream_snapshot.json` | 翻译当时的上游状态，下次比对的基准 | ✅ 必须 |
| `README.md` | `build.sh` 生成，勿手工编辑 | ✅ |
| `tools/parse.py` | 解析/回装，含往返一致性校验 | ✅ |
| `tools/sync_check.py` | 上游差异比对 | ✅ |
| `tools/update_snapshot.py` | 更新比对基准 | ✅ |
| `tools/verify.py` | 五项硬验收 | ✅ |
| `blocks.json` | 解析中间产物 | ❌ 每次重建 |
| `batch_*.json` | 翻译批次的临时草稿 | ❌ 每次重建 |

---

## 六、已知坑位

1. **构建前不更新上游 README** → 见第 1 步。会导致「同步后反而变少」。

2. **`apply` 会跳过已存在的 URL。** 译文库按 URL 去重，已经有译文时再 `apply`
   同一批不会覆盖。若要修正某条已入库的译文，**直接改 `entry_translations.json`**。

3. **批次草稿会残留。** 合并前务必清掉不属于当前批次的 `batch_tr_*.json`，
   否则索引越界会报错，或把上一批的译文混进来。

4. **批次索引必须是整数。** 合并脚本里 JSON 读出来的键是字符串，
   用整数 `i` 去索引会全部判定为「缺译」。统一用 `int(k)` 转换。

5. **上游本身可能有重复条目。** `upstream_snapshot.json` 按 URL 去重，
   所以「条目数」和「唯一 URL 数」可能差 1~2，这是上游的问题，不是漏译。

---

## 七、自检清单

提交前逐条确认：

- [ ] 上游 README 已更新（第 1 步）
- [ ] 新增条目全部翻译，`变更` 条目全部替换，`删除` 条目已清理
- [ ] `upstream_snapshot.json` 已更新（第 3 步）
- [ ] `bash build.sh` 五项验收全绿
- [ ] 「条目描述汉化」数字**不低于**同步前
- [ ] 「外部链接」数字**有上涨**（有新增条目时）
- [ ] `sync_check.py` 复检输出 **0 / 0 / 0**
- [ ] `entry_translations.json` 已提交