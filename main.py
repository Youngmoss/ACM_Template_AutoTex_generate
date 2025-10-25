import os

def sanitize_latex(text):
    replacements = {
        '\\': r'\textbackslash{}',
        '{': r'\{',
        '}': r'\}',
        '#': r'\#',
        '$': r'\$',
        '%': r'\%',
        '&': r'\&',
        '_': r'\_',
        '^': r'\^{}',
        '~': r'\~{}',
    }
    for key, val in replacements.items():
        text = text.replace(key, val)
    return text

def collect_cpp_files(base_path):
    cpp_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".cpp"):
                relative_path = os.path.relpath(os.path.join(root, file), base_path)
                cpp_files.append(relative_path)
    return sorted(cpp_files)

def generate_latex(base_path, output_path="output.tex"):
    cpp_files = collect_cpp_files(base_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(r"""
\documentclass[10pt,a4paper]{article}
\usepackage{xeCJK}
\usepackage{amsmath, amsthm}
\usepackage{listings,xcolor}
\usepackage{geometry} 
\usepackage{fontspec}
\usepackage{graphicx}
\usepackage[colorlinks]{hyperref}
\usepackage{setspace}
\usepackage{fancyhdr}

\setsansfont{Consolas} 
\setmonofont[Mapping={}]{Consolas} 

\linespread{1.2}

\title{Template For ICPC}
\author{ChenJr @ GDUT}
\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}

\pagestyle{fancy}
% 页眉左侧显示当前文件的目录路径（中文字体）
\lhead{\CJKfamily{kai}\nouppercase{\currentfilepath}}
\chead{}
\rhead{\CJKfamily{kai}第 \thepage 页}

\lfoot{}
\cfoot{}
\rfoot{}

\renewcommand{\headrulewidth}{0.4pt} 
\renewcommand{\footrulewidth}{0pt} % 去掉页脚线
\geometry{left=3.18cm,right=3.18cm,top=2.54cm,bottom=2.54cm}
\setlength{\columnsep}{30pt}

\lstset{
    language    = c++,
    numbers     = left,
    numberstyle={\small\color{black}\fontspec{Consolas}},
    commentstyle = \color[RGB]{0,128,0}\bfseries,
    keywordstyle={\color[RGB]{40,40,255}\fontspec{Consolas Bold}\bfseries},
    stringstyle={\color[RGB]{128,0,0}\fontspec{Consolas}\bfseries},
    basicstyle={\fontspec{Consolas}\small\ttfamily},
    emphstyle=\color[RGB]{112,64,160},
    breaklines=true,
    tabsize=4,
    frame=none,
    columns=fullflexible,
    rulesepcolor=\color{red!20!green!20!blue!20},
    showstringspaces=false,
    escapeinside={\%*}{*)},
}

\begin{document}
\title{ICPC Templates}
\author{daonali}
\maketitle
\tableofcontents
\newpage
""")

        current_dirs = []

        def section_cmd(level):
            if level == 1:
                return r"\section"
            elif level == 2:
                return r"\subsection"
            elif level == 3:
                return r"\subsubsection"
            else:
                return r"\paragraph"

        for path in cpp_files:
            parts = path.split(os.sep)
            # 打印目录层级（文件夹名）
            for depth in range(len(parts)-1):
                dir_name = parts[depth]
                if len(current_dirs) <= depth or current_dirs[depth] != dir_name:
                    current_dirs = current_dirs[:depth]
                    current_dirs.append(dir_name)
                    cmd = section_cmd(depth+1)
                    f.write(f"{cmd}*{{{sanitize_latex(dir_name)}}}\n")
                    f.write(r"\markboth{" + sanitize_latex(dir_name) + "}{" + sanitize_latex(dir_name) + "}\n")
                    f.write(r"\addcontentsline{toc}{" + cmd[1:] + "}{" + sanitize_latex(dir_name) + "}\n")

            filename = parts[-1]
            file_level = len(parts)
            cmd = section_cmd(file_level)
            f.write(f"{cmd}*{{{sanitize_latex(filename)}}}\n")
            f.write(r"\markboth{" + sanitize_latex(filename) + "}{" + sanitize_latex(filename) + "}\n")
            f.write(r"\addcontentsline{toc}{" + cmd[1:] + "}{" + sanitize_latex(filename) + "}\n")

            # 计算当前文件相对目录路径（去掉文件名）
            dir_path = os.path.dirname(path)
            if dir_path == "":
                dir_path_latex = "."  # 根目录可显示点或者空
            else:
                # 转换为 LaTeX 安全格式，比如替换 _ 等
                dir_path_latex = sanitize_latex(dir_path.replace(os.sep, "/"))

            # 定义 \currentfilepath 宏，供页眉使用
            f.write(r"\def\currentfilepath{" + dir_path_latex + "}" + "\n")

            f.write(r"\begin{lstlisting}[language=C++]" + "\n")
            full_path = os.path.join(base_path, path)
            with open(full_path, "r", encoding="utf-8", errors="ignore") as cpp_file:
                content = cpp_file.read()
                f.write(content)
            f.write("\n\\end{lstlisting}\n\n")

        f.write(r"\end{document}")

if __name__ == "__main__":
    base_dir = "."
    generate_latex(base_dir, "output.tex")
