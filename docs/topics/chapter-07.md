---
title: 第7章 文件和异常
eyebrow: CHAPTER 07
chapter: true
code: 第7章
---

<div class="chapter-source">依据第7章课件（64 页）整理。理论范围包含 7.1、7.2，不含 7.3、7.4；编程考试范围为第 1–6 章。</div>

## 7.1 文件读写

文件存储可长期保留的数据。基本流程是打开、读写、关闭，推荐用 `with` 保证退出代码块时关闭文件。

```python
with open('scores.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.rstrip('\n'))
```

| 模式 | 含义 | 注意 |
| --- | --- | --- |
| `r` | 读取 | 文件不存在时报错 |
| `w` | 写入 | 文件存在时清空原内容 |
| `a` | 追加 | 写入文件末尾 |
| `x` | 新建 | 文件已存在时报错 |
| `b` | 二进制 | 如 `rb`，读取字节而非字符串 |
| `+` | 更新 | 如 `r+`，允许读写 |

文本模式可显式写 `t`，如 `rt`。文件路径相对当前工作目录解析，不一定相对脚本所在目录。

### 读取与写入方法

- `read()`：读取剩余全部内容；`read(n)` 最多读取 n 个字符（文本模式）或字节（二进制模式）。
- `readline()`：读取一行，通常保留行末换行。
- `readlines()`：返回各行组成的列表。
- 直接遍历文件对象：逐行处理，适合大文件。
- `write(s)`：写入字符串，**不自动添加换行**。
- `writelines(lines)`：逐项写入字符串，也不会自动添加行间分隔符。

```python
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write('name,score\n')
    file.write('Li,90\n')
```

### 编码与标准输入

文本文件读写时要匹配编码。UTF-8 文件用 `encoding='utf-8'`；二进制模式不传 `encoding`。不匹配的编码可能导致解码错误或乱码。

```python
import sys
# 从标准输入读取所有内容，适用于重定向输入。
text = sys.stdin.read()
```

## 7.2 异常处理

异常表示程序执行过程中出现的问题。捕获具体异常能对预期错误作出处理；不应把所有错误都静默忽略。

```python
try:
    value = int(input())
    result = 10 / value
except ValueError:
    print('请输入整数')
except ZeroDivisionError:
    print('除数不能为零')
else:
    print(result)
finally:
    print('处理结束')
```

`try` 中异常发生后的语句不再执行，转入第一个匹配的 `except`。`else` 在无异常时执行，`finally` 用于清理工作。子类异常应放在父类异常前面。

| 异常 | 常见原因 |
| --- | --- |
| `ValueError` | 值或格式不合法，如 `int('3.5')` |
| `TypeError` | 类型不适用，如 `'age'+23` |
| `IndexError` | 序列索引越界 |
| `KeyError` | 字典键不存在 |
| `NameError` | 名称未定义 |
| `AttributeError` | 对象没有所需属性或方法 |
| `FileNotFoundError` | 文件不存在 |
| `ZeroDivisionError` | 除数为零 |

### raise 与 assert

```python
def area(radius):
    if radius < 0:
        raise ValueError('半径不能为负')
    return 3.141592653589793 * radius * radius

assert 2 + 2 == 4
```

`raise` 主动抛出异常；`assert` 条件为假时抛出 `AssertionError`。优化模式可能移除断言，不能仅靠 `assert` 校验必要的外部输入。

## 7.3 Pandas读写常见格式文件

本节不在所给考试范围内。课件介绍第三方模块安装、DataFrame，以及 CSV、Excel、JSON 文件读写。

```python
# 需要在本地 Python 环境安装 pandas。
import pandas as pd

data = pd.DataFrame({'name': ['Li', 'Wang'], 'score': [90, 85]})
data.to_csv('scores.csv', index=False, encoding='utf-8')
```

Excel 读写还需要对应引擎，例如 `.xlsx` 常使用 `openpyxl`。网页展示这些示例不需要浏览器加载 Pandas。

## 7.4 交互式数据可视化

本节不在所给考试范围内。课件介绍 Plotly 的折线图、柱状图与地图。图表可从 DataFrame 创建并导出为 HTML。

```python
# 在本地 Python 环境运行，需要 plotly。
import plotly.express as px
fig = px.bar(x=['Li', 'Wang'], y=[90, 85], labels={'x': '姓名', 'y': '成绩'})
fig.write_html('scores.html', include_plotlyjs=True)
```

`include_plotlyjs=True` 将图表脚本写入导出文件，便于离线查看。

<div class="chapter-links"><a href="./chapter-06.html">← 第6章</a><a href="./chapter-08.html">第8章 →</a></div>
