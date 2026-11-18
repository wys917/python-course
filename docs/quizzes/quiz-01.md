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

在Python中，可以用else作为变量名。

<div class="question-tags"><span class="question-tag">关键字</span> <span class="question-tag">变量命名</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

else 是关键字，不能用作变量名。

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

A 的 ASCII 编码和 Unicode 码点都是 65。

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

++i 不是自增，只是两次一元正号，i 保持 3；脚本也不会自动输出表达式。

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

int('10.0') 引发 ValueError，应使用 float() 读取小数。

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

字符串默认左对齐，两个补齐空格应位于 123 右侧。

</div>

:::

::::

:::: question judgment-6 | 1-6 判断题

下面语句的输出是：这是数字输出格式$\Box$$\Box$123。 $\Box$表示空格  
`print("这是数字输出格式{:5d}".format(123))`

<div class="question-tags"><span class="question-tag">字符串格式化</span> <span class="question-tag">右对齐</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

整数默认右对齐，宽度 5 时在 123 左边补两个空格。

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

None 的布尔值为 False。

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

bin() 不接受浮点数 12.5，会产生 TypeError。

</div>

:::

::::

:::: question judgment-9 | 1-9 判断题

int("92",8)的值是74。

<div class="question-tags"><span class="question-tag">int函数</span> <span class="question-tag">八进制转换</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

八进制没有数码 9，int('92',8) 会产生 ValueError。

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

结果是整数 0，and 返回操作数，不是布尔对象 False。

</div>

:::

::::

:::: question judgment-11 | 1-11 判断题

z已赋值，x=(y=z+1)语句是错误语句

<div class="question-tags"><span class="question-tag">赋值语句</span> <span class="question-tag">链式赋值</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

赋值语句不能放在这种表达式位置，应写 x=y=z+1。

</div>

:::

::::

:::: question judgment-12 | 1-12 判断题

print(("12 "*3).strip()==" ".join(["12","12","12"]))的输出结果是True

<div class="question-tags"><span class="question-tag">strip方法</span> <span class="question-tag">join方法</span> <span class="question-tag">字符串比较</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

strip() 去掉重复字符串末尾的空格后，两侧都得到 12 12 12。

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

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先原地排序，再遍历列表，顺序为 a、c、d、e；print(end=" ") 还会在最后保留一个空格。

</div>

:::

::::

:::: question judgment-14 | 1-14 判断题

[4,5]`*`3的结果是[4,5],[4,5],[4,5]。

<div class="question-tags"><span class="question-tag">列表重复</span> <span class="question-tag">序列嵌套</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

[4,5]*3 得到单个列表 [4,5,4,5,4,5]，不会生成三个子列表或元组。

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

Python 脚本文件通常以 .py 结尾。

</div>

:::

::::

:::: question choice-2 | 2-8 单选题

_______号表示同一行的后面部分是Python程序的注释。

**A.** *

**B.** %

**C.** /

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

半角 # 引出同行注释。

</div>

:::

::::

:::: question choice-3 | 2-9 单选题

Python语言正确的标识符是_______。

**A.** 2you

**B.** my-name

**C.** _item

**D.** abc*234

<div class="question-tags"><span class="question-tag">标识符</span> <span class="question-tag">变量命名</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

_item 合法，不能以数字开头或含连字符、星号。

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

C 属于过程式语言，其他选项提供类等面向对象机制。

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

Python 没有独立的 char 内置类型。

</div>

:::

::::

:::: question choice-6 | 2-6 单选题

Python 语句 print(0xA + 0xB)的输出结果是______________。

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

0xA=10，0xB=11，相加为 21。

</div>

:::

::::

:::: question choice-7 | 2-7 单选题

Python 语句x=’car’; y = 2; print (x+y)的输出结果是____________。

**A.** 语法错

**B.** 2

**C.** 'car2’

**D.** 'carcar’

<div class="question-tags"><span class="question-tag">字符串拼接</span> <span class="question-tag">类型错误</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

无严格正确选项；按普通引号还原后为运行时 `TypeError`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

题面使用弯引号，原样作为 Python 代码会产生 SyntaxError；若按普通字符串引号理解，字符串 car 与整数 2 相加会产生 TypeError，不能称为语法错误。A 仅在原样弯引号情形下适用。

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

两个平方根结果分别为浮点数 2.0 和 3.0，乘积为 6.0。

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

复数虚部后缀可以为 j 或 J，如 1J 合法。实部、虚部属性为浮点数，调用 conjugate() 得到共轭复数。选项 A 是概念示意，实际代码不能在数字与 j 之间插入空格。

</div>

:::

::::

:::: question choice-10 | 2-10 单选题

Python 语句 print(chr(65))的运行结果是___________。

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

码点 65 对应字符 A。

</div>

:::

::::

:::: question choice-11 | 2-12 单选题

关于Python字符串，下列说法错误的是___________。

**A.** 字符即长度为1的字符串

**B.** 字符串以\0标志字符串的结束

**C.** 既可以用单引号，也可以用双引号创建字符串

**D.** 在三引号字符串中可以包含换行回车等特殊字符

<div class="question-tags"><span class="question-tag">字符串</span> <span class="question-tag">字符编码</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 字符串不使用 \0 标记结束。

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

a 错：i*=3+5 等价于 i=i*(3+5)；b 错：科学计数法指数不能写成 2.0；c 对：int("3.5",10) 确实运行时报错；d 错：整数默认右对齐，字符串默认左对齐。

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

**B.** Fasle [1, 2, 3] False [1, 5, 3]

**C.** True [1, 5, 3] True [1, 7, 3]

**D.** False [1, 2, 3] True [1, 5, 3]

<div class="question-tags"><span class="question-tag">id函数</span> <span class="question-tag">列表引用</span> <span class="question-tag">浅拷贝</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

b 和 a 指向同一列表，修改 a 后 b 同步变化；d=a[:] 是外层副本，后续 a[1]=7 不改变 d。

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

2AC₁₆ = 684₁₀ = 1254₈；按题目不额外添加 0o 前缀。

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

106=64+32+8+2，是正数，8 位原码、反码和补码相同。

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

78 的 7 位数值部分为 1001110；原码符号位置 1，反码保留符号位并翻转其余位，补码再加 1。

</div>

:::

::::

:::: question blank-4 | 4-4 填空题

Python 表达式 0 and 1 or not 2&lt;True 的值为 _____ 。

<div class="question-tags"><span class="question-tag">逻辑运算</span> <span class="question-tag">运算符优先级</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算 2<True，即 2<1，为假；not 后为真。0 and 1 得到 0，再与 True 做 or 得到 True。

</div>

:::

::::

:::: question blank-5 | 4-8 填空题

Python 语句 print(abs(-10.2), round(abs(8-2j),3)) 的输出结果是 _____ 。

<div class="question-tags"><span class="question-tag">abs函数</span> <span class="question-tag">复数模</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`10.2 8.246`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

abs(-10.2)=10.2；复数的模为 sqrt(8²+(-2)²)=sqrt(68)，保留 3 位小数为 8.246。

</div>

:::

::::

:::: question blank-6 | 4-14 填空题

表达式 3 and 0 and 5的结果是什么？。 _____

<div class="question-tags"><span class="question-tag">and运算符</span> <span class="question-tag">短路求值</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`0`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

and 短路并返回遇到的假值 0，不继续检查 5。

</div>

:::

::::

:::: question blank-7 | 4-16 填空题

表达式 ---3 的结果是什么？ _____ 。

<div class="question-tags"><span class="question-tag">一元负号</span> <span class="question-tag">运算符优先级</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`-3`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

三次一元负号，最终为负。

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

32.2//6 为 5.0，24//6 为 4，差为浮点数 1.0。

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

每个字符先判断大写并转小写，再独立判断小写并转大写；原本大写会连续转换两次，原本小写转换一次，最终全部大写。两个 if 不是 if-elif。

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
result = 0 if x == 0 else 1 / (2 * x)
print(f'g({x:.3f}) = {result:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

x=0 时单独处理，避免除零；其他情况计算 1/(2x)，两个数都保留三位小数。

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

<div class="question-tags"><span class="question-tag">sorted函数</span> <span class="question-tag">map函数</span> <span class="question-tag">join方法</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
values = sorted(map(int, input().split()), reverse=True)
print('>'.join(map(str, values)))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

按数值降序排序，再转字符串以 > 连接；不能先按字符串排序。

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

<div class="question-tags"><span class="question-tag">时间换算</span> <span class="question-tag">整除与取余</span> <span class="question-tag">map函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
start, end = map(int, input().split())
start_minutes = start // 100 * 60 + start % 100
end_minutes = end // 100 * 60 + end % 100
hours, minutes = divmod(end_minutes - start_minutes, 60)
print(f'在途时间是{hours}小时{minutes}分钟')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

小时用 //100 提取，分钟用 %100 提取，统一换算为分钟求差，再除以 60。题目保证同日到达，无需跨日处理。

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

<div class="question-tags"><span class="question-tag">Fraction类</span> <span class="question-tag">floor函数</span> <span class="question-tag">序列求和</span></div>

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

每项为 i²+1/i，求和后按题目提示 floor 向下取整。Fraction 保留精确值，避免例如 m=n=1 时的浮点误差。题面“小于”与 floor 在整数处不同，此处采用提示的 floor 定义。

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
result = math.sin(math.radians(35)) + (math.exp(x) - 15 * x) / math.sqrt(x ** 4 + 1) - math.log(7 * x)
print(f'f({x})={result:.3f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

图中 sin(35°) 需先将角度转弧度；分母为 sqrt(x⁴+1)，ln 用 math.log。x 按 float 输出，函数值保留三位小数。

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
n = int(input())
for i in range(1, n + 1):
    print('* ' * i)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

每行有 i 个星号，每个星号后输出一个空格，保留原始网页样例的行尾空格。

</div>

:::

::::
