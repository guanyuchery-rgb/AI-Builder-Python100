# Day74 - 项目三Agent日志与评估

学习定位：记录工具调用日志并建立小型评估集。

## 2小时安排

- 15 分钟：读定位和最小代码。
- 25 分钟：手打一遍最小案例。
- 70 分钟：完成 5 道递进题。
- 10 分钟：记录 Debug、边界情况和项目迁移点。

## 核心知识点：Agent Project Build

### 定义

今天的主题是把一个小能力固定成可复用、可测试、可迁移的工程单元。

### 为什么存在

长期学习不能只靠临时理解。每个能力都要能进入项目：有输入、有输出、有失败处理、有复盘入口。

### 最小案例

```python
def choose_next(state: dict) -> str:
    if state.get("error"):
        return "ask_human"
    if not state.get("done"):
        return "run_next_tool"
    return "write_summary"
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

- [OpenAI API docs](https://platform.openai.com/docs/)
- [Pydantic docs](https://docs.pydantic.dev/latest/)
- [pytest docs](https://docs.pytest.org/)

### 今日产出

一个和“项目三Agent日志与评估”相关的可复用函数、脚本或项目模块。

### 5 道递进题

#### 1. Easy - Tool Schema

题目：描述工具名、用途、必填参数。

讲解：Agent 调工具前，需要知道边界。

```python
def tool_schema() -> dict:
    return {"name": "calculate_metric", "required": ["values"], "description": "calculate simple metric"}
```

#### 2. Easy - 参数校验

题目：缺少必填参数时返回错误。

讲解：工具不要因为坏输入直接崩溃。

```python
def validate_payload(payload: dict, required: list[str]) -> list[str]:
    return [key for key in required if key not in payload]
```

#### 3. Medium - Tool Result

题目：统一成功和失败输出。

讲解：统一结构方便 Agent 继续决策。

```python
def tool_result(ok: bool, data=None, error: str | None = None) -> dict:
    return {"ok": ok, "data": data, "error": error}
```

#### 4. Medium - 下一步选择

题目：根据工具结果决定下一步。

讲解：Agent 循环的核心是状态判断。

```python
def choose_next(result: dict) -> str:
    if not result["ok"]:
        return "ask_human"
    return "continue"
```

#### 5. Hard - Agent-ready Tool

题目：把校验、计算、结果包装到一个函数。

讲解：这是后续 Agent 项目的基本单元。

```python
def metric_tool(payload: dict) -> dict:
    errors = validate_payload(payload, ["values"])
    if errors:
        return tool_result(False, error="missing: " + ",".join(errors))
    values = payload["values"]
    return tool_result(True, data={"mean": sum(values) / len(values)})
```
