# Day24 - pandas读取与检查表格

学习定位：用 pandas 读取 CSV 并做第一轮数据体检。

## 2小时安排

- 15 分钟：读定位和最小代码。
- 25 分钟：手打一遍最小案例。
- 70 分钟：完成 5 道递进题。
- 10 分钟：记录 Debug、边界情况和项目迁移点。

## 核心知识点：DataFrame Inspection

### 定义

DataFrame Inspection 是把今天能力固定成可复用模块的方式。

### 为什么存在

它让代码从“这次能跑”变成“下次能复查、能迁移、能被项目调用”。

### 最小案例

```python
import pandas as pd

df = pd.read_csv("prices.csv")
print(df.head())
print(df.dtypes)
print(df.isna().sum())
```

### 常见错误

- 直接把逻辑写在 notebook 或临时脚本里。
- 输入字段没有校验。
- 结果只 print，不保存。
- 失败原因没有记录。

### 工程应用

- 数据清洗和指标计算。
- Quant research 小项目。
- LLM report assistant。
- Agent tool prototype。

### 未来扩展

- 增加测试。
- 增加 README 运行说明。
- 增加 CLI/API/UI 入口。
- 接入真实项目数据。

## Debug 日志

- 路径错误：先打印当前工作目录。
- 类型错误：先检查输入字段和 dtype。
- 结果异常：先缩小到 3 行样例数据。
- 依赖错误：记录安装命令和 Python 版本。

## 面试 / 项目角度

能说明今天代码的输入、输出、失败情况，以及它如何进入一个真实项目。

## Quant 关联

行情、持仓、交易记录大多先进入 DataFrame。

## LLM / Agent 关联

Agent 调用数据工具前，需要知道字段是否完整。

## 复习检查

- [ ] 我能独立解释今天能力解决什么问题。
- [ ] 我能手打一遍最小案例。
- [ ] 我能完成 5 道递进题。
- [ ] 我能说清输入、输出和失败情况。
- [ ] 我知道它如何迁移到 Quant / LLM / Agent 项目。

## 题目驱动训练

### 参考题 / 资料

- [pandas docs](https://pandas.pydata.org/docs/)
- [csv](https://docs.python.org/3/library/csv.html)
- [Python Docs](https://docs.python.org/3/)

### 今日产出

数据字段体检清单。

### 5 道递进题

#### 1. Easy - 读取并查看行情表

题目：读取 CSV，输出前 5 行、字段类型、缺失值数量。

讲解：先做 data inspection，再决定怎么清洗。

```python
import pandas as pd

def inspect_table(path: str) -> dict:
    df = pd.read_csv(path)
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "missing": df.isna().sum().to_dict(),
    }
```

#### 2. Easy - 字段类型修正

题目：把日期列转成 datetime，把数值列转成 numeric。

讲解：错误类型会让统计结果看起来能跑但实际错。

```python
import pandas as pd

def fix_types(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for col in ["price", "return_rate", "volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df
```

#### 3. Medium - 分组指标

题目：按 symbol 输出均值、标准差、样本数。

讲解：summary 是给人和 LLM 阅读的中间层。

```python
import pandas as pd

def symbol_summary(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    return df.groupby("symbol")[value_col].agg(["mean", "std", "count"]).reset_index()
```

#### 4. Medium - 异常行定位

题目：找出缺少 symbol 或数值为空的行。

讲解：不要只 dropna，要先知道坏数据在哪里。

```python
import pandas as pd

def find_bad_rows(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    mask = df["symbol"].isna() | df[value_col].isna()
    return df.loc[mask]
```

#### 5. Hard - CSV 到报告流水线

题目：读取、修正、汇总，并输出 Markdown 文本。

讲解：这是最小可复盘数据流水线。

```python
def build_table_report(path: str, value_col: str) -> str:
    df = fix_types(pd.read_csv(path))
    summary = symbol_summary(df.dropna(subset=[value_col]), value_col)
    return summary.to_markdown(index=False)
```
