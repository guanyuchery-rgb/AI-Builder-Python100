# Python100 Library Learning Map

这个文件解决一个问题：学 Python 不是只学语法，还要学会“库的认知地图”。

以后每次第一次遇到新库，都先按这个顺序看：

```text
这个库解决什么问题
  ↓
库里的核心工具有哪些
  ↓
每个工具的输入是什么
  ↓
每个工具的输出是什么
  ↓
它和旧知识有什么关系
  ↓
最小代码怎么写
  ↓
常见错误是什么
  ↓
未来会在哪里用
```

## 1. 标准库基础

这些库是 Python 工程化最基础的工具箱。

| 库 | 核心工具 | 输入 | 输出 | 未来用途 |
| --- | --- | --- | --- | --- |
| `csv` | `reader`, `writer`, `DictReader`, `DictWriter` | CSV 文件 / list / dict | 行数据 / CSV 文件 | 表格日志、数据导入 |
| `json` | `load`, `dump`, `loads`, `dumps` | dict / list / JSON 字符串 | Python 对象 / JSON | API、配置、Agent 日志 |
| `re` | `search`, `findall`, `sub` | 文本 | 匹配结果 / 清洗后文本 | 文本解析、脱敏、规则抽取 |
| `datetime` | `date`, `datetime`, `timedelta` | 字符串 / 时间对象 | 标准时间对象 | 时间序列、日志、Quant |
| `pathlib` | `Path`, `glob`, `exists` | 文件路径 | 路径对象 / 文件列表 | 项目结构、批处理 |
| `argparse` | `ArgumentParser` | 命令行参数 | 可用参数对象 | CLI 工具 |
| `logging` | `logger`, `info`, `warning`, `error` | 运行事件 | 日志记录 | Debug、Agent 可观测性 |
| `sqlite3` | `connect`, `execute`, `fetchall` | SQL / 参数 | 查询结果 / 本地数据库 | 结果存储、记忆、实验追踪 |

## 2. 数据分析库

这些库是数据分析、Quant、机器学习的地基。

| 库 | 核心工具 | 输入 | 输出 | 未来用途 |
| --- | --- | --- | --- | --- |
| `pandas` | `DataFrame`, `read_csv`, `groupby`, `merge` | 表格数据 | 可分析表格 | 清洗、聚合、特征工程 |
| `numpy` | `array`, `mean`, `where`, 向量化计算 | list / 数值表 | 数组 / 数值结果 | 机器学习、Embedding、Quant |
| `matplotlib` | `plot`, `bar`, `hist`, `savefig` | 数值序列 | 图表 | 报告、回测曲线 |

## 3. 机器学习库

机器学习先不追求复杂模型，先理解统一动作：

```text
数据 -> 特征 -> 模型 -> fit -> predict -> evaluate
```

| 库 | 核心工具 | 输入 | 输出 | 未来用途 |
| --- | --- | --- | --- | --- |
| `sklearn.model_selection` | `train_test_split` | 特征表 + 标签 | 训练集 / 测试集 | 防止只在样本内自嗨 |
| `sklearn.preprocessing` | `StandardScaler` | 数值特征 | 标准化特征 | 模型训练前处理 |
| `sklearn.linear_model` | `LinearRegression`, `LogisticRegression` | 特征 + 标签 | 可预测模型 | 回归、分类、基线模型 |
| `sklearn.metrics` | `accuracy_score`, `mean_squared_error` | 真实值 + 预测值 | 评分 | 评估模型是否有效 |
| `sklearn.pipeline` | `Pipeline` | 预处理步骤 + 模型 | 可复用训练流程 | 工程化建模 |

## 4. 深度学习库

深度学习先不从大模型开始，而是先理解 PyTorch 的最小地图。

```text
Tensor -> Dataset -> DataLoader -> nn.Module -> loss -> optimizer -> train loop
```

| 库 | 核心工具 | 输入 | 输出 | 未来用途 |
| --- | --- | --- | --- | --- |
| `torch` | `tensor`, `matmul`, `no_grad` | 数值数组 | Tensor / 计算结果 | 神经网络计算 |
| `torch.utils.data` | `Dataset`, `DataLoader` | 样本数据 | 小批量 batch | 训练循环 |
| `torch.nn` | `Module`, `Linear`, `Embedding` | Tensor | 模型输出 | 神经网络结构 |
| `torch.optim` | `SGD`, `Adam` | 模型参数 + 梯度 | 更新后的参数 | 训练模型 |

## 5. Transformer / LLM 基础库

LLM 和 Agent 不是凭空出现的。它们依赖这些基础概念：

```text
文本 -> token -> embedding -> attention/transformer -> output -> tool/action
```

| 库 | 核心工具 | 输入 | 输出 | 未来用途 |
| --- | --- | --- | --- | --- |
| `transformers` | `AutoTokenizer`, `AutoModel`, `pipeline` | 文本 / 模型名 | token / 向量 / 生成结果 | LLM、Embedding、RAG |
| `tokenizers` | tokenizer | 文本 | token id | 理解上下文长度和成本 |
| `pydantic` | `BaseModel` | dict / JSON | 校验后的对象 | 结构化输出、Tool 参数 |
| `httpx` / `requests` | `get`, `post` | URL / JSON | API 响应 | 调用模型服务和外部工具 |

## 6. Agent 需要的库能力

Agent 本质上是把多个基础库组合起来。

| Agent 能力 | 依赖的库基础 | 你需要先懂什么 |
| --- | --- | --- |
| Tool | `pydantic`, `argparse`, `requests` | 输入输出契约 |
| Memory | `json`, `sqlite3`, `pandas` | 状态保存和读取 |
| Retrieval | `numpy`, `transformers`, 向量相似度 | Embedding 和 top-k |
| Workflow | `logging`, `datetime`, `pathlib` | 步骤、日志、文件组织 |
| Evaluation | `pandas`, `sklearn.metrics` | 样例集、评分、错误分析 |

## 学习原则

- 先学库的地图，再学函数。
- 先看输入输出，再看参数。
- 先写最小例子，再写复杂流程。
- 先知道这个库会在哪里复用，再决定要不要深入。
- 对初学者来说，库学习的目标不是背 API，而是建立“看到新库也不慌”的迁移能力。
