# IC017 - logging与Debug日志

> Python100 x IC100 最终版：Day100 负责知识体系，IC100 负责能力体系。

## 1. 今日定位

- 所属阶段：基础能力启动
- 学习目标：统计学硕士 -> AI Native Builder -> Agent / LLM / Quant 方向实习求职。
- 今日原则：不做学生管理系统、通讯录、猜数字等低求职价值项目；所有练习都服务数据、Quant、LLM、Agent 和 GitHub 作品集。

## 2. Part A - LeetCode 2 题

每天只做 2 题。目标是高质量 200 题，而不是低质量刷数量。

### A1. [binary-tree-postorder-traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

- 难度：Easy
- 类型：树 / DFS / BFS
- 为什么做：这题训练 `树 / DFS / BFS` 的基本面试表达，同时帮助你把 Python 数据结构用熟。
- 思路：把树问题拆成“当前节点做什么”和“左右子树返回什么”。
- 解题步骤：
   1. 确定递归函数输入输出。
   2. 写空节点 base case。
   3. 合并左右子树结果，或用队列按层处理。
- 易错点：递归返回值语义不清，会导致左右子树结果混在一起。
- 做题记录要求：在 LeetCode 官方页面提交，通过后把通过截图或提交记录链接写进当天 `review.md`。

### A2. [intersection-of-two-linked-lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

- 难度：Easy
- 类型：链表
- 为什么做：这题训练 `链表` 的基本面试表达，同时帮助你把 Python 数据结构用熟。
- 思路：把节点关系当成指针重连问题，优先使用 dummy 节点降低头结点特判。
- 解题步骤：
   1. 画出当前节点、前驱节点、后继节点。
   2. 先保存 next，再改指针。
   3. 最后返回 dummy.next 或新的 head。
- 易错点：改指针前丢失 next，会导致后续链表断掉。
- 做题记录要求：在 LeetCode 官方页面提交，通过后把通过截图或提交记录链接写进当天 `review.md`。

## 3. Part B - 强化任务

### B1. 今日任务

把 Day 学到的「logging与Debug日志」做成一个可运行小脚本，保留 `main.py`、`notes.md`、`errors.md`。

### B2. 输入

- 最近 Day 学到的知识点。
- 前一个 IC 留下的代码、数据、README 或 review。
- 一个足够小、能在本地运行的样例。

### B3. 输出

- `main.py`
- `notes.md`
- `errors.md`
- `README.md`

### B4. 工业操作步骤

1. 写清今天要解决的问题，不超过 3 句话。
2. 建立最小目录和最小输入，不提前做大系统。
3. 写最小可运行代码，优先保证能跑通。
4. 保存输出文件、截图或日志。
5. 更新 README 或 review，说明今天做了什么、怎么复现、哪里还不稳。

### B5. GitHub 提交要求

```text
IC017: logging与Debug日志
```

提交必须包含：代码或文档、运行结果、Debug 记录、两道 LeetCode 复盘。

## 4. Part C - Review

```text
IC编号：IC017
主题：logging与Debug日志
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

> 我在 `基础能力启动` 中完成 `logging与Debug日志` 阶段，能把知识点转化为可运行代码、可复现输出和可解释复盘。
