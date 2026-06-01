# Day08 - 面向对象基础与 dataclass

学习定位：在函数和字典之后学习对象。今天只写简单类和 dataclass，不做复杂设计模式。

## 今日只允许使用

- class
- __init__
- 属性
- 方法
- dataclass

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
class Position:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares

pos = Position("AAPL", 3)
print(pos.symbol)
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

1. 写一个只有两个属性的 class。
2. 创建一个对象并打印属性。
3. 给 class 加一个方法。
4. 用 dataclass 表示一条记录。
5. 把 dict 记录改成 dataclass。
6. 创建两个对象放进列表。
7. 记录一次属性名写错的问题。

## 题目驱动训练

### 参考资料

- [Python 官方教程](https://docs.python.org/3/tutorial/)

### 5 道基础巩固题

#### 1. 基础巩固 - 最小类

题目：写一个 Position 类。

讲解：类先理解属性。

```python
class Position:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares

pos = Position("AAPL", 3)
print(pos.symbol)
```

#### 2. 基础巩固 - 对象方法

题目：给 Position 加市值计算。

讲解：方法就是对象里的函数。

```python
class Position:
    def __init__(self, symbol, shares, price):
        self.symbol = symbol
        self.shares = shares
        self.price = price

    def value(self):
        return self.shares * self.price

pos = Position("AAPL", 3, 100)
print(pos.value())
```

#### 3. 基础巩固 - dataclass 记录

题目：用 dataclass 表示学习记录。

讲解：dataclass 适合纯数据。

```python
from dataclasses import dataclass

@dataclass
class LearningLog:
    topic: str
    minutes: int

log = LearningLog("函数", 60)
print(log.topic)
```

#### 4. 基础巩固 - 对象列表

题目：创建多个学习记录并求总分钟。

讲解：对象也可以放进列表。

```python
logs = [LearningLog("函数", 60), LearningLog("列表", 45)]
total = 0
for log in logs:
    total = total + log.minutes
print(total)
```

#### 5. 基础巩固 - 对象转文字

题目：给对象生成一句摘要。

讲解：练习属性读取。

```python
log = LearningLog("Python", 120)
print(f"学习 {log.topic}，{log.minutes} 分钟")
```
