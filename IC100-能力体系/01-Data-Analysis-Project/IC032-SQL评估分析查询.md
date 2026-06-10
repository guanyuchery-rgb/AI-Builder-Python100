# IC032 - SQL评估分析查询

> IC100 Data Analysis Project：LLM Evaluation Analytics Platform。

## 1. 今日定位

用 SQL 回答分析问题：排行榜、失败类型、成本最高任务、低分样本。

- 所属项目：Data Analysis Project。
- 项目方向：LLM Evaluation Analytics Platform。
- 训练目标：统计学背景 + Python 数据分析 + LLM 评估理解 + GitHub 作品集。
- 今日不做：真实 API 调用、复杂前端、完整 LLM 系统。

## 项目总目标

最终做出一个 `LLM Evaluation Analytics Platform`。它不是训练大模型，也不是直接写 Agent 系统，而是先把 LLM 评估结果变成可分析、可复现、可展示的数据产品。

你要训练的能力是：

- 看懂 LLM eval log 的字段。
- 用 Python 清洗 JSONL / CSV。
- 用 pandas / NumPy / SQL 做指标。
- 用统计学解释模型差异。
- 用 Matplotlib / Streamlit 做展示。
- 用 README / 报告 / 截图把项目放到 GitHub。

## 本项目数据模型

核心事实表：`eval_results`。

| 字段 | 含义 | 例子 |
| --- | --- | --- |
| `eval_id` | 单条评估记录 ID | `e0001` |
| `model` | 被评估模型 | `gpt-x` / `local-y` |
| `task_type` | 任务类型 | `qa` / `summary` / `extract` |
| `prompt_version` | prompt 版本 | `v1` / `v2` |
| `score` | 评分，0 到 1 | `0.82` |
| `judge_label` | 评审标签 | `pass` / `partial` / `fail` |
| `latency_ms` | 延迟毫秒 | `1200` |
| `cost_usd` | 单次成本 | `0.003` |
| `error_type` | 错误类型 | `hallucination` / `format_error` |
| `created_at` | 评估时间 | `2026-06-10` |

## 2. 今日知识加厚

### 核心知识：SQL group by / join / where / order by

这一天不只是“做一个任务”，还要补齐项目背后的知识。你要能回答：

- 这个步骤的输入是什么。
- 这个步骤的输出是什么。
- 如果这个步骤做错，后面哪个环节会被污染。
- 这个步骤如何服务最终 dashboard、报告和简历项目。

### 输入 -> 处理 -> 输出

| 部分 | 本日要求 |
| --- | --- |
| 输入 | raw eval logs、上一 IC 产物或手写 toy data |
| 处理 | SQL group by / join / where / order by |
| 输出 | `sql/eval_queries.sql` |

### 为什么这一步存在

LLM 评估不是只看一个总分。真实工作里，你要同时解释质量、成本、延迟、失败类型和样本可靠性。这个 IC 的作用是把其中一个环节做稳，让后面每一步都有干净输入。

## 3. Part A - 工程任务

### A1. 今日任务

写 5 条可复用 SQL，不只在 Python 里 groupby。

### A2. 具体步骤

1. 在项目根目录确认当前文件结构。
2. 新建或更新今天需要的 `data/`、`src/`、`outputs/`、`docs/` 文件。
3. 只实现今天这个小环节，不提前把整个系统写完。
4. 保存一个可复查输出，文件名要稳定。
5. 在 README 或 review 里记录运行命令和错误。

### A3. 最小代码片段

```python
query = "select model, avg(score) as avg_score from eval_results group by model order by avg_score desc"
print(query)
```

这段代码不是最终项目代码，只是今天知识点的最小验证。正式项目里，稳定逻辑应该逐步放进 `src/`，不要长期留在 notebook 或临时代码里。

### A4. 验收标准

- 生成 `sql/eval_queries.sql` 或对应文档。
- 每条 SQL 对应一个业务问题。
- 能说清今天输入、处理、输出。
- 能写出今天最容易出错的 2 个点。
- 有一次 GitHub commit。

### A5. GitHub 提交要求

```text
IC032: SQL评估分析查询
```

提交必须包含：代码或文档、运行结果、Debug 记录、项目复盘。

## Review 模板

```text
IC编号：IC032
主题：SQL评估分析查询
完成日期：

今天完成的工程动作：
今天补上的知识点：
今天遇到的错误：
我是怎么 Debug 的：
产出文件：
GitHub commit：
下次继续做什么：
```

## 5. 求职沉淀

今天完成后，长期作品集里可以沉淀一句话：

> 我在 `LLM Evaluation Analytics Platform` 中完成 `SQL评估分析查询`，能把 LLM 评估日志转化为可复现的数据资产和可解释分析结果。
