# Day14 - 网络请求、API 与数据获取

学习定位：掌握从 HTTP API 获取数据的基础能力，这是量化数据、LLM API、Agent 工具和数据产品的共同入口。

## 2小时安排

- 20 分钟：理解 HTTP、URL、status code、JSON response。
- 30 分钟：手打一个 `urllib` 标准库请求案例。
- 35 分钟：封装一个 API 获取函数。
- 20 分钟：处理超时、失败和数据字段缺失。
- 15 分钟：写 Quant 与 Agent 场景。

## 知识点 1：HTTP 请求

### 定义

HTTP 请求是客户端向服务器获取或提交资源的方式。常见方法有 GET、POST。

### 为什么存在

现代数据大多通过 API 获取：行情、宏观数据、LLM、数据库服务、内部系统。

### 最小案例

```python
import json
from urllib.request import urlopen

url = "https://api.github.com"

with urlopen(url, timeout=10) as response:
    data = json.loads(response.read().decode("utf-8"))

print(data["current_user_url"])
```

### 常见错误

- 网络超时。
- status code 不是 200。
- 返回不是预期 JSON。
- API 有 rate limit。

### 工程应用

- 获取行情数据。
- 调用 LLM API。
- 调用内部服务。
- Agent tool 的网络能力。

### 未来扩展

- `requests`。
- `httpx`。
- retry。
- API key 管理。

## 知识点 2：封装 API 函数

### 定义

封装 API 函数是把请求、解析、错误处理放进一个可复用函数。

### 为什么存在

避免每个脚本重复写网络细节，也方便测试和替换数据源。

### 最小案例

```python
import json
from urllib.error import URLError
from urllib.request import urlopen


def fetch_json(url: str, timeout: int = 10) -> dict:
    try:
        with urlopen(url, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except URLError as error:
        raise RuntimeError(f"请求失败: {url}") from error


data = fetch_json("https://api.github.com")
print(data["zen"])
```

### 常见错误

- 函数直接 print，不 return。
- 不设置 timeout。
- 把 API key 写死在代码里。

### 工程应用

- 数据采集模块。
- LLM client。
- Agent 工具。
- 定时任务。

### 未来扩展

- 环境变量。
- 缓存。
- 速率限制。
- 响应 schema 验证。

## Debug 日志

- `URLError`：网络、DNS、SSL 或服务器问题。
- `TimeoutError`：请求等待太久。
- `KeyError`：返回 JSON 没有预期字段。
- `JSONDecodeError`：返回内容不是合法 JSON。


## 面试角度 Interview

能说明 HTTP status code、timeout、JSON response、API key 和 rate limit 的基本概念。

## Quant 关联

行情和宏观数据经常来自 API。封装数据获取函数能让研究过程可复现。

## LLM / Agent 关联

调用 LLM 本质上也是 API 请求。Agent 的外部世界能力大多来自 API tool。

## 复习检查

- [ ] 我能发起一个 GET 请求。
- [ ] 我能解析 JSON。
- [ ] 我能处理网络失败。
- [ ] 我知道不要把密钥写进代码。

## 简单路线 7 题（不超前）

只用今天及之前学过的能力。做不出来时，先回看当天最小案例，不跳到后面知识。

1. 写一个普通同步函数。
2. 给函数加超时/失败说明。
3. 请求一个公开 JSON 或模拟 JSON。
4. 把 API 返回字段安全读取出来。
5. 列出一个文件夹中的目标文件。
6. 生成一个 Markdown 小报告。
7. 记录一次网络或文件路径错误。
## 题目驱动训练

### 参考题 / 资料

- [Python urllib docs](https://docs.python.org/3/library/urllib.request.html)
- [Python json docs](https://docs.python.org/3/library/json.html)
- [httpbin JSON endpoint](https://httpbin.org/json)

### 5 道递进题

#### 1. Easy - 请求 JSON

题目：请求公开 JSON 接口并打印标题。

讲解：网络请求最小闭环是 request -> bytes -> text -> JSON。

```python
import json
from urllib.request import urlopen

url = "https://httpbin.org/json"
with urlopen(url, timeout=10) as response:
    raw = response.read().decode("utf-8")
    data = json.loads(raw)

print(data["slideshow"]["title"])
```

#### 2. Easy - fetch_json 函数

题目：输入 URL，返回 dict。

讲解：把请求细节封装起来，后续才能复用和测试。

```python
import json
from urllib.request import urlopen

def fetch_json(url: str, timeout: int = 10) -> dict:
    with urlopen(url, timeout=timeout) as response:
        text = response.read().decode("utf-8")
        return json.loads(text)
```

#### 3. Medium - 安全读取字段

题目：字段缺失时返回默认值。

讲解：外部 API 返回结构可能变，读取要有兜底。

```python
def get_slideshow_title(data: dict) -> str:
    # nested get 避免 KeyError
    return data.get("slideshow", {}).get("title", "N/A")
```

#### 4. Medium - 错误处理

题目：处理网络失败和 JSON 解析失败。

讲解：工具函数不要静默失败，要返回可定位的错误。

```python
import json
from urllib.error import URLError, HTTPError

def fetch_json_safe(url: str) -> dict:
    try:
        return fetch_json(url)
    except HTTPError as error:
        return {"ok": False, "error": f"http {error.code}"}
    except URLError as error:
        return {"ok": False, "error": f"network: {error.reason}"}
    except json.JSONDecodeError:
        return {"ok": False, "error": "invalid json"}
```

#### 5. Hard - DataClient 类

题目：实现 `fetch/parse/validate` 三步。

讲解：这是工业数据源封装的基础形状。

```python
import json
from urllib.request import urlopen

class DataClient:
    def fetch(self, url: str) -> str:
        # fetch 只负责拿原始文本
        with urlopen(url, timeout=10) as response:
            return response.read().decode("utf-8")

    def parse(self, text: str) -> dict:
        # parse 只负责 JSON 解析
        return json.loads(text)

    def validate(self, data: dict, required: list[str]) -> list[str]:
        # validate 返回缺失字段，方便记录 Debug
        return [field for field in required if field not in data]
```
