# Day14 - class、对象、方法与 self

> 阶段二：基础 Python 收束：面向对象

## 学习定位

今天正式进入 class。目标不是背面向对象术语，而是看懂：**class 是模板，对象是实例，属性保存状态，方法保存行为，self 代表当前对象。**

## 认知地图

| 概念 | 写法 | 含义 |
| --- | --- | --- |
| class | `class Record:` | 定义对象模板 |
| object | `Record(...)` | 创建具体对象 |
| attribute | `self.value` | 对象自己的数据 |
| method | `def is_valid(self):` | 对象自己的行为 |
| self | `self` | 当前这个对象 |
| constructor | `__init__` | 创建对象时初始化状态 |

## What

dict 可以保存数据：

```python
row = {"name": "item_a", "value": 10}
```

class 可以把数据和行为放在一起：

```python
class Record:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def is_valid(self):
        return self.value >= 0
```

## Why

只用 dict 时，字段和行为分散：

- 字段名容易写错。
- 校验逻辑到处复制。
- 相关函数不知道应该放哪里。
- 程序变大后边界不清楚。

class 的作用是把“某类数据的结构和行为”集中到一个地方。

## How：从 JSON/dict 进入 class

```text
dict 数据
  ↓
__init__ 初始化字段
  ↓
self 保存状态
  ↓
方法读取 self 完成计算
  ↓
to_dict 输出回 JSON
```

### 最小正规 class

```python
class Record:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def is_valid(self):
        return isinstance(self.value, (int, float))
```

## 对象拆解方法

| 代码 | 拆解 |
| --- | --- |
| `Record("item_a", 10)` | 调用类名，创建对象 |
| `__init__(self, name, value)` | 创建对象时自动执行 |
| `self.name = name` | 把参数保存到当前对象 |
| `record.is_valid()` | 调用对象方法 |
| `type(record).__name__` | 查看对象所属类 |

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 忘记 `self` | `TypeError` | 实例方法第一个参数写 `self` |
| 写成 `_init_` | 初始化不执行 | 前后都是两个下划线 |
| 属性名不一致 | `AttributeError` | 统一用 `self.value` |
| 方法忘记 return | 得到 `None` | 方法输出要明确 |
| 把类当对象 | 没有实例状态 | 用 `Record(...)` 创建对象 |

## 今日强化题（带具体代码）

### 强化题 1：复现 class 完整流程

任务：运行下面代码。

验收：生成 `outputs/day014/class_records.json`。

### 强化题 2：替换输入

任务：新增一条 raw dict，再转成对象。

### 强化题 3：边界检查

任务：把 value 改成字符串，确认错误进入 errors。

### 参考代码：`main.py`

```python
from pathlib import Path
import json

DAY = 14
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


class Record:
    def __init__(self, name, value, group="default"):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.value = value
        self.group = group

    def is_valid(self):
        return isinstance(self.value, (int, float)) and self.value >= 0

    def score(self, baseline):
        if not self.is_valid() or baseline == 0:
            return None
        return round(self.value / baseline, 4)

    def to_dict(self, baseline):
        return {
            "class": type(self).__name__,
            "name": self.name,
            "group": self.group,
            "value": self.value,
            "valid": self.is_valid(),
            "score": self.score(baseline),
        }


def build_records(raw_items):
    records = []
    errors = []
    for index, item in enumerate(raw_items):
        try:
            record = Record(item.get("name"), item.get("value"), item.get("group", "default"))
        except ValueError as exc:
            errors.append({"index": index, "item": item, "error": str(exc)})
            continue
        records.append(record)
    return records, errors


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    raw_items = [
        {"name": "item_a", "value": 10, "group": "A"},
        {"name": "item_b", "value": 15, "group": "A"},
        {"name": "item_c", "value": "bad", "group": "B"},
        {"name": "", "value": 8, "group": "B"},
    ]
    records, errors = build_records(raw_items)
    valid_values = [record.value for record in records if record.is_valid()]
    baseline = sum(valid_values) / len(valid_values)
    payload = {
        "topic": "class object method self",
        "baseline": baseline,
        "items": [record.to_dict(baseline) for record in records],
        "errors": errors,
    }
    (OUT / "class_records.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day14：class、对象、方法与 self

class 是什么：
对象是什么：
self 代表什么：
__init__ 做什么：
方法和函数的区别：
```
