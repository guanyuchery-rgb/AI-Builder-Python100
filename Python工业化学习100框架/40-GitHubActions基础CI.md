# Day40 - GitHubActions基础CI

学习定位：让 GitHub 自动跑测试，建立项目底线。

## 2小时安排

- 15 分钟：读定位和最小代码。
- 25 分钟：手打一遍最小案例。
- 70 分钟：完成 5 道递进题。
- 10 分钟：记录 Debug、边界情况和项目迁移点。

## 核心知识点：Testing and CI

### 定义

今天的主题是把一个小能力固定成可复用、可测试、可迁移的工程单元。

### 为什么存在

长期学习不能只靠临时理解。每个能力都要能进入项目：有输入、有输出、有失败处理、有复盘入口。

### 最小案例

```python
def add(a: int, b: int) -> int:
    return a + b

def test_add():
    assert add(2, 3) == 5
```

### 常见错误

- 只在临时脚本里跑通，没有沉淀成函数。
- 输入字段没有校验，结果出了错才发现。
- 只 print 结果，不保存中间产物。
- 没有 README、测试或 Debug 记录，几天后难以接上。

### 工程应用

- 数据清洗和指标计算。
- Quant research 小项目。
- LLM report assistant。
- Agent tool prototype。
- 个人作品集沉淀。

### 未来扩展

- 增加单元测试。
- 增加 CLI/API/UI 入口。
- 接入真实数据。
- 写入项目 README 和复盘文档。

## Debug 日志

- 路径错误：先打印当前工作目录。
- 类型错误：先检查输入字段和 dtype。
- 结果异常：先缩小到 3 行样例数据。
- 依赖错误：记录安装命令和 Python 版本。

## 面试 / 项目角度

能说明今天代码的输入、输出、失败情况，以及它如何进入一个真实项目。

## Quant 关联

这一天服务于 Quant 学习：让数据、指标、回测和报告更可复现。

## LLM / Agent 关联

这一天服务于 LLM/Agent 学习：明确输入、输出、失败情况和可审查边界。

## 复习检查

- [ ] 我能独立解释今天能力解决什么问题。
- [ ] 我能手打一遍最小案例。
- [ ] 我能完成 5 道递进题。
- [ ] 我能说清输入、输出和失败情况。
- [ ] 我知道它如何迁移到 Quant / LLM / Agent 项目。

## 题目驱动训练

### 参考题 / 资料

- [pytest docs](https://docs.pytest.org/)
- [Python Docs](https://docs.python.org/3/)
- [GitHub Actions docs](https://docs.github.com/actions)

### 今日产出

一个和“GitHubActions基础CI”相关的可复用函数、脚本或项目模块。

### 5 道递进题

#### 1. Easy - 标准化输入

题目：把原始 dict 转成统一字段。

讲解：统一字段名，后续函数才稳定。

```python
def normalize_row(raw: dict) -> dict:
    return {"name": str(raw.get("name", "")).strip(), "value": float(raw.get("value", 0) or 0), "tag": str(raw.get("tag", "default"))}
```

#### 2. Easy - 校验输入

题目：返回错误列表，而不是直接崩溃。

讲解：错误要可复盘。

```python
def validate_row(row: dict) -> list[str]:
    errors = []
    if not row.get("name"):
        errors.append("name is required")
    if row.get("value", 0) < 0:
        errors.append("value must be non-negative")
    return errors
```

#### 3. Medium - 批量汇总

题目：按 tag 汇总 value。

讲解：这是数据项目和日志分析的通用动作。

```python
from collections import defaultdict

def summarize_rows(rows: list[dict]) -> dict[str, float]:
    summary = defaultdict(float)
    for row in rows:
        summary[row["tag"]] += row["value"]
    return dict(summary)
```

#### 4. Medium - 保存结果

题目：把 summary 保存成 JSON。

讲解：结果落盘，第二天才能继续。

```python
import json
from pathlib import Path

def save_summary(path: str, summary: dict) -> None:
    Path(path).write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
```

#### 5. Hard - Tool 化

题目：输入原始 rows，返回 ok/data/errors。

讲解：这是 Agent-ready 的最小工程形状。

```python
def summary_tool(rows: list[dict]) -> dict:
    clean_rows = [normalize_row(row) for row in rows]
    errors = [error for row in clean_rows for error in validate_row(row)]
    if errors:
        return {"ok": False, "errors": errors}
    return {"ok": True, "data": summarize_rows(clean_rows)}
```
