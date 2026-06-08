# Day18 - pandas DataFrame 基础

> 阶段三：数据分析三大库

## 学习定位

今天学习 pandas 的核心对象：**DataFrame 是带行列标签的表格**。

## 认知地图

| 工具 | 输入 | 输出 | 用途 |
| --- | --- | --- | --- |
| `pd.DataFrame()` | dict/list | DataFrame | 创建表 |
| `.head()` | DataFrame | 前几行 | 看样例 |
| `.shape` | DataFrame | 行列数 | 看规模 |
| `.dtypes` | DataFrame | 每列类型 | 看类型 |
| `.describe()` | 数值列 | 统计摘要 | 快速体检 |

## What

pandas DataFrame 可以理解成“有字段名、有行索引的二维表”。

它比 list/dict 更适合做筛选、清洗、分组、聚合、导出。

## Why

CSV/JSON 负责保存数据，pandas 负责分析表格数据。

数据分析第一步不是建模，而是体检：

1. 有多少行列？
2. 字段名是什么？
3. 每列类型是什么？
4. 有没有缺失值？
5. 前几行长什么样？

## How：dict -> DataFrame -> 体检

```text
records
  ↓
pd.DataFrame
  ↓
head / shape / dtypes / describe
  ↓
summary json
```

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 数字列读成 object | 不能正常计算 | `pd.to_numeric` |
| 缺失值没看 | 后续统计偏差 | `.isna().sum()` |
| 只看 head | 忽略类型和规模 | 固定做五项体检 |

## 今日强化题（带具体代码）

### 强化题 1：创建 DataFrame 并体检

验收：生成 `pandas_dataframe_profile.json`。

### 参考代码：`main.py`

```python
from pathlib import Path
import json
import pandas as pd

DAY = 18
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


def profile_dataframe(df):
    numeric_df = df.select_dtypes(include="number")
    return {
        "shape": list(df.shape),
        "columns": list(df.columns),
        "dtypes": {column: str(dtype) for column, dtype in df.dtypes.items()},
        "missing": df.isna().sum().to_dict(),
        "numeric_summary": numeric_df.describe().round(4).to_dict(),
        "head": df.head(3).to_dict(orient="records"),
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = [
        {"date": "2026-01-01", "group": "A", "value": 10.0, "flag": 1},
        {"date": "2026-01-02", "group": "A", "value": 12.5, "flag": 0},
        {"date": "2026-01-03", "group": "B", "value": None, "flag": 1},
        {"date": "2026-01-04", "group": "B", "value": 9.5, "flag": 0},
    ]
    df = pd.DataFrame(rows)
    payload = {"topic": "pandas dataframe basics", "profile": profile_dataframe(df)}
    (OUT / "pandas_dataframe_profile.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day18：pandas DataFrame 基础

DataFrame 是什么：
shape 看什么：
dtypes 看什么：
isna().sum() 看什么：
```
