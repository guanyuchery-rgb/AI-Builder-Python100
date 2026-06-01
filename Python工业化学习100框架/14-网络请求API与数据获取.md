# Day14 - 网络请求、API 与数据获取

学习定位：在函数、异常、JSON 之后学习 API。今天只请求公开 JSON，并处理失败。

## 今日只允许使用

- urllib.request
- json.loads
- try/except
- dict 读取
- timeout

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
import json
from urllib.request import urlopen

with urlopen("https://httpbin.org/json", timeout=10) as response:
    data = json.loads(response.read().decode("utf-8"))
print(data.keys())
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

1. 打开一个公开 JSON URL。
2. 读取 response bytes。
3. decode 成字符串。
4. json.loads 转 dict。
5. 用 `.get()` 读取字段。
6. 加 timeout。
7. 记录一次网络失败。

## 题目驱动训练

### 参考资料

- [Python 官方教程](https://docs.python.org/3/tutorial/)

### 5 道基础巩固题

#### 1. 基础巩固 - 请求 JSON

题目：请求 httpbin JSON。

讲解：网络最小闭环。

```python
import json
from urllib.request import urlopen

with urlopen("https://httpbin.org/json", timeout=10) as response:
    text = response.read().decode("utf-8")
    data = json.loads(text)
print(data.keys())
```

#### 2. 基础巩固 - 封装 fetch

题目：把请求封装成函数。

讲解：复用 Day06 函数。

```python
import json
from urllib.request import urlopen

def fetch_json(url):
    with urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))

print(fetch_json("https://httpbin.org/json").keys())
```

#### 3. 基础巩固 - 安全读取

题目：字段不存在时给默认值。

讲解：API 字段可能变化。

```python
data = {"name": "demo"}
print(data.get("price", "N/A"))
```

#### 4. 基础巩固 - 错误处理

题目：请求失败时返回错误信息。

讲解：不要直接崩。

```python
from urllib.error import URLError

try:
    data = fetch_json("https://httpbin.org/json")
    print(data)
except URLError as error:
    print("请求失败", error)
```

#### 5. 基础巩固 - API 记录

题目：把 URL 和结果字段写成摘要。

讲解：为后续项目复盘。

```python
url = "https://httpbin.org/json"
data = fetch_json(url)
summary = {"url": url, "fields": list(data.keys())}
print(summary)
```
