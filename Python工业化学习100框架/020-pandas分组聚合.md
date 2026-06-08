# Day20 - pandas 分组聚合

> 阶段三：数据分析三大库

## 学习定位

今天学习 pandas 的核心分析动作：**按类别分组，再计算指标**。

## 认知地图

| 工具 | 输入 | 输出 | 用途 |
| --- | --- | --- | --- |
| `groupby` | 类别字段 | 分组对象 | 按组计算 |
| `.agg()` | 多个指标 | 汇总表 | 一次算多列 |
| `.sort_values()` | 表格 | 排序表 | 找高低 |
| `.reset_index()` | 分组结果 | 普通表 | 方便保存 |

## What

分组聚合就是回答：

```text
每个组分别怎么样？
```

例如每个 group 的样本数、均值、最大值。

## Why

数据分析不只看总体，还要比较分组。统计学里的分组均值、组间差异、样本量意识，在 pandas 里主要靠 `groupby`。

## How：明细表 -> 指标表

```text
clean df
  ↓
groupby("group")
  ↓
agg count mean max
  ↓
sort / save
```

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 分组字段有缺失 | unknown 组消失 | 先 fillna |
| 样本量太小 | 均值不稳 | 同时看 count |
| agg 后多级列名复杂 | 保存不方便 | 手动改列名 |

## 今日强化题（带具体代码）

### 强化题 1：生成分组指标表

验收：生成 `group_metrics.csv` 和 `group_metrics.json`。

### 参考代码：`main.py`

```python
from pathlib import Path
import json
import pandas as pd

DAY = 20
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


def build_group_metrics(df):
    grouped = (
        df.groupby("group", dropna=False)
        .agg(
            n=("value", "count"),
            mean_value=("value", "mean"),
            max_value=("value", "max"),
            min_value=("value", "min"),
        )
        .reset_index()
        .sort_values("mean_value", ascending=False)
    )
    grouped["mean_value"] = grouped["mean_value"].round(4)
    return grouped


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame([
        {"group": "A", "value": 10},
        {"group": "A", "value": 12},
        {"group": "A", "value": 15},
        {"group": "B", "value": 8},
        {"group": "B", "value": 11},
        {"group": "C", "value": 20},
    ])
    metrics = build_group_metrics(df)
    metrics.to_csv(OUT / "group_metrics.csv", index=False)
    payload = {
        "topic": "pandas groupby aggregation",
        "metrics": metrics.to_dict(orient="records"),
    }
    (OUT / "group_metrics.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day20：pandas 分组聚合

groupby 解决什么问题：
agg 的输入输出是什么：
为什么要同时看 n 和 mean：
reset_index 为什么常用：
```
