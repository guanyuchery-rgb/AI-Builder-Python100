# Day21 - Matplotlib 基础图表

> 阶段三：数据分析三大库

## 学习定位

今天学习 Matplotlib：**把数据变成可复查的图表文件**。

本机环境如果 Matplotlib 暂时不可用，参考代码会自动降级保存文本报告，保证学习不中断。

## 认知地图

| 工具 | 输入 | 输出 | 用途 |
| --- | --- | --- | --- |
| `plt.subplots()` | 画布参数 | fig, ax | 创建图 |
| `ax.plot()` | x/y | 折线 | 趋势 |
| `ax.bar()` | 类别/数值 | 柱状图 | 对比 |
| `fig.savefig()` | 路径 | 图片文件 | 保存 |

## What

Matplotlib 是 Python 最基础的绘图库。它关注三层：

```text
figure 整张图
axis/ax 一个子图
plot/bar/scatter 图形元素
```

## Why

数据分析不能只给表。图表能更快暴露趋势、异常、分组差异。

## How：数据 -> 图表 -> 文件

```text
x/y 数据
  ↓
fig, ax
  ↓
ax.plot / ax.bar
  ↓
title / labels
  ↓
savefig
```

## Common Errors

| 错误 | 表现 | 修法 |
| --- | --- | --- |
| 图只 show 不保存 | 结果不可复查 | 固定 `savefig` |
| 标签缺失 | 图看不懂 | 加 title/xlabel/ylabel |
| 环境依赖坏 | import 报错 | 先保存 fallback 报告 |

## 今日强化题（带具体代码）

### 强化题 1：保存一张趋势图

验收：环境正常时生成 PNG；环境异常时生成 fallback 文本。

### 参考代码：`main.py`

```python
from pathlib import Path
import json

DAY = 21
OUT = Path(__file__).resolve().parent / "outputs" / f"day{DAY:03d}"


def save_line_plot(x, y, path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        fallback = path.with_suffix(".txt")
        fallback.write_text(f"matplotlib unavailable: {type(exc).__name__}: {exc}\\nx={x}\\ny={y}\\n", encoding="utf-8")
        return {"ok": False, "fallback": str(fallback), "error": str(exc)}

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, marker="o")
    ax.set_title("Value Trend")
    ax.set_xlabel("step")
    ax.set_ylabel("value")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return {"ok": True, "image": str(path)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 9, 15, 18]
    result = save_line_plot(x, y, OUT / "line_plot.png")
    payload = {"topic": "matplotlib basic line plot", "plot_result": result}
    (OUT / "plot_report.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

## 今日复盘模板

```text
Day21：Matplotlib 基础图表

figure 和 ax 是什么：
plot 的输入是什么：
为什么要保存图片：
我的环境是否能正常生成 PNG：
```
