# Day20 - Quant / LLM / Agent 综合小项目

学习定位：只组合前 19 天学过的能力，做一个 CSV -> 指标 -> Markdown prompt 的小项目。

## 今日只允许使用

- 函数
- list/dict
- CSV
- JSON/Markdown
- 测试/日志
- prompt 字符串

## 今日目标

- 能独立手打当天最小代码。
- 能说清输入、输出和可能报错的位置。
- 做题时不使用后面天数才学的知识。
- 把一个错误记录到 Debug 日志。

## 知识点 1：今日边界

### 定义

只使用当天及之前出现过的知识。

### 为什么存在

它让当前阶段的代码更容易看懂、运行和复查。
## 知识点 2：工程习惯

### 定义

每个小能力都要有输入、输出和可复查结果。

### 为什么存在

它让当前阶段的代码更容易看懂、运行和复查。

## 最小案例

```python
returns = [0.01, -0.02, 0.03]
avg = sum(returns) / len(returns)
prompt = f"请解释平均收益：{avg:.2%}"
print(prompt)
```

## 常见错误

- 还没学到的写法先不要硬用。
- 代码能跑但解释不清输入输出。
- 报错后直接问答案，没有先缩小到最小案例。

## Debug 日志

- 先记录报错类型。
- 再记录触发它的最小代码。
- 最后记录修复方式。

## Quant / LLM / Agent 关联

今天只建立最小基础，不提前做复杂项目。Quant、LLM、Agent 的连接点只作为方向提醒，不作为做题要求。

## 复习检查

- [ ] 我没有使用后面才学的知识点。
- [ ] 我能从头手打一遍最小案例。
- [ ] 我能解释每一行代码。
- [ ] 我完成了 7 道简单路线题和 5 道基础巩固题。

## 简单路线 7 题（不超前）

只用今天及之前学过的能力。做不出来时，先回看当天最小案例，不跳到后面知识。

1. 准备 3 个收益率数字。
2. 计算平均收益。
3. 把结果保存到 dict。
4. 生成一段 prompt 字符串。
5. 把 prompt 写入 md 文件。
6. 给平均收益函数写 assert。
7. 记录这个小项目的输入和输出。

## 题目驱动训练

### 参考资料

- [Python 官方教程](https://docs.python.org/3/tutorial/)

### 5 道基础巩固题

#### 1. 基础巩固 - 平均收益

题目：计算收益率列表平均值。

讲解：综合 Day05/Day06。

```python
def average_return(returns):
    return sum(returns) / len(returns)

returns = [0.01, -0.02, 0.03]
print(average_return(returns))
```

#### 2. 基础巩固 - 指标 dict

题目：把指标保存成字典。

讲解：结构化结果方便保存。

```python
returns = [0.01, -0.02, 0.03]
metrics = {"avg_return": average_return(returns), "count": len(returns)}
print(metrics)
```

#### 3. 基础巩固 - 生成 prompt

题目：让 LLM 审查指标。

讲解：LLM 只解释，不替你计算。

```python
metrics = {"avg_return": 0.01, "count": 3}
prompt = f"请解释这组指标：{metrics}"
print(prompt)
```

#### 4. 基础巩固 - 写报告

题目：把 prompt 写成 md。

讲解：项目结果要落盘。

```python
from pathlib import Path

Path("llm_prompt.md").write_text(prompt, encoding="utf-8")
```

#### 5. 基础巩固 - 小测试

题目：测试 average_return。

讲解：综合项目也要测核心函数。

```python
assert average_return([0.1, 0.2]) == 0.15000000000000002
```
