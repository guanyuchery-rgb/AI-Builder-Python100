# Day22 - Matplotlib 多图与保存

> 阶段三：数据分析三大库

## 学习定位

今天把 Matplotlib 从“一张图”升级到“多图布局”：**同一份数据可以同时展示趋势和分布**。

## 认知地图

| 工具 | 输入 | 输出 | 用途 |
| --- | --- | --- | --- |
| `plt.subplots(1, 2)` | 行列数 | 多个 ax | 多图布局 |
| `ax.hist()` | 一列数值 | 直方图 | 分布 |
| `ax.scatter()` | x/y | 散点图 | 关系 |
| `fig.tight_layout()` | figure | 调整布局 | 避免重叠 |

## What

多图不是为了花哨，而是为了同时回答多个问题：

- 趋势是什么？
- 分布是什么？
- 两个变量有没有关系？

## Why

单张图容易片面。数据分析里常见组合：

- 折线图看时间趋势。
- 直方图看分布。
- 柱状图看组间对比。
- 散点图看两个变量关系。

## How：一份数据，多张图

```text
DataFrame
  ↓
取列
  ↓
subplots
  ↓
plot / hist / scatter
  ↓
savefig
```

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 多图标题重叠 | 图难看 | `tight_layout()` |
| x/y 长度不同 | 报错 | 先检查长度 |
| 图太小 | 字挤在一起 | 设置 `figsize` |

## 今日强化题（带具体代码）

### 强化题 1：保存一张双图

验收：生成 `dashboard.png` 或 fallback 文本。

### 参考代码：`main.py`

```python
from pathlib import Path
import json
import pandas as pd

DAY = 22
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


def save_dashboard(df, path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        fallback = path.with_suffix(".txt")
        fallback.write_text(
            "matplotlib unavailable\\n"
            f"error={type(exc).__name__}: {exc}\\n"
            f"data={df.to_dict(orient='records')}\\n",
            encoding="utf-8",
        )
        return {"ok": False, "fallback": str(fallback), "error": str(exc)}

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))
    axes[0].plot(df["step"], df["value"], marker="o")
    axes[0].set_title("Trend")
    axes[0].set_xlabel("step")
    axes[0].set_ylabel("value")

    axes[1].hist(df["value"], bins=4)
    axes[1].set_title("Distribution")
    axes[1].set_xlabel("value")
    axes[1].set_ylabel("count")

    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return {"ok": True, "image": str(path)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame({
        "step": [1, 2, 3, 4, 5, 6],
        "value": [10, 13, 9, 16, 14, 18],
    })
    result = save_dashboard(df, OUT / "dashboard.png")
    payload = {
        "topic": "matplotlib multi plot and savefig",
        "rows": len(df),
        "plot_result": result,
    }
    (OUT / "dashboard_report.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day22：Matplotlib 多图与保存

subplots 的输入输出：
hist 看什么：
plot 看什么：
tight_layout 的作用：
```
