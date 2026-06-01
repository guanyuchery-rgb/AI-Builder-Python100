from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_DIR = ROOT / "Python工业化学习100框架"
DOCS_DIR = ROOT / "docs"


def course_files() -> list[Path]:
    def day_number(path: Path) -> int:
        match = re.match(r"(\d+)-", path.name)
        return int(match.group(1)) if match else 9999

    return sorted(COURSE_DIR.glob("[0-9]*-*.md"), key=day_number)


def rewrite_links(text: str) -> str:
    def obsidian_link(match: re.Match[str]) -> str:
        target = match.group(1)
        if "|" in target:
            file_name, label = target.split("|", 1)
        else:
            file_name = target
            label = target
        if not file_name.endswith(".md"):
            file_name += ".md"
        return f"[{label}](Python工业化学习100框架/{file_name})"

    return re.sub(r"\[\[([^\]]+)\]\]", obsidian_link, text)


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    in_code = False
    in_list = False
    code_lines: list[str] = []
    i = 0

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            output.append("</ul>")
            in_list = False

    def inline(text: str) -> str:
        escaped = html.escape(text)
        escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
        escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
        escaped = re.sub(
            r"\[([^\]]+)\]\((https?://[^)]+)\)",
            r'<a href="\2">\1</a>',
            escaped,
        )
        return escaped

    def is_table_separator(line: str) -> bool:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)

    def render_table(table_lines: list[str]) -> str:
        rows = [
            [inline(cell.strip()) for cell in line.strip().strip("|").split("|")]
            for line in table_lines
        ]
        header = "".join(f"<th>{cell}</th>" for cell in rows[0])
        body_rows = []
        for row in rows[2:]:
            body_rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
        return "<table><thead><tr>" + header + "</tr></thead><tbody>" + "".join(body_rows) + "</tbody></table>"

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            if not in_code:
                close_list()
                in_code = True
                code_lines = []
            else:
                output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                in_code = False
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not line.strip():
            close_list()
            i += 1
            continue

        if (
            line.strip().startswith("|")
            and i + 1 < len(lines)
            and is_table_separator(lines[i + 1])
        ):
            close_list()
            table_lines = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            output.append(render_table(table_lines))
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            close_list()
            level = len(heading.group(1))
            text = inline(heading.group(2))
            output.append(f"<h{level}>{text}</h{level}>")
            i += 1
            continue

        if line.startswith("- "):
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(f"<li>{inline(line[2:])}</li>")
            i += 1
            continue

        close_list()
        output.append(f"<p>{inline(line)}</p>")
        i += 1

    close_list()
    return "\n".join(output)


def build_mobile_markdown() -> None:
    lines = [
        "# AI Builder Python100 手机学习入口",
        "",
        "这是开源 Python100 课程的手机端入口。每天打开一个 Day，按 2 小时节奏完成：读定位、跑最小案例、做 7 道简单题 + 5 道基础巩固题、记录 Debug。",
        "",
        "## 学习入口",
        "",
        "- [成长路线图 GROWTH_ROADMAP](GROWTH_ROADMAP.md)",
        "- [课程地图 COURSE_MAP](COURSE_MAP.md)",
        "- [Python工业化学习100框架 README](Python工业化学习100框架/README.md)",
    ]
    for path in course_files():
        title = path.stem
        lines.append(f"- [{title}](Python工业化学习100框架/{path.name})")
    lines.extend(
        [
            "",
            "## 使用方式",
            "",
            "- 手机上优先看这个文件或 GitHub Pages 网页。",
            "- Mac 上继续用 Obsidian 打开原 Vault。",
            "- 每天只追求一个稳定的小进步。",
        ]
    )
    (ROOT / "MOBILE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_index_html() -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    nav = []
    articles = []
    roadmap = ROOT / "GROWTH_ROADMAP.md"
    if roadmap.exists():
        nav.append('<a href="#growth-roadmap">成长路线图</a>')
        body = markdown_to_html(roadmap.read_text(encoding="utf-8"))
        articles.append(f'<article id="growth-roadmap">{body}</article>')
    for path in course_files():
        anchor = path.stem
        title = path.stem
        nav.append(f'<a href="#{html.escape(anchor)}">{html.escape(title)}</a>')
        body = markdown_to_html(rewrite_links(path.read_text(encoding="utf-8")))
        articles.append(f'<article id="{html.escape(anchor)}">{body}</article>')

    page = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Python100 手机学习入口</title>
  <style>
    :root {{
      color-scheme: light;
      --text: #1d1d1f;
      --muted: #6e6e73;
      --line: #e5e5ea;
      --bg: #fbfbfd;
      --panel: #ffffff;
      --accent: #0066cc;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font: 17px/1.62 -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", sans-serif;
      color: var(--text);
      background: var(--bg);
    }}
    header {{
      position: sticky;
      top: 0;
      z-index: 2;
      padding: 18px 18px 14px;
      background: rgba(251, 251, 253, .92);
      backdrop-filter: blur(18px);
      border-bottom: 1px solid var(--line);
    }}
    h1 {{ margin: 0 0 4px; font-size: 28px; line-height: 1.15; }}
    .sub {{ color: var(--muted); margin: 0; font-size: 14px; }}
    nav {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 12px 18px;
      border-bottom: 1px solid var(--line);
      background: var(--panel);
    }}
    nav a {{
      white-space: nowrap;
      text-decoration: none;
      color: var(--accent);
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 7px 11px;
      font-size: 14px;
    }}
    main {{ max-width: 860px; margin: 0 auto; padding: 16px; }}
    article {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 18px;
      margin: 0 0 18px;
      box-shadow: 0 1px 2px rgba(0,0,0,.03);
    }}
    h1, h2, h3, h4 {{ letter-spacing: 0; line-height: 1.24; }}
    h2 {{ margin-top: 34px; padding-top: 12px; border-top: 1px solid var(--line); }}
    h3 {{ margin-top: 24px; }}
    h4 {{ margin-top: 22px; }}
    p, li {{ word-break: break-word; }}
    a {{ color: var(--accent); }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0;
      font-size: 15px;
    }}
    th, td {{
      text-align: left;
      vertical-align: top;
      border: 1px solid var(--line);
      padding: 9px 10px;
    }}
    th {{ background: #f5f5f7; }}
    pre {{
      overflow-x: auto;
      padding: 14px;
      border-radius: 10px;
      background: #f5f5f7;
      border: 1px solid var(--line);
      font-size: 14px;
      line-height: 1.55;
    }}
    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: .92em;
    }}
    @media (max-width: 640px) {{
      body {{ font-size: 16px; }}
      main {{ padding: 10px; }}
      article {{ border-radius: 10px; padding: 14px; }}
      h1 {{ font-size: 25px; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>AI Builder Python100</h1>
    <p class="sub">开源 100 天课程：Python + Data + Quant + LLM + Agent</p>
  </header>
  <nav>{''.join(nav)}</nav>
  <main>{''.join(articles)}</main>
</body>
</html>
"""
    (DOCS_DIR / "index.html").write_text(page, encoding="utf-8")


def main() -> None:
    build_mobile_markdown()
    build_index_html()


if __name__ == "__main__":
    main()
