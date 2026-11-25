---
title: 第1章作业
eyebrow: HOMEWORK 01
code: HOMEWORK 01
description: 题目、参考答案与解析。
questionGroups:
  - [判断题, judgment, 11]
  - [单选题, choice, 12]
  - [填空题, blank, 4]
  - [编程题, programming, 4]
---

<div class="editor-note">

题目整理自所提供的 PTA 网页，参考答案按 Python 3 核对，未在 PTA 平台提交验证。原题编号重复时保留原编号，以页面题序区分。

</div>

<h2 id="judgment" class="quiz-group">判断题<span>11 QUESTIONS</span></h2>

:::: question judgment-1 | 1-1 判断题

高级语言程序要被机器执行,只有用解释器来解释执行。

<div class="question-tags">
<span class="question-tag">编译与解释</span>
<span class="question-tag">Python 运行机制</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

“高级语言”描述的是编程语言，“编译”和“解释”描述的是程序的执行方式。程序可以先经过编译，再运行；也可以由解释器执行。同一种语言也可能采用两种方式。

例如，常用的 CPython 会先把 Python 源代码编译成字节码，再由解释器执行。因此，高级语言并非只能通过解释器运行，题目说法错误。

</div>

:::

::::

:::: question judgment-2 | 1-2 判断题

不可以在同一台计算机上安装多个不同的Python解释器版本。

<div class="question-tags">
<span class="question-tag">Python 解释器</span>
<span class="question-tag">Python 版本</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

解释器是负责执行 Python 代码的软件。同一台计算机可以安装多个 Python 版本，例如 Python 3.10 和 Python 3.12。运行程序时，选择对应的解释器即可。

因此，多个版本可以共存，题目说法错误。需要注意：安装第三方库时，也要确认使用的是当前运行程序的那个 Python 环境。

</div>

:::

::::

:::: question judgment-3 | 1-3 判断题

Python是一种跨平台、开源、免费的动态编程语言。

<div class="question-tags">
<span class="question-tag">Python 语言特点</span>
<span class="question-tag">动态类型</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

题目中的三个说法都正确：Python 可以在 Windows、macOS、Linux 等系统上运行，因此具有跨平台性；它是开源软件，源代码可以公开获取；使用 Python 本身不需要付费。

Python 还是动态类型语言，变量不需要提前声明固定类型。例如，`x = 3` 后还可以执行 `x = "hello"`，让变量名 `x` 绑定到字符串对象。因此本题正确。

</div>

:::

::::

:::: question judgment-4 | 1-4 判断题

math模块是python语言的数学模块。

<div class="question-tags">
<span class="question-tag">math 模块</span>
<span class="question-tag">Python 标准库</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`math` 是 Python 标准库中的数学模块，提供了常用数学函数和常量，例如平方根 `math.sqrt()`、正弦函数 `math.sin()` 和圆周率 `math.pi`。

使用前需要先导入：

```python
import math
print(math.sqrt(9))  # 3.0
```

因此，题目说法正确。

</div>

:::

::::

:::: question judgment-5 | 1-5 判断题

在Python 3.x中，input()函数把用户的键盘输入作为字符串返回。

<div class="question-tags">
<span class="question-tag">input 函数</span>
<span class="question-tag">字符串与数字转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`input()` 读取键盘输入，并且始终以字符串形式返回。即使输入的是 `18`，得到的也是字符串 `"18"`。

如果后续需要进行数学运算，就要先转换类型，例如 `int(input())` 将输入转成整数，`float(input())` 将输入转成浮点数。因此本题正确。

</div>

:::

::::

:::: question judgment-6 | 1-6 判断题

print()函数是输出函数。

<div class="question-tags">
<span class="question-tag">print 函数</span>
<span class="question-tag">输出格式</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`print()` 是 Python 的输出函数，可以把内容显示在屏幕上。例如：

```python
print("Hello")
```

默认情况下，`print(a, b)` 会在两个参数之间加一个空格，并在输出结束后换行。因此本题正确。

</div>

:::

::::

:::: question judgment-7 | 1-7 判断题

在Python中，可以用else作为变量名。

<div class="question-tags">
<span class="question-tag">标识符</span>
<span class="question-tag">Python 关键字</span>
</div>

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

:::: question judgment-8 | 1-8 判断题

已知 x=3, 则执行“ x=7”后，id(x)的返回值与原来没有变化。

<div class="question-tags">
<span class="question-tag">变量赋值</span>
<span class="question-tag">对象与 id()</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

理解本题的关键是：Python 中的变量不是一个装值的"盒子"，而是贴在对象上的"标签"。赋值语句 `x = 值` 做的事情是**让标签 `x` 指向某个对象**，而不是把值存进一个叫 `x` 的容器里。

- `x = 3` 时，Python 创建（或复用）整数对象 `3`，并把标签 `x` 贴上去，此时 `id(x)` 就是对象 `3` 在内存中的身份标识。
- `x = 7` 执行后，Python 创建一个新的整数对象 `7`，把标签 `x` 从 `3` 身上摘下来贴到 `7` 上。`x` 这个名字没变，但它所指向的对象已经换了。

因为 `3` 和 `7` 是两个不同的对象，它们的 `id()` 必然不同，所以重新赋值后 `id(x)` 一定发生了变化，题目说法错误。

</div>

:::

::::

:::: question judgment-9 | 1-9 判断题

字母A的ASCII编码值和Unicode编码值相同。

<div class="question-tags">
<span class="question-tag">ASCII 编码</span>
<span class="question-tag">Unicode 编码</span>
</div>

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

:::: question judgment-10 | 1-10 判断题

下面程序输入是`3 5`，输出是8。

```python
m,n=int(input().split())
print(m+n)
```

<div class="question-tags">
<span class="question-tag">split 函数</span>
<span class="question-tag">map 函数</span>
<span class="question-tag">int 类型转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入 `3 5` 后，`input()` 读取到字符串 `"3 5"`，`split()` 按空格拆分，得到列表 `['3', '5']`。

原程序接着执行 `int()`，试图把整个列表转换成整数。`int()` 只能转换单个数字字符串，不能直接转换列表，因此程序会报错，无法输出 8。

正确写法是：

```python
m, n = map(int, input().split())
print(m + n)
```

`map(int, ...)` 会把列表中的每个字符串分别转换成整数，再赋值给 `m` 和 `n`。

</div>

:::

::::

:::: question judgment-11 | 1-11 判断题

下面程序的输出是5。

```python
print=3
print(5)
```

<div class="question-tags">
<span class="question-tag">print 函数</span>
<span class="question-tag">变量赋值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

理解本题的关键是：`print` 本质上也只是一个**名字**，和普通变量名没有本质区别，只不过它在程序开始时就已经指向内置的输出函数。Python 并不会特殊保护内置函数的名字。

- 执行 `print = 3` 后，名字 `print` 被重新绑定到整数对象 `3`，原来指向输出函数的绑定被覆盖（这种现象称为"遮蔽"）。
- 此时 `print` 已经不再是函数，而是一个整数。
- 下一行 `print(5)` 的写法是"调用 `print` 并传入参数 `5`"，但 `print` 现在是整数 `3`，整数是不可调用的，程序会抛出 `TypeError`，而不是输出 `5`。

因此本题错误。这提醒我们：`print`、`list`、`sum` 这类内置名称虽然可以被重新赋值，但一旦赋值就会丢失原本的功能，应当避免用它们作普通变量名。

</div>

:::

::::

<h2 id="choice" class="quiz-group">单选题<span>12 QUESTIONS</span></h2>

:::: question choice-1 | 2-1 单选题

计算机存储器的单位是字节（B,Byte）,1B等于__________。

**A.** 一位二进制

**B.** 四位二进制

**C.** 八位二进制

**D.** 十六位二进制

<div class="question-tags">
<span class="question-tag">字节与比特</span>
<span class="question-tag">计算机存储单位</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

计算机存储单位是一套由小到大的换算体系：

- **bit（位）**：最小的信息单位，只能表示 0 或 1。
- **Byte（字节，B）**：规定由 **8 个 bit** 组成一组，是计算机中最基本的存储和寻址单位。
- **更大单位**：往上每级按 1024（即 2¹⁰）倍递增，如 1 KB = 1024 B，1 MB = 1024 KB，依此类推。

之所以 8 个 bit 为一组，是因为早期用 8 位恰好能表示 256（2⁸）种不同的编码，足以覆盖英文字母、数字和常用符号，久而久之成为统一标准。

因此，1B 等于八位二进制，选择 C。

</div>

:::

::::

:::: question choice-2 | 2-2 单选题

Python程序在Windows上的扩展名是_________。

**A.** py

**B.** exe

**C.** docx

**D.** jpg

<div class="question-tags">
<span class="question-tag">Python 文件扩展名</span>
<span class="question-tag">Python 源代码</span>
</div>

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

:::: question choice-3 | 2-3 单选题

Python的输出函数是________。

**A.** input()

**B.** print()

**C.** math()

**D.** turtle()

<div class="question-tags">
<span class="question-tag">print 函数</span>
<span class="question-tag">input 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`print()` 用于把内容输出到屏幕；`input()` 用于读取用户输入。`math` 是数学模块，`turtle` 是绘图模块。

因此，Python 的输出函数是 `print()`，选择 B。

</div>

:::

::::

:::: question choice-4 | 2-4 单选题

10的二进制值是__________。

**A.** 1100

**B.** 1010

**C.** 0011

**D.** 1110

<div class="question-tags">
<span class="question-tag">二进制转换</span>
<span class="question-tag">位权</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

十进制转二进制的通用方法是**除 2 取余法**：不断用商去除以 2，把每次的余数记录下来，最后把余数从下往上排列。

| 计算 | 商 | 余数 |
|---|---:|---:|
| 10 ÷ 2 | 5 | 0 |
| 5 ÷ 2 | 2 | 1 |
| 2 ÷ 2 | 1 | 0 |
| 1 ÷ 2 | 0 | 1 |

余数从下往上读，得到 `1010`。

也可以反过来验证：二进制从右往左每一位的位权依次是 1、2、4、8……，`1010` 对应 $1\times 8 + 0\times 4 + 1\times 2 + 0\times 1 = 10$，与原数相符。

因此选择 B。

</div>

:::

::::

:::: question choice-5 | 2-5 单选题

八进制35的十进制值是_________。

**A.** 30

**B.** 25

**C.** 19

**D.** 29

<div class="question-tags">
<span class="question-tag">八进制转换</span>
<span class="question-tag">位权</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

任何进制转十进制都遵循同一个通用公式：**把每一位数字乘以它所在位置的位权（基数的幂次），再把结果相加。** 位权从右往左依次是 基数⁰、基数¹、基数²……

对于八进制（基数为 8）的 `35`，从右往左两位的位权分别是 $8^0=1$ 和 $8^1=8$：

\[
3\times 8^1 + 5\times 8^0 = 24 + 5 = 29
\]

所以八进制 `35` 对应的十进制数是 29，选择 D。

</div>

:::

::::

:::: question choice-6 | 2-6 单选题

计算机系统由硬件和________组成。

**A.** 语言

**B.** 控制器

**C.** 存储器

**D.** 软件

<div class="question-tags">
<span class="question-tag">计算机硬件</span>
<span class="question-tag">计算机软件</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

计算机系统由硬件和软件组成。硬件是看得见、摸得着的物理设备，例如处理器、内存和存储器；软件是运行在计算机上的程序，例如操作系统和应用程序。

控制器和存储器都属于硬件的一部分，因此应选择“软件”，答案为 D。

</div>

:::

::::

:::: question choice-7 | 2-7 单选题

______是不等长编码。

**A.** ASCII码

**B.** Unicode码

**C.** UTF-8码

**D.** 以上都不

<div class="question-tags">
<span class="question-tag">Unicode 编码</span>
<span class="question-tag">UTF-8 编码</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

理解本题要先分清两个层面的概念：

- **ASCII / Unicode**：规定的是字符对应哪个**码点**（一个数字），不涉及具体怎么存成字节。ASCII 用 7 位数字表示每个字符，长度固定；Unicode 给每个字符分配唯一码点，本身也只是数字，不是存储方案。
- **UTF-8**：是把 Unicode 码点转换成**字节序列**的一种具体编码方案，规则是码点越小用的字节越少：常见英文字符用 1 个字节，大多数汉字用 3 个字节，罕见字符甚至要 4 个字节。

正因为不同字符占用的字节数不同，UTF-8 才被称为"变长编码"（不等长编码）。

因此，题目中的不等长编码是 UTF-8，选择 C。

</div>

:::

::::

:::: question choice-8 | 2-8 单选题

_______号表示同一行的后面部分是Python程序的注释。

**A.** *

**B.** %

**C.** /

**D.**

```python
#
```

<div class="question-tags">
<span class="question-tag">Python 注释</span>
<span class="question-tag"># 符号</span>
</div>

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

:::: question choice-9 | 2-9 单选题

Python语言正确的标识符是_______。

**A.** 2you

**B.** my-name

**C.** _item

**D.** abc*234

<div class="question-tags">
<span class="question-tag">标识符</span>
<span class="question-tag">变量命名规则</span>
</div>

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

:::: question choice-10 | 2-10 单选题

Python语言的官方网站地址是_______。

**A.** [www.python.org](http://www.python.org/)

**B.** [www.python.com](http://www.python.com/)

**C.** [www.python.edu](http://www.python.edu/)

**D.** [www.pythontutor.com](http://www.pythontutor.com/)

<div class="question-tags">
<span class="question-tag">Python 官方网站</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 的官方网站是 `www.python.org`，可以在这里获取 Python 安装程序、官方文档和相关资料。

因此选择 A。

</div>

:::

::::

:::: question choice-11 | 2-11 单选题

不是面向对象的程序设计语言是________。

**A.** Java

**B.** C

**C.** C++

**D.** Python

<div class="question-tags">
<span class="question-tag">面向对象编程</span>
<span class="question-tag">程序设计范式</span>
</div>

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

:::: question choice-12 | 2-12 单选题

下面程序的输出是什么？

```python
a,b=5,9
print(a, b)
```

**A.** `59`

**B.** `5,9`

**C.** 5$\Box$9 ($\Box$表示空格)

**D.** 5$\Box$$\Box$9 (5和9之间二个空格)

<div class="question-tags">
<span class="question-tag">print 函数</span>
<span class="question-tag">sep 参数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

执行 `print(a, b)` 时，`print()` 默认会用一个空格分隔多个参数。题目中 `a = 5`、`b = 9`，所以输出为：

```text
5 9
```

两个数字之间只有一个空格，因此选择 C。

</div>

:::

::::

<h2 id="blank" class="quiz-group">填空题<span>04 QUESTIONS</span></h2>

:::: question blank-1 | 4-1 填空题

十进制19.625的二进制是 _____ 。（整数部分用八位二进制表示）

<div class="question-tags">
<span class="question-tag">二进制转换</span>
<span class="question-tag">小数进制转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`00010011.101`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

带小数的十进制数要**把整数部分和小数部分分开转换**，因为两部分的转换方法正好相反：整数部分是"除 2 取余"，小数部分是"乘 2 取整"，最后再拼接在一起。

**整数部分 19：除以 2 依次取余，余数从下往上读：**

| 计算 | 商 | 余数 |
|---|---:|---:|
| 19 ÷ 2 | 9 | 1 |
| 9 ÷ 2 | 4 | 1 |
| 4 ÷ 2 | 2 | 0 |
| 2 ÷ 2 | 1 | 0 |
| 1 ÷ 2 | 0 | 1 |

余数从下往上读得到 `10011`。题目要求八位，因此在左侧补三个 0，得到 `00010011`。

**小数部分 0.625：不断乘以 2，每次记录结果的整数部分，再把小数部分继续乘 2，直到小数部分变为 0（或达到题目要求的位数）：**

| 计算 | 记录的整数部分 |
|---|---:|
| 0.625 × 2 = 1.25 | 1 |
| 0.25 × 2 = 0.5 | 0 |
| 0.5 × 2 = 1.0 | 1 |

按计算顺序从上往下排列，得到 `.101`。最后把两部分拼接，答案为 `00010011.101`。

</div>

:::

::::

:::: question blank-2 | 4-2 填空题

十六进制`2AC`的八进制表示是 _____ 。

<div class="question-tags">
<span class="question-tag">十六进制转换</span>
<span class="question-tag">八进制转换</span>
</div>

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

:::: question blank-3 | 4-3 填空题

十进制106的原码是 _____ ，反码是 _____ ，补码是 _____ 。 （用八位表示）

<div class="question-tags">
<span class="question-tag">原码、反码与补码</span>
<span class="question-tag">二进制表示</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`01101010`、`01101010`、`01101010`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

在带符号数的八位表示中，**最高位是符号位**（0 表示正数，1 表示负数），其余 7 位表示数值大小。原码、反码、补码的转换规则如下：

| | 正数 | 负数 |
|---|---|---|
| 原码 | 符号位 0 + 数值的二进制 | 符号位 1 + 数值的二进制 |
| 反码 | 与原码相同 | 符号位不变，数值位逐位取反 |
| 补码 | 与原码相同 | 反码 + 1 |

正数的原码、反码、补码之所以完全相同，是因为正数不需要做符号位以外的变换。

先把 106 转换成二进制：

\[
106 = 64 + 32 + 8 + 2 = (1101010)_2
\]

写成八位（符号位 0 + 7 位数值）是 `01101010`。按上表，106 是正数，三种编码完全相同。

因此三个空依次填写：`01101010`、`01101010`、`01101010`。

</div>

:::

::::

:::: question blank-4 | 4-4 填空题

-78的原码是 _____ ，反码是 _____ ，补码是 _____ 。 （用八位表示）

<div class="question-tags">
<span class="question-tag">原码、反码与补码</span>
<span class="question-tag">负数的二进制表示</span>
</div>

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

**第一步：** 先写出绝对值 78 的八位二进制：`01001110`。

**第二步：原码** —— 把符号位改为 1，数值位不变，得到 `11001110`。

**第三步：反码** —— 保留符号位 1，将其余七位逐位取反，得到 `10110001`。

**第四步：补码** —— 在反码基础上加 1，得到 `10110010`。

因此答案依次为 `11001110`、`10110001`、`10110010`。

补码之所以常用，是因为用它做加减法时不需要对符号位做特殊处理，计算机硬件可以统一按加法处理，同时也避免了原码、反码中"+0"和"-0"同时存在的歧义。

</div>

:::

::::

<h2 id="programming" class="quiz-group">编程题<span>04 QUESTIONS</span></h2>

:::: question programming-1 | 7-1 从键盘输入两个数，求它们的和并输出

本题目要求读入2个整数A和B，然后输出它们的和。

#### 输入格式:

在一行中给出一个被加数  
在另一行中给出一个加数

#### 输出格式:

在一行中输出和值。

#### 输入样例:

在这里给出一组输入。例如：

```text
18
-48
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
-30
```

<div class="question-tags">
<span class="question-tag">input 函数</span>
<span class="question-tag">int 类型转换</span>
<span class="question-tag">print 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a = int(input())
b = int(input())
print(a + b)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

题目要求读取两行整数，再输出它们的和，因此需要调用两次 `input()`：

```python
a = int(input())
b = int(input())
print(a + b)
```

`input()` 读取一行输入，`int()` 将字符串转换成整数。第一行读入 `18`，第二行读入 `-48`，所以 `a + b = -30`，最后由 `print()` 输出结果。

注意：题目要求两个数分两行输入，因此这里要写两次 `input()`。

</div>

:::

::::

:::: question programming-2 | 7-2 从键盘输入三个数到a,b,c中，按公式值输出

在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值

#### 输入格式:

在一行中输入三个数。

#### 输出格式:

在一行中输出公式值。

#### 输入样例:

在这里给出一组输入。例如：

```text
3 4 5
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
-44
```

<div class="question-tags">
<span class="question-tag">split 函数</span>
<span class="question-tag">map 函数</span>
<span class="question-tag">算术运算符</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a, b, c = map(int, input().split())
print(b * b - 4 * a * c)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

题目中的三个数在同一行输入，因此可以先用 `split()` 拆分，再用 `map(int, ...)` 将它们转换成整数：

```python
a, b, c = map(int, input().split())
```

接着计算题目要求的表达式：

```python
print(b * b - 4 * a * c)
```

输入 `3 4 5` 时，`a = 3`、`b = 4`、`c = 5`，计算结果为：

\[
4\times4-4\times3\times5=16-60=-44
\]

因此输出 `-44`。

</div>

:::

::::

:::: question programming-3 | 7-3 输出“人生苦短，我学Python”

#### 输入格式:

无

#### 输出格式:

人生苦短，我学Python

#### 输入样例:

```text

```

#### 输出样例:

```text
人生苦短，我学Python
```

<div class="question-tags">
<span class="question-tag">print 函数</span>
<span class="question-tag">字符串输出</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
print('人生苦短，我学Python')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这道题没有输入，只要求输出指定的一句话。直接使用 `print()`，并将要输出的内容放在引号中即可：

```python
print('人生苦短，我学Python')
```

注意保留题目中的中文逗号，以及 `Python` 的大小写。

</div>

:::

::::

:::: question programming-4 | 7-4 写字母H

字母`H`可以这样输出。编程序输出`H`

```python
*   *
*   *
*****
*   *
*   *
```

#### 输入格式:

无

#### 输出格式:

输出字母`H`图形。

#### 输入样例:

在这里给出一组输入。例如：

```text

```

#### 输出样例:

在这里给出相应的输出。例如：

```text
*   *
*   *
*****
*   *
*   *
```

<div class="question-tags">
<span class="question-tag">print 函数</span>
<span class="question-tag">转义字符 \n</span>
<span class="question-tag">字符串输出</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
print('*   *\n*   *\n*****\n*   *\n*   *')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

题目要求输出一个由五行组成的字母 H。可以把五行内容放在同一个字符串中，并用 `\n` 表示换行：

```python
print('*   *\n*   *\n*****\n*   *\n*   *')
```

`\n` 是换行符，运行时会让后面的内容从下一行开始输出。每行两个星号之间有三个空格，空格数量也要与样例保持一致。

</div>

:::

::::
