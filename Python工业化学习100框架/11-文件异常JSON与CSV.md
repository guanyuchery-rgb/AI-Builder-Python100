# Day11 - 文件、异常、JSON 与 CSV

学习定位：在 CLI 小项目之后学习读写文件。今天先用小文件和小数据。

## 今日只允许使用

- open/read/write
- Path
- try/except
- json
- csv

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

path = Path("note.txt")
path.write_text("hello", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
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

1. 写入一个 txt 文件。
2. 读取一个 txt 文件。
3. 文件不存在时用 try/except 捕获。
4. 写入一个 JSON 文件。
5. 读取一个 JSON 文件。
6. 读取一个 2 行 CSV。
7. 记录一次路径错误。

## 题目驱动训练

### 参考资料

- [Python 官方教程](https://docs.python.org/3/tutorial/)

### 5 道基础巩固题

#### 1. 基础巩固 - 写文本

题目：写入 note.txt。

讲解：先掌握最小文件写入。

```python
from pathlib import Path

path = Path("note.txt")
path.write_text("今天学习文件读写", encoding="utf-8")
```

#### 2. 基础巩固 - 读文本

题目：读取 note.txt。

讲解：读写配套练。

```python
from pathlib import Path

path = Path("note.txt")
print(path.read_text(encoding="utf-8"))
```

#### 3. 基础巩固 - 异常处理

题目：文件不存在时提示。

讲解：不要让程序直接崩。

```python
from pathlib import Path

path = Path("missing.txt")
try:
    print(path.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("文件不存在")
```

#### 4. 基础巩固 - JSON 保存

题目：保存一个 dict。

讲解：JSON 适合保存结构化结果。

```python
import json
from pathlib import Path

data = {"topic": "Python", "minutes": 60}
Path("summary.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
```

#### 5. 基础巩固 - CSV 读取

题目：读取小 CSV 字符串。

讲解：先读懂行和字段。

```python
import csv
from io import StringIO

text = "topic,minutes\nPython,60\nSQL,30"
reader = csv.DictReader(StringIO(text))
for row in reader:
    print(row["topic"], row["minutes"])
```
