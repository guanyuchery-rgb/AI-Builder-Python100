# Day14 - JSON 文件读写与嵌套结构

> 阶段二：Python 工程化基本功

## 学习定位

今天只学习一个核心主题：**json.load / json.dump：JSON 文件 <-> Python dict/list，并读懂嵌套路径**。

Day13 学的是字符串层面的 `loads / dumps`。今天升级到文件层面的 `load / dump`，并开始处理真实 JSON 最常见的嵌套结构。

## 前置知识

- 上一站：Day13 JSON loads / dumps
- 下一站：Day15 CSV vs JSON 结构选择
- 必须先会：dict/list、文件打开、`with`、`Path`、`.get()`。

## 认知地图

| 工具 | 输入 | 输出 | 适合什么 |
| --- | --- | --- | --- |
| `json.load(f)` | 文件对象 | Python dict/list | 从 `.json` 文件读取结构 |
| `json.dump(obj, f)` | Python dict/list + 文件对象 | `.json` 文件 | 把结构写到文件 |
| `data["items"][0]` | 嵌套 dict/list | 内层对象 | 按路径读取嵌套字段 |
| `dict.get(key, default)` | dict | 字段值或默认值 | 缺字段时不直接崩溃 |

## What

`load / dump` 和 `loads / dumps` 只差一个 `s`，但输入输出不同。

```text
loads: string -> Python object
dumps: Python object -> string

load: file object -> Python object
dump: Python object -> file object
```

记忆方法：带 `s` 的处理 string；不带 `s` 的处理 file。

## Why

真实项目里，JSON 通常不是只存在于一个字符串变量里，而是来自文件或 API。

例如：

- `config.json` 保存运行参数。
- `response.json` 保存 API 返回结果。
- `agent_trace.json` 保存 Agent 执行过程。
- `eval_cases.json` 保存 LLM 评估样例。

如果只会 `loads / dumps`，你还缺“长期保存和复查”的能力。`load / dump` 解决的是文件读写边界。

## How：从文件读写到嵌套路径

数据流是：

```text
Python dict/list
  ↓
json.dump(obj, f)
  ↓
本地 .json 文件
  ↓
json.load(f)
  ↓
Python dict/list
  ↓
按路径读取嵌套字段
```

### 最小写入文件

```python
import json
from pathlib import Path

path = Path("config.json")
config = {"metadata": {"source": "demo"}, "settings": {"language": "zh", "daily_hours": 4}}

with path.open("w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
```

### 最小读取文件

```python
with path.open("r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["settings"]["daily_hours"])
```

### 嵌套路径怎么读

```python
data["sessions"][0]["metrics"]["minutes"]
```

这条路径的意思是：

```text
data 是 dict
  -> 取 "sessions" 得到 list
  -> 取第 0 个元素得到 dict
  -> 取 "metrics" 得到 dict
  -> 取 "minutes" 得到数字
```

## 参数拆解方法

### `json.dump(obj, f, ensure_ascii=False, indent=2)`

| 参数 | 含义 | 你要问的问题 |
| --- | --- | --- |
| `obj` | Python dict/list | 里面有没有不能 JSON 化的对象，例如 Path、set、函数？ |
| `f` | 文件对象 | 是否用 `"w"` 模式和 `utf-8` 编码打开？ |
| `ensure_ascii=False` | 中文可读 | 学习日志、中文字段是否正常显示？ |
| `indent=2` | 缩进 | 人能不能直接读懂文件？ |
| 返回值 | `None` | 它直接写文件，不返回 JSON 字符串 |

### `json.load(f)`

| 部分 | 含义 | 易错点 |
| --- | --- | --- |
| `f` | 文件对象 | 必须是已经打开的 JSON 文件 |
| 返回值 | dict 或 list | 先 `print(type(data))` 再取字段 |
| 失败情况 | JSONDecodeError | 文件不是合法 JSON |
| 编码 | `encoding="utf-8"` | 中文文件建议固定写清楚 |

## 和旧知识的连接

| Day13 | Day14 | 升级点 |
| --- | --- | --- |
| JSON 字符串 | JSON 文件 | 从临时文本到长期保存 |
| `loads(text)` | `load(f)` | 输入从字符串变文件对象 |
| `dumps(obj)` | `dump(obj, f)` | 输出从字符串变文件 |
| dict/list | 嵌套路径 | 学会逐层进入结构 |
| `row.get(...)` | `dict.get(...)` | 缺字段时给默认值 |

## Common Errors

| 错误 | 表现 | 定位方法 |
| --- | --- | --- |
| 把 `dump` 当 `dumps` | 以为返回字符串，结果是 `None` | 记住 `dump` 直接写文件 |
| 文件不是合法 JSON | `JSONDecodeError` | 检查双引号、逗号、括号 |
| 顶层类型看错 | `TypeError` | 先打印 `type(data)` |
| 嵌套路径写错 | `KeyError` / `IndexError` | 每进入一层就打印一次 |
| 写入 Path/set | `TypeError: not JSON serializable` | 转成 str/list 后再保存 |

## Future Usage

- Data：保存字段字典、清洗配置、EDA 摘要。
- Quant：保存策略参数、回测配置、风险阈值。
- LLM：保存 prompt 配置、评估样例、模型输出。
- Agent：保存 memory、tool trace、human review 状态。

## 4 小时学习节奏

| 时间 | 做什么 | 产物 |
| --- | --- | --- |
| 30 分钟 | 对比 loads/dumps 和 load/dump | notes.md |
| 60 分钟 | 手打 JSON 文件读写 | main.py |
| 45 分钟 | 逐层打印嵌套路径 | trace.md |
| 45 分钟 | 制造缺字段和坏 JSON | errors.md |
| 40 分钟 | 写迁移说明 | review.md |

## 今日强化题（带具体代码）

### 强化题 1：复现最小案例

任务：复制下面代码到 `main.py` 并运行。

验收：生成 `outputs/day014/config.json` 和 `report.json`。

### 强化题 2：替换输入

任务：新增一个 `session`，包含 `topic`、`minutes`、`errors`。

验收：汇总结果变化。

### 强化题 3：边界检查

任务：删除某个 session 的 `metrics` 字段。

验收：程序不会直接崩溃，坏记录进入 `skipped`。

### 强化题 4：结果保存

任务：把清洗后的 summary 保存为 JSON 文件。

验收：文件可读、有缩进、中文正常。

### 强化题 5：迁移说明

任务：写 3 句话说明嵌套 JSON 为什么是 API、LLM、Agent 的基础。

### 参考代码：`main.py`

```python
from pathlib import Path
import json

DAY = 14
TOPIC = "JSON load / dump and nested data"
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs" / f"day{DAY:03d}"


def ensure_dirs():
    OUT.mkdir(parents=True, exist_ok=True)


def write_config(path: Path):
    config = {
        "metadata": {"source": "demo", "schema_version": 1},
        "sessions": [
            {"day": 13, "topic": "json basics", "metrics": {"minutes": 50, "errors": 1}},
            {"day": 14, "topic": "nested json", "metrics": {"minutes": 40, "errors": 0}},
            {"day": 14, "topic": "bad session"},
        ],
    }
    with path.open("w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def load_and_summarize(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    valid = []
    skipped = []
    for index, session in enumerate(data.get("sessions", [])):
        metrics = session.get("metrics")
        if not isinstance(metrics, dict):
            skipped.append({"index": index, "session": session, "reason": "missing metrics"})
            continue
        valid.append({
            "day": session.get("day"),
            "topic": session.get("topic"),
            "minutes": metrics.get("minutes", 0),
            "errors": metrics.get("errors", 0),
        })
    return {
        "topic": TOPIC,
        "source": data.get("metadata", {}).get("source", "unknown"),
        "valid_count": len(valid),
        "total_minutes": sum(item["minutes"] for item in valid),
        "total_errors": sum(item["errors"] for item in valid),
        "skipped": skipped,
    }


def main():
    ensure_dirs()
    config_path = OUT / "config.json"
    write_config(config_path)
    summary = load_and_summarize(config_path)
    with (OUT / "report.json").open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day14：JSON 文件读写与嵌套结构

load 和 loads 的区别：
dump 和 dumps 的区别：
我今天读懂的一条嵌套路径：
我制造的缺字段错误：
未来会在哪个 IC 使用：
```
