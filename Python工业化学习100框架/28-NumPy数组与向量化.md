# Day28 - NumPy数组与向量化

学习定位：用 NumPy 做批量数值计算，减少手写循环。

## 2小时安排

- 15 分钟：读定位和最小代码。
- 25 分钟：手打一遍最小案例。
- 70 分钟：完成 5 道递进题。
- 10 分钟：记录 Debug、边界情况和项目迁移点。

## 核心知识点：Vectorization

### 定义

Vectorization 是把今天能力固定成可复用模块的方式。

### 为什么存在

它让代码从“这次能跑”变成“下次能复查、能迁移、能被项目调用”。

### 最小案例

```python
import numpy as np

prices = np.array([100, 102, 101, 105], dtype=float)
returns = prices[1:] / prices[:-1] - 1
print(returns.mean(), returns.std())
```

### 常见错误

- 直接把逻辑写在 notebook 或临时脚本里。
- 输入字段没有校验。
- 结果只 print，不保存。
- 失败原因没有记录。

### 工程应用

- 数据清洗和指标计算。
- Quant research 小项目。
- LLM report assistant。
- Agent tool prototype。

### 未来扩展

- 增加测试。
- 增加 README 运行说明。
- 增加 CLI/API/UI 入口。
- 接入真实项目数据。

## Debug 日志

- 路径错误：先打印当前工作目录。
- 类型错误：先检查输入字段和 dtype。
- 结果异常：先缩小到 3 行样例数据。
- 依赖错误：记录安装命令和 Python 版本。

## 面试 / 项目角度

能说明今天代码的输入、输出、失败情况，以及它如何进入一个真实项目。

## Quant 关联

大规模指标计算需要向量化思维。

## LLM / Agent 关联

Agent tool 内部可以用 NumPy 算，输出仍保持简单 dict。

## 复习检查

- [ ] 我能独立解释今天能力解决什么问题。
- [ ] 我能手打一遍最小案例。
- [ ] 我能完成 5 道递进题。
- [ ] 我能说清输入、输出和失败情况。
- [ ] 我知道它如何迁移到 Quant / LLM / Agent 项目。

## 简单路线 7 题（不超前）

只用今天及之前学过的能力。做不出来时，先回看当天最小案例，不跳到后面知识。

1. 为今天主题新建一个最小 `.py` 文件。
2. 写一个只处理 3 行样例数据的版本。
3. 打印输入字段和输出字段。
4. 把核心逻辑整理成一个函数。
5. 保存一个 JSON 或 Markdown 结果。
6. 写 1 条 Debug 记录。
7. 写一句它如何进入 Quant / LLM / Agent 项目。
## 题目驱动训练

### 参考题 / 资料

- [NumPy docs](https://numpy.org/doc/stable/)
- [Python Docs](https://docs.python.org/3/)
- [LeetCode 53 - Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

### 今日产出

收益率数组和统计值。

### 5 道递进题

#### 1. Easy - 数组输入校验

题目：把 list 转成 float array，并拒绝空输入。

讲解：数值计算前先保护边界。

```python
import numpy as np

def to_float_array(values: list[float]) -> np.ndarray:
    if not values:
        raise ValueError("values cannot be empty")
    return np.array(values, dtype=float)
```

#### 2. Easy - 基础统计

题目：返回均值、标准差、最小值、最大值。

讲解：先用清楚指标描述数据。

```python
import numpy as np

def basic_stats(values: list[float]) -> dict:
    arr = to_float_array(values)
    return {"mean": float(arr.mean()), "std": float(arr.std(ddof=1)), "min": float(arr.min()), "max": float(arr.max())}
```

#### 3. Medium - 相关系数

题目：计算两个序列的相关系数。

讲解：相关性需要长度一致，且不是因果。

```python
import numpy as np

def correlation(x: list[float], y: list[float]) -> float:
    if len(x) != len(y):
        raise ValueError("x and y must have same length")
    return float(np.corrcoef(to_float_array(x), to_float_array(y))[0, 1])
```

#### 4. Medium - 标准化

题目：把数据转成 z-score。

讲解：很多模型和因子比较前需要统一尺度。

```python
import numpy as np

def zscore(values: list[float]) -> list[float]:
    arr = to_float_array(values)
    std = arr.std(ddof=1)
    if std == 0:
        return [0.0 for _ in values]
    return ((arr - arr.mean()) / std).tolist()
```

#### 5. Hard - 指标包

题目：组合统计、相关性和标准化输出。

讲解：项目中更常用的是指标包，而不是单个函数。

```python
def build_metric_pack(values: list[float], benchmark: list[float]) -> dict:
    return {
        "stats": basic_stats(values),
        "corr_to_benchmark": correlation(values, benchmark),
        "zscore_tail": zscore(values)[-3:],
    }
```
