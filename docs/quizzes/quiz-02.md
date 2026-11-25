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

Python 可以解析 `'age' + 23`，但执行时会报 `TypeError`：`+` 不能直接把字符串和整数拼接。若想得到 `age23`，需要先把整数转换成字符串：`'age' + str(23)`。因此题目说法正确。

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

`find()` 是字符串方法，列表没有这个方法。判断元素是否在列表中，可以使用 `x in lst`；如果需要查找元素第一次出现的位置，可以使用 `lst.index(x)`。因此题目说法错误。

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

字符串和元组创建后，不能直接修改其中某个位置的元素；列表则可以通过下标修改，也可以增删元素。因此字符串、元组是不可变对象，列表是可变对象，本题正确。

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

`lst[1::2]` 从下标 1 开始，每次移动 2 位，取得下标 `1、3、5、7、9` 的元素，结果是 `[-5, -10, 35, 49, -21]`，与题目给出的结果不同，因此错误。

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

`lst[3:8:2]` 从下标 3 开始，每次增加 2，直到下标达到 8 前停止。实际取得下标 `3、5、7`，对应 `-10、35、49`。切片的终点 8 不包含在结果中，因此本题正确。

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

切片的起止位置超出列表范围时，Python 会自动截取到合法边界，不会因此报错。`lst[0:100]` 会从开头一直取到列表末尾，结果就是整个列表。因此“结果是错误”的说法不正确。

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

Python 会把 `a < b < c` 这样的表达式理解为 `a < b and b < c`。因此，`'34' in '1234' == True` 相当于同时判断 `'34' in '1234'` 和 `'1234' == True`。前者为真，后者为假，所以整体结果为 `False`。若想先判断成员关系再与 `True` 比较，需要加括号。

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

`'12 ' * 3` 的结果是 `'12 12 12 '`，末尾仍然有一个空格。`' '.join(['12','12','12'])` 的结果是 `'12 12 12'`，只在元素之间放空格。两者末尾是否有空格不同，因此比较结果为 `False`。

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

格式说明 `{:8s}` 表示字符串占用宽度至少为 8。字符串默认左对齐，因此 `this` 后面补 4 个空格，结果是 `this□□□□`，而不是在 `this` 前面补空格。本题错误。

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

格式说明 `{:8d}` 表示整数按十进制显示，字段宽度为 8。整数默认右对齐，`1234` 前面会补 4 个空格，实际结果是 `□□□□1234`，不是题目描述的格式。因此本题错误。

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

列表乘以整数表示重复列表中的元素。`[4, 5] * 3` 得到 `[4, 5, 4, 5, 4, 5]`，不会把原列表整体复制成三个嵌套列表。因此本题错误。

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

`c.lower` 只是取得 `lower` 方法本身，并没有执行大小写转换。调用方法时需要加括号：`c.lower()`，结果才是字符串 `'a'`。原程序打印的是方法对象，不会输出字符 `a`，因此本题错误。

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

输入 `3,4` 后，`input()` 读取到字符串 `"3,4"`，`split(",")` 按逗号拆分，得到列表 `['3', '4']`。

原程序接着执行 `int()`，试图把整个列表转换成整数。`int()` 只能转换单个数字字符串，不能直接转换列表，因此程序会报错，无法将 3 和 4 分别赋给 `m` 和 `n`。

正确写法是：

```python
m, n = map(int, input().split(","))
```

`map(int, ...)` 会把列表中的每个字符串分别转换成整数，再赋值给 `m` 和 `n`。

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

要输出 `smith\exam1\test.txt`，两个分隔位置都需要一个反斜杠。在普通字符串字面量中，`\\` 表示一个反斜杠，所以选 B。选项 A 中的 `\t` 会被解释为制表符。

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

`list1[:-1]` 从列表开头取值，切片终点 `-1` 指向最后一个元素。切片不包含终点，因此只去掉末尾的 `1`，得到 `[1, 2, 3, 4, 5, 4, 3, 2]`，所以选 C。

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

`lst.append(5)` 会把整数 `5` 作为一个新元素追加到 `lst` 末尾，所以选 B。

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

用 `'/'` 作分隔符时，每组相邻的两个斜杠之间都会产生一个空字符串。因此分割结果是 `['3', '', '11', '', '2018']`，共 `5` 个元素。

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

这道题由四步操作串联而成，建议从里到外逐步拆解：

1. **`range(2,12,2)`**：从 2 开始、到 12（不含）结束、步长为 2，生成 `2, 4, 6, 8, 10`。
2. **`list(...)`**：把这个 range 对象转换成列表 `[2, 4, 6, 8, 10]`。
3. **`[:-2]`**：切片操作，`-2` 表示从末尾往前数第 2 个位置，`[:-2]` 表示"取到倒数第 2 个之前"，也就是去掉最后两个元素，留下 `[2, 4, 6]`。
4. **`.pop()`**：不带参数时，默认删除并返回列表的**最后一个**元素，这里是 `6`。

因此最终结果是 `6`。

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

理解本题的关键是：`.format()` 的位置参数编号**从 0 开始**，而且格式字符串里 `{编号}` 出现的顺序可以和参数顺序不一致，按编号去对应参数即可，不需要按从左到右的顺序读参数。

先列出参数与编号的对应关系：

| 编号 | `{0}` | `{1}` | `{2}` |
|---|---|---|---|
| 参数 | `2` | `3` | `2+3=5` |

格式字符串是 `"{1}+{0}={2}"`，依次取出对应编号的参数填进去：`{1}` → `3`，`{0}` → `2`，`{2}` → `5`。

拼接起来得到 `3+2=5`。

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

`{first}` 和 `{second}` 按名称分别取到 `a` 的值 `34` 和 `b` 的值 `23`。`{0}` 取第一个位置参数 `34-23` 的值 `11`，输出 `34-23=11`。

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

`bin(31)` 得到 `'0b11111'`，切片 `[2:]` 去掉前缀 `0b`。格式说明 `:>08s` 把剩下的 5 个字符右对齐到 8 位，左侧补 3 个零，输出 `00011111`。

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

`"programming"` 中没有字符 `x`。`find("x")` 在找不到目标时返回 `-1`，因此输出 `-1`。

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

`strip()`、`lstrip()`、`rstrip()` 这三个方法的区别只在于去除空白的**方向**，可以从前缀字母记忆：`l` 是 left（左），`r` 是 right（右），不带前缀的 `strip()` 两边都去除。

原字符串左边有 3 个空格，右边有 2 个空格，中间是 `xyz`，用 `□` 标记一个空格记作 `□□□xyz□□`。分别处理：

- **`strip()`**：左右两边的空格都去掉，只留下 `xyz`。
- **`rstrip()`**：只去掉右边的空格，左边的 3 个空格保留，得到 `□□□xyz`。
- **`lstrip()`**：只去掉左边的空格，右边的 2 个空格保留，得到 `xyz□□`。

`print()` 输出多个参数时，默认会在相邻参数之间自动加一个空格分隔，因此三段结果拼接后要再插入两个分隔空格：`xyz` + `□`(分隔符) + `□□□xyz` + `□`(分隔符) + `xyz□□`，整理后就是 `xyz□□□□xyz□xyz□□`。

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

理解本题的关键是区分"**让新名字指向同一个对象**"和"**创建一个新对象**"这两种完全不同的操作：

- **`b = a`**：这是单纯的赋值，并没有创建新的列表，只是让 `b` 这个名字也指向 `a` 已经指向的那个列表对象（类似贴了第二个标签在同一个对象上）。因此 `a` 和 `b` 的 `id()` 完全相同，`id(a)==id(b)` 为 `True`。
- **`c = a.copy()`**：`.copy()` 会创建一个**新的列表对象**，把 `a` 中的元素依次复制进去，`c` 指向的是这个新对象，和 `a` 是两个不同的列表（虽然内容相同）。因此 `id(a)==id(c)` 为 `False`。
- **`d = a[:]`**：`[:]` 是切片操作，不写起止位置表示取整个列表的副本，同样会创建一个新的列表对象。因此 `id(a)==id(d)` 也为 `False`。

所以三次输出依次是 `True`、`False`、`False`。这也提醒我们：`.copy()` 和 `[:]` 都属于**浅拷贝**，效果上是等价的，都会创建新列表，而普通赋值 `=` 不会创建新对象，只是多了一个指向同一对象的名字。

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

每行都是一个包含学号和姓名的元组。`for id,name in students` 已将两列拆包，所以第一空填 `id,name`。按下标遍历时，`students[index]` 是当前行，再用 `[0]`、`[1]` 取两列，第二空填 `students[index][0],students[index][1]`。

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

元组 `(1,3,5,7,9)` 的元素之和是 `25`，元素个数是 `5`。Python 3 中 `/` 对这两个整数做除法会得到浮点数，因此输出 `5.0`。

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

执行 `t,a=2,t+1` 时，先计算右侧的两个值。此时 `t` 仍是 `1`，所以右侧得到 `(2, 2)`。再依次赋给 `t` 和 `a`，最后 `print(a)` 输出 `2`。

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

先用 `str()` 把整数转换成字符串，这样每一位数字就可以逐个访问。`len(s)` 得到字符串长度，也就是正整数的位数；`sum(int(c) for c in s)` 则把每个字符重新转成整数后求和。例如 `456` 的位数是 3，各位数字之和是 `4+5+6=15`。

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

先读取字符串，并用 `lstrip(' ')` 去掉开头的普通空格，再用 `len()` 计算长度。变量 `longest` 始终保存目前遇到的最大长度；每读入一行，就用 `max(longest, 当前长度)` 更新它。循环结束后输出最大长度。这里使用 `lstrip(' ')`，所以字符串内部和末尾的空格仍会计入长度。

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

<div class="question-tags"><span class="question-tag">字符范围判断</span> <span class="question-tag">ord与chr函数</span> <span class="question-tag">字符串切片</span> <span class="question-tag">回文判断</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
raw = input()
s = ''
for c in raw:
    if 'A' <= c <= 'Z':
        s += chr(ord(c) - ord('A') + ord('a'))
    elif 'a' <= c <= 'z':
        s += c
    elif '0' <= c <= '9':
        s += c
print('yes' if s == s[::-1] else 'no')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

本题要先把输入"清洗"成只含数字和小写字母的字符串，再判断是否回文。清洗的时候要同时处理两件事：筛选字符、统一大小写，可以用三个分支依次判断：

- **`if 'A' <= c <= 'Z'`：`c` 是大写字母。** 字母和数字在字符编码表中都是连续排列的，所以可以直接用范围比较判断类型，不借助 `isalpha()`/`isalnum()` 这类内置方法。大写字母需要转成小写再保留：大写字母和对应小写字母在编码表中相差一个固定的偏移量 `ord('a') - ord('A')`，所以 `chr(ord(c) - ord('A') + ord('a'))` 能把任意大写字母 `c` 换算成对应的小写字母，换算后再拼接到 `s` 中。
- **`elif 'a' <= c <= 'z'`：`c` 已经是小写字母。** 不需要转换，直接拼接到 `s` 中。
- **`elif '0' <= c <= '9'`：`c` 是数字字符。** 同样直接拼接到 `s` 中。

如果 `c` 不满足以上任何一种情况（比如空格、逗号、分号等标点），三个分支都不会执行，`c` 就被跳过，不会进入 `s`。

遍历完整个输入后，`s` 中只剩下统一为小写的字母和数字。最后比较 `s` 和它的逆序 `s[::-1]`：相等就是回文，输出 `yes`；否则输出 `no`。

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

合法的十六进制字符只有 `0-9`、`a-f` 和 `A-F`。程序遍历输入字符串，只保留这些字符，并用 `join()` 组成新的字符串 `h`。`int(h, 16)` 将十六进制字符串转换成十进制整数；如果没有筛选出任何字符，就按代码中的条件输出 0，避免对空字符串调用 `int()`。

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

遍历字符串 A 中的每个字符，判断它是否出现在字符串 B 中。`c in b` 的结果是 `True` 或 `False`，如果为真，就令计数器 `count` 加 1。循环结束后，`count` 就是 A 中同时出现在 B 中的字符个数。题目说明 A 没有重复字符，所以不会重复计数。

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
