# Day76 - Streamlit项目首页与上传流程

学习定位：把项目结果做成本地可看的上传页面。

## 2小时安排

- 15 分钟：读定位和最小代码。
- 25 分钟：手打一遍最小案例。
- 70 分钟：完成 5 道递进题。
- 10 分钟：记录 Debug、边界情况和项目迁移点。

## 核心知识点：Data App

### 定义

今天的主题是把一个小能力固定成可复用、可测试、可迁移的工程单元。

### 为什么存在

长期学习不能只靠临时理解。每个能力都要能进入项目：有输入、有输出、有失败处理、有复盘入口。

### 最小案例

```python
import pandas as pd
import streamlit as st

st.title("Learning Dashboard")
uploaded = st.file_uploader("Upload CSV")
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())
```

### 常见错误

- 只在临时脚本里跑通，没有沉淀成函数。
- 输入字段没有校验，结果出了错才发现。
- 只 print 结果，不保存中间产物。
- 没有 README、测试或 Debug 记录，几天后难以接上。

### 工程应用

- 数据清洗和指标计算。
- Quant research 小项目。
- LLM report assistant。
- Agent tool prototype。
- 个人作品集沉淀。

### 未来扩展

- 增加单元测试。
- 增加 CLI/API/UI 入口。
- 接入真实数据。
- 写入项目 README 和复盘文档。

## Debug 日志

- 路径错误：先打印当前工作目录。
- 类型错误：先检查输入字段和 dtype。
- 结果异常：先缩小到 3 行样例数据。
- 依赖错误：记录安装命令和 Python 版本。

## 面试 / 项目角度

能说明今天代码的输入、输出、失败情况，以及它如何进入一个真实项目。

## Quant 关联

这一天服务于 Quant 学习：让数据、指标、回测和报告更可复现。

## LLM / Agent 关联

这一天服务于 LLM/Agent 学习：明确输入、输出、失败情况和可审查边界。

## 复习检查

- [ ] 我能独立解释今天能力解决什么问题。
- [ ] 我能手打一遍最小案例。
- [ ] 我能完成 5 道递进题。
- [ ] 我能说清输入、输出和失败情况。
- [ ] 我知道它如何迁移到 Quant / LLM / Agent 项目。

## 简单路线 7 题（不超前）

只用今天及之前学过的能力。做不出来时，先回看当天最小案例，不跳到后面知识。

1. 确认今天属于 UI、API、DB、RAG 或策略的哪一层。
2. 写一个只返回假数据的最小版本。
3. 替换成 3 行真实样例数据。
4. 加入输入校验。
5. 加入结果保存。
6. 写一个手动验收步骤。
7. 记录后续不要过度工程化的一点。
## 题目驱动训练

### 参考题 / 资料

- [Streamlit docs](https://docs.streamlit.io/)
- [pandas docs](https://pandas.pydata.org/docs/)
- [Python Docs](https://docs.python.org/3/)

### 今日产出

一个和“Streamlit项目首页与上传流程”相关的可复用函数、脚本或项目模块。

### 5 道递进题

#### 1. Easy - 核心函数

题目：写一个不依赖 UI/API 的核心函数。

讲解：核心逻辑要和展示层分开。

```python
def calculate_score(value: float, weight: float = 1.0) -> float:
    return value * weight
```

#### 2. Easy - 输入验证

题目：拒绝负数输入。

讲解：API 和 UI 都要共享同一套验证规则。

```python
def validate_value(value: float) -> list[str]:
    if value < 0:
        return ["value must be non-negative"]
    return []
```

#### 3. Medium - 服务层

题目：返回统一结构：ok/data/errors。

讲解：统一返回结构方便前端、API、Agent 调用。

```python
def score_service(payload: dict) -> dict:
    value = float(payload.get("value", 0))
    errors = validate_value(value)
    if errors:
        return {"ok": False, "errors": errors}
    return {"ok": True, "data": {"score": calculate_score(value)}}
```

#### 4. Medium - 展示调用

题目：把服务层结果显示出来。

讲解：展示层只负责展示，不复制业务计算。

```python
result = score_service({"value": 2})
print(result)
```

#### 5. Hard - 服务层测试

题目：为成功和失败各写一个测试。

讲解：只测服务层，不测 UI 细节。

```python
def test_score_service_ok():
    assert score_service({"value": 2})["data"]["score"] == 2

def test_score_service_error():
    assert score_service({"value": -1})["ok"] is False
```
