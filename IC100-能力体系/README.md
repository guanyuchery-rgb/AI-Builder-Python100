# IC100 能力体系

IC100 是 Python100 的能力验证线。现在它只负责工程项目、GitHub 提交、作品沉淀和复盘；算法刷题已经独立到 [`leetcode（hot code）300`](../leetcode（hot%20code）300/README.md)。

```text
Python100 = 知识体系
IC100 = 能力体系
GitHub = 成果体系
LeetCode Hot Code 300 = 算法体系
```

目标人群：统计学硕士 -> AI Native Builder -> Agent / LLM / Quant 方向实习求职。

核心原则：Day 只负责 What / Why / How / Common Errors / Future Usage；IC 只负责能力验证、工程训练和作品沉淀。

## 结构

- IC020-IC039：Data Analysis Project，最终形成 LLM Evaluation Analytics Platform。
- IC040-IC059：Quant Research Project，最终形成 Mini Quant Research Framework。
- IC060-IC079：LLM Application Project，最终形成 RAG Knowledge Assistant。
- IC080-IC100：Agent Workflow Project，最终形成 Agent Workflow System。

## 独立算法线

- [LeetCode（Hot Code）300](../leetcode（hot%20code）300/README.md)：60 天，每天 5 道，官方链接，不重复。

## 全部 IC 索引

### Data Analysis Project

最终项目：LLM Evaluation Analytics Platform。

- [IC020 - 评估平台问题定义](01-Data-Analysis-Project/IC020-%E8%AF%84%E4%BC%B0%E5%B9%B3%E5%8F%B0%E9%97%AE%E9%A2%98%E5%AE%9A%E4%B9%89.md)
- [IC021 - 数据集与目录设计](01-Data-Analysis-Project/IC021-%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8E%E7%9B%AE%E5%BD%95%E8%AE%BE%E8%AE%A1.md)
- [IC022 - JSONLCSV原始数据检查](01-Data-Analysis-Project/IC022-JSONLCSV%E5%8E%9F%E5%A7%8B%E6%95%B0%E6%8D%AE%E6%A3%80%E6%9F%A5.md)
- [IC023 - Pandas评估数据体检](01-Data-Analysis-Project/IC023-Pandas%E8%AF%84%E4%BC%B0%E6%95%B0%E6%8D%AE%E4%BD%93%E6%A3%80.md)
- [IC024 - 评估结果清洗标准化](01-Data-Analysis-Project/IC024-%E8%AF%84%E4%BC%B0%E7%BB%93%E6%9E%9C%E6%B8%85%E6%B4%97%E6%A0%87%E5%87%86%E5%8C%96.md)
- [IC025 - 模型指标与分组聚合](01-Data-Analysis-Project/IC025-%E6%A8%A1%E5%9E%8B%E6%8C%87%E6%A0%87%E4%B8%8E%E5%88%86%E7%BB%84%E8%81%9A%E5%90%88.md)
- [IC026 - 维表与实验元数据设计](01-Data-Analysis-Project/IC026-%E7%BB%B4%E8%A1%A8%E4%B8%8E%E5%AE%9E%E9%AA%8C%E5%85%83%E6%95%B0%E6%8D%AE%E8%AE%BE%E8%AE%A1.md)
- [IC027 - 时间序列与版本趋势](01-Data-Analysis-Project/IC027-%E6%97%B6%E9%97%B4%E5%BA%8F%E5%88%97%E4%B8%8E%E7%89%88%E6%9C%AC%E8%B6%8B%E5%8A%BF.md)
- [IC028 - NumPy评分指标计算](01-Data-Analysis-Project/IC028-NumPy%E8%AF%84%E5%88%86%E6%8C%87%E6%A0%87%E8%AE%A1%E7%AE%97.md)
- [IC029 - 统计检验与模型差异解释](01-Data-Analysis-Project/IC029-%E7%BB%9F%E8%AE%A1%E6%A3%80%E9%AA%8C%E4%B8%8E%E6%A8%A1%E5%9E%8B%E5%B7%AE%E5%BC%82%E8%A7%A3%E9%87%8A.md)
- [IC030 - Matplotlib评估可视化](01-Data-Analysis-Project/IC030-Matplotlib%E8%AF%84%E4%BC%B0%E5%8F%AF%E8%A7%86%E5%8C%96.md)
- [IC031 - SQLite评估结果入库](01-Data-Analysis-Project/IC031-SQLite%E8%AF%84%E4%BC%B0%E7%BB%93%E6%9E%9C%E5%85%A5%E5%BA%93.md)
- [IC032 - SQL评估分析查询](01-Data-Analysis-Project/IC032-SQL%E8%AF%84%E4%BC%B0%E5%88%86%E6%9E%90%E6%9F%A5%E8%AF%A2.md)
- [IC033 - 数据质量与异常报告](01-Data-Analysis-Project/IC033-%E6%95%B0%E6%8D%AE%E8%B4%A8%E9%87%8F%E4%B8%8E%E5%BC%82%E5%B8%B8%E6%8A%A5%E5%91%8A.md)
- [IC034 - Streamlit评估看板](01-Data-Analysis-Project/IC034-Streamlit%E8%AF%84%E4%BC%B0%E7%9C%8B%E6%9D%BF.md)
- [IC035 - README截图与运行说明](01-Data-Analysis-Project/IC035-README%E6%88%AA%E5%9B%BE%E4%B8%8E%E8%BF%90%E8%A1%8C%E8%AF%B4%E6%98%8E.md)
- [IC036 - LLM评估分析报告](01-Data-Analysis-Project/IC036-LLM%E8%AF%84%E4%BC%B0%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A.md)
- [IC037 - 一键复现脚本](01-Data-Analysis-Project/IC037-%E4%B8%80%E9%94%AE%E5%A4%8D%E7%8E%B0%E8%84%9A%E6%9C%AC.md)
- [IC038 - LLM Evaluation Analytics总交付](01-Data-Analysis-Project/IC038-LLMEvaluationAnalytics%E6%80%BB%E4%BA%A4%E4%BB%98.md)
- [IC039 - Data项目简历表达](01-Data-Analysis-Project/IC039-Data%E9%A1%B9%E7%9B%AE%E7%AE%80%E5%8E%86%E8%A1%A8%E8%BE%BE.md)

### Quant Research Project

最终项目：Mini Quant Research Framework。

- [IC040 - 行情数据源选择](02-Quant-Research-Project/IC040-%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE%E6%BA%90%E9%80%89%E6%8B%A9.md)
- [IC041 - 价格数据清洗](02-Quant-Research-Project/IC041-%E4%BB%B7%E6%A0%BC%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97.md)
- [IC042 - 收益率与波动率](02-Quant-Research-Project/IC042-%E6%94%B6%E7%9B%8A%E7%8E%87%E4%B8%8E%E6%B3%A2%E5%8A%A8%E7%8E%87.md)
- [IC043 - 最大回撤与净值曲线](02-Quant-Research-Project/IC043-%E6%9C%80%E5%A4%A7%E5%9B%9E%E6%92%A4%E4%B8%8E%E5%87%80%E5%80%BC%E6%9B%B2%E7%BA%BF.md)
- [IC044 - Sharpe与风险指标](02-Quant-Research-Project/IC044-Sharpe%E4%B8%8E%E9%A3%8E%E9%99%A9%E6%8C%87%E6%A0%87.md)
- [IC045 - 信号生成](02-Quant-Research-Project/IC045-%E4%BF%A1%E5%8F%B7%E7%94%9F%E6%88%90.md)
- [IC046 - 未来函数防护](02-Quant-Research-Project/IC046-%E6%9C%AA%E6%9D%A5%E5%87%BD%E6%95%B0%E9%98%B2%E6%8A%A4.md)
- [IC047 - 手续费与滑点](02-Quant-Research-Project/IC047-%E6%89%8B%E7%BB%AD%E8%B4%B9%E4%B8%8E%E6%BB%91%E7%82%B9.md)
- [IC048 - 仓位管理](02-Quant-Research-Project/IC048-%E4%BB%93%E4%BD%8D%E7%AE%A1%E7%90%86.md)
- [IC049 - 策略参数实验](02-Quant-Research-Project/IC049-%E7%AD%96%E7%95%A5%E5%8F%82%E6%95%B0%E5%AE%9E%E9%AA%8C.md)
- [IC050 - 因子分组](02-Quant-Research-Project/IC050-%E5%9B%A0%E5%AD%90%E5%88%86%E7%BB%84.md)
- [IC051 - 事件研究](02-Quant-Research-Project/IC051-%E4%BA%8B%E4%BB%B6%E7%A0%94%E7%A9%B6.md)
- [IC052 - 回测结果入库](02-Quant-Research-Project/IC052-%E5%9B%9E%E6%B5%8B%E7%BB%93%E6%9E%9C%E5%85%A5%E5%BA%93.md)
- [IC053 - Quant图表报告](02-Quant-Research-Project/IC053-Quant%E5%9B%BE%E8%A1%A8%E6%8A%A5%E5%91%8A.md)
- [IC054 - 策略限制说明](02-Quant-Research-Project/IC054-%E7%AD%96%E7%95%A5%E9%99%90%E5%88%B6%E8%AF%B4%E6%98%8E.md)
- [IC055 - 回测复现脚本](02-Quant-Research-Project/IC055-%E5%9B%9E%E6%B5%8B%E5%A4%8D%E7%8E%B0%E8%84%9A%E6%9C%AC.md)
- [IC056 - Mini框架README](02-Quant-Research-Project/IC056-Mini%E6%A1%86%E6%9E%B6README.md)
- [IC057 - 研究结论与复盘](02-Quant-Research-Project/IC057-%E7%A0%94%E7%A9%B6%E7%BB%93%E8%AE%BA%E4%B8%8E%E5%A4%8D%E7%9B%98.md)
- [IC058 - Quant项目总交付](02-Quant-Research-Project/IC058-Quant%E9%A1%B9%E7%9B%AE%E6%80%BB%E4%BA%A4%E4%BB%98.md)
- [IC059 - Quant简历表达](02-Quant-Research-Project/IC059-Quant%E7%AE%80%E5%8E%86%E8%A1%A8%E8%BE%BE.md)

### LLM Application Project

最终项目：RAG Knowledge Assistant。

- [IC060 - Prompt任务边界](03-LLM-Application-Project/IC060-Prompt%E4%BB%BB%E5%8A%A1%E8%BE%B9%E7%95%8C.md)
- [IC061 - Context输入整理](03-LLM-Application-Project/IC061-Context%E8%BE%93%E5%85%A5%E6%95%B4%E7%90%86.md)
- [IC062 - 文档数据集构造](03-LLM-Application-Project/IC062-%E6%96%87%E6%A1%A3%E6%95%B0%E6%8D%AE%E9%9B%86%E6%9E%84%E9%80%A0.md)
- [IC063 - 文本清洗与切分](03-LLM-Application-Project/IC063-%E6%96%87%E6%9C%AC%E6%B8%85%E6%B4%97%E4%B8%8E%E5%88%87%E5%88%86.md)
- [IC064 - Embedding认知地图](03-LLM-Application-Project/IC064-Embedding%E8%AE%A4%E7%9F%A5%E5%9C%B0%E5%9B%BE.md)
- [IC065 - 向量索引](03-LLM-Application-Project/IC065-%E5%90%91%E9%87%8F%E7%B4%A2%E5%BC%95.md)
- [IC066 - 向量检索TopK](03-LLM-Application-Project/IC066-%E5%90%91%E9%87%8F%E6%A3%80%E7%B4%A2TopK.md)
- [IC067 - RAG上下文打包](03-LLM-Application-Project/IC067-RAG%E4%B8%8A%E4%B8%8B%E6%96%87%E6%89%93%E5%8C%85.md)
- [IC068 - 引用回答](03-LLM-Application-Project/IC068-%E5%BC%95%E7%94%A8%E5%9B%9E%E7%AD%94.md)
- [IC069 - 结构化输出](03-LLM-Application-Project/IC069-%E7%BB%93%E6%9E%84%E5%8C%96%E8%BE%93%E5%87%BA.md)
- [IC070 - LLM评估集](03-LLM-Application-Project/IC070-LLM%E8%AF%84%E4%BC%B0%E9%9B%86.md)
- [IC071 - 错误案例库](03-LLM-Application-Project/IC071-%E9%94%99%E8%AF%AF%E6%A1%88%E4%BE%8B%E5%BA%93.md)
- [IC072 - 成本缓存与延迟](03-LLM-Application-Project/IC072-%E6%88%90%E6%9C%AC%E7%BC%93%E5%AD%98%E4%B8%8E%E5%BB%B6%E8%BF%9F.md)
- [IC073 - 隐私脱敏](03-LLM-Application-Project/IC073-%E9%9A%90%E7%A7%81%E8%84%B1%E6%95%8F.md)
- [IC074 - RAG Streamlit Demo](03-LLM-Application-Project/IC074-RAG-Streamlit-Demo.md)
- [IC075 - README与截图](03-LLM-Application-Project/IC075-README%E4%B8%8E%E6%88%AA%E5%9B%BE.md)
- [IC076 - 失败案例复盘](03-LLM-Application-Project/IC076-%E5%A4%B1%E8%B4%A5%E6%A1%88%E4%BE%8B%E5%A4%8D%E7%9B%98.md)
- [IC077 - RAG Knowledge Assistant总交付](03-LLM-Application-Project/IC077-RAG-Knowledge-Assistant%E6%80%BB%E4%BA%A4%E4%BB%98.md)
- [IC078 - LLM项目简历表达](03-LLM-Application-Project/IC078-LLM%E9%A1%B9%E7%9B%AE%E7%AE%80%E5%8E%86%E8%A1%A8%E8%BE%BE.md)
- [IC079 - LLM面试讲解脚本](03-LLM-Application-Project/IC079-LLM%E9%9D%A2%E8%AF%95%E8%AE%B2%E8%A7%A3%E8%84%9A%E6%9C%AC.md)

### Agent Workflow Project

最终项目：Agent Workflow System。

- [IC080 - Tool契约设计](04-Agent-Workflow-Project/IC080-Tool%E5%A5%91%E7%BA%A6%E8%AE%BE%E8%AE%A1.md)
- [IC081 - 工具Schema校验](04-Agent-Workflow-Project/IC081-%E5%B7%A5%E5%85%B7Schema%E6%A0%A1%E9%AA%8C.md)
- [IC082 - 工具路由](04-Agent-Workflow-Project/IC082-%E5%B7%A5%E5%85%B7%E8%B7%AF%E7%94%B1.md)
- [IC083 - 执行器](04-Agent-Workflow-Project/IC083-%E6%89%A7%E8%A1%8C%E5%99%A8.md)
- [IC084 - 状态存储](04-Agent-Workflow-Project/IC084-%E7%8A%B6%E6%80%81%E5%AD%98%E5%82%A8.md)
- [IC085 - Memory设计](04-Agent-Workflow-Project/IC085-Memory%E8%AE%BE%E8%AE%A1.md)
- [IC086 - Planning最小流程](04-Agent-Workflow-Project/IC086-Planning%E6%9C%80%E5%B0%8F%E6%B5%81%E7%A8%8B.md)
- [IC087 - Human in the Loop](04-Agent-Workflow-Project/IC087-Human-in-the-Loop.md)
- [IC088 - 日志与可观测性](04-Agent-Workflow-Project/IC088-%E6%97%A5%E5%BF%97%E4%B8%8E%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7.md)
- [IC089 - 错误恢复](04-Agent-Workflow-Project/IC089-%E9%94%99%E8%AF%AF%E6%81%A2%E5%A4%8D.md)
- [IC090 - 多步骤Workflow](04-Agent-Workflow-Project/IC090-%E5%A4%9A%E6%AD%A5%E9%AA%A4Workflow.md)
- [IC091 - 文件工具与安全边界](04-Agent-Workflow-Project/IC091-%E6%96%87%E4%BB%B6%E5%B7%A5%E5%85%B7%E4%B8%8E%E5%AE%89%E5%85%A8%E8%BE%B9%E7%95%8C.md)
- [IC092 - API工具与失败处理](04-Agent-Workflow-Project/IC092-API%E5%B7%A5%E5%85%B7%E4%B8%8E%E5%A4%B1%E8%B4%A5%E5%A4%84%E7%90%86.md)
- [IC093 - Agent评估集](04-Agent-Workflow-Project/IC093-Agent%E8%AF%84%E4%BC%B0%E9%9B%86.md)
- [IC094 - 成本与延迟控制](04-Agent-Workflow-Project/IC094-%E6%88%90%E6%9C%AC%E4%B8%8E%E5%BB%B6%E8%BF%9F%E6%8E%A7%E5%88%B6.md)
- [IC095 - 演示与截图](04-Agent-Workflow-Project/IC095-%E6%BC%94%E7%A4%BA%E4%B8%8E%E6%88%AA%E5%9B%BE.md)
- [IC096 - Agent Workflow System总交付](04-Agent-Workflow-Project/IC096-Agent-Workflow-System%E6%80%BB%E4%BA%A4%E4%BB%98.md)
- [IC097 - Agent项目简历表达](04-Agent-Workflow-Project/IC097-Agent%E9%A1%B9%E7%9B%AE%E7%AE%80%E5%8E%86%E8%A1%A8%E8%BE%BE.md)
- [IC098 - AI Native Builder作品集](04-Agent-Workflow-Project/IC098-AI-Native-Builder%E4%BD%9C%E5%93%81%E9%9B%86.md)
- [IC099 - IC100最终复盘](04-Agent-Workflow-Project/IC099-IC100%E6%9C%80%E7%BB%88%E5%A4%8D%E7%9B%98.md)
- [IC100 - GitHub作品集总整理](04-Agent-Workflow-Project/IC100-GitHub%E4%BD%9C%E5%93%81%E9%9B%86%E6%80%BB%E6%95%B4%E7%90%86.md)

## 最终产出

- 4 个 GitHub 项目：LLM Evaluation Analytics Platform、Quant Research Framework、RAG Knowledge Assistant、Agent Workflow System。
- 每个项目都有 README、运行说明、截图、复盘和简历描述。
- 算法刷题记录单独沉淀在 `leetcode（hot code）300`。
