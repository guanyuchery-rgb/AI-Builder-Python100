# Day13 - JSON 完整学习

> 阶段二：基础 Python 收束

## 学习定位

今天把 JSON 一次讲完整：**JSON 是跨程序传递结构化数据的文本格式；Python 用 `json` 标准库完成字符串和文件的读写。**

前两天你已经学了 CSV。CSV 适合二维表，JSON 适合 dict/list 嵌套结构。今天只聚焦 JSON，不再拆到后面。

## 认知地图

| 工具 | 输入 | 输出 | 用途 |
| --- | --- | --- | --- |
| `json.loads(text)` | JSON 字符串 | Python dict/list | 解析 API 文本、模型输出文本 |
| `json.dumps(obj)` | Python dict/list | JSON 字符串 | 打印、日志、网络传输 |
| `json.load(f)` | 文件对象 | Python dict/list | 读取 `.json` 文件 |
| `json.dump(obj, f)` | Python dict/list + 文件对象 | `.json` 文件 | 保存配置、结果、状态 |

### JSON 与 Python 类型对应

| JSON | Python |
| --- | --- |
| object | dict |
| array | list |
| string | str |
| number | int / float |
| true / false | True / False |
| null | None |

## What

JSON 本质是“长得像 dict/list 的文本”。它不是 Python 对象，必须经过解析。

```python
import json

text = '{"name": "item_a", "value": 10}'
data = json.loads(text)
print(data)
```

`text` 是字符串，`data` 是 dict。这个区别非常重要。

## Why

JSON 存在的原因是：不同程序、不同语言、不同机器之间需要一种通用结构化格式。

- 配置文件需要保存参数。
- API 需要返回结构化结果。
- LLM 需要输出可校验字段。
- Agent 需要保存 tool 调用状态。
- Quant 实验需要保存参数、指标、错误信息。

## How：四个函数一次打通

```text
JSON 字符串 --loads--> Python 对象 --dumps--> JSON 字符串
JSON 文件   --load ---> Python 对象 --dump ---> JSON 文件
```

### 字符串读写

```python
import json

text = '{"name": "item_a", "value": 10}'
data = json.loads(text)
print(data["value"])

json_text = json.dumps(data, ensure_ascii=False, indent=2)
print(json_text)
```

### 文件读写

```python
from pathlib import Path
import json

path = Path("data.json")
with path.open("w", encoding="utf-8") as f:
    json.dump({"items": [{"name": "item_a", "value": 10}]}, f, ensure_ascii=False, indent=2)

with path.open("r", encoding="utf-8") as f:
    data = json.load(f)
```

### 嵌套路径

```python
data = {"items": [{"name": "item_a", "value": 10}]}
value = data["items"][0]["value"]
print(value)
```

读法：

```text
dict -> key "items" -> list -> index 0 -> dict -> key "value"
```

## 参数拆解方法

### `json.dumps(obj, ensure_ascii=False, indent=2)`

| 参数 | 含义 | 建议 |
| --- | --- | --- |
| `obj` | 要转成 JSON 的 Python 对象 | 优先 dict/list |
| `ensure_ascii=False` | 中文正常显示 | 写中文内容时固定加 |
| `indent=2` | 缩进 2 格 | 人类可读、Git diff 清楚 |

### `json.dump(obj, f, ensure_ascii=False, indent=2)`

| 参数 | 含义 | 易错点 |
| --- | --- | --- |
| `obj` | Python 对象 | 不能包含函数、Path、set 等不可序列化对象 |
| `f` | 文件对象 | 要用 `"w"` 和 `encoding="utf-8"` |
| 返回值 | `None` | 它直接写文件，不返回字符串 |

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 单引号写 JSON | `JSONDecodeError` | JSON 字符串用双引号 |
| 字符串当 dict | `TypeError` | 先 `json.loads(text)` |
| `dump` 当 `dumps` | 得到 `None` | `dump` 写文件，`dumps` 返回字符串 |
| 顶层类型看错 | list/dict 取值方式错 | 先 `print(type(data))` |
| 写入 set/Path | not JSON serializable | 先转成 list/str |

## 今日强化题（带具体代码）

### 强化题 1：跑通四个函数

任务：运行下面代码，确认 `loads/dumps/load/dump` 都出现。

验收：生成 `outputs/day013/records.json` 和 `summary.json`。

### 强化题 2：替换输入

任务：新增一条 record，并修改一个嵌套字段。

### 强化题 3：边界检查

任务：把一条 value 改成 `null`，观察 skipped。

### 强化题 4：总结 JSON vs CSV

任务：写 3 句话说明什么时候 JSON 比 CSV 更合适。

### 参考代码：`main.py`

```python
from pathlib import Path
import json

DAY = 13
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


def parse_json_text(text):
    data = json.loads(text)
    return data


def validate_records(data):
    valid = []
    skipped = []
    for index, item in enumerate(data.get("records", [])):
        value = item.get("metrics", {}).get("value")
        if not isinstance(value, (int, float)):
            skipped.append({"index": index, "item": item, "reason": "value must be numeric"})
            continue
        valid.append(item)
    return valid, skipped


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    raw_text = """
    {
      "metadata": {"source": "demo", "schema_version": 1},
      "records": [
        {"name": "item_a", "group": "A", "metrics": {"value": 10}},
        {"name": "item_b", "group": "A", "metrics": {"value": 15}},
        {"name": "item_c", "group": "B", "metrics": {"value": null}}
      ]
    }
    """
    data = parse_json_text(raw_text)
    valid, skipped = validate_records(data)
    with (OUT / "records.json").open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with (OUT / "records.json").open("r", encoding="utf-8") as f:
        loaded = json.load(f)
    summary = {
        "topic": "complete json basics",
        "source": loaded["metadata"]["source"],
        "valid_count": len(valid),
        "total_value": sum(item["metrics"]["value"] for item in valid),
        "skipped": skipped,
    }
    summary_text = json.dumps(summary, ensure_ascii=False, indent=2)
    (OUT / "summary.json").write_text(summary_text, encoding="utf-8")
    print(summary_text)


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day13：JSON 完整学习

loads / dumps 的区别：
load / dump 的区别：
JSON 和 dict/list 的关系：
我今天读懂的一条嵌套路径：
JSON 最常见错误：
```
