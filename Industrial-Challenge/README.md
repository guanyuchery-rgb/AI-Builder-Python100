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

- Part A：5 道 LeetCode，总计 250 道，不重复，使用官方题目链接。
- Part B：一个工程挑战，只使用最近 Day 学到的知识。
- Part C：Challenge Review，记录学到什么、遇到什么错误、如何 Debug、如何改进。

## Day 和 IC 的边界

- Day：知识、原理、API、小型示例、Debug 方法。
- IC：刷题记录、工程挑战、GitHub 提交、作品集沉淀。

已有 Day 内容不删除；如果某个 Day 里出现项目名，把它视为知识场景或旧版训练说明。真正的项目交付统一放到 IC。

## 最终沉淀

- Project01：数据分析项目（SQL + Pandas）
- Project02：Quant 项目（Factor + Backtest）
- Project03：LLM 项目（RAG 系统）
- Project04：Agent 项目（Multi-Agent Workflow）

每个最终项目必须有：GitHub 仓库、README、项目截图、运行说明、简历描述。

## IC 索引

- [IC01 - 学习日志字段设计](IC01.md)：Day01-Day02，变量、类型与输入输出，Project01 数据分析基础
- [IC02 - 学习时间分类器](IC02.md)：Day03-Day04，分支、循环与输入验证，Project01 数据分析基础
- [IC03 - 函数化学习记录处理器](IC03.md)：Day05-Day06，列表、函数与返回值，Project01 数据分析基础
- [IC04 - CSV 前置：手工文件日志](IC04.md)：Day07-Day08，字典、集合、文件读写，Project01 数据分析基础
- [IC05 - Todo / Learning CLI v0](IC05.md)：Day09-Day10，模块、包与学习记录 CLI，Project01 数据分析基础
- [IC06 - 结构化日志导入器](IC06.md)：Day11-Day12，CSV、JSON、正则解析，Project01 数据分析基础
- [IC07 - 日期化学习记录分析器](IC07.md)：Day13-Day14，推导式、迭代器、datetime，Project01 数据分析基础
- [IC08 - 命令行记录管理器](IC08.md)：Day15-Day16，dataclass、argparse，Project01 数据分析基础
- [IC09 - Debug 与测试样例库](IC09.md)：Day17-Day18，logging、pytest，Project01 数据分析基础
- [IC10 - 学习管理 CLI v1](IC10.md)：Day19-Day20，类型标注、配置、Data CLI，Project01 数据分析基础
- [IC11 - 可复现数据项目骨架](IC11.md)：Day21-Day22，项目骨架、requirements，Project01 数据分析基础
- [IC12 - 表格数据体检器](IC12.md)：Day23-Day24，pandas读取、缺失值清洗，Project01 数据分析基础
- [IC13 - 学习指标分析器](IC13.md)：Day25-Day26，分组聚合、表连接，Project01 数据分析基础
- [IC14 - 时间序列指标实验](IC14.md)：Day27-Day28，时间序列、NumPy，Project01 数据分析基础
- [IC15 - 统计报告生成器](IC15.md)：Day29-Day30，统计指标、Markdown报告，Project01 数据分析基础
- [IC16 - SQLite 学习管理器](IC16.md)：Day31-Day32，SQLite、SQL Join，Project01 数据分析基础
- [IC17 - 数据质量检查器](IC17.md)：Day33-Day34，配置、数据校验，Project01 数据分析基础
- [IC18 - 本地数据管道 v1](IC18.md)：Day35-Day36，数据管道、文件批处理，Project01 数据分析基础
- [IC19 - API 数据采集器](IC19.md)：Day37-Day38，HTTP、API、重试，Project01 数据分析基础
- [IC20 - 数据分析小看板](IC20.md)：Day39-Day40，FastAPI、Streamlit，Project01 数据分析项目
- [IC21 - 可交付数据工具](IC21.md)：Day41-Day42，Docker轻量、GitHub Actions，Project01 数据分析项目
- [IC22 - 项目结构审查器](IC22.md)：Day43-Day44，src布局、开源README，Project01 数据分析项目
- [IC23 - Prompt 输入边界练习](IC23.md)：Day45-Day46，Data Tool、Prompt模板，Project03 LLM 基础
- [IC24 - 结构化输出评估集](IC24.md)：Day47-Day48，Schema、LLM评估，Project03 LLM 基础
- [IC25 - 本地文本相似度工具](IC25.md)：Day49-Day50，Embedding、相似度，Project03 LLM 基础
- [IC26 - 脱敏上下文打包器](IC26.md)：Day51-Day52，RAG上下文、隐私边界，Project03 LLM 基础
- [IC27 - Agent Tool 输入输出契约](IC27.md)：Day53-Day54，缓存、Tool契约，Project04 Agent 基础
- [IC28 - 工具路由模拟器](IC28.md)：Day55-Day56，工具路由、计划执行观察，Project04 Agent 基础
- [IC29 - Agent 日志审查器](IC29.md)：Day57-Day58，人工审查、可观测性，Project04 Agent 基础
- [IC30 - 本地知识助手最小验证](IC30.md)：Day59-Day60，LLM/Agent Capstone原理，Project03 LLM 项目
- [IC31 - 收益率与波动率实验](IC31.md)：Day61-Day62，行情适配器、收益波动，Project02 Quant 基础
- [IC32 - 未来函数防护检查器](IC32.md)：Day63-Day64，信号、回测原理，Project02 Quant 基础
- [IC33 - 风险预算计算器](IC33.md)：Day65-Day66，手续费、仓位风险，Project02 Quant 基础
- [IC34 - 因子暴露分析器](IC34.md)：Day67-Day68，组合权重、因子分析，Project02 Quant 基础
- [IC35 - 事件研究报告器](IC35.md)：Day69-Day70，事件研究、图表报告，Project02 Quant 基础
- [IC36 - 策略实验配置器](IC36.md)：Day71-Day72，配置实验、函数测试，Project02 Quant 项目
- [IC37 - 回测结果存储与看板](IC37.md)：Day73-Day74，SQLite回测结果、看板，Project02 Quant 项目
- [IC38 - Quant 项目骨架初始化](IC38.md)：Day75-Day76，Quant Starter骨架，Project02 Quant 项目
- [IC39 - Quant 数据与指标层](IC39.md)：Day77-Day78，数据层、指标回测层，Project02 Quant 项目
- [IC40 - Quant 项目交付复盘](IC40.md)：Day79-Day80，报告、测试、README，Project02 Quant 项目
- [IC41 - LLM 报告助手骨架](IC41.md)：Day81-Day82，LLM报告助手、上下文打包，Project03 LLM 项目
- [IC42 - LLM 评估与错误案例](IC42.md)：Day83-Day84，结构化解析、评估集，Project03 LLM 项目
- [IC43 - Agent Tool Prototype骨架](IC43.md)：Day85-Day86，LLM交付、Agent骨架，Project04 Agent 项目
- [IC44 - Agent 工具执行器](IC44.md)：Day87-Day88，工具Schema、错误恢复，Project04 Agent 项目
- [IC45 - Agent 工作流演示](IC45.md)：Day89-Day90，状态存储、端到端演示，Project04 Agent 项目
- [IC46 - RAG 知识库索引器](IC46.md)：Day91-Day92，RAG骨架、索引检索，Project03 LLM 项目
- [IC47 - RAG 回答与评估](IC47.md)：Day93-Day94，引用回答、RAG评估，Project03 LLM 项目
- [IC48 - 作品集发布检查](IC48.md)：Day95-Day96，RAG交付、Pages维护，Project03/04 交付
- [IC49 - 项目讲解脚本](IC49.md)：Day97-Day98，作品集README、面试故事，作品集
- [IC50 - 四项目作品集总验收](IC50.md)：Day99-Day100，错误库、总Capstone，作品集

## 使用节奏

每 2 个 Day 做 1 个 IC。先完成 Day 主线，再进入 IC。IC 没完成，不影响继续学 Day，但会影响作品集沉淀。
