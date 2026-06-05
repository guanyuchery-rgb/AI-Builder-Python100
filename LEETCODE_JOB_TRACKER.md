# LeetCode 求职刷题记录

这个表用于把刷题变成可长期复用的求职资产。

做题时优先点击课程里的 LeetCode 官方链接，并登录自己的 LeetCode 账号提交。

这样平台会留下提交记录、Accepted 记录、日历和题目进度。

本文件只记录复盘、迁移和面试表达，不替代 LeetCode 官方提交记录。

课程 Day11-Day100 覆盖 100 道左右独立 LeetCode 官方题目，共 720 个分层训练位。

前期优先做「必做」题。

中期逐步做「选做」题。

后期再处理「挑战」题。

求职准备时，优先把其中至少 60 道做到 Accepted，并保留官方提交记录；如果时间充足，再逐步冲到 100 道。

## 使用方式

1. 在当天课程里点击 LeetCode 官方题目链接。
2. 在 LeetCode 上提交代码，尽量拿到 Accepted。
3. 回到当天课程，填写「做题复盘模板」。
4. 把值得长期保留的题目复制到下面总表。
5. 面试前按题型筛选，集中复习解法、边界和项目迁移点。

## 总表

| Day | 题目 | 官方链接 | 题型 | 状态 | 提交日期 | 最优解法 | 复杂度 | 面试表达 | 项目迁移点 |
|---|---|---|---|---|---|---|---|---|---|
| Day11 | Two Sum | https://leetcode.com/problems/two-sum/ | 数组 / 哈希表 | 未做 |  | 哈希表一次遍历 | O(n) / O(n) | 用哈希表把查找从线性降到常数级 | 去重、匹配、索引构建 |
| Day11 | Contains Duplicate | https://leetcode.com/problems/contains-duplicate/ | 集合 / 去重 | 未做 |  | set 扫描 | O(n) / O(n) | 用集合维护已见状态 | 重复任务检测、幂等检查 |
| Day11 | Valid Anagram | https://leetcode.com/problems/valid-anagram/ | 字符串 / 计数 | 未做 |  | Counter | O(n) / O(k) | 用频次表比较两个对象结构 | 文本特征、标签统计 |
| Day11 | Valid Palindrome | https://leetcode.com/problems/valid-palindrome/ | 双指针 | 未做 |  | 双指针 | O(n) / O(1) | 在扫描中跳过无效字符并保持边界正确 | 文本清洗、输入校验 |
| Day11 | Best Time to Buy and Sell Stock | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ | 数组 / Quant | 未做 |  | 历史最低价 | O(n) / O(1) | 避免未来函数，只用历史信息决策 | 回测、收益率分析 |
| Day11 | Subarray Sum Equals K | https://leetcode.com/problems/subarray-sum-equals-k/ | 前缀和 / 哈希表 | 未做 |  | 前缀和计数字典 | O(n) / O(n) | 把区间问题转成状态差问题 | 时间窗口、累计指标 |

## 复盘字段说明

- 状态：未做 / 已尝试 / Accepted / 需二刷。
- 最优解法：写自己真正理解并能复现的解法。
- 复杂度：格式使用 `时间 / 空间`。
- 面试表达：用一句话说清这题训练了什么能力。
- 项目迁移点：写这题能迁移到数据分析、Quant、LLM、Agent 或工程工具的哪个场景。

## 面试前筛选

优先复习这几类：

- 哈希表：Two Sum、Contains Duplicate、Valid Anagram。
- 双指针：Valid Palindrome、盛水类、区间类。
- 前缀和：Subarray Sum Equals K。
- 栈：Valid Parentheses。
- 二分：Binary Search。
- 树和图：Maximum Depth of Binary Tree、Number of Islands。
- 动态规划：Climbing Stairs、Coin Change。

## 简历表达模板

```text
系统刷题并复盘 Python 数据结构与算法题，覆盖哈希表、双指针、栈、二分、树、图、动态规划等主题。
将算法题迁移到数据清洗、日志统计、Quant 回测、RAG 检索和 Agent tool 输入输出设计中。
```
