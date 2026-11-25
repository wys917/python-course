---
title: 第一次上机小测
eyebrow: QUIZ 01
code: QUIZ 01
description: 题目、参考答案与解析。
questionGroups:
  - [判断题, judgment, 14]
  - [单选题, choice, 13]
  - [填空题, blank, 9]
  - [编程题, programming, 6]
---

<h2 id="judgment" class="quiz-group">判断题<span>14 QUESTIONS</span></h2>

:::: question judgment-1 | 1-7 判断题

在Python中，可以用else作为变量名。

<div class="question-tags"><span class="question-tag">关键字</span> <span class="question-tag">变量命名</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`else` 是 Python 关键字，标识符不能和关键字重名，所以本题错误。

Python 标识符命名规则：

- **组成字符**：只能包含字母（含汉字）、数字、下划线 `_`，不能有空格、连字符等其他符号。
- **开头字符**：只能以字母或下划线开头，不能以数字开头。`score_1` 合法，`1score`、`my-score`、`my score` 都不合法。
- **不能是关键字**：`else`、`if`、`for` 等关键字已被语言占用，不能作为标识符。
- **区分大小写**：`score` 和 `Score` 是两个不同的名字。
- **命名习惯**：推荐全小写、多单词用下划线连接，如 `total_score`；`list` 等内置名称虽可用作变量名，但应避免，以免遮蔽原有含义。

</div>

:::

::::

:::: question judgment-2 | 1-9 判断题

字母A的ASCII编码值和Unicode编码值相同。

<div class="question-tags"><span class="question-tag">ASCII编码</span> <span class="question-tag">Unicode编码</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这道题的关键不是死记 `A` 是 65，而是理解 ASCII 和 Unicode 之间的关系：**Unicode 在设计时把 ASCII 的全部 128 个字符（码点 0~127）原样搬了过去，作为自己的前 128 个码点**，这样做是为了兼容已有的英文文本和系统。

- ASCII 中 `A` 的编码值是 65（十进制）。
- Unicode 中 `A` 的码点是 `U+0041`，换算成十进制同样是 65。
- 因为 65 落在前 128 个码点范围内，所以 ASCII 和 Unicode 对 `A` 的编码值完全一致。

也可以在 Python 中用 `ord('A')` 直接验证，结果就是 `65`。因此本题正确。只要是 ASCII 字符（如字母、数字、常见标点），它们在 Unicode 下的码点都和 ASCII 编码值相同；但汉字等超出 ASCII 范围的字符就没有这个对应关系。

</div>

:::

::::

:::: question judgment-3 | 1-3 判断题

下面程序的运行结果是4。

```python
    i=3         
    ++i
```

<div class="question-tags"><span class="question-tag">一元运算符</span> <span class="question-tag">++运算符辨析</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 没有 `++` 自增运算符。`++i` 会被理解为 `+(+i)`，只是连续使用两次一元正号，变量 `i` 的值仍然是 3。若要让 `i` 增加 1，应写 `i += 1`。

另外，题目代码没有使用 `print()`，即使正常执行也不会输出 4，因此说法错误。

</div>

:::

::::

:::: question judgment-4 | 1-4 判断题

当输入是`10.0`时，下面程序的输出是`f(10.0) = 0.1`。

```python
x=int(input())
if x==0:
    result=0
else:
    result=1/x
print('f({0:.1f}) = {1:.1f}'.format(x,result))
```

<div class="question-tags"><span class="question-tag">input函数</span> <span class="question-tag">int与float转换</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

本题的易错点在于混淆了 `input()`、`int()`、`float()` 三者的关系：

- `input()` 读取用户输入，返回值永远是**字符串**，不管用户敲的是整数还是小数。
- `int(字符串)` 只能把形如 `'10'` 这种看起来像整数的字符串转换成整数，遇到带小数点的字符串（如 `'10.0'`）会直接报错 `ValueError`，并不会先转成小数再取整。
- 要读取小数，应改用 `float(字符串)`。

题目输入是 `10.0`，`int(input())` 会在这一步直接抛出异常，程序随即中断，根本不会执行到后面的 `print()`，更不可能输出 `f(10.0) = 0.1`。

如果把代码改成 `float(input())`，则 `x` 为 `10.0`，执行 `1 / x` 得到 `0.1`，再通过 `:.1f` 保留一位小数，才会得到题目描述的输出。因此本题错误。

</div>

:::

::::

:::: question judgment-5 | 1-5 判断题

下面程序的输出是：这是字符串输出格式□□123。 □表示空格。

`print("这是字符串输出格式{:5s}".format("123"))`

<div class="question-tags"><span class="question-tag">字符串格式化</span> <span class="question-tag">左对齐</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

要理解这道题，需要记住 `.format()` 的一条通用规则：**字符串类型（`s`）默认左对齐，数字类型（`d`、`f` 等）默认右对齐**，可以对照下一题 1-6 来记忆这个区别。

格式说明 `:5s` 表示按字符串处理，最小宽度为 5。`'123'` 只有 3 个字符，左对齐意味着内容放在左边，不足的宽度用空格补在**右侧**。

因此实际输出是 `这是字符串输出格式123□□`（空格在 `123` 后面），而题目说空格在 `123` 前面，顺序弄反了，所以本题错误。

</div>

:::

::::

:::: question judgment-6 | 1-6 判断题

下面语句的输出是：这是数字输出格式□□123。□ 表示空格。

`print("这是数字输出格式{:5d}".format(123))`

<div class="question-tags"><span class="question-tag">字符串格式化</span> <span class="question-tag">右对齐</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

本题与 1-5 正好相对，可以对照记忆：**数字类型（`:5d`）默认右对齐**，与字符串类型（`:5s`）默认左对齐正好相反。

格式说明 `:5d` 表示整数按十进制显示，最小宽度为 5。整数 `123` 只有 3 位，右对齐意味着内容靠在右边，不足的宽度用空格补在**左侧**。

因此输出内容就是 `这是数字输出格式□□123`（空格在 `123` 前面，`□` 表示空格），与题目描述一致，所以本题正确。

小结：字符串默认左对齐、补右边空格；数字默认右对齐、补左边空格。如果想改变默认对齐方式，可以在宽度前加 `<`（左对齐）、`>`（右对齐）或 `^`（居中）明确指定，例如 `{:>5s}` 能让字符串右对齐。

</div>

:::

::::

:::: question judgment-7 | 1-7 判断题

`bool(None)`的返回值是False。

<div class="question-tags"><span class="question-tag">bool函数</span> <span class="question-tag">None</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`None` 表示空值，在 Python 的条件判断中属于假值。

因此 `bool(None)` 的结果是 `False`，题目说法正确。

</div>

:::

::::

:::: question judgment-8 | 1-8 判断题

`print(bin(12.5))`的输出是`0b1100.1`

<div class="question-tags"><span class="question-tag">bin函数</span> <span class="question-tag">整数与浮点数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`bin()` 用于把整数转换成二进制字符串，例如 `bin(12)` 得到 `'0b1100'`。它的参数必须是整数。

题目传入的是浮点数 `12.5`，因此 `bin(12.5)` 会引发 `TypeError`，不会输出 `0b1100.1`。

</div>

:::

::::

:::: question judgment-9 | 1-9 判断题

`int("92",8)`的值是74。

<div class="question-tags"><span class="question-tag">int函数</span> <span class="question-tag">八进制转换</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`int(字符串, 进制)` 会把字符串按照指定的进制解析成十进制整数。不同进制允许出现的数字字符是有限的：

| 进制 | 允许的数字字符 |
|---|---|
| 二进制 | `0`、`1` |
| 八进制 | `0`～`7` |
| 十进制 | `0`～`9` |
| 十六进制 | `0`～`9`、`a`～`f`（大小写均可） |

八进制只允许出现 `0` 到 `7`，不能出现 `8` 或 `9`。题目中的字符串 `'92'` 含有数字 `9`，超出了八进制允许的字符范围。

因此 `int('92', 8)` 并不会得到 74，而是直接引发 `ValueError`，题目错误。

</div>

:::

::::

:::: question judgment-10 | 1-10 判断题

表达式`3 and 0 and "hello"`的值是False。

<div class="question-tags"><span class="question-tag">and运算符</span> <span class="question-tag">短路求值</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

理解本题要记住 Python 中 `and`、`or` 的一条重要规则：**它们返回的是参与运算的某个操作数本身，而不一定是布尔值 `True`/`False`**。具体规则是：

- `and` 从左到右依次检查，遇到第一个假值就立即停止并返回这个假值；如果都是真值，则返回最后一个操作数。
- `or` 从左到右依次检查，遇到第一个真值就立即停止并返回这个真值；如果都是假值，则返回最后一个操作数。

这种"结果已经确定就不再继续计算"的行为称为**短路求值**。

回到本题：`3` 是真值，继续检查下一个；`0` 是假值，`and` 立即停止并返回 `0` 本身，后面的 `'hello'` 根本不会被求值。

所以表达式的结果是整数 `0`，而不是布尔对象 `False`。虽然 `0 == False` 为 `True`（数值相等），但 `0 is False` 为 `False`（二者类型不同，不是同一个对象），因此题目说法错误。

</div>

:::

::::

:::: question judgment-11 | 1-11 判断题

`z` 已赋值，`x=(y=z+1)` 是错误语句。

<div class="question-tags"><span class="question-tag">赋值语句</span> <span class="question-tag">链式赋值</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

理解本题的关键是：在 Python 中，`=` 赋值是一条**语句**（statement），而不是像 `+`、`*` 那样可以产生值的**表达式**（expression）。语句本身没有"值"，因此不能把 `y=z+1` 当作一个值放进括号里再赋给 `x`，这正是 `x=(y=z+1)` 会直接报 `SyntaxError` 的根本原因。

如果希望 `x` 和 `y` 都等于 `z+1`，有两种写法：

- **链式赋值：** `x = y = z + 1`，依次把 `z+1` 的结果赋给 `y` 和 `x`。
- **先赋值再引用：** 先写 `y = z + 1`，再写 `x = y`。

补充：Python 3.8 引入了海象运算符 `:=`（赋值表达式），可以在表达式内部完成赋值并返回值，例如 `if (y := z + 1) > 0:`，但这是专门的新语法，并不等同于普通的 `=`。

因此本题说法正确，`x=(y=z+1)` 确实是错误语句。

</div>

:::

::::

:::: question judgment-12 | 1-12 判断题

`print(("12 "*3).strip()==" ".join(["12","12","12"]))` 的输出结果是 `True`。

<div class="question-tags"><span class="question-tag">strip方法</span> <span class="question-tag">join方法</span> <span class="question-tag">字符串比较</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`'12 ' * 3` 的结果是 `'12 12 12 '`，末尾仍然有一个空格；调用 `.strip()` 后去掉首尾空白，得到 `'12 12 12'`。`' '.join(['12','12','12'])` 的结果是 `'12 12 12'`，只在元素之间放空格。经过 `.strip()` 处理后，两边字符串相同，因此比较结果为 `True`，`print()` 输出 `True`。

</div>

:::

::::

:::: question judgment-13 | 1-13 判断题

下面的程序当输入是 `c d e a`时，输出是 `a c d e`。

```python
a = input().split(" ")
a.sort()
for i in a:    
    print(i,end=" ")
```

<div class="question-tags"><span class="question-tag">sort方法</span> <span class="question-tag">字符串排序</span> <span class="question-tag">print函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（按字母顺序判断）。若要求输出逐字符相同，则为 F，实际末尾还有一个空格。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`a.sort()` 会直接对列表 `a` 排序，但它的返回值是 `None`。本题先执行 `a.sort()`，再遍历 `a`，因此可以正常输出。输入 `c d e a` 后，列表排为 `['a', 'c', 'd', 'e']`，输出顺序为 `a c d e`。

注意：`end=" "` 让每次输出后都有一个空格，因此最后的 `e` 后也有空格，且没有换行。按字母顺序判断，本题正确；若要求逐字符相同，实际末尾比题面多一个空格。

</div>

:::

::::

:::: question judgment-14 | 1-14 判断题

`[4,5]*3` 的结果是 `[4,5],[4,5],[4,5]`。

<div class="question-tags"><span class="question-tag">列表重复</span> <span class="question-tag">序列嵌套</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

列表乘以整数表示重复列表中的元素。`[4, 5] * 3` 得到 `[4, 5, 4, 5, 4, 5]`，不会得到题目所写的三个 `[4,5]`。因此本题错误。

</div>

:::

::::

<h2 id="choice" class="quiz-group">单选题<span>13 QUESTIONS</span></h2>

:::: question choice-1 | 2-2 单选题

Python程序在Windows上的扩展名是_________。

**A.** py

**B.** exe

**C.** docx

**D.** jpg

<div class="question-tags"><span class="question-tag">Python文件扩展名</span> <span class="question-tag">源代码文件</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 源代码文件通常使用 `.py` 作为扩展名，例如 `hello.py`。`.exe` 通常是 Windows 下的可执行文件，`.docx` 是 Word 文档，`.jpg` 是图片文件。

因此选择 A。

</div>

:::

::::

:::: question choice-2 | 2-8 单选题

_______号表示同一行的后面部分是Python程序的注释。

**A.** `*`

**B.** `%`

**C.** `/`

**D.**

```python
#
```

<div class="question-tags"><span class="question-tag">注释</span> <span class="question-tag">#符号</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 使用英文半角 `#` 表示单行注释。从 `#` 开始直到本行结束的内容都会被当作注释，不参与程序执行。

例如：

```python
x = 3  # 给变量 x 赋值
```

因此选择 D。

</div>

:::

::::

:::: question choice-3 | 2-9 单选题

Python语言正确的标识符是_______。

**A.** `2you`

**B.** `my-name`

**C.** `_item`

**D.** `abc*234`

<div class="question-tags"><span class="question-tag">标识符</span> <span class="question-tag">变量命名</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 标识符可以由字母、数字和下划线组成，但不能以数字开头。

- `2you`：以数字开头，不合法。
- `my-name`：包含减号，会被理解为减法表达式。
- `_item`：以下划线开头，合法。
- `abc*234`：包含乘号，不合法。

因此选择 C。

</div>

:::

::::

:::: question choice-4 | 2-11 单选题

不是面向对象的程序设计语言是________。

**A.** Java

**B.** C

**C.** C++

**D.** Python

<div class="question-tags"><span class="question-tag">面向对象编程</span> <span class="question-tag">程序设计范式</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Java、C++ 和 Python 都支持面向对象编程，可以通过类和对象组织程序。C 语言通常归类为过程式编程语言，主要通过函数和语句组织程序。

因此，按常见的程序设计语言分类，本题选择 B。

</div>

:::

::::

:::: question choice-5 | 2-1 单选题

下列数据类型中， Python不支持的是_____________。

**A.** char

**B.** int

**C.** float

**D.** list

<div class="question-tags"><span class="question-tag">数据类型</span> <span class="question-tag">字符串</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 提供 `int`、`float`、`str`、`list` 等内置数据类型，但没有单独的 `char`（字符）类型。

单个字符也使用字符串表示，例如 `'A'` 的类型是 `str`，长度为 1。因此选择 A。

</div>

:::

::::

:::: question choice-6 | 2-6 单选题

Python 语句 `print(0xA + 0xB)`的输出结果是______________。

**A.** 0xA + 0xB

**B.** A + B

**C.** 0xA0xB

**D.** 21

<div class="question-tags"><span class="question-tag">十六进制</span> <span class="question-tag">整数运算</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`0x` 是十六进制整数的前缀。`0xA` 表示十进制的 10，`0xB` 表示十进制的 11。

两者相加得到 21。Python 的整数本身不固定使用某种进制存储，`print()` 默认以十进制显示这个结果，因此选择 D。

</div>

:::

::::

:::: question choice-7 | 2-7 单选题

Python 语句 `x = 'car'; y = 2; print(x + y)` 的输出结果是____________。

**A.** 语法错

**B.** 2

**C.** `'car2'`

**D.** `'carcar'`

<div class="question-tags"><span class="question-tag">字符串拼接</span> <span class="question-tag">类型错误</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

现有选项无正确项。执行 `x + y` 时触发 `TypeError`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`x` 是字符串 `'car'`，`y` 是整数 `2`。Python 中 `+` 作用在字符串上表示拼接，但前提是两边必须都是字符串；`+` 作用在数字上表示加法，前提是两边都是数字。字符串和整数是两种不同的数据类型，`+` 并不知道该按哪种规则处理，所以 `x + y` 无法执行。

执行到 `print(x + y)` 这一行时，程序会抛出 `TypeError: can only concatenate str (not "int") to str`，程序因此中断，不会输出任何结果，更不会自动把 `2` 转换成字符串 `'2'` 去拼接。

这里发生的是运行时的 `TypeError`，而不是语法错误 `SyntaxError`，所以严格来说现有选项无正确项。想要输出 `'car2'` 这样的结果，需要先用 `str(y)` 把 `2` 转换成字符串，再拼接：`x + str(y)`。

</div>

:::

::::

:::: question choice-8 | 2-8 单选题

如math模块已引入，Python 表达式 `math.sqrt(4)*math.sqrt(9)`的值为________。

**A.** 36.0

**B.** 6

**C.** 13

**D.** 6.0

<div class="question-tags"><span class="question-tag">math模块</span> <span class="question-tag">sqrt函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`math.sqrt()` 用于计算平方根，返回浮点数：`math.sqrt(4)` 得到 `2.0`，`math.sqrt(9)` 得到 `3.0`。

两者相乘得到 `6.0`，所以选择 D。注意，结果虽然数值上等于 6，类型和显示形式仍是浮点数。

</div>

:::

::::

:::: question choice-9 | 2-10 单选题

关于Python中的复数，下列说法错误的是___________。

**A.** 表示复数的语法是real + imag j

**B.** 实部和虚部都是浮点数

**C.** 虚部必须后缀j, 且必须是小写

**D.** 方法conjugate 返回复数的共轭复数

<div class="question-tags"><span class="question-tag">复数</span> <span class="question-tag">共轭复数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 的复数虚部可以使用小写 `j`，也可以使用大写 `J`，例如 `3+4j` 和 `3+4J` 都合法。

因此“虚部必须是小写 j”的说法错误，选择 C。复数的实部和虚部可以分别通过 `.real` 和 `.imag` 读取。

</div>

:::

::::

:::: question choice-10 | 2-10 单选题

Python 语句 `print(chr(65))`的运行结果是___________。

**A.** 65

**B.** 6

**C.** 5

**D.** A

<div class="question-tags"><span class="question-tag">chr函数</span> <span class="question-tag">Unicode码点</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`chr()` 可以把一个整数码点转换成对应字符。数字 65 对应英文字母 `A`，所以 `chr(65)` 返回字符串 `'A'`。

`print()` 输出该字符，因此选择 D。与之相对，`ord('A')` 可以把字符转换成对应的整数码点。

</div>

:::

::::

:::: question choice-11 | 2-12 单选题

关于Python字符串，下列说法错误的是___________。

**A.** 字符即长度为1的字符串

**B.** 字符串以 `\0` 标志字符串的结束

**C.** 既可以用单引号，也可以用双引号创建字符串

**D.** 在三引号字符串中可以包含换行回车等特殊字符

<div class="question-tags"><span class="question-tag">字符串</span> <span class="question-tag">字符编码</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 字符串可以用单引号、双引号或三引号创建，三引号字符串也可以包含换行。Python 没有独立的 `char` 类型，单个字符仍然是长度为 1 的字符串。

本题的关键在于理解 Python 字符串和 C 语言字符串的区别：

- **C 语言字符串**：以一个特殊的空字符 `\0`（即值为 0 的字节）作为结束标志，程序通过扫描到 `\0` 来判断字符串在哪里结束。
- **Python 字符串**：是一个独立的对象，自身就记录了长度和内容，并不依靠任何特殊字符来标记结尾。因此 Python 字符串里完全可以包含 `\0` 这个字符本身，它只是字符串内容的一部分，不会被当作结束标志，也不会提前截断字符串。

因此“字符串以 `\0` 标志字符串的结束”这一说法错误，选择 B。

</div>

:::

::::

:::: question choice-12 | 2-12 单选题

下列语句错误的有____个。

```python
a、语句i*=3+5等价于i=i*3+5。
b、科学记数法2.3e2.0得到的数是230.0。
c、语句print(int("3.5",10))是不会执行的即运行错误。
d、语句print("{:8s}".format("ab"))和print("{:8d}".format(12))得到的值均是左对齐。
```

**A.** 1

**B.** 2

**C.** 3

**D.** 4

<div class="question-tags"><span class="question-tag">复合赋值运算符</span> <span class="question-tag">科学计数法</span> <span class="question-tag">格式化输出</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C（3 个）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

把每句话改写成一次最小实验。涉及“等价”时要选能区分两种写法的输入，涉及“错误”时要辨明错误发生的阶段。

| 项 | 如何验证 | 对原说法的判断 |
| --- | --- | --- |
| a | 取 `i = 2`，执行 `i *= 3 + 5` 先算完整右侧，得到 `2 × 8 = 16`。而 `2 * 3 + 5` 得到 `11` | 错 |
| b | `2.3e2` 得到 `230.0`。科学计数法的指数要写成整数，`2.3e2.0` 在解析时便触发 `SyntaxError` | 错 |
| c | `int("3.5", 10)` 在运行时因小数点触发 `ValueError`，外层 `print` 无法输出 | 对 |
| d | 宽度 8 时 `"ab"` 后补 6 个空格，整数 `12` 前补 6 个空格，两者默认对齐方向不同 | 错 |

题目让数的是**错误**说法，共 a、b、d 三项。c 可回看输入转换的判断题，d 可用格式表复核。[1-4 输入转换](#judgment-4) · [1-5 对齐规则](#judgment-5)

</div>

:::

::::

:::: question choice-13 | 2-13 单选题

执行下列代码后的输出结果是：

```python
a=[1,2,3]
b=a
a[1]=5
print(id(a)==id(b),end=" ")
print(b,end=" ")
d=a[:]
a[1]=7
print(id(a)==id(d),end=" ")
print(d)
```

**A.** True [1, 5, 3] False [1, 5, 3]

**B.** False [1, 2, 3] False [1, 5, 3]

**C.** True [1, 5, 3] True [1, 7, 3]

**D.** False [1, 2, 3] True [1, 5, 3]

<div class="question-tags"><span class="question-tag">id函数</span> <span class="question-tag">列表引用</span> <span class="question-tag">浅拷贝</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

追踪列表时，分别记“名字指向哪个列表”和“这个列表现在装什么”。这里用甲、乙标记两个实际创建的列表。

| 执行到 | 名字指向 | 列表内容 |
| --- | --- | --- |
| `b = a` | `a`、`b` 都指向甲 | 甲为 `[1, 2, 3]` |
| `a[1] = 5` | `b` 也能看到甲的变化 | 甲为 `[1, 5, 3]` |
| `d = a[:]` | 切片创建乙，`d` 指向乙 | 乙此时也含 `[1, 5, 3]` |
| `a[1] = 7` | 只改了甲的第二个位置 | 甲为 `[1, 7, 3]`，乙仍为 `[1, 5, 3]` |

按打印发生的时刻读表。第一次比较身份时 `a` 与 `b` 指向同一个对象，输出 `True` 和当时的 `b`。第二次 `a` 与 `d` 指向两个对象，输出 `False` 和 `d`，合起来对应 A。

</div>

:::

::::

<h2 id="blank" class="quiz-group">填空题<span>09 QUESTIONS</span></h2>

:::: question blank-1 | 4-2 填空题

十六进制`2AC`的八进制表示是 _____ 。

<div class="question-tags"><span class="question-tag">十六进制转换</span> <span class="question-tag">八进制转换</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`1254`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

十六进制、八进制之间一般不直接互相转换，而是**以二进制为桥梁**：因为 $16=2^4$、$8=2^3$，所以每 1 位十六进制数恰好对应 4 位二进制，每 1 位八进制数恰好对应 3 位二进制。

**第一步：十六进制 → 二进制**，每一位展开成 4 位：

- `2` → `0010`
- `A` → `1010`
- `C` → `1100`

拼接后 `2AC` 对应二进制 `001010101100`。

**第二步：二进制 → 八进制**，从右往左每 3 位分成一组（不足 3 位在左侧补 0）：`001 010 101 100`，每组转换成一位八进制数，得到 `1 2 5 4`。

因此答案是 `1254`。

</div>

:::

::::

:::: question blank-2 | 4-3 填空题

十进制106的原码是 _____ ，反码是 _____ ，补码是 _____ 。 （用八位表示）

<div class="question-tags"><span class="question-tag">原码、反码与补码</span> <span class="question-tag">二进制表示</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`01101010`、`01101010`、`01101010`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

在八位原码表示中，**最高位是符号位**（0 表示正数，1 表示负数），其余 7 位表示数值大小。原码、反码、补码的转换规则如下：

| | 正数 | 负数 |
|---|---|---|
| 原码 | 符号位 0 + 数值的二进制 | 符号位 1 + 数值的二进制 |
| 反码 | 与原码相同 | 符号位不变，数值位逐位取反 |
| 补码 | 与原码相同 | 反码 + 1 |

正数的原码、反码、补码之所以完全相同，是因为正数不需要做符号位以外的变换。

先用**除 2 倒取余法**把 106 转换成二进制：每次除以 2，记录商和余数，用商继续除，直到商为 0。

| 被除数 | 除以 2 的商 | 余数 |
| --- | --- | --- |
| 106 | 53 | 0 |
| 53 | 26 | 1 |
| 26 | 13 | 0 |
| 13 | 6 | 1 |
| 6 | 3 | 0 |
| 3 | 1 | 1 |
| 1 | 0 | 1 |

余数**从下往上读**，得到 `1101010`。

写成八位（符号位 0 + 7 位数值）是 `01101010`。按上表，106 是正数，三种编码完全相同。

因此三个空依次填写：`01101010`、`01101010`、`01101010`。

</div>

:::

::::

:::: question blank-3 | 4-4 填空题

-78的原码是 _____ ，反码是 _____ ，补码是 _____ 。 （用八位表示）

<div class="question-tags"><span class="question-tag">原码、反码与补码</span> <span class="question-tag">负数表示</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`11001110`、`10110001`、`10110010`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

负数要先求出其绝对值（78）的二进制，再按照负数规则（符号位置 1 → 数值位取反 → 加 1）依次变换，具体规则见下表：

| | 负数 |
|---|---|
| 原码 | 符号位 1 + 数值的二进制 |
| 反码 | 符号位不变，数值位逐位取反 |
| 补码 | 反码 + 1 |

**第一步：** 用**除 2 倒取余法**求绝对值 78 的二进制：

| 被除数 | 除以 2 的商 | 余数 |
| --- | --- | --- |
| 78 | 39 | 0 |
| 39 | 19 | 1 |
| 19 | 9 | 1 |
| 9 | 4 | 1 |
| 4 | 2 | 0 |
| 2 | 1 | 0 |
| 1 | 0 | 1 |

余数**从下往上读**，得到 `1001110`，在前面补 0 写成八位是 `01001110`。

**第二步：原码** —— 把符号位改为 1，数值位不变，得到 `11001110`。

**第三步：反码** —— 保留符号位 1，将其余七位逐位取反，得到 `10110001`。

**第四步：补码** —— 在反码基础上加 1，得到 `10110010`。

因此答案依次为 `11001110`、`10110001`、`10110010`。

补码之所以常用，是因为用它做加减法时不需要对符号位做特殊处理，计算机硬件可以统一按加法处理，同时也避免了原码、反码中"+0"和"-0"同时存在的歧义。

</div>

:::

::::

:::: question blank-4 | 4-4 填空题

Python 表达式 `0 and 1 or not 2<True` 的值为 _____ 。

<div class="question-tags"><span class="question-tag">逻辑运算</span> <span class="question-tag">运算符优先级</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先按优先级分析右侧的比较表达式 `2 < True`。在 Python 中 `True` 对应数值 1，因此 `2 < 1` 为 `False`，取反后 `not (2 < True)` 得到 `True`。

`and` 的优先级高于 `or`：`0 and 1` 返回 0，随后 `0 or True` 返回 `True`。所以最终结果是 `True`。

借这道题把本章常考的运算符优先级**从高到低**系统汇总一下（同一行内的运算符优先级相同；乘方从右向左结合）：

| 优先级 | 运算符 | 说明 |
|---|---|---|
| 高 | `()` | 括号，强制最先计算 |
| ↑ | `**` | 乘方（从右向左结合，如 `2**3**2 = 2**(3**2)`） |
| ↑ | `+x`、`-x`、`~x` | 一元正负号、按位取反 |
| ↑ | `*`、`/`、`//`、`%` | 乘、除、整除、取余 |
| ↑ | `+`、`-` | 加、减 |
| ↑ | `<<`、`>>` | 位移 |
| ↑ | `&` | 按位与 |
| ↑ | `^` | 按位异或 |
| ↑ | `\|` | 按位或 |
| ↑ | `==`、`!=`、`<`、`>`、`<=`、`>=` | 比较运算符 |
| ↑ | `not` | 逻辑非 |
| ↑ | `and` | 逻辑与 |
| 低 | `or` | 逻辑或 |

几条最容易考到、也最容易出错的记忆点：

- **乘方比负号优先**：`-2**4` 等于 `-(2**4) = -16`，而不是 `(-2)**4 = 16`。
- **算术运算符比比较运算符优先**：先算加减乘除，再比较大小。
- **比较运算符比逻辑运算符优先**：`a > b and c > d` 会先分别算出两个比较结果，再用 `and` 连接。
- **`not` > `and` > `or`**：三者优先级依次降低，拿不准时可以加括号明确顺序。
- **按位运算符的优先级比比较运算符高**，比加减运算符低，容易和加减运算的直觉顺序搞混，建议写按位运算时主动加括号。

</div>

:::

::::

:::: question blank-5 | 4-8 填空题

Python 语句 `print(abs(-10.2), round(abs(8-2j),3))` 的输出结果是 _____ 。

<div class="question-tags"><span class="question-tag">abs函数</span> <span class="question-tag">复数模</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`10.2 8.246`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`abs()` 对普通实数返回绝对值，所以 `abs(-10.2) = 10.2`。对复数，`abs()` 返回复数的模：实部平方加虚部平方后再开平方。

`abs(8-2j) = √(8²+(-2)²) = √68 ≈ 8.246211`，保留三位小数得到 `8.246`。因此输出为 `10.2 8.246`。

</div>

:::

::::

:::: question blank-6 | 4-14 填空题

表达式 `3 and 0 and 5` 的结果是什么？ _____

<div class="question-tags"><span class="question-tag">and运算符</span> <span class="question-tag">短路求值</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`0`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`and` 从左向右检查操作数，遇到第一个假值就停止，并返回这个假值本身。`3` 是真值，所以继续检查；`0` 是假值，因此表达式直接返回整数 `0`，后面的 `5` 不再计算。

</div>

:::

::::

:::: question blank-7 | 4-16 填空题

表达式 `---3` 的结果是什么？ _____ 。

<div class="question-tags"><span class="question-tag">一元负号</span> <span class="question-tag">运算符优先级</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`-3`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

连续三个负号相当于 `-(-(-3))`。从里向外计算：`-3` 变成 `3`，再变成 `-3`。

因此最终结果为 `-3`。

</div>

:::

::::

:::: question blank-8 | 4-17 填空题

表达式`32.2//6-24//6`的值是 _____ 。

<div class="question-tags"><span class="question-tag">整除运算符</span> <span class="question-tag">浮点数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`1.0`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先分别计算两个整除表达式。`32.2 // 6` 的结果为 `5.0`，因为参与运算的数中有浮点数，所以结果类型仍为浮点数；`24 // 6` 得到整数 `4`。

两者相减得到 `1.0`。注意，`//` 表示向下取整的除法，结果类型还会受到操作数类型影响。

</div>

:::

::::

:::: question blank-9 | 4-9 填空题

输入aBcD后，下列程序的打印结果是(若打印的是字符串，不要加引号) _____

```python
s=list(input()) 
for i in range(len(s)):
    if 'A'<=s[i]<='Z':
        s[i]=chr(ord(s[i])+ord('a')-ord('A'))
    if 'a'<=s[i]<='z':
        s[i]=chr(ord(s[i])-ord('a')+ord('A'))
    print(s[i],end="") 
```

<div class="question-tags"><span class="question-tag">if语句</span> <span class="question-tag">ord与chr函数</span> <span class="question-tag">大小写转换</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`ABCD`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先看两个条件之间有没有 `elif`。这里是两个独立的 `if`，第二次判断会读取**第一步处理后的字符**。ASCII 英文字母大小写之间相差 `ord('a') - ord('A') = 32`，加 32 把大写转小写，减 32 把小写转大写。

| 读到的字符 | 第一个 `if` 后 | 第二个 `if` 后，也是本轮输出 |
| --- | --- | --- |
| `a` | `a` | `A` |
| `B` | `b` | `B` |
| `c` | `c` | `C` |
| `D` | `d` | `D` |

`end=""` 让四次打印紧挨着，填 `ABCD`。若第二个条件改成 `elif`，原来大写的字符在第一次转换后就会跳过第二个分支。[对照 2-10 的 chr 题](#choice-10)

</div>

:::

::::

<h2 id="programming" class="quiz-group">编程题<span>06 QUESTIONS</span></h2>

:::: question programming-1 | 7-1 计算分段函数

本题目要求计算下列分段函数g(x)的值：

$g(x)= \begin{cases}0& \text{x=0}\\ \frac{1}{2x}& \text{x!=0} \end{cases}$

#### 输入格式:

在一行中输入实数x。

#### 输出格式:

在一行中按“g(x) = result”的格式输出，其中x与result都保留3位小数。

#### 输入样例1:

在这里给出一组输入。例如：

```text
500
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
g(500.000) = 0.001
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
0
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
g(0.000) = 0.000
```

<div class="question-tags"><span class="question-tag">if条件判断</span> <span class="question-tag">float函数</span> <span class="question-tag">格式化输出</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
x = float(input())
if x == 0:
    result = 0
else:
    result = 1 / (2 * x)
print(f'g({x:.3f}) = {result:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入可能包含小数，因此使用 `float(input())`。根据分段函数，先判断 `x` 是否为 0：如果是，结果为 0；否则计算 `1 / (2 * x)`，这样可以避免除以 0。

代码通过 `if...else` 分别处理这两种情况。最后 `:.3f` 表示将 x 和结果都按三位小数显示。

</div>

:::

::::

:::: question programming-2 | 7-5 三个数的大小比较

在同一行输入三个互不相等的整数a,b,c(a,b,c输入时以空格间隔)，在另一行从大到小输出这三个数。

#### 输入格式:

在同一行输入三个互不相等的整数a,b,c(a,b,c输入时以空格间隔)

#### 输出格式:

在一行中从大到小输出这三个数。

#### 输入样例1:

在这里给出一组输入。例如：

```text
20 10 30
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
30>20>10
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
-10 2 3
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
3>2>-10
```

<div class="question-tags"><span class="question-tag">整数转换</span> <span class="question-tag">列表降序排序</span> <span class="question-tag">print 分隔符</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
fields = input().split()
numbers = []
for field in fields:
    numbers.append(int(field))
numbers.sort(reverse=True)
print(numbers[0], numbers[1], numbers[2], sep='>')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先问“按什么比较”。`input().split()` 切出的每一项仍是文本，字符串按字符顺序比较，例如 `'10' < '2'`。题目要求比较整数，就在循环中把每一项转换成 `int` 后加入列表。

再决定排序方向与输出分隔符。`sort(reverse=True)` 让最大的数排在下标 0。样例 `20 10 30` 因而得到 `[30, 20, 10]`。把三个元素作为 `print` 的三个参数，并设 `sep='>'`，分隔符就只会出现在两个数之间，负数的负号也会自然保留。[对照 1-13 的列表排序](#judgment-13)

</div>

:::

::::

:::: question programming-3 | 7-6 计算在途时间

在同一行输入2个整数time1和time2(输入time1和time2以空格分隔)，表示火车的出发时间和到达时间，现要求计算并输出旅途时间。  
有效的时间范围是0000到2359，且不需要考虑出发时间晚于到达时间的情况。

#### 输入格式:

在同一行输入2个整数time1和time2(输入time1和time2以空格分隔)

#### 输出格式:

在途时间是m小时n分钟

#### 输入样例1:

在这里给出一组输入。例如：

```text
0615 1314
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
在途时间是6小时59分钟
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
0405 0605
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
在途时间是2小时0分钟
```

<div class="question-tags"><span class="question-tag">时间换算</span> <span class="question-tag">整除与取余</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
departure_text, arrival_text = input().split()
departure = int(departure_text)
arrival = int(arrival_text)

departure_minutes = departure // 100 * 60 + departure % 100
arrival_minutes = arrival // 100 * 60 + arrival % 100
duration = arrival_minutes - departure_minutes

hours = duration // 60
minutes = duration % 60
print(f'在途时间是{hours}小时{minutes}分钟')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

钟面上的 `HHMM` 把两个单位挤在同一串数字里。先拆成时、分，换成从零点起经过的分钟数，两个时刻才可以直接相减。

| 样例时刻 | 用 `// 100` 取小时 | 用 `% 100` 取分钟 | 从零点起的分钟数 |
| --- | --- | --- | --- |
| `0615` | 6 | 15 | `6 × 60 + 15 = 375` |
| `1314` | 13 | 14 | `13 × 60 + 14 = 794` |

同一天内相差 `794 - 375 = 419` 分钟。最后用 `419 // 60` 取整小时，用 `419 % 60` 取余下分钟，得到 6 小时 59 分钟。拆输入时每两位十进制数字为一组，所以用 100。还原时每 60 分钟为一小时，所以用 60。

</div>

:::

::::

:::: question programming-4 | 7-11 求平方与倒数序列的近似和

本题要求对两个正整数m和n（m≤n）编写程序，计算序列近似和。近似和定义为小于序列和的最大整数。（提示：用floor函数）

$m^{2}$+1/m+$(m+1)^{2}$+1/(m+1)+⋯+$n^{2}$+1/n。

#### 输入格式:

输入在一行中给出两个正整数m和n（m≤n），其间以空格分开。

#### 输出格式:

在一行中按照“sum ≈ S”的格式输出近似和S。

#### 输入样例:

在这里给出一组输入。例如：

```text
5  10
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
sum ≈ 355
```

<div class="question-tags"><span class="question-tag">循环累加</span> <span class="question-tag">向下取整</span> <span class="question-tag">序列求和</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
import math

m_text, n_text = input().split()
m = int(m_text)
n = int(n_text)
total = 0
for i in range(m, n + 1):
    total += i ** 2 + 1 / i

result = math.floor(total)
print(f'sum ≈ {result}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

从 m 到 n 逐个取整数 i，每一项为 `i ** 2 + 1 / i`，因此循环范围使用 `range(m, n + 1)`，保证包含 n。用累加变量 `total` 从 0 开始，在循环中把每一项加进去，就能求出整个序列的和。

最后用 `math.floor()` 向下取整，得到不大于总和的最大整数。题目提示使用 floor，因此最后输出 `math.floor(total)`。

题面写的是“小于序列和的最大整数”，但提示使用 `floor`。两者在总和恰为整数时有区别：例如输入 `1 1`，总和为 `2`，严格小于应得 `1`，而 `floor` 得 `2`。参考代码按题目提示使用 `floor`。

</div>

:::

::::

:::: question programming-5 | 7-12 计算函数f(x)

计算函数f(x):  
f(x) =![捕获.JPG](/images/problems/998d17f8300b.jpg)

#### 输入格式:

在一行输入x, x>0。

#### 输出格式:

在一行输出结果,函数值输出保留3位小数。

#### 输入样例1:

在这里给出一组输入。例如：

```text
3.64
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
f(3.64)=-3.907
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
20
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
f(20.0)=1212904.080
```

<div class="question-tags"><span class="question-tag">math模块</span> <span class="question-tag">三角函数</span> <span class="question-tag">数学函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
import math

x = float(input())
angle = math.radians(35)
numerator = math.exp(x) - 15 * x
denominator = math.sqrt(x ** 4 + 1)
result = math.sin(angle) + numerator / denominator - math.log(7 * x)
print(f'f({x})={result:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入 x 是实数，因此先用 `float(input())` 转换。公式中的正弦、指数、平方根和自然对数分别使用 `math.sin()`、`math.exp()`、`math.sqrt()` 和 `math.log()`。

题目中的角度是 35°，而 `math.sin()` 接收弧度，所以先用 `math.radians(35)` 转换。分式的分子和分母分别保存在 `numerator` 和 `denominator` 中，明确计算范围，最后通过 `:.3f` 将函数值保留三位小数。

</div>

:::

::::

:::: question programming-6 | 7-14 输出指定图形

输入正整数（1&lt;=n&lt;=7），输出指定图形。(提示：用`*`运算符）

#### 输入格式:

输入正整数n。

#### 输出格式:

输出有n行的图形。

#### 输入样例1:

在这里给出一组输入。例如：

```text
1
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
* 
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
3
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
* 
* * 
* * * 
```

<div class="question-tags"><span class="question-tag">for循环</span> <span class="question-tag">range函数</span> <span class="question-tag">字符串重复</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
row_count = int(input())
for row_number in range(1, row_count + 1):
    print('* ' * row_number)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先读取行数 `row_count`，再用 `range(1, row_count + 1)` 让循环变量 `row_number` 依次取 1 到 `row_count`。第 `row_number` 行需要输出 `row_number` 个星号，因此可以使用字符串重复：`'* ' * row_number`。

例如 `row_number = 3` 时，`'* ' * 3` 得到 `'* * * '`。`print()` 每次输出后会自动换行，于是最终形成 `row_count` 行递增的图形。

</div>

:::

::::
