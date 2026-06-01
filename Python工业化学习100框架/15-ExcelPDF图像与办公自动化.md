# Day15 - 办公文件与自动化入门

学习定位：先不处理复杂 Excel/PDF，零基础阶段做文件清单、CSV 报告和 Markdown 输出。

## 今日只允许使用

- Path.iterdir
- 文件后缀
- CSV 文本
- Markdown 报告
- 函数

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
from pathlib import Path

for path in Path(".").iterdir():
    print(path.name)
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

1. 列出当前目录文件。
2. 筛选 `.md` 文件。
3. 统计文件数量。
4. 生成一个 Markdown 字符串。
5. 把报告写入文件。
6. 读取 CSV 文本并打印字段。
7. 记录一次文件路径错误。

## 题目驱动训练

### 参考资料

- [Python 官方教程](https://docs.python.org/3/tutorial/)

### 5 道基础巩固题

#### 1. 基础巩固 - 列文件

题目：打印当前目录文件名。

讲解：办公自动化先从文件发现开始。

```python
from pathlib import Path

for path in Path(".").iterdir():
    print(path.name)
```

#### 2. 基础巩固 - 筛选后缀

题目：只打印 md 文件。

讲解：后缀判断很常用。

```python
from pathlib import Path

for path in Path(".").iterdir():
    if path.suffix == ".md":
        print(path.name)
```

#### 3. 基础巩固 - 生成 Markdown

题目：生成一个简单报告。

讲解：Markdown 是轻量报告格式。

```python
lines = ["# 今日报告", "", "- 完成 Python 学习"]
report = "\n".join(lines)
print(report)
```

#### 4. 基础巩固 - 保存报告

题目：把 Markdown 写入文件。

讲解：结果要落盘。

```python
from pathlib import Path

report = "# 今日报告\n\n- 完成 Python 学习"
Path("report.md").write_text(report, encoding="utf-8")
```

#### 5. 基础巩固 - 文件清单函数

题目：返回指定后缀文件名。

讲解：函数化后可复用。

```python
from pathlib import Path

def list_files(folder, suffix):
    names = []
    for path in Path(folder).iterdir():
        if path.suffix == suffix:
            names.append(path.name)
    return names

print(list_files(".", ".md"))
```
