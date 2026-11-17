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

<div class="section-label">题干 <span>QUESTION</span></div>

```python
'age'+23不是正确的表达式。  
```

::: answer

T（正确）。

:::

::: explanation

字符串不能与整数直接相加，执行 'age'+23 会产生 TypeError；这里把代码块末尾中文视为题目说明。

<!-- teaching-notes:start -->

**从本题理解：同一个运算符对不同类型有不同含义**

对数字，`+` 表示加法；对字符串，表示拼接；对列表，表示连接两边的元素。例如 `2+3` 为 5，`'2'+'3'` 为 `'23'`，`[2]+[3]` 为 `[2,3]`。Python 不会为了完成拼接自动把整数变成字符串，所以 `'age'+23` 在运行时产生 `TypeError`。

若要拼接，使用 `'age'+str(23)` 或 `f'age{23}'`；若要计算，使用 `int('23')+1`。二者目的不同，不能随意选择一种转换。还要把语法阶段和执行阶段分开：正常引号下的字符串加整数，能通过语法解析；弯引号 `“ ”` 不是 Python 字符串定界符，原样输入会先出现语法错误。

继续阅读：[第2章：字符串与类型转换](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-2 | 1-2 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表可以用find()函数来搜索数据是否在列表中。

::: answer

F（错误）。

:::

::: explanation

find() 是字符串方法，列表查找位置用 index()，判断有无用 in。

<!-- teaching-notes:start -->

**从本题理解：查存在、查位置与查全部匹配**

只判断有无时使用 `x in seq`，结果为布尔值。字符串 `find()` 返回第一次匹配的起始下标，找不到返回 -1；字符串和列表的 `index()` 也查首次位置，但找不到会引发 `ValueError`。列表没有 `find()` 方法。

```python
s = 'programming'
print(s.find('r'))      # 1
print(s.find('r', 2))   # 4：从下标 2 开始找
print('x' in s)         # False
```

不能写 `if s.find(x)` 判断存在：找到在下标 0 时是假值，没找到的 -1 反而是真值。应写 `if x in s` 或 `if s.find(x) != -1`。题目要求输出所有匹配位置时，需要遍历下标或重复搜索，而不是只调用一次查找；要求倒序位置时还需改变遍历方向。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-3 | 1-3 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

将列表中的元素顺序打乱的函数shuffle()不是random模块的函数或方法。

::: answer

F（错误）。

:::

::: explanation

random.shuffle() 就是 random 模块提供的方法，原地打乱列表并返回 None。

<!-- teaching-notes:start -->

**从本题理解：排序的对象、顺序与返回值**

`sorted(items)` 返回新的已排序列表，原对象不变；`a.sort()` 原地修改列表并返回 `None`。要降序使用 `reverse=True`。`max()` 只取最大元素，不返回排序后的完整序列，空序列且无默认值时还会报错。

排序前先确定按什么比较：整数 `[2,10]` 排成 `[2,10]`，字符串 `['2','10']` 则排成 `['10','2']`。若题意是按数值大小，必须先转成数值再排序，最后再转回字符串用于输出。`random.shuffle(a)` 也原地修改列表并返回 `None`，但它是打乱，不是排序；不要写 `a=random.shuffle(a)`。

继续阅读：[第3章：列表方法](../topics/chapter-03.md)与[第4章：搜索和排序](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-4 | 1-4 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

字符串和列表都是序列类型。

::: answer

T（正确）。

:::

::: explanation

两者都有顺序、索引和切片等序列操作。

<!-- teaching-notes:start -->

**从本题理解：字符串是不可变的字符序列**

Python 没有单独的内置 `char` 类型，`'A'` 是长度为 1 的 `str`。字符串支持索引、切片、遍历、成员判断与长度查询，但不支持 `s[0]='B'` 这样的原地修改。要更改字符，可构造新字符串并重新赋值，例如 `s='B'+s[1:]`。

字符串的长度由对象记录，不依赖 `\0` 作为结束标志；`len('a\0b')` 为 3，中间的空字符也计入长度。`list('abc')` 会遍历字符串，生成 `['a','b','c']`；`['abc']` 则只含一个完整字符串。这个区别也适用于拆包和 `extend()`：传入字符串时，它通常被当成可逐字符遍历的序列。

继续阅读：[第3章：序列与字符串](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-5 | 1-5 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

可以通过[]来访问字符串的某个字符，也可以将它修改成其他字符。

::: answer

F（错误）。

:::

::: explanation

可索引读取，但字符串不可变，不能通过 s[i]=... 修改字符。

<!-- teaching-notes:start -->

**从本题理解：原地修改与生成新对象**

列表是可变对象，能原地修改元素或增删；字符串、元组不能更改自身位置上的引用。`s=s+'x'` 虽然能执行，但它创建新字符串并让名字 `s` 重新绑定，不能证明字符串可变。元组里的列表仍可改变，如 `t=([1],)` 后执行 `t[0].append(2)` 合法。

另一个常考区别是返回值：`a.sort()`、`a.reverse()`、`a.append(x)` 修改列表并返回 `None`；`sorted(a)`、`a[::-1]` 返回新列表。因此 `b=a.sort()` 后 `b` 不是已排序列表，而是 `None`。阅读代码时分别记录“原对象现在是什么”和“表达式返回了什么”，就能避免把二者混为一谈。

继续阅读：[第3章：列表修改与返回值](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-6 | 1-6 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

字符串对象和元组对象是不可变对象，列表对象为可变对象。

::: answer

T（正确）。

:::

::: explanation

列表可原地增删改，字符串和元组自身不能原地改位置上的引用。

<!-- teaching-notes:start -->

**从本题理解：原地修改与生成新对象**

列表是可变对象，能原地修改元素或增删；字符串、元组不能更改自身位置上的引用。`s=s+'x'` 虽然能执行，但它创建新字符串并让名字 `s` 重新绑定，不能证明字符串可变。元组里的列表仍可改变，如 `t=([1],)` 后执行 `t[0].append(2)` 合法。

另一个常考区别是返回值：`a.sort()`、`a.reverse()`、`a.append(x)` 修改列表并返回 `None`；`sorted(a)`、`a[::-1]` 返回新列表。因此 `b=a.sort()` 后 `b` 不是已排序列表，而是 `None`。阅读代码时分别记录“原对象现在是什么”和“表达式返回了什么”，就能避免把二者混为一谈。

继续阅读：[第3章：列表修改与返回值](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-7 | 1-7 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[::]的结果是[12, -5, -22, -10, -26, 35, 0, 49, 3, -21]。

::: answer

T（正确）。

:::

::: explanation

省略起止和步长的 [::] 复制整个列表，值与原列表一致。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-8 | 1-8 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[::-1]的结果是[-21, 3, 49, 0, 35, -26, -10, -22, -5, 12]。

::: answer

T（正确）。

:::

::: explanation

负步长 -1 从末尾向前遍历，生成逆序新列表。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-9 | 1-9 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[::2]的结果是[12, -22, -26, 0, 3]。

::: answer

T（正确）。

:::

::: explanation

步长 2 从下标 0 开始，依次取 0、2、4、6、8。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-10 | 1-10 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[1::2]的结果是[12, -22, -26, 0, 3]。

::: answer

F（错误）。

:::

::: explanation

从下标 1 开始应取 1、3、5、7、9，结果为 [-5,-10,35,49,-21]。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-11 | 1-11 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[3:8:2]的结果是[-10, 35, 49]。

::: answer

T（正确）。

:::

::: explanation

取下标 3、5、7，分别为 -10、35、49，终点 8 不包含。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-12 | 1-12 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[0:100]的结果是错误。

::: answer

F（错误）。

:::

::: explanation

切片边界自动截到末尾，lst[0:100] 返回整个列表的浅拷贝，不报错。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-13 | 1-13 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[100:]的结果是[]。

::: answer

T（正确）。

:::

::: explanation

切片起点超出末尾返回空列表。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-14 | 1-14 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

列表lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21],lst[100]的结果是运行错误。

::: answer

T（正确）。

:::

::: explanation

单元素索引 100 越界，会产生 IndexError。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-15 | 1-15 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面的程序当输入是 `c d e a`时，输出是 `a c d e`。

```python
a = input().split(" ")
for i in a.sort():    
    print(i,end=" ")
```

::: answer

F（错误）。

:::

::: explanation

sort() 原地排序并返回 None；遍历 None 会产生 TypeError。应先 a.sort()，再 for i in a。

<!-- teaching-notes:start -->

**从本题理解：排序的对象、顺序与返回值**

`sorted(items)` 返回新的已排序列表，原对象不变；`a.sort()` 原地修改列表并返回 `None`。要降序使用 `reverse=True`。`max()` 只取最大元素，不返回排序后的完整序列，空序列且无默认值时还会报错。

排序前先确定按什么比较：整数 `[2,10]` 排成 `[2,10]`，字符串 `['2','10']` 则排成 `['10','2']`。若题意是按数值大小，必须先转成数值再排序，最后再转回字符串用于输出。`random.shuffle(a)` 也原地修改列表并返回 `None`，但它是打乱，不是排序；不要写 `a=random.shuffle(a)`。

继续阅读：[第3章：列表方法](../topics/chapter-03.md)与[第4章：搜索和排序](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-16 | 1-16 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

表达式：`"34" in "1234"==True` 返回值是True。

::: answer

F（错误）。

:::

::: explanation

in 与 == 组成链式比较，还需检查 "1234"==True，此项为假，整体为假。

<!-- teaching-notes:start -->

**从本题理解：链式比较会复用中间操作数**

`a < b < c` 按逻辑可理解为 `a < b and b < c`，并不是先把 `a < b` 的布尔值拿去与 `c` 比较。成员运算 `in` 也属于比较运算，所以 `'34' in '1234' == True` 中，中间操作数是字符串 `'1234'`，后一项比较的是 `'1234' == True`，结果为假。

加括号会改变分组：`('34' in '1234') == True` 先得到成员判断结果，因此为真。实际编程中直接写 `'34' in '1234'` 更清楚。链式比较还具有短路特性，前一项为假时不再计算后项；遇到混合比较符号时，把它拆成相邻两项的比较，再逐项分析最可靠。

继续阅读：[第4章：条件语句](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-17 | 1-17 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

F（错误）。

:::

::: explanation

s1 在最后一个元素后仍有空格，join 得到的 s2 没有末尾空格，程序输出 no。

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

:::: question judgment-18 | 1-18 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

`"12 "*3==" ".join(["12","12","12"])` 的输出是True

::: answer

F（错误）。

:::

::: explanation

左侧重复得到 12 12 12 后还带末尾空格，右侧 join 不带末尾空格。

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

:::: question judgment-19 | 1-19 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

语句`print("输出结果是{:8s}".format("this"))`的输出是：输出结果是 $\Box$$\Box$$\Box$$\Box$this。  
 $\Box$表示空格。

::: answer

F（错误）。

:::

::: explanation

字符串默认左对齐，实际输出 this 后四个空格。

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

:::: question judgment-20 | 1-20 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

语句`print("输出结果是{:8d}".format(1234))`的输出是：输出结果是 1234□□□□。 □表示空格。

::: answer

F（错误）。

:::

::: explanation

整数默认右对齐，实际输出 1234 前四个空格。

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

:::: question judgment-21 | 1-21 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

语句`print("输出结果是{:08.2f}".format(14.345))`的输出是：输出结果是00014.34。

::: answer

F（错误）。

:::

::: explanation

按 Python 3 实际格式化结果为 00014.35；14.345 的二进制浮点近似值会影响舍入，不应填 00014.34。

<!-- teaching-notes:start -->

**从本题理解：浮点近似与最终显示**

多数十进制小数不能被二进制浮点数精确表示，计算机保存的是附近的可表示值。因此 `round()` 或 `.2f` 格式化所处理的，可能并不是纸面上那个精确的十进制数。遇到 14.345 一类边界值，不能机械地按十进制“第三位是 5”判断结果。

即使没有表示误差，Python 的 `round()` 在恰好居中时也采用向偶数舍入，而不是一律进位：`round(2.5)` 为 2，`round(3.5)` 为 4。格式化返回字符串，`round(x,2)` 返回数值，不保证显示末尾的零。若业务要求精确十进制及指定舍入规则，应从原始文本构造 `Decimal` 并明确舍入方式；不要先转成 `float` 再期望恢复精确输入。

继续阅读：[第2章：数字类型与格式化输出](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-22 | 1-22 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

[1,2,[3]]+[4,5]的结果是[1,2,3,4,5]。

::: answer

F（错误）。

:::

::: explanation

列表拼接不会展开内部列表，结果为 [1,2,[3],4,5]。

<!-- teaching-notes:start -->

**从本题理解：序列重复与内部引用共享**

字符串或列表乘整数表示重复，不是把内容解释成数值。`'23'*3` 为 `'232323'`，`[4,5]*3` 为 `[4,5,4,5,4,5]`，不会自动生成三个子列表。字符串原有的空格也会一起重复，所以 `'12 '*3` 在最后仍有一个空格。

若元素本身是可变列表，重复操作复制的是引用：`rows=[[0]*2]*3` 中三行是同一个对象，执行 `rows[0][0]=1` 会让三行都改变。要创建独立的行，应写 `rows=[[0]*2 for _ in range(3)]`。同样，列表 `+` 只连接一层，`[1,2]+[[3]]` 得到 `[1,2,[3]]`，不会递归展开内部列表。

继续阅读：[第3章：序列运算与嵌套引用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-23 | 1-23 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

[4,5]`*`3的结果是[[4,5],[4,5],[4,5]]。

::: answer

F（错误）。

:::

::: explanation

列表重复的是元素，结果为 [4,5,4,5,4,5]。

<!-- teaching-notes:start -->

**从本题理解：序列重复与内部引用共享**

字符串或列表乘整数表示重复，不是把内容解释成数值。`'23'*3` 为 `'232323'`，`[4,5]*3` 为 `[4,5,4,5,4,5]`，不会自动生成三个子列表。字符串原有的空格也会一起重复，所以 `'12 '*3` 在最后仍有一个空格。

若元素本身是可变列表，重复操作复制的是引用：`rows=[[0]*2]*3` 中三行是同一个对象，执行 `rows[0][0]=1` 会让三行都改变。要创建独立的行，应写 `rows=[[0]*2 for _ in range(3)]`。同样，列表 `+` 只连接一层，`[1,2]+[[3]]` 得到 `[1,2,[3]]`，不会递归展开内部列表。

继续阅读：[第3章：序列运算与嵌套引用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question judgment-24 | 1-24 判断题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序的输出是字符`a`

```python
c="A"
print(c.lower)
```

::: answer

F（错误）。

:::

::: explanation

c.lower 是方法对象；调用 c.lower() 才得到 a。

<!-- teaching-notes:start -->

**从本题理解：取得方法与执行方法是两回事**

`c.lower` 取得绑定到对象 `c` 上的方法对象，`c.lower()` 才真正调用它并返回小写字符串。打印方法对象会得到方法描述，不能当成转换结果。字符串不可变，因此 `lower()` 不会改变原对象，若要保存结果需写 `c=c.lower()`。

```python
c = 'AbC'
result = c.lower()
print(c)          # AbC：原值不变
print(result)     # abc
print(c.isalpha())# True
```

`isdigit()`、`isalpha()`、`isalnum()` 检查整个字符串是否非空且每个字符都满足相应类别；空串的这几种判断为假。它们按 Unicode 规则工作，不只接受 ASCII 字符。题目严格要求英文字母或十六进制字符时，应按明确范围判断，不能直接把“属于字母数字”当成“合法十六进制数码”。

继续阅读：[第3章：字符串方法](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="choice" class="quiz-group">单选题<span>05 QUESTIONS</span></h2>

:::: question choice-1 | 2-1 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

max((3, 5, 1, 7, 4))的结果是____。

**A.** 1

**B.** 3

**C.** 5

**D.** 7

::: answer

D。

:::

::: explanation

max 返回序列最大值 7。

<!-- teaching-notes:start -->

**从本题理解：排序的对象、顺序与返回值**

`sorted(items)` 返回新的已排序列表，原对象不变；`a.sort()` 原地修改列表并返回 `None`。要降序使用 `reverse=True`。`max()` 只取最大元素，不返回排序后的完整序列，空序列且无默认值时还会报错。

排序前先确定按什么比较：整数 `[2,10]` 排成 `[2,10]`，字符串 `['2','10']` 则排成 `['10','2']`。若题意是按数值大小，必须先转成数值再排序，最后再转回字符串用于输出。`random.shuffle(a)` 也原地修改列表并返回 `None`，但它是打乱，不是排序；不要写 `a=random.shuffle(a)`。

继续阅读：[第3章：列表方法](../topics/chapter-03.md)与[第4章：搜索和排序](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-2 | 2-2 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

以下哪句打印出smith\exam1\test.txt？

**A.** `print("smith\exam1\test.txt")`

**B.** `print("smith\\exam1\\test.txt")`

**C.** `print("smith\"exam1\"test.txt")`

**D.** `print("smith"\exam1"\test.txt")`

::: answer

B。

:::

::: explanation

字符串字面量中的真反斜杠需写成 \\；A 中 \t 被解释为制表符。

<!-- teaching-notes:start -->

**从本题理解：源码写法与实际字符串并不相同**

普通字符串中的反斜杠引出转义，例如 `\n` 是一个换行符、`\t` 是一个制表符，`\\` 才是一个真实反斜杠。因此 Windows 风格路径中的 `\test` 如果直接写进普通字符串，开头的 `\t` 会被解释成制表符，打印结果就改变了。

```python
path = r'smith\exam1\test.txt'
print(path)
print(len('\t'))   # 1：一个制表符
print(len('\\t'))  # 2：反斜杠和字母 t
```

`r` 前缀可以减少路径中的转义处理，但原始字符串也有语法限制，例如不能以奇数个反斜杠紧接结束引号。查看 `repr(path)` 会得到便于观察转义的表示，不能把其中为展示而写出的双反斜杠误认为实际内容里有两个反斜杠。

继续阅读：[第2章：字符串类型](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-3 | 2-3 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

list("abcd")的结果是?

**A.** ['a', 'b', 'c', 'd']

**B.** ['ab']

**C.** ['cd']

**D.** ['abcd']

::: answer

A。

:::

::: explanation

list() 逐字符遍历字符串，得到 4 个字符元素。

<!-- teaching-notes:start -->

**从本题理解：字符串是不可变的字符序列**

Python 没有单独的内置 `char` 类型，`'A'` 是长度为 1 的 `str`。字符串支持索引、切片、遍历、成员判断与长度查询，但不支持 `s[0]='B'` 这样的原地修改。要更改字符，可构造新字符串并重新赋值，例如 `s='B'+s[1:]`。

字符串的长度由对象记录，不依赖 `\0` 作为结束标志；`len('a\0b')` 为 3，中间的空字符也计入长度。`list('abc')` 会遍历字符串，生成 `['a','b','c']`；`['abc']` 则只含一个完整字符串。这个区别也适用于拆包和 `extend()`：传入字符串时，它通常被当成可逐字符遍历的序列。

继续阅读：[第3章：序列与字符串](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-4 | 2-4 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

如果list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]，那么以下那个是list1[:-1]？

**A.** 0

**B.** [1, 2, 3, 4, 5, 4, 3, 2, 1]

**C.** [1, 2, 3, 4, 5, 4, 3, 2]

**D.** [0, 1, 2, 3, 4, 3, 2, 1, 0]

::: answer

C。

:::

::: explanation

切片终点 -1 不包含最后一个元素，结果少最后的 1。

<!-- teaching-notes:start -->

**从本题理解：索引、切片与负步长**

索引 `a[i]` 取得一个元素，下标从 0 开始，负下标从尾部计数，`-1` 是最后一个元素。切片 `a[start:stop:step]` 取得一个新序列：从起点开始，每次前进步长，只要还没到终点就继续，终点本身不取。正步长时可用 `range(start,stop,step)` 列出目标下标。

```python
a = [10, 20, 30, 40, 50]
print(a[1:5:2])  # [20, 40]：下标 1、3
print(a[:-1])    # [10, 20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

切片越界会裁剪到合法边界，而单个索引越界会报错。负步长时默认起点和终点随方向改变，`a[::-1]` 的省略终点不等于显式写 `a[-1:-1:-1]`；后者是空列表。步长不能为 0。列表切片是浅拷贝，外层新建，内部可变对象仍可能共享。

继续阅读：[第3章：序列的访问及运算符](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question choice-5 | 2-5 单选题

<div class="section-label">题干 <span>QUESTION</span></div>

要把5加到列表lst的末尾，用的是___ 。

**A.** lst.add(5)

**B.** lst.append(5)

**C.** lst.addLast(5)

**D.** lst.addEnd(5)

::: answer

B。

:::

::: explanation

append(5) 将 5 作为单个元素追加到列表末尾。

<!-- teaching-notes:start -->

**从本题理解：列表方法按“位置”还是“值”操作**

`append(x)` 把 x 作为一个整体追加，`extend(items)` 把可迭代对象逐项追加，`insert(i,x)` 在位置 i 前插入。删除时，`remove(x)` 删除第一个值等于 x 的元素，不返回被删元素；`pop(i)` 按下标删除并返回元素，省略下标则处理最后一项。

```python
a = [3, 4, 3]
a.remove(3)
print(a)       # [4, 3]：只删首个 3
print(a.pop()) # 3
print(a)       # [4]
```

元素删除后，右边元素的下标会前移；跟踪程序时每一步都应写出新的列表。`append()`、`remove()`、`sort()` 等修改列表后返回 `None`，不能把它们的返回值再赋给列表变量。`pop()` 则特意返回被删元素，是这一组题里很容易混淆的差别。

继续阅读：[第3章：列表修改与返回值](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="blank" class="quiz-group">填空题<span>17 QUESTIONS</span></h2>

:::: question blank-1 | 4-1 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

'23'*3的结果是_______。 _____ (答案不要加引号）

::: answer

`232323`。

:::

::: explanation

字符串重复三次，并非数值乘法。

<!-- teaching-notes:start -->

**从本题理解：序列重复与内部引用共享**

字符串或列表乘整数表示重复，不是把内容解释成数值。`'23'*3` 为 `'232323'`，`[4,5]*3` 为 `[4,5,4,5,4,5]`，不会自动生成三个子列表。字符串原有的空格也会一起重复，所以 `'12 '*3` 在最后仍有一个空格。

若元素本身是可变列表，重复操作复制的是引用：`rows=[[0]*2]*3` 中三行是同一个对象，执行 `rows[0][0]=1` 会让三行都改变。要创建独立的行，应写 `rows=[[0]*2 for _ in range(3)]`。同样，列表 `+` 只连接一层，`[1,2]+[[3]]` 得到 `[1,2,[3]]`，不会递归展开内部列表。

继续阅读：[第3章：序列运算与嵌套引用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-2 | 4-2 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

len('3//11//2018'.split('/'))的结果是_____。 _____

::: answer

`5`。

:::

::: explanation

指定 '/' 分隔时，连续分隔符产生空字符串，列表为 ['3','','11','','2018']。

<!-- teaching-notes:start -->

**从本题理解：指定分隔符与默认拆分不同**

`split('/')` 把每一个 `/` 都视为分界，连续分隔符之间会产生空字符串，首尾分隔符也会产生空项。因此 `'3//11//2018'.split('/')` 有 5 项，两个空字符串也各算一个列表元素。

```python
print('a,,b,'.split(','))  # ['a', '', 'b', '']
print('  a   b  '.split()) # ['a', 'b']
print(''.split(','))      # ['']
print(''.split())         # []
```

不带参数的 `split()` 按连续空白拆分，合并空白并忽略两端空白，这与显式 `split(' ')` 也不同。选择方式取决于数据格式：普通空格分隔数值通常用 `split()`；CSV 式的空字段若有意义，就不能先合并分隔符。`len()` 数的是结果中的元素，而不是非空元素。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-3 | 4-3 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

lst=[3,4,5,6,5,4,3],执行lst.remove(3)后，lst[0]的值是：_。 _____

::: answer

`4`。

:::

::: explanation

remove(3) 删除首个 3，原下标 1 的 4 成为新首元素。

<!-- teaching-notes:start -->

**从本题理解：列表方法按“位置”还是“值”操作**

`append(x)` 把 x 作为一个整体追加，`extend(items)` 把可迭代对象逐项追加，`insert(i,x)` 在位置 i 前插入。删除时，`remove(x)` 删除第一个值等于 x 的元素，不返回被删元素；`pop(i)` 按下标删除并返回元素，省略下标则处理最后一项。

```python
a = [3, 4, 3]
a.remove(3)
print(a)       # [4, 3]：只删首个 3
print(a.pop()) # 3
print(a)       # [4]
```

元素删除后，右边元素的下标会前移；跟踪程序时每一步都应写出新的列表。`append()`、`remove()`、`sort()` 等修改列表后返回 `None`，不能把它们的返回值再赋给列表变量。`pop()` 则特意返回被删元素，是这一组题里很容易混淆的差别。

继续阅读：[第3章：列表修改与返回值](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-4 | 4-4 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

list(range(2,12,2))[:-2].pop()的结果是：_____。 _____

::: answer

`6`。

:::

::: explanation

range 得到 [2,4,6,8,10]，切片去掉末尾两项，再 pop 返回末尾的 6。

<!-- teaching-notes:start -->

**从本题理解：列表方法按“位置”还是“值”操作**

`append(x)` 把 x 作为一个整体追加，`extend(items)` 把可迭代对象逐项追加，`insert(i,x)` 在位置 i 前插入。删除时，`remove(x)` 删除第一个值等于 x 的元素，不返回被删元素；`pop(i)` 按下标删除并返回元素，省略下标则处理最后一项。

```python
a = [3, 4, 3]
a.remove(3)
print(a)       # [4, 3]：只删首个 3
print(a.pop()) # 3
print(a)       # [4]
```

元素删除后，右边元素的下标会前移；跟踪程序时每一步都应写出新的列表。`append()`、`remove()`、`sort()` 等修改列表后返回 `None`，不能把它们的返回值再赋给列表变量。`pop()` 则特意返回被删元素，是这一组题里很容易混淆的差别。

继续阅读：[第3章：列表修改与返回值](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-5 | 4-5 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

要想得到[0,100]范围内的随机数，random.randint(0,n)里的n应该是：___。 _____

::: answer

`100`。

:::

::: explanation

randint(a,b) 包含两个端点。

<!-- teaching-notes:start -->

**从本题理解：随机区间的端点**

`random.random()` 返回满足 $0\le x<1$ 的随机浮点数；对非负值使用 `int()` 相当于向下取整，所以题目中的 `int(x*90)+10` 按区间分析得到 10～99。直接取整数时，`randint(10,99)` 包含两个端点，`randrange(10,100)` 不包含右端。

```python
import random
n = random.randint(10, 99)
items = [1, 2, 3]
random.shuffle(items)  # 原地打乱，返回 None
```

区间题先写原始范围，再依次做乘法、取整和平移，不要只试几个随机样本来猜端点。随机运行未碰到某个边界，不代表边界不可能出现；`seed()` 用于帮助复现实验序列，也不改变这些函数约定的区间。

继续阅读：[第3章：random 库](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-6 | 4-6 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

`print("{1}+{0}={2}".format(2,3,2+3))`的输出是 _____ (答案不要加引号）。

::: answer

`3+2=5`。

:::

::: explanation

参数 0 为 2、参数 1 为 3、参数 2 为 5，按占位编号替换。

<!-- teaching-notes:start -->

**从本题理解：格式串中的占位符怎样取值**

`str.format()` 的位置参数编号从 0 开始，编号与占位符出现顺序可以不同。`'{1}+{0}={2}'.format(2,3,5)` 先得到三个参数 2、3、5，再按编号替换，输出 `3+2=5`。同一个参数也可以多次引用。

命名占位符需要显式传参，例如 `'{first}-{second}={0}'.format(11,first=34,second=23)`。花括号外的减号与等号只是文本，不会再执行运算；花括号里的 `first` 也不会自动去局部变量中查找。f-string 则可直接写表达式，如 `f'{a}-{b}={a-b}'`。分清这两种机制，就不会把字符串里的算式误认为真正参与计算的代码。

继续阅读：[第2章：格式化输出](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-7 | 4-7 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

```python
a=34
b=23
print("{first}-{second}={0}".format(34-23,first=a,second=b))
```

上面程序输出是 _____ (答案不要加引号）。

::: answer

`34-23=11`。

:::

::: explanation

first、second 分别取 34、23，位置参数 0 为差值 11。

<!-- teaching-notes:start -->

**从本题理解：格式串中的占位符怎样取值**

`str.format()` 的位置参数编号从 0 开始，编号与占位符出现顺序可以不同。`'{1}+{0}={2}'.format(2,3,5)` 先得到三个参数 2、3、5，再按编号替换，输出 `3+2=5`。同一个参数也可以多次引用。

命名占位符需要显式传参，例如 `'{first}-{second}={0}'.format(11,first=34,second=23)`。花括号外的减号与等号只是文本，不会再执行运算；花括号里的 `first` 也不会自动去局部变量中查找。f-string 则可直接写表达式，如 `f'{a}-{b}={a-b}'`。分清这两种机制，就不会把字符串里的算式误认为真正参与计算的代码。

继续阅读：[第2章：格式化输出](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-8 | 4-8 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

`print("{:>08s}".format(bin(31)[2:]))`的输出是 _____ 。

::: answer

`00011111`。

:::

::: explanation

31 的二进制为 11111，去掉前缀后左侧补零至宽度 8。

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

:::: question blank-9 | 4-9 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

`print("programming".find("r",2))`的输出是 _____ 。

。

::: answer

`4`。

:::

::: explanation

从下标 2 起查找 r，第一次遇到的是下标 4，跳过下标 1 的 r。

<!-- teaching-notes:start -->

**从本题理解：查存在、查位置与查全部匹配**

只判断有无时使用 `x in seq`，结果为布尔值。字符串 `find()` 返回第一次匹配的起始下标，找不到返回 -1；字符串和列表的 `index()` 也查首次位置，但找不到会引发 `ValueError`。列表没有 `find()` 方法。

```python
s = 'programming'
print(s.find('r'))      # 1
print(s.find('r', 2))   # 4：从下标 2 开始找
print('x' in s)         # False
```

不能写 `if s.find(x)` 判断存在：找到在下标 0 时是假值，没找到的 -1 反而是真值。应写 `if x in s` 或 `if s.find(x) != -1`。题目要求输出所有匹配位置时，需要遍历下标或重复搜索，而不是只调用一次查找；要求倒序位置时还需改变遍历方向。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-10 | 4-10 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

`print("programming".find("x"))`的输出是 _____ 。

::: answer

`-1`。

:::

::: explanation

字符串中不存在 x，find 返回 -1。

<!-- teaching-notes:start -->

**从本题理解：查存在、查位置与查全部匹配**

只判断有无时使用 `x in seq`，结果为布尔值。字符串 `find()` 返回第一次匹配的起始下标，找不到返回 -1；字符串和列表的 `index()` 也查首次位置，但找不到会引发 `ValueError`。列表没有 `find()` 方法。

```python
s = 'programming'
print(s.find('r'))      # 1
print(s.find('r', 2))   # 4：从下标 2 开始找
print('x' in s)         # False
```

不能写 `if s.find(x)` 判断存在：找到在下标 0 时是假值，没找到的 -1 反而是真值。应写 `if x in s` 或 `if s.find(x) != -1`。题目要求输出所有匹配位置时，需要遍历下标或重复搜索，而不是只调用一次查找；要求倒序位置时还需改变遍历方向。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-11 | 4-11 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

`print("a123".isdigit())`的输出是 _____ 。

::: answer

`False`。

:::

::: explanation

a 不是数字，因此整个字符串不是全数字。

<!-- teaching-notes:start -->

**从本题理解：取得方法与执行方法是两回事**

`c.lower` 取得绑定到对象 `c` 上的方法对象，`c.lower()` 才真正调用它并返回小写字符串。打印方法对象会得到方法描述，不能当成转换结果。字符串不可变，因此 `lower()` 不会改变原对象，若要保存结果需写 `c=c.lower()`。

```python
c = 'AbC'
result = c.lower()
print(c)          # AbC：原值不变
print(result)     # abc
print(c.isalpha())# True
```

`isdigit()`、`isalpha()`、`isalnum()` 检查整个字符串是否非空且每个字符都满足相应类别；空串的这几种判断为假。它们按 Unicode 规则工作，不只接受 ASCII 字符。题目严格要求英文字母或十六进制字符时，应按明确范围判断，不能直接把“属于字母数字”当成“合法十六进制数码”。

继续阅读：[第3章：字符串方法](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-12 | 4-12 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

`print("aABC".isalpha())`的输出是 _____ 。

::: answer

`True`。

:::

::: explanation

aABC 的每个字符都是字母。

<!-- teaching-notes:start -->

**从本题理解：取得方法与执行方法是两回事**

`c.lower` 取得绑定到对象 `c` 上的方法对象，`c.lower()` 才真正调用它并返回小写字符串。打印方法对象会得到方法描述，不能当成转换结果。字符串不可变，因此 `lower()` 不会改变原对象，若要保存结果需写 `c=c.lower()`。

```python
c = 'AbC'
result = c.lower()
print(c)          # AbC：原值不变
print(result)     # abc
print(c.isalpha())# True
```

`isdigit()`、`isalpha()`、`isalnum()` 检查整个字符串是否非空且每个字符都满足相应类别；空串的这几种判断为假。它们按 Unicode 规则工作，不只接受 ASCII 字符。题目严格要求英文字母或十六进制字符时，应按明确范围判断，不能直接把“属于字母数字”当成“合法十六进制数码”。

继续阅读：[第3章：字符串方法](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-13 | 4-13 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

print("$\Box$$\Box$$\Box$xyz$\Box$$\Box$".strip(),"$\Box$$\Box$$\Box$xyz$\Box$$\Box$".rstrip(),  
"$\Box$$\Box$$\Box$xyz$\Box$$\Box$".lstrip())的输出是 _____ 。（答案不要加引号，$\Box$表示空格）

::: answer

`xyz□□□□xyz□xyz□□`（□ 表示空格）。

:::

::: explanation

将题面 □ 还原为空格：strip 得 'xyz'，rstrip 得 '   xyz'，lstrip 得 'xyz  '；print 又在参数之间各加一个空格，末尾保留两个空格。

<!-- teaching-notes:start -->

**从本题理解：清理哪一端，保留哪些字符**

`strip()` 清理两端空白，`lstrip()` 仅清理左端，`rstrip()` 仅清理右端；它们都返回新字符串，保留中间空格。默认空白还包括制表符、换行符，而 `lstrip(' ')` 明确只清理普通空格。题目要求保留尾部空格时，不能用 `strip()` 替代单侧处理。

传入参数时，它表示“可被清理的字符集合”，不是一个固定前缀或后缀。例如 `'abbaXba'.strip('ab')` 得到 `'X'`，因为两端连续的 a、b 都被去掉。若只想删除一个完整前缀，可用 `removeprefix()`。输出多个清理结果时，别忘了 `print()` 默认还会在参数之间加一个空格，应把清理后的内容与输出分隔符分开计算。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-14 | 4-14 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

`True`、`False`、`False`。

:::

::: explanation

b=a 共享同一对象；copy() 和 [:] 都创建不同的外层列表对象。

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

:::: question blank-15 | 4-15 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

第1空：`id,name`；第2空：`students[index][0],students[index][1]`。

:::

::: explanation

第一种循环直接拆包行元组；第二种先取行，再取第 0 和第 1 列，逗号让 print 用默认空格分隔。

<!-- teaching-notes:start -->

**从本题理解：遍历元素、遍历下标与拆包**

`for row in students` 每次拿到一整行，`row[0]` 再访问其中第一个字段；`for number,name in students` 则要求每行恰好有两个元素，并直接拆包。二维访问 `students[i][j]` 是先选第 i 行，再选该行第 j 项，不是同时对一个平面下标取值。

```python
students = [(1001, '张三'), (1002, '李四')]
for index, (number, name) in enumerate(students):
    print(index, number, name)
```

只需要内容时直接遍历元素；还需要下标时使用 `enumerate()`；需要特定方向或步长时再遍历 `range()`。拆包不会自动转换类型，字符串拆包得到的仍是字符。也尽量避免用 `id`、`list` 等内置名称命名变量，防止遮蔽其功能。

继续阅读：[第3章：计数、序列拆包与元组](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-16 | 4-16 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

`print(sum((1,3,5,7,9))/len((1,3,5,7,9)))`的输出是 _____ 。

::: answer

`5.0`。

:::

::: explanation

sum 为 25、len 为 5，Python 3 的 / 返回浮点数 5.0。

<!-- teaching-notes:start -->

**从本题理解：计数、求和、平均值与最值累积**

`len()` 数元素个数，`sum()` 累加数值，平均值是 `sum(values)/len(values)`。Python 3 的 `/` 返回普通除法结果，因此 25 除以 5 输出 `5.0`；换成 `//` 会改变含义，不能为了输出没有小数点就随意换运算符。空序列需要先处理，避免除以 0。

逐项统计可维护一个累积量：求和从 0 开始；计数遇到匹配加 1；求非负长度最大值可从 0 开始，再令 `longest=max(longest,当前长度)`。每次循环结束后，这个变量都应该代表“已经处理过的所有数据”的统计结果。比较是否高于平均值时，也可比较 `x*人数 > 总和`，避免不必要的浮点除法。

继续阅读：[第4章：循环、搜索和最值](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question blank-17 | 4-17 填空题

<div class="section-label">题干 <span>QUESTION</span></div>

下面程序的输出是 _____ 。

```python
t=1
t,a=2,t+1
print(a)
```

::: answer

`2`。

:::

::: explanation

先计算右侧，此时旧 t 为 1，因此 t+1=2，然后再赋给 a。

<!-- teaching-notes:start -->

**从本题理解：赋值、表达式与拆包顺序**

普通 `=` 是赋值语句，不是比较运算 `==`，不能直接嵌入 `x=(y=z+1)+1` 这种表达式。若两个名字都要接收同一个结果，可写 `x=y=z+1`。`i*=3+5` 要先求出整个右侧，数值情形下相当于 `i=i*(3+5)`，不是 `i=i*3+5`。

拆包赋值先求整个右侧，再从左到右赋给各目标。若旧 `t=1`，`t,a=2,t+1` 先得到右侧 `(2,2)`，所以 `a=2`；交换 `a,b=b,a` 也利用此规则。右侧必须可迭代且元素数量匹配：整数 34 不能直接拆成 3 和 4，字符串 `'3 4'` 则有 3 个字符，而不是两个数。

继续阅读：[第2章：赋值与拆包](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

<h2 id="programming" class="quiz-group">编程题<span>17 QUESTIONS</span></h2>

:::: question programming-1 | 7-1 大于身高的平均值

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
heights = list(map(int, input().split()))
total = sum(heights)
for height in heights:
    if height * len(heights) > total:
        print(height, end=' ')
print()
```

:::

::: explanation

通过 height×人数 > 总和 比较是否高于平均值，避免浮点误差，保留原输入顺序及每个数后的空格。

<!-- teaching-notes:start -->

**解题步骤与边界**

先读完整组身高并求总和，再按原顺序逐一判断。条件 `height*人数 > 总和` 与“身高严格大于平均值”等价，却无需浮点除法。等于平均值的不输出，也不能先排序改变原序。每个合格身高后按样例保留一个空格，最后另行换行。

**从本题理解：计数、求和、平均值与最值累积**

`len()` 数元素个数，`sum()` 累加数值，平均值是 `sum(values)/len(values)`。Python 3 的 `/` 返回普通除法结果，因此 25 除以 5 输出 `5.0`；换成 `//` 会改变含义，不能为了输出没有小数点就随意换运算符。空序列需要先处理，避免除以 0。

逐项统计可维护一个累积量：求和从 0 开始；计数遇到匹配加 1；求非负长度最大值可从 0 开始，再令 `longest=max(longest,当前长度)`。每次循环结束后，这个变量都应该代表“已经处理过的所有数据”的统计结果。比较是否高于平均值时，也可比较 `x*人数 > 总和`，避免不必要的浮点除法。

继续阅读：[第4章：循环、搜索和最值](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-2 | 7-2 输出字母在字符串中位置索引

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
s = input()
a, b = input().split()
for i in range(len(s) - 1, -1, -1):
    if s[i] == a or s[i] == b:
        print(i, s[i])
```

:::

::: explanation

从最大下标倒序检查，两种字符任意匹配即输出；即使两字符相同也不会重复输出。

<!-- teaching-notes:start -->

**解题步骤与边界**

最大合法下标是 `len(s)-1`，倒序遍历用 `range(len(s)-1,-1,-1)`，其中终点 -1 不会被取到，所以下标 0 仍会检查。匹配 a 或 b 用一个 `or`，两字符恰好相同时也只输出一次。输出的是原字符串下标和原字符，不能先反转字符串后直接使用反转后的下标。

**从本题理解：查存在、查位置与查全部匹配**

只判断有无时使用 `x in seq`，结果为布尔值。字符串 `find()` 返回第一次匹配的起始下标，找不到返回 -1；字符串和列表的 `index()` 也查首次位置，但找不到会引发 `ValueError`。列表没有 `find()` 方法。

```python
s = 'programming'
print(s.find('r'))      # 1
print(s.find('r', 2))   # 4：从下标 2 开始找
print('x' in s)         # False
```

不能写 `if s.find(x)` 判断存在：找到在下标 0 时是假值，没找到的 -1 反而是真值。应写 `if x in s` 或 `if s.find(x) != -1`。题目要求输出所有匹配位置时，需要遍历下标或重复搜索，而不是只调用一次查找；要求倒序位置时还需改变遍历方向。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-3 | 7-3 求整数的位数及各位数字之和

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
s = str(int(input()))
print(len(s), sum(int(c) for c in s))
```

:::

::: explanation

整数转成规范字符串后，用长度统计位数，逐字符转数字求和。

<!-- teaching-notes:start -->

**解题步骤与边界**

先把输入规范化为整数，再转成字符串，因而不会把前导零算进位数。位数等于字符个数，各位和则逐字符转成整数累加。输入 0 时字符串是 `0`，位数为 1、数字和为 0。代码按题目给定的非负数范围工作；若扩展到负数，应先取绝对值，不能把负号送给 `int(c)`。

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

:::: question programming-4 | 7-4 字符替换

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
s = input()
table = tuple('ZYXWVUTSRQPONMLKJIHGFEDCBA')
print(''.join(table[ord(c) - ord('A')] if 'A' <= c <= 'Z' else c for c in s))
```

:::

::: explanation

转换表按 A→Z、B→Y 的顺序保存，只替换大写英文字母，其余字符原样保留。

<!-- teaching-notes:start -->

**解题步骤与边界**

反向字母表从 Z 到 A，原字母相对 A 的偏移量为 `ord(c)-ord('A')`，用这个偏移量索引转换表。只转换 A～Z，其余字符原样保留。检查 A→Z、Z→A、M→N 三个位置，可以确认映射起点和方向；`join()` 只拼接结果，不增加分隔符。

**从本题理解：筛选条件与保留内容应分开设计**

字符串处理通常分三步：逐字符检查条件、保留需要的字符、用 `join()` 组成结果。用于判断的标准化形式不一定就是输出形式。例如不区分大小写地去重，可以用 `c.lower()` 判断是否见过，却把原字符 `c` 放进结果，这样能保留首次出现的大小写。

```python
text = 'A1-b2!'
clean = ''.join(c.lower() for c in text if c.isalnum())
print(clean)  # a1b2
```

先确认题目允许哪些字符：`isalnum()` 包括 Unicode 字母数字，十六进制则只能从 `0123456789abcdefABCDEF` 选择。还要明确空结果如何处理、是否保留空格、比较是否区分大小写。不要为简化代码而擅自删除题目没有要求忽略的字符。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-5 | 7-5 删除字符

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
s = input().strip()
target = input().strip().lower()
result = ''.join(c for c in s if c.lower() != target)
print('result:', result)
```

:::

::: explanation

按题意清理两端空格，用小写形式比较、原字符输出，保留字符串内部其他空格。

<!-- teaching-notes:start -->

**解题步骤与边界**

先按题意处理输入两端空格，再把目标字符转为小写，作为比较标准。遍历 s 时用 `c.lower()` 判断是否应删去，但保留下来的仍是原字符 c，因此不会把整串都变成小写。内部空格不应因删除字符而自动合并，若题意没有要求忽略大小写，也不能自行标准化。

**从本题理解：筛选条件与保留内容应分开设计**

字符串处理通常分三步：逐字符检查条件、保留需要的字符、用 `join()` 组成结果。用于判断的标准化形式不一定就是输出形式。例如不区分大小写地去重，可以用 `c.lower()` 判断是否见过，却把原字符 `c` 放进结果，这样能保留首次出现的大小写。

```python
text = 'A1-b2!'
clean = ''.join(c.lower() for c in text if c.isalnum())
print(clean)  # a1b2
```

先确认题目允许哪些字符：`isalnum()` 包括 Unicode 字母数字，十六进制则只能从 `0123456789abcdefABCDEF` 选择。还要明确空结果如何处理、是否保留空格、比较是否区分大小写。不要为简化代码而擅自删除题目没有要求忽略的字符。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-6 | 7-6 输出10个不重复的英文字母

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

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

:::

::: explanation

只接受英文字母，使用小写形式去重，保留首次出现的大小写与顺序，满 10 个立即停止。

<!-- teaching-notes:start -->

**解题步骤与边界**

`seen` 保存已经接受过的字母的小写形式，用于不区分大小写地判断重复；`result` 保存原字符，保留首次出现的大小写。先排除非英文字母，再判断首次出现，满 10 个后立即停止。最后检查是否确实凑够 10 个，不足时输出 `not found`，不能输出不完整结果。

**从本题理解：存在性、出现次数与字符多重集合**

“是否出现”用成员判断，“出现几次”需要计数，“字符和次数都一致”则需要比较多重集合。比如 `'aab'` 与 `'abb'` 的字符集合相同，但不是变位词，因为 a、b 的次数不同；排序后比较或 `collections.Counter` 才能保留次数信息。

去重又是另一种任务：集合可以快速记录见过的字符，但直接转集合不能保留原输入顺序。需要保序时，遍历原序列，用集合判断是否首次出现，再追加到结果。统计两个字符串共有多少字符前，也要看题目保证哪一边不重复；遍历重复的一边可能把同一个字符多算。大小写、空格、标点是否参与比较，都必须由题意决定。

继续阅读：[第5章：集合、字典与字符计数](../topics/chapter-05.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-7 | 7-7 逆序的三位数

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
print(int(input().strip()[::-1]))
```

:::

::: explanation

反转文本后转整数，自动去掉逆序结果的前导零，例如 700→007→7。

<!-- teaching-notes:start -->

**解题步骤与边界**

反转对象是数字的十进制文本，而不是整数本身。`[::-1]` 产生反向字符串，再转成整数会自动去掉前导零，所以 700 得到 7。此解按题目非负输入范围处理；若扩展到负数，需要单独保存符号，不能让反转后的负号落在末尾。

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

:::: question programming-8 | 7-8 判断两个字符串是否为变位词

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
a = input().lower()
b = input().lower()
print('yes' if sorted(a) == sorted(b) else 'no')
```

:::

::: explanation

按样例 1 忽略大小写，排序后逐字符比较，保留数字、空格及字符重复次数；不能只比较集合。原始样例 3 中 Wellcom 与 mocllew 在忽略大小写后确为变位词，但给定输出为 no，与题意及样例 1 冲突；本解按题意输出 yes，保留原始样例并注明差异。

<!-- teaching-notes:start -->

**解题步骤与边界**

先统一大小写，再对字符排序。排序既保留字符种类，也保留每种字符的出现次数，因此能区分 aab 与 abb；单纯比较 `set()` 做不到。空格、数字及标点没有被题意排除时都参与比较，不能随意删掉。原样例冲突仍按上文保留和说明，参考代码遵循忽略大小写的题意。

**从本题理解：存在性、出现次数与字符多重集合**

“是否出现”用成员判断，“出现几次”需要计数，“字符和次数都一致”则需要比较多重集合。比如 `'aab'` 与 `'abb'` 的字符集合相同，但不是变位词，因为 a、b 的次数不同；排序后比较或 `collections.Counter` 才能保留次数信息。

去重又是另一种任务：集合可以快速记录见过的字符，但直接转集合不能保留原输入顺序。需要保序时，遍历原序列，用集合判断是否首次出现，再追加到结果。统计两个字符串共有多少字符前，也要看题目保证哪一边不重复；遍历重复的一边可能把同一个字符多算。大小写、空格、标点是否参与比较，都必须由题意决定。

继续阅读：[第5章：集合、字典与字符计数](../topics/chapter-05.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-9 | 7-9 输入字符串，排序后输出最大字符及该字符在原字符串中的索引

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
s = input()
char, index = max((c, i) for i, c in enumerate(s))
print(f'{char}   {index}')
```

:::

::: explanation

元组先比较字符，再比较下标，因此重复最大字符时选最大下标；中间严格输出三个空格。题目按非空字符串处理。

<!-- teaching-notes:start -->

**解题步骤与边界**

`enumerate(s)` 产生字符及其下标，代码交换成 `(字符,下标)` 元组交给 `max()`。元组先比较第一项，相同才比较第二项，因此会选最大字符的最后一次出现位置。这是利用元组的字典序规则，而不是 `max()` 自动知道题意。非空字符串是前提，空串没有可选元素。

**从本题理解：排序的对象、顺序与返回值**

`sorted(items)` 返回新的已排序列表，原对象不变；`a.sort()` 原地修改列表并返回 `None`。要降序使用 `reverse=True`。`max()` 只取最大元素，不返回排序后的完整序列，空序列且无默认值时还会报错。

排序前先确定按什么比较：整数 `[2,10]` 排成 `[2,10]`，字符串 `['2','10']` 则排成 `['10','2']`。若题意是按数值大小，必须先转成数值再排序，最后再转回字符串用于输出。`random.shuffle(a)` 也原地修改列表并返回 `None`，但它是打乱，不是排序；不要写 `a=random.shuffle(a)`。

继续阅读：[第3章：列表方法](../topics/chapter-03.md)与[第4章：搜索和排序](../topics/chapter-04.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-10 | 7-10 计算有n个字符串中最长的字符串长度

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
n = int(input())
longest = 0
for _ in range(n):
    longest = max(longest, len(input().lstrip(' ')))
print(f'length={longest}')
```

:::

::: explanation

逐行读取，去掉左端普通空格，保留末尾空格，累计最大长度。输出前缀按样例为 length=。

<!-- teaching-notes:start -->

**解题步骤与边界**

每次用 `input()` 读取完整一行，只去掉左侧普通空格后测长度。末尾空格属于有效内容，不能用 `strip()`；中间空格也不能用拆分输入的方式破坏。`longest` 从 0 开始，每轮代表已读各行的最大有效长度。输出 `length=` 后紧跟数值，没有额外空格。

**从本题理解：清理哪一端，保留哪些字符**

`strip()` 清理两端空白，`lstrip()` 仅清理左端，`rstrip()` 仅清理右端；它们都返回新字符串，保留中间空格。默认空白还包括制表符、换行符，而 `lstrip(' ')` 明确只清理普通空格。题目要求保留尾部空格时，不能用 `strip()` 替代单侧处理。

传入参数时，它表示“可被清理的字符集合”，不是一个固定前缀或后缀。例如 `'abbaXba'.strip('ab')` 得到 `'X'`，因为两端连续的 a、b 都被去掉。若只想删除一个完整前缀，可用 `removeprefix()`。输出多个清理结果时，别忘了 `print()` 默认还会在参数之间加一个空格，应把清理后的内容与输出分隔符分开计算。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-11 | 7-11 位1的个数

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
n = int(input())
print(bin(n).count('1'))
```

:::

::: explanation

bin 得到二进制文本，统计 1 的出现次数，n=0 时也正确得到 0。

<!-- teaching-notes:start -->

**解题步骤与边界**

`bin(n)` 返回带 `0b` 前缀的二进制字符串，前缀里没有字符 1，因此直接统计 `1` 即可。n=0 得到 `0b0`，统计结果仍是 0。这里统计的是值为 1 的位，不是总位数，也不是十进制数字 1 的个数；补前导零不会改变答案。

**从本题理解：按位运算与数位统计**

先把整数对齐为二进制位，再逐位计算：`&` 仅在两位都为 1 时得 1，`|` 有一位为 1 就得 1，`^` 仅在两位不同时得 1。因此 `x^y` 中的 1 的个数，就是两个非负整数二进制表示的不同位数。`^` 不是乘方，乘方要写 `**`。

负整数按符号扩展的补码语义处理，可以选足够宽的位数手算，但不能把最高位截掉后当成无符号数。取反满足 `~x == -x-1`，例如 `~9=-10`。统计二进制 1 的数量可用 `bin(n).count('1')`，而统计总位数时，0 和负数的符号、前缀需要另行分析。本节按课程范围说明保留，不代表新增考试要求。

继续阅读：[第2章：位运算](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-12 | 7-12 整数的二进制相加

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
a = int(input())
b = int(input())
print(f'{a:08b}')
print(f'{b:08b}')
print('--------')
print(f'{a + b:08b}')
```

:::

::: explanation

08b 表示二进制并补零到 8 位，先输出两操作数，再输出分隔线及和。

<!-- teaching-notes:start -->

**解题步骤与边界**

分别把两个整数格式化为至少 8 位二进制，然后输出分隔线和两数的和。`08b` 中 0 表示补零，8 是最小宽度，b 是二进制；若和需要第 9 位，不会被截掉。不要只把两个输入的二进制字符串拼接，也不要先把格式化文本当十进制数相加。

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

:::: question programming-13 | 7-13 汉明距离

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
x, y = map(int, input().split())
print(bin(x ^ y).count('1'))
```

:::

::: explanation

异或在不同二进制位上产生 1，统计这些 1 即为汉明距离。

<!-- teaching-notes:start -->

**解题步骤与边界**

对每一二进制位，异或只在两数该位不同的时候产生 1。因此先求 `x^y`，再统计其二进制中 1 的数量即可。两数相等时异或为 0，距离为 0；高位补零后仍适用。这个做法依赖题目的非负整数表示语义，负数若未规定固定字长，不能直接照搬汉明距离解释。

**从本题理解：按位运算与数位统计**

先把整数对齐为二进制位，再逐位计算：`&` 仅在两位都为 1 时得 1，`|` 有一位为 1 就得 1，`^` 仅在两位不同时得 1。因此 `x^y` 中的 1 的个数，就是两个非负整数二进制表示的不同位数。`^` 不是乘方，乘方要写 `**`。

负整数按符号扩展的补码语义处理，可以选足够宽的位数手算，但不能把最高位截掉后当成无符号数。取反满足 `~x == -x-1`，例如 `~9=-10`。统计二进制 1 的数量可用 `bin(n).count('1')`，而统计总位数时，0 和负数的符号、前缀需要另行分析。本节按课程范围说明保留，不代表新增考试要求。

继续阅读：[第2章：位运算](../topics/chapter-02.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-14 | 7-14 判断回文字符串

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
s = ''.join(c.lower() for c in input() if c.isalnum())
print('yes' if s == s[::-1] else 'no')
```

:::

::: explanation

只保留字母数字、统一小写，再比较自身与逆序字符串。isalnum 按 Unicode 字符规则判断。

<!-- teaching-notes:start -->

**解题步骤与边界**

先筛出字母数字，再统一小写，最后比较标准化字符串与逆序结果。三个步骤的顺序与目的要分开：标点不参与，大小写不影响匹配，数字仍参与。清理后为空串时，它和自身逆序相等，代码输出 yes。若题目只允许 ASCII 字母数字，需要相应缩小筛选范围。

**从本题理解：筛选条件与保留内容应分开设计**

字符串处理通常分三步：逐字符检查条件、保留需要的字符、用 `join()` 组成结果。用于判断的标准化形式不一定就是输出形式。例如不区分大小写地去重，可以用 `c.lower()` 判断是否见过，却把原字符 `c` 放进结果，这样能保留首次出现的大小写。

```python
text = 'A1-b2!'
clean = ''.join(c.lower() for c in text if c.isalnum())
print(clean)  # a1b2
```

先确认题目允许哪些字符：`isalnum()` 包括 Unicode 字母数字，十六进制则只能从 `0123456789abcdefABCDEF` 选择。还要明确空结果如何处理、是否保留空格、比较是否区分大小写。不要为简化代码而擅自删除题目没有要求忽略的字符。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-15 | 7-15 输入一行字符串，并将它转换成10进制数输出

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
s = input()
h = ''.join(c for c in s if c in '0123456789abcdefABCDEF')
print(h)
print(int(h, 16) if h else 0)
```

:::

::: explanation

筛选合法十六进制字符，保留原大小写，再按基数 16 转整数。题面未规定完全无合法字符时的输出，此解约定输出空行和 0。

<!-- teaching-notes:start -->

**解题步骤与边界**

按原顺序筛出合法十六进制字符，构造 h；保留原字符是为了满足第一行输出的大小写要求。第二行再用 `int(h,16)` 计算数值，例如 a1B 为 `10*16**2+1*16+11=2587`。`isalnum()` 会接受 G 等非法十六进制字符，不能替代白名单。空结果的处理约定已在上文说明。

**从本题理解：筛选条件与保留内容应分开设计**

字符串处理通常分三步：逐字符检查条件、保留需要的字符、用 `join()` 组成结果。用于判断的标准化形式不一定就是输出形式。例如不区分大小写地去重，可以用 `c.lower()` 判断是否见过，却把原字符 `c` 放进结果，这样能保留首次出现的大小写。

```python
text = 'A1-b2!'
clean = ''.join(c.lower() for c in text if c.isalnum())
print(clean)  # a1b2
```

先确认题目允许哪些字符：`isalnum()` 包括 Unicode 字母数字，十六进制则只能从 `0123456789abcdefABCDEF` 选择。还要明确空结果如何处理、是否保留空格、比较是否区分大小写。不要为简化代码而擅自删除题目没有要求忽略的字符。

继续阅读：[第3章：字符串使用](../topics/chapter-03.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-16 | 7-16 统计满足特定条件的字符数

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

```python
a = input()
b = input()
print(sum(c in b for c in a))
```

:::

::: explanation

遍历不含重复字符的 A，逐个判断是否在 B 中，不统计 B 中的重复次数，比较区分大小写。

<!-- teaching-notes:start -->

**解题步骤与边界**

A 保证没有重复字符，因此逐个遍历 A 并检查是否在 B 中，每个共同字符恰好计数一次。布尔值可参与求和，`sum(c in b for c in a)` 就是把每次匹配的 True 当成 1。不能改为遍历 B，因为它的重复字符可能多算；大小写按原字符比较，不能额外转小写。

**从本题理解：存在性、出现次数与字符多重集合**

“是否出现”用成员判断，“出现几次”需要计数，“字符和次数都一致”则需要比较多重集合。比如 `'aab'` 与 `'abb'` 的字符集合相同，但不是变位词，因为 a、b 的次数不同；排序后比较或 `collections.Counter` 才能保留次数信息。

去重又是另一种任务：集合可以快速记录见过的字符，但直接转集合不能保留原输入顺序。需要保序时，遍历原序列，用集合判断是否首次出现，再追加到结果。统计两个字符串共有多少字符前，也要看题目保证哪一边不重复；遍历重复的一边可能把同一个字符多算。大小写、空格、标点是否参与比较，都必须由题意决定。

继续阅读：[第5章：集合、字典与字符计数](../topics/chapter-05.md)。

<!-- teaching-notes:end -->

:::

::::

:::: question programming-17 | 7-17 查验身份证

<div class="section-label">题干 <span>QUESTION</span></div>

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

::: answer

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

:::

::: explanation

先确认前 17 位均为数字，再计算加权和，对 11 取模并查表。按输入顺序保存错误号码，全部正确时输出 All passed。

<!-- teaching-notes:start -->

**解题步骤与边界**

先检查长度和前 17 位是否均为十进制数字，避免转换时报错；合法后让每一位与对应权重相乘，再求和。余数 `total%11` 是校验表下标，查到的字符必须与第 18 位完全一致，包括大写 X。错误号码按输入顺序收集，最后统一输出；只有列表为空时才输出 `All passed`。

**从本题理解：存在性、出现次数与字符多重集合**

“是否出现”用成员判断，“出现几次”需要计数，“字符和次数都一致”则需要比较多重集合。比如 `'aab'` 与 `'abb'` 的字符集合相同，但不是变位词，因为 a、b 的次数不同；排序后比较或 `collections.Counter` 才能保留次数信息。

去重又是另一种任务：集合可以快速记录见过的字符，但直接转集合不能保留原输入顺序。需要保序时，遍历原序列，用集合判断是否首次出现，再追加到结果。统计两个字符串共有多少字符前，也要看题目保证哪一边不重复；遍历重复的一边可能把同一个字符多算。大小写、空格、标点是否参与比较，都必须由题意决定。

继续阅读：[第5章：集合、字典与字符计数](../topics/chapter-05.md)。

<!-- teaching-notes:end -->

:::

::::
