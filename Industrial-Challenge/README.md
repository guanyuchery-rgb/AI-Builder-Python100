# Industrial Challenge（IC01-IC50）

IC 是 Python100 的能力验证体系，不占 Day 数。

Day01-Day100 只负责知识学习：

```text
What -> Why -> How -> Common Errors -> Future Usage
```

IC01-IC50 负责验证你是否真的会用这些知识。

IC 不挤占 Day 的 4 小时上限。

如果当天 Day 主线已经接近 4 小时，IC 顺延到下一次学习。

每个 IC 固定三部分：

- Part A：5 个知识自测问题，检查 What、Why、How、Common Errors 和 Future Usage。
- Part B：一个工程挑战，只使用最近 Day 学到的知识。
- Part C：Challenge Review，记录学到什么、遇到什么错误、如何 Debug、如何改进。

## Day 和 IC 的边界

- Day：知识、原理、API、小型示例、Debug 方法。
- IC：工程挑战、GitHub 提交、作品集沉淀。

Day 主线不保留完整项目。旧 Day76-Day95 的项目化材料已迁移到 `Migrated-Day-Project-Material/`，真正的项目交付统一放到 IC。

## 最终沉淀

- Project01：数据分析作品（SQL + Pandas）
- Project02：Quant 作品（Factor + Backtest）
- Project03：LLM 作品（RAG 系统）
- Project04：Agent 作品（Multi-Agent Workflow）

每个最终项目必须有：GitHub 仓库、README、项目截图、运行说明、简历描述。

## IC 索引

- [IC01 - Study Log Blueprint｜学习日志蓝图](IC01-Study-Log-Blueprint.md)：Day01-Day02，变量、类型与输入输出，Project01 数据分析基础
- [IC02 - Rhythm Classifier｜学习节奏分类器](IC02-Rhythm-Classifier.md)：Day03-Day04，分支、循环与输入验证，Project01 数据分析基础
- [IC03 - Function Lab｜函数处理实验室](IC03-Function-Lab.md)：Day05-Day06，列表、函数与返回值，Project01 数据分析基础
- [IC04 - File Journal Seed｜文件日志种子](IC04-File-Journal-Seed.md)：Day07-Day08，字典、集合、文件读写，Project01 数据分析基础
- [IC05 - Command Line Notebook｜命令行学习本](IC05-Command-Line-Notebook.md)：Day09-Day10，模块、包与学习记录 CLI，Project01 数据分析基础
- [IC06 - Structured Log Gate｜结构化日志入口](IC06-Structured-Log-Gate.md)：Day11-Day12，CSV、JSON、正则解析，Project01 数据分析基础
- [IC07 - Time Lens Analyzer｜时间视角分析器](IC07-Time-Lens-Analyzer.md)：Day13-Day14，推导式、迭代器、datetime，Project01 数据分析基础
- [IC08 - CLI Control Desk｜命令行控制台](IC08-CLI-Control-Desk.md)：Day15-Day16，dataclass、argparse，Project01 数据分析基础
- [IC09 - Debug Evidence Box｜Debug 证据盒](IC09-Debug-Evidence-Box.md)：Day17-Day18，logging、pytest，Project01 数据分析基础
- [IC10 - Learning Ops Console｜学习管理控制台](IC10-Learning-Ops-Console.md)：Day19-Day20，类型标注、配置、Data CLI，Project01 数据分析基础
- [IC11 - Reproducible Workspace｜可复现工作台](IC11-Reproducible-Workspace.md)：Day21-Day22，项目骨架、requirements，Project01 数据分析基础
- [IC12 - Data Health Scanner｜数据体检扫描器](IC12-Data-Health-Scanner.md)：Day23-Day24，pandas读取、缺失值清洗，Project01 数据分析基础
- [IC13 - Metric Workshop｜指标工坊](IC13-Metric-Workshop.md)：Day25-Day26，分组聚合、表连接，Project01 数据分析基础
- [IC14 - Time Series Sandbox｜时间序列沙盒](IC14-Time-Series-Sandbox.md)：Day27-Day28，时间序列、NumPy，Project01 数据分析基础
- [IC15 - Stat Report Room｜统计报告室](IC15-Stat-Report-Room.md)：Day29-Day30，统计指标、Markdown报告，Project01 数据分析基础
- [IC16 - SQLite Memory Base｜SQLite 记忆库](IC16-SQLite-Memory-Base.md)：Day31-Day32，SQLite、SQL Join，Project01 数据分析基础
- [IC17 - Data Quality Gate｜数据质量闸门](IC17-Data-Quality-Gate.md)：Day33-Day34，配置、数据校验，Project01 数据分析基础
- [IC18 - Local Pipeline Starter｜本地管道起点](IC18-Local-Pipeline-Starter.md)：Day35-Day36，数据管道、文件批处理，Project01 数据分析基础
- [IC19 - API Harvest Kit｜API 采集套件](IC19-API-Harvest-Kit.md)：Day37-Day38，HTTP、API、重试，Project01 数据分析基础
- [IC20 - Data Insight Board｜数据洞察看板](IC20-Data-Insight-Board.md)：Day39-Day40，FastAPI、Streamlit，Project01 数据分析项目
- [IC21 - Delivery Runbook｜交付运行手册](IC21-Delivery-Runbook.md)：Day41-Day42，Docker轻量、GitHub Actions，Project01 数据分析项目
- [IC22 - Repo Review Studio｜仓库审查室](IC22-Repo-Review-Studio.md)：Day43-Day44，src布局、开源README，Project01 数据分析项目
- [IC23 - Prompt Boundary Lab｜Prompt 边界实验室](IC23-Prompt-Boundary-Lab.md)：Day45-Day46，Data Tool、Prompt模板，Project03 LLM 基础
- [IC24 - Structured Output Bench｜结构化输出评测台](IC24-Structured-Output-Bench.md)：Day47-Day48，Schema、LLM评估，Project03 LLM 基础
- [IC25 - Semantic Search Seed｜语义检索种子](IC25-Semantic-Search-Seed.md)：Day49-Day50，Embedding、相似度，Project03 LLM 基础
- [IC26 - Context Privacy Pack｜上下文隐私包](IC26-Context-Privacy-Pack.md)：Day51-Day52，RAG上下文、隐私边界，Project03 LLM 基础
- [IC27 - Tool Contract Forge｜工具契约锻造台](IC27-Tool-Contract-Forge.md)：Day53-Day54，缓存、Tool契约，Project04 Agent 基础
- [IC28 - Router Playground｜工具路由游乐场](IC28-Router-Playground.md)：Day55-Day56，工具路由、计划执行观察，Project04 Agent 基础
- [IC29 - Agent Trace Inspector｜Agent 轨迹检查器](IC29-Agent-Trace-Inspector.md)：Day57-Day58，人工审查、可观测性，Project04 Agent 基础
- [IC30 - Knowledge Assistant Trial｜知识助手试炼](IC30-Knowledge-Assistant-Trial.md)：Day59-Day60，LLM/Agent Capstone原理，Project03 LLM 项目
- [IC31 - Return Volatility Lab｜收益波动实验室](IC31-Return-Volatility-Lab.md)：Day61-Day62，行情适配器、收益波动，Project02 Quant 基础
- [IC32 - Lookahead Defense Gate｜未来函数防线](IC32-Lookahead-Defense-Gate.md)：Day63-Day64，信号、回测原理，Project02 Quant 基础
- [IC33 - Risk Budget Desk｜风险预算台](IC33-Risk-Budget-Desk.md)：Day65-Day66，手续费、仓位风险，Project02 Quant 基础
- [IC34 - Factor Lens｜因子观察镜](IC34-Factor-Lens.md)：Day67-Day68，组合权重、因子分析，Project02 Quant 基础
- [IC35 - Event Study Notebook｜事件研究本](IC35-Event-Study-Notebook.md)：Day69-Day70，事件研究、图表报告，Project02 Quant 基础
- [IC36 - Strategy Config Lab｜策略配置实验室](IC36-Strategy-Config-Lab.md)：Day71-Day72，配置实验、函数测试，Project02 Quant 项目
- [IC37 - Backtest Result Vault｜回测结果库](IC37-Backtest-Result-Vault.md)：Day73-Day74，SQLite回测结果、看板，Project02 Quant 项目
- [IC38 - Quant Workspace Seed｜Quant 工作台种子](IC38-Quant-Workspace-Seed.md)：Day75-Day76，Quant Starter骨架，Project02 Quant 项目
- [IC39 - Quant Metrics Engine｜Quant 指标引擎](IC39-Quant-Metrics-Engine.md)：Day77-Day78，数据层、指标回测层，Project02 Quant 项目
- [IC40 - Quant Delivery Room｜Quant 交付室](IC40-Quant-Delivery-Room.md)：Day79-Day80，报告、测试、README，Project02 Quant 项目
- [IC41 - LLM Report Desk｜LLM 报告台](IC41-LLM-Report-Desk.md)：Day81-Day82，LLM报告助手、上下文打包，Project03 LLM 项目
- [IC42 - LLM Error Review｜LLM 错误审查室](IC42-LLM-Error-Review.md)：Day83-Day84，结构化解析、评估集，Project03 LLM 项目
- [IC43 - Agent Tool Studio｜Agent 工具工作室](IC43-Agent-Tool-Studio.md)：Day85-Day86，LLM交付、Agent骨架，Project04 Agent 项目
- [IC44 - Tool Executor Bench｜工具执行台](IC44-Tool-Executor-Bench.md)：Day87-Day88，工具Schema、错误恢复，Project04 Agent 项目
- [IC45 - Agent Workflow Stage｜Agent 工作流舞台](IC45-Agent-Workflow-Stage.md)：Day89-Day90，状态存储、端到端演示，Project04 Agent 项目
- [IC46 - RAG Index Foundry｜RAG 索引工坊](IC46-RAG-Index-Foundry.md)：Day91-Day92，RAG骨架、索引检索，Project03 LLM 项目
- [IC47 - RAG Answer Bench｜RAG 回答评测台](IC47-RAG-Answer-Bench.md)：Day93-Day94，引用回答、RAG评估，Project03 LLM 项目
- [IC48 - Portfolio Release Gate｜作品集发布闸门](IC48-Portfolio-Release-Gate.md)：Day95-Day96，RAG交付、Pages维护，Project03/04 交付
- [IC49 - Project Story Studio｜项目叙事工作室](IC49-Project-Story-Studio.md)：Day97-Day98，作品集README、面试故事，作品集
- [IC50 - AI Builder Final Board｜AI Builder 总验收板](IC50-AI-Builder-Final-Board.md)：Day99-Day100，错误库、总Capstone，作品集

## 使用节奏

每 2 个 Day 做 1 个 IC。先完成 Day 主线，再进入 IC。IC 没完成，不影响继续学 Day，但会影响作品集沉淀。

## 迁移说明

Day76-Day95 旧版项目化材料已经移动到 [Migrated-Day-Project-Material](Migrated-Day-Project-Material/)。Day 主线只保留知识学习；完整工程实践在 IC38-IC50 中完成。
