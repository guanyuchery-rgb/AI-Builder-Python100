# IC097 - Agent项目简历表达

> Python100 x IC100 最终版：Day100 负责知识体系，IC100 负责能力体系。

## 1. 今日定位

- 所属阶段：Agent Workflow Project
- 学习目标：统计学硕士 -> AI Native Builder -> Agent / LLM / Quant 方向实习求职。
- 今日原则：不做学生管理系统、通讯录、猜数字等低求职价值项目；所有练习都服务数据、Quant、LLM、Agent 和 GitHub 作品集。

## 2. Part A - LeetCode 2 题

每天只做 2 题。目标是高质量 200 题，而不是低质量刷数量。

### A1. [is-graph-bipartite](https://leetcode.com/problems/is-graph-bipartite/)

- 难度：Medium
- 类型：图 / BFS / DFS
- 为什么做：这题训练 `图 / BFS / DFS` 的基本面试表达，同时帮助你把 Python 数据结构用熟。
- 思路：把树问题拆成“当前节点做什么”和“左右子树返回什么”。
- 解题步骤：
   1. 确定递归函数输入输出。
   2. 写空节点 base case。
   3. 合并左右子树结果，或用队列按层处理。
- 易错点：递归返回值语义不清，会导致左右子树结果混在一起。
- 做题记录要求：在 LeetCode 官方页面提交，通过后把通过截图或提交记录链接写进当天 `review.md`。

### A2. [binary-subarrays-with-sum](https://leetcode.com/problems/binary-subarrays-with-sum/)

- 难度：Medium
- 类型：二分 / 搜索
- 为什么做：这题训练 `二分 / 搜索` 的基本面试表达，同时帮助你把 Python 数据结构用熟。
- 思路：在有序答案空间里不断排除一半，关键是判断函数单调。
- 解题步骤：
   1. 写清搜索区间含义。
   2. 计算 mid 并判断答案在左边还是右边。
   3. 循环结束后检查边界是否仍合法。
- 易错点：left/right 更新不收缩，会出现死循环。
- 做题记录要求：在 LeetCode 官方页面提交，通过后把通过截图或提交记录链接写进当天 `review.md`。

## 3. Part B - 强化任务

### B1. 今日任务

围绕 Agent Workflow System，完成「Agent项目简历表达」阶段，所有工具调用、状态变化和人工审查都要可追踪。

### B2. 输入

- 最近 Day 学到的知识点。
- 前一个 IC 留下的代码、数据、README 或 review。
- 一个足够小、能在本地运行的样例。

### B3. 输出

- `src/tools.py 或 src/workflow.py`
- `outputs/agent/*.jsonl`
- `review_notes.md`
- `README.md`

### B4. 工业操作步骤

1. 写清今天要解决的问题，不超过 3 句话。
2. 建立最小目录和最小输入，不提前做大系统。
3. 写最小可运行代码，优先保证能跑通。
4. 保存输出文件、截图或日志。
5. 更新 README 或 review，说明今天做了什么、怎么复现、哪里还不稳。

### B5. GitHub 提交要求

```text
IC097: Agent项目简历表达
```

提交必须包含：代码或文档、运行结果、Debug 记录、两道 LeetCode 复盘。

## 4. Part C - Review

```text
IC编号：IC097
主题：Agent项目简历表达
完成日期：

今天学到什么：
今天犯了什么错：
我是怎么 Debug 的：
下次如何优化：
LeetCode 题目1提交记录：
LeetCode 题目2提交记录：
GitHub commit：
```

## 5. 求职沉淀

用一句话写进长期作品集：

> 我在 `Agent Workflow Project` 中完成 `Agent项目简历表达` 阶段，能把知识点转化为可运行代码、可复现输出和可解释复盘。
