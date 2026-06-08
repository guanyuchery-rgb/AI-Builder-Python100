# Day16 - NumPy 数组基础

> 阶段三：数据分析三大库

## 学习定位

今天开始数据分析库。第一站是 **NumPy**：它把 Python list 升级成可以高速计算的数组。

## 认知地图

| 工具 | 输入 | 输出 | 用途 |
| --- | --- | --- | --- |
| `np.array()` | list | ndarray | 创建数组 |
| `.shape` | ndarray | 维度 | 看行列结构 |
| `.dtype` | ndarray | 数据类型 | 看数字类型 |
| `.sum()` / `.mean()` | ndarray | 数值 | 汇总 |
| 切片 | ndarray | 子数组 | 取部分数据 |

## What

NumPy 数组不是普通 list。list 更像容器，NumPy array 更像数学对象。

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr + 10)  # [11 12 13]
```

list 不能这样直接做向量计算。

## Why

数据分析、机器学习、深度学习和量化都离不开矩阵和向量。NumPy 是这些库的底层基础。

你先要掌握三件事：

1. 数组长什么样：`.shape`。
2. 数组里面是什么类型：`.dtype`。
3. 数组如何整体计算：向量化。

## How：list -> array -> 计算

```text
Python list
  ↓
np.array
  ↓
ndarray
  ↓
shape / dtype / slicing
  ↓
sum / mean / min / max
```

## 参数拆解方法

### `np.array(data, dtype=float)`

| 参数 | 含义 | 注意 |
| --- | --- | --- |
| `data` | list 或嵌套 list | 每一行长度最好一致 |
| `dtype` | 数组元素类型 | 数据分析常用 float |
| 返回值 | ndarray | 后续可做向量计算 |

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 行长度不一致 | 创建 object 数组或报错 | 保证二维数据列数一致 |
| 字符串混入数字 | dtype 变成字符串 | 先清洗再转换 |
| 轴理解错 | 汇总方向错 | `axis=0` 按列，`axis=1` 按行 |

## 今日强化题（带具体代码）

### 强化题 1：创建一维和二维数组

验收：输出 shape、dtype、列均值。

### 强化题 2：替换输入

任务：新增一行二维数据。

### 强化题 3：边界检查

任务：尝试加入字符串，解释为什么要先清洗。

### 参考代码：`main.py`

```python
from pathlib import Path
import json
import numpy as np

DAY = 16
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


def describe_array(matrix):
    arr = np.array(matrix, dtype=float)
    return {
        "shape": list(arr.shape),
        "dtype": str(arr.dtype),
        "column_sum": arr.sum(axis=0).round(4).tolist(),
        "column_mean": arr.mean(axis=0).round(4).tolist(),
        "first_row": arr[0].tolist(),
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    matrix = [
        [10, 1.2, 0],
        [12, 1.5, 1],
        [9, 1.1, 0],
        [15, 1.8, 1],
    ]
    payload = {"topic": "numpy array basics", "summary": describe_array(matrix)}
    (OUT / "numpy_array_summary.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day16：NumPy 数组基础

ndarray 和 list 的区别：
shape 表示什么：
dtype 表示什么：
axis=0 和 axis=1 的区别：
```
