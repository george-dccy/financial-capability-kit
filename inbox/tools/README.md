# Inbox 工具

## scan-inbox.py

扫描 inbox/raw/ 下的素材，提取文本并生成初步分类元数据。

### 用法

```bash
# 扫描指定类别
python inbox/tools/scan-inbox.py --category regulatory

# 扫描所有类别
python inbox/tools/scan-inbox.py --all

# 扫描单个文件
python inbox/tools/scan-inbox.py --file inbox/raw/industry/some-report.pdf

# 仅预览，不生成元数据
python inbox/tools/scan-inbox.py --all --dry-run
```

### 支持的文件格式

| 格式 | 处理方式 |
|------|----------|
| `.md`, `.txt` | 直接读取文本 |
| `.pdf` | 使用 PyPDF2 或 pdfplumber 提取文本 |
| `.url.txt` | 读取第一行作为 URL，使用 requests + trafilatura 抓取 |
| `.docx` | 使用 python-docx 提取文本 |
| `.xlsx`, `.csv` | 使用 openpyxl / pandas 读取表头和前 N 行 |

### 输出

在 `inbox/processed/` 下生成 `{原文件名}.meta.json`，字段参见 `inbox/schema/inbox-entry.schema.json`。

### 依赖

```bash
pip install requests trafilatura PyPDF2 python-docx openpyxl
```

纯 Python 标准库即可运行基本功能（md/txt/url.txt），其他格式按需安装。
