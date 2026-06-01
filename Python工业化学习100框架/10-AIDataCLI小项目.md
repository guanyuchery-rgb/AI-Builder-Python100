# Day10 - AI/Data CLI 小项目

学习定位：把 Day01-Day09 能力串起来。今天才正式使用 argparse，做一个很小的命令行脚本。

## 今日只允许使用

- argparse
- 函数
- 列表
- 字典
- class/dataclass
- main

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
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--topic")
args = parser.parse_args()
print(args.topic)
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

1. 写一个接收 `--topic` 的 argparse 脚本。
2. 写一个接收 `--minutes` 的参数。
3. 把参数打印出来。
4. 把核心逻辑放进函数。
5. 用列表保存 2 条学习记录。
6. 按分钟汇总总时间。
7. 记录一次参数缺失问题。

## 题目驱动训练

### 参考资料

- [Python 官方教程](https://docs.python.org/3/tutorial/)

### 5 道基础巩固题

#### 1. 基础巩固 - 最小 argparse

题目：读取一个 topic 参数。

讲解：CLI 从这里开始。

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--topic", required=True)
args = parser.parse_args()
print(args.topic)
```

#### 2. 基础巩固 - 分钟参数

题目：读取整数分钟。

讲解：参数也有类型。

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--minutes", type=int, required=True)
args = parser.parse_args()
print(args.minutes)
```

#### 3. 基础巩固 - 核心函数

题目：把显示逻辑放进函数。

讲解：CLI 只负责拿输入。

```python
def build_message(topic, minutes):
    return f"学习 {topic}，{minutes} 分钟"

print(build_message("Python", 60))
```

#### 4. 基础巩固 - 学习记录列表

题目：保存两条记录并汇总。

讲解：复用 list 和 dict。

```python
logs = [{"topic": "Python", "minutes": 60}, {"topic": "SQL", "minutes": 30}]
total = 0
for log in logs:
    total = total + log["minutes"]
print(total)
```

#### 5. 基础巩固 - main 组合

题目：把 argparse 和函数放进 main。

讲解：小项目从结构清楚开始。

```python
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--minutes", type=int, required=True)
    args = parser.parse_args()
    print(build_message(args.topic, args.minutes))

if __name__ == "__main__":
    main()
```
