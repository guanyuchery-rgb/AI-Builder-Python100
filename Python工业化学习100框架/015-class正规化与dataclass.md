# Day15 - class 正规化与 dataclass

> 阶段二：基础 Python 收束：面向对象

## 学习定位

今天把 class 学到“够用、正规、能接工程”的水平：**dataclass、类型标注、默认值、`from_dict`、`to_dict`、对象校验。**

学完今天，基础 Python 第一阶段结束。Day16 开始进入数据分析三大库：NumPy、pandas、Matplotlib。

## 认知地图

| 工具 | 输入 | 输出 | 作用 |
| --- | --- | --- | --- |
| `@dataclass` | 字段声明 | 自动生成初始化方法 | 少写样板代码 |
| 类型标注 | `value: float` | 可读边界 | 告诉人和工具字段类型 |
| `field(default_factory=list)` | 可变默认值 | 独立 list | 避免多个对象共享同一个 list |
| `@classmethod` | dict / 外部数据 | 对象 | 常用于 `from_dict` |
| `asdict(obj)` | dataclass 对象 | dict | 输出到 JSON/日志 |

## What

普通 class：

```python
class Record:
    def __init__(self, name, value):
        self.name = name
        self.value = value
```

dataclass：

```python
from dataclasses import dataclass

@dataclass
class Record:
    name: str
    value: float

record = Record(name="item_a", value=10.0)
print(record)
```

它们都能创建对象。dataclass 更适合“主要保存结构化数据”的类。

## Why

当对象字段比较固定时，dataclass 能减少重复代码，并让结构更清楚。

它适合：

- 配置对象。
- 数据记录对象。
- API 输入输出对象。
- LLM/Agent 的结构化结果。
- Quant 参数和指标结果。

## How：正规对象边界

```text
raw dict
  ↓
from_dict 校验和转换
  ↓
dataclass 对象
  ↓
方法计算
  ↓
to_dict / asdict
  ↓
JSON 保存
```

## 参数拆解方法

### `@dataclass`

| 部分 | 含义 |
| --- | --- |
| `@dataclass` | 装饰器，让类自动获得 `__init__`、`repr` 等方法 |
| `name: str` | 字段名和类型提示 |
| `tags: list[str]` | list 字段，注意默认值 |
| `field(default_factory=list)` | 每个对象独立创建一个空 list |

### `@classmethod`

| 部分 | 含义 |
| --- | --- |
| `cls` | 当前类本身 |
| `from_dict` | 从 dict 创建对象的常用命名 |
| `return cls(...)` | 返回这个类的新对象 |

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| list 默认值写成 `[]` | 多个对象共享 list | 用 `field(default_factory=list)` |
| 类型标注当强制校验 | 运行时仍可能传错 | 在 `from_dict` 里转换和检查 |
| `asdict` 忘记导入 | `NameError` | `from dataclasses import asdict` |
| from_dict 不处理缺字段 | 后面才报错 | 在入口统一校验 |

## Future Usage

- NumPy/pandas 里用 dataclass 保存分析配置。
- Matplotlib 里用 dataclass 保存图表参数。
- Quant 里用 dataclass 保存策略参数。
- LLM/Agent 里用 dataclass 保存结构化输入输出。

## 今日强化题（带具体代码）

### 强化题 1：复现 dataclass 流程

任务：运行下面代码。

验收：生成 `outputs/day015/dataclass_records.json`。

### 强化题 2：替换输入

任务：新增一条 raw dict，并添加 tags。

### 强化题 3：边界检查

任务：把 value 改成无法转成数字的字符串。

### 强化题 4：总结

任务：写 3 句话说明普通 class 和 dataclass 的区别。

### 参考代码：`main.py`

```python
from dataclasses import dataclass, field, asdict
from pathlib import Path
import json

DAY = 15
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


@dataclass
class Record:
    name: str
    value: float
    group: str = "default"
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data):
        if not data.get("name"):
            raise ValueError("name is required")
        try:
            value = float(data.get("value"))
        except (TypeError, ValueError):
            raise ValueError("value must be numeric")
        tags = data.get("tags", [])
        if not isinstance(tags, list):
            raise ValueError("tags must be list")
        return cls(
            name=data["name"],
            value=value,
            group=data.get("group", "default"),
            tags=tags,
        )

    def is_high_value(self, threshold):
        return self.value >= threshold

    def to_dict(self, threshold):
        output = asdict(self)
        output["high_value"] = self.is_high_value(threshold)
        return output


def build_records(raw_items):
    records = []
    errors = []
    for index, item in enumerate(raw_items):
        try:
            records.append(Record.from_dict(item))
        except ValueError as exc:
            errors.append({"index": index, "item": item, "error": str(exc)})
    return records, errors


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    raw_items = [
        {"name": "item_a", "value": "10", "group": "A", "tags": ["clean"]},
        {"name": "item_b", "value": 18, "group": "A", "tags": ["important"]},
        {"name": "item_c", "value": "bad", "group": "B"},
    ]
    records, errors = build_records(raw_items)
    values = [record.value for record in records]
    threshold = sum(values) / len(values)
    payload = {
        "topic": "dataclass and typed object boundary",
        "threshold": threshold,
        "items": [record.to_dict(threshold) for record in records],
        "errors": errors,
    }
    (OUT / "dataclass_records.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day15：class 正规化与 dataclass

dataclass 解决什么重复：
类型标注能做什么、不能做什么：
from_dict 的作用：
to_dict 的作用：
基础 Python 到这里结束，我最稳的 5 个能力：
```
