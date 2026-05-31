# Day15 - Excel、PDF、图像与办公自动化

学习定位：掌握常见办公文件的自动化处理思维，为数据分析、报告生成、研报处理和 LLM 文档工作流打基础。

## 2小时安排

- 20 分钟：理解办公文件自动化的边界。
- 30 分钟：用 CSV 模拟 Excel 数据处理。
- 30 分钟：理解 PDF/图片处理流程。
- 25 分钟：设计一个报告生成小流程。
- 15 分钟：记录 LLM 文档处理注意事项。

## 知识点 1：表格文件处理

### 定义

表格文件处理是读取、清洗、汇总和输出结构化数据。早期可以先用 CSV，之后再扩展到 Excel。

### 为什么存在

金融、运营、研究和学习资料大量存在于 Excel/CSV 中。

### 最小案例

```python
import csv
from pathlib import Path

rows = [
    {"symbol": "AAPL", "return": "0.05"},
    {"symbol": "MSFT", "return": "0.03"},
]

path = Path("returns.csv")
with path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["symbol", "return"])
    writer.writeheader()
    writer.writerows(rows)

with path.open(encoding="utf-8") as file:
    reader = csv.DictReader(file)
    returns = [float(row["return"]) for row in reader]

print(f"平均收益率: {sum(returns) / len(returns):.2%}")
```

### 常见错误

- Excel 和 CSV 混淆。
- 数字被读成字符串。
- 中文编码乱码。
- 空值没有处理。

### 工程应用

- 批量处理报表。
- 数据清洗。
- 研究结果导出。
- 自动生成报告数据。

### 未来扩展

- `openpyxl`。
- `pandas.read_excel`。
- 报告模板。

## 知识点 2：PDF、图像与文档工作流

### 定义

PDF 和图像处理通常包括提取文本、提取表格、OCR、压缩、转换和生成报告。

### 为什么存在

研报、公告、账单、截图、扫描件都不是天然适合数据分析的格式。

### 最小流程

```text
PDF/图片
-> 提取文本或表格
-> 清洗字段
-> 保存 CSV/JSON
-> 交给 Python 分析或 LLM 总结
```

### 常见错误

- 以为所有 PDF 都能直接提取文本。
- 扫描 PDF 需要 OCR。
- 表格提取后列名错位。
- LLM 总结前没有保留来源页码。

### 工程应用

- 研报摘要。
- 公告事件提取。
- 财报数据整理。
- 文档问答知识库。

### 未来扩展

- `pdfplumber`。
- OCR。
- 文档切分 chunking。
- RAG。

## Debug 日志

- 表格字段错位：先打印原始行。
- 中文乱码：检查编码。
- PDF 提取为空：判断是否扫描件。
- LLM 摘要不可信：保留原文片段和页码。


## 面试角度 Interview

办公自动化不是“会操作文件”而已，重点是把非结构化/半结构化材料变成可复现的数据流程。

## Quant 关联

财报、公告、研报、策略结果都可能从 Excel/PDF 来。自动化处理能减少手工复制错误。

## LLM / Agent 关联

LLM 文档问答前必须先处理来源、切分、结构化和验证。Agent 可以自动跑文档处理流程，但必须保留来源证据。

## 复习检查

- [ ] 我能用 CSV 模拟表格处理。
- [ ] 我知道 Excel/PDF/图片处理的差异。
- [ ] 我能设计一个文档到数据的流程。
- [ ] 我知道 LLM 总结文档要保留来源。

## 简单路线 7 题（不超前）

只用今天及之前学过的能力。做不出来时，先回看当天最小案例，不跳到后面知识。

1. 写一个普通同步函数。
2. 给函数加超时/失败说明。
3. 请求一个公开 JSON 或模拟 JSON。
4. 把 API 返回字段安全读取出来。
5. 列出一个文件夹中的目标文件。
6. 生成一个 Markdown 小报告。
7. 记录一次网络或文件路径错误。
## 题目驱动训练

### 参考题 / 资料

- [Python csv docs](https://docs.python.org/3/library/csv.html)
- [Python pathlib docs](https://docs.python.org/3/library/pathlib.html)
- [openpyxl documentation](https://openpyxl.readthedocs.io/)

### 5 道递进题

#### 1. Easy - CSV 读取成 dict

题目：把 CSV 文本读取成行列表。

讲解：Excel 能力先从表格数据结构开始，不急着操作界面。

```python
import csv
from io import StringIO

def read_csv_rows(text: str) -> list[dict]:
    # DictReader 会用表头作为 key
    return list(csv.DictReader(StringIO(text)))
```

#### 2. Easy - 生成汇总 CSV

题目：把 summary dict 写成 CSV 文本。

讲解：输出能被 Excel 打开，就是最小办公自动化。

```python
import csv
from io import StringIO

def summary_to_csv(summary: dict[str, float]) -> str:
    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["metric", "value"])
    for key, value in summary.items():
        writer.writerow([key, value])
    return buffer.getvalue()
```

#### 3. Medium - 收集 PDF 文件

题目：列出目录下所有 PDF 路径。

讲解：办公自动化经常先做文件发现和分类。

```python
from pathlib import Path

def list_pdfs(folder: str) -> list[Path]:
    root = Path(folder)
    return sorted(root.glob("*.pdf"))
```

#### 4. Medium - 图片清单 manifest

题目：生成图片文件清单，包含文件名和后缀。

讲解：先建立资产索引，再决定是否压缩、识别或归档。

```python
from pathlib import Path

def build_image_manifest(folder: str) -> list[dict[str, str]]:
    exts = {".png", ".jpg", ".jpeg"}
    rows = []
    for path in Path(folder).iterdir():
        if path.suffix.lower() in exts:
            rows.append({"name": path.name, "suffix": path.suffix.lower()})
    return rows
```

#### 5. Hard - 自动化报告索引

题目：把 PDF、图片、CSV 结果组合成 Markdown 报告。

讲解：项目交付可以先用 Markdown 作为轻量报告层。

```python
from pathlib import Path

def build_report_index(files: list[Path], summary: dict[str, float]) -> str:
    lines = ["# 自动化报告", "", "## 指标"]
    for key, value in summary.items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## 文件"])
    for file in files:
        lines.append(f"- {file.name}")
    return "\n".join(lines)
```
