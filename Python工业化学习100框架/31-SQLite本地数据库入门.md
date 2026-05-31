# Day31 - SQLite本地数据库入门

学习定位：用 sqlite3 保存结构化数据，为后续查询和 Agent tool 做准备。

## 2小时安排

- 15 分钟：读定位和最小代码。
- 25 分钟：手打一遍最小案例。
- 70 分钟：完成 5 道递进题。
- 10 分钟：记录 Debug、边界情况和项目迁移点。

## 核心知识点：Local Database / Analytical SQL

### 定义

今天的主题是把一个小能力固定成可复用、可测试、可迁移的工程单元。

### 为什么存在

长期学习不能只靠临时理解。每个能力都要能进入项目：有输入、有输出、有失败处理、有复盘入口。

### 最小案例

```python
import sqlite3

with sqlite3.connect("research.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS records (name TEXT, value REAL, tag TEXT)")
    conn.execute("INSERT INTO records VALUES (?, ?, ?)", ("demo", 1.0, "test"))
    rows = conn.execute("SELECT tag, AVG(value) FROM records GROUP BY tag").fetchall()
print(rows)
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

1. 写一个最小配置或连接示例。
2. 用 3 条假数据跑通主流程。
3. 把主流程拆成输入、处理、输出三步。
4. 写一个失败输入案例。
5. 给核心函数写 1 个 assert 或 pytest。
6. 补一行运行命令。
7. 补一行 README 说明。
## 题目驱动训练

### 参考题 / 资料

- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [pandas docs](https://pandas.pydata.org/docs/)
- [Python Docs](https://docs.python.org/3/)

### 今日产出

一个和“SQLite本地数据库入门”相关的可复用函数、脚本或项目模块。

### 5 道递进题

#### 1. Easy - 建表

题目：创建 `records` 表，字段为 `name/value/tag`。

讲解：表结构是长期数据资产的第一层边界。

```python
import sqlite3

def create_records(conn: sqlite3.Connection) -> None:
    conn.execute("CREATE TABLE IF NOT EXISTS records (name TEXT, value REAL, tag TEXT)")
```

#### 2. Easy - 参数化插入

题目：插入一条记录。

讲解：SQL 参数用 `?`，不要拼接字符串。

```python
def insert_record(conn, name: str, value: float, tag: str) -> None:
    conn.execute("INSERT INTO records VALUES (?, ?, ?)", (name, value, tag))
    conn.commit()
```

#### 3. Medium - 聚合查询

题目：按 tag 统计平均值和数量。

讲解：SQL 很适合做第一层聚合。

```python
def summary_by_tag(conn) -> list[tuple]:
    sql = "SELECT tag, AVG(value), COUNT(*) FROM records GROUP BY tag"
    return conn.execute(sql).fetchall()
```

#### 4. Medium - Repository 封装

题目：把连接和查询封装成类。

讲解：业务逻辑不应到处写 SQL 细节。

```python
class RecordRepository:
    def __init__(self, path: str):
        self.path = path

    def connect(self):
        return sqlite3.connect(self.path)
```

#### 5. Hard - SQL Tool

题目：输入 tag，返回结构化查询结果。

讲解：这是 Agent 查询本地数据库的最小形状。

```python
def query_records_tool(db_path: str, tag: str) -> dict:
    with sqlite3.connect(db_path) as conn:
        rows = conn.execute("SELECT name, value FROM records WHERE tag = ?", (tag,)).fetchall()
    data = [{"name": name, "value": value} for name, value in rows]
    return {"ok": True, "data": data}
```
