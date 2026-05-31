# Day01 - Python 环境与第一段程序

学习定位：不只是“能打印 Hello World”，而是理解 Python 程序如何运行，并从第一天开始建立可复现的学习环境。

## 今日目标

- 理解解释器、脚本、终端、编辑器、项目文件夹的关系。
- 能运行第一个 Python 文件。
- 建立稳定的学习目录，而不是到处散落 `.py` 文件。
- 学会用 AI 做解释、复盘和 Debug，而不是直接抄答案。


## 知识点 1：Python 程序如何运行

### 定义

Python 程序是文本文件，解释器读取这些文本，并按照 Python 语法执行。

### 为什么存在

文本代码方便阅读、搜索、版本管理和迁移，这是长期工程资产的基础。

### 最小案例

```python
print("你好，AI Builder")
print(2 + 3)
```

预期输出：

```text
你好，AI Builder
5
```

### 常见错误

- `SyntaxError`：引号、括号、冒号写错。
- `NameError`：用了还没定义的名字。
- 找不到文件：终端当前目录不是脚本所在目录。

### 工程应用

- 自动化脚本。
- 数据清洗脚本。
- Quant 指标计算。
- Agent 工具函数。

### 未来扩展

- 虚拟环境。
- `requirements.txt`。
- `README.md`。
- 测试和日志。

## 知识点 2：可复现学习环境

### 定义

可复现学习环境，是指半年后重新打开文件夹，还知道运行哪个文件、预期输出是什么、它为什么存在。

### 为什么存在

早期学习最容易产生一堆散文件，后来完全无法复用。稳定目录能把练习变成长期资产。

### 最小案例

```text
day01/
├── hello.py
└── notes.md
```

```python
# hello.py
message = "Python 学习从可复现的小例子开始。"
print(message)
```

### 常见错误

- 文件放在随机位置。
- 永远叫 `test.py`。
- 没写这个脚本的用途。

### 工程应用

每个未来项目都应该能回答：代码在哪里、数据在哪里、怎么运行、结果是什么。

### 未来扩展

- 项目 README。
- `.gitignore`。
- `src/`。
- `tests/`。

## AI 时代补充

写完代码后，可以这样问 AI：

```text
请作为 Python 导师审查这段初学者代码。
请说明：
1. 它做了什么。
2. 可能哪里会错。
3. 一个更简单版本。
4. 一个更工程化版本。
不要引入不必要的高级概念。
```


## Debug 日志

- 如果提示 `command not found: python`，尝试 `python3`。
- 如果找不到文件，用 `pwd` 看当前目录。
- 如果输出不对，把代码缩小到最小案例再检查。

## 面试角度

Python 是解释型、高级语言，常用于自动化、后端服务、数据分析、AI 工具和脚本开发。

## Quant 关联

Python 会成为读取价格、计算收益率、清洗数据、测试策略想法的主要工具。

## Agent 关联

Agent 的可靠性取决于工具函数的可靠性。Python 脚本是最小的可靠工具。

## 复习检查

- [ ] 我能从终端运行 `.py` 文件。
- [ ] 我知道文件保存在哪里。
- [ ] 我能解释解释器和脚本的关系。
- [ ] 我会让 AI 审查代码，而不是直接抄答案。

## 题目驱动训练

少读长讲义，直接做题。每题先手写，再对照注释版。

### 参考题 / 资料

- [LeetCode 2235 - Add Two Integers](https://leetcode.com/problems/add-two-integers/)
- [LeetCode 2413 - Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### 5 道递进题

#### 1. Easy - 学习名片输出

题目：打印学习者代号、方向、今日目标。

讲解：先确认脚本能运行，再谈复杂能力。

```python
# 输入: 变量 name / track / goal
# 输出: 一行可读的学习名片
name = "学习者"
track = "AI / Data / Quant"
goal = "用 Python 支撑 LLM、Agent 和量化项目"

print(f"{name} | {track} | {goal}")
```

#### 2. Easy - Add Two Integers

关联题：[LeetCode 2235](https://leetcode.com/problems/add-two-integers/)

题目：写函数返回两个整数之和。

讲解：函数要清楚输入和输出，不要只在函数里 `print`。

```python
# 输入: 两个 int
# 输出: 一个 int
# 边界: 负数、0、大整数都可以直接相加
def sum_two(a: int, b: int) -> int:
    return a + b

print(sum_two(2, 3))
```

#### 3. Medium - Smallest Even Multiple

关联题：[LeetCode 2413](https://leetcode.com/problems/smallest-even-multiple/)

题目：返回同时能被 `n` 和 `2` 整除的最小正整数。

讲解：先写最小规则，不急着套复杂公式。

```python
# 如果 n 是偶数，n 自己就是答案
# 如果 n 是奇数，2 * n 才能同时被 2 和 n 整除
def smallest_even_multiple(n: int) -> int:
    if n % 2 == 0:
        return n
    return n * 2
```

#### 4. Medium - 脚本入口 main

题目：写 `main()`，输出今天要做的三个动作。

讲解：`main()` 是以后 CLI、Agent tool、批处理脚本的统一入口。

```python
# main 只负责组织流程，具体逻辑以后再拆函数
def main() -> None:
    actions = ["读目标", "手打代码", "记录 Debug"]
    for action in actions:
        print(action)

# 只有直接运行这个文件时才执行 main
if __name__ == "__main__":
    main()
```

#### 5. Hard - 学习启动检查器

题目：给定任务清单，返回还没完成的项目。

讲解：这是最小版 checklist，也像 Agent 执行前的前置条件检查。

```python
# 输入: dict，key 是任务名，value 表示是否完成
# 输出: 未完成任务列表
def find_missing_tasks(tasks: dict[str, bool]) -> list[str]:
    missing = []
    for name, done in tasks.items():
        if not done:
            missing.append(name)
    return missing

tasks = {"打开 Obsidian": True, "完成 Day01": False, "记录问题": False}
print(find_missing_tasks(tasks))
```
