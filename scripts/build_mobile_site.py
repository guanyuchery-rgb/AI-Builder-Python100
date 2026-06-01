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

    for line in lines:
        if line.startswith("```"):
            if not in_code:
                close_list()
                in_code = True
                code_lines = []
            else:
                output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                in_code = False
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            close_list()
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            close_list()
            level = len(heading.group(1))
            text = inline(heading.group(2))
            output.append(f"<h{level}>{text}</h{level}>")
            continue

        if line.startswith("- "):
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(f"<li>{inline(line[2:])}</li>")
            continue

        close_list()
        output.append(f"<p>{inline(line)}</p>")

    close_list()
    return "\n".join(output)


def build_mobile_markdown() -> None:
    lines = [
        "# Python100 手机学习入口",
        "",
        "这是手机端入口。Day01-Day20 严格零基础递进；每天打开一个 Day，按 2 小时节奏完成：读目标、跑代码、做 7 道简单题 + 5 道基础巩固题、记录 Debug。",
        "",
        "## 学习入口",
        "",
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
    <h1>Python100 手机学习入口</h1>
    <p class="sub">零基础递进 + 7 道简单题 + 5 道基础巩固题 + Quant / LLM / Agent 迁移点</p>
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
