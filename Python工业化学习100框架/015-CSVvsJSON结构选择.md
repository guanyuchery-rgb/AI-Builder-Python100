# Day15 - CSV vs JSON 结构选择

> 阶段二：Python 工程化基本功

## 学习定位

今天只学习一个核心主题：**什么时候用 CSV，什么时候用 JSON**。

Day11-12 你学了 CSV，Day13-14 你学了 JSON。今天不是再背 API，而是建立“格式选择能力”：同一份信息，为什么有时保存成表格，有时保存成嵌套结构。

## 前置知识

- 上一站：Day14 JSON 文件读写与嵌套结构
- 下一站：Day16 argparse 与命令行参数
- 必须先会：CSV reader/writer、DictReader/DictWriter、JSON load/dump、dict/list。

## 认知地图

| 格式 | 更像什么 | 适合什么 | 不适合什么 |
| --- | --- | --- | --- |
| CSV | 二维表 | 多条同结构记录、批量分析、Excel/Pandas | 深层嵌套、复杂配置 |
| JSON | dict/list 组合 | 配置、API 响应、嵌套日志、LLM/Agent 输出 | 大型二维数值表 |

一个非常实用的判断：

```text
每条记录字段都一样 -> 优先 CSV
字段里还有列表/dict -> 优先 JSON
```

## What

CSV 和 JSON 都是结构化数据格式，但结构表达能力不同。

CSV 强在“行列稳定”：

```text
day,topic,minutes
11,csv,35
12,dict csv,45
```

JSON 强在“层级清楚”：

```json
{
  "learner": "Claire",
  "sessions": [
    {"day": 11, "topic": "csv", "metrics": {"minutes": 35}}
  ]
}
```

## Why

格式选错，会让后面的代码变难。

如果你用 CSV 保存嵌套结构，可能会把列表塞进一个单元格，后面解析很痛苦。

如果你用 JSON 保存大表格，Pandas 读取、筛选、分组会比 CSV 麻烦。

格式选择本质是在回答：

- 后面是谁读？人、Pandas、API、Agent，还是另一个脚本？
- 数据是二维表，还是嵌套对象？
- 未来更常做筛选聚合，还是读取配置和状态？

## How：用同一份学习记录做两种保存

数据流是：

```text
Python records
  ↓
如果每条记录字段一致 -> CSV
  ↓
如果要保存元信息、嵌套指标、配置 -> JSON
  ↓
读取后先做结构体检
```

### CSV 版本

```python
records = [
    {"day": 11, "topic": "csv", "minutes": 35},
    {"day": 12, "topic": "dict csv", "minutes": 45},
]
```

适合保存成 CSV，因为每条记录字段一致。

### JSON 版本

```python
payload = {
    "learner": {"name": "Claire", "background": "statistics"},
    "records": records,
    "summary": {"total_minutes": 80}
}
```

适合保存成 JSON，因为它除了记录列表，还有 learner 和 summary 这种元信息。

## 参数拆解方法

### `csv.DictWriter(f, fieldnames=records[0].keys())`

| 部分 | 含义 | 易错点 |
| --- | --- | --- |
| `records[0].keys()` | 从第一条记录取字段名 | 如果后面记录字段不一致，会丢字段或报错 |
| `fieldnames` | CSV 表头和列顺序 | 表格结构必须扁平 |
| `writerows(records)` | 批量写入 dict | 每个 dict 最好字段一致 |

### `json.dump(payload, f, ensure_ascii=False, indent=2)`

| 部分 | 含义 | 易错点 |
| --- | --- | --- |
| `payload` | 可以包含 dict/list 嵌套 | 不能包含 set、函数、Path 等不可序列化对象 |
| `f` | JSON 输出文件 | 用 `encoding="utf-8"` |
| `indent=2` | 人类可读 | 适合学习记录、配置、Agent trace |

## 和旧知识的连接

| 已学内容 | 今天怎么选择 |
| --- | --- |
| Day11 reader/writer | 适合最简单的行列读写 |
| Day12 DictReader/DictWriter | 适合有字段名的二维表 |
| Day13 loads/dumps | 适合字符串和 Python 对象互转 |
| Day14 load/dump | 适合长期保存嵌套结构 |
| Day16 argparse | 以后命令行参数可以读取 JSON 配置或 CSV 输入路径 |

## Common Errors

| 错误 | 表现 | 定位方法 |
| --- | --- | --- |
| CSV 里塞嵌套 dict | 单元格里是一大串字符串 | 如果字段值还是 dict/list，优先 JSON |
| JSON 里保存大表 | 后续分析不方便 | 如果每条记录字段一致，优先 CSV/Pandas |
| 字段不一致还写 CSV | 列缺失或报错 | 写前检查所有 `row.keys()` |
| 只保存结果不保存元信息 | 复盘不知道来源 | JSON 里加 `source/config/summary` |
| 忘记先体检 | 后面计算报错 | 读取后先打印类型、数量、第一条 |

## Future Usage

- Data：原始明细通常 CSV，数据字典和清洗配置通常 JSON。
- Quant：行情表通常 CSV，策略参数和实验摘要通常 JSON。
- LLM：评估集可用 CSV，模型输出和引用链更适合 JSON。
- Agent：tool trace、memory、workflow state 通常更适合 JSON。

## 4 小时学习节奏

| 时间 | 做什么 | 产物 |
| --- | --- | --- |
| 30 分钟 | 画 CSV vs JSON 判断表 | notes.md |
| 60 分钟 | 同一份 records 保存两种格式 | main.py |
| 45 分钟 | 制造字段不一致和嵌套字段 | errors.md |
| 45 分钟 | 读回两个文件并比较结构 | summary.json |
| 40 分钟 | 写未来迁移说明 | review.md |

## 今日强化题（带具体代码）

### 强化题 1：复现最小案例

任务：复制下面代码到 `main.py` 并运行。

验收：同时生成 `records.csv`、`payload.json`、`decision_report.json`。

### 强化题 2：替换输入

任务：新增字段 `tags`，它是一个 list。

验收：你能判断为什么 `tags` 更适合 JSON，不适合普通 CSV。

### 强化题 3：边界检查

任务：制造一条字段缺失记录。

验收：报告里能指出字段不一致。

### 强化题 4：结果保存

任务：把格式选择理由保存成 JSON 报告。

验收：以后不用重新跑代码也能复查选择理由。

### 强化题 5：迁移说明

任务：写 3 句话说明你的 Data / Quant / LLM / Agent 项目里分别会怎么选 CSV 或 JSON。

### 参考代码：`main.py`

```python
from pathlib import Path
import csv
import json

DAY = 15
TOPIC = "CSV vs JSON structure choice"
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs" / f"day{DAY:03d}"


def ensure_dirs():
    OUT.mkdir(parents=True, exist_ok=True)


def records_are_flat(records):
    bad_fields = []
    for index, row in enumerate(records):
        for key, value in row.items():
            if isinstance(value, (dict, list)):
                bad_fields.append({"index": index, "field": key, "type": type(value).__name__})
    return bad_fields


def write_csv(path: Path, records):
    fieldnames = ["day", "topic", "minutes"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in records:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def write_json(path: Path, payload):
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def main():
    ensure_dirs()
    records = [
        {"day": 11, "topic": "csv", "minutes": 35},
        {"day": 12, "topic": "dict csv", "minutes": 45},
        {"day": 13, "topic": "json", "minutes": 50, "tags": ["data", "agent"]},
    ]
    payload = {
        "learner": {"name": "Claire", "background": "statistics"},
        "records": records,
        "summary": {"total_minutes": sum(row.get("minutes", 0) for row in records)},
    }
    nested_fields = records_are_flat(records)
    write_csv(OUT / "records.csv", records)
    write_json(OUT / "payload.json", payload)
    report = {
        "topic": TOPIC,
        "csv_good_for": "flat rows with stable fields",
        "json_good_for": "nested metadata, config, API and Agent trace",
        "nested_fields_found": nested_fields,
        "decision": "use CSV for flat analysis table; use JSON for full payload",
    }
    write_json(OUT / "decision_report.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day15：CSV vs JSON 结构选择

什么情况优先 CSV：
什么情况优先 JSON：
我今天发现的嵌套字段：
我会如何保存 Data / Quant / LLM / Agent 的不同数据：
未来会在哪个 IC 使用：
```
