# Day12 - CSV 进阶 DictReader / DictWriter

> 阶段二：Python 工程化基本功

## 学习定位

今天只学习一个核心主题：**csv.DictReader / csv.DictWriter：CSV -> dict，dict -> CSV**。

Day11 你已经知道 `reader` 读出来是一行行 list。今天升级成“用字段名读写”，让代码从 `row[2]` 变成 `row["minutes"]`。

这一天的核心不是更高级，而是更可读、更稳、更接近真实数据分析。

## 前置知识

- 上一站：Day11 CSV reader / writer
- 下一站：Day13 JSON 基础 loads / dumps
- 必须先会：dict、字段名、文件读写、`int()` 类型转换。

## 认知地图

| 工具 | 输入 | 输出 | 适合什么 |
| --- | --- | --- | --- |
| `csv.DictReader(f)` | 带表头的 CSV 文件 | 一行行 dict | 用字段名读取记录 |
| `csv.DictWriter(f, fieldnames=...)` | 文件对象 + 字段名 | writer 对象 | 按字段名写 CSV |
| `writer.writeheader()` | `fieldnames` | 表头行 | 先写列名 |
| `writer.writerow(row)` | 一个 dict | CSV 一行 | 写单条记录 |
| `writer.writerows(rows)` | 多个 dict | CSV 多行 | 批量写记录 |

## What

`DictReader / DictWriter` 是 CSV 工具里的“字段名版本”。

```text
DictReader: CSV -> dict
DictWriter: dict -> CSV
```

Day11 的 `row[2]` 依赖列位置；Day12 的 `row["minutes"]` 依赖字段名。

真实数据里，字段名比位置更重要。你以后读 Kaggle、行情、评估集时，通常会关心 `date`、`close`、`label`、`question` 这些字段，而不是“第 3 列”。

## Why

不用 `DictReader` 也能读 CSV，但代码会变脆：

```python
minutes = int(row[2])
```

如果以后表格列顺序变了，`row[2]` 可能不再是 minutes。

改成字段名后：

```python
minutes = int(row["minutes"])
```

你一眼能看懂这行在取什么。字段名也是数据分析里的“变量名”，它让数据有语义。

## How：从 list 行升级成 dict 行

数据流是：

```text
dict 记录
  ↓
DictWriter(fieldnames)
  ↓
带表头 CSV
  ↓
DictReader
  ↓
一行行 dict
  ↓
按字段名取值、校验、汇总
```

### 最小写入

```python
import csv
from pathlib import Path

path = Path("study_log.csv")
records = [
    {"day": "11", "topic": "csv reader writer", "minutes": "35"},
    {"day": "12", "topic": "dict csv", "minutes": "45"},
]

with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["day", "topic", "minutes"])
    writer.writeheader()
    writer.writerows(records)
```

### 最小读取

```python
with path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["topic"], int(row["minutes"]))
```

## 参数拆解方法

### `csv.DictWriter(f, fieldnames=[...])`

| 部分 | 含义 | 为什么重要 |
| --- | --- | --- |
| `csv` | CSV 标准库 | 专门处理表格文本 |
| `DictWriter` | dict 写入 CSV 的类 | 把字段名和列顺序绑定起来 |
| `f` | 文件对象 | 必须是可写文件，通常 `"w"` 模式 |
| `fieldnames` | 表头字段列表 | 决定 CSV 列名和列顺序 |
| 返回值 `writer` | 写入器对象 | 继续调用 `writeheader()`、`writerow()`、`writerows()` |

### `writer.writeheader()`

| 部分 | 含义 |
| --- | --- |
| `writer` | 上一步创建的写入器 |
| `writeheader()` | 把 `fieldnames` 写成 CSV 第一行 |
| 常见错误 | 忘记写表头，后面 `DictReader` 就不知道字段名 |

### `csv.DictReader(f)`

| 部分 | 含义 |
| --- | --- |
| `DictReader` | dict 读取器 |
| `f` | 可读文件对象 |
| 输出 | 每一行是 dict，key 来自表头 |
| 常见错误 | 表头字段拼错，`row["minutes"]` 会 `KeyError` |

## 和旧知识的连接

| Day11 | Day12 | 升级点 |
| --- | --- | --- |
| `row[2]` | `row["minutes"]` | 从位置意识升级到字段意识 |
| list 行 | dict 记录 | 字段含义更清楚 |
| 手工记列顺序 | `fieldnames` 固定表头 | 输出更稳定 |
| 打印整行 | 打印 `row.keys()` | Debug 更容易 |

## Common Errors

| 错误 | 表现 | 定位方法 |
| --- | --- | --- |
| `fieldnames` 缺字段 | 写入时报错或字段丢失 | 对比 `records[0].keys()` |
| 忘记 `writeheader()` | 读回来第一行变字段名 | 打开 CSV 看第一行 |
| 数字仍是字符串 | 不能正确计算 | `print(type(row["minutes"]))` |
| 字段名拼错 | `KeyError` | `print(row.keys())` |
| 空值没处理 | `int("")` 报错 | 转换前先判断 |

## Future Usage

- Data：清洗 CSV 原始数据时，字段名就是变量名。
- Quant：行情字段 `date/open/high/low/close/volume` 要稳定。
- LLM：评估集字段 `question/answer/score` 适合 CSV。
- Agent：执行日志里的 `step/tool/status/error` 可以先用 CSV 复盘。

## 4 小时学习节奏

| 时间 | 做什么 | 产物 |
| --- | --- | --- |
| 30 分钟 | 对比 reader 和 DictReader | notes 表格 |
| 60 分钟 | 手打 DictWriter / DictReader | main.py |
| 45 分钟 | 改字段名和列顺序 | errors.md |
| 45 分钟 | 加空值和坏数据 | skipped 输出 |
| 40 分钟 | 写迁移说明 | review.md |

## 今日强化题（带具体代码）

### 强化题 1：复现最小案例

任务：复制下面代码到 `main.py` 并运行。

验收：生成 `outputs/day012/study_log.csv` 和 `summary.json`。

### 强化题 2：替换输入

任务：新增字段 `source`，例如 `book`、`video`、`codex`。

验收：你能说明为什么 `fieldnames` 也要同步改。

### 强化题 3：边界检查

任务：删除一行的 `minutes` 或把它改成 `abc`。

验收：坏行进入 `skipped`，程序继续跑。

### 强化题 4：结果保存

任务：把有效记录和跳过记录分别保存。

验收：能复查哪些数据被排除。

### 强化题 5：迁移说明

任务：写 3 句话说明字段意识为什么是 Pandas、SQL、LLM 评估集的基础。

### 参考代码：`main.py`

```python
from pathlib import Path
import csv
import json

DAY = 12
TOPIC = "CSV DictReader / DictWriter"
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs" / f"day{DAY:03d}"
FIELDS = ["day", "topic", "minutes", "source"]


def ensure_dirs():
    OUT.mkdir(parents=True, exist_ok=True)


def write_records(path: Path):
    records = [
        {"day": "11", "topic": "csv reader writer", "minutes": "35", "source": "course"},
        {"day": "12", "topic": "dict csv", "minutes": "45", "source": "course"},
        {"day": "12", "topic": "bad row", "minutes": "abc", "source": "manual"},
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)


def load_records(path: Path):
    valid = []
    skipped = []
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):
            try:
                minutes = int(row["minutes"])
            except ValueError:
                skipped.append({"line": line_no, "row": row, "reason": "minutes is not int"})
                continue
            row["minutes"] = minutes
            valid.append(row)
    return valid, skipped


def main():
    ensure_dirs()
    csv_path = OUT / "study_log.csv"
    write_records(csv_path)
    valid, skipped = load_records(csv_path)
    summary = {
        "topic": TOPIC,
        "fields": FIELDS,
        "valid_count": len(valid),
        "total_minutes": sum(row["minutes"] for row in valid),
        "sources": sorted({row["source"] for row in valid}),
        "skipped": skipped,
    }
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day12：CSV DictReader / DictWriter

DictReader 的输入是什么：
DictReader 的输出是什么：
fieldnames 决定了什么：
我今天制造了什么错误：
未来会在哪个 IC 使用：
```
