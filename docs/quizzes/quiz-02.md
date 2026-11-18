---
title: 第二次上机小测
eyebrow: QUIZ 02
description: 题目、参考答案与解析。
code: Quiz 02
questionGroups:
  - [判断题, judgment, 17]
  - [单选题, choice, 6]
  - [填空题, blank, 11]
  - [编程题, programming, 7]
---

<div class="editor-note">

本次小测共 **41 题**：判断题 17 题、单选题 6 题、填空题 11 题、编程题 7 题。整理自原始小测资料，答案按 Python 3 语义核对；编程题代码未在 PTA 平台提交验证。

文中 `□` 表示一个空格；真实输出放在代码块中，请注意前导和末尾空格。

</div>


<h2 id="judgment" class="quiz-group">判断题<span>17 QUESTIONS</span></h2>


:::: question judgment-1 | Q01. 判断题

 `'age'+23` 不是正确的表达式。

<div class="question-tags"><span class="question-tag">字符串拼接</span> <span class="question-tag">类型转换</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`'age'` 是字符串，`23` 是整数。`+` 用于字符串拼接时，两边都必须是字符串，Python 不会自动把整数转换成字符串，因此执行时会引发 `TypeError`。

这里考查**数据类型与显式转换**：`'age'+str(23)` 得到 `'age23'`；`int('23')+1` 得到整数 `24`。注意：`'age'+23` 本身没有语法错误，错误发生在运行时。

</div>

:::

::::


:::: question judgment-2 | Q02. 判断题

 列表可以用 `find()` 函数来搜索数据是否在列表中。

<div class="question-tags"><span class="question-tag">find方法</span> <span class="question-tag">in运算符</span> <span class="question-tag">index方法</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`find()` 是字符串方法，列表没有这个方法。例如 `'abc'.find('b')` 返回下标 `1`，但 `[1,2,3].find(2)` 会引发 `AttributeError`。

这里考查**成员判断与查找方法**：`2 in [1,2,3]` 判断是否存在，返回布尔值；`[1,2,3].index(2)` 查找首次出现的位置，返回下标 `1`。`index()` 找不到时会报错，因此只判断有无时直接用 `in`。

</div>

:::

::::


:::: question judgment-3 | Q03. 判断题

 字符串对象和元组对象是不可变对象，列表对象为可变对象。

<div class="question-tags"><span class="question-tag">可变与不可变对象</span> <span class="question-tag">列表与字符串</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

“可变”指对象创建后，能否原地修改其内容。列表可以执行 `a[0]=新值`、`append()`、`pop()`；字符串和元组不能直接给某个位置重新赋值。

这里考查**对象可变性与变量绑定**：`s=s+'x'` 可以执行，但这是生成新字符串再让 `s` 指向它，不是修改原字符串。元组若包含列表，内部列表仍可修改；不可变的是元组自身各位置保存的引用。

</div>

:::

::::


:::: question judgment-4 | Q04. 判断题

 列表 `lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21]`，`lst[1::2]` 的结果是 `[12, -22, -26, 0, 3]`。

<div class="question-tags"><span class="question-tag">列表切片</span> <span class="question-tag">range函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

切片格式是 `序列[start:stop:step]`，下标从 `0` 开始。`lst[1::2]` 表示从下标 `1` 起，每次前进 `2` 个位置，取下标 `1、3、5、7、9` 的元素，结果为 `[-5,-10,35,49,-21]`。

这里考查**切片起点与步长**：正步长时省略终点表示一直取到末尾。题目给出的 `[12,-22,-26,0,3]` 实际对应 `lst[::2]`，即从下标 `0` 开始取。

</div>

:::

::::


:::: question judgment-5 | Q05. 判断题

 列表 `lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21]`，`lst[3:8:2]` 的结果是 `[-10, 35, 49]`。

<div class="question-tags"><span class="question-tag">列表切片</span> <span class="question-tag">左闭右开</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst[3:8:2]` 从下标 `3` 开始，以 `2` 为步长，取下标 `3、5、7`，对应 `-10、35、49`，因此题目正确。

这里考查**切片左闭右开规则**：包含起点，不包含终点。可先用 `range(3,8,2)` 列出目标下标，再逐个查元素；正步长切片若起点不小于终点，则结果为空序列。

</div>

:::

::::


:::: question judgment-6 | Q06. 判断题

 列表 `lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21]`，`lst[0:100]` 的结果是错误。

<div class="question-tags"><span class="question-tag">列表切片</span> <span class="question-tag">索引越界</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst[0:100]` 是切片，终点超出列表长度时会自动截到末尾，因此返回整个列表的浅拷贝，不会报错。

这里考查**切片与单元素索引的区别**：`lst[100]` 访问不存在的元素，会引发 `IndexError`；`lst[100:200]` 则返回空列表。切片产生新列表，但其中的元素并不一定被复制。

</div>

:::

::::


:::: question judgment-7 | Q07. 判断题

 表达式 `"34" in "1234"==True` 返回值是 `True`。

<div class="question-tags"><span class="question-tag">链式比较</span> <span class="question-tag">in运算符</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`in` 和 `==` 都属于比较运算符，这里会形成链式比较：`"34" in "1234" == True` 等价于 `("34" in "1234") and ("1234" == True)`。前半部分为 `True`，后半部分为 `False`，所以整体为 `False`。

这里考查**链式比较**：它和 `1<x<10` 使用相同规则，不会先算出成员判断结果再与 `True` 比较。若只想判断子串是否存在，直接写 `"34" in "1234"` 即可；加括号后 `("34" in "1234")==True` 也为真。

</div>

:::

::::


:::: question judgment-8 | Q08. 判断题

 `"12 "*3==" ".join(["12","12","12"])` 的输出是 `True`。

<div class="question-tags"><span class="question-tag">字符串重复</span> <span class="question-tag">join方法</span> <span class="question-tag">空格处理</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

字符串乘以整数会完整重复原字符串，包括原有空格。因此 `"12 "*3` 得到 `'12 12 12 '`，末尾仍有空格；`" ".join(["12","12","12"])` 得到 `'12 12 12'`，两者不相等。

这里考查**字符串重复、连接与精确比较**：`join()` 只在相邻元素之间插入分隔符，不在开头和结尾额外添加。排查空格问题可用 `repr()` 显示字符串边界，或用 `len()` 比较长度。

</div>

:::

::::


:::: question judgment-9 | Q09. 判断题

 语句 `print("输出结果是{:8s}".format("this"))` 的输出是 `输出结果是□□□□this`，`□` 表示空格。

<div class="question-tags"><span class="question-tag">字符串格式化</span> <span class="question-tag">左对齐</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`{:8s}` 中，`s` 表示按字符串格式输出，`8` 表示最小字段宽度。`this` 长度为 `4`，字符串默认左对齐，所以在右边补 `4` 个空格，实际为 `输出结果是this□□□□`。

这里考查**格式化宽度与对齐**：`<` 左对齐、`>` 右对齐、`^` 居中。若想得到题目所示结果，应写 `{:>8s}`。宽度是最小值，字符串长度超过 `8` 时不会被截断。

</div>

:::

::::


:::: question judgment-10 | Q10. 判断题

 语句 `print("输出结果是{:8d}".format(1234))` 的输出是 `输出结果是1234□□□□`，`□` 表示空格。

<div class="question-tags"><span class="question-tag">整数格式化</span> <span class="question-tag">右对齐</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`{:8d}` 中，`d` 表示十进制整数格式，字段最小宽度为 `8`。整数 `1234` 占 `4` 位，数值默认右对齐，所以左边补 `4` 个空格，实际为 `输出结果是□□□□1234`。

这里考查**数值格式化与默认对齐方式**：字符串默认左对齐，数值默认右对齐。`{:<8d}` 可使整数左对齐，`{:08d}` 可用前导零补足宽度，得到 `00001234`。

</div>

:::

::::


:::: question judgment-11 | Q11. 判断题

 `[4,5]*3` 的结果是 `[[4,5],[4,5],[4,5]]`。

<div class="question-tags"><span class="question-tag">列表重复</span> <span class="question-tag">嵌套列表</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

列表乘以整数会重复其中的元素，不会自动把原列表嵌套成一个元素。因此 `[4,5]*3` 得到 `[4,5,4,5,4,5]`；若要三个子列表，形式应为 `[[4,5]]*3`。

这里考查**序列重复与引用共享**：`[[4,5]]*3` 的三个位置指向同一个内部列表，修改其中一个会同时影响另外两个。需要相互独立的子列表时，可写 `[[4,5] for _ in range(3)]`。

</div>

:::

::::


:::: question judgment-12 | Q12. 判断题

 下面程序的输出是字符 `a`。

```python
c="A"
print(c.lower)
```

<div class="question-tags"><span class="question-tag">lower方法</span> <span class="question-tag">方法调用</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`c.lower` 只是取得绑定在字符串 `c` 上的方法对象，并没有执行方法；`print()` 输出的是方法对象的描述，而不是字符 `a`。应写成 `print(c.lower())`。

这里考查**方法引用与方法调用**：函数或方法名称后加 `()` 才会调用。`lower()` 返回转换后的新字符串，不改变原字符串；若要更新变量，应写 `c=c.lower()`。

</div>

:::

::::


:::: question judgment-13 | Q13. 判断题

 执行 `import random;print(int(random.random()*90)+10)` 可以随机产生二位正整数。

<div class="question-tags"><span class="question-tag">random模块</span> <span class="question-tag">随机数范围</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`random.random()` 生成 `[0,1)` 范围内的随机浮点数，乘 `90` 后属于 `[0,90)`。对非负数用 `int()` 去掉小数部分，得到 `0～89`，再加 `10` 就得到 `10～99` 的二位整数。

这里考查**随机数范围变换与取整**：注意上界 `1` 不包含，所以不会得到 `100`。直接生成此范围的整数也可以用 `random.randint(10,99)` 或 `random.randrange(10,100)`，前者包含两端，后者不包含右端。

</div>

:::

::::


:::: question judgment-14 | Q14. 判断题

 执行语句 `m,n=int(input().split(","))` 时，输入 `3,4` 可以得到 `m` 和 `n` 的值分别为 3 和 4。

<div class="question-tags"><span class="question-tag">split方法</span> <span class="question-tag">map函数</span> <span class="question-tag">拆包赋值</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

输入 `3,4` 后，`input()` 得到字符串 `'3,4'`，`split(',')` 得到列表 `['3','4']`。`int()` 不能把整个列表一次转换成整数，所以程序在拆包前就会引发 `TypeError`。

这里考查**输入、拆分、逐项转换与拆包**：应写 `m,n=map(int,input().split(','))`，先将每一项转成整数，再分别赋值。拆分出的项目数也必须与左侧变量数匹配；若输入用空格分隔，则可用不带参数的 `split()`。

</div>

:::

::::


:::: question judgment-15 | Q15. 判断题

 赋值语句 `L=[123,"abc",True]` 是正确的。

<div class="question-tags"><span class="question-tag">列表</span> <span class="question-tag">混合数据类型</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 列表可以存放不同类型的对象，因此整数 `123`、字符串 `'abc'` 和布尔值 `True` 可以同时作为元素，赋值语句合法。

这里考查**列表的基本特性**：列表有序、可变、允许重复，也不要求元素类型相同。需要区分“可以放在一起”和“可以统一运算”：这个列表不能直接用 `sum()` 求和，因为字符串不能与整数相加。

</div>

:::

::::


:::: question judgment-16 | Q16. 判断题

 要使用 `math` 库，只须在使用 `math` 库函数之前，用 `import math` 语句导入 `math` 库即可。即语句 `import math` 不必放在源程序的第一行。

<div class="question-tags"><span class="question-tag">import语句</span> <span class="question-tag">模块导入</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`import math` 是可以执行的语句，程序只要在执行 `math.sqrt()`、`math.sin()` 等调用前完成导入，并且当前作用域能访问名称 `math`，就能使用相应函数。

这里考查**模块导入与执行顺序**：导入语句不强制位于第一行，但通常集中放在文件开头以方便阅读。`import math` 后用 `math.sqrt(4)`；`from math import sqrt` 后则直接用 `sqrt(4)`。

</div>

:::

::::


:::: question judgment-17 | Q17. 判断题

 设列表 `a=[1,2,3]`，则 `a[::-1]` 和 `a.reverse()` 是一样的，均是把列表 `a` 反转（即逆向）过来。

<div class="question-tags"><span class="question-tag">reverse方法</span> <span class="question-tag">列表切片</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`a[::-1]` 用步长 `-1` 生成反转后的新列表 `[3,2,1]`，原列表 `a` 仍是 `[1,2,3]`。`a.reverse()` 则直接把原列表改成 `[3,2,1]`，方法返回值为 `None`。

这里考查**返回新对象与原地修改**：若写 `b=a[::-1]`，`b` 是新列表；若写 `b=a.reverse()`，`b` 得到的是 `None`。列表的 `append()`、`sort()` 也属于修改原列表并返回 `None` 的常见方法。

</div>

:::

::::


<h2 id="choice" class="quiz-group">单选题<span>06 QUESTIONS</span></h2>


:::: question choice-1 | Q01. 单选题

 以下哪句打印出 `smith\exam1\test.txt`？

```text
A. print("smith\exam1\test.txt")
B. print("smith\\exam1\\test.txt")
C. print("smith\"exam1\"test.txt")
D. print("smith"\exam1"\test.txt")
```

<div class="question-tags"><span class="question-tag">转义字符</span> <span class="question-tag">原始字符串</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

普通字符串中的反斜杠用于引出转义序列，例如 `\t` 表示制表符、`\n` 表示换行。要输出一个真实的反斜杠，应在字符串字面量中写 `\\`，所以 B 能输出所需路径。

这里考查**转义字符与原始字符串**：也可以写 `print(r"smith\exam1\test.txt")`，用 `r` 前缀保留反斜杠。C 中的 `\"` 表示双引号，输出内容不符；D 的引号与反斜杠写法不构成合法表达式。

</div>

:::

::::


:::: question choice-2 | Q02. 单选题

 如果 `list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]`，那么以下哪个是 `list1[:-1]`？

```text
A. 0
B. [1, 2, 3, 4, 5, 4, 3, 2, 1]
C. [1, 2, 3, 4, 5, 4, 3, 2]
D. [0, 1, 2, 3, 4, 3, 2, 1, 0]
```

<div class="question-tags"><span class="question-tag">列表切片</span> <span class="question-tag">负索引</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`list1[:-1]` 从列表开头取到下标 `-1` 之前，最后一个元素不包含在结果中，所以得到 `[1,2,3,4,5,4,3,2]`。

这里考查**负索引与切片**：`-1` 表示最后一个元素，`-2` 表示倒数第二个元素。`list1[-1]` 取得单个元素，而 `list1[:-1]` 取得列表；类似地，`list1[-2:]` 取得最后两个元素。

</div>

:::

::::


:::: question choice-3 | Q03. 单选题

 要把 5 加到列表 `lst` 的末尾，用的是哪一句？

```text
A. lst.add(5)
B. lst.append(5)
C. lst.addLast(5)
D. lst.addEnd(5)
```

<div class="question-tags"><span class="question-tag">append方法</span> <span class="question-tag">列表操作</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst.append(5)` 会把整数 `5` 作为一个元素追加到列表末尾，其他选项不是列表提供的方法。注意 `append()` 修改原列表，返回 `None`，不要写成 `lst=lst.append(5)`。

这里考查**列表添加元素的方法**：`append(x)` 添加一个整体；`extend(可迭代对象)` 逐项追加，例如 `[1].extend([2,3])` 后列表为 `[1,2,3]`；`insert(i,x)` 则在指定位置插入。`add()` 是集合常见的添加方法。

</div>

:::

::::


:::: question choice-4 | Q04. 单选题

 下列语句正确的有多少个？

```text
a、语句a,b="3 4"是错误的。
b、执行语句a,b=34可以得到a、b的值分别是3和4。
c、赋值语句a,b=4可以得到a和b的值均为4。
d、执行语句a,b=eval(input())时，输入10  20可以得到a和b的值分别为10和20。

A. 0
B. 1
C. 2
D. 3
```

<div class="question-tags"><span class="question-tag">拆包赋值</span> <span class="question-tag">eval函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B（1 个）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

只有 a 正确。`a,b="3 4"` 会把字符串按字符拆包，但它含有 `'3'`、空格、`'4'` 三项，两个变量接收不了；b、c 的右侧都是不可迭代的整数，也不能直接拆包。d 中 `eval("10  20")` 不是合法 Python 表达式，会引发语法错误。

这里考查**拆包赋值与输入格式**：`a,b=3,4` 可分别赋值，`a=b=4` 可令两者都为 `4`。`eval()` 解析的是 Python 表达式，`10,20` 可解析成元组，而空格分隔的数字应使用 `map(int,input().split())`。

</div>

:::

::::


:::: question choice-5 | Q05. 单选题

 执行语句 `import math as t` 后，以下哪两句是正确的？

```text
(1)语句math.sin(10)是错误的。
(2)语句math.sin(10)是正确的。
(3)语句t.sin(10)是正确的。
(4)语句t.sin(10)是错误的。

A. (1)(3)
B. (1)(4)
C. (2)(3)
D. (2)(4)
```

<div class="question-tags"><span class="question-tag">import别名</span> <span class="question-tag">math模块</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`import math as t` 加载 `math` 模块后，将它绑定到当前名称 `t`，所以可以用 `t.sin(10)`。假定此前没有另外定义或导入 `math`，此时 `math.sin(10)` 会因名称未定义而报错，因此 (1)、(3) 正确。

这里考查**模块别名与命名空间**：`as` 后的别名是本次导入后实际用于访问模块的名称。还要注意 `sin()` 的参数单位是弧度；若要计算角度的正弦，可先用 `t.radians(角度)` 转换。

</div>

:::

::::


:::: question choice-6 | Q06. 单选题

 如果下述循环正常结束（即无 `break` 语句），则循环结束后 `i` 的值是？

```python
for i in range(10,0,-2):
    循环体语句
print(i)
```

```text
A. 无法确定
B. 2
C. 0
D. -2
```

<div class="question-tags"><span class="question-tag">range函数</span> <span class="question-tag">for循环</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`range(10,0,-2)` 依次产生 `10、8、6、4、2`，不包含终点 `0`。按题意循环体不另改 `i`，循环结束后 `i` 保留最后一次获得的值 `2`，所以选择 B。

这里考查**range 的边界与循环变量**：`range(start,stop,step)` 左闭右开，步长为负时递减。Python 的 `for` 不会在结束时额外把变量减一次，也不会创建独立的块级作用域；若序列为空，循环不会为变量赋新值。

</div>

:::

::::


<h2 id="blank" class="quiz-group">填空题<span>11 QUESTIONS</span></h2>


:::: question blank-1 | Q01. 填空题

 `len('3//11//2018'.split('/'))` 的结果是 _____。

<div class="question-tags"><span class="question-tag">split函数</span> <span class="question-tag">len函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`5`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

指定 `'/'` 为分隔符时，`'3//11//2018'.split('/')` 得到 `['3','','11','','2018']`。两个连续的分隔符之间没有内容，仍会保留一个空字符串，因此长度是 `5`。

这里考查**split 的两种行为**：指定分隔符会保留连续分隔符产生的空项；不带参数的 `split()` 按空白分隔，会合并连续空白并忽略两端空白。`len()` 统计列表元素个数，空字符串也算一个元素。

</div>

:::

::::


:::: question blank-2 | Q02. 填空题

 `list(range(2,12,2))[:-2].pop()` 的结果是 _____。

<div class="question-tags"><span class="question-tag">range函数</span> <span class="question-tag">列表切片</span> <span class="question-tag">pop方法</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`6`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先算 `range(2,12,2)`，转换成列表为 `[2,4,6,8,10]`。`[:-2]` 去掉最后两个元素，得到新列表 `[2,4,6]`；最后的 `pop()` 删除并返回末尾元素，所以结果是整数 `6`。

这里考查**链式求值、切片与删除方法**：`pop(i)` 删除并返回指定下标的元素，省略下标时取最后一个；空列表调用 `pop()` 会报错。`remove(x)` 则按元素值删除首次匹配项，并不返回被删元素。

</div>

:::

::::


:::: question blank-3 | Q03. 填空题

 下列语句的输出是 _____（答案不要加引号）。

```python
print("{1}+{0}={2}".format(2,3,2+3))
```

<div class="question-tags"><span class="question-tag">format方法</span> <span class="question-tag">位置参数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```text
3+2=5
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`format(2,3,2+3)` 的三个位置参数依次是 `2、3、5`，编号从 `0` 开始。因此 `{1}` 替换成 `3`，`{0}` 替换成 `2`，`{2}` 替换成 `5`，最终输出 `3+2=5`。

这里考查**位置参数格式化**：花括号中的编号决定使用哪个参数，与它在字符串中出现的顺序无关，同一个参数可以被重复引用。花括号之外的 `+`、`=` 只是普通文本，不会作为表达式参与运算。

</div>

:::

::::


:::: question blank-4 | Q04. 填空题

 下面程序的输出是 _____（答案不要加引号）。

```python
a=34
b=23
print("{first}-{second}={0}".format(34-23,first=a,second=b))
```

<div class="question-tags"><span class="question-tag">format方法</span> <span class="question-tag">关键字参数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```text
34-23=11
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先计算位置参数 `34-23`，得到 `11`，它对应 `{0}`；关键字参数 `first=a`、`second=b` 分别对应 `{first}`、`{second}`。依次替换后输出 `34-23=11`。

这里考查**位置参数与关键字参数混用**：格式串可同时按编号和名称取值，调用时位置参数要放在关键字参数之前。`{first}` 是读取传入参数名，不会自动查找程序中的同名变量，必须显式传入。

</div>

:::

::::


:::: question blank-5 | Q05. 填空题

 下列语句的输出是 _____。

```python
print("{:>08s}".format(bin(31)[2:]))
```

<div class="question-tags"><span class="question-tag">bin函数</span> <span class="question-tag">字符串切片</span> <span class="question-tag">格式化输出</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```text
00011111
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`bin(31)` 得到字符串 `'0b11111'`，`[2:]` 去掉前缀 `'0b'`，剩下 `'11111'`。格式 `>08s` 表示将字符串按宽度 `8` 右对齐并在左侧补零，需要补 `3` 个 `0`，所以得到 `00011111`。

这里考查**进制表示、切片与格式控制**：更明确的写法是 `'{:0>8s}'.format(...)`，其中 `0` 为填充字符、`>` 为对齐方式、`8` 为最小宽度。也可直接用 `format(31,'08b')` 输出宽度为 8 的二进制表示。

</div>

:::

::::


:::: question blank-6 | Q06. 填空题

 `print("programming".find("x"))` 的输出是 _____。

<div class="question-tags"><span class="question-tag">find方法</span> <span class="question-tag">字符串查找</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`-1`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

字符串 `'programming'` 中没有子串 `'x'`，因此 `find('x')` 返回 `-1`。找到时返回首次匹配位置，位置从 `0` 开始，例如 `'programming'.find('p')` 返回 `0`。

这里考查**子串查找与返回值判断**：`find()` 找不到返回 `-1`，`index()` 找不到则报错。不要用 `if s.find(x)` 判断是否存在，因为下标 `0` 为假而 `-1` 为真；应写 `x in s` 或 `s.find(x)!=-1`。

</div>

:::

::::


:::: question blank-7 | Q07. 填空题

 下列语句的输出是 _____（答案不要加引号）。用 `□` 表示空格，各字符串均为前面 3 个空格、后面 2 个空格。

```python
print("   xyz  ".strip(),"   xyz  ".rstrip(),
      "   xyz  ".lstrip())
```

<div class="question-tags"><span class="question-tag">strip方法</span> <span class="question-tag">rstrip方法</span> <span class="question-tag">lstrip方法</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

**用 `□` 显示空格：** `xyz□□□□xyz□xyz□□`

**实际输出（末尾有两个空格）：**

```text
xyz    xyz xyz  
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

三个字符串都是前面 `3` 个空格、后面 `2` 个空格。调用后依次得到 `'xyz'`、`'   xyz'`、`'xyz  '`，而 `print()` 默认在相邻参数间再加一个空格，因此最终为 `xyz□□□□xyz□xyz□□`。

这里考查**两端清理与输出分隔符**：`strip()` 去两端空白，`rstrip()` 只去右端，`lstrip()` 只去左端，都不会删除中间空格，也不修改原字符串。`print(...,sep='')` 可取消参数间分隔空格；其默认 `end='\n'` 表示输出后换行。

</div>

:::

::::


:::: question blank-8 | Q08. 填空题

 下面程序的输出依次分别是 _____、_____、_____。

```python
a=[1,2,3,4]
b=a
print(id(a)==id(b))
c=a.copy()
print(id(a)==id(c))
d=a[:]
print(id(a)==id(d))
```

<div class="question-tags"><span class="question-tag">id函数</span> <span class="question-tag">copy方法</span> <span class="question-tag">浅拷贝</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`、`False`、`False`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`b=a` 不复制列表，只让两个变量指向同一个对象，因此 `id(a)==id(b)` 为 `True`。`a.copy()` 和 `a[:]` 都创建新列表，虽然元素相同，但对象身份不同，后两次结果均为 `False`。

这里考查**赋值、相等、身份与浅拷贝**：`==` 比较内容是否相等，`is` 判断是否为同一个对象，`id()` 获取对象的身份标识。浅拷贝只复制外层容器；若列表中还包含列表，内部对象仍可能共享，递归复制可用 `copy.deepcopy()`。

</div>

:::

::::


:::: question blank-9 | Q09. 填空题

 列表加元组可以表示二维表。下面程序用三种不同方式打印表格内容，请填空完成与第一种方式输出一样的后面两种方式，不要加无用空格。

| 学号 | 姓名 |
| --- | --- |
| 3180102988 | 褚好 |
| 3170102465 | 王凯亮 |
| 3160104456 | 李永 |
| 3171104169 | 陈鑫 |
| 318400429 | 徐杭诚 |

```python
students=[(3180102988,"褚好"),
          (3170102465,"王凯亮"),
          (3160104456,"李永"),
          (3171104169,"陈鑫"),
          (318400429,"徐杭诚")]

for row in students: #按行存取
    print(row[0],row[1])
print()

for id,name in students: #按行拆包存取
    print(_____)  # 第1空
print()

for index in range(len(students)): #按索引存取
    print(_____)  # 第2空
```

<div class="question-tags"><span class="question-tag">二维列表</span> <span class="question-tag">元组拆包</span> <span class="question-tag">索引访问</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```text
第1空：id,name
第2空：students[index][0],students[index][1]
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`for row in students` 每次取得一个二元组，所以第一种写法用 `row[0]`、`row[1]` 访问学号和姓名。`for id,name in students` 会把每个二元组直接拆包，因此第一空是 `id,name`；按索引遍历时，第二空是 `students[index][0],students[index][1]`。

这里考查**嵌套序列、拆包与二维索引**：`students[index]` 先选定一行，再用 `[0]` 或 `[1]` 选字段。逗号让 `print()` 接收两个参数并自动用空格分隔；若还需要行号，常用 `for index,row in enumerate(students)`。

</div>

:::

::::


:::: question blank-10 | Q10. 填空题

 `print(sum((1,3,5,7,9))/len((1,3,5,7,9)))` 的输出是 _____。

<div class="question-tags"><span class="question-tag">sum函数</span> <span class="question-tag">len函数</span> <span class="question-tag">平均值</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`5.0`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

元组共有 `5` 个元素，总和为 `1+3+5+7+9=25`，所以表达式计算 `25/5`。Python 3 中 `/` 对整数执行的也是普通除法，结果为浮点数 `5.0`，不能填成 `5`。

这里考查**聚合函数与除法类型**：`sum()` 求和，`len()` 统计元素个数，两者结合常用于求平均值。`//` 才是向下取整除法，例如 `25//5` 为 `5`、`-3//2` 为 `-2`；计算平均值前还要避免序列为空。

</div>

:::

::::


:::: question blank-11 | Q11. 填空题

 下面程序的输出是 _____。

```python
t=1
t,a=2,t+1
print(a)
```

<div class="question-tags"><span class="question-tag">拆包赋值</span> <span class="question-tag">赋值顺序</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`2`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

执行 `t,a=2,t+1` 时，先计算整个右侧。此时旧的 `t` 为 `1`，右侧两个值是 `2` 和 `2`，随后再分别赋给左侧的 `t`、`a`，因此输出 `2`。

这里考查**多目标拆包赋值的求值顺序**：不是先让 `t=2` 再计算 `a=t+1`，所以 `a` 不会得到 `3`。常见的交换写法 `a,b=b,a` 也利用此规则，无需额外的临时变量。

</div>

:::

::::


<h2 id="programming" class="quiz-group">编程题<span>07 QUESTIONS</span></h2>


:::: question programming-1 | Q01. 求整数的位数及各位数字之和

 对于给定的正整数 N，求它的位数及其各位数字之和。（提示：把整数转换成字符串、列表，用 `sum` 和 `len` 函数。）

**输入格式：** 在一行中给出一个正整数 N。

**输出格式：** 在一行中输出 N 的位数及其各位数字之和，中间用一个空格隔开。

**输入样例：**

```text
456
```

**输出样例：**

```text
3 15
```

<div class="question-tags"><span class="question-tag">类型转换</span> <span class="question-tag">字符串遍历</span> <span class="question-tag">sum函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = str(int(input()))
print(len(s), sum(int(c) for c in s))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`input()` 读到字符串，先转成整数再转回字符串，可去掉前导零等输入形式的影响。对于 `'456'`，`len(s)` 得到 `3`，逐个把 `'4'`、`'5'`、`'6'` 转成整数并求和，得到 `15`。

这里考查**类型转换、字符串遍历与生成器表达式**：`sum(int(c) for c in s)` 逐项转换后累加，不需要先创建列表。`print()` 接收两个参数时默认用一个空格分隔，正好符合输出要求；若有 k 位数字，遍历耗时为 O(k)。

</div>

:::

::::


:::: question programming-2 | Q02. 计算有n个字符串中最长的字符串长度

 编写程序，计算 n（1<n<10）个字符串中最长的字符串的长度。前导空格不要计算在内！

**输入格式：** 第一行输入 n，接下来的每行输入一个字符串。

**输出格式：** 在一行中输出最长的字符串的长度，按样例输出 `length=长度`。

**输入样例：**

```text
4
        blue
yellow
red
green
```

**输出样例：**

```text
length=6
```

<div class="question-tags"><span class="question-tag">逐行输入</span> <span class="question-tag">lstrip方法</span> <span class="question-tag">max函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
longest = 0
for _ in range(n):
    s = input().lstrip(' ')
    longest = max(longest, len(s))
print(f"length={longest}")
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先读入字符串个数，再逐行处理。`input()` 读取整行并去掉行尾换行符，但保留字符串中的空格；`lstrip(' ')` 只去掉左侧普通空格。每读一行，就用 `max(longest,len(s))` 更新当前最大长度。

这里考查**逐行输入、单侧清理与最值累积**：不能用 `strip()`，否则会连末尾空格一起删除；也不能直接按空格拆分整份输入，否则会破坏每行字符串。最后用 f-string 输出严格的 `length=数值`，等号两侧不加空格。

</div>

:::

::::


:::: question programming-3 | Q03. 判断回文字符串

 回文就是字符串中心对称，从左向右读和从右向左读的内容一样。输入一个字符串，判断它是否为回文，只考虑数字和字母字符，字母大小写没有区别。

**输入格式：** 输入一个字符串。

**输出格式：** 是回文则一行输出 `yes`，否则输出 `no`。

**输入样例：**

```text
A man,a plan; cnalPanama
```

**输出样例：**

```text
yes
```

<div class="question-tags"><span class="question-tag">isalnum方法</span> <span class="question-tag">字符串切片</span> <span class="question-tag">回文判断</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
s = ''.join(c.lower() for c in s if c.isalnum())
print('yes' if s == s[::-1] else 'no')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先用 `c.isalnum()` 筛出字母和数字，再用 `lower()` 统一字母大小写，最后通过 `''.join(...)` 拼成新字符串。样例处理后为 `'amanaplancnalpanama'`，与反转后的结果相同，因此输出 `yes`。

这里考查**字符判断、字符串构造与回文判断**：`s[::-1]` 利用负步长切片反转字符串；条件表达式根据比较结果选择输出。标点和空格完全不参与比较，数字仍需保留；筛选后为空串时，它也与自身反转相等。

</div>

:::

::::


:::: question programming-4 | Q04. 输入一行字符串，并将它转换成10进制数输出

 输入一行字符串，去掉非 16 进制字符，并将它转换成 10 进制数输出。

**输入格式：** 输入一行字符串。

**输出格式：** 输出筛选后的 16 进制字符串和转换后的 10 进制数，分别占一行。

**输入样例：**

```text
_ahg1*B
```

**输出样例：**

```text
a1B
2587
```

<div class="question-tags"><span class="question-tag">字符过滤</span> <span class="question-tag">十六进制转换</span> <span class="question-tag">int函数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
h = ''.join(c for c in s if c in '0123456789abcdefABCDEF')
print(h)
print(int(h, 16) if h else 0)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

十六进制的合法字符只有 `0～9`、`a～f` 和 `A～F`，按原顺序筛选样例得到 `'a1B'`，不能为了比较方便而改变输出字符串的大小写。`int(h,16)` 按十六进制解析，数值为 `10×16²+1×16+11=2587`。

这里考查**字符过滤与进制转换**：`int(字符串,基数)` 可将指定进制的文本转换成整数，`print()` 默认以十进制输出整数。`if h else 0` 避免对空字符串执行转换；题面未规定完全无合法字符时的结果，本解约定输出空行和 `0`。

</div>

:::

::::


:::: question programming-5 | Q05. 统计满足特定条件的字符数

 输入字符串 A（没有重复字符），再输入字符串 B。统计 A 中同时出现在 B 中的字符个数。提示：用 `in` 运算符。

**输入格式：** 第一行输入字符串 A，第二行输入字符串 B。

**输出格式：** 一行输出字符数。

**输入样例：**

```text
AEIOU
HELLO World!
```

**输出样例：**

```text
2
```

<div class="question-tags"><span class="question-tag">in运算符</span> <span class="question-tag">计数器</span> <span class="question-tag">集合</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a = input()
b = input()
count = 0
for c in a:
    if c in b:
        count += 1
print(count)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

遍历的是没有重复字符的 A，对每个字符只判断一次它是否存在于 B，不统计它在 B 中出现了几次。样例中 A 的 `E`、`O` 出现在 B 中，而小写 `o` 不等于大写 `O`，最终计数为 `2`。

这里考查**成员运算与计数对象的选择**：`c in b` 返回布尔值，存在就令计数器加一。不能反过来直接遍历 B 计数，否则 B 中重复字符可能被多算；若数据很大，可先做 `set(b)`，再对集合进行成员判断。

</div>

:::

::::


:::: question programming-6 | Q06. 打印m到n的等腰图形

 在同一行输入两个正整数 m 和 n，以一个空格分隔，满足 1≤m≤n≤9。输出从 m 开始到 n 的等腰图形，形状见样例。

**输入格式：** 在同一行输入 m 和 n，以一个空格分隔。

**输出格式：** 每行数字从 1 递增到当前行数值，再递减回 1；左侧补空格，使图形居中。

**输入样例 1：**

```text
2 4
```

**输出样例 1：**

```text
  121
 12321
1234321
```

**输入样例 2：**

```text
3 3
```

**输出样例 2：**

```text
12321
```

<div class="question-tags"><span class="question-tag">for循环</span> <span class="question-tag">range函数</span> <span class="question-tag">字符串拼接</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m, n = map(int, input().split())
for i in range(m, n + 1):
    left = ''.join(str(j) for j in range(1, i + 1))
    right = ''.join(str(j) for j in range(i - 1, 0, -1))
    print(' ' * (n - i) + left + right)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

外层循环依次取峰值 `i=m～n`，并不是每行从数字 m 开始。每行前半段为 `1～i`，后半段为 `i-1～1`，两段连接后共有 `2i-1` 个数字，峰值只出现一次。

这里考查**range 边界、字符串拼接与居中对齐**：最底行宽度为 `2n-1`，与当前行相差 `2(n-i)`，所以左侧补 `n-i` 个空格即可。反向部分使用 `range(i-1,0,-1)`；输出不额外补右侧空格，避免格式错误。

</div>

:::

::::


:::: question programming-7 | Q07. 十进制纯小数转成二进制小数

 在一行输入一个正的纯小数，把它转换成二进制小数，在下一行输出。如果转换结果超过 10 位或者出现无穷，则保留二进制小数部分的前 10 位。保证输入值转成二进制后不小于 `0.0000000001`。

**输入格式：** 输入一个正的纯小数 n。

**输出格式：** 输出 n 的二进制小数；提前转换完毕时无需补零。

**输入样例 1：**

```text
0.75
```

**输出样例 1：**

```text
0.11
```

**输入样例 2：**

```text
0.1324
```

**输出样例 2：**

```text
0.0010000111
```

<div class="question-tags"><span class="question-tag">Fraction类</span> <span class="question-tag">二进制小数转换</span> <span class="question-tag">循环终止条件</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
from fractions import Fraction

x = Fraction(input().strip())
bits = ''
for _ in range(10):
    x *= 2
    bit = int(x)
    bits += str(bit)
    x -= bit
    if x == 0:
        break
print('0.' + bits)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

十进制纯小数转二进制采用“乘 2 取整”：将余数乘 `2`，整数部分就是下一位二进制数，再留下小数部分继续。例如 `0.75×2=1.5` 取 `1`，`0.5×2=1` 再取 `1`，余数归零，得到 `0.11`。

这里考查**小数进制转换、循环终止与精度**：余数为零就提前结束，否则最多取 `10` 位，直接截断而不四舍五入。`Fraction` 从输入字符串构造精确分数，避免先转换成 `float` 引入误差；例如十进制 `0.1` 的二进制是无限循环小数，不能总等余数归零才停止。

</div>

:::

::::
