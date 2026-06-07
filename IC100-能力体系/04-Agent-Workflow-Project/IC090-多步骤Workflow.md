# IC090 - 多步骤Workflow

> Python100 x IC100 最终版：Day100 负责知识体系，IC100 负责能力体系。

## 1. 今日定位

- 所属阶段：Agent Workflow Project
- 学习目标：统计学硕士 -> AI Native Builder -> Agent / LLM / Quant 方向实习求职。
- 今日原则：不做学生管理系统、通讯录、猜数字等低求职价值项目；所有练习都服务数据、Quant、LLM、Agent 和 GitHub 作品集。

## 2. Part A - LeetCode 2 题

每天只做 2 题。目标是高质量 200 题，而不是低质量刷数量。

### A1. [find-all-anagrams-in-a-string](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

- 难度：Medium
- 类型：字符串 / 滑动窗口
- 为什么做：这题训练 `字符串 / 滑动窗口` 的基本面试表达，同时帮助你把 Python 数据结构用熟。
- 思路：用左右边界表达当前区间，避免重复切片和多层循环。
- 解题步骤：
   1. 定义窗口或左右指针含义。
   2. 移动一个边界后立刻维护状态。
   3. 每一步都确认答案在何时更新。
- 易错点：窗口收缩条件写反，容易漏掉最后一个合法区间。
- 做题记录要求：在 LeetCode 官方页面提交，通过后把通过截图或提交记录链接写进当天 `review.md`。

### A2. [target-sum](https://leetcode.com/problems/target-sum/)

- 难度：Medium
- 类型：动态规划 / 前缀和
- 为什么做：这题训练 `动态规划 / 前缀和` 的基本面试表达，同时帮助你把 Python 数据结构用熟。
- 思路：把重复子问题保存下来，用状态转移替代重复搜索。
- 解题步骤：
   1. 定义 dp[i] 的含义。
   2. 写初始状态。
   3. 写从旧状态到新状态的转移，并检查顺序。
- 易错点：dp 含义写成“答案大概是什么”，后面转移会失控。
- 做题记录要求：在 LeetCode 官方页面提交，通过后把通过截图或提交记录链接写进当天 `review.md`。

## 3. Part B - 强化任务

### B1. 今日任务

围绕 Agent Workflow System，完成「多步骤Workflow」阶段，所有工具调用、状态变化和人工审查都要可追踪。

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
IC090: 多步骤Workflow
```

提交必须包含：代码或文档、运行结果、Debug 记录、两道 LeetCode 复盘。

## 4. Part C - Review

```text
IC编号：IC090
主题：多步骤Workflow
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

> 我在 `Agent Workflow Project` 中完成 `多步骤Workflow` 阶段，能把知识点转化为可运行代码、可复现输出和可解释复盘。
