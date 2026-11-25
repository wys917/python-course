---
title: 第3章作业
eyebrow: HOMEWORK 03
code: HOMEWORK 03
description: 题目、参考答案与解析。
questionGroups:
  - [判断题, judgment, 24]
  - [单选题, choice, 5]
  - [填空题, blank, 17]
  - [编程题, programming, 17]
---

<div class="editor-note">

题目整理自所提供的 PTA 网页，参考答案按 Python 3 核对，未在 PTA 平台提交验证。原题编号重复时保留原编号，以页面题序区分。

</div>

<h2 id="judgment" class="quiz-group">判断题<span>24 QUESTIONS</span></h2>

:::: question judgment-1 | 1-1 判断题

```python
'age'+23不是正确的表达式。  
```

<div class="question-tags">
<span class="question-tag">字符串拼接</span>
<span class="question-tag">类型转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 可以解析 `'age' + 23`，但执行时会报 `TypeError`：`+` 不能直接把字符串和整数拼接。若想得到 `age23`，需要先把整数转换成字符串：`'age' + str(23)`。因此题目说法正确。
</div>

:::

::::

:::: question judgment-2 | 1-2 判断题

列表可以用find()函数来搜索数据是否在列表中。

<div class="question-tags">
<span class="question-tag">列表查找</span>
<span class="question-tag">find 方法</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`find()` 是字符串方法，列表没有这个方法。判断元素是否在列表中，可以使用 `x in lst`；如果需要查找元素第一次出现的位置，可以使用 `lst.index(x)`。因此题目说法错误。
</div>

:::

::::

:::: question judgment-3 | 1-3 判断题

将列表中的元素顺序打乱的函数shuffle()不是random模块的函数或方法。

<div class="question-tags">
<span class="question-tag">random 模块</span>
<span class="question-tag">shuffle 方法</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`shuffle()` 是 `random` 模块提供的方法，用于随机打乱列表中的元素顺序。例如 `random.shuffle(lst)` 会直接修改原列表。因此题目说它不是 `random` 模块的方法，错误。注意：`shuffle()` 原地修改列表，返回值是 `None`。
</div>

:::

::::

:::: question judgment-4 | 1-4 判断题

字符串和列表都是序列类型。

<div class="question-tags">
<span class="question-tag">序列类型</span>
<span class="question-tag">字符串与列表</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

字符串和列表都属于序列类型，都有确定的元素顺序，可以通过下标访问元素，也支持切片和 `len()`。区别在于：字符串不可变，列表可变。因此本题正确。
</div>

:::

::::

:::: question judgment-5 | 1-5 判断题

可以通过[]来访问字符串的某个字符，也可以将它修改成其他字符。

<div class="question-tags">
<span class="question-tag">字符串索引</span>
<span class="question-tag">字符串不可变</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

字符串可以通过下标读取字符，例如 `s[0]`，但不能通过下标直接修改字符。执行 `s[0] = 'B'` 会报错，因为字符串是不可变对象。若要替换字符，需要构造一个新字符串。因此本题错误。
</div>

:::

::::

:::: question judgment-6 | 1-6 判断题

字符串对象和元组对象是不可变对象，列表对象为可变对象。

<div class="question-tags">
<span class="question-tag">可变与不可变对象</span>
<span class="question-tag">列表与元组</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

字符串和元组创建后，不能直接修改其中某个位置的元素；列表则可以通过下标修改，也可以增删元素。因此字符串、元组是不可变对象，列表是可变对象，本题正确。
</div>

:::

::::

:::: question judgment-7 | 1-7 判断题

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[::]的结果是[12, -5, -22, -10, -26, 35, 0, 49, 3, -21]。

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">切片步长</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst[::]` 省略了起点、终点和步长，默认从头到尾、每次取一个元素，因此会得到包含原列表全部元素的新列表。它与原列表内容相同，但外层列表对象是新建的。本题正确。
</div>

:::

::::

:::: question judgment-8 | 1-8 判断题

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[::-1]的结果是[-21, 3, 49, 0, 35, -26, -10, -22, -5, 12]。

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">列表逆序</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

切片中的步长为 `-1`，表示从右向左每次移动一个位置。`lst[::-1]` 因此会把列表中的元素按相反顺序取出，结果正好是题目给出的逆序列表。本题正确。
</div>

:::

::::

:::: question judgment-9 | 1-9 判断题

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[::2]的结果是[12, -22, -26, 0, 3]。

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">切片步长</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst[::2]` 表示从下标 0 开始，每次向后移动 2 个位置，所以依次取得下标 `0、2、4、6、8` 的元素：`[12, -22, -26, 0, 3]`。与题目一致，因此正确。
</div>

:::

::::

:::: question judgment-10 | 1-10 判断题

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[1::2]的结果是[12, -22, -26, 0, 3]。

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">切片起点</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst[1::2]` 从下标 1 开始，每次移动 2 位，取得下标 `1、3、5、7、9` 的元素，结果是 `[-5, -10, 35, 49, -21]`，与题目给出的结果不同，因此错误。
</div>

:::

::::

:::: question judgment-11 | 1-11 判断题

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[3:8:2]的结果是[-10, 35, 49]。

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">切片终点</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst[3:8:2]` 从下标 3 开始，每次增加 2，直到下标达到 8 前停止。实际取得下标 `3、5、7`，对应 `-10、35、49`。切片的终点 8 不包含在结果中，因此本题正确。
</div>

:::

::::

:::: question judgment-12 | 1-12 判断题

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[0:100]的结果是错误。

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">切片越界</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

切片的起止位置超出列表范围时，Python 会自动截取到合法边界，不会因此报错。`lst[0:100]` 会从开头一直取到列表末尾，结果就是整个列表。因此“结果是错误”的说法不正确。
</div>

:::

::::

:::: question judgment-13 | 1-13 判断题

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[100:]的结果是[]。

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">切片越界</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst[100:]` 表示从下标 100 开始取到末尾。列表没有这么大的下标，因此切片结果为空列表 `[]`。切片越界不会报错，所以本题正确。
</div>

:::

::::

:::: question judgment-14 | 1-14 判断题

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[100]的结果是运行错误。

<div class="question-tags">
<span class="question-tag">列表索引</span>
<span class="question-tag">索引越界</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst[100]` 是直接访问下标为 100 的单个元素。列表长度只有 10，下标范围是 `0` 到 `9`，因此会触发 `IndexError`。注意：单个索引越界会报错，切片越界通常会自动截取。
</div>

:::

::::

:::: question judgment-15 | 1-15 判断题

下面的程序当输入是 `c d e a`时，输出是 `a c d e`。

```python
a = input().split(" ")
for i in a.sort():    
    print(i,end=" ")
```

<div class="question-tags">
<span class="question-tag">sort 方法</span>
<span class="question-tag">列表方法返回值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`a.sort()` 会直接对列表 `a` 排序，但它的返回值是 `None`。因此 `for i in a.sort()` 实际上是在遍历 `None`，会报 `TypeError`，程序无法按题目所说输出。正确写法是先执行 `a.sort()`，再遍历 `a`。
</div>

:::

::::

:::: question judgment-16 | 1-16 判断题

表达式：`"34" in "1234"==True` 返回值是True。

<div class="question-tags">
<span class="question-tag">链式比较</span>
<span class="question-tag">in 运算符</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

Python 会把 `a < b < c` 这样的表达式理解为 `a < b and b < c`。因此，`'34' in '1234' == True` 相当于同时判断 `'34' in '1234'` 和 `'1234' == True`。前者为真，后者为假，所以整体结果为 `False`。若想先判断成员关系再与 `True` 比较，需要加括号。
</div>

:::

::::

:::: question judgment-17 | 1-17 判断题

下面程序输出是`yes`。

```python
lst=["1","2","3","4","5"]
s1=""
for c in lst:
    s1=s1+c+" "
s2=" ".join(lst)
if s1==s2:
    print("yes")
else:
    print("no")
```

<div class="question-tags">
<span class="question-tag">join 方法</span>
<span class="question-tag">字符串比较</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

循环中每次都执行 `s1 = s1 + c + ' '`，所以 `s1` 最后会多出一个末尾空格。`' '.join(lst)` 只在元素之间添加空格，不会在末尾添加空格。两个字符串因此不相等，程序输出 `no`，本题说输出 `yes` 是错误的。
</div>

:::

::::

:::: question judgment-18 | 1-18 判断题

`"12 "*3==" ".join(["12","12","12"])` 的输出是True

<div class="question-tags">
<span class="question-tag">字符串重复</span>
<span class="question-tag">空格处理</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`'12 ' * 3` 的结果是 `'12 12 12 '`，末尾仍然有一个空格。`' '.join(['12','12','12'])` 的结果是 `'12 12 12'`，只在元素之间放空格。两者末尾是否有空格不同，因此比较结果为 `False`。
</div>

:::

::::

:::: question judgment-19 | 1-19 判断题

语句`print("输出结果是{:8s}".format("this"))`的输出是：输出结果是 $\Box$$\Box$$\Box$$\Box$this。  
 $\Box$表示空格。

<div class="question-tags">
<span class="question-tag">format 方法</span>
<span class="question-tag">字符串对齐</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

格式说明 `{:8s}` 表示字符串占用宽度至少为 8。字符串默认左对齐，因此 `this` 后面补 4 个空格，结果是 `this□□□□`，而不是在 `this` 前面补空格。本题错误。
</div>

:::

::::

:::: question judgment-20 | 1-20 判断题

语句`print("输出结果是{:8d}".format(1234))`的输出是：输出结果是 1234□□□□。 □表示空格。

<div class="question-tags">
<span class="question-tag">format 方法</span>
<span class="question-tag">数字对齐</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

格式说明 `{:8d}` 表示整数按十进制显示，字段宽度为 8。整数默认右对齐，`1234` 前面会补 4 个空格，实际结果是 `□□□□1234`，不是题目描述的格式。因此本题错误。
</div>

:::

::::

:::: question judgment-21 | 1-21 判断题

语句`print("输出结果是{:08.2f}".format(14.345))`的输出是：输出结果是00014.34。

<div class="question-tags">
<span class="question-tag">浮点数</span>
<span class="question-tag">格式化输出</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`{:08.2f}` 的格式说明可以拆成三部分理解：`0` 表示不足宽度时在左侧补 `0`（而不是补空格），`8` 表示总宽度至少为 8（包括小数点和符号），`.2f` 表示按浮点数显示并保留 2 位小数。

容易出错的地方在于：很多人凭直觉认为 `14.345` 保留两位小数应该是"四舍五入到 `14.34`"还是"`14.35`"存在争议，但这其实不是重点——真正的原因在于**浮点数在计算机里无法精确存储十进制小数**。`14.345` 这个十进制小数转换成二进制浮点数后，实际存储的值并不是正好的 `14.345`，而是 `14.34500000000000063949...`，比 `14.345` 略大一点点。

因此按正常的四舍五入规则处理这个略大于 `14.345` 的实际值，第三位小数（`5` 往后那一位）对应的结果是进位，保留两位小数后得到 `14.35`。再加上宽度为 8、左侧补 `0`，最终输出是 `00014.35`。

题目说输出是 `00014.34`，与实际结果 `00014.35` 不符，因此本题错误。这也提醒我们：涉及浮点数的精确结果时，不能单纯凭十进制直觉去猜测，最好的办法是直接在 Python 里运行验证。
</div>

:::

::::

:::: question judgment-22 | 1-22 判断题

[1,2,[3]]+[4,5]的结果是[1,2,3,4,5]。

<div class="question-tags">
<span class="question-tag">列表拼接</span>
<span class="question-tag">嵌套列表</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

列表的 `+` 会把两个列表的元素依次连接起来，不会自动展开内部的嵌套列表。因此 `[1, 2, [3]] + [4, 5]` 的结果是 `[1, 2, [3], 4, 5]`，其中 `[3]` 仍然是一个子列表。本题错误。
</div>

:::

::::

:::: question judgment-23 | 1-23 判断题

[4,5]`*`3的结果是[[4,5],[4,5],[4,5]]。

<div class="question-tags">
<span class="question-tag">列表重复</span>
<span class="question-tag">序列运算</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

列表乘以整数表示重复列表中的元素。`[4, 5] * 3` 得到 `[4, 5, 4, 5, 4, 5]`，不会把原列表整体复制成三个嵌套列表。因此本题错误。
</div>

:::

::::

:::: question judgment-24 | 1-24 判断题

下面程序的输出是字符`a`

```python
c="A"
print(c.lower)
```

<div class="question-tags">
<span class="question-tag">字符串方法</span>
<span class="question-tag">lower 方法</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`c.lower` 只是取得 `lower` 方法本身，并没有执行大小写转换。调用方法时需要加括号：`c.lower()`，结果才是字符串 `'a'`。原程序打印的是方法对象，不会输出字符 `a`，因此本题错误。
</div>

:::

::::

<h2 id="choice" class="quiz-group">单选题<span>05 QUESTIONS</span></h2>

:::: question choice-1 | 2-1 单选题

max((3, 5, 1, 7, 4))的结果是____。

**A.** 1

**B.** 3

**C.** 5

**D.** 7

<div class="question-tags">
<span class="question-tag">max 函数</span>
<span class="question-tag">元组</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

D。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

传给 `max()` 的元组是 `(3, 5, 1, 7, 4)`。其中最大的整数是 `7`，所以选 D。
</div>

:::

::::

:::: question choice-2 | 2-2 单选题

以下哪句打印出smith\exam1\test.txt？

**A.** `print("smith\exam1\test.txt")`

**B.** `print("smith\\exam1\\test.txt")`

**C.** `print("smith\"exam1\"test.txt")`

**D.** `print("smith"\exam1"\test.txt")`

<div class="question-tags">
<span class="question-tag">字符串转义</span>
<span class="question-tag">反斜杠</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

要输出 `smith\exam1\test.txt`，两个分隔位置都需要一个反斜杠。在普通字符串字面量中，`\\` 表示一个反斜杠，所以选 B。选项 A 中的 `\t` 会被解释为制表符。
</div>

:::

::::

:::: question choice-3 | 2-3 单选题

list("abcd")的结果是?

**A.** ['a', 'b', 'c', 'd']

**B.** ['ab']

**C.** ['cd']

**D.** ['abcd']

<div class="question-tags">
<span class="question-tag">list 函数</span>
<span class="question-tag">字符串遍历</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`list("abcd")` 按顺序读取字符串中的每个字符，每个字符成为一个列表元素，得到 `['a', 'b', 'c', 'd']`，所以选 A。
</div>

:::

::::

:::: question choice-4 | 2-4 单选题

如果list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]，那么以下那个是list1[:-1]？

**A.** 0

**B.** [1, 2, 3, 4, 5, 4, 3, 2, 1]

**C.** [1, 2, 3, 4, 5, 4, 3, 2]

**D.** [0, 1, 2, 3, 4, 3, 2, 1, 0]

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">负索引</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`list1[:-1]` 从列表开头取值，切片终点 `-1` 指向最后一个元素。切片不包含终点，因此只去掉末尾的 `1`，得到 `[1, 2, 3, 4, 5, 4, 3, 2]`，所以选 C。
</div>

:::

::::

:::: question choice-5 | 2-5 单选题

要把5加到列表lst的末尾，用的是___ 。

**A.** lst.add(5)

**B.** lst.append(5)

**C.** lst.addLast(5)

**D.** lst.addEnd(5)

<div class="question-tags">
<span class="question-tag">列表方法</span>
<span class="question-tag">append 方法</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst.append(5)` 会把整数 `5` 作为一个新元素追加到 `lst` 末尾，所以选 B。
</div>

:::

::::

<h2 id="blank" class="quiz-group">填空题<span>17 QUESTIONS</span></h2>

:::: question blank-1 | 4-1 填空题

'23'*3的结果是_______。 _____ (答案不要加引号）

<div class="question-tags">
<span class="question-tag">字符串重复</span>
<span class="question-tag">乘法运算符</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`232323`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`'23'` 是字符串，乘以整数 `3` 会把它连续重复三次。按题意去掉表示字符串的引号，填 `232323`。
</div>

:::

::::

:::: question blank-2 | 4-2 填空题

len('3//11//2018'.split('/'))的结果是_____。 _____

<div class="question-tags">
<span class="question-tag">split 方法</span>
<span class="question-tag">len 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`5`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

用 `'/'` 作分隔符时，每组相邻的两个斜杠之间都会产生一个空字符串。因此分割结果是 `['3', '', '11', '', '2018']`，共 `5` 个元素。
</div>

:::

::::

:::: question blank-3 | 4-3 填空题

lst=[3,4,5,6,5,4,3],执行lst.remove(3)后，lst[0]的值是：_。 _____

<div class="question-tags">
<span class="question-tag">remove 方法</span>
<span class="question-tag">列表索引</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`4`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`lst.remove(3)` 删除从左往右遇到的第一个 `3`。列表变为 `[4, 5, 6, 5, 4, 3]`，所以新的 `lst[0]` 是 `4`。
</div>

:::

::::

:::: question blank-4 | 4-4 填空题

list(range(2,12,2))[:-2].pop()的结果是：_____。 _____

<div class="question-tags">
<span class="question-tag">列表切片</span>
<span class="question-tag">pop 方法</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`6`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这道题由三步操作串联而成，建议从里到外逐步拆解：

1. **`range(2,12,2)`**：从 2 开始、到 12（不含）结束、步长为 2，生成 `2, 4, 6, 8, 10`。
2. **`list(...)`**：把这个 range 对象转换成列表 `[2, 4, 6, 8, 10]`。
3. **`[:-2]`**：切片操作，`-2` 表示从末尾往前数第 2 个位置，`[:-2]` 表示"取到倒数第 2 个之前"，也就是去掉最后两个元素，留下 `[2, 4, 6]`。
4. **`.pop()`**：不带参数时，默认删除并返回列表的**最后一个**元素，这里是 `6`。

因此最终结果是 `6`。
</div>

:::

::::

:::: question blank-5 | 4-5 填空题

要想得到[0,100]范围内的随机数，random.randint(0,n)里的n应该是：___。 _____

<div class="question-tags">
<span class="question-tag">randint 函数</span>
<span class="question-tag">随机整数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`100`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`random.randint(0,n)` 可以取到两个端点，包括上限 `n`。要覆盖从 0 到 100 的所有整数，且最大值恰好为 100，应填 `100`。
</div>

:::

::::

:::: question blank-6 | 4-6 填空题

`print("{1}+{0}={2}".format(2,3,2+3))`的输出是 _____ (答案不要加引号）。

<div class="question-tags">
<span class="question-tag">format 方法</span>
<span class="question-tag">位置参数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`3+2=5`。

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

:::: question blank-7 | 4-7 填空题

```python
a=34
b=23
print("{first}-{second}={0}".format(34-23,first=a,second=b))
```

上面程序输出是 _____ (答案不要加引号）。

<div class="question-tags">
<span class="question-tag">format 方法</span>
<span class="question-tag">关键字参数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`34-23=11`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`{first}` 和 `{second}` 按名称分别取到 `a` 的值 `34` 和 `b` 的值 `23`。`{0}` 取第一个位置参数 `34-23` 的值 `11`，输出 `34-23=11`。
</div>

:::

::::

:::: question blank-8 | 4-8 填空题

`print("{:>08s}".format(bin(31)[2:]))`的输出是 _____ 。

<div class="question-tags">
<span class="question-tag">bin 函数</span>
<span class="question-tag">格式化补零</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`00011111`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`bin(31)` 得到 `'0b11111'`，切片 `[2:]` 去掉前缀 `0b`。格式说明 `:>08s` 把剩下的 5 个字符右对齐到 8 位，左侧补 3 个零，输出 `00011111`。
</div>

:::

::::

:::: question blank-9 | 4-9 填空题

`print("programming".find("r",2))`的输出是 _____ 。

。

<div class="question-tags">
<span class="question-tag">find 方法</span>
<span class="question-tag">字符串索引</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`4`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`"programming"` 中两个 `r` 的下标分别是 `1` 和 `4`。`find("r",2)` 从下标 `2` 开始向右查找，返回找到的第一个 `r` 在原字符串中的下标 `4`。
</div>

:::

::::

:::: question blank-10 | 4-10 填空题

`print("programming".find("x"))`的输出是 _____ 。

<div class="question-tags">
<span class="question-tag">find 方法</span>
<span class="question-tag">字符串查找</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`-1`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`"programming"` 中没有字符 `x`。`find("x")` 在找不到目标时返回 `-1`，因此输出 `-1`。
</div>

:::

::::

:::: question blank-11 | 4-11 填空题

`print("a123".isdigit())`的输出是 _____ 。

<div class="question-tags">
<span class="question-tag">isdigit 方法</span>
<span class="question-tag">数字字符</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`False`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`isdigit()` 要求字符串非空且每个字符都是数字字符。`"a123"` 的首字符 `a` 是字母，所以输出 `False`。
</div>

:::

::::

:::: question blank-12 | 4-12 填空题

`print("aABC".isalpha())`的输出是 _____ 。

<div class="question-tags">
<span class="question-tag">isalpha 方法</span>
<span class="question-tag">字母判断</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`True`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`"aABC"` 是非空字符串，四个字符都是字母。大小写都符合 `isalpha()` 的条件，所以输出 `True`。
</div>

:::

::::

:::: question blank-13 | 4-13 填空题

print("$\Box$$\Box$$\Box$xyz$\Box$$\Box$".strip(),"$\Box$$\Box$$\Box$xyz$\Box$$\Box$".rstrip(),  
"$\Box$$\Box$$\Box$xyz$\Box$$\Box$".lstrip())的输出是 _____ 。（答案不要加引号，$\Box$表示空格）

<div class="question-tags">
<span class="question-tag">strip 方法</span>
<span class="question-tag">空格输出</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`xyz□□□□xyz□xyz□□`（□ 表示空格）。

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

:::: question blank-14 | 4-14 填空题

```python
a=[1,2,3,4]
b=a
print(id(a)==id(b))
c=a.copy()
print(id(a)==id(c))
d=a[:]
print(id(a)==id(d))
```

上面程序的输出依次分别是： _____ , _____ , _____ 。

<div class="question-tags">
<span class="question-tag">对象身份</span>
<span class="question-tag">列表浅拷贝</span>
</div>

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

:::: question blank-15 | 4-15 填空题

列表加元组可以表示二维表。

![捕获.PNG](/images/problems/3691b42b6062.png)

下面程序用三种不同方式打印表格内容，请填空完成与第一种方式输出一样的后面两种方式，不要加无用空格。

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
    print(_____)
print()

for index in range(len(students)):  #按索引存取
    print(_____)   
```

<div class="question-tags">
<span class="question-tag">元组拆包</span>
<span class="question-tag">嵌套索引</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

第1空：`id,name`；第2空：`students[index][0],students[index][1]`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

每行都是一个包含学号和姓名的元组。`for id,name in students` 已将两列拆包，所以第一空填 `id,name`。按下标遍历时，`students[index]` 是当前行，再用 `[0]`、`[1]` 取两列，第二空填 `students[index][0],students[index][1]`。
</div>

:::

::::

:::: question blank-16 | 4-16 填空题

`print(sum((1,3,5,7,9))/len((1,3,5,7,9)))`的输出是 _____ 。

<div class="question-tags">
<span class="question-tag">sum 函数</span>
<span class="question-tag">平均值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`5.0`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

元组 `(1,3,5,7,9)` 的元素之和是 `25`，元素个数是 `5`。Python 3 中 `/` 对这两个整数做除法会得到浮点数，因此输出 `5.0`。
</div>

:::

::::

:::: question blank-17 | 4-17 填空题

下面程序的输出是 _____ 。

```python
t=1
t,a=2,t+1
print(a)
```

<div class="question-tags">
<span class="question-tag">多重赋值</span>
<span class="question-tag">求值顺序</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`2`。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

执行 `t,a=2,t+1` 时，先计算右侧的两个值。此时 `t` 仍是 `1`，所以右侧得到 `(2, 2)`。再依次赋给 `t` 和 `a`，最后 `print(a)` 输出 `2`。
</div>

:::

::::

<h2 id="programming" class="quiz-group">编程题<span>17 QUESTIONS</span></h2>

:::: question programming-1 | 7-1 大于身高的平均值

中小学生每个学期都要体检，要量身高，因为身高可以反映孩子的生长状况。现在，一个班的身高已经量好了，请输出其中超过平均身高的那些身高。程序的输入为一行数据，其中以空格分隔，每个数据都是一个正整数。程序要输出那些超过输入的正整数的平均数的输入值，每个数后面有一个空格，输出的顺序和输入的相同。

#### 输入格式:

在一行输入中一个班的身高值，以空格分隔。

#### 输出格式:

在一行输出超过输入的平均数的输入值，以空格分隔。

#### 输入样例:

在这里给出一组输入。例如：

```text
143 174 119 127 117 164 110 128
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
143 174 164 
```

<div class="question-tags">
<span class="question-tag">map 函数</span>
<span class="question-tag">sum 函数</span>
<span class="question-tag">平均值</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
heights = list(map(int, input().split()))
total = sum(heights)
for height in heights:
    if height * len(heights) > total:
        print(height, end=' ')
print()
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先用 `input().split()` 将一行输入拆成多个字符串，再用 `map(int, ...)` 转成整数列表。`sum()` 求总身高，`len()` 求人数。判断某个身高是否超过平均值，可以直接比较 `height * 人数 > 总和`，避免先计算浮点平均值。循环按原顺序输出符合条件的身高，`end=' '` 让每个数字后面保留一个空格。
</div>

:::

::::

:::: question programming-2 | 7-2 输出字母在字符串中位置索引

输入一个字符串，再输入两个字符，求这两个字符在字符串中的索引。

#### 输入格式:

第一行输入字符串  
第二行输入两个字符，用空格分开。

#### 输出格式:

从右向左输出字符和索引，即下标最大的字符最先输出。每行一个。

#### 输入样例:

在这里给出一组输入。例如：

```text
pmispsissippi
s p
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
11 p
10 p
8 s
7 s
5 s
4 p
3 s
0 p
```

<div class="question-tags">
<span class="question-tag">字符串索引</span>
<span class="question-tag">range 函数</span>
<span class="question-tag">倒序遍历</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
a, b = input().split()
for i in range(len(s) - 1, -1, -1):
    if s[i] == a or s[i] == b:
        print(i, s[i])
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

本题要"从右向左"遍历字符串，关键在于 `range()` 的三个参数怎么构造倒序序列：`range(起点, 终点, 步长)`，要从右往左，步长就要写成 `-1`（每次减 1）；起点是字符串最后一个合法下标 `len(s)-1`；终点要写成 `-1` 而不是 `0`，因为 `range()` 不包含终点，写 `-1` 才能让下标 `0` 也被取到。

循环体中，`s[i] == a or s[i] == b` 判断当前字符是否等于两个目标字符中的任意一个，只要满足就用 `print(i, s[i])` 输出下标和字符（`print()` 的多个参数默认用一个空格分隔）。

按这个顺序遍历，下标从大到小依次检查，凡是等于 `s` 或 `p` 的位置就打印出来，正好符合"从右向左、下标最大的先输出"的要求。
</div>

:::

::::

:::: question programming-3 | 7-3 求整数的位数及各位数字之和

对于给定的正整数N，求它的位数及其各位数字之和。(提示：把整数转换成字符串，列表，用sum和len函数)

#### 输入格式:

输入在一行中给出一个正整数N。

#### 输出格式:

在一行中输出N的位数及其各位数字之和，中间用一个空格隔开。

#### 输入样例:

在这里给出一组输入。例如：

```text
456
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
3 15
```

<div class="question-tags">
<span class="question-tag">str 函数</span>
<span class="question-tag">len 函数</span>
<span class="question-tag">sum 函数</span>
</div>

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

:::: question programming-4 | 7-4 字符替换

本题要求编写程序，将输入字符串中的大写英文字母按以下对应规则替换，其他字符不变。(提示：转换表用元组实现）

| 原字母 | 对应字母 |
| --- | --- |
| A | Z |
| B | Y |
| C | X |
| D | W |
| ... | ... |
| X | C |
| Y | B |
| Z | A |

#### 输入格式:

在一行中输入字符串

#### 输出格式:

在一行中给出替换完成后的字符串。

#### 输入样例:

在这里给出一组输入。例如：

```text
This is a pen.
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
Ghis is a pen.
```

<div class="question-tags">
<span class="question-tag">ord 函数</span>
<span class="question-tag">chr 函数</span>
<span class="question-tag">字符串拼接</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
result = ''
for c in s:
    if 'A' <= c <= 'Z':
        result += chr(ord('A') + ord('Z') - ord(c))
    else:
        result += c
print(result)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

观察替换规则表可以发现一个规律：A↔Z、B↔Y、C↔X……每一对字母在字母表中的位置正好是"对称"的，A 是第一个、Z 是最后一个，离两端的距离相等。这种对称关系可以用一个公式表示：

`chr(ord('A') + ord('Z') - ord(c))`

意思是用 `ord('A') + ord('Z')` 这个固定的和，减去当前字母 `c` 的编码，再转换回字符。例如 `c='A'` 时，结果是 `ord('Z')`，对应字符 `Z`；`c='T'` 时，`ord('A')+ord('Z')-ord('T') = 65+90-84 = 71`，对应字符 `G`。可以验证这个公式对 A~Z 中任意一个字母都成立。

程序中用 `result = ''` 作为空字符串起点，遍历输入字符串 `s` 中的每个字符 `c`：如果 `c` 是大写字母（`'A' <= c <= 'Z'`），就按公式算出替换后的字母拼接到 `result` 末尾；否则原样保留该字符。遍历结束后，`result` 就是替换完成的字符串。
</div>

:::

::::

:::: question programming-5 | 7-5 删除字符

输入一个字符串 str，再输入要删除字符 c(非空格字符），大小写不区分，将字符串 str 中出现的所有字符 c 删除。提示：去掉两端的空格。

#### 输入格式:

在第一行中输入一行字符  
在第二行输入待删除的字符

#### 输出格式:

在一行中输出删除后的字符串

#### 输入样例1:

在这里给出一组输入。例如：

```text
        Bee
   E
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
result: B
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
  7!jdk*!ASyu
  !
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
result: 7jdk*ASyu
```

<div class="question-tags">
<span class="question-tag">strip 方法</span>
<span class="question-tag">lower 方法</span>
<span class="question-tag">join 方法</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input().strip()
target = input().strip().lower()
result = ''
for c in s:
    if c.lower() != target:
        result += c
print('result:', result)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先处理输入：第一行、第二行都先用 `strip()` 去掉两端多余的空格，避免空格干扰判断；待删除字符额外用 `.lower()` 转成小写，作为后续比较的统一标准。

接着用一个普通的 `for` 循环逐个检查原字符串 `s` 中的每个字符 `c`：

- 把 `c` 也转成小写（`c.lower()`），和目标字符 `target` 比较。
- 如果两者不相等，说明 `c` 不是要删除的字符，就把 `c`（注意是原字符 `c`，不是转换后的小写字符）拼接到 `result` 后面。
- 如果相等，就跳过这个字符，不拼接，相当于把它删除了。

循环结束后，`result` 里保留的就是去掉所有目标字符（不区分大小写）之后的字符串，且每个字符都保留了原来的大小写。
</div>

:::

::::

:::: question programming-6 | 7-6 输出10个不重复的英文字母

随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。  
如没有10个英文字母，显示信息“not found”

#### 输入格式:

在一行中输入字符串

#### 输出格式:

在一行中输出最左边的10个不重复的英文字母或显示信息“not found"

#### 输入样例1:

在这里给出一组输入。例如：

```text
poemp134567
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
not found
```

#### 输入样例2

在这里给出一组输入。例如：

```text
This 156is a test example
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
Thisaexmpl
```

<div class="question-tags">
<span class="question-tag">set 集合</span>
<span class="question-tag">字符串去重</span>
<span class="question-tag">break 语句</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
seen = set()
result = ''
for c in s:
    if ('a' <= c <= 'z' or 'A' <= c <= 'Z') and c.lower() not in seen:
        seen.add(c.lower())
        result += c
        if len(result) == 10:
            break
print(result if len(result) == 10 else 'not found')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`seen` 集合用来记录已经出现过的字母。遍历字符串时，先判断字符是否为英文字母，再用 `c.lower()` 统一大小写后检查是否出现过；第一次出现才加入集合和结果字符串。找到 10 个后用 `break` 提前结束循环。最后若结果长度不足 10，就输出 `not found`。
</div>

:::

::::

:::: question programming-7 | 7-7 逆序的三位数

程序每次读入一个正3位数，然后输出按位逆序的数字。注意：当输入的数字含有结尾的0时，输出不应带有前导的0。比如输入700，输出应该是7。

#### 输入格式：

每个测试是一个3位的正整数。

#### 输出格式：

输出按位逆序的数。

#### 输入样例：

```text
123
```

#### 输出样例：

```text
321
```

**鸣谢安阳师范学院软件学院李康康同学补充数据！**

<div class="question-tags">
<span class="question-tag">字符串切片</span>
<span class="question-tag">int 类型转换</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
print(int(input().strip()[::-1]))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`input()` 读入的三位数先作为字符串处理。`[::-1]` 将字符顺序反转，例如 `'700'` 变成 `'007'`。再用 `int()` 转成整数，前面的零会自动去掉，因此输出 `7`，而不是 `007`。
</div>

:::

::::

:::: question programming-8 | 7-8 判断两个字符串是否为变位词

如果一个字符串是 另一个字符串的重新排列组合，那么这两个字符串互为变位词。比如，”heart”与”earth”互为变位 词，”Mary”与”arMy”也互为变位词。

#### 输入格式:

第一行输入第一个字符串，第二行输入第二个字符串。

#### 输出格式:

输出“yes”,表示是互换词，输出“no”,表示不是互换词。

#### 输入样例1:

在这里给出一组输入。例如：

```text
Mary
arMy
```

#### 输出样例1

在这里给出相应的输出。例如：

```text
yes
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
hello 114
114 hello
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
yes
```

#### 输入样例3:

在这里给出一组输入。例如：

```text
Wellcom
mocllew
```

#### 输出样例3:

在这里给出相应的输出。例如：

```text
no
```

<div class="question-tags">
<span class="question-tag">sorted 函数</span>
<span class="question-tag">字符串比较</span>
<span class="question-tag">变位词</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a = input().lower()
b = input().lower()
print('yes' if sorted(a) == sorted(b) else 'no')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

变位词要求两个字符串包含完全相同的字符，并且每个字符出现的次数也相同。先用 `lower()` 忽略大小写，再用 `sorted()` 将字符排序；如果排序后的两个列表相等，就说明字符及其出现次数完全一致。注意不能只比较 `set()`，因为集合会丢失重复次数。题目样例 3 中 `Wellcom` 与 `mocllew` 实际上也是变位词，按题意应输出 `yes`，与原样例给出的 `no` 不一致。
</div>

:::

::::

:::: question programming-9 | 7-9 输入字符串，排序后输出最大字符及该字符在原字符串中的索引

输入字符串，排序后输出最大字符及该字符在原字符串中的索引。相同字符的索引取最大值。提示：用元组实现。

#### 输入格式:

在一行输入字符串。

#### 输出格式:

在一行输出字符和索引。

#### 输入样例:

在这里给出一组输入。例如：

```text
Hello Python
```

#### 输出样例:

在这里给出相应的输出。字符和数字间空3格。例如：

```text
y   7
```

<div class="question-tags">
<span class="question-tag">enumerate 函数</span>
<span class="question-tag">max 函数</span>
<span class="question-tag">元组比较</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
char, index = max((c, i) for i, c in enumerate(s))
print(f'{char}   {index}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`enumerate(s)` 同时提供每个字符的下标和字符，生成 `(字符, 下标)` 元组。`max()` 比较元组时先比较第一个元素，也就是字符；字符相同时再比较下标，因此会选中最大字符最后一次出现的位置。最后用 f-string 输出字符、三个空格和下标。
</div>

:::

::::

:::: question programming-10 | 7-10 计算有n个字符串中最长的字符串长度

编写程序，用于计算有n(1&lt;n&lt;10)个字符串中最长的字符串的长度。前导空格不要计算在内！

#### 输入格式:

在第一行中输入n,接下的每行输入一个字符串

#### 输出格式:

在一行中输出最长的字符串的长度

#### 输入样例:

在这里给出一组输入。例如：

```text
4    
        blue
yellow
red
green
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
length=6
```

<div class="question-tags">
<span class="question-tag">lstrip 方法</span>
<span class="question-tag">len 函数</span>
<span class="question-tag">max 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
longest = 0
for _ in range(n):
    longest = max(longest, len(input().lstrip(' ')))
print(f'length={longest}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先读取字符串，并用 `lstrip(' ')` 去掉开头的普通空格，再用 `len()` 计算长度。变量 `longest` 始终保存目前遇到的最大长度；每读入一行，就用 `max(longest, 当前长度)` 更新它。循环结束后输出最大长度。这里使用 `lstrip(' ')`，所以字符串内部和末尾的空格仍会计入长度。
</div>

:::

::::

:::: question programming-11 | 7-11 位1的个数

输入一个非负整数，求它变成二进制后1的个数（提示：用bin函数）。

#### 输入格式:

输入一个正整数。

#### 输出格式:

输出1的个数。

#### 输入样例1:

在这里给出一组输入。例如：

```text
37
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
3
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
0
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
0
```

<div class="question-tags">
<span class="question-tag">bin 函数</span>
<span class="question-tag">count 方法</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
print(bin(n).count('1'))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`bin(n)` 将整数转换成二进制字符串，例如 `bin(37)` 得到 `'0b100101'`。其中 `0b` 是进制前缀，`count('1')` 统计字符串中字符 `1` 出现的次数，因此输出二进制表示中 1 的个数。输入为 0 时，`bin(0)` 为 `'0b0'`，统计结果也是 0。
</div>

:::

::::

:::: question programming-12 | 7-12 整数的二进制相加

输入两个整数，大小在`[0,63]`之间。求它们的二进制和，二进制用8位表示。

#### 输入格式:

在一行输入一个整数，在另一行输入另一个整数。

#### 输出格式:

输出它们的二进制和。

#### 输入样例:

在这里给出一组输入。例如：

```text
5
7
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
00000101
00000111
--------
00001100
```

<div class="question-tags">
<span class="question-tag">二进制格式化</span>
<span class="question-tag">f-string</span>
<span class="question-tag">格式宽度</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a = int(input())
b = int(input())
print(f'{a:08b}')
print(f'{b:08b}')
print('--------')
print(f'{a + b:08b}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

格式说明 `08b` 中，`b` 表示按二进制输出，`8` 表示最小宽度为 8，前面的 `0` 表示位数不足时在左侧补零。程序分别输出两个数的 8 位二进制形式，再输出分隔线，最后把两数相加并按相同格式输出。题目给定的数值范围保证和也能用 8 位表示。
</div>

:::

::::

:::: question programming-13 | 7-13 汉明距离

两个整数间的汉明距离指的是这两个数对应二进制位不同的位置的数目。输入两个整数x,y, 0&lt;=x,y&lt;=$2^{31}$。输出x,y的汉明距离。

#### 输入格式:

在一行输入x,y。

#### 输出格式:

在一行输出x,y汉明距离。

#### 输入样例:

在这里给出一组输入。例如：

```text
1 4
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
2
```

<div class="question-tags">
<span class="question-tag">异或运算</span>
<span class="question-tag">汉明距离</span>
<span class="question-tag">bin 函数</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
x, y = map(int, input().split())
print(bin(x ^ y).count('1'))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

本题的核心是理解异或运算 `^` 的逐位规则：**两个对应位相同得 0，不同得 1**。这个规则正好可以用来"标记出两个数哪些二进制位不一样"。

以样例 `x=1, y=4` 为例，写成二进制（取 3 位便于观察）：

| | 二进制 |
|---|---|
| `x=1` | `001` |
| `y=4` | `100` |
| `x^y` | `101` |

`x ^ y` 结果中每一位是 1，就代表 `x` 和 `y` 在这一位上不同；是 0 则代表相同。因此，**汉明距离就等于 `x ^ y` 这个结果中 1 的个数**。

具体实现上，先计算 `x ^ y`，再用 `bin(...)` 把它转换成二进制字符串（形如 `'0b101'`），最后用 `.count('1')` 统计字符串中 `'1'` 这个字符出现的次数——这正是结果中二进制位为 1 的个数。

样例中 `x^y = 1^4 = 5`，二进制是 `101`，包含 2 个 1，因此输出 `2`。
</div>

:::

::::

:::: question programming-14 | 7-14 判断回文字符串

回文就是字符串中心对称，从左向右读和从右向左读的内容是一样的。  
输入一个字符串，判断该字符串是否为回文，只考虑数字和字母字符，字母的大小写没有区别。

#### 输入格式:

输入一个字符串。

#### 输出格式:

是回文，一行输出`yes`,否则输出`no`。

#### 输入样例:

在这里给出一组输入。例如：

```text
A man,a plan; cnalPanama
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
yes
```

<div class="question-tags">
<span class="question-tag">字符范围判断</span>
<span class="question-tag">ord 与 chr 函数</span>
<span class="question-tag">字符串逆序</span>
</div>

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

:::: question programming-15 | 7-15 输入一行字符串，并将它转换成10进制数输出

输入一行字符串，去掉非16进制字符，并将它转换成10进制数输出。

#### 输入格式:

输入一行字符串。

#### 输出格式:

输出16进制字符串和转换后的10进制数。

#### 输入样例:

在这里给出一组输入。例如：

```text
_ahg1*B
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
a1B
2587
```

<div class="question-tags">
<span class="question-tag">字符串筛选</span>
<span class="question-tag">int 函数</span>
<span class="question-tag">十六进制转换</span>
</div>

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

:::: question programming-16 | 7-16 统计满足特定条件的字符数

输入字符串A(没有重复字符），输入字符串B，求在字符串A中字符的个数，这些字符必须同时又在字符串B中。提示：用`in`运算符。

#### 输入格式:

一行输入字符串A。  
一行输入字符串B。

#### 输出格式:

一行输出字符数。

#### 输入样例:

在这里给出一组输入。例如：

```text
AEIOU
HELLO World!
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
2
```

<div class="question-tags">
<span class="question-tag">in 运算符</span>
<span class="question-tag">sum 函数</span>
<span class="question-tag">字符串遍历</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
a = input()
b = input()
print(sum(c in b for c in a))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

遍历字符串 A 中的每个字符，判断它是否出现在字符串 B 中。`c in b` 的结果是 `True` 或 `False`，而 Python 中 `True` 可以按 1、`False` 按 0 参与求和，因此 `sum(c in b for c in a)` 就是在统计 A 中有多少个字符也出现在 B 中。题目说明 A 没有重复字符，所以不会重复计数。
</div>

:::

::::

:::: question programming-17 | 7-17 查验身份证

一个合法的身份证号码由17位地区、日期编号和顺序编号加1位校验码组成。校验码的计算规则如下：

首先对前17位数字加权求和，权重分配为：{7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2}；然后将计算的和对11取模得到值`Z`；最后按照以下关系对应`Z`值与校验码`M`的值：

```python
Z：0 1 2 3 4 5 6 7 8 9 10
M：1 0 X 9 8 7 6 5 4 3 2
```

现在给定一些身份证号码，请你验证校验码的有效性，并输出有问题的号码。

#### 输入格式：

输入第一行给出正整数$N$（$\le 100$）是输入的身份证号码的个数。随后$N$行，每行给出1个18位身份证号码。

#### 输出格式：

按照输入的顺序每行输出1个有问题的身份证号码。这里并不检验前17位是否合理，只检查前17位是否全为数字且最后1位校验码计算准确。如果所有号码都正常，则输出`All passed`。

#### 输入样例1：

```text
4
320124198808240056
12010X198901011234
110108196711301866
37070419881216001X
```

#### 输出样例1：

```text
12010X198901011234
110108196711301866
37070419881216001X
```

#### 输入样例2：

```python
2
320124198808240056
110108196711301862
```

#### 输出样例2：

```python
All passed
```

**鸣谢阜阳师范学院范建中老师补充数据**

**鸣谢浙江工业大学之江学院石洗凡老师纠正数据**

<div class="question-tags">
<span class="question-tag">zip 函数</span>
<span class="question-tag">any 函数</span>
<span class="question-tag">身份证校验码</span>
</div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
codes = '10X98765432'
invalid = []
for _ in range(n):
    number = input().strip()
    if len(number) != 18 or any(c not in '0123456789' for c in number[:17]):
        invalid.append(number)
        continue
    total = sum(int(c) * w for c, w in zip(number[:17], weights))
    if number[-1] != codes[total % 11]:
        invalid.append(number)
print('\n'.join(invalid) if invalid else 'All passed')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先检查号码长度是否为 18，以及前 17 位是否全部为数字；不符合就直接记为错误号码。对合格号码，用 `zip(number[:17], weights)` 将每一位数字与对应权重配对，计算加权总和，再用 `total % 11` 得到索引，从 `codes` 中查出正确校验码。若计算出的校验码与最后一位不同，就输出该号码；全部通过时输出 `All passed`。
</div>

:::

::::
