### 脚本功能

该脚本用于递归扫描指定目录下的所有 `.cpp` 文件，自动生成一个 LaTeX 文档（`output.tex`），文档中包含按目录层级组织的章节标题和文件名，并将每个 `.cpp` 文件的源码以带有语法高亮的代码块形式嵌入文档。适合用于生成 ICPC（国际大学生程序设计竞赛）模板集或代码笔记。

### 主要特性

- 支持多层目录结构，自动生成对应的章节、子章节标题。  
- 使用 `listings` 宏包展示高亮的 C++ 代码。  
- 自动处理 LaTeX 特殊字符转义，防止编译报错。  
- 页眉显示当前代码文件的相对目录路径，便于导航。  
- 代码字体使用 Consolas，排版美观。  

### 使用方法

1. 确保你的系统安装了 Python 3。  
2. 将该脚本放在你想要生成模板的代码根目录（`base_dir`）下，或者修改脚本中 `base_dir` 为目标路径。  
3. 运行脚本：

```bash
python generate_latex.py
```

4. 脚本会在当前目录生成 `output.tex` 文件。  
5. 用 XeLaTeX 编译生成的 `output.tex`，例如：

```bash
xelatex output.tex
```

6. 查看生成的 PDF，包含所有 `.cpp` 文件及其目录结构。

### 依赖说明

- 该脚本仅依赖 Python 标准库，无需额外安装包。  
- LaTeX 编译需要安装 `xeCJK`、`listings`、`xcolor` 等宏包，推荐使用较新的 TeX 发行版（如 TeX Live 或 MiKTeX）。  
- 编译时使用 XeLaTeX，确保字体配置生效。

---

### Script Description

This Python script recursively scans a specified directory for all `.cpp` files and automatically generates a LaTeX document (`output.tex`). The document arranges the files into sections and subsections according to the directory hierarchy and embeds each `.cpp` file's source code as syntax-highlighted code blocks. It is suitable for producing ICPC (International Collegiate Programming Contest) template collections or code notebooks.

### Features

- Supports multi-level directory structure, automatically generating corresponding section and subsection titles.  
- Uses the `listings` package for highlighted C++ code display.  
- Automatically escapes LaTeX special characters to avoid compilation errors.  
- Displays the current file's relative directory path in the page header for easier navigation.  
- Uses Consolas font for code formatting, enhancing readability.

### Usage

1. Ensure Python 3 is installed on your system.  
2. Place the script in the root directory where you want to generate the template collection, or modify `base_dir` variable in the script to your target directory.  
3. Run the script:

```bash
python generate_latex.py
```

4. The script generates an `output.tex` file in the current directory.  
5. Compile the resulting LaTeX file with XeLaTeX, for example:

```bash
xelatex output.tex
```

6. View the generated PDF, which contains all `.cpp` files organized by directory structure.

### Requirements

- The script only requires Python standard libraries.  
- LaTeX compilation requires packages like `xeCJK`, `listings`, and `xcolor`. A recent TeX distribution (TeX Live or MiKTeX) is recommended.  
- Compile with XeLaTeX to ensure proper font support.