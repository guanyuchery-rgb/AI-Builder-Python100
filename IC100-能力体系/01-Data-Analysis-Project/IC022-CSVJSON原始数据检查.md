# IC022 - CSVJSON原始数据检查

> Python100 x IC100 最终版：Day100 负责知识体系，IC100 负责能力体系。

## 1. 今日定位

- 所属阶段：Data Analysis Project
- 学习目标：统计学硕士 -> AI Native Builder -> Agent / LLM / Quant 方向实习求职。
- 今日原则：不做学生管理系统、通讯录、猜数字等低求职价值项目；所有练习都服务数据、Quant、LLM、Agent 和 GitHub 作品集。

## 2. Part A - LeetCode 2 题

每天只做 2 题。目标是高质量 200 题，而不是低质量刷数量。

### A1. [reverse-linked-list](https://leetcode.com/problems/reverse-linked-list/)

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

### A2. [contains-duplicate](https://leetcode.com/problems/contains-duplicate/)

- 难度：Easy
- 类型：哈希表 / 计数
- 为什么做：这题训练 `哈希表 / 计数` 的基本面试表达，同时帮助你把 Python 数据结构用熟。
- 思路：把“查找是否出现过”改成字典或集合查询，用空间换时间。
- 解题步骤：
   1. 明确 key 是什么，value 存什么。
   2. 遍历时先查旧状态，再更新新状态。
   3. 注意重复值、下标和计数边界。
- 易错点：先更新再查询可能把当前元素和自己配对。
- 做题记录要求：在 LeetCode 官方页面提交，通过后把通过截图或提交记录链接写进当天 `review.md`。

## 3. Part B - 强化任务

### B1. 今日任务

围绕电商用户行为分析，完成「CSVJSON原始数据检查」阶段，让数据从原始文件逐步走向报告和 Dashboard。

### B2. 输入

- 最近 Day 学到的知识点。
- 前一个 IC 留下的代码、数据、README 或 review。
- 一个足够小、能在本地运行的样例。

### B3. 输出

- `src/`
- `data/raw 或 data/processed`
- `outputs/reports/`
- `README.md`

### B4. 工业操作步骤

1. 写清今天要解决的问题，不超过 3 句话。
2. 建立最小目录和最小输入，不提前做大系统。
3. 写最小可运行代码，优先保证能跑通。
4. 保存输出文件、截图或日志。
5. 更新 README 或 review，说明今天做了什么、怎么复现、哪里还不稳。

### B5. GitHub 提交要求

```text
IC022: CSVJSON原始数据检查
```

提交必须包含：代码或文档、运行结果、Debug 记录、两道 LeetCode 复盘。

## 4. Part C - Review

```text
IC编号：IC022
主题：CSVJSON原始数据检查
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

> 我在 `Data Analysis Project` 中完成 `CSVJSON原始数据检查` 阶段，能把知识点转化为可运行代码、可复现输出和可解释复盘。
