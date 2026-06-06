# Day11 - CSV 基础：reader / writer

> 阶段二：Python 工程化基本功

## 学习定位

今天只学一件事：CSV 是什么，以及 `csv.reader` / `csv.writer` 怎么把“表格文件”和“Python 列表”互相转换。

今天不学 `DictReader`、`DictWriter` 和 JSON。

这些内容后面再讲。先把第一层地基打稳。

## 前置知识

- 推荐前置：Day10 文件读写
- 上一站：Day10
- 下一站：Day12

## 今日知识地图

```text
Day10：f.write() 手工写普通文本
  ↓
Day11：csv.writer() 自动写表格行
  ↓
Day11：csv.reader() 自动读表格行
```

CSV 可以先理解成“用逗号分隔的表格文件”。

例如：

```text
day,topic,minutes
Day11,CSV,60
Day12,CSV Dict,70
```

## csv 库认知地图

`csv` 是 Python 自带的标准库，专门处理 CSV 表格文件。

今天只看前两个工具：

| 工具 | 输入 | 输出 | 你可以怎么理解 |
| --- | --- | --- | --- |
| `csv.reader` | CSV 文件 | 一行行 list | 把表格读成列表 |
| `csv.writer` | list / tuple | CSV 文件 | 把列表写成表格 |

先记住：

```text
reader : CSV  -> list
writer : list -> CSV
```

后面再升级：

```text
DictReader : CSV  -> dict
DictWriter : dict -> CSV
json       : dict/list <-> JSON
```

## What

CSV 基础，就是让 Python 能稳定读写简单表格。

它解决的问题不是“保存文字”，而是“保存一行一行、每行结构相同的数据”。

## Why

如果只用 `f.write()`，你需要自己拼字符串：

```python
f.write("Day11,CSV,60
")
```

这能跑，但容易出错：

- 忘记逗号。
- 忘记换行。
- 字段顺序写反。
- 后面读取时还要自己 `split(",")`。

`csv.writer()` 和 `csv.reader()` 的意义是：让 Python 帮你处理表格格式。

## How

### 1. 写入 CSV：list -> CSV

```python
import csv
from pathlib import Path

path = Path("learning_log.csv")

rows = [
    ["day", "topic", "minutes"],
    ["Day11", "CSV", 60],
    ["Day12", "CSV Dict", 70],
]

with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

逐项拆解：

| 代码 | 含义 |
| --- | --- |
| `import csv` | 引入 CSV 工具箱 |
| `Path("learning_log.csv")` | 准备文件路径 |
| `path.open("w")` | 以写入模式打开文件 |
| `newline=""` | 避免 CSV 多出空行 |
| `csv.writer(f)` | 创建“写 CSV 的工具” |
| `writer.writerows(rows)` | 一次写入多行 |

### 2. 读取 CSV：CSV -> list

```python
import csv
from pathlib import Path

path = Path("learning_log.csv")

with path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

print(rows)
```

输出大概是：

```python
[
    ["day", "topic", "minutes"],
    ["Day11", "CSV", "60"],
    ["Day12", "CSV Dict", "70"],
]
```

注意：CSV 读出来通常先是字符串，所以 `"60"` 不是数字 `60`。

需要计算时再转换：

```python
minutes = int(rows[1][2])
```

## Common Errors

| 错误 | 原因 | 修法 |
| --- | --- | --- |
| 文件多出空行 | 没写 `newline=""` | 打开文件时加上 |
| 读出来数字是字符串 | CSV 本质是文本 | 用 `int()` / `float()` 转换 |
| 找不到文件 | 路径不对 | `print(path.resolve())` 检查 |
| 行列位置拿错 | 只用 list 依赖下标 | 后面学习 `DictReader` |

## Future Usage

CSV 基础后面会继续出现：

- pandas 读取 CSV。
- Quant 行情表。
- 学习记录表。
- API 数据落地。
- Agent 工具执行日志。

今天只要掌握一件事：

```text
CSV 是表格文本。
csv.writer 把 list 写成 CSV。
csv.reader 把 CSV 读成 list。
```

## 今日练习

1. 手写 3 行学习记录，保存为 CSV。
2. 重新读取 CSV，并打印所有行。
3. 取出第二行的 minutes，把它转成 int。
4. 故意把路径写错一次，观察报错。
5. 用自己的话写下：为什么下一步要学习 DictReader。
