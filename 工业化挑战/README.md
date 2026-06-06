# 工业化挑战 IC01-IC74

IC 从 Day15 面向对象与 dataclass 结束后开始。

Day01-Day100 负责知识学习；工业化挑战负责项目能力验证。

现在 IC 按平级项目分组，不在根目录平铺。Project01-Project08 是平级作品方向；编号顺序只表示推荐学习顺序，不表示项目之间有上下级。推荐顺序遵循：数据分析 -> 机器学习 -> 深度学习 -> 强化学习 -> LLM/RAG -> Agent -> Quant -> 现代 AI 工程。

## 为什么这样排序

- 数据分析是所有方向共同地基。
- 机器学习先训练特征、标签、评估和泛化意识。
- 深度学习在机器学习之后，再进入张量、训练循环、CNN、Transformer。
- 强化学习需要先有模型训练和评估意识，再学习状态、动作、奖励。
- LLM/RAG 是现代 AI 应用层，依赖 embedding、检索、评估和上下文工程。
- Agent 是更后段的系统工程，依赖 LLM、工具、状态、日志、安全边界。
- Quant 是金融数据专业方向，可在数据分析之后长期并行，但项目交付上放到后段。
- 现代 AI 工程是综合交付层。

## 使用原则

- [LeetCode 热题结构](LEETCODE_HOT_LIST.md)：370 题，Easy 90 / Medium 240 / Hard 40。

- 不占 Day 数。
- Project01-Project08 是平级关系，每个项目都可以独立成为 GitHub 作品。
- 不要求 Day 学完 100 才开始；Day15 后可以从 Project01 慢慢做。
- 每个 IC 都要有工程任务、GitHub 提交、Review 和 LeetCode 训练。
- 项目目录优先长期维护，不为了炫技增加复杂 infra。

## 平级项目分组

- [数据分析求职项目（IC01-IC15）](Project01-数据分析项目/README.md)：从公开数据到 SQL / Pandas / 可视化 / 报告。
- [机器学习求职项目（IC16-IC23）](Project02-机器学习项目/README.md)：从标签、特征、sklearn baseline、评估、解释到推理接口。
- [深度学习求职项目（IC24-IC29）](Project03-深度学习项目/README.md)：从 PyTorch Dataset、训练循环、CNN 到 Transformer。
- [强化学习实验项目（IC30-IC34）](Project04-强化学习项目/README.md)：从环境、策略、老虎机、Q-learning 到 Policy Gradient。
- [LLM / RAG 求职项目（IC35-IC46）](Project05-LLM-RAG项目/README.md)：从文档数据到切分、Embedding、检索、引用回答和评估。
- [Agent 工作流求职项目（IC47-IC56）](Project06-Agent工作流项目/README.md)：从工具契约到路由、执行、状态、日志和人工审查。
- [Quant 研究求职项目（IC57-IC69）](Project07-Quant研究项目/README.md)：从行情数据到收益、风险、因子、回测和报告。
- [现代 AI 工程项目（IC70-IC74）](Project08-现代AI工程项目/README.md)：从 HuggingFace、Benchmark、模型路由、安全审查到作品集。

## 推荐推进顺序

下面只是学习顺序，不是目录层级，也不是项目重要性排序。

1. Project01 数据分析：先练数据、文件、SQL、Pandas、可视化。
2. Project02 机器学习：练标签、特征、sklearn、评估和推理。
3. Project03 深度学习：练 PyTorch、训练循环、CNN、Transformer。
4. Project04 强化学习：练环境、策略、奖励、Q-learning。
5. Project05 LLM/RAG：练文本、Embedding、检索、引用回答。
6. Project06 Agent：练工具调用、状态、日志和人工审查。
7. Project07 Quant：练行情、收益、风险、因子、回测。
8. Project08 现代 AI 工程：练评估、路由、安全、轻量 MLOps。

## 全部 IC 索引

### 数据分析求职项目（IC01-IC15）

- [IC01 - Kaggle数据选题](Project01-数据分析项目/IC01-Kaggle数据选题.md)
- [IC02 - 数据下载与目录设计](Project01-数据分析项目/IC02-数据下载与目录设计.md)
- [IC03 - CSVJSON清洗](Project01-数据分析项目/IC03-CSVJSON清洗.md)
- [IC04 - Pandas特征表](Project01-数据分析项目/IC04-Pandas特征表.md)
- [IC05 - NumPy指标计算](Project01-数据分析项目/IC05-NumPy指标计算.md)
- [IC06 - Matplotlib可视化](Project01-数据分析项目/IC06-Matplotlib可视化.md)
- [IC07 - SQLite入库](Project01-数据分析项目/IC07-SQLite入库.md)
- [IC08 - SQL分析查询](Project01-数据分析项目/IC08-SQL分析查询.md)
- [IC09 - 缺失值与异常值报告](Project01-数据分析项目/IC09-缺失值与异常值报告.md)
- [IC10 - 统计检验与业务解释](Project01-数据分析项目/IC10-统计检验与业务解释.md)
- [IC11 - Streamlit数据看板](Project01-数据分析项目/IC11-Streamlit数据看板.md)
- [IC12 - README与截图](Project01-数据分析项目/IC12-README与截图.md)
- [IC13 - 数据分析报告](Project01-数据分析项目/IC13-数据分析报告.md)
- [IC14 - 复现脚本](Project01-数据分析项目/IC14-复现脚本.md)
- [IC15 - 数据分析项目总交付](Project01-数据分析项目/IC15-数据分析项目总交付.md)

### 机器学习求职项目（IC16-IC23）

- [IC16 - 机器学习问题定义与标签设计](Project02-机器学习项目/IC16-机器学习问题定义与标签设计.md)
- [IC17 - ScikitLearn基线模型](Project02-机器学习项目/IC17-ScikitLearn基线模型.md)
- [IC18 - 特征工程与Pipeline](Project02-机器学习项目/IC18-特征工程与Pipeline.md)
- [IC19 - 训练验证切分](Project02-机器学习项目/IC19-训练验证切分.md)
- [IC20 - 分类评估与阈值](Project02-机器学习项目/IC20-分类评估与阈值.md)
- [IC21 - 回归评估与误差分析](Project02-机器学习项目/IC21-回归评估与误差分析.md)
- [IC22 - 模型解释与特征重要性](Project02-机器学习项目/IC22-模型解释与特征重要性.md)
- [IC23 - 模型保存与推理接口](Project02-机器学习项目/IC23-模型保存与推理接口.md)

### 深度学习求职项目（IC24-IC29）

- [IC24 - PyTorch张量与Dataset](Project03-深度学习项目/IC24-PyTorch张量与Dataset.md)
- [IC25 - 神经网络前向传播](Project03-深度学习项目/IC25-神经网络前向传播.md)
- [IC26 - 训练循环与反向传播](Project03-深度学习项目/IC26-训练循环与反向传播.md)
- [IC27 - 过拟合与正则化](Project03-深度学习项目/IC27-过拟合与正则化.md)
- [IC28 - CNN图像分类入门](Project03-深度学习项目/IC28-CNN图像分类入门.md)
- [IC29 - Transformer最小认知地图](Project03-深度学习项目/IC29-Transformer最小认知地图.md)

### 强化学习实验项目（IC30-IC34）

- [IC30 - 强化学习问题建模](Project04-强化学习项目/IC30-强化学习问题建模.md)
- [IC31 - Gymnasium环境与随机策略](Project04-强化学习项目/IC31-Gymnasium环境与随机策略.md)
- [IC32 - 多臂老虎机与探索利用](Project04-强化学习项目/IC32-多臂老虎机与探索利用.md)
- [IC33 - Qlearning表格方法](Project04-强化学习项目/IC33-Qlearning表格方法.md)
- [IC34 - PolicyGradient最小版](Project04-强化学习项目/IC34-PolicyGradient最小版.md)

### LLM / RAG 求职项目（IC35-IC46）

- [IC35 - 文档数据集构造](Project05-LLM-RAG项目/IC35-文档数据集构造.md)
- [IC36 - 文本清洗与切分](Project05-LLM-RAG项目/IC36-文本清洗与切分.md)
- [IC37 - Embedding地图](Project05-LLM-RAG项目/IC37-Embedding地图.md)
- [IC38 - 向量检索](Project05-LLM-RAG项目/IC38-向量检索.md)
- [IC39 - RAG上下文打包](Project05-LLM-RAG项目/IC39-RAG上下文打包.md)
- [IC40 - 引用回答](Project05-LLM-RAG项目/IC40-引用回答.md)
- [IC41 - 结构化输出](Project05-LLM-RAG项目/IC41-结构化输出.md)
- [IC42 - LLM评估集](Project05-LLM-RAG项目/IC42-LLM评估集.md)
- [IC43 - 错误案例库](Project05-LLM-RAG项目/IC43-错误案例库.md)
- [IC44 - RAGStreamlitDemo](Project05-LLM-RAG项目/IC44-RAGStreamlitDemo.md)
- [IC45 - README与截图](Project05-LLM-RAG项目/IC45-README与截图.md)
- [IC46 - RAG总交付](Project05-LLM-RAG项目/IC46-RAG总交付.md)

### Agent 工作流求职项目（IC47-IC56）

- [IC47 - Tool契约设计](Project06-Agent工作流项目/IC47-Tool契约设计.md)
- [IC48 - 工具路由](Project06-Agent工作流项目/IC48-工具路由.md)
- [IC49 - 执行器](Project06-Agent工作流项目/IC49-执行器.md)
- [IC50 - 状态存储](Project06-Agent工作流项目/IC50-状态存储.md)
- [IC51 - 人工审查点](Project06-Agent工作流项目/IC51-人工审查点.md)
- [IC52 - 日志与可观测性](Project06-Agent工作流项目/IC52-日志与可观测性.md)
- [IC53 - 错误恢复](Project06-Agent工作流项目/IC53-错误恢复.md)
- [IC54 - 多步骤Workflow](Project06-Agent工作流项目/IC54-多步骤Workflow.md)
- [IC55 - 演示与截图](Project06-Agent工作流项目/IC55-演示与截图.md)
- [IC56 - Agent总交付](Project06-Agent工作流项目/IC56-Agent总交付.md)

### Quant 研究求职项目（IC57-IC69）

- [IC57 - 行情数据源选择](Project07-Quant研究项目/IC57-行情数据源选择.md)
- [IC58 - 价格数据清洗](Project07-Quant研究项目/IC58-价格数据清洗.md)
- [IC59 - 收益率与波动率](Project07-Quant研究项目/IC59-收益率与波动率.md)
- [IC60 - 最大回撤](Project07-Quant研究项目/IC60-最大回撤.md)
- [IC61 - 信号生成](Project07-Quant研究项目/IC61-信号生成.md)
- [IC62 - 未来函数防护](Project07-Quant研究项目/IC62-未来函数防护.md)
- [IC63 - 手续费滑点](Project07-Quant研究项目/IC63-手续费滑点.md)
- [IC64 - 仓位管理](Project07-Quant研究项目/IC64-仓位管理.md)
- [IC65 - 因子分组](Project07-Quant研究项目/IC65-因子分组.md)
- [IC66 - 事件研究](Project07-Quant研究项目/IC66-事件研究.md)
- [IC67 - 回测结果入库](Project07-Quant研究项目/IC67-回测结果入库.md)
- [IC68 - Quant图表报告](Project07-Quant研究项目/IC68-Quant图表报告.md)
- [IC69 - Quant总交付](Project07-Quant研究项目/IC69-Quant总交付.md)

### 现代 AI 工程项目（IC70-IC74）

- [IC70 - HuggingFace微调流程](Project08-现代AI工程项目/IC70-HuggingFace微调流程.md)
- [IC71 - AI评估与Benchmark](Project08-现代AI工程项目/IC71-AI评估与Benchmark.md)
- [IC72 - 模型路由与成本控制](Project08-现代AI工程项目/IC72-模型路由与成本控制.md)
- [IC73 - AI安全与人工审查](Project08-现代AI工程项目/IC73-AI安全与人工审查.md)
- [IC74 - 现代AI作品集总交付](Project08-现代AI工程项目/IC74-现代AI作品集总交付.md)
