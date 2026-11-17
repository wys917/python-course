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

<div class="section-label">题干 <span>QUESTION</span></div>

高级语言程序要被机器执行,只有用解释器来解释执行。

::: answer

F（错误）。

:::

::: explanation

高级语言既可编译执行，也可解释执行，或结合两者，并非只能使用解释器。

<!-- teaching-notes:start -->

**从本题理解：源代码怎样运行**

“高级语言”描述的是语言抽象层次，“编译”和“解释”描述的是实现程序的执行方式，不能把两者一一对应。编译器可以先把程序翻译成另一种形式，解释器则负责执行相应指令；同一种语言也可以有不同实现。

以常用的 CPython 为例，源代码先编译成字节码，再由解释器执行，因此把 Python 理解成“完全不经过编译”也不准确。`.py` 是源文件扩展名，不是运行结果；终端执行 `python 文件名.py` 时，真正运行程序的是所选 Python 解释器。交互环境会显示裸表达式的值，脚本通常需要 `print()` 才会输出。

继续阅读：[第1章：Python 与运行环境](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-2 | 1-2 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

不可以在同一台计算机上安装多个不同的Python解释器版本。

::: answer

F（错误）。

:::

::: explanation

多个 Python 版本可以共存，运行程序时需选择对应解释器。

<!-- teaching-notes:start -->

**从本题理解：解释器、编辑器与版本**

编辑器负责写代码，解释器负责执行代码，二者不是同一个工具。IDLE 将编辑和交互运行放在一起，但保存 `.py` 文件后，也可以从终端调用解释器执行。

同一台电脑可以安装多个 Python 版本。遇到“这里能运行，那里找不到模块”，先确认两个环境使用的解释器是否一致：在交互环境执行 `import sys`，再查看 `sys.executable` 和 `sys.version`。安装第三方包时，`python -m pip` 会使用这个 `python` 对应的环境。开源、免费和跨平台不意味着任意平台的文件路径、系统命令都完全相同。

继续阅读：[第1章：Python 简介与开发环境](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-3 | 1-3 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

Python是一种跨平台、开源、免费的动态编程语言。

::: answer

T（正确）。

:::

::: explanation

Python 跨平台、开源、免费，变量名在运行时绑定到对象。

<!-- teaching-notes:start -->

**从本题理解：解释器、编辑器与版本**

编辑器负责写代码，解释器负责执行代码，二者不是同一个工具。IDLE 将编辑和交互运行放在一起，但保存 `.py` 文件后，也可以从终端调用解释器执行。

同一台电脑可以安装多个 Python 版本。遇到“这里能运行，那里找不到模块”，先确认两个环境使用的解释器是否一致：在交互环境执行 `import sys`，再查看 `sys.executable` 和 `sys.version`。安装第三方包时，`python -m pip` 会使用这个 `python` 对应的环境。开源、免费和跨平台不意味着任意平台的文件路径、系统命令都完全相同。

继续阅读：[第1章：Python 简介与开发环境](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-4 | 1-4 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

math模块是python语言的数学模块。

::: answer

T（正确）。

:::

::: explanation

标准库 math 提供平方根、三角函数、向上取整等数学功能，使用前先导入。

<!-- teaching-notes:start -->

**从本题理解：数学公式如何翻译成 Python**

先识别公式的运算结构，再选择函数。平方根用 `math.sqrt()`，自然对数用 `math.log()`，指数 $e^x$ 用 `math.exp()`；乘法必须明确写 `*`，分式的分子、分母需要分别加括号。`sqrt(4)` 返回 `2.0`，所以后续乘积可能是浮点数而不是整数。

三角函数参数以弧度为单位，角度先用 `math.radians()` 转换。还要检查定义域：实数平方根的参数不能为负，自然对数参数必须大于 0，分母不能为 0。输出格式化只控制最后显示多少位，并不修复公式、定义域或中间计算的错误。`ceil()` 向上取整，`floor()` 向下取整，均与向零截断的 `int()` 有区别。

继续阅读：[第2章：math 库](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-5 | 1-5 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

在Python 3.x中，input()函数把用户的键盘输入作为字符串返回。

::: answer

T（正确）。

:::

::: explanation

input() 返回字符串，去掉行末换行；数值输入需要 int() 或 float() 转换。

<!-- teaching-notes:start -->

**从本题理解：输入处理的四个步骤**

多项数值输入可按“读整行 → 拆文本 → 逐项转换 → 拆包赋值”理解。输入 `3 5` 时，`input()` 返回 `'3 5'`，`split()` 得到 `['3','5']`，`map(int,...)` 按需将每一项转成整数，最后两个变量分别接收 3 和 5。

```python
line = input()
parts = line.split()
m, n = map(int, parts)
```

`int(parts)` 不会逐项处理，而会因参数是列表而报错。输入 `3,5` 应使用 `split(',')`。拆出的项目数和变量数不匹配会产生 `ValueError`；数字格式非法也会在转换时产生 `ValueError`。处理整行字符串时不要随意 `split()`，否则原有空格结构会丢失。

继续阅读：[第1章：输入及输出函数](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-6 | 1-6 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

print()函数是输出函数。

::: answer

T（正确）。

:::

::: explanation

print() 将参数转换成文本并输出，默认以空格分隔、换行结束。

<!-- teaching-notes:start -->

**从本题理解：输出内容由哪些部分组成**

`print(a,b)` 不是把两个变量原样紧贴输出，而是先将参数转成文本，再用 `sep` 连接，最后加上 `end`。默认 `sep=' '`、`end='\n'`，所以参数间有一个空格，输出后换行。`print(a,b,sep='')` 才是无分隔拼接。

```python
print(5, 9)             # 5 9
print(5, 9, sep='-')    # 5-9
print('*', end=' ')     # 星号后有一个空格，暂不换行
```

判断题和编程题都要检查前导空格、参数间空格、行尾空格与换行。不要给自动评测的输出加入“请输入”等提示语。观察不可见字符时可先构造字符串，再使用 `repr()` 查看其边界；直接看网页中排版后的文字不一定能分辨空格数量。

继续阅读：[第1章：print 与输出格式](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-7 | 1-7 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

在Python中，可以用else作为变量名。

::: answer

F（错误）。

:::

::: explanation

else 是关键字，不能作为变量名。

<!-- teaching-notes:start -->

**从本题理解：标识符、关键字与内置名称**

入门题中常见的合法名字由字母、数字和下划线组成，不能以数字开头，且区分大小写。`item_1` 与 `_item` 合法；`1item` 不合法；`item-name` 会被当成减法表达式，而不是一个名字。Python 也允许部分 Unicode 字符用于标识符。

还要区分关键字和内置名称：`else`、`for` 是语法保留字，不能作普通变量名；`print`、`list` 不是关键字，给它们赋值在语法上合法，却会遮蔽原有功能。例如 `print=3` 后再执行 `print(5)`，是在调用整数，因而报 `TypeError`。布尔常量必须写作 `True`、`False`，大小写变化后会被当成别的名字。

继续阅读：[第1章：标识符和变量](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-8 | 1-8 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

已知 x=3, 则执行“ x=7”后，id(x)的返回值与原来没有变化。

::: answer

F（错误）。

:::

::: explanation

x=7 将 x 从整数对象 3 重新绑定到整数对象 7，对象身份随之改变。

<!-- teaching-notes:start -->

**从本题理解：变量绑定与对象身份**

把变量理解成“指向对象的名字”，比理解成“永远装着某种类型的盒子”更准确。`x=3` 将名字 `x` 绑定到整数对象；执行 `x=7` 是重新绑定，不是把整数对象 3 修改成 7。类型属于对象，变量可以随后绑定到另一种类型的对象。

`==` 比较值，`is` 比较是否为同一对象，`id()` 给出对象存活期间的身份标识。判断两个数是否相等应使用 `==`，不能依赖小整数缓存或字符串复用造成的 `is` 结果。可变列表的原地修改与名字重新赋值也有区别：前者可能被所有别名观察到，后者只改变当前名字的绑定。

继续阅读：[第3章：赋值与对象引用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-9 | 1-9 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

字母A的ASCII编码值和Unicode编码值相同。

::: answer

T（正确）。

:::

::: explanation

ASCII 字符 A 的编码值与 Unicode 码点均为十进制 65。

<!-- teaching-notes:start -->

**从本题理解：字符、码点与字节编码**

Unicode 为字符分配码点，例如 `ord('A')` 为 65，`ord('张')` 为 24352；`chr()` 完成反向转换。`U+5F20` 和十进制 24352 表示同一码点，只是记数方式不同。`ord()` 接收单个字符，不能直接把整个多字符字符串转换成一个码点。

UTF-8 则规定如何把码点编码成字节，不能把它和 Unicode 字符集合混为一谈。例如 `len('张')` 为 1，而 `len('张'.encode('utf-8'))` 为 3；前者数 Python 字符串中的码点，后者数字节。ASCII 字符在 UTF-8 中仍占一个字节，这也是英文字符 A 的编码值在本题中保持 65 的原因。

继续阅读：[第1章：字符编码](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-10 | 1-10 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序输入是`3 5`，输出是8。

```python
m,n=int(input().split())
print(m+n)
```

::: answer

F（错误）。

:::

::: explanation

split() 得到列表 ['3','5']，int() 不能一次转换整个列表。应写 m,n=map(int,input().split())。

<!-- teaching-notes:start -->

**从本题理解：输入处理的四个步骤**

多项数值输入可按“读整行 → 拆文本 → 逐项转换 → 拆包赋值”理解。输入 `3 5` 时，`input()` 返回 `'3 5'`，`split()` 得到 `['3','5']`，`map(int,...)` 按需将每一项转成整数，最后两个变量分别接收 3 和 5。

```python
line = input()
parts = line.split()
m, n = map(int, parts)
```

`int(parts)` 不会逐项处理，而会因参数是列表而报错。输入 `3,5` 应使用 `split(',')`。拆出的项目数和变量数不匹配会产生 `ValueError`；数字格式非法也会在转换时产生 `ValueError`。处理整行字符串时不要随意 `split()`，否则原有空格结构会丢失。

继续阅读：[第1章：输入及输出函数](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-11 | 1-11 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序的输出是5。

```python
print=3
print(5)
```

::: answer

F（错误）。

:::

::: explanation

print=3 遮蔽了内置函数名称，随后 print(5) 相当于调用整数，引发 TypeError。

<!-- teaching-notes:start -->

**从本题理解：标识符、关键字与内置名称**

入门题中常见的合法名字由字母、数字和下划线组成，不能以数字开头，且区分大小写。`item_1` 与 `_item` 合法；`1item` 不合法；`item-name` 会被当成减法表达式，而不是一个名字。Python 也允许部分 Unicode 字符用于标识符。

还要区分关键字和内置名称：`else`、`for` 是语法保留字，不能作普通变量名；`print`、`list` 不是关键字，给它们赋值在语法上合法，却会遮蔽原有功能。例如 `print=3` 后再执行 `print(5)`，是在调用整数，因而报 `TypeError`。布尔常量必须写作 `True`、`False`，大小写变化后会被当成别的名字。

继续阅读：[第1章：标识符和变量](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="choice" class="quiz-group">单选题<span>12 QUESTIONS</span></h2>

:::: question choice-1 | 2-1 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

计算机存储器的单位是字节（B,Byte）,1B等于__________。

**A.** 一位二进制

**B.** 四位二进制

**C.** 八位二进制

**D.** 十六位二进制

::: answer

C。

:::

::: explanation

1 字节等于 8 个二进制位，即 1 B = 8 bit。

<!-- teaching-notes:start -->

**从本题理解：硬件、软件与存储单位**

硬件是处理器、内存、存储设备等物理部件；软件是让硬件完成任务的程序及相关数据。操作系统属于系统软件，编辑器等工具属于软件，Python 源程序本身也不是硬件。

最小的二进制信息单位是 bit，一个字节 B 通常含 8 bit，因此 2 B 可保存 16 个二进制位。要区分“位数”和“可表示的状态数”：8 bit 有 $2^8=256$ 种组合，无符号整数范围为 0～255，而不是 1～256。字符占几个字节还取决于编码，不能把一个字符直接等同于一个字节。

继续阅读：[第1章：计算机基础](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-2 | 2-2 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python程序在Windows上的扩展名是_________。

**A.** py

**B.** exe

**C.** docx

**D.** jpg

::: answer

A。

:::

::: explanation

Python 源代码脚本通常使用 .py 扩展名。

<!-- teaching-notes:start -->

**从本题理解：源代码怎样运行**

“高级语言”描述的是语言抽象层次，“编译”和“解释”描述的是实现程序的执行方式，不能把两者一一对应。编译器可以先把程序翻译成另一种形式，解释器则负责执行相应指令；同一种语言也可以有不同实现。

以常用的 CPython 为例，源代码先编译成字节码，再由解释器执行，因此把 Python 理解成“完全不经过编译”也不准确。`.py` 是源文件扩展名，不是运行结果；终端执行 `python 文件名.py` 时，真正运行程序的是所选 Python 解释器。交互环境会显示裸表达式的值，脚本通常需要 `print()` 才会输出。

继续阅读：[第1章：Python 与运行环境](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-3 | 2-3 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python的输出函数是________。

**A.** input()

**B.** print()

**C.** math()

**D.** turtle()

::: answer

B。

:::

::: explanation

print() 输出，input() 输入。

<!-- teaching-notes:start -->

**从本题理解：输入处理的四个步骤**

多项数值输入可按“读整行 → 拆文本 → 逐项转换 → 拆包赋值”理解。输入 `3 5` 时，`input()` 返回 `'3 5'`，`split()` 得到 `['3','5']`，`map(int,...)` 按需将每一项转成整数，最后两个变量分别接收 3 和 5。

```python
line = input()
parts = line.split()
m, n = map(int, parts)
```

`int(parts)` 不会逐项处理，而会因参数是列表而报错。输入 `3,5` 应使用 `split(',')`。拆出的项目数和变量数不匹配会产生 `ValueError`；数字格式非法也会在转换时产生 `ValueError`。处理整行字符串时不要随意 `split()`，否则原有空格结构会丢失。

继续阅读：[第1章：输入及输出函数](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-4 | 2-4 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

10的二进制值是__________。

**A.** 1100

**B.** 1010

**C.** 0011

**D.** 1110

::: answer

B。

:::

::: explanation

10 = 8+2，二进制为 1010。

<!-- teaching-notes:start -->

**从本题理解：进制转换与位权**

在基数为 $b$ 的计数制中，各位从右往左的权重依次为 $b^0,b^1,b^2,\ldots$。例如八进制 `35` 是 $3\times8+5=29$，十六进制 `2AC` 是 $2\times16^2+10\times16+12=684$。转换到目标进制时，可反复除以目标基数，并把余数倒序排列。

```python
n = int('2AC', 16)
print(n)          # 684
print(oct(n))     # 0o1254
print(bin(10))    # 0b1010
```

整数对象只保存数值，`0xA` 与 `10` 不是两种整数类型。`bin()`、`oct()`、`hex()` 返回带前缀的字符串，而 `int(文本,基数)` 返回整数；题目只要求数字部分时，不能额外写进制前缀。某基数的合法数码必须小于该基数，例如八进制不能含 8 或 9。

继续阅读：[第1章：数制与进制转换](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-5 | 2-5 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

八进制35的十进制值是_________。

**A.** 30

**B.** 25

**C.** 19

**D.** 29

::: answer

D。

:::

::: explanation

八进制 35 = 3×8+5 = 29。

<!-- teaching-notes:start -->

**从本题理解：进制转换与位权**

在基数为 $b$ 的计数制中，各位从右往左的权重依次为 $b^0,b^1,b^2,\ldots$。例如八进制 `35` 是 $3\times8+5=29$，十六进制 `2AC` 是 $2\times16^2+10\times16+12=684$。转换到目标进制时，可反复除以目标基数，并把余数倒序排列。

```python
n = int('2AC', 16)
print(n)          # 684
print(oct(n))     # 0o1254
print(bin(10))    # 0b1010
```

整数对象只保存数值，`0xA` 与 `10` 不是两种整数类型。`bin()`、`oct()`、`hex()` 返回带前缀的字符串，而 `int(文本,基数)` 返回整数；题目只要求数字部分时，不能额外写进制前缀。某基数的合法数码必须小于该基数，例如八进制不能含 8 或 9。

继续阅读：[第1章：数制与进制转换](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-6 | 2-6 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

计算机系统由硬件和________组成。

**A.** 语言

**B.** 控制器

**C.** 存储器

**D.** 软件

::: answer

D。

:::

::: explanation

计算机系统包括硬件和软件。

<!-- teaching-notes:start -->

**从本题理解：硬件、软件与存储单位**

硬件是处理器、内存、存储设备等物理部件；软件是让硬件完成任务的程序及相关数据。操作系统属于系统软件，编辑器等工具属于软件，Python 源程序本身也不是硬件。

最小的二进制信息单位是 bit，一个字节 B 通常含 8 bit，因此 2 B 可保存 16 个二进制位。要区分“位数”和“可表示的状态数”：8 bit 有 $2^8=256$ 种组合，无符号整数范围为 0～255，而不是 1～256。字符占几个字节还取决于编码，不能把一个字符直接等同于一个字节。

继续阅读：[第1章：计算机基础](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-7 | 2-7 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

______是不等长编码。

**A.** ASCII码

**B.** Unicode码

**C.** UTF-8码

**D.** 以上都不

::: answer

C。

:::

::: explanation

UTF-8 是变长编码，Unicode 标量值编码后占 1～4 字节；Unicode 本身是字符与码点体系，不应简单视为一种定长字节编码。

<!-- teaching-notes:start -->

**从本题理解：字符、码点与字节编码**

Unicode 为字符分配码点，例如 `ord('A')` 为 65，`ord('张')` 为 24352；`chr()` 完成反向转换。`U+5F20` 和十进制 24352 表示同一码点，只是记数方式不同。`ord()` 接收单个字符，不能直接把整个多字符字符串转换成一个码点。

UTF-8 则规定如何把码点编码成字节，不能把它和 Unicode 字符集合混为一谈。例如 `len('张')` 为 1，而 `len('张'.encode('utf-8'))` 为 3；前者数 Python 字符串中的码点，后者数字节。ASCII 字符在 UTF-8 中仍占一个字节，这也是英文字符 A 的编码值在本题中保持 65 的原因。

继续阅读：[第1章：字符编码](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-8 | 2-8 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

_______号表示同一行的后面部分是Python程序的注释。

**A.** *

**B.** %

**C.** /

**D.**

```python
#
```

::: answer

D。

:::

::: explanation

英文半角 # 引出同一行的注释，字符串内部的 # 不作为注释起点。

<!-- teaching-notes:start -->

**从本题理解：注释与字符串的边界**

英文半角 `#` 在字符串外引出单行注释，从它开始到本行末尾不再作为代码执行。例如 `x=3 # 说明` 中，赋值仍然会执行。全角 `＃` 不是 Python 注释符号。

字符串内部的 `#` 属于普通字符：`print('#')` 会输出井号。判断一段代码时，先确认引号边界，再识别注释，不能看到 `#` 就认为后面全部无效。三引号首先定义的是多行字符串；它在模块、类或函数开头时可以作为文档字符串，不能简单地把所有三引号字符串都称为注释。

继续阅读：[第1章：注释](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-9 | 2-9 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python语言正确的标识符是_______。

**A.** 2you

**B.** my-name

**C.** _item

**D.** abc*234

::: answer

C。

:::

::: explanation

_item 以字母或下划线开头，后续可含数字；其他项含非法字符或以数字开头。

<!-- teaching-notes:start -->

**从本题理解：标识符、关键字与内置名称**

入门题中常见的合法名字由字母、数字和下划线组成，不能以数字开头，且区分大小写。`item_1` 与 `_item` 合法；`1item` 不合法；`item-name` 会被当成减法表达式，而不是一个名字。Python 也允许部分 Unicode 字符用于标识符。

还要区分关键字和内置名称：`else`、`for` 是语法保留字，不能作普通变量名；`print`、`list` 不是关键字，给它们赋值在语法上合法，却会遮蔽原有功能。例如 `print=3` 后再执行 `print(5)`，是在调用整数，因而报 `TypeError`。布尔常量必须写作 `True`、`False`，大小写变化后会被当成别的名字。

继续阅读：[第1章：标识符和变量](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-10 | 2-10 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python语言的官方网站地址是_______。

**A.** [www.python.org](http://www.python.org/)

**B.** [www.python.com](http://www.python.com/)

**C.** [www.python.edu](http://www.python.edu/)

**D.** [www.pythontutor.com](http://www.pythontutor.com/)

::: answer

A。

:::

::: explanation

Python 的官方网站是 www.python.org。

<!-- teaching-notes:start -->

**从本题理解：解释器、编辑器与版本**

编辑器负责写代码，解释器负责执行代码，二者不是同一个工具。IDLE 将编辑和交互运行放在一起，但保存 `.py` 文件后，也可以从终端调用解释器执行。

同一台电脑可以安装多个 Python 版本。遇到“这里能运行，那里找不到模块”，先确认两个环境使用的解释器是否一致：在交互环境执行 `import sys`，再查看 `sys.executable` 和 `sys.version`。安装第三方包时，`python -m pip` 会使用这个 `python` 对应的环境。开源、免费和跨平台不意味着任意平台的文件路径、系统命令都完全相同。

继续阅读：[第1章：Python 简介与开发环境](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-11 | 2-11 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

不是面向对象的程序设计语言是________。

**A.** Java

**B.** C

**C.** C++

**D.** Python

::: answer

B。

:::

::: explanation

按题目对语言的常见分类，C 是过程式语言；Java、C++ 和 Python 提供直接的面向对象机制。

<!-- teaching-notes:start -->

**从本题理解：程序设计语言的分类**

过程式编程围绕“按什么步骤完成任务”组织函数和语句；面向对象编程把状态与相关操作组织到对象中。它们是组织程序的思路，不是语言只能二选一的标签。

例如计算一组成绩的平均分，可以用函数接收列表并返回结果；管理学生姓名、成绩及相关操作时，也可以设计 `Student` 类。Python 支持过程式、面向对象等多种方式。题目按课程常见分类选择答案时，需要理解分类依据；不能据此推断 Python 程序必须使用类，或 C 语言不能实现复杂的数据抽象。

继续阅读：[第8章：类和对象](../topics/chapter-08.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-12 | 2-12 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序的输出是什么？

```python
a,b=5,9
print(a, b)
```

**A.** `59`

**B.** `5,9`

**C.** 5$\Box$9 ($\Box$表示空格)

**D.** 5$\Box$$\Box$9 (5和9之间二个空格)

::: answer

C。

:::

::: explanation

print(a,b) 默认在两个参数间输出一个空格，因此是 5□9。

<!-- teaching-notes:start -->

**从本题理解：输出内容由哪些部分组成**

`print(a,b)` 不是把两个变量原样紧贴输出，而是先将参数转成文本，再用 `sep` 连接，最后加上 `end`。默认 `sep=' '`、`end='\n'`，所以参数间有一个空格，输出后换行。`print(a,b,sep='')` 才是无分隔拼接。

```python
print(5, 9)             # 5 9
print(5, 9, sep='-')    # 5-9
print('*', end=' ')     # 星号后有一个空格，暂不换行
```

判断题和编程题都要检查前导空格、参数间空格、行尾空格与换行。不要给自动评测的输出加入“请输入”等提示语。观察不可见字符时可先构造字符串，再使用 `repr()` 查看其边界；直接看网页中排版后的文字不一定能分辨空格数量。

继续阅读：[第1章：print 与输出格式](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="blank" class="quiz-group">填空题<span>04 QUESTIONS</span></h2>

:::: question blank-1 | 4-1 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

十进制19.625的二进制是 _____ 。（整数部分用八位二进制表示）

::: answer

`00010011.101`。

:::

::: explanation

整数 19 为 10011，补足 8 位得到 00010011；小数 .625 乘 2 取整依次为 1、0、1。

<!-- teaching-notes:start -->

**从本题理解：整数和小数的进制转换方向不同**

整数部分用“除基取余、逆序排列”；纯小数部分用“乘基取整、顺序排列”。例如 $0.625\times2=1.25$ 取 1，$0.25\times2=0.5$ 取 0，$0.5\times2=1$ 取 1，于是 $0.625=(0.101)_2$。整数 19 是 `10011`，若题目要求整数部分占 8 位，再在左侧补零。

为什么有些小数算不完？一个最简分数能用有限二进制小数表示，当且仅当分母只含质因子 2，例如 $5/8$ 可以，$1/10$ 不可以。因此循环既要判断余数是否归零，也要遵守题目给定位数上限；截断和四舍五入是两种不同要求。精确转换十进制输入时，可用 `Fraction(输入字符串)`，避免先转 `float` 造成近似。

继续阅读：[第1章：数制与进制转换](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-2 | 4-2 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

十六进制`2AC`的八进制表示是 _____ 。

::: answer

`1254`。

:::

::: explanation

2AC₁₆ = 684₁₀ = 1254₈；按题目不额外添加 0o 前缀。

<!-- teaching-notes:start -->

**从本题理解：进制转换与位权**

在基数为 $b$ 的计数制中，各位从右往左的权重依次为 $b^0,b^1,b^2,\ldots$。例如八进制 `35` 是 $3\times8+5=29$，十六进制 `2AC` 是 $2\times16^2+10\times16+12=684$。转换到目标进制时，可反复除以目标基数，并把余数倒序排列。

```python
n = int('2AC', 16)
print(n)          # 684
print(oct(n))     # 0o1254
print(bin(10))    # 0b1010
```

整数对象只保存数值，`0xA` 与 `10` 不是两种整数类型。`bin()`、`oct()`、`hex()` 返回带前缀的字符串，而 `int(文本,基数)` 返回整数；题目只要求数字部分时，不能额外写进制前缀。某基数的合法数码必须小于该基数，例如八进制不能含 8 或 9。

继续阅读：[第1章：数制与进制转换](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-3 | 4-3 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

十进制106的原码是 _____ ，反码是 _____ ，补码是 _____ 。 （用八位表示）

::: answer

`01101010`、`01101010`、`01101010`。

:::

::: explanation

106=64+32+8+2，是正数，8 位原码、反码和补码相同。

<!-- teaching-notes:start -->

**从本题理解：固定字长下的原码、反码、补码**

先确定题目规定的字长，再写二进制位。8 位有符号表示中，正数的原码、反码和补码相同，最高位为 0；负数的原码将最高位置 1，反码保留符号位并翻转其余位，补码在反码基础上加 1。

以 -78 为例：正数 78 是 `01001110`，负数原码 `11001110`，反码 `10110001`，补码 `10110010`。也可用 $2^8-78=178$ 验证其补码位型。8 位补码范围为 -128～127，不能把任意大整数强行塞进 8 位。Python 的 `int` 不固定为 8 位；本题的字长来自表示要求，而不是 Python 整数的实际存储大小。

继续阅读：[第1章：原码、反码、补码](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-4 | 4-4 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

-78的原码是 _____ ，反码是 _____ ，补码是 _____ 。 （用八位表示）

::: answer

`11001110`、`10110001`、`10110010`。

:::

::: explanation

78 的 7 位数值部分为 1001110；原码符号位置 1，反码保留符号位并翻转其余位，补码再加 1。

<!-- teaching-notes:start -->

**从本题理解：固定字长下的原码、反码、补码**

先确定题目规定的字长，再写二进制位。8 位有符号表示中，正数的原码、反码和补码相同，最高位为 0；负数的原码将最高位置 1，反码保留符号位并翻转其余位，补码在反码基础上加 1。

以 -78 为例：正数 78 是 `01001110`，负数原码 `11001110`，反码 `10110001`，补码 `10110010`。也可用 $2^8-78=178$ 验证其补码位型。8 位补码范围为 -128～127，不能把任意大整数强行塞进 8 位。Python 的 `int` 不固定为 8 位；本题的字长来自表示要求，而不是 Python 整数的实际存储大小。

继续阅读：[第1章：原码、反码、补码](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="programming" class="quiz-group">编程题<span>04 QUESTIONS</span></h2>

:::: question programming-1 | 7-1 从键盘输入两个数，求它们的和并输出

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
a = int(input())
b = int(input())
print(a + b)
```

:::

::: explanation

分别读取两行整数，再输出它们的和，不附加提示语。

<!-- teaching-notes:start -->

**解题步骤与边界**

两次 `input()` 对应两行输入，而不是同一行里的两个数。每次先用 `int()` 转换，再做加法；若直接相加两次读取的字符串，输入 12 和 3 会得到 123 而不是 15。最后一次 `print()` 只输出结果，不能附带说明。

**从本题理解：输入处理的四个步骤**

多项数值输入可按“读整行 → 拆文本 → 逐项转换 → 拆包赋值”理解。输入 `3 5` 时，`input()` 返回 `'3 5'`，`split()` 得到 `['3','5']`，`map(int,...)` 按需将每一项转成整数，最后两个变量分别接收 3 和 5。

```python
line = input()
parts = line.split()
m, n = map(int, parts)
```

`int(parts)` 不会逐项处理，而会因参数是列表而报错。输入 `3,5` 应使用 `split(',')`。拆出的项目数和变量数不匹配会产生 `ValueError`；数字格式非法也会在转换时产生 `ValueError`。处理整行字符串时不要随意 `split()`，否则原有空格结构会丢失。

继续阅读：[第1章：输入及输出函数](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-2 | 7-2 从键盘输入三个数到a,b,c中，按公式值输出

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
a, b, c = map(int, input().split())
print(b * b - 4 * a * c)
```

:::

::: explanation

同一行拆分三个整数，按乘法优先级计算公式。若输入允许小数，可将 int 改为 float；原题样例采用整数。

<!-- teaching-notes:start -->

**解题步骤与边界**

先把同一行的三个系数依次拆给 a、b、c，再计算判别式。`b*b` 是平方，`4*a*c` 的乘号不能省略。这里只计算判别式，不需要继续开平方或求方程根；判别式为负也是合法结果，不能自行改成 0。

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-3 | 7-3 输出“人生苦短，我学Python”

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
print('人生苦短，我学Python')
```

:::

::: explanation

题目无输入，按原文输出，注意中文逗号及 Python 的大小写。这句话属于题面要求。

<!-- teaching-notes:start -->

**解题步骤与边界**

这道题没有输入，所以不应写 `input()` 等待数据。字符串定界用的引号不会被打印；引号内部的中文逗号、英文字母大小写和文字内容则都是输出的一部分。`print()` 会在行末自动加一个换行。

**从本题理解：输出内容由哪些部分组成**

`print(a,b)` 不是把两个变量原样紧贴输出，而是先将参数转成文本，再用 `sep` 连接，最后加上 `end`。默认 `sep=' '`、`end='\n'`，所以参数间有一个空格，输出后换行。`print(a,b,sep='')` 才是无分隔拼接。

```python
print(5, 9)             # 5 9
print(5, 9, sep='-')    # 5-9
print('*', end=' ')     # 星号后有一个空格，暂不换行
```

判断题和编程题都要检查前导空格、参数间空格、行尾空格与换行。不要给自动评测的输出加入“请输入”等提示语。观察不可见字符时可先构造字符串，再使用 `repr()` 查看其边界；直接看网页中排版后的文字不一定能分辨空格数量。

继续阅读：[第1章：print 与输出格式](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-4 | 7-4 写字母H

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
print('*   *\n*   *\n*****\n*   *\n*   *')
```

:::

::: explanation

使用换行符分隔五行；第一、二、四、五行的星号之间有三个空格。

<!-- teaching-notes:start -->

**解题步骤与边界**

把图形按行拆成五个字符串。前两行与后两行都是星号、三个空格、星号，中间一行是五个连续星号。`\n` 分隔行而不产生额外空行；不要用制表符代替三个空格，因为显示宽度与实际字符都不同。

**从本题理解：把图形拆成行号和行内规律**

先确定第 i 行由哪几段组成，再决定循环。星号三角形常见规律是第 i 行有 i 个星号；等腰数字图形则可以拆成左侧空格、递增段和递减段。最高值只出现一次，所以递减段从 i-1 开始，而不是再次从 i 开始。

假设所有数字都占一个字符，峰值为 i 的回文数字行宽为 `2*i-1`，最终行峰值为 n，则左侧空格数是 n-i。若数字可能达到两位，必须重新核对题目限制和实际字符宽度，不能继续套单字符公式。输出前用小输入手算每行的前导空格、分隔符、行尾空格和换行；不要用网页里看起来相近的形状替代精确字符比较。

继续阅读：[第4章：for 循环](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::
