# Day11 - 文件、异常、JSON 与 CSV

学习定位：掌握 Python 处理本地数据文件的基础能力，这是数据分析、量化研究、LLM 数据准备和 Agent 工具落地的共同入口。

## 2小时安排

- 20 分钟：理解路径、文件读写、异常处理。
- 30 分钟：手打文本、JSON、CSV 三个最小案例。
- 35 分钟：完成一个小型行情数据读写练习。
- 20 分钟：记录 2 个常见错误。
- 15 分钟：写 Quant 与 Agent 关联。

## 知识点 1：路径与文件读写

### 定义

文件读写是程序和本地磁盘交换数据的方式。`pathlib.Path` 是现代 Python 中处理路径的推荐工具。

### 为什么存在

数据分析和量化研究经常从 CSV、JSON、日志、文本开始。没有稳定文件读写能力，后续工具无法复现。

### 最小案例

```python
from pathlib import Path

path = Path("day11_note.txt")
path.write_text("Python 文件读写练习", encoding="utf-8")

content = path.read_text(encoding="utf-8")
print(content)
```

### 常见错误

- 路径不在当前工作目录。
- 忘记指定 `encoding="utf-8"`。
- 把相对路径和绝对路径混淆。

### 工程应用

- 保存中间数据。
- 读取配置文件。
- 记录学习日志。
- 给 Agent 提供本地资料。

### 未来扩展

- 项目目录结构。
- 日志文件。
- 数据版本管理。
- 云存储。

## 知识点 2：异常处理 Exception

### 定义

异常处理用于在错误发生时控制程序行为，而不是让程序直接崩溃。

### 为什么存在

真实数据总会有缺失、格式错误、文件不存在、网络失败。异常处理让程序可恢复、可解释。

### 最小案例

```python
from pathlib import Path

path = Path("missing.csv")

try:
    text = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"文件不存在: {path}")
```

### 常见错误

- 用裸 `except:` 吞掉所有错误。
- 捕获异常后不记录原因。
- 把数据错误和程序错误混在一起。

### 工程应用

- 数据导入工具。
- API 重试逻辑。
- Agent 工具失败返回。
- Quant 数据质量检查。

### 未来扩展

- 自定义异常。
- 日志 logging。
- 错误上报。

## 知识点 3：JSON 与 CSV

### 定义

JSON 适合保存结构化对象，CSV 适合保存表格数据。

### 为什么存在

LLM/Agent 常用 JSON 交换结构化信息；数据分析和量化数据常用 CSV 保存表格。

### 最小案例

```python
import csv
import json
from pathlib import Path

records = [
    {"symbol": "AAPL", "price": 102.5},
    {"symbol": "MSFT", "price": 210.0},
]

json_path = Path("prices.json")
json_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

csv_path = Path("prices.csv")
with csv_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["symbol", "price"])
    writer.writeheader()
    writer.writerows(records)

print(json_path.read_text(encoding="utf-8"))
```

## Debug 日志

- `FileNotFoundError`：路径不对或文件不存在。
- `UnicodeDecodeError`：编码不一致。
- `json.JSONDecodeError`：JSON 格式不合法。
- CSV 读出来都是字符串，需要手动转换类型。


## 面试角度 Interview

能说明 JSON 和 CSV 的使用场景差异，并解释为什么文件操作要使用上下文管理器 `with`。

## Quant 关联

行情、交易、回测结果最常见的落地形式就是 CSV/JSON。稳定读写能力是量化实验可复现的第一步。

## LLM / Agent 关联

Agent 工具经常读取本地文件、输出 JSON 结果。JSON 是 LLM 工具调用和结构化输出的核心格式。

## 复习检查

- [ ] 我能用 `Path` 读写文本。
- [ ] 我能处理文件不存在异常。
- [ ] 我能读写 JSON。
- [ ] 我能读写 CSV 并理解类型转换问题。

## 简单路线 7 题（不超前）

只用今天及之前学过的能力。做不出来时，先回看当天最小案例，不跳到后面知识。

1. 读取一个文本文件。
2. 写入一个 JSON 文件。
3. 读取一段 CSV 文本。
4. 用 try/except 捕获文件不存在。
5. 用正则提取一个日期或邮箱。
6. 把解析结果保存成 dict。
7. 记录一次解析失败，并说明兜底方案。
## 题目驱动训练

### 参考题 / 资料

- [Python pathlib docs](https://docs.python.org/3/library/pathlib.html)
- [Python json docs](https://docs.python.org/3/library/json.html)
- [Python csv docs](https://docs.python.org/3/library/csv.html)

### 5 道递进题

#### 1. Easy - 安全读取文本

题目：文件不存在时返回空字符串。

讲解：批处理脚本要能处理缺文件，不要一上来崩。

```python
from pathlib import Path

def read_text_safe(path: str) -> str:
    file = Path(path)
    if not file.exists():
        return ""
    return file.read_text(encoding="utf-8")
```

#### 2. Easy - JSON 读取

题目：读取 JSON，解析失败时返回默认 dict。

讲解：外部文件不可信，解析要有兜底。

```python
import json

def load_json_safe(path: str) -> dict:
    text = read_text_safe(path)
    if not text:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}
```

#### 3. Medium - CSV 求和

题目：读取 CSV 字符串，按某一列求和。

讲解：这是数据分析脚本最小单元。

```python
import csv
from io import StringIO

def sum_csv_column(csv_text: str, column: str) -> float:
    reader = csv.DictReader(StringIO(csv_text))
    total = 0.0
    for row in reader:
        total += float(row.get(column, 0) or 0)
    return total
```

#### 4. Medium - 合并配置

题目：用户配置覆盖默认配置。

讲解：项目默认值要稳定，用户只改需要改的部分。

```python
def merge_config(defaults: dict, user_config: dict) -> dict:
    merged = defaults.copy()
    merged.update(user_config)
    return merged
```

#### 5. Hard - 文件处理流水线

题目：读取 JSON 配置，读取 CSV，输出汇总结果。

讲解：这就是最小 ETL：extract、transform、load。

```python
# 每一步都独立，出错时容易定位
def run_pipeline(config_path: str, csv_text: str) -> dict:
    config = merge_config({"amount_column": "amount"}, load_json_safe(config_path))
    amount = sum_csv_column(csv_text, config["amount_column"])
    return {"amount_sum": amount, "config": config}
```
