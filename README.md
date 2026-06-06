# AI Builder Python100

一个面向 AI Builder、数据分析、Quant、LLM 和 Agent 项目的开源 Python 100 天学习路径。

目标不是堆语法，也不是承诺某几个预设项目一定有用。

更真实的目标是：训练学习者如何把一个模糊想法，拆成输入、输出、最小版本、边界处理、调试、交付和复盘。

课程从 Day10 开始采用“工程问题解决路线”：先看真实任务和场景，再解释为什么需要这个知识点，最后才进入语法实现。

## 在线阅读

- GitHub Pages: 仓库启用 Pages 后可直接在线阅读课程网页。
- 成长路线图：[GROWTH_ROADMAP.md](GROWTH_ROADMAP.md)
- 课程地图：[COURSE_MAP.md](COURSE_MAP.md)
- 课程设计原则：[COURSE_DESIGN_PRINCIPLES.md](COURSE_DESIGN_PRINCIPLES.md)
- 项目过程与聊天式风格：[PROJECT_PROCESS_STYLE_GUIDE.md](PROJECT_PROCESS_STYLE_GUIDE.md)
- Python100 能力达标标准：[PYTHON100_ABILITY_RUBRIC.md](PYTHON100_ABILITY_RUBRIC.md)
- 后续学习路径优化：[PERSONALIZED_LEARNING_PATH.md](PERSONALIZED_LEARNING_PATH.md)
- 知识广度索引：[KNOWLEDGE_EXPANSION_INDEX.md](KNOWLEDGE_EXPANSION_INDEX.md)
- 库学习地图：[LIBRARY_LEARNING_MAP.md](LIBRARY_LEARNING_MAP.md)
- Industrial Challenge 能力验证：[Industrial-Challenge](Industrial-Challenge/README.md)
- 手机入口：[MOBILE.md](MOBILE.md)
- 100 天课程目录：[Python工业化学习100框架](Python工业化学习100框架/README.md)

## 适合谁

- Python 零基础或基础不稳，希望按知识主线 + IC 验证学习的人。
- 统计、金融、数据分析背景，想进入 AI / Quant / Agent 工程实践的人。
- 想用 GitHub 公开沉淀学习过程和 IC 作品集的人。

## 课程结构

1. Day01-Day09：Python 零基础与语法地基
2. Day10：第一个工程问题闭环，学习记录 CLI
3. Day11-Day20：Python 工程化基本功
4. Day21-Day35：数据分析与本地数据系统
5. Day36-Day45：应用接口、自动化与交付
6. Day46-Day60：LLM / RAG / Agent 基础
7. Day61-Day75：Quant 研究与回测基础
8. Day76-Day100：知识整合、复盘与长期维护

## Day 和 IC 的边界

Day01-Day100 保留，不减少。

当前主线解释为：

- Day：知识学习、原理理解、API 使用、小型示例、Debug 能力。
- IC：能力验证、工程挑战、GitHub 提交、作品集沉淀。

Day 的统一学习模板是：

```text
What
Why
How
Common Errors
Future Usage
```

Agent / LLM / Quant 的通识知识继续保留在 Day100 主线里，例如 Tool、Memory、Workflow、Planning、Prompt、Context、Embedding、RAG 原理、Return、Volatility、Sharpe、Drawdown 和 Backtest 原理。

课程基础部分会持续强调“库的学习”：遇到 `csv`、`json`、`pandas`、`numpy`、`sklearn`、`torch`、`transformers`、`pydantic` 等库时，先建立认知地图，再拆函数和参数。机器学习、深度学习、Transformer 和 PyTorch 作为 LLM / Agent 的基础知识进入 Day 主线，但只讲概念、输入输出和最小示例，不提前做完整大模型项目。

完整 RAG 系统、Agent 系统、Quant 回测框架、多 Agent 协作和 Dashboard 项目，统一放到 [Industrial Challenge](Industrial-Challenge/README.md) 做能力验证。

## 新学习风格

后续内容会逐步改成更接近 GPT 对话的学习体验：

- 单段更短。
- 每次只讲一个小问题。
- 总体内容不减少。
- 项目名降级为例子。
- 重点放在“如何做项目的过程”。

也就是说，不是让你相信某个项目一定有用，而是让你掌握做项目时可迁移的判断方法。

## 每天怎么学

Day 主线每天最多按 4 小时设计。

推荐学习量是 2 小时左右。

如果当天内容超过 4 小时，优先砍掉大型工程任务和作品集整理，把它们移动到 IC。

- 15 分钟：读学习定位和知识地图。
- 25 分钟：手打最小案例并运行。
- 35 分钟：完成 7 道简单路线题。
- 35 分钟：完成 5 道基础巩固题。
- 10 分钟：记录 Debug、结果和下一步。

上面是 Day 主线节奏，不包含 IC。

IC 是额外能力验证，不强行塞进同一天。

## 100 天后能到什么水平

如果你已经学完前 10 天，并且有统计、金融或数据背景，学完这 100 天后可以形成比较强的 Python 实战能力。具体达标口径见 [Python100 能力达标标准](PYTHON100_ABILITY_RUBRIC.md)。

这里的“比较强”不是指背完所有语法，而是指你能独立完成这些事：

- 用 Python 处理 CSV、JSON、SQLite 和基础 API 数据。
- 把一个模糊任务拆成输入、输出、函数、测试、日志和 README。
- 写出能复现、能解释、能交付的小工具。
- 用 pandas、SQL、Streamlit、FastAPI 做轻量数据应用。
- 看懂机器学习、深度学习、Transformer 和 PyTorch 的基础库地图。
- 理解 Prompt、Context、Embedding、RAG、Tool、Memory 和 Workflow 的基本原理。
- 理解 Return、Volatility、Sharpe、Drawdown 和 Backtest 的基本工程边界。

前提是每天要手打代码、跑通结果，并写下复盘。只读完文本不会自动变强。

## IC 能力验证线

Day01-Day100 不承担大型工程交付职责。

IC01-IC50 用来验证工程能力：

- 每个 IC 有 5 个知识自测问题。
- 每个 IC 有 1 个工程挑战。
- 每个 IC 要留下运行结果、Debug 记录和 GitHub 提交。
- IC 最终沉淀为 4 个作品集项目：数据分析、Quant、LLM、Agent。

## 开源说明

本仓库是公开学习资源。示例代码和示例数据使用虚拟样例，公开内容只保留课程、练习、项目和精选学习资产。

本地 Obsidian Vault 可以记录更真实的 Debug、学习日志和认知变化；公开 GitHub 仓库只保留适合外部阅读的课程、练习、项目和精选学习资产。

## License

MIT License. See [LICENSE](LICENSE).
