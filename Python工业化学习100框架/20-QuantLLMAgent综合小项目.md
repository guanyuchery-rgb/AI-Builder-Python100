# Day20 - Quant / LLM / Agent 综合小项目

学习定位：把前 19 天的 Python 基础连接成一个可进入项目阶段的小工具。完成后，你可以开始做真正的 Quant、LLM、Agent 小项目。

## 2小时安排

- 20 分钟：读项目目标和结构。
- 35 分钟：手打数据模型和核心函数。
- 35 分钟：完成 CSV 输入、JSON 输出。
- 20 分钟：补测试和日志。
- 10 分钟：写下一步项目计划。

## 项目目标

构建一个 `research_summary_cli.py`：

- 读取本地 CSV 中的资产收益率。
- 计算简单统计指标。
- 输出 JSON summary。
- 生成一段可交给 LLM 总结的 prompt。
- 保持函数化、可测试、可扩展。

## 项目结构

```text
day20_research_summary/
├── research_summary_cli.py
├── returns.csv
└── README.md
```

## 核心代码

```python
import csv
import json
import logging
from dataclasses import dataclass
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


@dataclass
class ReturnRecord:
    symbol: str
    return_rate: float


def load_returns(path: Path) -> list[ReturnRecord]:
    records: list[ReturnRecord] = []
    with path.open(encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(
                ReturnRecord(
                    symbol=row["symbol"].strip().upper(),
                    return_rate=float(row["return_rate"]),
                )
            )
    return records


def summarize(records: list[ReturnRecord]) -> dict:
    if not records:
        raise ValueError("records cannot be empty")

    returns = [record.return_rate for record in records]
    best = max(records, key=lambda record: record.return_rate)
    worst = min(records, key=lambda record: record.return_rate)

    return {
        "count": len(records),
        "average_return": sum(returns) / len(returns),
        "best_symbol": best.symbol,
        "best_return": best.return_rate,
        "worst_symbol": worst.symbol,
        "worst_return": worst.return_rate,
    }


def build_llm_prompt(summary: dict) -> str:
    return (
        "请用统计硕士能理解的方式解释以下资产收益率摘要。"
        "请指出表现最好、最差资产，并提醒样本量限制。\\n"
        f"{json.dumps(summary, ensure_ascii=False, indent=2)}"
    )


def main() -> None:
    input_path = Path("returns.csv")
    output_path = Path("summary.json")

    logging.info("loading returns from %s", input_path)
    records = load_returns(input_path)
    summary = summarize(records)

    output_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(build_llm_prompt(summary))
    logging.info("summary saved to %s", output_path)


if __name__ == "__main__":
    main()
```

## 示例 CSV

```csv
symbol,return_rate
AAPL,0.05
MSFT,0.03
NVDA,0.08
TSLA,-0.02
```

## 知识点串联

### 定义

综合小项目是把文件、类型、函数、异常、日志、数据结构和输出格式组合成一个完整工作流。

### 为什么存在

只有项目能检验基础知识是否真的能被使用。

### 最小案例

读取 CSV -> 计算 summary -> 保存 JSON -> 构造 LLM prompt。

### 常见错误

- CSV 字段名不一致。
- 空数据导致除零或 max/min 报错。
- 输出 JSON 中文转义。
- 函数里混太多 print。

### 工程应用

- Quant 研究摘要。
- LLM 辅助分析。
- Agent 工具函数。
- 数据报告自动化。

### 未来扩展

- 增加波动率。
- 增加最大回撤。
- 接入真实行情 API。
- 做成 Streamlit dashboard。
- 封装成 Agent tool。

## Debug 日志

- `KeyError`：检查 CSV header。
- `ValueError`：收益率无法转成 float。
- 输出文件没生成：检查当前工作目录。
- LLM prompt 太长：先摘要再发送。


## 面试角度 Interview

这个项目展示了 Python 基础到工程应用的闭环：数据输入、模型、函数、验证、输出、日志、LLM 连接。

## Quant 关联

这是最小 Quant research workflow：读取收益率、计算摘要、保存结果、解释结果。

## LLM / Agent 关联

LLM 可以解释 summary；Agent 可以调用这个工具生成 summary，再决定是否继续下载数据或生成报告。

## 复习检查

- [ ] 我能解释项目结构。
- [ ] 我能运行 CSV -> JSON 流程。
- [ ] 我能说明每个函数的职责。
- [ ] 我能添加一个新指标。
- [ ] 我能说出下一步项目方向。

## 题目驱动训练

### 参考题 / 资料

- [LeetCode 121 - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [Python csv docs](https://docs.python.org/3/library/csv.html)
- [Python json docs](https://docs.python.org/3/library/json.html)

### 5 道递进题

#### 1. Easy - 读取价格 CSV

题目：从 CSV 文本中读取价格列表。

讲解：项目入口先从稳定数据结构开始。

```python
import csv
from io import StringIO

def load_prices(csv_text: str) -> list[float]:
    reader = csv.DictReader(StringIO(csv_text))
    return [float(row["price"]) for row in reader]
```

#### 2. Easy - 计算收益率序列

题目：把价格变成日收益率。

讲解：Quant 学习从价格到收益率，这是第一步。

```python
def returns_from_prices(prices: list[float]) -> list[float]:
    returns = []
    for i in range(1, len(prices)):
        returns.append(prices[i] / prices[i - 1] - 1)
    return returns
```

#### 3. Medium - 均线信号

题目：短均线大于长均线时输出 `BUY`，否则 `HOLD`。

讲解：这是最小策略规则，不代表能赚钱，但能训练流程。

```python
def moving_average_signal(prices: list[float], short: int = 3, long: int = 5) -> str:
    if len(prices) < long:
        return "HOLD"
    short_ma = sum(prices[-short:]) / short
    long_ma = sum(prices[-long:]) / long
    return "BUY" if short_ma > long_ma else "HOLD"
```

#### 4. Medium - LLM Prompt Pack

题目：把指标打包成给 LLM 审查的 prompt。

讲解：LLM 适合解释和审查，不替代你的指标计算。

```python
def build_review_prompt(symbol: str, metrics: dict) -> str:
    return (
        f"请审查 {symbol} 的量化指标。\n"
        f"指标: {metrics}\n"
        "请指出数据质量、风险解释和下一步验证。"
    )
```

#### 5. Hard - 端到端小流水线

题目：CSV -> prices -> returns -> metrics -> prompt。

讲解：这就是后续项目的最小骨架。

```python
def run_quant_llm_pipeline(symbol: str, csv_text: str) -> dict:
    prices = load_prices(csv_text)
    rets = returns_from_prices(prices)
    metrics = {
        "last_price": prices[-1] if prices else None,
        "avg_return": sum(rets) / len(rets) if rets else 0.0,
        "signal": moving_average_signal(prices),
    }
    prompt = build_review_prompt(symbol, metrics)
    return {"symbol": symbol, "metrics": metrics, "prompt": prompt}
```
