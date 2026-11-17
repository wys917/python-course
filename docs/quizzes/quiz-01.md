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

<div class="editor-note">

题目整理自所提供的 PTA 网页，参考答案按 Python 3 核对，未在 PTA 平台提交验证。原题编号重复时保留原编号，以页面题序区分。

</div>

<h2 id="judgment" class="quiz-group">判断题<span>14 QUESTIONS</span></h2>

:::: question judgment-1 | 1-7 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

在Python中，可以用else作为变量名。

::: answer

F（错误）。

:::

::: explanation

else 是关键字，不能用作变量名。

<!-- teaching-notes:start -->

**从本题理解：标识符、关键字与内置名称**

入门题中常见的合法名字由字母、数字和下划线组成，不能以数字开头，且区分大小写。`item_1` 与 `_item` 合法；`1item` 不合法；`item-name` 会被当成减法表达式，而不是一个名字。Python 也允许部分 Unicode 字符用于标识符。

还要区分关键字和内置名称：`else`、`for` 是语法保留字，不能作普通变量名；`print`、`list` 不是关键字，给它们赋值在语法上合法，却会遮蔽原有功能。例如 `print=3` 后再执行 `print(5)`，是在调用整数，因而报 `TypeError`。布尔常量必须写作 `True`、`False`，大小写变化后会被当成别的名字。

继续阅读：[第1章：标识符和变量](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-2 | 1-9 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

字母A的ASCII编码值和Unicode编码值相同。

::: answer

T（正确）。

:::

::: explanation

A 的 ASCII 编码和 Unicode 码点都是 65。

<!-- teaching-notes:start -->

**从本题理解：字符、码点与字节编码**

Unicode 为字符分配码点，例如 `ord('A')` 为 65，`ord('张')` 为 24352；`chr()` 完成反向转换。`U+5F20` 和十进制 24352 表示同一码点，只是记数方式不同。`ord()` 接收单个字符，不能直接把整个多字符字符串转换成一个码点。

UTF-8 则规定如何把码点编码成字节，不能把它和 Unicode 字符集合混为一谈。例如 `len('张')` 为 1，而 `len('张'.encode('utf-8'))` 为 3；前者数 Python 字符串中的码点，后者数字节。ASCII 字符在 UTF-8 中仍占一个字节，这也是英文字符 A 的编码值在本题中保持 65 的原因。

继续阅读：[第1章：字符编码](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-3 | 1-3 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序的运行结果是4。

```python
    i=3         
    ++i
```

::: answer

F（错误）。

:::

::: explanation

++i 不是自增，只是两次一元正号，i 保持 3；脚本也不会自动输出表达式。

<!-- teaching-notes:start -->

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-4 | 1-4 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

当输入是`10.0`时，下面程序的输出是`f(10.0) = 0.1`。

```python
x=int(input())
if x==0:
    result=0
else:
    result=1/x
print('f({0:.1f}) = {1:.1f}'.format(x,result))
```

::: answer

F（错误）。

:::

::: explanation

int('10.0') 引发 ValueError，应使用 float() 读取小数。

<!-- teaching-notes:start -->

**从本题理解：文本形式与数值类型转换**

`input()` 的结果永远先是字符串。`int('10')` 解析整数文本，`float('10.0')` 解析浮点文本，`str(10)` 则生成数值的字符串形式。`int('10.0')` 不会先自动转成浮点数，因此报 `ValueError`；`int(10.9)` 则接收数值并向零截断，得到 10。

```python
a = 3
print('a' * 2)         # aa：引号里是字母，不是变量
print(str(a) * 2)      # 33：先取变量值，再转字符串
print(int('11', 2))    # 3：以二进制解析
```

要分清错误种类：传入不支持的对象类型通常是 `TypeError`，支持的类型中内容不合法通常是 `ValueError`。也不要用 `int(float(文本))` 盲目修补输入，它会丢掉小数部分；题意要求保留小数时应直接使用 `float()`。

继续阅读：[第2章：内置转换函数](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-5 | 1-5 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序的输出是：这是字符串输出格式□□123。 □表示空格。

`print("这是字符串输出格式{:5s}".format("123"))`

::: answer

F（错误）。

:::

::: explanation

字符串默认左对齐，两个补齐空格应位于 123 右侧。

<!-- teaching-notes:start -->

**从本题理解：格式规格由填充、对齐、宽度和类型组成**

常见结构为 `[[填充字符]对齐方式][宽度][.精度][类型]`。`<` 左对齐、`>` 右对齐、`^` 居中；字符串默认左对齐，数值默认右对齐。宽度是最小宽度，不会截断过长内容。`d` 用于十进制整数，`s` 用于字符串，`.2f` 表示小数点后保留两位。

```python
print(f'|{"this":8s}|') # |this    |
print(f'|{1234:8d}|')   # |    1234|
print(f'{31:08b}')      # 00011111
print(f'{"11":0>5s}')  # 00011
```

先算内容本身长度，再用字段宽度减去它，才知道补几个字符。动态宽度应显式写成 `f'{s:^{width}}'`，格式串里的普通字母不会自动读取同名变量。浮点格式化的宽度还包含符号和小数点，精度不等于总字符数。

继续阅读：[第2章：格式化输出](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-6 | 1-6 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面语句的输出是：这是数字输出格式$\Box$$\Box$123。 $\Box$表示空格  
`print("这是数字输出格式{:5d}".format(123))`

::: answer

T（正确）。

:::

::: explanation

整数默认右对齐，宽度 5 时在 123 左边补两个空格。

<!-- teaching-notes:start -->

**从本题理解：格式规格由填充、对齐、宽度和类型组成**

常见结构为 `[[填充字符]对齐方式][宽度][.精度][类型]`。`<` 左对齐、`>` 右对齐、`^` 居中；字符串默认左对齐，数值默认右对齐。宽度是最小宽度，不会截断过长内容。`d` 用于十进制整数，`s` 用于字符串，`.2f` 表示小数点后保留两位。

```python
print(f'|{"this":8s}|') # |this    |
print(f'|{1234:8d}|')   # |    1234|
print(f'{31:08b}')      # 00011111
print(f'{"11":0>5s}')  # 00011
```

先算内容本身长度，再用字段宽度减去它，才知道补几个字符。动态宽度应显式写成 `f'{s:^{width}}'`，格式串里的普通字母不会自动读取同名变量。浮点格式化的宽度还包含符号和小数点，精度不等于总字符数。

继续阅读：[第2章：格式化输出](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-7 | 1-7 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

`bool(None)`的返回值是False。

::: answer

T（正确）。

:::

::: explanation

None 的布尔值为 False。

<!-- teaching-notes:start -->

**从本题理解：布尔对象与“真假性”**

`True` 和 `False` 是布尔常量，转换成整数分别为 1 和 0。条件判断却不要求表达式本身一定是布尔对象：数值 0、`None`、空字符串及空容器是假值，大多数其他对象是真值。例如 `bool([])` 为假，而 `bool([0])` 为真，因为后者并不为空。

要区分 `False` 与字符串 `'False'`：后者有 5 个字符，是真值。同样，`0 == False` 为真不意味着它们类型相同，`type(0)` 为 `int`，`type(False)` 为 `bool`。未定义的名字 `FALSE` 会先触发 `NameError`，程序根本还没进入真假转换阶段。`None` 的判断通常写 `x is None`，用于区分“没有值”和合法的数值 0。

继续阅读：[第2章：布尔类型与空值](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-8 | 1-8 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

`print(bin(12.5))`的输出是`0b1100.1`

::: answer

F（错误）。

:::

::: explanation

bin() 不接受浮点数 12.5，会产生 TypeError。

<!-- teaching-notes:start -->

**从本题理解：文本形式与数值类型转换**

`input()` 的结果永远先是字符串。`int('10')` 解析整数文本，`float('10.0')` 解析浮点文本，`str(10)` 则生成数值的字符串形式。`int('10.0')` 不会先自动转成浮点数，因此报 `ValueError`；`int(10.9)` 则接收数值并向零截断，得到 10。

```python
a = 3
print('a' * 2)         # aa：引号里是字母，不是变量
print(str(a) * 2)      # 33：先取变量值，再转字符串
print(int('11', 2))    # 3：以二进制解析
```

要分清错误种类：传入不支持的对象类型通常是 `TypeError`，支持的类型中内容不合法通常是 `ValueError`。也不要用 `int(float(文本))` 盲目修补输入，它会丢掉小数部分；题意要求保留小数时应直接使用 `float()`。

继续阅读：[第2章：内置转换函数](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-9 | 1-9 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

int("92",8)的值是74。

::: answer

F（错误）。

:::

::: explanation

八进制没有数码 9，int('92',8) 会产生 ValueError。

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

:::: question judgment-10 | 1-10 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式`3 and 0 and "hello"`的值是False。

::: answer

F（错误）。

:::

::: explanation

结果是整数 0，and 返回操作数，不是布尔对象 False。

<!-- teaching-notes:start -->

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-11 | 1-11 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

z已赋值，x=(y=z+1)语句是错误语句

::: answer

T（正确）。

:::

::: explanation

赋值语句不能放在这种表达式位置，应写 x=y=z+1。

<!-- teaching-notes:start -->

**从本题理解：赋值、表达式与拆包顺序**

普通 `=` 是赋值语句，不是比较运算 `==`，不能直接嵌入 `x=(y=z+1)+1` 这种表达式。若两个名字都要接收同一个结果，可写 `x=y=z+1`。`i*=3+5` 要先求出整个右侧，数值情形下相当于 `i=i*(3+5)`，不是 `i=i*3+5`。

拆包赋值先求整个右侧，再从左到右赋给各目标。若旧 `t=1`，`t,a=2,t+1` 先得到右侧 `(2,2)`，所以 `a=2`；交换 `a,b=b,a` 也利用此规则。右侧必须可迭代且元素数量匹配：整数 34 不能直接拆成 3 和 4，字符串 `'3 4'` 则有 3 个字符，而不是两个数。

继续阅读：[第2章：赋值与拆包](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-12 | 1-12 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

print(("12 "*3).strip()==" ".join(["12","12","12"]))的输出结果是True

::: answer

T（正确）。

:::

::: explanation

strip() 去掉重复字符串末尾的空格后，两侧都得到 12 12 12。

<!-- teaching-notes:start -->

**从本题理解：连接字符串与空格精确比较**

`分隔符.join(各字符串)` 只在相邻项之间放分隔符，不会自动在首尾添加。例如 `' '.join(['12','12','12'])` 为 `'12 12 12'`，而 `'12 '*3` 为 `'12 12 12 '`，末尾多一个空格，比较结果为假。

```python
parts = ['12', '12', '12']
s = ' '.join(parts)
print(repr(s))         # '12 12 12'
print(len(s))          # 8
```

`join()` 的元素必须是字符串，数值列表先用 `map(str,values)` 转换。`strip()` 能改变两端空白，但不能为了解决输出问题随意使用：若空格属于题目要求，去掉它就是改变答案。比较字符串时，先写出每一段内容和长度，再叠加 `print()` 自带的 `sep`，能更准确地定位多余空格。

继续阅读：[第3章：字符串和列表的互转](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-13 | 1-13 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面的程序当输入是 `c d e a`时，输出是 `a c d e`。

```python
a = input().split(" ")
a.sort()
for i in a:    
    print(i,end=" ")
```

::: answer

T（正确）。

:::

::: explanation

先原地排序，再遍历列表，顺序为 a、c、d、e；print(end=" ") 还会在最后保留一个空格。

<!-- teaching-notes:start -->

**从本题理解：排序的对象、顺序与返回值**

`sorted(items)` 返回新的已排序列表，原对象不变；`a.sort()` 原地修改列表并返回 `None`。要降序使用 `reverse=True`。`max()` 只取最大元素，不返回排序后的完整序列，空序列且无默认值时还会报错。

排序前先确定按什么比较：整数 `[2,10]` 排成 `[2,10]`，字符串 `['2','10']` 则排成 `['10','2']`。若题意是按数值大小，必须先转成数值再排序，最后再转回字符串用于输出。`random.shuffle(a)` 也原地修改列表并返回 `None`，但它是打乱，不是排序；不要写 `a=random.shuffle(a)`。

继续阅读：[第3章：列表方法](../topics/chapter-03.md)与[第4章：搜索和排序](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-14 | 1-14 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

[4,5]`*`3的结果是[4,5],[4,5],[4,5]。

::: answer

F（错误）。

:::

::: explanation

[4,5]*3 得到单个列表 [4,5,4,5,4,5]，不会生成三个子列表或元组。

<!-- teaching-notes:start -->

**从本题理解：序列重复与内部引用共享**

字符串或列表乘整数表示重复，不是把内容解释成数值。`'23'*3` 为 `'232323'`，`[4,5]*3` 为 `[4,5,4,5,4,5]`，不会自动生成三个子列表。字符串原有的空格也会一起重复，所以 `'12 '*3` 在最后仍有一个空格。

若元素本身是可变列表，重复操作复制的是引用：`rows=[[0]*2]*3` 中三行是同一个对象，执行 `rows[0][0]=1` 会让三行都改变。要创建独立的行，应写 `rows=[[0]*2 for _ in range(3)]`。同样，列表 `+` 只连接一层，`[1,2]+[[3]]` 得到 `[1,2,[3]]`，不会递归展开内部列表。

继续阅读：[第3章：序列运算与嵌套引用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="choice" class="quiz-group">单选题<span>13 QUESTIONS</span></h2>

:::: question choice-1 | 2-2 单选题

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

Python 脚本文件通常以 .py 结尾。

<!-- teaching-notes:start -->

**从本题理解：源代码怎样运行**

“高级语言”描述的是语言抽象层次，“编译”和“解释”描述的是实现程序的执行方式，不能把两者一一对应。编译器可以先把程序翻译成另一种形式，解释器则负责执行相应指令；同一种语言也可以有不同实现。

以常用的 CPython 为例，源代码先编译成字节码，再由解释器执行，因此把 Python 理解成“完全不经过编译”也不准确。`.py` 是源文件扩展名，不是运行结果；终端执行 `python 文件名.py` 时，真正运行程序的是所选 Python 解释器。交互环境会显示裸表达式的值，脚本通常需要 `print()` 才会输出。

继续阅读：[第1章：Python 与运行环境](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-2 | 2-8 单选题

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

半角 # 引出同行注释。

<!-- teaching-notes:start -->

**从本题理解：注释与字符串的边界**

英文半角 `#` 在字符串外引出单行注释，从它开始到本行末尾不再作为代码执行。例如 `x=3 # 说明` 中，赋值仍然会执行。全角 `＃` 不是 Python 注释符号。

字符串内部的 `#` 属于普通字符：`print('#')` 会输出井号。判断一段代码时，先确认引号边界，再识别注释，不能看到 `#` 就认为后面全部无效。三引号首先定义的是多行字符串；它在模块、类或函数开头时可以作为文档字符串，不能简单地把所有三引号字符串都称为注释。

继续阅读：[第1章：注释](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-3 | 2-9 单选题

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

_item 合法，不能以数字开头或含连字符、星号。

<!-- teaching-notes:start -->

**从本题理解：标识符、关键字与内置名称**

入门题中常见的合法名字由字母、数字和下划线组成，不能以数字开头，且区分大小写。`item_1` 与 `_item` 合法；`1item` 不合法；`item-name` 会被当成减法表达式，而不是一个名字。Python 也允许部分 Unicode 字符用于标识符。

还要区分关键字和内置名称：`else`、`for` 是语法保留字，不能作普通变量名；`print`、`list` 不是关键字，给它们赋值在语法上合法，却会遮蔽原有功能。例如 `print=3` 后再执行 `print(5)`，是在调用整数，因而报 `TypeError`。布尔常量必须写作 `True`、`False`，大小写变化后会被当成别的名字。

继续阅读：[第1章：标识符和变量](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-4 | 2-11 单选题

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

C 属于过程式语言，其他选项提供类等面向对象机制。

<!-- teaching-notes:start -->

**从本题理解：程序设计语言的分类**

过程式编程围绕“按什么步骤完成任务”组织函数和语句；面向对象编程把状态与相关操作组织到对象中。它们是组织程序的思路，不是语言只能二选一的标签。

例如计算一组成绩的平均分，可以用函数接收列表并返回结果；管理学生姓名、成绩及相关操作时，也可以设计 `Student` 类。Python 支持过程式、面向对象等多种方式。题目按课程常见分类选择答案时，需要理解分类依据；不能据此推断 Python 程序必须使用类，或 C 语言不能实现复杂的数据抽象。

继续阅读：[第8章：类和对象](../topics/chapter-08.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-5 | 2-1 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

下列数据类型中， Python不支持的是_____________。

**A.** char

**B.** int

**C.** float

**D.** list

::: answer

A。

:::

::: explanation

Python 没有独立的 char 内置类型。

<!-- teaching-notes:start -->

**从本题理解：字符串是不可变的字符序列**

Python 没有单独的内置 `char` 类型，`'A'` 是长度为 1 的 `str`。字符串支持索引、切片、遍历、成员判断与长度查询，但不支持 `s[0]='B'` 这样的原地修改。要更改字符，可构造新字符串并重新赋值，例如 `s='B'+s[1:]`。

字符串的长度由对象记录，不依赖 `\0` 作为结束标志；`len('a\0b')` 为 3，中间的空字符也计入长度。`list('abc')` 会遍历字符串，生成 `['a','b','c']`；`['abc']` 则只含一个完整字符串。这个区别也适用于拆包和 `extend()`：传入字符串时，它通常被当成可逐字符遍历的序列。

继续阅读：[第3章：序列与字符串](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-6 | 2-6 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 print(0xA + 0xB)的输出结果是______________。

**A.** 0xA + 0xB

**B.** A + B

**C.** 0xA0xB

**D.** 21

::: answer

D。

:::

::: explanation

0xA=10，0xB=11，相加为 21。

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

:::: question choice-7 | 2-7 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句x=’car’; y = 2; print (x+y)的输出结果是____________。

**A.** 语法错

**B.** 2

**C.** 'car2’

**D.** 'carcar’

::: answer

无严格正确选项；按普通引号还原后为运行时 `TypeError`。

:::

::: explanation

题面使用弯引号，原样作为 Python 代码会产生 SyntaxError；若按普通字符串引号理解，字符串 car 与整数 2 相加会产生 TypeError，不能称为语法错误。A 仅在原样弯引号情形下适用。

<!-- teaching-notes:start -->

**从本题理解：同一个运算符对不同类型有不同含义**

对数字，`+` 表示加法；对字符串，表示拼接；对列表，表示连接两边的元素。例如 `2+3` 为 5，`'2'+'3'` 为 `'23'`，`[2]+[3]` 为 `[2,3]`。Python 不会为了完成拼接自动把整数变成字符串，所以 `'age'+23` 在运行时产生 `TypeError`。

若要拼接，使用 `'age'+str(23)` 或 `f'age{23}'`；若要计算，使用 `int('23')+1`。二者目的不同，不能随意选择一种转换。还要把语法阶段和执行阶段分开：正常引号下的字符串加整数，能通过语法解析；弯引号 `“ ”` 不是 Python 字符串定界符，原样输入会先出现语法错误。

继续阅读：[第2章：字符串与类型转换](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-8 | 2-8 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

如math模块已引入，Python 表达式 `math.sqrt(4)*math.sqrt(9)`的值为________。

**A.** 36.0

**B.** 6

**C.** 13

**D.** 6.0

::: answer

D。

:::

::: explanation

两个平方根结果分别为浮点数 2.0 和 3.0，乘积为 6.0。

<!-- teaching-notes:start -->

**从本题理解：数学公式如何翻译成 Python**

先识别公式的运算结构，再选择函数。平方根用 `math.sqrt()`，自然对数用 `math.log()`，指数 $e^x$ 用 `math.exp()`；乘法必须明确写 `*`，分式的分子、分母需要分别加括号。`sqrt(4)` 返回 `2.0`，所以后续乘积可能是浮点数而不是整数。

三角函数参数以弧度为单位，角度先用 `math.radians()` 转换。还要检查定义域：实数平方根的参数不能为负，自然对数参数必须大于 0，分母不能为 0。输出格式化只控制最后显示多少位，并不修复公式、定义域或中间计算的错误。`ceil()` 向上取整，`floor()` 向下取整，均与向零截断的 `int()` 有区别。

继续阅读：[第2章：math 库](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-9 | 2-10 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

关于Python中的复数，下列说法错误的是___________。

**A.** 表示复数的语法是real + imag j

**B.** 实部和虚部都是浮点数

**C.** 虚部必须后缀j, 且必须是小写

**D.** 方法conjugate 返回复数的共轭复数

::: answer

C。

:::

::: explanation

复数虚部后缀可以为 j 或 J，如 1J 合法。实部、虚部属性为浮点数，调用 conjugate() 得到共轭复数。选项 A 是概念示意，实际代码不能在数字与 j 之间插入空格。

<!-- teaching-notes:start -->

**从本题理解：复数的表示、属性与模**

Python 使用 `j` 或 `J` 表示虚数单位，例如 `1J`、`3+4j` 都是复数。实部和虚部分别由 `.real`、`.imag` 读取，返回浮点数；`.conjugate()` 返回共轭复数。必须调用方法才能得到结果，不能把 `.conjugate` 方法对象当成计算后的值。

```python
z = 3 + 4j
print(z.real, z.imag)  # 3.0 4.0
print(z.conjugate())   # (3-4j)
print(abs(z))          # 5.0
```

复数的绝对值是模，按 $\sqrt{a^2+b^2}$ 计算，不是分别把实部虚部取绝对值。复数不能用 `<`、`>` 排大小；普通数值比较的结果才是布尔值。复数字面量中数字和 `j` 要连写，概念公式 `a+bj` 也不能直接替代变量运算 `complex(a,b)`。

继续阅读：[第2章：数字类型](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-10 | 2-10 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 print(chr(65))的运行结果是___________。

**A.** 65

**B.** 6

**C.** 5

**D.** A

::: answer

D。

:::

::: explanation

码点 65 对应字符 A。

<!-- teaching-notes:start -->

**从本题理解：字符、码点与字节编码**

Unicode 为字符分配码点，例如 `ord('A')` 为 65，`ord('张')` 为 24352；`chr()` 完成反向转换。`U+5F20` 和十进制 24352 表示同一码点，只是记数方式不同。`ord()` 接收单个字符，不能直接把整个多字符字符串转换成一个码点。

UTF-8 则规定如何把码点编码成字节，不能把它和 Unicode 字符集合混为一谈。例如 `len('张')` 为 1，而 `len('张'.encode('utf-8'))` 为 3；前者数 Python 字符串中的码点，后者数字节。ASCII 字符在 UTF-8 中仍占一个字节，这也是英文字符 A 的编码值在本题中保持 65 的原因。

继续阅读：[第1章：字符编码](../topics/chapter-01.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-11 | 2-12 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

关于Python字符串，下列说法错误的是___________。

**A.** 字符即长度为1的字符串

**B.** 字符串以\0标志字符串的结束

**C.** 既可以用单引号，也可以用双引号创建字符串

**D.** 在三引号字符串中可以包含换行回车等特殊字符

::: answer

B。

:::

::: explanation

Python 字符串不使用 \0 标记结束。

<!-- teaching-notes:start -->

**从本题理解：字符串是不可变的字符序列**

Python 没有单独的内置 `char` 类型，`'A'` 是长度为 1 的 `str`。字符串支持索引、切片、遍历、成员判断与长度查询，但不支持 `s[0]='B'` 这样的原地修改。要更改字符，可构造新字符串并重新赋值，例如 `s='B'+s[1:]`。

字符串的长度由对象记录，不依赖 `\0` 作为结束标志；`len('a\0b')` 为 3，中间的空字符也计入长度。`list('abc')` 会遍历字符串，生成 `['a','b','c']`；`['abc']` 则只含一个完整字符串。这个区别也适用于拆包和 `extend()`：传入字符串时，它通常被当成可逐字符遍历的序列。

继续阅读：[第3章：序列与字符串](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-12 | 2-12 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

C（3 个）。

:::

::: explanation

a 错：i*=3+5 等价于 i=i*(3+5)；b 错：科学计数法指数不能写成 2.0；c 对：int("3.5",10) 确实运行时报错；d 错：整数默认右对齐，字符串默认左对齐。

<!-- teaching-notes:start -->

**从本题理解：赋值、表达式与拆包顺序**

普通 `=` 是赋值语句，不是比较运算 `==`，不能直接嵌入 `x=(y=z+1)+1` 这种表达式。若两个名字都要接收同一个结果，可写 `x=y=z+1`。`i*=3+5` 要先求出整个右侧，数值情形下相当于 `i=i*(3+5)`，不是 `i=i*3+5`。

拆包赋值先求整个右侧，再从左到右赋给各目标。若旧 `t=1`，`t,a=2,t+1` 先得到右侧 `(2,2)`，所以 `a=2`；交换 `a,b=b,a` 也利用此规则。右侧必须可迭代且元素数量匹配：整数 34 不能直接拆成 3 和 4，字符串 `'3 4'` 则有 3 个字符，而不是两个数。

继续阅读：[第2章：赋值与拆包](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-13 | 2-13 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

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

**B.** Fasle [1, 2, 3] False [1, 5, 3]

**C.** True [1, 5, 3] True [1, 7, 3]

**D.** False [1, 2, 3] True [1, 5, 3]

::: answer

A。

:::

::: explanation

b 和 a 指向同一列表，修改 a 后 b 同步变化；d=a[:] 是外层副本，后续 a[1]=7 不改变 d。

<!-- teaching-notes:start -->

**从本题理解：赋值、浅拷贝和深拷贝**

`b=a` 只复制引用，两个名字指向同一个列表；`b=a[:]`、`b=a.copy()` 新建外层列表，但其中的元素仍指向原对象。浅拷贝后，给一个位置重新赋值通常只影响所在的外层列表，修改共享的内部列表则会被两边看到。

```python
a = [[1], 2]
b = a.copy()
b[0].append(3)
print(a)          # [[1, 3], 2]：内部列表共享
b[1] = 9
print(a[1])       # 2：外层位置独立
```

需要递归复制内部可变对象时可使用 `copy.deepcopy()`。`==` 比较内容，`is` 比较身份，因此浅拷贝后可以同时满足 `a == b` 和 `a is not b`。判断一道题是否会“跟着改变”，关键是找到真正被修改的对象，而不是只看变量名是否不同。

继续阅读：[第3章：赋值、浅拷贝与嵌套引用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="blank" class="quiz-group">填空题<span>09 QUESTIONS</span></h2>

:::: question blank-1 | 4-2 填空题

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

:::: question blank-2 | 4-3 填空题

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

:::: question blank-3 | 4-4 填空题

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

:::: question blank-4 | 4-4 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 表达式 0 and 1 or not 2&lt;True 的值为 _____ 。

::: answer

`True`。

:::

::: explanation

先计算 2<True，即 2<1，为假；not 后为真。0 and 1 得到 0，再与 True 做 or 得到 True。

<!-- teaching-notes:start -->

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-5 | 4-8 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 print(abs(-10.2), round(abs(8-2j),3)) 的输出结果是 _____ 。

::: answer

`10.2 8.246`。

:::

::: explanation

abs(-10.2)=10.2；复数的模为 sqrt(8²+(-2)²)=sqrt(68)，保留 3 位小数为 8.246。

<!-- teaching-notes:start -->

**从本题理解：复数的表示、属性与模**

Python 使用 `j` 或 `J` 表示虚数单位，例如 `1J`、`3+4j` 都是复数。实部和虚部分别由 `.real`、`.imag` 读取，返回浮点数；`.conjugate()` 返回共轭复数。必须调用方法才能得到结果，不能把 `.conjugate` 方法对象当成计算后的值。

```python
z = 3 + 4j
print(z.real, z.imag)  # 3.0 4.0
print(z.conjugate())   # (3-4j)
print(abs(z))          # 5.0
```

复数的绝对值是模，按 $\sqrt{a^2+b^2}$ 计算，不是分别把实部虚部取绝对值。复数不能用 `<`、`>` 排大小；普通数值比较的结果才是布尔值。复数字面量中数字和 `j` 要连写，概念公式 `a+bj` 也不能直接替代变量运算 `complex(a,b)`。

继续阅读：[第2章：数字类型](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-6 | 4-14 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式 3 and 0 and 5的结果是什么？。 _____

::: answer

`0`。

:::

::: explanation

and 短路并返回遇到的假值 0，不继续检查 5。

<!-- teaching-notes:start -->

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-7 | 4-16 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式 ---3 的结果是什么？ _____ 。

::: answer

`-3`。

:::

::: explanation

三次一元负号，最终为负。

<!-- teaching-notes:start -->

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-8 | 4-17 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式`32.2//6-24//6`的值是 _____ 。

::: answer

`1.0`。

:::

::: explanation

32.2//6 为 5.0，24//6 为 4，差为浮点数 1.0。

<!-- teaching-notes:start -->

**从本题理解：运算符决定值，也影响结果类型**

`int` 表示整数，`float` 表示浮点数，`complex` 表示复数，`bool` 是整数类型的子类。整数与浮点数进行常见算术运算时，结果通常转为浮点数；`/` 即使两侧都是整数，也执行普通除法，例如 `1/2` 为 `0.5`、`4/2` 为 `2.0`。

`//` 向负无穷取整，不是简单删除小数：`-3//2` 为 -2，而 `int(-3/2)` 为 -1。对于正除数，余数满足 `a == (a//b)*b + a%b`。`32.2//6` 的值虽然是整数大小的 5，但类型仍为 `float`，打印成 `5.0`；判断输出时必须同时跟踪数值与类型。

继续阅读：[第2章：数字类型](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-9 | 4-9 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

`ABCD`。

:::

::: explanation

每个字符先判断大写并转小写，再独立判断小写并转大写；原本大写会连续转换两次，原本小写转换一次，最终全部大写。两个 if 不是 if-elif。

<!-- teaching-notes:start -->

**从本题理解：两个 if 与 if-elif 的执行差别**

连续的两个 `if` 会分别判断，前一个分支修改变量后，后一个条件看到的是新值。`if-elif-else` 则只选择第一个满足条件的分支，选中后不再判断后续分支。因此先把大写改小写、再独立判断是否小写并改大写，会把原本大写的字符转换两次。

```python
c = 'A'
if c.isupper():
    c = c.lower()
if c.islower():
    c = c.upper()
print(c)  # A
```

若目的是互换大小写，应让两个分支互斥，或直接用 `swapcase()`。分段函数、计费与输入校验也需要先决定分支是否互斥，并明确边界上的等号归哪一段，避免同一个输入被重复处理或遗漏。

继续阅读：[第4章：条件语句](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="programming" class="quiz-group">编程题<span>06 QUESTIONS</span></h2>

:::: question programming-1 | 7-1 计算分段函数

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
x = float(input())
result = 0 if x == 0 else 1 / (2 * x)
print(f'g({x:.3f}) = {result:.3f}')
```

:::

::: explanation

x=0 时单独处理，避免除零；其他情况计算 1/(2x)，两个数都保留三位小数。

<!-- teaching-notes:start -->

**解题步骤与边界**

分段点为 x=0：该点返回 0，其他输入才计算 `1/(2*x)`。条件表达式仅求所选分支，因而能避免除零。输入值和计算值分别保留三位小数；不要先舍入输入再判断它是否等于 0。

**从本题理解：两个 if 与 if-elif 的执行差别**

连续的两个 `if` 会分别判断，前一个分支修改变量后，后一个条件看到的是新值。`if-elif-else` 则只选择第一个满足条件的分支，选中后不再判断后续分支。因此先把大写改小写、再独立判断是否小写并改大写，会把原本大写的字符转换两次。

```python
c = 'A'
if c.isupper():
    c = c.lower()
if c.islower():
    c = c.upper()
print(c)  # A
```

若目的是互换大小写，应让两个分支互斥，或直接用 `swapcase()`。分段函数、计费与输入校验也需要先决定分支是否互斥，并明确边界上的等号归哪一段，避免同一个输入被重复处理或遗漏。

继续阅读：[第4章：条件语句](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-2 | 7-5 三个数的大小比较

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
values = sorted(map(int, input().split()), reverse=True)
print('>'.join(map(str, values)))
```

:::

::: explanation

按数值降序排序，再转字符串以 > 连接；不能先按字符串排序。

<!-- teaching-notes:start -->

**解题步骤与边界**

先把输入转成整数，再按 `reverse=True` 降序排序。排序完成后用 `map(str,values)` 转回文本，以 `>` 连接，因此符号只在相邻两项之间出现。用 2、10、3 检查可以发现按字符串排序与按整数排序的区别。

**从本题理解：排序的对象、顺序与返回值**

`sorted(items)` 返回新的已排序列表，原对象不变；`a.sort()` 原地修改列表并返回 `None`。要降序使用 `reverse=True`。`max()` 只取最大元素，不返回排序后的完整序列，空序列且无默认值时还会报错。

排序前先确定按什么比较：整数 `[2,10]` 排成 `[2,10]`，字符串 `['2','10']` 则排成 `['10','2']`。若题意是按数值大小，必须先转成数值再排序，最后再转回字符串用于输出。`random.shuffle(a)` 也原地修改列表并返回 `None`，但它是打乱，不是排序；不要写 `a=random.shuffle(a)`。

继续阅读：[第3章：列表方法](../topics/chapter-03.md)与[第4章：搜索和排序](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-3 | 7-6 计算在途时间

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
start, end = map(int, input().split())
start_minutes = start // 100 * 60 + start % 100
end_minutes = end // 100 * 60 + end % 100
hours, minutes = divmod(end_minutes - start_minutes, 60)
print(f'在途时间是{hours}小时{minutes}分钟')
```

:::

::: explanation

小时用 //100 提取，分钟用 %100 提取，统一换算为分钟求差，再除以 60。题目保证同日到达，无需跨日处理。

<!-- teaching-notes:start -->

**解题步骤与边界**

HHMM 不是以 100 为进制的时间长度。用 `//100` 取小时、`%100` 取分钟，各自换算成当天累计分钟，再相减。最后用 `divmod(差值,60)` 得到小时和分钟，如 0950 到 1010 是 20 分钟，不能直接用 1010-950 当分钟数。此解按题目同日到达前提处理。

**从本题理解：文本形式与数值类型转换**

`input()` 的结果永远先是字符串。`int('10')` 解析整数文本，`float('10.0')` 解析浮点文本，`str(10)` 则生成数值的字符串形式。`int('10.0')` 不会先自动转成浮点数，因此报 `ValueError`；`int(10.9)` 则接收数值并向零截断，得到 10。

```python
a = 3
print('a' * 2)         # aa：引号里是字母，不是变量
print(str(a) * 2)      # 33：先取变量值，再转字符串
print(int('11', 2))    # 3：以二进制解析
```

要分清错误种类：传入不支持的对象类型通常是 `TypeError`，支持的类型中内容不合法通常是 `ValueError`。也不要用 `int(float(文本))` 盲目修补输入，它会丢掉小数部分；题意要求保留小数时应直接使用 `float()`。

继续阅读：[第2章：内置转换函数](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-4 | 7-11 求平方与倒数序列的近似和

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
from fractions import Fraction
from math import floor
m, n = map(int, input().split())
total = sum((i * i + Fraction(1, i) for i in range(m, n + 1)), Fraction())
print(f'sum ≈ {floor(total)}')
```

:::

::: explanation

每项为 i²+1/i，求和后按题目提示 floor 向下取整。Fraction 保留精确值，避免例如 m=n=1 时的浮点误差。题面“小于”与 floor 在整数处不同，此处采用提示的 floor 定义。

<!-- teaching-notes:start -->

**解题步骤与边界**

第 i 项是 `i*i+1/i`，i 从 m 到 n 且包含两端。先以精确分数求总和，再统一向下取整，不能先把每个分数部分删除。`floor()` 对整数保持原值，与“严格小于”字面定义的差别沿用原题提示并已作说明。

**从本题理解：求和、精确分数与取整时机**

序列求和先把“第 i 项”写清楚，再确定 i 的起止和步长。交错符号常用 `(-1)**(i-1)`，从第 1 项开始为正；分母若为连续奇数，可写 `2*i-1`。取整应按题意在整个和算完之后执行，通常不能把每项先取整再相加。

`floor()` 向负无穷取整，`ceil()` 向正无穷取整，`int()` 向零截断，三者不同。含分数的和若要求准确判断整数边界，可用 `Fraction(1,分母)` 累加，避免浮点误差使最终取整偏差。还要区分“向下取整”和“严格小于原数的最大整数”：当原数本身为整数时，后者比前者少 1，必须根据题目提示说明采用哪种定义。

继续阅读：[第2章：数字类型](../topics/chapter-02.md)与[第4章：循环](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-5 | 7-12 计算函数f(x)

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
import math
x = float(input())
result = math.sin(math.radians(35)) + (math.exp(x) - 15 * x) / math.sqrt(x ** 4 + 1) - math.log(7 * x)
print(f'f({x})={result:.3f}')
```

:::

::: explanation

图中 sin(35°) 需先将角度转弧度；分母为 sqrt(x⁴+1)，ln 用 math.log。x 按 float 输出，函数值保留三位小数。

<!-- teaching-notes:start -->

**解题步骤与边界**

先把公式分为角度正弦、指数分式和自然对数。35 度转成弧度后调用 `sin()`，分母使用完整的 `sqrt(x**4+1)`，对数使用 `log(7*x)`。自然对数要求 x>0。最后只格式化结果，不在中间任意取整，以免放大误差。

**从本题理解：数学公式如何翻译成 Python**

先识别公式的运算结构，再选择函数。平方根用 `math.sqrt()`，自然对数用 `math.log()`，指数 $e^x$ 用 `math.exp()`；乘法必须明确写 `*`，分式的分子、分母需要分别加括号。`sqrt(4)` 返回 `2.0`，所以后续乘积可能是浮点数而不是整数。

三角函数参数以弧度为单位，角度先用 `math.radians()` 转换。还要检查定义域：实数平方根的参数不能为负，自然对数参数必须大于 0，分母不能为 0。输出格式化只控制最后显示多少位，并不修复公式、定义域或中间计算的错误。`ceil()` 向上取整，`floor()` 向下取整，均与向零截断的 `int()` 有区别。

继续阅读：[第2章：math 库](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-6 | 7-14 输出指定图形

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
n = int(input())
for i in range(1, n + 1):
    print('* ' * i)
```

:::

::: explanation

每行有 i 个星号，每个星号后输出一个空格，保留原始网页样例的行尾空格。

<!-- teaching-notes:start -->

**解题步骤与边界**

第 i 行重复 i 次 `* `，包括每个星号后的普通空格，行末空格与原样例一致。循环从 1 到 n，终点用 n+1；`print()` 每轮自动换行，因此不需要在字符串中再加一个换行。

**从本题理解：把图形拆成行号和行内规律**

先确定第 i 行由哪几段组成，再决定循环。星号三角形常见规律是第 i 行有 i 个星号；等腰数字图形则可以拆成左侧空格、递增段和递减段。最高值只出现一次，所以递减段从 i-1 开始，而不是再次从 i 开始。

假设所有数字都占一个字符，峰值为 i 的回文数字行宽为 `2*i-1`，最终行峰值为 n，则左侧空格数是 n-i。若数字可能达到两位，必须重新核对题目限制和实际字符宽度，不能继续套单字符公式。输出前用小输入手算每行的前导空格、分隔符、行尾空格和换行；不要用网页里看起来相近的形状替代精确字符比较。

继续阅读：[第4章：for 循环](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::
