---
title: 第2章作业
eyebrow: HOMEWORK 02
code: HOMEWORK 02
description: 题目、参考答案与解析。
questionGroups:
  - [判断题, judgment, 16]
  - [单选题, choice, 12]
  - [填空题, blank, 21]
  - [编程题, programming, 14]
---

<div class="editor-note">

题目整理自所提供的 PTA 网页，参考答案按 Python 3 核对，未在 PTA 平台提交验证。原题编号重复时保留原编号，以页面题序区分。

</div>

<h2 id="judgment" class="quiz-group">判断题<span>16 QUESTIONS</span></h2>

:::: question judgment-1 | 1-1 判断题

输入正整数6和5,要求和，`6+66+666+6666+66666`,下面程序正确吗？

```python
 a=int(input())    
 n=int(input())    
 print(sum([int('a'*i) for i in range(1,n+1)]))
```

<div class="question-tags">
<span class="question-tag">字符串重复</span>
<span class="question-tag">str 与 int 转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`'a'` 是引号中的固定字符，并不会读取变量 `a` 的值。执行 `'a' * i` 得到的是 `'a'`、`'aa'` 等字符串，随后 `int('a')` 无法转换成整数，会引发 `ValueError`。

如果要重复变量 `a` 中的数字，应先用 `str(a)` 将它转成字符串，再重复并转回整数，例如 `int(str(a) * i)`。因此原程序错误。

</div>

:::

::::

:::: question judgment-2 | 1-2 判断题

下面程序的运行结果是4。

```python
    i=3         
    ++i
```

<div class="question-tags">
<span class="question-tag">一元运算符</span>
<span class="question-tag">自增运算</span>
</div>

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

:::: question judgment-3 | 1-3 判断题

当输入是：`45,8` 时，下面程序的输出结果是37。

```python
a,b = input().split(',')
b=int(b)
c=int('a',b)
print(c)
```

<div class="question-tags">
<span class="question-tag">split 函数</span>
<span class="question-tag">int 进制转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入 `45,8` 后，`split(',')` 得到两个字符串：`a` 为 `'45'`，`b` 为 `'8'`。执行 `b = int(b)` 后，`b` 变成整数 8。

问题出在 `int('a', b)`：引号里的 `'a'` 是字母 a，并不是变量 `a`。八进制不包含字母 a，因此会报错。正确写法应为 `int(a, b)`，即把字符串 `'45'` 按八进制转换，结果为 37。

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

<div class="question-tags">
<span class="question-tag">input 函数</span>
<span class="question-tag">int 与 float 转换</span>
<span class="question-tag">格式化输出</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入 `10.0` 后，`input()` 得到字符串 `'10.0'`。`int()` 不能直接把带小数点的字符串转换成整数，因此 `int(input())` 会引发 `ValueError`，程序无法继续执行。

如果题目允许输入小数，应改用 `float(input())`。这样 `x` 为 `10.0`，计算 `1 / x` 得到 `0.1`，再通过 `:.1f` 保留一位小数。

</div>

:::

::::

:::: question judgment-5 | 1-5 判断题

表达式 `-2**4` 等于16。

<div class="question-tags">
<span class="question-tag">运算符优先级</span>
<span class="question-tag">乘方运算</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 中乘方 `**` 的优先级高于左侧的一元负号。因此 `-2**4` 会先计算 `2**4`，再加上负号：

\(-2**4 = -(2**4) = -16\)。

如果希望先把 -2 作为整体进行乘方，需要加括号：`(-2)**4`，结果才是 16。

</div>

:::

::::

:::: question judgment-6 | 1-6 判断题

下面程序的输入是5，输出是：

```python
*****
*****
```

```python
m=int(input())
print('{:^5}'.format('*'*m))
print('{:^m}'.format('*'*m))
```

<div class="question-tags">
<span class="question-tag">format 格式化</span>
<span class="question-tag">字符串重复</span>
<span class="question-tag">动态宽度</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入 `5` 后，`'*' * m` 会生成五个星号。第一句 `'{:^5}'.format(...)` 使用宽度 5 居中输出，字符串本身正好有 5 个字符，因此显示 `*****`。

第二句中的 `'{:^m}'` 把字母 `m` 当成格式说明的一部分，并不会自动读取变量 `m`，因此格式说明无效，会引发错误。若要使用变量控制宽度，可以写 `'{:^{}}'.format('*' * m, m)`。所以原程序无法得到题目所说的输出。

</div>

:::

::::

:::: question judgment-7 | 1-7 判断题

下面程序的输出是：这是字符串输出格式□□123。 □表示空格。

`print("这是字符串输出格式{:5s}".format("123"))`

<div class="question-tags">
<span class="question-tag">format 格式化</span>
<span class="question-tag">字符串对齐</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

格式说明 `:5s` 表示字符串至少占 5 个字符宽度。字符串默认左对齐，`'123'` 只有 3 个字符，因此会在右侧补两个空格。

实际结果是 `这是字符串输出格式123  `，空格位于 `123` 后面，而题目说空格在前面，所以判断为错误。

</div>

:::

::::

:::: question judgment-8 | 1-8 判断题

下面语句的输出是：这是数字输出格式$\Box$$\Box$123。 $\Box$表示空格  
`print("这是数字输出格式{:5d}".format(123))`

<div class="question-tags">
<span class="question-tag">format 格式化</span>
<span class="question-tag">数字对齐</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

格式说明 `:5d` 表示整数按十进制显示，最小宽度为 5。整数 `123` 只有 3 位，而数字默认右对齐，因此会在左侧补两个空格。

输出内容就是 `这是数字输出格式□□123`，其中 `□` 表示空格，所以题目说法正确。

</div>

:::

::::

:::: question judgment-9 | 1-9 判断题

`int(True)`的返回值是1。

<div class="question-tags">
<span class="question-tag">bool 类型</span>
<span class="question-tag">int 类型转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 中 `bool` 是 `int` 的子类，两个布尔值也可以参与整数运算：`True` 对应 1，`False` 对应 0。

因此 `int(True)` 的结果是整数 `1`，题目说法正确。

</div>

:::

::::

:::: question judgment-10 | 1-10 判断题

`bool(FALSE)`的返回值是True。

<div class="question-tags">
<span class="question-tag">布尔常量</span>
<span class="question-tag">标识符大小写</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 区分大小写，布尔常量必须写成 `True` 和 `False`。题目中的 `FALSE` 并不是布尔常量；如果此前没有定义名为 `FALSE` 的变量，执行 `bool(FALSE)` 时会因为找不到这个名字而引发 `NameError`。

因此程序无法得到 `True`，题目说法错误。

</div>

:::

::::

:::: question judgment-11 | 1-11 判断题

`bool([])`的返回值是False。

<div class="question-tags">
<span class="question-tag">bool 函数</span>
<span class="question-tag">空列表</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 中空容器会被视为假值，例如空列表 `[]`、空字符串 `''` 和空字典 `{}`。

因此 `bool([])` 的结果是 `False`，题目说法正确。注意，非空列表即使里面只有 0，例如 `[0]`，仍然是真值。

</div>

:::

::::

:::: question judgment-12 | 1-12 判断题

`bool(None)`的返回值是False。

<div class="question-tags">
<span class="question-tag">bool 函数</span>
<span class="question-tag">None 空值</span>
</div>

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

:::: question judgment-13 | 1-13 判断题

`print(bin(12.5))`的输出是`0b1100.1`

<div class="question-tags">
<span class="question-tag">bin 函数</span>
<span class="question-tag">整数与浮点数</span>
</div>

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

:::: question judgment-14 | 1-14 判断题

int("92",8)的值是74。

<div class="question-tags">
<span class="question-tag">int 函数</span>
<span class="question-tag">进制转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`int(字符串, 进制)` 会按照指定进制解析字符串。八进制只允许出现 `0` 到 `7`，不能出现数字 `8` 或 `9`。

因此 `int('92', 8)` 会因为字符串中含有非法数字 `9` 而引发 `ValueError`，不会得到 74，题目错误。

</div>

:::

::::

:::: question judgment-15 | 1-15 判断题

表达式`3 and 0 and "hello"`的值是False。

<div class="question-tags">
<span class="question-tag">and 运算</span>
<span class="question-tag">短路求值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`and` 会从左向右检查操作数，遇到第一个假值时就停止，并返回这个假值本身。这里 `3` 是真值，接着遇到 `0`，所以整个表达式返回整数 `0`，后面的字符串 `'hello'` 不再参与判断。

结果是 `0`，并非布尔对象 `False`。虽然 `0 == False` 的结果为 `True`，但二者类型不同，因此题目说法错误。

</div>

:::

::::

:::: question judgment-16 | 1-16 判断题

z已赋值，x=(y=z+1)语句是错误语句

<div class="question-tags">
<span class="question-tag">赋值语句</span>
<span class="question-tag">链式赋值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 中普通赋值符号 `=` 是一条语句，不能像数学表达式那样嵌套在另一个赋值表达式中。因此 `x=(y=z+1)` 会产生语法错误。

如果希望让 `x` 和 `y` 都等于 `z+1`，可以使用链式赋值：`x = y = z + 1`。所以题目中的语句错误。

</div>

:::

::::

<h2 id="choice" class="quiz-group">单选题<span>12 QUESTIONS</span></h2>

:::: question choice-1 | 2-1 单选题

下列数据类型中， Python不支持的是_____________。

**A.** char

**B.** int

**C.** float

**D.** list

<div class="question-tags">
<span class="question-tag">Python 数据类型</span>
<span class="question-tag">字符串类型</span>
</div>

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

:::: question choice-2 | 2-2 单选题

Python 语句print(type(1J))的输出结果是______________。

**A.** `<class‘complex’>`

**B.** `<class ‘int’>`

**C.** `<class ‘float’>`

**D.** `<class ‘dict’>`

<div class="question-tags">
<span class="question-tag">complex 复数类型</span>
<span class="question-tag">type 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 使用 `j` 或 `J` 表示虚数单位，因此 `1J` 是一个复数。`type()` 用于查看数据的类型，`type(1J)` 返回 `<class 'complex'>`。

所以选择 A。

</div>

:::

::::

:::: question choice-3 | 2-3 单选题

Python 语句print(type(1/2))的输出结果是______________。

**A.** `<class ‘int’>`

**B.** `<class ‘number’>`

**C.** `<class ‘float’>`

**D.** `<class ‘double’>`

<div class="question-tags">
<span class="question-tag">除法运算</span>
<span class="question-tag">type 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 中 `/` 表示普通除法，即使两个操作数都是整数，结果也会是浮点数。

例如 `1 / 2` 得到 `0.5`，其类型为 `float`，所以选择 C。

</div>

:::

::::

:::: question choice-4 | 2-4 单选题

Python 语句print(type(1//2))的输出结果是______________。

**A.** `<class ‘int’>`

**B.** `<class ‘number’>`

**C.** `<class ‘float’>`

**D.** `<class ‘double’>`

<div class="question-tags">
<span class="question-tag">整除运算</span>
<span class="question-tag">type 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`//` 表示整除。两个整数进行整除，结果仍然是整数。题目中 `1 // 2` 的结果为整数 `0`，因此 `type(1 // 2)` 返回 `<class 'int'>`。

所以选择 A。

</div>

:::

::::

:::: question choice-5 | 2-5 单选题

Python 语句 a=121+1.21; print(type(a))的输出结果是_____________。

**A.** `<class ‘int’>`

**B.** `<class ‘float’>`

**C.** `<class ‘double’>`

**D.** `<class ‘long’>`

<div class="question-tags">
<span class="question-tag">int 与 float</span>
<span class="question-tag">混合类型运算</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

表达式 `121 + 1.21` 中，一个操作数是整数，另一个是浮点数。两者相加时，结果会转换为浮点数。

因此 `a` 的类型是 `float`，选择 B。

</div>

:::

::::

:::: question choice-6 | 2-6 单选题

Python 语句 print(0xA + 0xB)的输出结果是______________。

**A.** 0xA + 0xB

**B.** A + B

**C.** 0xA0xB

**D.** 21

<div class="question-tags">
<span class="question-tag">十六进制</span>
<span class="question-tag">整数运算</span>
</div>

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

Python 语句x=’car’; y = 2; print (x+y)的输出结果是____________。

**A.** 语法错

**B.** 2

**C.** 'car2’

**D.** 'carcar’

<div class="question-tags">
<span class="question-tag">字符串拼接</span>
<span class="question-tag">数据类型错误</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

无严格正确选项；按普通引号还原后为运行时 `TypeError`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

如果把题目中的弯引号按普通字符串引号理解，`x` 是字符串 `'car'`，`y` 是整数 `2`。字符串和整数不能直接使用 `+` 相加，因此执行 `x + y` 时会产生运行时 `TypeError`。

如果代码真的使用题面显示的弯引号，Python 会在解析代码时先报 `SyntaxError`。无论按哪种情况理解，选项中都没有准确描述普通引号下运行时错误的选项；原题选项存在不严谨之处。

</div>

:::

::::

:::: question choice-8 | 2-8 单选题

表达式1+2*3.14>0的结果类型是:

**A.** int

**B.** long

**C.** float

**D.** bool

<div class="question-tags">
<span class="question-tag">比较运算符</span>
<span class="question-tag">bool 类型</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先按运算优先级计算乘法：`1 + 2 * 3.14 = 7.28`，再判断 `7.28 > 0`。比较运算符 `>` 的结果是布尔值 `True` 或 `False`。

因此整个表达式的类型是 `bool`，选择 D。

</div>

:::

::::

:::: question choice-9 | 2-9 单选题

如math模块已引入，Python 表达式 `math.sqrt(4)*math.sqrt(9)`的值为________。

**A.** 36.0

**B.** 6

**C.** 13

**D.** 6.0

<div class="question-tags">
<span class="question-tag">math.sqrt 函数</span>
<span class="question-tag">浮点数运算</span>
</div>

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

:::: question choice-10 | 2-10 单选题

关于Python中的复数，下列说法错误的是___________。

**A.** 表示复数的语法是real + imag j

**B.** 实部和虚部都是浮点数

**C.** 虚部必须后缀j, 且必须是小写

**D.** 方法conjugate 返回复数的共轭复数

<div class="question-tags">
<span class="question-tag">complex 复数类型</span>
<span class="question-tag">虚数单位</span>
</div>

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

:::: question choice-11 | 2-11 单选题

Python 语句 print(chr(65))的运行结果是___________。

**A.** 65

**B.** 6

**C.** 5

**D.** A

<div class="question-tags">
<span class="question-tag">chr 函数</span>
<span class="question-tag">字符编码</span>
</div>

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

:::: question choice-12 | 2-12 单选题

关于Python字符串，下列说法错误的是___________。

**A.** 字符即长度为1的字符串

**B.** 字符串以\0标志字符串的结束

**C.** 既可以用单引号，也可以用双引号创建字符串

**D.** 在三引号字符串中可以包含换行回车等特殊字符

<div class="question-tags">
<span class="question-tag">字符串类型</span>
<span class="question-tag">字符串长度</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 字符串可以用单引号、双引号或三引号创建，三引号字符串也可以包含换行。Python 没有独立的 `char` 类型，单个字符仍然是长度为 1 的字符串。

字符串的结束位置由 Python 字符串对象自身记录，并不依靠 ` ` 作为结束标志。字符串中即使包含空字符 ` `，它也仍然是字符串内容的一部分。因此 B 的说法错误。

</div>

:::

::::

<h2 id="blank" class="quiz-group">填空题<span>21 QUESTIONS</span></h2>

:::: question blank-1 | 4-1 填空题

Python 表达式 10 + 5//3 –True+False的值为 _____ .

<div class="question-tags">
<span class="question-tag">运算符优先级</span>
<span class="question-tag">bool 与整数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`10`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算整除：`5 // 3 = 1`。再注意 Python 中 `True` 转成整数是 1，`False` 转成整数是 0。

所以表达式的值为 `10 + 1 - 1 + 0 = 10`。

</div>

:::

::::

:::: question blank-2 | 4-2 填空题

Python 表达式 3**2**3 的值为 _____

<div class="question-tags">
<span class="question-tag">乘方运算</span>
<span class="question-tag">运算符结合方向</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`6561`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 的乘方运算符 `**` 从右向左结合，因此 `3**2**3` 等价于 `3**(2**3)`。

先算 `2**3 = 8`，再算 `3**8 = 6561`。

</div>

:::

::::

:::: question blank-3 | 4-3 填空题

Python 表达式 round(17.0/3**2,2) 的值为 _____ 。

<div class="question-tags">
<span class="question-tag">round 函数</span>
<span class="question-tag">小数精度</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`1.89`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算乘方：`3**2 = 9`；再计算除法：`17.0 / 9 ≈ 1.888888...`。最后 `round(数值, 2)` 将结果四舍五入到小数点后两位。

因此结果为 `1.89`。

</div>

:::

::::

:::: question blank-4 | 4-4 填空题

Python 表达式 0 and 1 or not 2&lt;True 的值为 _____ 。

<div class="question-tags">
<span class="question-tag">逻辑运算优先级</span>
<span class="question-tag">短路求值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算比较表达式 `2 < True`。在 Python 中 `True` 对应数值 1，因此 `2 < 1` 为 `False`，取反后 `not (2 < True)` 得到 `True`。

`and` 的优先级高于 `or`：`0 and 1` 返回 0，随后 `0 or True` 返回 `True`。所以最终结果是 `True`。

</div>

:::

::::

:::: question blank-5 | 4-5 填空题

Python 语句 print(int("20", 16), int("101",2))的输出结果是 _____ 。

<div class="question-tags">
<span class="question-tag">int 函数</span>
<span class="question-tag">进制转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`32 5`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`int(字符串, 进制)` 会按照指定进制把字符串转换成十进制整数。`int('20', 16)` 表示十六进制的 20，即 `2 × 16 = 32`；`int('101', 2)` 表示二进制的 101，即 `4 + 1 = 5`。

`print()` 默认用一个空格分隔两个参数，因此输出 `32 5`。

</div>

:::

::::

:::: question blank-6 | 4-6 填空题

Python 语句 print(hex(16), bin(10))的输出结果是(进制用小写字母表示） _____ 。

<div class="question-tags">
<span class="question-tag">hex 函数</span>
<span class="question-tag">bin 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`0x10 0b1010`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`hex()` 把整数转换成带 `0x` 前缀的十六进制字符串，`bin()` 把整数转换成带 `0b` 前缀的二进制字符串。

因此 `hex(16)` 得到 `'0x10'`，`bin(10)` 得到 `'0b1010'`。`print()` 会在两者之间自动加一个空格。

</div>

:::

::::

:::: question blank-7 | 4-7 填空题

已知 a=3; b=5; c=6; d=True, 则表达式 not d or a>=0 and a+c>b+3的值是 _____ 。

<div class="question-tags">
<span class="question-tag">not、and、or</span>
<span class="question-tag">逻辑表达式</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算 `not d`。因为 `d=True`，所以 `not d` 为 `False`。再计算比较：`a >= 0` 为真，`a+c=9`，`b+3=8`，所以 `a+c > b+3` 也为真。

因此右侧 `and` 的结果为 `True`，最后 `False or True` 得到 `True`。

</div>

:::

::::

:::: question blank-8 | 4-8 填空题

Python 语句 print(abs(-10.2), round(abs(8-2j),3)) 的输出结果是 _____ 。

<div class="question-tags">
<span class="question-tag">abs 函数</span>
<span class="question-tag">复数的模</span>
</div>

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

:::: question blank-9 | 4-9 填空题

Python 语句 x=True; y=False; z=False; print(x or y and z)的程序运行结果是 _____ 。

<div class="question-tags">
<span class="question-tag">and 与 or</span>
<span class="question-tag">运算符优先级</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`and` 的优先级高于 `or`，所以先计算 `y and z`。由于 `y=False`，结果为 `False`。

原表达式相当于 `True or False`，最终结果为 `True`。

</div>

:::

::::

:::: question blank-10 | 4-10 填空题

Python 语句 x=0; y= True; print(x>=y and‘A'&lt;'B') 的程序运行结果是 _____ 。

<div class="question-tags">
<span class="question-tag">比较运算</span>
<span class="question-tag">and 短路求值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`False`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算 `x >= y`。这里 `x=0`，`y=True`，而 `True` 在数值比较中相当于 1，所以 `0 >= 1` 为 `False`。

`and` 遇到左侧假值后会直接返回，不再计算右侧的字符串比较。因此最终结果为 `False`。

</div>

:::

::::

:::: question blank-11 | 4-11 填空题

Python 表达式 16-25>78/2 or "XYZ"!="xyz"and not (10-6>18/2)的值是 _____ 。

<div class="question-tags">
<span class="question-tag">逻辑运算优先级</span>
<span class="question-tag">字符串比较</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算算术和比较：`16-25=-9`，`78/2=39`，所以第一项比较为假。字符串比较区分大小写，因此 `'XYZ' != 'xyz'` 为真。

括号中 `10-6=4`、`18/2=9`，所以 `4>9` 为假，取反后为真。于是右侧 `True and True` 为真，最终 `False or True` 得到 `True`。

</div>

:::

::::

:::: question blank-12 | 4-12 填空题

Python输出 print("hello" 'world')的结果是 _____ 。

<div class="question-tags">
<span class="question-tag">字符串字面量</span>
<span class="question-tag">print 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`helloworld`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 允许把相邻的字符串字面量直接写在一起，编译时会自动将它们拼接。例如 `'hello' 'world'` 等价于 `'helloworld'`。

因此 `print()` 只接收到一个字符串参数，输出 `helloworld`，中间不会自动添加空格。

</div>

:::

::::

:::: question blank-13 | 4-13 填空题

表达式((2>=2) or (2&lt;2)) and 2的值为多少？ _____

<div class="question-tags">
<span class="question-tag">and 与 or</span>
<span class="question-tag">逻辑运算返回值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`2`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算括号：`2 >= 2` 为 `True`，`2 < 2` 为 `False`，两者通过 `or` 连接后结果为 `True`。

Python 的 `and` 不一定返回布尔值：左侧为真时会返回右侧操作数。因此 `True and 2` 的结果是整数 `2`。

</div>

:::

::::

:::: question blank-14 | 4-14 填空题

表达式 3 and 0 and 5的结果是什么？。 _____

<div class="question-tags">
<span class="question-tag">and 运算</span>
<span class="question-tag">短路求值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`0`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`and` 从左向右检查操作数，遇到第一个假值就停止，并返回这个假值本身。`3` 是真值，所以继续检查；`0` 是假值，因此表达式直接返回整数 `0`，后面的 `5` 不再计算。

</div>

:::

::::

:::: question blank-15 | 4-15 填空题

表达式 --3 的结果是什么？ _____ 。

<div class="question-tags">
<span class="question-tag">一元负号</span>
<span class="question-tag">运算符解析</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`3`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

连续两个负号相当于对数字取两次相反数：`--3` 等价于 `-(-3)`。

第一次得到 `-3`，第二次再取相反数，最终结果为 `3`。

</div>

:::

::::

:::: question blank-16 | 4-16 填空题

表达式 ---3 的结果是什么？ _____ 。

<div class="question-tags">
<span class="question-tag">一元负号</span>
<span class="question-tag">运算符解析</span>
</div>

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

:::: question blank-17 | 4-17 填空题

表达式`32.2//6-24//6`的值是 _____ 。

<div class="question-tags">
<span class="question-tag">整除运算</span>
<span class="question-tag">浮点数结果类型</span>
</div>

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

:::: question blank-18 | 4-18 填空题

**猜生日**  
运行下面程序，输入是10011时，输出是 _____ 。

如果你的生日在列表中，输入1，否则输入0。如你的生日是19号，输入`11001`。这个程序能猜到你的生日吗？ _____ 。能,填yes;不能,填no。

```python
lst1=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
lst2=[2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
lst3=[4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
lst4=[8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
lst5=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
s=input()
print((lst1[0] if s[0]=="1" else 0) 
        +(lst2[0] if s[1]=="1" else 0) 
        +(lst3[0] if s[2]=="1" else 0)
        +(lst4[0] if s[3]=="1" else 0)
        +(lst5[0] if s[4]=="1" else 0))
```

<div class="question-tags">
<span class="question-tag">二进制位权</span>
<span class="question-tag">列表索引</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`25`；`yes`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

程序用五个列表分别表示生日数字的 1、2、4、8、16 这五个二进制位。输入 `10011` 时，`s[0]` 和 `s[3]`、`s[4]` 为 `'1'`，因此程序把对应的 1、8、16 相加，得到 `25`。

第二问填 `yes`。每个列表对应一个二进制位，用户按提示输入各位是否包含自己的生日，程序把对应位权相加，就能还原 1～31 之间的日期。注意题目给出的输入顺序是从低位到高位，所以 19 号输入为 `11001`。

</div>

:::

::::

:::: question blank-19 | 4-19 填空题

汉字`张`的Unicode编码是 _____ 。

<div class="question-tags">
<span class="question-tag">ord 函数</span>
<span class="question-tag">Unicode 编码</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`24352`（十六进制 `U+5F20`）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`ord()` 可以查询字符对应的 Unicode 码点。执行 `ord('张')` 得到十进制整数 `24352`，它对应的十六进制码点写作 `U+5F20`。

因此答案可以写为 `24352`，也可以写成 `U+5F20`。

</div>

:::

::::

:::: question blank-20 | 4-20 填空题

```python
-7 & 5 的结果是_____ 。
-7 | 9  的结果是_____。
-7 ^ 9 的结果是_____。
 ~9 的结果是_____
```

<div class="question-tags">
<span class="question-tag">按位运算</span>
<span class="question-tag">补码表示</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`1`、`-7`、`-16`、`-10`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

按位运算会逐位处理二进制数。用 8 位补码观察，`-7` 可写成 `11111001`，`5` 为 `00000101`，所以 `-7 & 5` 得到 `00000001`，即 1。

`-7 | 9` 的结果为 -7，`-7 ^ 9` 的结果为 -16。按位取反还满足公式 `~x = -x - 1`，因此 `~9 = -10`。

</div>

:::

::::

:::: question blank-21 | 4-21 填空题

下面程序输出是 _____ 。

```python
n = 39
remainders = []
while n>0:
    n,remainder = divmod(n,2)
    remainders.insert(0,remainder)
print(len(remainders))

```

<div class="question-tags">
<span class="question-tag">divmod 函数</span>
<span class="question-tag">while 循环</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`6`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`divmod(n, 2)` 会同时返回除以 2 的商和余数。程序每循环一次，就把当前数字除以 2，并把余数插入列表最前面，直到商变成 0。

39 的二进制是 `100111`，共有 6 位，因此循环执行 6 次，`remainders` 中有 6 个元素，`len(remainders)` 输出 `6`。

</div>

:::

::::

<h2 id="programming" class="quiz-group">编程题<span>14 QUESTIONS</span></h2>

:::: question programming-1 | 7-1 计算 11+12+13+...+m

输入一个正整数m(20&lt;=m&lt;=100)，计算 11+12+13+...+m 的值。

#### 输入格式:

在一行输入一个正整数m。

#### 输出格式:

在一行中按照格式“sum = S”输出对应的和S.

#### 输入样例:

在这里给出一组输入。例如：

```text
90 
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
sum = 4040
```

<div class="question-tags">
<span class="question-tag">range 函数</span>
<span class="question-tag">sum 函数</span>
<span class="question-tag">f-string</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m = int(input())
print(f'sum = {sum(range(11, m + 1))}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先读取整数 `m`。`range(11, m + 1)` 从 11 开始，步长默认为 1；由于 `range()` 不包含终点，所以终点写成 `m + 1`，才能把 `m` 也加进去。

`sum()` 将这些整数相加，最后用 f-string 按题目要求输出 `sum = 结果`。例如 `m=90` 时，计算的就是 11 到 90 的和。

</div>

:::

::::

:::: question programming-2 | 7-2 计算分段函数

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

<div class="question-tags">
<span class="question-tag">if 条件判断</span>
<span class="question-tag">条件表达式</span>
<span class="question-tag">float 类型</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
x = float(input())
result = 0 if x == 0 else 1 / (2 * x)
print(f'g({x:.3f}) = {result:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入可能包含小数，因此使用 `float(input())`。根据分段函数，先判断 `x` 是否为 0：如果是，结果为 0；否则计算 `1 / (2 * x)`，这样可以避免除以 0。

代码中的 `A if 条件 else B` 是条件表达式，条件成立时取 A，否则取 B。最后 `:.3f` 表示将 x 和结果都按三位小数显示。

</div>

:::

::::

:::: question programming-3 | 7-3 阶梯电价

为了提倡居民节约用电，某省电力公司执行“阶梯电价”，安装一户一表的居民用户电价分为两个“阶梯”：月用电量50千瓦时（含50千瓦时）以内的，电价为0.53元/千瓦时；超过50千瓦时的，超出部分的用电量，电价上调`X`元/千瓦时。请编写程序计算电费。

#### 输入格式:

一行中输入某用户的月用电量（单位：千瓦时）和电价上调的`X`值（单位：元），中间用空格分开。

#### 输出格式:

在一行中输出该用户应支付的电费（元），结果保留两位小数，格式如：“cost = 应付电费值”。

#### 输入样例1:

在这里给出一组输入。例如：

```text
10 0.05
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
cost = 5.30
```

#### 输入样例:

在这里给出一组输入。例如：

```text
100 0.05
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
cost = 55.50
```

<div class="question-tags">
<span class="question-tag">map 函数</span>
<span class="question-tag">min 与 max 函数</span>
<span class="question-tag">阶梯计费</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
usage, extra = map(float, input().split())
cost = min(usage, 50) * 0.53 + max(usage - 50, 0) * (0.53 + extra)
print(f'cost = {cost:.2f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入的用电量和加价 `X` 都可能是小数，因此用 `map(float, input().split())` 将两个输入分别转换成浮点数。

费用分成两部分：前 50 度按每度 0.53 元计算，`min(usage, 50)` 用来取得这部分电量；超过 50 度的部分按每度 `0.53 + extra` 计算，`max(usage - 50, 0)` 用来取得超出电量。最后用 `:.2f` 保留两位小数。

</div>

:::

::::

:::: question programming-4 | 7-4 求奇数分之一序列前N项近似和

本题要求编写程序，计算序列 1 + 1/3 + 1/5 + ... 的前N项近似和（提示：用ceil函数）。

#### 输入格式:

输入在一行中给出一个正整数N。

#### 输出格式:

在一行中按照“sum ≈ S”的格式输出近似和S。S是大于序列和的最小整数

#### 输入样例:

在这里给出一组输入。例如：

```text
23
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
sum ≈ 3
```

<div class="question-tags">
<span class="question-tag">range 函数</span>
<span class="question-tag">Fraction 分数</span>
<span class="question-tag">ceil 向上取整</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
from fractions import Fraction
from math import ceil
n = int(input())
total = sum((Fraction(1, 2 * i - 1) for i in range(1, n + 1)), Fraction())
print(f'sum ≈ {ceil(total)}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

第 i 项的分母是 `2*i-1`，所以前 N 项可以通过 `i=1` 到 `i=N` 逐项生成：`1/1、1/3、1/5……`。`Fraction(1, 2*i-1)` 用分子和分母创建精确分数，避免浮点数近似误差。

`sum()` 将各项相加，`ceil()` 则向上取整，得到不小于总和的最小整数。代码中的 `Fraction()` 是求和的初始值 0。

</div>

:::

::::

:::: question programming-5 | 7-5 求交错序列前N项和

本题要求编写程序，计算交错序列 1-2/3+3/5-4/7+5/9-6/11+... 的前N项之和。

#### 输入格式:

输入在一行中给出一个正整数N。

#### 输出格式:

在一行中输出部分和的值，结果保留三位小数。

#### 输入样例:

```text
5
```

#### 输出样例:

```text
0.917
```

<div class="question-tags">
<span class="question-tag">range 函数</span>
<span class="question-tag">累加求和</span>
<span class="question-tag">交错符号</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
total = sum((-1) ** (i - 1) * i / (2 * i - 1) for i in range(1, n + 1))
print(f'{total:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

第 i 项的分子是 i，分母是 `2*i-1`，所以每项的数值为 `i/(2*i-1)`。符号由 `(-1)**(i-1)` 控制：i 为奇数时得到正号，i 为偶数时得到负号，正好形成 `1 - 2/3 + 3/5 - 4/7 ...`。

`range(1, n+1)` 生成前 N 项，`sum()` 累加它们，最后 `:.3f` 将结果保留三位小数。

</div>

:::

::::

:::: question programming-6 | 7-6 产生每位数字相同的n位数

读入2个正整数A和B，1&lt;=A&lt;=9, 1&lt;=B&lt;=10,产生数字AA...A,一共B个A

#### 输入格式:

在一行中输入A和B。

#### 输出格式:

在一行中输出整数AA...A,一共B个A

#### 输入样例1:

在这里给出一组输入。例如：

```text
  1,  5
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
11111
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
        3  ,4
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
3333
```

<div class="question-tags">
<span class="question-tag">replace 函数</span>
<span class="question-tag">split 函数</span>
<span class="question-tag">字符串重复</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a, b = map(int, input().replace(',', ' ').split())
print(int(str(a) * b))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

题目样例中既有逗号分隔，也有空格分隔，因此先用 `replace(',', ' ')` 把逗号统一替换为空格，再用 `split()` 拆分输入。`map(int, ...)` 将 A 和 B 转换成整数。

`str(a) * b` 会把数字 a 转成字符串后重复 b 次，例如 `str(3) * 4` 得到 `'3333'`。最后用 `int()` 将这个字符串转回整数输出。

</div>

:::

::::

:::: question programming-7 | 7-7 转换函数使用

输入一个整数和进制，转换成十进制输出

#### 输入格式:

在一行输入整数和进制

#### 输出格式:

在一行十进制输出结果

#### 输入样例:

在这里给出一组输入。例如：

```text
45,8
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
37
```

<div class="question-tags">
<span class="question-tag">split 函数</span>
<span class="question-tag">int 进制转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
digits, base = input().replace(',', ' ').split()
print(int(digits, int(base)))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先用 `replace(',', ' ')` 将输入中的逗号替换为空格，再用 `split()` 分离数字文本和进制。这里保留 `digits` 为字符串，因为 `int()` 的第二个参数需要根据指定进制解析字符串。

`int(digits, int(base))` 表示按 base 进制读取 digits。样例中 `45` 是八进制数，换算为 `4*8+5=37`，因此输出 37。

</div>

:::

::::

:::: question programming-8 | 7-8 比较大小

输入3个不同整数,这3个整数分别对应3个字母的ASCII码值，把这3个字母按它的ASCII码值从小到大输出。

#### 输入格式:

输入在一行中给出3个整数，其间以空格分隔

#### 输出格式:

在一行中将3个字母按ASCII码值从小到大输出，其间以“&lt;”相连。

#### 输入样例:

在这里给出一组输入。例如：

```text
97 65 100
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
A<a<d
```

<div class="question-tags">
<span class="question-tag">sorted 函数</span>
<span class="question-tag">chr 函数</span>
<span class="question-tag">join 方法</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
numbers = sorted(map(int, input().split()))
print('<'.join(chr(n) for n in numbers))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先用 `input().split()` 拆分三个输入，再通过 `map(int, ...)` 转成整数。`sorted()` 按数值从小到大排序，得到三个 ASCII 码。

`chr(n)` 将 ASCII 码转换成对应字符，`'<'.join(...)` 再用字符 `<` 把三个字母连接起来。样例中的 65、97、100 对应 A、a、d，因此输出 `A<a<d`。

</div>

:::

::::

:::: question programming-9 | 7-9 输出摄氏-华氏温度转换表

输入2个正整数lower和upper（-20&lt;=lower&lt;=upper&lt;=50），表示摄氏范围。请输出一张取值范围为[lower，upper]、  
且每次增加2摄氏度的摄氏-华氏温度转换表。温度转换的计算公式：  
 F=C×1.8+32  
其中：C表示摄氏温度，F表示华氏温度。

#### 输入格式:

在一行中输入2个整数，分别表示lower和upper的值，中间用空格分开。

#### 输出格式:

第一行输出："celsius$\Box\Box\Box\Box$fahr"

接着每行输出一个摄氏温度celsius（整数）与一个华氏温度fahr（占据14个字符宽度，靠右对齐，保留1位小数）。

若输入的范围不合法，则输出"Invalid."。

#### 输入样例1:

在这里给出一组输入。例如：

```text
2 9
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
celsius    fahr
2          35.6
4          39.2
6          42.8
8          46.4
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
2 51
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
Invalid.
```

<div class="question-tags">
<span class="question-tag">range 函数</span>
<span class="question-tag">条件判断</span>
<span class="question-tag">格式化输出</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
lower, upper = map(int, input().split())
if not (-20 <= lower <= upper <= 50):
    print('Invalid.')
else:
    print('celsius    fahr')
    for c in range(lower, upper + 1, 2):
        print(f'{c}{c * 1.8 + 32:14.1f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先检查输入范围是否满足 `-20 <= lower <= upper <= 50`。这是连续比较，表示三个条件必须同时成立；不满足时输出 `Invalid.`。

合法时，`range(lower, upper + 1, 2)` 从 lower 开始，每次增加 2。因为 range 不包含终点，所以使用 `upper + 1`，确保能够取到符合步长的 upper。`{fahr:14.1f}` 表示华氏温度占 14 个字符宽度、右对齐并保留一位小数。

</div>

:::

::::

:::: question programming-10 | 7-10 偶数位特殊序列和

给定不超过9的正整数a，给定正整数n,n是偶数,4&lt;=n&lt;=18，要求编写程序求aa+aaaa+aaaaaa+⋯+aa⋯a（n个a）之和。

#### 输入格式:

在一行中给出不超过9的正整数a和n。

#### 输出格式:

在一行中输出对应的和。

#### 输入样例:

在这里给出一组输入。例如：

```text
1 4
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
1122
```

<div class="question-tags">
<span class="question-tag">range 函数</span>
<span class="question-tag">字符串重复</span>
<span class="question-tag">sum 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a, n = map(int, input().split())
print(sum(int(str(a) * width) for width in range(2, n + 1, 2)))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

题目要求的数字长度依次为 2、4、6，直到 n，因此使用 `range(2, n + 1, 2)` 每次增加 2。对每个长度 `width`，`str(a) * width` 会生成对应长度的重复数字字符串，再用 `int()` 转成整数。

最后 `sum()` 把所有项相加。例如输入 `1 4`，得到 `11 + 1111 = 1122`。

</div>

:::

::::

:::: question programming-11 | 7-11 求平方与倒数序列的近似和

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

<div class="question-tags">
<span class="question-tag">range 函数</span>
<span class="question-tag">Fraction 分数</span>
<span class="question-tag">floor 向下取整</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
from fractions import Fraction
from math import floor
m, n = map(int, input().split())
total = sum((i * i + Fraction(1, i) for i in range(m, n + 1)), Fraction())
print(f'sum ≈ {floor(total)}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

从 m 到 n 逐个取整数 i，每一项为 `i*i + 1/i`，因此循环范围使用 `range(m, n + 1)`，保证包含 n。`Fraction(1, i)` 表示精确分数 1/i，避免浮点数近似影响最后取整。

`sum()` 累加所有项，`floor()` 向下取整，得到不大于总和的最大整数。题目提示使用 floor，因此最后输出 `floor(total)`。

</div>

:::

::::

:::: question programming-12 | 7-12 计算函数f(x)

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

<div class="question-tags">
<span class="question-tag">math 模块</span>
<span class="question-tag">三角函数与对数</span>
<span class="question-tag">格式化输出</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
import math
x = float(input())
result = math.sin(math.radians(35)) + (math.exp(x) - 15 * x) / math.sqrt(x ** 4 + 1) - math.log(7 * x)
print(f'f({x})={result:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入 x 是实数，因此先用 `float(input())` 转换。公式中的正弦、指数、平方根和自然对数分别使用 `math.sin()`、`math.exp()`、`math.sqrt()` 和 `math.log()`。

题目中的角度是 35°，而 `math.sin()` 接收弧度，所以先用 `math.radians(35)` 转换。分式的分子和分母用括号明确范围，最后通过 `:.3f` 将函数值保留三位小数。

</div>

:::

::::

:::: question programming-13 | 7-13 分段计算居民水费

为鼓励居民节约用水，自来水公司采取按用水量阶梯式计价的办法，居民应交水费$y$（元）与月用水量$x$（吨）相关：当$x$不超过15吨时，$y=4x/3$；超过后，$y=2.5x-17.5$。请编写程序实现水费的计算。

#### 输入格式：

输入在一行中给出非负实数$x$。

#### 输出格式：

在一行输出应交的水费，精确到小数点后2位。

#### 输入样例1：

```text
12
```

#### 输出样例1：

```text
16.00
```

#### 输入样例2：

```python
16
```

#### 输出样例2：

```python
22.50
```

<div class="question-tags">
<span class="question-tag">条件表达式</span>
<span class="question-tag">分段函数</span>
<span class="question-tag">float 类型</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
x = float(input())
y = 4 * x / 3 if x <= 15 else 2.5 * x - 17.5
print(f'{y:.2f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入水量可能是小数，因此使用 `float(input())`。当 `x <= 15` 时，按第一段公式 `4*x/3` 计算；超过 15 吨时，按第二段公式 `2.5*x-17.5` 计算。

`A if 条件 else B` 会根据条件选择其中一个表达式。最后 `:.2f` 将水费保留两位小数。

</div>

:::

::::

:::: question programming-14 | 7-14 输出指定图形

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

<div class="question-tags">
<span class="question-tag">for 循环</span>
<span class="question-tag">range 函数</span>
<span class="question-tag">字符串重复</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
for i in range(1, n + 1):
    print('* ' * i)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先读取行数 n，再用 `range(1, n + 1)` 让循环变量 i 依次取 1 到 n。第 i 行需要输出 i 个星号，因此可以使用字符串重复：`'* ' * i`。

例如 i=3 时，`'* ' * 3` 得到 `'* * * '`。`print()` 每次输出后会自动换行，于是最终形成 n 行递增的图形。

</div>

:::

::::
