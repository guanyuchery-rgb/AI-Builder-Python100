# Day13 - JSON 基础 loads / dumps

> 阶段二：Python 工程化基本功

## 学习定位

今天只学习一个核心主题：**json.loads / json.dumps：JSON 字符串 <-> Python dict/list**。

Day11-12 学的是 CSV。CSV 像二维表；JSON 像 Python 里的 dict/list 组合。今天先不碰复杂 API，只把 JSON 的基本转换打稳。

## 前置知识

- 上一站：Day12 CSV DictReader / DictWriter
- 下一站：Day14 JSON 文件读写与嵌套结构
- 必须先会：dict、list、字符串、类型检查、`print(type(x))`。

## 认知地图

JSON 是一种通用数据格式。它最常见于：配置文件、API 响应、LLM 结构化输出、Agent tool 参数、实验记录。

| 工具 | 输入 | 输出 | 适合什么 |
| --- | --- | --- | --- |
| `json.loads(text)` | JSON 字符串 | Python dict/list | 把外部文本变成 Python 对象 |
| `json.dumps(obj)` | Python dict/list | JSON 字符串 | 把 Python 对象变成可保存/传输的文本 |
| `ensure_ascii=False` | 中文输出开关 | 中文正常显示 | 避免中文变成 `\u4e2d` |
| `indent=2` | 缩进格式 | 更好读的 JSON | 方便复查和 Git diff |

### JSON 和 Python 类型对照

| JSON | Python | 例子 |
| --- | --- | --- |
| object | dict | `{"topic": "python"}` |
| array | list | `["csv", "json"]` |
| string | str | `"python"` |
| number | int / float | `120`, `3.14` |
| true / false | True / False | `true` -> `True` |
| null | None | `null` -> `None` |

## What

JSON 不是 Python 专属格式，但它和 Python 的 dict/list 非常像。

你可以先这样记：

```text
JSON 字符串
  ↓ json.loads
Python dict/list
  ↓ json.dumps
JSON 字符串
```

今天的重点是看清“字符串”和“Python 对象”的区别。

```python
text = '{"topic": "python", "minutes": 120}'
data = json.loads(text)
```

`text` 是字符串，`data` 才是 dict。

## Why

如果你把 JSON 字符串当 dict 用，会马上卡住：

```python
text = '{"topic": "python"}'
print(text["topic"])  # 错：字符串不能用字段名取值
```

必须先 `json.loads(text)`，把它变成 Python 对象。

反过来，如果你要把 dict 保存成文件、发给 API、写进日志，也不能直接把 dict 当标准 JSON 文本，需要 `json.dumps(data)`。

## How：先区分字符串和对象

数据流是：

```text
外部 JSON 文本
  ↓
json.loads
  ↓
Python dict/list
  ↓
字段读取、类型转换、检查
  ↓
json.dumps
  ↓
可保存、可复制、可传输的 JSON 文本
```

### 最小读取：字符串 -> dict

```python
import json

text = '{"topic": "python", "minutes": 120}'
data = json.loads(text)

print(type(text))  # str
print(type(data))  # dict
print(data["topic"])
```

### 最小输出：dict -> 字符串

```python
result = {"topic": "JSON", "ok": True, "errors": []}
json_text = json.dumps(result, ensure_ascii=False, indent=2)
print(json_text)
```

## 参数拆解方法

### `json.loads(text)`

| 部分 | 含义 | 你要问的问题 |
| --- | --- | --- |
| `json` | 标准库模块 | 这个工具箱负责 JSON 编码/解码 |
| `loads` | load string | 输入必须是字符串，不是文件对象 |
| `text` | JSON 字符串 | 它是不是合法 JSON？双引号、逗号、括号对不对？ |
| 返回值 | dict 或 list | 后面按 `data["key"]` 或 `data[0]` 使用 |

### `json.dumps(obj, ensure_ascii=False, indent=2)`

| 参数 | 含义 | 为什么重要 |
| --- | --- | --- |
| `obj` | Python dict/list | 要转换成 JSON 的对象 |
| `ensure_ascii=False` | 中文正常显示 | 学习日志和中文字段更可读 |
| `indent=2` | 缩进 2 格 | 文件好读，Git diff 好看 |
| 返回值 | str | 只是字符串，还没写入文件 |

## 和旧知识的连接

| 旧知识 | 今天升级成 | 升级后解决什么 |
| --- | --- | --- |
| dict | JSON object | 字段结构可以跨程序保存 |
| list | JSON array | 多条记录可以保存成数组 |
| 字符串 | JSON text | 外部传输格式和内部对象分开 |
| `print(type(x))` | JSON 调试第一步 | 先确认顶层类型再取字段 |
| CSV 表格 | JSON 嵌套 | 可以表达配置、日志、API 响应 |

## Common Errors

| 错误 | 表现 | 定位方法 |
| --- | --- | --- |
| 单引号写 JSON | `JSONDecodeError` | JSON 标准要求字符串用双引号 |
| 多写逗号 | `JSONDecodeError` | 检查最后一个字段后有没有多余逗号 |
| 把 JSON 字符串当 dict | `TypeError` | `print(type(value))` |
| 中文变 `\u4e2d` | 输出难读 | `ensure_ascii=False` |
| 顶层类型看错 | list 当 dict 用 | 先打印 `type(data)` 和第一条样例 |

## Future Usage

- Data：保存清洗配置、字段字典、数据报告摘要。
- Quant：保存策略参数、实验结果、回测摘要。
- LLM：保存 prompt、模型输出、评估样例。
- Agent：保存 tool 参数、执行状态、错误信息。

## 4 小时学习节奏

| 时间 | 做什么 | 产物 |
| --- | --- | --- |
| 30 分钟 | 写 JSON/Python 类型对照表 | notes.md |
| 60 分钟 | 手打 loads / dumps | main.py |
| 45 分钟 | 制造非法 JSON | errors.md |
| 45 分钟 | 改中文和缩进参数 | outputs |
| 40 分钟 | 写 CSV vs JSON 初步区别 | review.md |

## 今日强化题（带具体代码）

### 强化题 1：复现最小案例

任务：复制下面代码到 `main.py` 并运行。

验收：终端打印 JSON，生成 `outputs/day013/summary.json`。

### 强化题 2：替换输入

任务：新增一个学习主题，例如 `"json"`、`"api"`、`"agent"`。

验收：`total_minutes` 和 `topics` 会变化。

### 强化题 3：边界检查

任务：把一条记录的 minutes 改成 `null` 或字符串 `"bad"`。

验收：坏记录进入 `skipped`。

### 强化题 4：结果保存

任务：把 `json.dumps(...)` 的结果写入文件。

验收：文件中中文正常显示，并且有缩进。

### 强化题 5：迁移说明

任务：写 3 句话说明 JSON 为什么适合 LLM/Agent 的输入输出。

### 参考代码：`main.py`

```python
from pathlib import Path
import json

DAY = 13
TOPIC = "JSON loads / dumps"
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs" / f"day{DAY:03d}"


def ensure_dirs():
    OUT.mkdir(parents=True, exist_ok=True)


def parse_learning_json(text: str):
    data = json.loads(text)
    valid = []
    skipped = []
    for index, item in enumerate(data["records"]):
        minutes = item.get("minutes")
        if not isinstance(minutes, int) or minutes <= 0:
            skipped.append({"index": index, "item": item, "reason": "minutes must be positive int"})
            continue
        valid.append(item)
    return {
        "topic": TOPIC,
        "total_minutes": sum(item["minutes"] for item in valid),
        "topics": [item["topic"] for item in valid],
        "skipped": skipped,
    }


def main():
    ensure_dirs()
    raw_text = '''{
      "records": [
        {"day": 11, "topic": "csv", "minutes": 35},
        {"day": 12, "topic": "dict csv", "minutes": 45},
        {"day": 13, "topic": "json", "minutes": null}
      ]
    }'''
    summary = parse_learning_json(raw_text)
    output_text = json.dumps(summary, ensure_ascii=False, indent=2)
    (OUT / "summary.json").write_text(output_text, encoding="utf-8")
    print(output_text)


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day13：JSON loads / dumps

JSON 字符串和 dict 的区别：
loads 的输入是什么：
dumps 的输出是什么：
我制造的 JSON 错误：
未来会在哪个 IC 使用：
```
