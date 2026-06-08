# Day17 - NumPy 向量化与统计

> 阶段三：数据分析三大库

## 学习定位

今天学习 NumPy 的核心价值：**不用手写循环，对整列数据一次性计算**。

## 认知地图

| 工具 | 输入 | 输出 | 用途 |
| --- | --- | --- | --- |
| 向量化 | array | array | 批量计算 |
| 布尔掩码 | 条件 | True/False 数组 | 筛选 |
| `np.where` | 条件和两个值 | array | 条件分支 |
| `mean/std/quantile` | array | 统计量 | 数据体检 |

## What

向量化就是把“一个一个算”改成“一整列一起算”。

```python
import numpy as np

prices = np.array([100, 102, 101, 105], dtype=float)
returns = prices[1:] / prices[:-1] - 1
print(returns)
```

这行代码一次性计算所有相邻收益率。

## Why

数据分析和 Quant 中，循环容易慢，也容易写错边界。NumPy 用数组运算表达数学关系，更接近统计学和线性代数。

## How：价格 -> 收益率 -> 风险指标

```text
prices
  ↓
vectorized return
  ↓
mean / std / drawdown
  ↓
summary
```

## 参数拆解方法

### `np.where(condition, x, y)`

| 参数 | 含义 |
| --- | --- |
| `condition` | True/False 数组 |
| `x` | 条件为 True 时取的值 |
| `y` | 条件为 False 时取的值 |

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 数组长度没对齐 | shape mismatch | 检查切片长度 |
| 除以 0 | inf 或 nan | 先检查分母 |
| std 样本口径混乱 | 结果略不同 | 明确 `ddof=0/1` |

## 今日强化题（带具体代码）

### 强化题 1：计算收益率

验收：生成 `numpy_vector_stats.json`。

### 强化题 2：添加阈值标签

任务：修改 `risk_threshold`。

### 参考代码：`main.py`

```python
from pathlib import Path
import json
import numpy as np

DAY = 17
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


def analyze_prices(prices, risk_threshold=0.03):
    arr = np.array(prices, dtype=float)
    returns = arr[1:] / arr[:-1] - 1
    labels = np.where(np.abs(returns) >= risk_threshold, "large_move", "normal")
    cumulative_max = np.maximum.accumulate(arr)
    drawdown = arr / cumulative_max - 1
    return {
        "prices": arr.round(4).tolist(),
        "returns": returns.round(6).tolist(),
        "labels": labels.tolist(),
        "mean_return": round(float(returns.mean()), 6),
        "volatility": round(float(returns.std(ddof=1)), 6),
        "max_drawdown": round(float(drawdown.min()), 6),
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    prices = [100, 102, 101, 107, 103, 110]
    payload = {"topic": "numpy vectorization and statistics", "summary": analyze_prices(prices)}
    (OUT / "numpy_vector_stats.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day17：NumPy 向量化与统计

向量化解决什么问题：
布尔掩码是什么：
np.where 怎么理解：
收益率数组为什么比价格数组少一位：
```
