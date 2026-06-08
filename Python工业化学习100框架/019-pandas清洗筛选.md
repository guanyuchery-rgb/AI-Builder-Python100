# Day19 - pandas 清洗与筛选

> 阶段三：数据分析三大库

## 学习定位

今天学习 pandas 的第二步：**把脏表格变成可分析表格**。

## 认知地图

| 工具 | 输入 | 输出 | 用途 |
| --- | --- | --- | --- |
| `pd.to_numeric` | 字符串列 | 数值列 | 类型转换 |
| `pd.to_datetime` | 日期字符串 | datetime | 时间字段转换 |
| `.dropna()` | DataFrame | 删除缺失后的表 | 去掉关键缺失 |
| `.fillna()` | DataFrame | 填补后的表 | 填补非关键缺失 |
| 布尔筛选 | 条件 | 子表 | 过滤记录 |

## What

清洗不是“让数据变漂亮”，而是让后续计算可信。

今天只做四件事：

1. 转日期。
2. 转数字。
3. 处理缺失值。
4. 按条件筛选。

## Why

真实数据不会按你的想法出现。常见问题：

- 数字列里混入字符串。
- 日期列还是普通文本。
- 关键字段缺失。
- 异常值进入统计。

不清洗就直接分析，结果看起来能跑，实际不可信。

## How：原始表 -> 清洗表

```text
raw df
  ↓
copy
  ↓
to_datetime / to_numeric
  ↓
dropna / fillna
  ↓
boolean filter
  ↓
clean df
```

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 直接改原表 | Debug 不好回退 | 先 `df.copy()` |
| 类型转换报错 | 无法转数字 | `errors="coerce"` |
| 过滤条件没括号 | 逻辑错误 | 每个条件加括号 |
| 缺失值全 drop | 样本损失太大 | 区分关键列和非关键列 |

## 今日强化题（带具体代码）

### 强化题 1：清洗一张脏表

验收：生成 `pandas_cleaning_report.json` 和 `cleaned.csv`。

### 参考代码：`main.py`

```python
from pathlib import Path
import json
import pandas as pd

DAY = 19
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


def clean_dataframe(df):
    cleaned = df.copy()
    cleaned["date"] = pd.to_datetime(cleaned["date"], errors="coerce")
    cleaned["value"] = pd.to_numeric(cleaned["value"], errors="coerce")
    before = len(cleaned)
    cleaned = cleaned.dropna(subset=["date", "value"])
    cleaned["group"] = cleaned["group"].fillna("unknown")
    cleaned = cleaned[(cleaned["value"] >= 0) & (cleaned["value"] <= 100)]
    return cleaned, {"before_rows": before, "after_rows": len(cleaned)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    raw = pd.DataFrame([
        {"date": "2026-01-01", "group": "A", "value": "10"},
        {"date": "bad-date", "group": "A", "value": "12"},
        {"date": "2026-01-03", "group": None, "value": "bad"},
        {"date": "2026-01-04", "group": "B", "value": "9.5"},
        {"date": "2026-01-05", "group": "B", "value": "999"},
    ])
    cleaned, stats = clean_dataframe(raw)
    cleaned.to_csv(OUT / "cleaned.csv", index=False)
    report = {
        "topic": "pandas cleaning and filtering",
        "stats": stats,
        "dtypes": {column: str(dtype) for column, dtype in cleaned.dtypes.items()},
        "records": cleaned.to_dict(orient="records"),
    }
    (OUT / "pandas_cleaning_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day19：pandas 清洗与筛选

to_numeric 做什么：
to_datetime 做什么：
dropna 和 fillna 的区别：
布尔筛选最容易错在哪里：
```
