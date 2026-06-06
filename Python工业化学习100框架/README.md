# Python 工业化学习 100 天

这是一个面向 AI Builder、数据分析、Quant、LLM 和 Agent 作品的开源 Python 100 天学习路径。

课程设计原则：零基础起步、难度逐步承接、每天都有可运行代码、每个阶段都能沉淀成可验证能力。

从 Day10 开始，课程不按“定义 -> 语法 -> 例题”展开，而按“真实任务 -> 场景 -> 为什么存在 -> 怎么解决 -> 语法实现”展开。

完整成长路线图见：[../GROWTH_ROADMAP.md](../GROWTH_ROADMAP.md)。
课程设计原则见：[../COURSE_DESIGN_PRINCIPLES.md](../COURSE_DESIGN_PRINCIPLES.md)。
工业化挑战 能力验证见：[../工业化挑战](../工业化挑战/README.md)。

## 当前推荐学习方式

如果你已经学到 Day10 左右，后面不要急着跳大工程。

Day 主线每天最多 4 小时。

更推荐按 2 小时左右完成。

超过 4 小时的内容，不应该继续塞在当天 Day 里。

处理规则：

- 大型工程任务移到 IC。
- 大型工程验证和作品沉淀移到 IC。
- 作品整理移到 IC。
- Day 只保留知识、原理、API、小型示例和 Debug。

先把这四件事练稳：

```text
路径
函数
数据
复盘
```

从 Day11 开始，每天至少留下：

```text
main.py
notes.md
errors.md
```

每个新知识点都要问：

```text
它解决什么问题？
输入是什么？
输出是什么？
能不能写成函数？
能迁移到数据分析、Quant、LLM 或 Agent 的哪个场景？
```

从 Day11 开始，每次第一次遇到新库、新函数或新 API，先看认知地图，再看代码。

固定顺序是：

```text
这个库是干什么的
  ↓
库里的核心工具有哪些
  ↓
每个工具的输入 -> 输出
  ↓
它和前一天旧知识的连接
  ↓
是什么
  ↓
为什么存在
  ↓
不用它会怎样
  ↓
最小语法
  ↓
逐参数拆解
  ↓
最小代码
```

例如 Day11 的 `csv.DictWriter(...)`，不能直接背。

要先知道 `csv` 是工具箱，`DictWriter` 是“把 dict 写成 CSV 的工具”，`f` 是文件对象，`fieldnames` 是表头字段，返回的 `writer` 才能继续 `writeheader()` 和 `writerows()`。

## Day 和 IC 的职责边界

Day01-Day100 不减少。

已有内容不删除。

但当前课程使用时，Day 只承担知识主线：

```text
What -> Why -> How -> Common Errors -> Future Usage
```

Day 主线不保留完整工程；完整工程实践统一进入 IC。

真正的能力验证、工程任务、GitHub 提交和作品沉淀，统一进入 [工业化挑战](../工业化挑战/README.md)。IC 项目之间是平级作品方向。

IC01-IC74 不占 Day 数。

每个 IC 包含：

- 5 个知识自测问题。
- 1 个工程挑战。
- GitHub 提交要求。
- Challenge Review。

库学习是 Day 主线的重要基础。遇到 `csv`、`json`、`pandas`、`numpy`、`sklearn`、`torch`、`transformers`、`pydantic` 等库时，先看 [库学习地图](../LIBRARY_LEARNING_MAP.md)，再进入代码。

LLM 和 Agent 需要的基础不是一上来写复杂系统，而是先理解：数据结构、API、向量、Embedding、Transformer、PyTorch Tensor、模型输入输出、结构化校验、日志和可观测性。

统计/数学直觉要保留。比如假设检验、吸附壁/阈值、示性函数，都可以翻译成 Python 里的判断条件、权重函数、风险边界和工具路由。

## 阶段路线

### 阶段一：Python 零基础与问题解决起步
- [Day01 - Python 环境与第一段程序](001-Python环境与第一段程序.md)
- [Day02 - 变量、类型与输入输出](002-变量、类型与输入输出.md)
- [Day03 - 分支结构与输入验证](003-分支结构与输入验证.md)
- [Day04 - 循环、计数器与重复任务](004-循环、计数器与重复任务.md)
- [Day05 - 列表与最小算法](005-列表与最小算法.md)
- [Day06 - 函数、参数与返回值](006-函数、参数与返回值.md)
- [Day07 - 字符串、字典与集合](007-字符串、字典与集合.md)
- [Day08 - 文件读写与异常处理](008-文件读写与异常处理.md)
- [Day09 - 模块、包与可复用脚本](009-模块、包与可复用脚本.md)
- [Day10 - 学习记录 CLI 基础](010-学习记录CLI基础.md)

### 阶段二：Python 工程化基本功
- [Day11 - CSV 基础 reader / writer](011-CSV基础readerwriter.md)
- [Day12 - CSV 进阶 DictReader / DictWriter](012-CSV进阶DictReaderDictWriter.md)
- [Day13 - 列表推导式、迭代器与生成器](013-列表推导式、迭代器与生成器.md)
- [Day14 - 日期时间与时间序列意识](014-日期时间与时间序列意识.md)
- [Day15 - 面向对象与 dataclass](015-面向对象与dataclass.md)
- [Day16 - argparse 与命令行参数](016-argparse与命令行参数.md)
- [Day17 - logging 与 Debug 记录](017-logging与Debug记录.md)
- [Day18 - pytest 与最小测试](018-pytest与最小测试.md)
- [Day19 - 类型标注、配置与输入边界](019-类型标注、配置与输入边界.md)
- [Day20 - CLI、日志与测试整合](020-CLI日志与测试整合.md)

### 阶段三：数据分析与本地数据系统
- [Day21 - 目录结构、说明文档 与 Git 基础](021-工程骨架、README与Git工作流.md)
- [Day22 - 虚拟环境与 requirements](022-虚拟环境与requirements.md)
- [Day23 - pandas 读取与数据体检](023-pandas读取与数据体检.md)
- [Day24 - 缺失值、类型转换与清洗](024-缺失值、类型转换与清洗.md)
- [Day25 - 分组聚合与业务指标](025-分组聚合与业务指标.md)
- [Day26 - 表连接、映射与维表](026-表连接、映射与维表.md)
- [Day27 - 时间序列、滚动窗口与移动平均](027-时间序列、滚动窗口与移动平均.md)
- [Day28 - NumPy 数组与向量化计算](028-NumPy数组与向量化计算.md)
- [Day29 - 统计指标、样本量与置信思维](029-统计指标、样本量与置信思维.md)
- [Day30 - 可视化与 Markdown 报告](030-可视化与Markdown报告.md)
- [Day31 - SQLite 本地数据库](031-SQLite本地数据库.md)
- [Day32 - SQL 查询、Join 与窗口意识](032-SQL查询、Join与窗口意识.md)
- [Day33 - 配置文件与环境变量](033-配置文件与环境变量.md)
- [Day34 - 数据校验与错误报告](034-数据校验与错误报告.md)
- [Day35 - 本地指标管道原理](035-本地指标管道原理.md)

### 阶段四：应用接口、自动化与交付
- [Day36 - 自动化文件整理与批处理](036-自动化文件整理与批处理.md)
- [Day37 - HTTP、API 与 JSON 数据获取](037-HTTP、API与JSON数据获取.md)
- [Day38 - 可重试 Data Client 与失败处理](038-可重试DataClient与失败处理.md)
- [Day39 - FastAPI 最小服务](039-FastAPI最小服务.md)
- [Day40 - Streamlit 数据看板](040-Streamlit数据看板.md)
- [Day41 - Docker 轻量运行说明](041-Docker轻量运行说明.md)
- [Day42 - 本地记录 Actions 最小 CI](042-GitHubActions最小CI.md)
- [Day43 - 模块打包与 src 布局](043-模块打包与src布局.md)
- [Day44 - 开源 说明文档、示例与文档](044-开源README、示例与文档.md)
- [Day45 - CLI、API、页面与 CI 整合原理](045-应用交付边界原理.md)

### 阶段五：LLM / RAG / Agent 基础
- [Day46 - Prompt 模板与事实边界](046-Prompt模板与事实边界.md)
- [Day47 - 结构化输出与 Schema 校验](047-结构化输出与Schema校验.md)
- [Day48 - LLM 评估集与评分标准](048-LLM评估集与评分标准.md)
- [Day49 - Embedding 与余弦相似度](049-Embedding与余弦相似度.md)
- [Day50 - 本地笔记检索器](050-本地笔记检索器.md)
- [Day51 - RAG 上下文打包与引用](051-RAG上下文打包与引用.md)
- [Day52 - 隐私脱敏与安全边界](052-隐私脱敏与安全边界.md)
- [Day53 - 缓存、成本与延迟控制](053-缓存、成本与延迟控制.md)
- [Day54 - Agent Tool 输入输出契约](054-AgentTool输入输出契约.md)
- [Day55 - 工具路由与参数选择](055-工具路由与参数选择.md)
- [Day56 - Agent 计划-执行-观察循环](056-Agent计划-执行-观察循环.md)
- [Day57 - Human-in-the-Loop 审查点](057-Human-in-the-Loop审查点.md)
- [Day58 - Agent 日志与可观测性](058-Agent日志与可观测性.md)
- [Day59 - LLM 结构化报告基础](059-LLM结构化报告基础.md)
- [Day60 - LLM Agent 本地知识助手原理](060-LLMAgent本地知识助手原理.md)

### 阶段六：Quant 研究与回测基础
- [Day61 - 行情数据适配器](061-行情数据适配器.md)
- [Day62 - 收益率、波动率与最大回撤](062-收益率、波动率与最大回撤.md)
- [Day63 - 交易信号与未来函数防护](063-交易信号与未来函数防护.md)
- [Day64 - 最小回测引擎](064-最小回测引擎.md)
- [Day65 - 手续费、滑点与现实约束](065-手续费、滑点与现实约束.md)
- [Day66 - 仓位管理与风险预算](066-仓位管理与风险预算.md)
- [Day67 - 组合指标与多资产权重](067-组合指标与多资产权重.md)
- [Day68 - 因子分析最小框架](068-因子分析最小框架.md)
- [Day69 - 事件研究 Event Study](069-事件研究EventStudy.md)
- [Day70 - Quant 报告与图表输出](070-Quant报告与图表输出.md)
- [Day71 - 配置驱动的策略实验](071-配置驱动的策略实验.md)
- [Day72 - 量化函数测试与样例数据](072-量化函数测试与样例数据.md)
- [Day73 - SQLite 保存回测结果](073-SQLite保存回测结果.md)
- [Day74 - Streamlit 策略看板](074-Streamlit策略看板.md)
- [Day75 - Quant 研究闭环原理](075-Quant研究闭环原理.md)

### 阶段七：知识整合、复盘与长期维护
- [Day76 - Quant 研究模块边界](076-Quant研究模块边界.md)
- [Day77 - Quant 数据层原理](077-Quant数据层原理.md)
- [Day78 - Quant 指标与回测层原理](078-Quant指标与回测层原理.md)
- [Day79 - Quant 报告、测试与 CLI 原理](079-Quant报告、测试与CLI原理.md)
- [Day80 - Quant 实验复盘方法](080-Quant实验复盘方法.md)
- [Day81 - LLM 报告助手模块边界](081-LLM报告助手模块边界.md)
- [Day82 - LLM 上下文打包与 Prompt](082-LLM上下文打包与Prompt.md)
- [Day83 - 结构化解析与审查规则](083-结构化解析与审查规则.md)
- [Day84 - LLM 评估集与样例报告](084-LLM评估集与样例报告.md)
- [Day85 - LLM 输出限制与公开说明](085-LLM输出限制与公开说明.md)
- [Day86 - Agent Tool 模块边界](086-AgentTool模块边界.md)
- [Day87 - Agent 工具 Schema 与校验](087-Agent工具Schema与校验.md)
- [Day88 - Agent 执行、错误恢复与日志](088-Agent执行、错误恢复与日志.md)
- [Day89 - Agent 状态存储与人工审查](089-Agent状态存储与人工审查.md)
- [Day90 - Agent 工作流端到端原理](090-Agent工作流端到端原理.md)
- [Day91 - RAG 模块边界](091-RAG模块边界.md)
- [Day92 - RAG 索引与检索层](092-RAG索引与检索层.md)
- [Day93 - RAG 回答 Prompt 与来源引用](093-RAG回答Prompt与来源引用.md)
- [Day94 - RAG 评估与错误案例](094-RAG评估与错误案例.md)
- [Day95 - RAG 限制、复盘与公开说明](095-RAG限制、复盘与公开说明.md)
- [Day96 - GitHub Pages 与课程网站维护](096-GitHubPages与课程网站维护.md)
- [Day97 - 知识索引与能力清单](097-知识索引与能力清单.md)
- [Day98 - 技术讲解脚本与面试表达](098-技术讲解脚本与面试表达.md)
- [Day99 - 错误库、片段库与长期维护](099-错误库、片段库与长期维护.md)
- [Day100 - AI Builder Python Roadmap 总复盘](100-AIBuilderPythonRoadmap总复盘.md)

## 使用方式

- 每天按 2 小时节奏学习，最多不超过 4 小时。
- 先跑通最小案例，再做 7 道简单路线题和 5 道基础巩固题；Day06-Day20 先读「完全看不懂版」和「基础知识深讲」。
- Day 学知识，IC 验能力；不要在 Day 主线里硬塞大型工程任务。
- Day10-Day100 增加工程问题解决结构，优先理解真实任务、场景、设计原因和未来使用位置。
- Day11 之后所有新库/API 默认先给认知地图和输入输出表，禁止直接抛复杂代码。
- IC01-IC74 负责知识自测、工程挑战、GitHub 提交和作品沉淀。
- 所有示例使用虚拟样例，保持可复现、可公开、可长期维护。
- 学完一个阶段，至少整理一次 notes 或阶段复盘；完整作品整理放到 IC。
