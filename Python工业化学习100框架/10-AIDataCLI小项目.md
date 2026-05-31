# Day10 - AI/Data CLI 小项目

学习定位：把前 9 天的基础能力组合成一个适合长期方向的小项目：命令行学习日志或数据汇总工具。

## 项目为什么重要

你的长期方向是 AI × 数据 × 系统，所以 Day10 要把前 9 天知识组合成一个小而实用的工具：

- 函数
- 分支
- 循环
- 集合类型
- dataclass
- CLI 输入输出
- 可复现项目结构
- AI 辅助审查

## 今日项目

构建一个 `learning_log_cli.py` 概念工具：记录学习条目，并按标签汇总学习时间。

暂时不需要数据库，不需要 Web，不需要大框架。目标是低维护、能运行、能扩展。

## 知识点 1：小项目结构

### 定义

小项目是把多个基础概念组合成一个有用工作流。

### 为什么存在

语法只有变成工具，才会真正留下来。

### 最小案例

```text
day10_learning_log/
├── learning_log_cli.py
└── README.md
```

### 常见错误

- 一开始就上框架。
- 逻辑没跑通就做界面。
- 所有代码堆在一个不可测试的大块里。

### 工程应用

- 学习记录器。
- 数据清洗器。
- Quant 指标计算器。
- Agent 任务检查器。

### 未来扩展

- 保存 JSON。
- 增加测试。
- 增加 Streamlit 页面。
- 未来接本地 embedding。

## 知识点 2：CLI 是长期工具入口

### 定义

CLI 是命令行界面，可以通过终端参数运行工具。

### 为什么存在

CLI 简单、可脚本化、可测试，是自动化和 Agent 工具的好基础。

### 最小案例

```python
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    print(f"你好，{args.name}")


if __name__ == "__main__":
    main()
```

### 常见错误

- CLI 接受参数但不验证。
- 脚本只打印，不返回可复用数据。
- 数据模型还不清楚就开始扩展功能。

### 工程应用

- 批处理脚本。
- 项目维护工具。
- 数据处理任务。
- Agent 可调用工具。

### 未来扩展

- `typer`。
- JSON 输入输出。
- 日志。
- 测试。

## 完整现代代码示例

```python
import argparse
from dataclasses import dataclass


@dataclass
class LearningItem:
    topic: str
    source: str
    minutes: int
    tag: str

    @property
    def is_deep_work(self) -> bool:
        return self.minutes >= 45


def summarize_items(items: list[LearningItem]) -> dict[str, int]:
    summary: dict[str, int] = {}
    for item in items:
        summary[item.tag] = summary.get(item.tag, 0) + item.minutes
    return summary


def build_demo_items() -> list[LearningItem]:
    return [
        LearningItem("Python 函数", "现代 Python Day06", 45, "Python"),
        LearningItem("SQL Join", "SQL 练习", 30, "SQL"),
        LearningItem("Agent 工具", "Agent 笔记", 50, "Agent"),
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="汇总学习条目")
    parser.add_argument("--tag", help="只查看某个标签")
    args = parser.parse_args()

    items = build_demo_items()
    summary = summarize_items(items)

    if args.tag:
        minutes = summary.get(args.tag, 0)
        print(f"{args.tag}: {minutes} 分钟")
        return

    for tag, minutes in summary.items():
        print(f"{tag}: {minutes} 分钟")


if __name__ == "__main__":
    main()
```

运行：

```bash
python3 learning_log_cli.py
python3 learning_log_cli.py --tag Python
```

## AI 时代补充

让 AI 做审查：

```text
请审查这个初学者 CLI 项目。
检查：
1. 半年后是否还能看懂？
2. 函数是否太大？
3. 数据模型是否清楚？
4. 下一步最小改进是什么？
不要添加 Web 框架。
```

让 AI 做测试设计：

```text
请为这个 CLI 的核心逻辑生成测试案例。
重点测试 summarize_items 和 tag 过滤。
暂时不要测试 argparse。
```


## Debug 日志

- `KeyError`：标签可能不存在时用 `.get()`。
- 汇总不对：在循环里打印每个 item。
- CLI 参数没生效：检查 `args.tag`。
- 太复杂：拆成数据模型、核心逻辑、CLI 边界。

## 面试角度

这个项目能展示基础工程能力：数据建模、函数、循环、条件、CLI 边界、可读结构。

## Quant 关联

同样模式可以汇总交易、收益、风险事件或研究记录。

## Agent 关联

同样模式可以成为 Agent 工具：输入条目、汇总、验证结果、返回结构化输出。

## 复习检查

- [ ] 我能解释小项目结构。
- [ ] 我能运行 CLI。
- [ ] 我能解释每个函数。
- [ ] 我能扩展 dataclass。
- [ ] 我能描述下一步最小改进。

## 简单路线 7 题（不超前）

只用今天及之前学过的能力。做不出来时，先回看当天最小案例，不跳到后面知识。

1. 用 class 或 dataclass 表示一条记录。
2. 给对象写一个返回金额的小方法。
3. 创建 2 个对象并打印字段。
4. 把 dict 改成数据对象。
5. 写一个列表保存多个对象。
6. 写一个汇总对象列表的函数。
7. 记录一次字段名写错的问题。
## 题目驱动训练

### 参考题 / 资料

- [Python argparse docs](https://docs.python.org/3/library/argparse.html)
- [Python json docs](https://docs.python.org/3/library/json.html)
- [LeetCode 1672 - Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/)

### 5 道递进题

#### 1. Easy - 解析学习条目

题目：把一行 `Python,45,code` 转成 dict。

讲解：CLI 项目的输入边界要先稳定。

```python
# 输入: topic,minutes,tag
# 输出: 标准 dict
def parse_learning_line(line: str) -> dict:
    topic, minutes, tag = [part.strip() for part in line.split(",")]
    return {"topic": topic, "minutes": int(minutes), "tag": tag}
```

#### 2. Easy - 汇总学习时间

题目：按 tag 汇总分钟数。

讲解：这和客户资产汇总、日志分类汇总是同一类问题。

```python
from collections import defaultdict

def summarize_minutes(items: list[dict]) -> dict[str, int]:
    summary = defaultdict(int)
    for item in items:
        summary[item["tag"]] += item["minutes"]
    return dict(summary)
```

#### 3. Medium - 按标签过滤

题目：只返回某个 tag 的学习记录。

讲解：过滤是数据产品最基础的交互能力。

```python
# tag 不匹配的行直接跳过
def filter_by_tag(items: list[dict], tag: str) -> list[dict]:
    return [item for item in items if item.get("tag") == tag]
```

#### 4. Medium - 写 JSON 报告

题目：把 summary 保存成 JSON 文件。

讲解：项目结果要能落盘，睡醒还能复盘。

```python
import json
from pathlib import Path

# ensure_ascii=False 保留中文可读性
def write_report(path: str, summary: dict[str, int]) -> None:
    Path(path).write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
```

#### 5. Hard - CLI 主流程

题目：组合 parse、filter、summary、report。

讲解：main 负责串流程，函数负责可测试逻辑。

```python
import argparse

# 这里只示范结构，真实项目可从文件读取 lines
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag")
    args = parser.parse_args()

    lines = ["Python,45,code", "SQL,30,data", "Agent,40,code"]
    items = [parse_learning_line(line) for line in lines]
    if args.tag:
        items = filter_by_tag(items, args.tag)
    print(summarize_minutes(items))
```
