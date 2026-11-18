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

<div class="section-label">题干 <span>QUESTION</span></div>

输入正整数6和5,要求和，`6+66+666+6666+66666`,下面程序正确吗？

```python
 a=int(input())    
 n=int(input())    
 print(sum([int('a'*i) for i in range(1,n+1)]))
```


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

'a' 是字面字符串，不是变量 a；int('a') 报错。应将变量写为 str(a)，如 int(str(a)*i)。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question judgment-2 | 1-2 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序的运行结果是4。

```python
    i=3         
    ++i
```


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<h4>Python 常见运算符优先级</h4><p>下面从高到低列出本课程常见的运算符。括号可以明确改变分组；同一层通常从左到右计算，乘方 <code>**</code> 是重要例外，它从右向左结合。</p><table><thead><tr><th>优先级</th><th>运算符</th><th>作用</th></tr></thead><tbody><tr><td>最高</td><td><code>(...)</code></td><td>括号</td></tr><tr><td></td><td><code>**</code></td><td>乘方</td></tr><tr><td></td><td><code>+x</code>、<code>-x</code>、<code>~x</code></td><td>一元运算</td></tr><tr><td></td><td><code>*</code>、<code>/</code>、<code>//</code>、<code>%</code></td><td>乘、除、整除、取余</td></tr><tr><td></td><td><code>+</code>、<code>-</code></td><td>加、减</td></tr><tr><td></td><td><code>&lt;</code>、<code>&lt;=</code>、<code>&gt;</code>、<code>&gt;=</code>、<code>==</code>、<code>!=</code>、<code>in</code>、<code>is</code></td><td>比较</td></tr><tr><td></td><td><code>not</code></td><td>逻辑非</td></tr><tr><td></td><td><code>and</code></td><td>逻辑与</td></tr><tr><td>最低</td><td><code>or</code></td><td>逻辑或</td></tr></tbody></table><p>例如 <code>3 + 2 * 4</code> 先算乘法；<code>3 ** 2 ** 3</code> 要看成 <code>3 ** (2 ** 3)</code>，所以结果是 6561。</p>

<h4>回到这道题</h4>

++i 是两次一元正号，不会自增，i 仍为 3；脚本中该表达式本身也不输出内容。原代码若整体前导缩进被直接保留，还会触发缩进错误。

<h4>容易出错的地方</h4>

<p>长表达式不要凭直觉从左往右算，先找括号，再按优先级分层。</p>

</div>

:::
:::: question judgment-3 | 1-3 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

当输入是：`45,8` 时，下面程序的输出结果是37。

```python
a,b = input().split(',')
b=int(b)
c=int('a',b)
print(c)
```


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

int('a',8) 解析的是字母 a，不是变量 a；八进制不包含 a。应写 int(a,b)。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

int('10.0') 引发 ValueError，程序不能运行到输出；应使用 float(input())。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question judgment-5 | 1-5 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式 `-2**4` 等于16。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<h4>Python 常见运算符优先级</h4><p>下面从高到低列出本课程常见的运算符。括号可以明确改变分组；同一层通常从左到右计算，乘方 <code>**</code> 是重要例外，它从右向左结合。</p><table><thead><tr><th>优先级</th><th>运算符</th><th>作用</th></tr></thead><tbody><tr><td>最高</td><td><code>(...)</code></td><td>括号</td></tr><tr><td></td><td><code>**</code></td><td>乘方</td></tr><tr><td></td><td><code>+x</code>、<code>-x</code>、<code>~x</code></td><td>一元运算</td></tr><tr><td></td><td><code>*</code>、<code>/</code>、<code>//</code>、<code>%</code></td><td>乘、除、整除、取余</td></tr><tr><td></td><td><code>+</code>、<code>-</code></td><td>加、减</td></tr><tr><td></td><td><code>&lt;</code>、<code>&lt;=</code>、<code>&gt;</code>、<code>&gt;=</code>、<code>==</code>、<code>!=</code>、<code>in</code>、<code>is</code></td><td>比较</td></tr><tr><td></td><td><code>not</code></td><td>逻辑非</td></tr><tr><td></td><td><code>and</code></td><td>逻辑与</td></tr><tr><td>最低</td><td><code>or</code></td><td>逻辑或</td></tr></tbody></table><p>例如 <code>3 + 2 * 4</code> 先算乘法；<code>3 ** 2 ** 3</code> 要看成 <code>3 ** (2 ** 3)</code>，所以结果是 6561。</p>

<h4>回到这道题</h4>

乘方优先于左侧负号，-2**4 等于 -(2**4)，结果为 -16。

<h4>容易出错的地方</h4>

<p>长表达式不要凭直觉从左往右算，先找括号，再按优先级分层。</p>

</div>

:::
:::: question judgment-6 | 1-6 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

第一句可以输出五个星号，第二句将 m 当作非法格式字符，不会自动读取变量。动态宽度可写 f'{s:^{m}}'。

<h4>容易出错的地方</h4>

<p>区分实际数值和显示形式；宽度是最小宽度，精度控制显示。</p>

</div>

:::
:::: question judgment-7 | 1-7 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序的输出是：这是字符串输出格式□□123。 □表示空格。

`print("这是字符串输出格式{:5s}".format("123"))`


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

字符串默认左对齐，实际是“这是字符串输出格式123□□”，空格在右侧。

<h4>容易出错的地方</h4>

<p>区分实际数值和显示形式；宽度是最小宽度，精度控制显示。</p>

</div>

:::
:::: question judgment-8 | 1-8 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面语句的输出是：这是数字输出格式$\Box$$\Box$123。 $\Box$表示空格  
`print("这是数字输出格式{:5d}".format(123))`


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

整数默认右对齐，宽度 5 而 123 长度为 3，左侧补两个空格。

<h4>容易出错的地方</h4>

<p>区分实际数值和显示形式；宽度是最小宽度，精度控制显示。</p>

</div>

:::
:::: question judgment-9 | 1-9 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

`int(True)`的返回值是1。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：布尔对象与“真假性”**

`True` 和 `False` 是布尔常量，转换成整数分别为 1 和 0。条件判断却不要求表达式本身一定是布尔对象：数值 0、`None`、空字符串及空容器是假值，大多数其他对象是真值。例如 `bool([])` 为假，而 `bool([0])` 为真，因为后者并不为空。

要区分 `False` 与字符串 `'False'`：后者有 5 个字符，是真值。同样，`0 == False` 为真不意味着它们类型相同，`type(0)` 为 `int`，`type(False)` 为 `bool`。未定义的名字 `FALSE` 会先触发 `NameError`，程序根本还没进入真假转换阶段。`None` 的判断通常写 `x is None`，用于区分“没有值”和合法的数值 0。

继续阅读：[第2章：布尔类型与空值](../topics/chapter-02.md)。



<h4>回到这道题</h4>

True 参与整数转换得到 1；False 转为 0。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question judgment-10 | 1-10 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

`bool(FALSE)`的返回值是True。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：标识符、关键字与内置名称**

入门题中常见的合法名字由字母、数字和下划线组成，不能以数字开头，且区分大小写。`item_1` 与 `_item` 合法；`1item` 不合法；`item-name` 会被当成减法表达式，而不是一个名字。Python 也允许部分 Unicode 字符用于标识符。

还要区分关键字和内置名称：`else`、`for` 是语法保留字，不能作普通变量名；`print`、`list` 不是关键字，给它们赋值在语法上合法，却会遮蔽原有功能。例如 `print=3` 后再执行 `print(5)`，是在调用整数，因而报 `TypeError`。布尔常量必须写作 `True`、`False`，大小写变化后会被当成别的名字。

继续阅读：[第1章：标识符和变量](../topics/chapter-01.md)。



<h4>回到这道题</h4>

Python 的布尔常量写作 False；未定义的 FALSE 会触发 NameError，不能直接求布尔值。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question judgment-11 | 1-11 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

`bool([])`的返回值是False。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：布尔对象与“真假性”**

`True` 和 `False` 是布尔常量，转换成整数分别为 1 和 0。条件判断却不要求表达式本身一定是布尔对象：数值 0、`None`、空字符串及空容器是假值，大多数其他对象是真值。例如 `bool([])` 为假，而 `bool([0])` 为真，因为后者并不为空。

要区分 `False` 与字符串 `'False'`：后者有 5 个字符，是真值。同样，`0 == False` 为真不意味着它们类型相同，`type(0)` 为 `int`，`type(False)` 为 `bool`。未定义的名字 `FALSE` 会先触发 `NameError`，程序根本还没进入真假转换阶段。`None` 的判断通常写 `x is None`，用于区分“没有值”和合法的数值 0。

继续阅读：[第2章：布尔类型与空值](../topics/chapter-02.md)。



<h4>回到这道题</h4>

空列表属于假值，bool([]) 为 False。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question judgment-12 | 1-12 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

`bool(None)`的返回值是False。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：布尔对象与“真假性”**

`True` 和 `False` 是布尔常量，转换成整数分别为 1 和 0。条件判断却不要求表达式本身一定是布尔对象：数值 0、`None`、空字符串及空容器是假值，大多数其他对象是真值。例如 `bool([])` 为假，而 `bool([0])` 为真，因为后者并不为空。

要区分 `False` 与字符串 `'False'`：后者有 5 个字符，是真值。同样，`0 == False` 为真不意味着它们类型相同，`type(0)` 为 `int`，`type(False)` 为 `bool`。未定义的名字 `FALSE` 会先触发 `NameError`，程序根本还没进入真假转换阶段。`None` 的判断通常写 `x is None`，用于区分“没有值”和合法的数值 0。

继续阅读：[第2章：布尔类型与空值](../topics/chapter-02.md)。



<h4>回到这道题</h4>

None 表示空值，布尔转换为 False。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question judgment-13 | 1-13 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

`print(bin(12.5))`的输出是`0b1100.1`


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

bin() 接受整数，不接受 12.5 这样的浮点数，会引发 TypeError。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question judgment-14 | 1-14 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

int("92",8)的值是74。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

八进制合法数字为 0～7，'92' 含有 9，int('92',8) 引发 ValueError。

<h4>容易出错的地方</h4>

<p>先确认源进制和目标进制，再选择 int、bin、oct、hex 等工具。</p>

</div>

:::
:::: question judgment-15 | 1-15 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式`3 and 0 and "hello"`的值是False。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

and 返回第一个为假的操作数，这里返回整数 0，而不是布尔对象 False；两者值比较相等但类型不同。

<h4>容易出错的地方</h4>

<p>and/or 会返回某个操作数，并可能因为短路而不计算右侧。</p>

</div>

:::
:::: question judgment-16 | 1-16 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

z已赋值，x=(y=z+1)语句是错误语句


::::

<h2 id="choice" class="quiz-group">单选题<span>12 QUESTIONS</span></h2>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：赋值、表达式与拆包顺序**

普通 `=` 是赋值语句，不是比较运算 `==`，不能直接嵌入 `x=(y=z+1)+1` 这种表达式。若两个名字都要接收同一个结果，可写 `x=y=z+1`。`i*=3+5` 要先求出整个右侧，数值情形下相当于 `i=i*(3+5)`，不是 `i=i*3+5`。

拆包赋值先求整个右侧，再从左到右赋给各目标。若旧 `t=1`，`t,a=2,t+1` 先得到右侧 `(2,2)`，所以 `a=2`；交换 `a,b=b,a` 也利用此规则。右侧必须可迭代且元素数量匹配：整数 34 不能直接拆成 3 和 4，字符串 `'3 4'` 则有 3 个字符，而不是两个数。

继续阅读：[第2章：赋值与拆包](../topics/chapter-02.md)。



<h4>回到这道题</h4>

普通赋值语句 y=z+1 不能嵌入表达式中。需要链式赋值可写 x=y=z+1。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-1 | 2-1 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

下列数据类型中， Python不支持的是_____________。

**A.** char

**B.** int

**C.** float

**D.** list


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：字符串是不可变的字符序列**

Python 没有单独的内置 `char` 类型，`'A'` 是长度为 1 的 `str`。字符串支持索引、切片、遍历、成员判断与长度查询，但不支持 `s[0]='B'` 这样的原地修改。要更改字符，可构造新字符串并重新赋值，例如 `s='B'+s[1:]`。

字符串的长度由对象记录，不依赖 `\0` 作为结束标志；`len('a\0b')` 为 3，中间的空字符也计入长度。`list('abc')` 会遍历字符串，生成 `['a','b','c']`；`['abc']` 则只含一个完整字符串。这个区别也适用于拆包和 `extend()`：传入字符串时，它通常被当成可逐字符遍历的序列。

继续阅读：[第3章：序列与字符串](../topics/chapter-03.md)。



<h4>回到这道题</h4>

Python 没有独立 char 类型，单个字符用长度为 1 的字符串表示。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-2 | 2-2 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句print(type(1J))的输出结果是______________。

**A.** `<class‘complex’>`

**B.** `<class ‘int’>`

**C.** `<class ‘float’>`

**D.** `<class ‘dict’>`


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

1J 是复数，type(1J) 为 complex。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-3 | 2-3 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句print(type(1/2))的输出结果是______________。

**A.** `<class ‘int’>`

**B.** `<class ‘number’>`

**C.** `<class ‘float’>`

**D.** `<class ‘double’>`


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：运算符决定值，也影响结果类型**

`int` 表示整数，`float` 表示浮点数，`complex` 表示复数，`bool` 是整数类型的子类。整数与浮点数进行常见算术运算时，结果通常转为浮点数；`/` 即使两侧都是整数，也执行普通除法，例如 `1/2` 为 `0.5`、`4/2` 为 `2.0`。

`//` 向负无穷取整，不是简单删除小数：`-3//2` 为 -2，而 `int(-3/2)` 为 -1。对于正除数，余数满足 `a == (a//b)*b + a%b`。`32.2//6` 的值虽然是整数大小的 5，但类型仍为 `float`，打印成 `5.0`；判断输出时必须同时跟踪数值与类型。

继续阅读：[第2章：数字类型](../topics/chapter-02.md)。



<h4>回到这道题</h4>

/ 执行普通除法，1/2 得到浮点数 0.5。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-4 | 2-4 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句print(type(1//2))的输出结果是______________。

**A.** `<class ‘int’>`

**B.** `<class ‘number’>`

**C.** `<class ‘float’>`

**D.** `<class ‘double’>`


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：运算符决定值，也影响结果类型**

`int` 表示整数，`float` 表示浮点数，`complex` 表示复数，`bool` 是整数类型的子类。整数与浮点数进行常见算术运算时，结果通常转为浮点数；`/` 即使两侧都是整数，也执行普通除法，例如 `1/2` 为 `0.5`、`4/2` 为 `2.0`。

`//` 向负无穷取整，不是简单删除小数：`-3//2` 为 -2，而 `int(-3/2)` 为 -1。对于正除数，余数满足 `a == (a//b)*b + a%b`。`32.2//6` 的值虽然是整数大小的 5，但类型仍为 `float`，打印成 `5.0`；判断输出时必须同时跟踪数值与类型。

继续阅读：[第2章：数字类型](../topics/chapter-02.md)。



<h4>回到这道题</h4>

两个整数进行 // 运算，1//2 得到整数 0。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-5 | 2-5 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 a=121+1.21; print(type(a))的输出结果是_____________。

**A.** `<class ‘int’>`

**B.** `<class ‘float’>`

**C.** `<class ‘double’>`

**D.** `<class ‘long’>`


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：运算符决定值，也影响结果类型**

`int` 表示整数，`float` 表示浮点数，`complex` 表示复数，`bool` 是整数类型的子类。整数与浮点数进行常见算术运算时，结果通常转为浮点数；`/` 即使两侧都是整数，也执行普通除法，例如 `1/2` 为 `0.5`、`4/2` 为 `2.0`。

`//` 向负无穷取整，不是简单删除小数：`-3//2` 为 -2，而 `int(-3/2)` 为 -1。对于正除数，余数满足 `a == (a//b)*b + a%b`。`32.2//6` 的值虽然是整数大小的 5，但类型仍为 `float`，打印成 `5.0`；判断输出时必须同时跟踪数值与类型。

继续阅读：[第2章：数字类型](../topics/chapter-02.md)。



<h4>回到这道题</h4>

整数和浮点数相加得到浮点数，121+1.21 为 float。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-6 | 2-6 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 print(0xA + 0xB)的输出结果是______________。

**A.** 0xA + 0xB

**B.** A + B

**C.** 0xA0xB

**D.** 21


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

0xA 为 10，0xB 为 11，相加得到十进制整数 21。

<h4>容易出错的地方</h4>

<p>先确认源进制和目标进制，再选择 int、bin、oct、hex 等工具。</p>

</div>

:::
:::: question choice-7 | 2-7 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句x=’car’; y = 2; print (x+y)的输出结果是____________。

**A.** 语法错

**B.** 2

**C.** 'car2’

**D.** 'carcar’


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

无严格正确选项；按普通引号还原后为运行时 `TypeError`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：同一个运算符对不同类型有不同含义**

对数字，`+` 表示加法；对字符串，表示拼接；对列表，表示连接两边的元素。例如 `2+3` 为 5，`'2'+'3'` 为 `'23'`，`[2]+[3]` 为 `[2,3]`。Python 不会为了完成拼接自动把整数变成字符串，所以 `'age'+23` 在运行时产生 `TypeError`。

若要拼接，使用 `'age'+str(23)` 或 `f'age{23}'`；若要计算，使用 `int('23')+1`。二者目的不同，不能随意选择一种转换。还要把语法阶段和执行阶段分开：正常引号下的字符串加整数，能通过语法解析；弯引号 `“ ”` 不是 Python 字符串定界符，原样输入会先出现语法错误。

继续阅读：[第2章：字符串与类型转换](../topics/chapter-02.md)。



<h4>回到这道题</h4>

题面使用弯引号，原样作为 Python 代码会产生 SyntaxError；若按普通字符串引号理解，字符串 car 与整数 2 相加会产生 TypeError，不能称为语法错误。A 仅在原样弯引号情形下适用。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-8 | 2-8 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式1+2*3.14>0的结果类型是:

**A.** int

**B.** long

**C.** float

**D.** bool


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：布尔对象与“真假性”**

`True` 和 `False` 是布尔常量，转换成整数分别为 1 和 0。条件判断却不要求表达式本身一定是布尔对象：数值 0、`None`、空字符串及空容器是假值，大多数其他对象是真值。例如 `bool([])` 为假，而 `bool([0])` 为真，因为后者并不为空。

要区分 `False` 与字符串 `'False'`：后者有 5 个字符，是真值。同样，`0 == False` 为真不意味着它们类型相同，`type(0)` 为 `int`，`type(False)` 为 `bool`。未定义的名字 `FALSE` 会先触发 `NameError`，程序根本还没进入真假转换阶段。`None` 的判断通常写 `x is None`，用于区分“没有值”和合法的数值 0。

继续阅读：[第2章：布尔类型与空值](../topics/chapter-02.md)。



<h4>回到这道题</h4>

比较运算 > 的结果类型为 bool。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-9 | 2-9 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

如math模块已引入，Python 表达式 `math.sqrt(4)*math.sqrt(9)`的值为________。

**A.** 36.0

**B.** 6

**C.** 13

**D.** 6.0


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：数学公式如何翻译成 Python**

先识别公式的运算结构，再选择函数。平方根用 `math.sqrt()`，自然对数用 `math.log()`，指数 $e^x$ 用 `math.exp()`；乘法必须明确写 `*`，分式的分子、分母需要分别加括号。`sqrt(4)` 返回 `2.0`，所以后续乘积可能是浮点数而不是整数。

三角函数参数以弧度为单位，角度先用 `math.radians()` 转换。还要检查定义域：实数平方根的参数不能为负，自然对数参数必须大于 0，分母不能为 0。输出格式化只控制最后显示多少位，并不修复公式、定义域或中间计算的错误。`ceil()` 向上取整，`floor()` 向下取整，均与向零截断的 `int()` 有区别。

继续阅读：[第2章：math 库](../topics/chapter-02.md)。



<h4>回到这道题</h4>

sqrt(4)=2.0，sqrt(9)=3.0，乘积为浮点数 6.0。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-10 | 2-10 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

关于Python中的复数，下列说法错误的是___________。

**A.** 表示复数的语法是real + imag j

**B.** 实部和虚部都是浮点数

**C.** 虚部必须后缀j, 且必须是小写

**D.** 方法conjugate 返回复数的共轭复数


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

复数虚部后缀可以为 j 或 J，如 1J 合法。实部、虚部属性为浮点数，调用 conjugate() 得到共轭复数。选项 A 是概念示意，实际代码不能在数字与 j 之间插入空格。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-11 | 2-11 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 print(chr(65))的运行结果是___________。

**A.** 65

**B.** 6

**C.** 5

**D.** A


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：字符、码点与字节编码**

Unicode 为字符分配码点，例如 `ord('A')` 为 65，`ord('张')` 为 24352；`chr()` 完成反向转换。`U+5F20` 和十进制 24352 表示同一码点，只是记数方式不同。`ord()` 接收单个字符，不能直接把整个多字符字符串转换成一个码点。

UTF-8 则规定如何把码点编码成字节，不能把它和 Unicode 字符集合混为一谈。例如 `len('张')` 为 1，而 `len('张'.encode('utf-8'))` 为 3；前者数 Python 字符串中的码点，后者数字节。ASCII 字符在 UTF-8 中仍占一个字节，这也是英文字符 A 的编码值在本题中保持 65 的原因。

继续阅读：[第1章：字符编码](../topics/chapter-01.md)。



<h4>回到这道题</h4>

chr(65) 返回字符 A。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question choice-12 | 2-12 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

关于Python字符串，下列说法错误的是___________。

**A.** 字符即长度为1的字符串

**B.** 字符串以\0标志字符串的结束

**C.** 既可以用单引号，也可以用双引号创建字符串

**D.** 在三引号字符串中可以包含换行回车等特殊字符


::::

<h2 id="blank" class="quiz-group">填空题<span>21 QUESTIONS</span></h2>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：字符串是不可变的字符序列**

Python 没有单独的内置 `char` 类型，`'A'` 是长度为 1 的 `str`。字符串支持索引、切片、遍历、成员判断与长度查询，但不支持 `s[0]='B'` 这样的原地修改。要更改字符，可构造新字符串并重新赋值，例如 `s='B'+s[1:]`。

字符串的长度由对象记录，不依赖 `\0` 作为结束标志；`len('a\0b')` 为 3，中间的空字符也计入长度。`list('abc')` 会遍历字符串，生成 `['a','b','c']`；`['abc']` 则只含一个完整字符串。这个区别也适用于拆包和 `extend()`：传入字符串时，它通常被当成可逐字符遍历的序列。

继续阅读：[第3章：序列与字符串](../topics/chapter-03.md)。



<h4>回到这道题</h4>

Python 字符串不依赖空字符 \0 表示结束，长度由字符串对象记录。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question blank-1 | 4-1 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 表达式 10 + 5//3 –True+False的值为 _____ .


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`10`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<h4>Python 常见运算符优先级</h4><p>下面从高到低列出本课程常见的运算符。括号可以明确改变分组；同一层通常从左到右计算，乘方 <code>**</code> 是重要例外，它从右向左结合。</p><table><thead><tr><th>优先级</th><th>运算符</th><th>作用</th></tr></thead><tbody><tr><td>最高</td><td><code>(...)</code></td><td>括号</td></tr><tr><td></td><td><code>**</code></td><td>乘方</td></tr><tr><td></td><td><code>+x</code>、<code>-x</code>、<code>~x</code></td><td>一元运算</td></tr><tr><td></td><td><code>*</code>、<code>/</code>、<code>//</code>、<code>%</code></td><td>乘、除、整除、取余</td></tr><tr><td></td><td><code>+</code>、<code>-</code></td><td>加、减</td></tr><tr><td></td><td><code>&lt;</code>、<code>&lt;=</code>、<code>&gt;</code>、<code>&gt;=</code>、<code>==</code>、<code>!=</code>、<code>in</code>、<code>is</code></td><td>比较</td></tr><tr><td></td><td><code>not</code></td><td>逻辑非</td></tr><tr><td></td><td><code>and</code></td><td>逻辑与</td></tr><tr><td>最低</td><td><code>or</code></td><td>逻辑或</td></tr></tbody></table><p>例如 <code>3 + 2 * 4</code> 先算乘法；<code>3 ** 2 ** 3</code> 要看成 <code>3 ** (2 ** 3)</code>，所以结果是 6561。</p>

<h4>回到这道题</h4>

按运算优先级先算 5//3=1，再计算 10+1-1+0=10；题面的长横线按减号理解。

<h4>容易出错的地方</h4>

<p>长表达式不要凭直觉从左往右算，先找括号，再按优先级分层。</p>

</div>

:::
:::: question blank-2 | 4-2 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 表达式 3**2**3 的值为 _____


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`6561`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<h4>Python 常见运算符优先级</h4><p>下面从高到低列出本课程常见的运算符。括号可以明确改变分组；同一层通常从左到右计算，乘方 <code>**</code> 是重要例外，它从右向左结合。</p><table><thead><tr><th>优先级</th><th>运算符</th><th>作用</th></tr></thead><tbody><tr><td>最高</td><td><code>(...)</code></td><td>括号</td></tr><tr><td></td><td><code>**</code></td><td>乘方</td></tr><tr><td></td><td><code>+x</code>、<code>-x</code>、<code>~x</code></td><td>一元运算</td></tr><tr><td></td><td><code>*</code>、<code>/</code>、<code>//</code>、<code>%</code></td><td>乘、除、整除、取余</td></tr><tr><td></td><td><code>+</code>、<code>-</code></td><td>加、减</td></tr><tr><td></td><td><code>&lt;</code>、<code>&lt;=</code>、<code>&gt;</code>、<code>&gt;=</code>、<code>==</code>、<code>!=</code>、<code>in</code>、<code>is</code></td><td>比较</td></tr><tr><td></td><td><code>not</code></td><td>逻辑非</td></tr><tr><td></td><td><code>and</code></td><td>逻辑与</td></tr><tr><td>最低</td><td><code>or</code></td><td>逻辑或</td></tr></tbody></table><p>例如 <code>3 + 2 * 4</code> 先算乘法；<code>3 ** 2 ** 3</code> 要看成 <code>3 ** (2 ** 3)</code>，所以结果是 6561。</p>

<h4>回到这道题</h4>

乘方从右向左结合：3**(2**3)=3**8=6561。

<h4>容易出错的地方</h4>

<p>长表达式不要凭直觉从左往右算，先找括号，再按优先级分层。</p>

</div>

:::
:::: question blank-3 | 4-3 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 表达式 round(17.0/3**2,2) 的值为 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`1.89`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：浮点近似与最终显示**

多数十进制小数不能被二进制浮点数精确表示，计算机保存的是附近的可表示值。因此 `round()` 或 `.2f` 格式化所处理的，可能并不是纸面上那个精确的十进制数。遇到 14.345 一类边界值，不能机械地按十进制“第三位是 5”判断结果。

即使没有表示误差，Python 的 `round()` 在恰好居中时也采用向偶数舍入，而不是一律进位：`round(2.5)` 为 2，`round(3.5)` 为 4。格式化返回字符串，`round(x,2)` 返回数值，不保证显示末尾的零。若业务要求精确十进制及指定舍入规则，应从原始文本构造 `Decimal` 并明确舍入方式；不要先转成 `float` 再期望恢复精确输入。

继续阅读：[第2章：数字类型与格式化输出](../topics/chapter-02.md)。



<h4>回到这道题</h4>

3**2=9，17.0/9≈1.8888889，round(...,2) 得到 1.89。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question blank-4 | 4-4 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 表达式 0 and 1 or not 2&lt;True 的值为 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

先计算 2<True，即 2<1，为假；not 后为真。0 and 1 得到 0，再与 True 做 or 得到 True。

<h4>容易出错的地方</h4>

<p>and/or 会返回某个操作数，并可能因为短路而不计算右侧。</p>

</div>

:::
:::: question blank-5 | 4-5 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 print(int("20", 16), int("101",2))的输出结果是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`32 5`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

十六进制 20 为十进制 32，二进制 101 为 5；print 在参数间添加一个空格。

<h4>容易出错的地方</h4>

<p>先确认源进制和目标进制，再选择 int、bin、oct、hex 等工具。</p>

</div>

:::
:::: question blank-6 | 4-6 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 print(hex(16), bin(10))的输出结果是(进制用小写字母表示） _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`0x10 0b1010`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

hex()、bin() 返回带小写前缀的字符串。

<h4>容易出错的地方</h4>

<p>先确认源进制和目标进制，再选择 int、bin、oct、hex 等工具。</p>

</div>

:::
:::: question blank-7 | 4-7 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

已知 a=3; b=5; c=6; d=True, 则表达式 not d or a>=0 and a+c>b+3的值是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

not d 为假，a>=0 为真，a+c=9>b+3=8 为真，整体为 True。

<h4>容易出错的地方</h4>

<p>and/or 会返回某个操作数，并可能因为短路而不计算右侧。</p>

</div>

:::
:::: question blank-8 | 4-8 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 print(abs(-10.2), round(abs(8-2j),3)) 的输出结果是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`10.2 8.246`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

abs(-10.2)=10.2；复数的模为 sqrt(8²+(-2)²)=sqrt(68)，保留 3 位小数为 8.246。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question blank-9 | 4-9 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 x=True; y=False; z=False; print(x or y and z)的程序运行结果是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

and 优先于 or，先得 y and z=False，再计算 True or False。

<h4>容易出错的地方</h4>

<p>and/or 会返回某个操作数，并可能因为短路而不计算右侧。</p>

</div>

:::
:::: question blank-10 | 4-10 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 语句 x=0; y= True; print(x>=y and‘A'&lt;'B') 的程序运行结果是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`False`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

x>=y 相当于 0>=1，为假，and 短路，结果为 False。题面弯引号按普通引号理解。

<h4>容易出错的地方</h4>

<p>and/or 会返回某个操作数，并可能因为短路而不计算右侧。</p>

</div>

:::
:::: question blank-11 | 4-11 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python 表达式 16-25>78/2 or "XYZ"!="xyz"and not (10-6>18/2)的值是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

第一项比较为假；XYZ 与 xyz 不同为真，10-6>18/2 为假，取反为真，因此右侧合取为真。

<h4>容易出错的地方</h4>

<p>and/or 会返回某个操作数，并可能因为短路而不计算右侧。</p>

</div>

:::
:::: question blank-12 | 4-12 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

Python输出 print("hello" 'world')的结果是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`helloworld`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

相邻的字符串字面量在编译时自动拼接，源码中的空格不属于字符串内容。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question blank-13 | 4-13 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式((2>=2) or (2&lt;2)) and 2的值为多少？ _____


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`2`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

括号内 or 得到 True，True and 2 返回右侧整数 2。

<h4>容易出错的地方</h4>

<p>and/or 会返回某个操作数，并可能因为短路而不计算右侧。</p>

</div>

:::
:::: question blank-14 | 4-14 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式 3 and 0 and 5的结果是什么？。 _____


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`0`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：短路求值不是只算 True 或 False**

`x and y` 先检查 `x`：若它是假值，直接返回 `x`；否则继续求值并返回 `y`。`x or y` 则在 `x` 为真值时直接返回 `x`，否则返回 `y`。它们返回的是操作数，所以 `3 and 0 and 5` 返回整数 0，`True and 2` 返回整数 2。只有 `not` 总返回布尔值。

```python
print(0 and 1 / 0)     # 0：右侧根本不执行
print('' or 'default') # default
print(not [])         # True
```

长表达式先算算术和比较，再按 `not`、`and`、`or` 的优先级组合；建议在纸上标出每个子式的值与类型。短路也常用于保护操作，例如 `n != 0 and total/n > 2`。用 `x or 默认值` 时要确认 0、空串等合法输入是否也应被替换，不能把它等同于“只有 None 才替换”。

继续阅读：[第2章：逻辑运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

and 短路并返回遇到的假值 0，不继续检查 5。

<h4>容易出错的地方</h4>

<p>and/or 会返回某个操作数，并可能因为短路而不计算右侧。</p>

</div>

:::
:::: question blank-15 | 4-15 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式 --3 的结果是什么？ _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`3`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<h4>Python 常见运算符优先级</h4><p>下面从高到低列出本课程常见的运算符。括号可以明确改变分组；同一层通常从左到右计算，乘方 <code>**</code> 是重要例外，它从右向左结合。</p><table><thead><tr><th>优先级</th><th>运算符</th><th>作用</th></tr></thead><tbody><tr><td>最高</td><td><code>(...)</code></td><td>括号</td></tr><tr><td></td><td><code>**</code></td><td>乘方</td></tr><tr><td></td><td><code>+x</code>、<code>-x</code>、<code>~x</code></td><td>一元运算</td></tr><tr><td></td><td><code>*</code>、<code>/</code>、<code>//</code>、<code>%</code></td><td>乘、除、整除、取余</td></tr><tr><td></td><td><code>+</code>、<code>-</code></td><td>加、减</td></tr><tr><td></td><td><code>&lt;</code>、<code>&lt;=</code>、<code>&gt;</code>、<code>&gt;=</code>、<code>==</code>、<code>!=</code>、<code>in</code>、<code>is</code></td><td>比较</td></tr><tr><td></td><td><code>not</code></td><td>逻辑非</td></tr><tr><td></td><td><code>and</code></td><td>逻辑与</td></tr><tr><td>最低</td><td><code>or</code></td><td>逻辑或</td></tr></tbody></table><p>例如 <code>3 + 2 * 4</code> 先算乘法；<code>3 ** 2 ** 3</code> 要看成 <code>3 ** (2 ** 3)</code>，所以结果是 6561。</p>

<h4>回到这道题</h4>

两次一元负号相互抵消。

<h4>容易出错的地方</h4>

<p>长表达式不要凭直觉从左往右算，先找括号，再按优先级分层。</p>

</div>

:::
:::: question blank-16 | 4-16 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式 ---3 的结果是什么？ _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`-3`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：优先级、结合方向与一元运算**

计算表达式时先列出括号，再处理乘方、乘除与整除求余、加减，最后处理比较和逻辑运算。同一层大多从左到右，但乘方从右向左结合：`3**2**3` 是 `3**(2**3)`，不是 `(3**2)**3`。

乘方与负号相邻时需特别注意：`-2**4` 是 `-(2**4)=-16`，`(-2)**4` 才是 16；右侧指数可以写负号，如 `2**-2=0.25`。Python 没有 `++` 自增运算，`++i` 只是两次一元正号，`--i` 是两次一元负号，都不会更新变量；真正增加 1 应写 `i+=1`。不要把其他语言的符号含义直接套到 Python。

继续阅读：[第2章：数字运算与语句](../topics/chapter-02.md)。

<h4>Python 常见运算符优先级</h4><p>下面从高到低列出本课程常见的运算符。括号可以明确改变分组；同一层通常从左到右计算，乘方 <code>**</code> 是重要例外，它从右向左结合。</p><table><thead><tr><th>优先级</th><th>运算符</th><th>作用</th></tr></thead><tbody><tr><td>最高</td><td><code>(...)</code></td><td>括号</td></tr><tr><td></td><td><code>**</code></td><td>乘方</td></tr><tr><td></td><td><code>+x</code>、<code>-x</code>、<code>~x</code></td><td>一元运算</td></tr><tr><td></td><td><code>*</code>、<code>/</code>、<code>//</code>、<code>%</code></td><td>乘、除、整除、取余</td></tr><tr><td></td><td><code>+</code>、<code>-</code></td><td>加、减</td></tr><tr><td></td><td><code>&lt;</code>、<code>&lt;=</code>、<code>&gt;</code>、<code>&gt;=</code>、<code>==</code>、<code>!=</code>、<code>in</code>、<code>is</code></td><td>比较</td></tr><tr><td></td><td><code>not</code></td><td>逻辑非</td></tr><tr><td></td><td><code>and</code></td><td>逻辑与</td></tr><tr><td>最低</td><td><code>or</code></td><td>逻辑或</td></tr></tbody></table><p>例如 <code>3 + 2 * 4</code> 先算乘法；<code>3 ** 2 ** 3</code> 要看成 <code>3 ** (2 ** 3)</code>，所以结果是 6561。</p>

<h4>回到这道题</h4>

三次一元负号，最终为负。

<h4>容易出错的地方</h4>

<p>长表达式不要凭直觉从左往右算，先找括号，再按优先级分层。</p>

</div>

:::
:::: question blank-17 | 4-17 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式`32.2//6-24//6`的值是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`1.0`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：运算符决定值，也影响结果类型**

`int` 表示整数，`float` 表示浮点数，`complex` 表示复数，`bool` 是整数类型的子类。整数与浮点数进行常见算术运算时，结果通常转为浮点数；`/` 即使两侧都是整数，也执行普通除法，例如 `1/2` 为 `0.5`、`4/2` 为 `2.0`。

`//` 向负无穷取整，不是简单删除小数：`-3//2` 为 -2，而 `int(-3/2)` 为 -1。对于正除数，余数满足 `a == (a//b)*b + a%b`。`32.2//6` 的值虽然是整数大小的 5，但类型仍为 `float`，打印成 `5.0`；判断输出时必须同时跟踪数值与类型。

继续阅读：[第2章：数字类型](../topics/chapter-02.md)。



<h4>回到这道题</h4>

32.2//6 为 5.0，24//6 为 4，差为浮点数 1.0。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question blank-18 | 4-18 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`25`；`yes`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

各位按权重 1、2、4、8、16 累加。10011 对应 1+8+16=25；生日 19 对应 11001，各列表分别表示一个二进制位，故可还原。

<h4>容易出错的地方</h4>

<p>先确认源进制和目标进制，再选择 int、bin、oct、hex 等工具。</p>

</div>

:::
:::: question blank-19 | 4-19 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

汉字`张`的Unicode编码是 _____ 。


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`24352`（十六进制 `U+5F20`）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：字符、码点与字节编码**

Unicode 为字符分配码点，例如 `ord('A')` 为 65，`ord('张')` 为 24352；`chr()` 完成反向转换。`U+5F20` 和十进制 24352 表示同一码点，只是记数方式不同。`ord()` 接收单个字符，不能直接把整个多字符字符串转换成一个码点。

UTF-8 则规定如何把码点编码成字节，不能把它和 Unicode 字符集合混为一谈。例如 `len('张')` 为 1，而 `len('张'.encode('utf-8'))` 为 3；前者数 Python 字符串中的码点，后者数字节。ASCII 字符在 UTF-8 中仍占一个字节，这也是英文字符 A 的编码值在本题中保持 65 的原因。

继续阅读：[第1章：字符编码](../topics/chapter-01.md)。



<h4>回到这道题</h4>

ord('张') 得到十进制 24352；若要求 Unicode 码点形式，则写 U+5F20。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question blank-20 | 4-20 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

```python
-7 & 5 的结果是_____ 。
-7 | 9  的结果是_____。
-7 ^ 9 的结果是_____。
 ~9 的结果是_____
```


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`1`、`-7`、`-16`、`-10`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：按位运算与数位统计**

先把整数对齐为二进制位，再逐位计算：`&` 仅在两位都为 1 时得 1，`|` 有一位为 1 就得 1，`^` 仅在两位不同时得 1。因此 `x^y` 中的 1 的个数，就是两个非负整数二进制表示的不同位数。`^` 不是乘方，乘方要写 `**`。

负整数按符号扩展的补码语义处理，可以选足够宽的位数手算，但不能把最高位截掉后当成无符号数。取反满足 `~x == -x-1`，例如 `~9=-10`。统计二进制 1 的数量可用 `bin(n).count('1')`，而统计总位数时，0 和负数的符号、前缀需要另行分析。本节按课程范围说明保留，不代表新增考试要求。

继续阅读：[第2章：位运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

负整数位运算按符号扩展的补码理解。分别计算 -7&5、-7|9、-7^9；取反满足 ~9=-9-1=-10。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question blank-21 | 4-21 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序输出是 _____ 。

```python
n = 39
remainders = []
while n>0:
    n,remainder = divmod(n,2)
    remainders.insert(0,remainder)
print(len(remainders))

```


::::

<h2 id="programming" class="quiz-group">编程题<span>14 QUESTIONS</span></h2>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`6`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：按位运算与数位统计**

先把整数对齐为二进制位，再逐位计算：`&` 仅在两位都为 1 时得 1，`|` 有一位为 1 就得 1，`^` 仅在两位不同时得 1。因此 `x^y` 中的 1 的个数，就是两个非负整数二进制表示的不同位数。`^` 不是乘方，乘方要写 `**`。

负整数按符号扩展的补码语义处理，可以选足够宽的位数手算，但不能把最高位截掉后当成无符号数。取反满足 `~x == -x-1`，例如 `~9=-10`。统计二进制 1 的数量可用 `bin(n).count('1')`，而统计总位数时，0 和负数的符号、前缀需要另行分析。本节按课程范围说明保留，不代表新增考试要求。

继续阅读：[第2章：位运算](../topics/chapter-02.md)。



<h4>回到这道题</h4>

39 的二进制为 100111，共 6 位，循环每次处理一个二进制位。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-1 | 7-1 计算 11+12+13+...+m

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m = int(input())
print(f'sum = {sum(range(11, m + 1))}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：range 的边界与循环结束状态**

`range(start,stop,step)` 包含起点，不包含终点；正步长要求当前值小于终点，负步长要求当前值大于终点。因此 `range(10,0,-2)` 是 10、8、6、4、2。若需要正向包含 n，常写 `range(1,n+1)`。步长为 0 会报错。

`for` 每次从可迭代对象取下一项，再赋给循环变量，结束时不会额外执行一次加减。循环体若未重赋该变量，非空遍历结束后它保留最后取到的值。空范围一次也不执行，若变量此前未定义，循环后访问它会报错。分析图形或序列和题时，先把小规模的取值逐个列出，再检查首项、末项和步长，能有效避免多算或少算一项。

继续阅读：[第4章：for 循环](../topics/chapter-04.md)。



<h4>回到这道题</h4>

range 终点取 m+1，保证包含 m，输出等号两侧各一个空格。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-2 | 7-2 计算分段函数

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
x = float(input())
result = 0 if x == 0 else 1 / (2 * x)
print(f'g({x:.3f}) = {result:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

x=0 时单独处理，避免除零；其他情况计算 1/(2x)，两个数都保留三位小数。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-3 | 7-3 阶梯电价

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
usage, extra = map(float, input().split())
cost = min(usage, 50) * 0.53 + max(usage - 50, 0) * (0.53 + extra)
print(f'cost = {cost:.2f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

前 50 度按基础单价收费，只有超过的部分加价；结果格式化为两位小数。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-4 | 7-4 求奇数分之一序列前N项近似和

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

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





<h4>回到这道题</h4>

第 i 项为 1/(2i-1)，累加后向上取整。使用 Fraction 避免整数边界附近的浮点累加误差。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-5 | 7-5 求交错序列前N项和

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
total = sum((-1) ** (i - 1) * i / (2 * i - 1) for i in range(1, n + 1))
print(f'{total:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>





<h4>回到这道题</h4>

第 i 项的分子为 i，分母为 2i-1，符号为 (-1) 的 i-1 次方；输出保留三位小数。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-6 | 7-6 产生每位数字相同的n位数

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a, b = map(int, input().replace(',', ' ').split())
print(int(str(a) * b))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

按样例兼容逗号及两侧空格，重复数字字符串 B 次，再按整数输出。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-7 | 7-7 转换函数使用

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
digits, base = input().replace(',', ' ').split()
print(int(digits, int(base)))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

保留第一个输入为字符串，再交给 int(字符串,基数) 解析，不能先按十进制转掉。

<h4>容易出错的地方</h4>

<p>先确认源进制和目标进制，再选择 int、bin、oct、hex 等工具。</p>

</div>

:::
:::: question programming-8 | 7-8 比较大小

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
numbers = sorted(map(int, input().split()))
print('<'.join(chr(n) for n in numbers))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：排序的对象、顺序与返回值**

`sorted(items)` 返回新的已排序列表，原对象不变；`a.sort()` 原地修改列表并返回 `None`。要降序使用 `reverse=True`。`max()` 只取最大元素，不返回排序后的完整序列，空序列且无默认值时还会报错。

排序前先确定按什么比较：整数 `[2,10]` 排成 `[2,10]`，字符串 `['2','10']` 则排成 `['10','2']`。若题意是按数值大小，必须先转成数值再排序，最后再转回字符串用于输出。`random.shuffle(a)` 也原地修改列表并返回 `None`，但它是打乱，不是排序；不要写 `a=random.shuffle(a)`。

继续阅读：[第3章：列表方法](../topics/chapter-03.md)与[第4章：搜索和排序](../topics/chapter-04.md)。



<h4>回到这道题</h4>

先按码点从小到大排序，用 chr 转字符，再以 < 连接，不加空格。

<h4>容易出错的地方</h4>

<p>先确认比较的是数字还是字符串，再确认升降序，并注意 sort 与 sorted 的返回值。</p>

</div>

:::
:::: question programming-9 | 7-9 输出摄氏-华氏温度转换表

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

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

**从本题理解：range 的边界与循环结束状态**

`range(start,stop,step)` 包含起点，不包含终点；正步长要求当前值小于终点，负步长要求当前值大于终点。因此 `range(10,0,-2)` 是 10、8、6、4、2。若需要正向包含 n，常写 `range(1,n+1)`。步长为 0 会报错。

`for` 每次从可迭代对象取下一项，再赋给循环变量，结束时不会额外执行一次加减。循环体若未重赋该变量，非空遍历结束后它保留最后取到的值。空范围一次也不执行，若变量此前未定义，循环后访问它会报错。分析图形或序列和题时，先把小规模的取值逐个列出，再检查首项、末项和步长，能有效避免多算或少算一项。

继续阅读：[第4章：for 循环](../topics/chapter-04.md)。



<h4>回到这道题</h4>

先验证范围。每次摄氏度递增 2；华氏数值占 14 字符宽度，右对齐并保留一位小数。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-10 | 7-10 偶数位特殊序列和

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a, n = map(int, input().split())
print(sum(int(str(a) * width) for width in range(2, n + 1, 2)))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>





<h4>回到这道题</h4>

长度依次取 2、4、…、n，分别构造对应的重复数字整数并求和。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-11 | 7-11 求平方与倒数序列的近似和

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


::::

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





<h4>回到这道题</h4>

每项为 i²+1/i，求和后按题目提示 floor 向下取整。Fraction 保留精确值，避免例如 m=n=1 时的浮点误差。题面“小于”与 floor 在整数处不同，此处采用提示的 floor 定义。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-12 | 7-12 计算函数f(x)

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


::::

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

**从本题理解：数学公式如何翻译成 Python**

先识别公式的运算结构，再选择函数。平方根用 `math.sqrt()`，自然对数用 `math.log()`，指数 $e^x$ 用 `math.exp()`；乘法必须明确写 `*`，分式的分子、分母需要分别加括号。`sqrt(4)` 返回 `2.0`，所以后续乘积可能是浮点数而不是整数。

三角函数参数以弧度为单位，角度先用 `math.radians()` 转换。还要检查定义域：实数平方根的参数不能为负，自然对数参数必须大于 0，分母不能为 0。输出格式化只控制最后显示多少位，并不修复公式、定义域或中间计算的错误。`ceil()` 向上取整，`floor()` 向下取整，均与向零截断的 `int()` 有区别。

继续阅读：[第2章：math 库](../topics/chapter-02.md)。



<h4>回到这道题</h4>

图中 sin(35°) 需先将角度转弧度；分母为 sqrt(x⁴+1)，ln 用 math.log。x 按 float 输出，函数值保留三位小数。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-13 | 7-13 分段计算居民水费

<div class="section-label">题干 <span>QUESTION</span></div>

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
x = float(input())
y = 4 * x / 3 if x <= 15 else 2.5 * x - 17.5
print(f'{y:.2f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

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



<h4>回到这道题</h4>

15 吨及以下用第一段，超过 15 吨用第二段；在边界处两段都为 20 元。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
:::: question programming-14 | 7-14 输出指定图形

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


::::

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
for i in range(1, n + 1):
    print('* ' * i)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**从本题理解：把图形拆成行号和行内规律**

先确定第 i 行由哪几段组成，再决定循环。星号三角形常见规律是第 i 行有 i 个星号；等腰数字图形则可以拆成左侧空格、递增段和递减段。最高值只出现一次，所以递减段从 i-1 开始，而不是再次从 i 开始。

假设所有数字都占一个字符，峰值为 i 的回文数字行宽为 `2*i-1`，最终行峰值为 n，则左侧空格数是 n-i。若数字可能达到两位，必须重新核对题目限制和实际字符宽度，不能继续套单字符公式。输出前用小输入手算每行的前导空格、分隔符、行尾空格和换行；不要用网页里看起来相近的形状替代精确字符比较。

继续阅读：[第4章：for 循环](../topics/chapter-04.md)。



<h4>回到这道题</h4>

每行输出 i 个星号，每个星号后一个空格，保留该作业原始样例的行尾空格。

<h4>容易出错的地方</h4>

<p>先把题目中的术语翻译成具体的 Python 对象或操作，再一步一步跟踪结果。</p>

</div>

:::
