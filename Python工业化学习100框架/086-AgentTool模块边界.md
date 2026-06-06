# Day86 - Agent Tool 模块边界

> 阶段七：知识整合、复盘与长期维护

## 学习定位

理解 Agent tool 的输入、输出、错误和权限边界。

今天只讲知识、原理、API 边界、小型示例和 Debug 方法。

不做完整工程，不做系统搭建，不要求交付作品。

工程验证统一进入 `Industrial-Challenge/`。

## 前置知识

- 推荐前置：Day85
- 上一站：Day85
- 下一站：Day87

## 今日知识地图

```text
What：今天的概念是什么
  ↓
Why：为什么需要它
  ↓
How：最小流程怎么写
  ↓
Common Errors：最常见错误怎么定位
  ↓
Future Usage：未来在哪个 IC 或作品中使用
```

今日学习产物：`Tool 边界` 的一页 notes 或一个最小函数。

## What

Agent Tool 模块边界 是一个知识模块，不是工程任务。

它帮助你把前面学过的 Python、数据处理、LLM/Agent 或 Quant 知识整理成更清楚的输入、处理、输出和错误边界。

## Why

如果不先理解这个知识模块，后面做 IC 时容易出现三个问题：

- 不知道输入数据应该长什么样。
- 不知道函数或模块应该返回什么。
- 报错后只能反复试，不能定位是哪一层出了问题。

Day 主线先解决认知地图，IC 再验证工程能力。

## How

最小学习流程：

1. 写清输入是什么。
2. 写清输出是什么。
3. 写一个最小函数或最小流程。
4. 用 1-2 条虚拟样例跑通。
5. 记录一个常见错误和定位方法。

```python
# Day86 - Tool 边界 最小示例

def describe_boundary(input_data):
    if input_data is None:
        return {"ok": False, "error": "empty input"}

    return {
        "ok": True,
        "input_type": type(input_data).__name__,
        "next_step": "write a smaller test case",
    }

print(describe_boundary({"sample": "demo"}))
```

## Common Errors

| 错误 | 表现 | Debug 方法 |
| --- | --- | --- |
| 输入边界没写清 | 函数不知道接收什么 | 打印 `type()` 和样例 |
| 输出格式不稳定 | 后续代码接不上 | 固定返回 dict 或表格字段 |
| 一次写太大 | 当天超过 4 小时 | 拆到 IC，不塞进 Day |
| 只看概念不运行 | 以为懂了但不会改 | 保留一个最小可运行例子 |

## Future Usage

这个知识会在 IC 中继续验证：

- Quant 工程实践：IC31-IC40。
- LLM 工程实践：IC41-IC42、IC46-IC47。
- Agent 工程实践：IC43-IC45。
- 最终交付：IC48-IC50。

Day 负责理解，IC 负责做出来。

## 今日练习

1. 用 3 句话解释 `Agent Tool 模块边界`。
2. 写出它的输入、输出和错误边界。
3. 写一个最小函数或最小流程。
4. 用虚拟样例跑通一次。
5. 写一句：这个知识未来会放进哪个 IC。
