# Day11 - CSV 基础 reader / writer

> 阶段二：Python 工程化基本功

## 学习定位

今天只学习一个核心主题：**csv.reader / csv.writer：CSV -> list，list -> CSV**。

你已经会 Day10 的本地 CLI，也会 `open()`、`f.write()`、列表和循环。今天不是突然背一个新库，而是把“手工写文本”升级成“按表格结构读写数据”。

Day 主线控制在 4 小时以内：先建立 CSV 库认知地图，再写最小 reader / writer，再做边界实验。

## 前置知识

- 上一站：Day10 CLI 基础
- 下一站：Day12 CSV 进阶 DictReader / DictWriter
- 必须先会：文件路径、`with open(...) as f`、列表、循环、`int()` 类型转换。

## 认知地图

CSV 可以先理解成“纯文本表格”。

```text
topic,minutes
python,120
sql,90
```

它看起来像 Excel，但本质还是文本文件：逗号分隔列，换行分隔行。

| 工具 | 输入 | 输出 | 适合什么 |
| --- | --- | --- | --- |
| `csv.reader(f)` | CSV 文件对象 | 一行行 list | 读取没有字段名意识的表格 |
| `csv.writer(f)` | CSV 文件对象 | writer 对象 | 把 list 行写进 CSV |
| `writer.writerow(row)` | 一个 list | 文件新增一行 | 写表头或单行数据 |
| `writer.writerows(rows)` | 多个 list | 文件新增多行 | 批量写数据 |

今天只学这四个点，不学 `DictReader` 和 `DictWriter`。后者留到 Day12。

## What

`csv` 是 Python 标准库里专门处理 CSV 的工具箱。

`reader / writer` 是最基础的一对工具：

```text
reader: CSV 文件 -> 一行行 list
writer: list 行 -> CSV 文件
```

这比手写 `"a,b,c\n"` 稳，因为 CSV 里会遇到逗号、换行、空字段、引号等细节。库的价值就是替你处理这些格式细节。

## Why

昨天如果要保存一组表格记录，你可能会这样写：

```python
f.write("day,topic,minutes\n")
f.write("11,csv,35\n")
```

这能跑，但问题是：

- 字段顺序靠你手工记。
- 值里有逗号时容易乱。
- 多写几行后换行和空格容易出错。
- 读回来时还要自己 `split(",")`。

`csv.writer` 和 `csv.reader` 的意义是：把“文本拼接”升级成“表格行读写”。

## How：从旧方法升级到 reader / writer

先看数据流，不直接背 API。

```text
list 行数据
  ↓
csv.writer(f).writerows(rows)
  ↓
records.csv
  ↓
csv.reader(f)
  ↓
一行行 list
  ↓
跳过表头、转换 minutes、汇总
```

### 最小写入

```python
import csv
from pathlib import Path

path = Path("records.csv")
rows = [
    ["day", "topic", "minutes"],
    ["11", "csv reader writer", "35"],
    ["12", "dict csv", "45"],
]

with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

### 最小读取

```python
with path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

你会看到每一行都是 list：

```text
['day', 'topic', 'minutes']
['11', 'csv reader writer', '35']
['12', 'dict csv', '45']
```

## 参数拆解方法

第一次看到 `csv.writer(f)`，不要只记函数名，按对象拆。

### `csv.writer(f)`

| 部分 | 含义 | 你要问的问题 |
| --- | --- | --- |
| `csv` | 标准库模块 | 这个工具箱管什么？CSV 表格文本。 |
| `writer` | 写 CSV 的函数 | 它把什么写到哪里？把 list 行写进文件。 |
| `f` | 文件对象 | 这个文件是用什么模式打开的？通常是 `"w"`。 |
| `newline=""` | 换行控制 | 为什么要写？避免部分系统写出多余空行。 |
| 返回值 `writer` | 写入器对象 | 后面可以调用 `writerow()` / `writerows()`。 |

### `csv.reader(f)`

| 部分 | 含义 | 你要问的问题 |
| --- | --- | --- |
| `reader` | 读 CSV 的函数 | 它把 CSV 变成什么？一行行 list。 |
| `f` | 文件对象 | 文件是否存在？编码是否正确？ |
| 返回值 | 可迭代对象 | 可以放进 `for row in reader`。 |
| `row` | 一行数据 | 这一行是 list，不是 dict。取字段要靠下标。 |

## 和旧知识的连接

| 旧知识 | 今天升级成 | 升级后解决什么 |
| --- | --- | --- |
| `f.write()` | `csv.writer()` | 不手工拼逗号和换行 |
| 字符串 | list 行 | 每一列的位置稳定 |
| `for` 循环 | `for row in reader` | 一行一行处理文件 |
| `int()` | 字段类型转换 | CSV 读出来默认多是字符串 |
| Debug 打印 | 打印 `row` 和 `type(row)` | 先看结构再计算 |

## Common Errors

| 错误 | 表现 | 定位方法 |
| --- | --- | --- |
| 忘记 `newline=""` | CSV 中间出现多余空行 | 写文件时固定加上 `newline=""` |
| 把 `row` 当 dict | `row["minutes"]` 报错 | `reader` 输出 list，只能用下标 |
| 忘记跳过表头 | `int("minutes")` 报错 | 先 `header = next(reader)` |
| 数字没转换 | `'35' + '45'` 变成字符串拼接 | `minutes = int(row[2])` |
| 路径不清楚 | 找不到文件 | 打印 `Path.cwd()` 和 `path.resolve()` |

## Future Usage

- Data：读取外部原始 CSV，先检查表头和前 5 行。
- Quant：读取行情样例，先把价格、成交量从字符串转成数字。
- LLM：把评估样例保存成 CSV，方便批量对比。
- Agent：把 tool 执行日志先落成表格，后续再分析。

## 4 小时学习节奏

| 时间 | 做什么 | 产物 |
| --- | --- | --- |
| 30 分钟 | 画 CSV -> list 的数据流 | `notes.md` |
| 60 分钟 | 手打 writer 和 reader | `main.py` |
| 45 分钟 | 改 2 行输入样例 | `records.csv` |
| 45 分钟 | 故意制造表头/类型错误 | `errors.md` |
| 40 分钟 | 写迁移说明 | 复盘 5 行 |

## 今日强化题（带具体代码）

### 强化题 1：复现最小案例

任务：复制下面代码到 `main.py` 并运行。

验收：终端打印 JSON，生成 `outputs/day011/records.csv` 和 `summary.json`。

### 强化题 2：替换输入

任务：新增 2 行样例记录，至少一行数值字段大于当前样例。

验收：`total_minutes` 和 `long_sessions` 会变化。

### 强化题 3：边界检查

任务：把一行 minutes 改成空字符串或 `abc`。

验收：程序不会崩溃，坏行进入 `skipped`。

### 强化题 4：结果保存

任务：保留 CSV 原始记录，同时保存 JSON 汇总。

验收：关闭终端后还能复查两个文件。

### 强化题 5：迁移说明

任务：写 3 句话说明 CSV reader / writer 如何迁移到 Data、Quant、LLM 或 Agent。

### 参考代码：`main.py`

```python
from pathlib import Path
import csv
import json

DAY = 11
TOPIC = "CSV reader / writer"
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs" / f"day{DAY:03d}"


def ensure_dirs():
    OUT.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path):
    rows = [
        ["day", "topic", "minutes"],
        ["11", "csv reader writer", "35"],
        ["12", "dict csv preview", "45"],
        ["13", "json preview", ""],
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def read_csv(path: Path):
    valid = []
    skipped = []
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for line_no, row in enumerate(reader, start=2):
            try:
                minutes = int(row[2])
            except (IndexError, ValueError):
                skipped.append({"line": line_no, "row": row, "reason": "bad minutes"})
                continue
            valid.append({"day": row[0], "topic": row[1], "minutes": minutes})
    return header, valid, skipped


def main():
    ensure_dirs()
    csv_path = OUT / "records.csv"
    write_csv(csv_path)
    header, valid, skipped = read_csv(csv_path)
    summary = {
        "topic": TOPIC,
        "header": header,
        "valid_count": len(valid),
        "total_minutes": sum(item["minutes"] for item in valid),
        "long_sessions": [item for item in valid if item["minutes"] >= 45],
        "skipped": skipped,
    }
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

### Debug 记录要求

```text
错误现象：
触发输入：
定位过程：
修复方式：
以后如何避免：
```

## 今日复盘模板

```text
Day11：CSV reader / writer

CSV 的输入是什么：
reader 的输出是什么：
writer 的输入是什么：
我今天最容易错在哪里：
未来会在哪个 IC 使用：
```
