---
title: 第4章作业
eyebrow: HOMEWORK 04
code: HOMEWORK 04
description: 题目、参考答案与解析。
questionGroups:
  - [判断题, judgment, 8]
  - [单选题, choice, 7]
  - [填空题, blank, 11]
  - [编程题, programming, 22]
---

<h2 id="judgment" class="quiz-group">判断题<span>08 QUESTIONS</span></h2>

:::: question judgment-1 | 1-1 判断题

在循环中 `continue` 语句的作用是退出循环的当前迭代。

<div class="question-tags"><span class="question-tag">continue</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先弄清两个词：循环体每执行一遍叫一次“迭代”（也就是一“轮”）；“退出当前迭代”的意思是**放弃这一轮后面还没执行的语句，直接进入下一轮**。它并不会结束整个循环，所以题目的说法是正确的。

看下面的例子，当 `i` 等于 3 时执行 `continue`：

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

逐轮走一遍：

- `i` 为 1、2：不满足 `i == 3`，正常执行 `print(i)`，输出 1、2。
- `i` 为 3：满足条件，执行 `continue`，这一轮后面的 `print(i)` 被跳过，所以 3 没有被输出。
- `i` 为 4、5：循环仍在继续，正常输出 4、5。

最终输出 `1 2 4 5`（每个数占一行）。可以看到，只有 3 这一轮被跳过，循环本身并没有停止。

跳过本轮之后接着做什么，取决于循环的类型：

- `for` 循环：取序列中的下一个元素，开始下一轮。
- `while` 循环：回到开头重新判断循环条件，条件成立才进入下一轮。

**易混淆点：** `continue` 只跳过“这一轮”，`break` 才是结束“整个循环”。如果把例子里的 `continue` 换成 `break`，输出就只剩 `1 2`。

</div>

:::

::::

:::: question judgment-2 | 1-2 判断题

带有 `else` 子句的循环如果因为执行了 `break` 语句而退出的话，会执行 `else` 子句的代码。

<div class="question-tags"><span class="question-tag">循环的 else 子句</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

循环的 `else` 子句有一条规则：**循环自然走完时才执行，被 `break` 打断时不执行**。

“自然走完”指的是：`for` 把序列里的元素全部取完，或者 `while` 的条件变成假。

对比下面两段代码：

```python
# 例 1：没有遇到 break，循环自然结束
for i in range(3):
    print(i)
else:
    print("循环结束")
```

输出 `0`、`1`、`2`、`循环结束`。3 个数都取完了，没有被打断，所以 `else` 执行。

```python
# 例 2：中途遇到 break
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("循环结束")
```

输出只有 `0`。`i` 等于 1 时执行 `break`，直接离开整个循环，`else` 被跳过，不会打印“循环结束”。

所以题目说“因为 `break` 退出时会执行 `else`”是错的，应该是**不会**执行。

**记忆方法：** 可以把循环的 `else` 理解成“没有被 `break` 打断时要做的收尾”。常见用法是查找：找到就 `break`，走完都没找到才执行 `else`，例如判断素数的题目就是这样用的。

</div>

:::

::::

:::: question judgment-3 | 1-3 判断题

使用 `for i in range(10)` 和 `for i in range(10,20)`，控制循环次数是一样的。

<div class="question-tags"><span class="question-tag">range</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

T（正确）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先记住 `range` 的取值规则：**包含起点，不包含终点**，也就是“左闭右开”。

- `range(10)` 等价于 `range(0, 10)`，起点省略时默认为 0，依次取 0、1、2、……、9，共 10 个数。
- `range(10, 20)` 依次取 10、11、12、……、19，共 10 个数（20 取不到）。

循环体执行几次，只取决于 `range` 里**有几个数**，与这些数的具体大小无关。两个 `range` 都有 10 个数，所以循环体都执行 10 次，题目的说法正确。

可以用下面的代码验证，两段都会输出 `10`：

```python
count = 0
for i in range(10):
    count += 1
print(count)

count = 0
for i in range(10, 20):
    count += 1
print(count)
```

两者的区别在于变量 `i` 的值：前者 `i` 从 0 变到 9，后者 `i` 从 10 变到 19。

**快速算法：** `range(a, b)` 的个数是 `b - a`（`b > a` 时），所以 `range(10, 20)` 有 20 − 10 = 10 个数。

</div>

:::

::::

:::: question judgment-4 | 1-4 判断题

在 Python 语言里，循环结构必须有 `else` 子句。

<div class="question-tags"><span class="question-tag">循环结构</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

`else` 是可选的。比如下面的循环只包含循环体，也能依次输出 0、1、2。

```python
for i in range(3):
    print(i)
```

</div>

:::

::::

:::: question judgment-5 | 1-5 判断题

下面程序输入 36，输出是 10。

```python
a=[3,5,7,11,13,16,21,24,28,32,36,40,46]
x = int(input())
found = -1
left = 0                 #第一个元素下标
right = len(a)-1         #最后一个元素下标
while left<right:
    mid = (left + right) // 2
    if a[mid] > x:
        right = mid - 1
    elif a[mid] < x:
        left = mid + 1
    else:                # a[mid]==x
        found = mid
        break
print(found)
```

<div class="question-tags"><span class="question-tag">二分查找</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

二分查找的思路是：`left` 和 `right` 表示还没排除的查找范围的两端，每次取中间位置 `mid` 的元素和 `x` 比较。

- 中间值比 `x` 大：`x` 只可能在左半边，所以 `right = mid - 1`。
- 中间值比 `x` 小：`x` 只可能在右半边，所以 `left = mid + 1`。
- 相等：找到了，记下 `mid` 并 `break`。

先数一下列表：共 13 个元素，下标 0 到 12，其中 `a[10]` 是 36。所以如果程序正确，应该输出 10。逐轮走一遍（`x = 36`）：

| 轮次 | left | right | mid = (left+right)//2 | a[mid] | 比较结果 | 下一步 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 12 | 6 | 21 | 21 < 36 | `left = 7` |
| 2 | 7 | 12 | 9 | 32 | 32 < 36 | `left = 10` |
| 3 | 10 | 12 | 11 | 40 | 40 > 36 | `right = 10` |
| 4 | 10 | 10 | — | — | `left < right` 为假 | 退出循环 |

第 3 轮之后，查找范围缩小到只剩下标 10 一个位置，而 36 恰好就在这里。但是循环条件写的是 `left<right`，`left` 和 `right` 相等时就不再进入循环，所以这最后一个位置没有被检查，`found` 始终是初始值 `-1`，输出 `-1`，不是 10。

**问题出在哪：** 范围里只剩一个元素时（`left == right`），这个元素仍然需要检查。标准写法的循环条件是 `while left <= right`，改成这样就能输出 10。

</div>

:::

::::

:::: question judgment-6 | 1-6 判断题

下面程序的输出是 3。

```python
lst=[34,6,7,0,0,0,9]
n=0
for i in lst:
    if i==0:
        lst.remove(i)
        n+=1
print(n)
```

<div class="question-tags"><span class="question-tag">遍历时删除元素</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

关键点：用 `for i in lst` 遍历列表时，Python 是靠一个**下标**依次取元素的（先取下标 0，再取下标 1……）。如果在遍历过程中删除元素，后面的元素会整体左移一位，但下标仍然照常加 1，于是有的元素会被“跳过”。

另外，`lst.remove(i)` 删除的是列表中**第一个**等于 `i` 的元素，不一定是当前位置的那个。

逐步走一遍，初始列表是 `[34,6,7,0,0,0,9]`：

| 当前下标 | 读到的 `i` | 操作 | 操作后的列表 | `n` |
| --- | --- | --- | --- | --- |
| 0 | 34 | 不是 0，跳过 | `[34,6,7,0,0,0,9]` | 0 |
| 1 | 6 | 不是 0，跳过 | `[34,6,7,0,0,0,9]` | 0 |
| 2 | 7 | 不是 0，跳过 | `[34,6,7,0,0,0,9]` | 0 |
| 3 | 0 | 删除第一个 0 | `[34,6,7,0,0,9]` | 1 |
| 4 | 0 | 删除第一个 0 | `[34,6,7,0,9]` | 2 |
| 5 | — | 列表只剩 5 个元素，下标 5 越界，遍历结束 | `[34,6,7,0,9]` | 2 |

第一次删除后，原来下标 4 的 0 左移到了下标 3，而循环下一步去看下标 4，于是这个 0 被跳过了。最后列表里还留着一个 0，所以 `n` 只有 2，不是 3，输出 `2`。

**经验：** 不要一边遍历列表一边删除它的元素。需要删除时，可以遍历列表的副本（`for i in lst[:]`），或者先把要保留的元素收集到新列表里。

</div>

:::

::::

:::: question judgment-7 | 1-7 判断题

下面程序输出是 2。

```python
lst=[0,34,6,0,7,0,9]
n=0
for i in lst:
    if i==0:
        lst.remove(i)
        n+=1
print(n)
```

<div class="question-tags"><span class="question-tag">遍历时删除元素</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这题和上一题（1-6）原理相同：遍历时删除元素，后面的元素左移，但下标照常加 1，所以有的元素会被跳过。`remove(i)` 删除的是列表中**第一个**等于 `i` 的元素。

逐步走一遍，初始列表是 `[0,34,6,0,7,0,9]`：

| 当前下标 | 读到的 `i` | 操作 | 操作后的列表 | `n` |
| --- | --- | --- | --- | --- |
| 0 | 0 | 删除第一个 0 | `[34,6,0,7,0,9]` | 1 |
| 1 | 6 | 不是 0，跳过 | `[34,6,0,7,0,9]` | 1 |
| 2 | 0 | 删除第一个 0 | `[34,6,7,0,9]` | 2 |
| 3 | 0 | 删除第一个 0 | `[34,6,7,9]` | 3 |
| 4 | — | 列表只剩 4 个元素，下标 4 越界，遍历结束 | `[34,6,7,9]` | 3 |

第一次删除后，34 左移到下标 0，循环下一步直接看下标 1，34 被跳过（它不是 0，所以没有影响结果）。第二次删除后，7 左移，同样被跳过，但它后面的 0 正好落在下标 3，被读到并删除。

三个 0 都被删除并计数，`n` 为 3，所以输出 `3`，题目说的 2 是错的。

**对比：** 这一题的 0 被其他数隔开，所以没有漏掉；1-6 里三个 0 连在一起，才漏掉了一个。

</div>

:::

::::

:::: question judgment-8 | 1-8 判断题

下面程序输出值是 1。

```python
data=[[1]*3]*3
data[0][1]=45
print(data[2][1])
```

<div class="question-tags"><span class="question-tag">二维列表引用</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

F（错误）。

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这题考的是列表的“引用”：列表是可变对象，变量或列表元素保存的并不是列表本身，而是指向它的“地址”。

分两步看 `data=[[1]*3]*3`：

1. 先算内层 `[1]*3`，得到**一个**新列表 `[1,1,1]`，记作行 A。
2. 再算外层 `[行A]*3`，它只是把“行 A 的地址”复制了 3 份，并没有造出 3 个新列表。

所以 `data` 的三个位置指向的是**同一个**行 A：

```text
data[0] ─┐
data[1] ─┼─→ 行 A：[1, 1, 1]
data[2] ─┘
```

执行 `data[0][1]=45` 时，修改的是行 A 的第二个元素，行 A 变成 `[1,45,1]`。由于 `data[2]` 也指向行 A，`data[2][1]` 读到的就是 `45`，不是 `1`，所以题目的说法错误。

此时整个 `data` 打印出来是 `[[1,45,1],[1,45,1],[1,45,1]]`，三行同时变了。

可以用 `is` 验证它们是同一个对象：

```python
data = [[1]*3]*3
print(data[0] is data[2])  # True
```

**正确创建二维列表的写法：** `data = [[1]*3 for _ in range(3)]`，每一轮循环都会新建一行，三行互相独立（见 4-10 题）。

</div>

:::

::::

<h2 id="choice" class="quiz-group">单选题<span>07 QUESTIONS</span></h2>

:::: question choice-1 | 2-1 单选题

continue语句用于________。

**A.** 退出循环程序

**B.** 结束本次循环

**C.** 空操作

**D.** 引发异常处理

<div class="question-tags"><span class="question-tag">continue</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

遇到 `continue`，程序跳过本轮余下的语句，接着判断能否进入下一轮。要退出整个循环才使用 `break`。

</div>

:::

::::

:::: question choice-2 | 2-2 单选题

下面程序中 ，i的循环终值是__________。

```python
for  i  in  range(10):
      print(i)
```

**A.** 9

**B.** 10

**C.** 11

**D.** 以上都不对

<div class="question-tags"><span class="question-tag">range</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

“循环终值”指的是循环变量 `i` 在最后一轮的取值。

`range(10)` 的规则是**从 0 开始，到 10 之前停止，10 本身取不到**。所以 `i` 依次被赋值为 0、1、2、3、4、5、6、7、8、9，一共 10 轮。

程序输出：

```text
0
1
2
3
4
5
6
7
8
9
```

最后一轮 `i` 等于 9，所以终值是 9，选 A。

**易错点：** 看到 `range(10)` 容易以为 `i` 会走到 10。其实 10 是“停止的界限”，不是最后一个取值。记住：`range(n)` 的取值是 0 到 n−1，共 n 个数。

</div>

:::

::::

:::: question choice-3 | 2-3 单选题

下面程序中语句print(i*j)共执行了___________________次。

```python
for i in  range(5):
       for j in range(2,5):
             print(i*j)
```

**A.** 15

**B.** 14

**C.** 20

**D.** 12

<div class="question-tags"><span class="question-tag">嵌套循环</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

嵌套循环的规则是：**外层循环每走一轮，内层循环都会从头完整地走一遍**。所以总次数 = 外层轮数 × 内层每轮次数。

- 外层 `range(5)`：i 取 0、1、2、3、4，共 **5** 轮。
- 内层 `range(2,5)`：从 2 开始，到 5 之前停止，j 取 2、3、4，共 **3** 个数（用 5 − 2 = 3 也能算出来）。

把每一轮写出来：

| 外层 i | 内层 j 依次取值 | 打印的 `i*j` | 打印次数 |
| --- | --- | --- | --- |
| 0 | 2、3、4 | 0、0、0 | 3 |
| 1 | 2、3、4 | 2、3、4 | 3 |
| 2 | 2、3、4 | 4、6、8 | 3 |
| 3 | 2、3、4 | 6、9、12 | 3 |
| 4 | 2、3、4 | 8、12、16 | 3 |

每一行打印 3 次，共 5 行，总次数是 5 × 3 = 15，选 A。

**易错点：** 题目问的是 `print` 语句**执行了几次**，不是打印出了几个不同的数。`i` 为 0 时打印的虽然都是 0，每个 0 也各算一次。

</div>

:::

::::

:::: question choice-4 | 2-4 单选题

执行下面程序产生的结果是___________________。

```python
x=2;y=2.0   #分号可把两个语句写在一行
if(x==y):
   print("相等")
else:
   print("不相等")
```

**A.** 相等

**B.** 不相等

**C.** 运行错误

**D.** 死循环

<div class="question-tags"><span class="question-tag">数值比较</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先看两个变量：`x=2` 是整数（`int`），`y=2.0` 是浮点数（`float`），它们的**类型不同**。

但 `==` 比较的是**数值**是否相等，不比较类型。Python 会先把整数 2 当作 2.0 再比较，结果是相等，所以 `x == y` 的值为 `True`。

逐步执行：

1. `x=2;y=2.0`：分号只是把两条语句写在同一行，等价于分成两行写。
2. 判断 `if(x==y)`：条件为 `True`，进入 `if` 分支。
3. 执行 `print("相等")`，`else` 分支被跳过。

输出 `相等`，选 A。

可以自己在终端验证：

```python
print(2 == 2.0)        # True，数值相等
print(type(2) == type(2.0))  # False，类型不同
```

**易错点：** 不要把“类型不同”和“值不相等”混为一谈。题目没有要求判断类型，所以不会走 `else`。也不存在运行错误：整数和浮点数比较是合法的，程序也不含循环，不会死循环。

</div>

:::

::::

:::: question choice-5 | 2-5 单选题

下面那个语句不能完成1到10的累加功能, total初值为0。

**A.** `for i in range(10,0):total+=i`

**B.** `for i in range(1,11):total+=i`

**C.** `for i in range(10,0,-1):total+=i`

**D.** `for i in (10,9,8,7,6,5,4,3,2,1):total+=i`

<div class="question-tags"><span class="question-tag">步长</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

A

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先记住 `range` 的完整写法：`range(起点, 终点, 步长)`。

- 取值**包含起点，不包含终点**。
- 步长省略时默认是 **+1**，即每次加 1。
- 步长为正，数字往大走，必须起点小于终点才有数；步长为负，数字往小走，必须起点大于终点才有数。

题目问的是“**不能**完成 1 到 10 累加”的那一项，逐项检查：

| 选项 | `range` 取到的数 | 累加结果 | 能否完成 |
| --- | --- | --- | --- |
| A. `range(10,0)` | 步长默认 +1，从 10 往大走，起点 10 已经大于终点 0，**一个数都没有** | `total` 仍为 0 | **不能** |
| B. `range(1,11)` | 1、2、……、10 | 55 | 能 |
| C. `range(10,0,-1)` | 步长 −1，10、9、……、1（0 取不到） | 55 | 能 |
| D. `for i in (10,9,...,1)` | 直接遍历这个元组，依次取 10 到 1 | 55 | 能 |

所以 A 的循环体一次也不会执行，选 A。

**易错点：** 想让 `range` 倒着数，必须**显式写出负的步长**，如 `range(10,0,-1)`。只写 `range(10,0)` 不会自动倒数，得到的是空序列。

</div>

:::

::::

:::: question choice-6 | 2-6 单选题

下面程序的运行结果是什么？

```python
s=0
a,b=1,2
if a>0:
    s=s+1
elif b>0:
    s=s+1
print(s)
```

**A.** 错误

**B.** 0

**C.** 1

**D.** 2

<div class="question-tags"><span class="question-tag">条件分支</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

C

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这题考的是 `if…elif` 的执行规则：**一组 `if / elif / else` 中，从上到下依次判断，只要有一个条件成立，就执行它的语句，后面的分支不再判断，直接跳过。**

先看变量：`a,b=1,2` 把 `a` 赋值为 1，`b` 赋值为 2，开头 `s=0`。

逐步执行：

1. 判断 `if a>0`：`a` 是 1，条件成立，执行 `s=s+1`，`s` 变成 1。
2. 因为 `if` 已经成立，后面的 `elif b>0` **不会被检查**，它的 `s=s+1` 也不会执行。
3. 执行 `print(s)`，输出 `1`，选 C。

**易错点：** 容易看到 `b>0` 也成立，就以为 `s` 加了两次，选成 2。如果想让两个条件都被检查，要把 `elif` 改成独立的 `if`：

```python
s=0
a,b=1,2
if a>0:
    s=s+1
if b>0:      # 独立的 if，会单独判断
    s=s+1
print(s)     # 输出 2
```

`elif` 的意思是“否则如果”，只有前面的条件不成立时才轮到它。

</div>

:::

::::

:::: question choice-7 | 2-7 单选题

下面程序输入`1`时，输出是什么？。

```python
num=int(input())
a=num-1
while a>1:
   if num % a == 0:
        print("不是素数")
        break
   a=a-1
else:
   print("是素数")
```

**A.** 不是素数

**B.** 是素数

**C.** 没有输出

**D.** 出现异常

<div class="question-tags"><span class="question-tag">while…else</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

B

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先回顾规则：`while` 的 `else` 在**循环条件变为假、循环自然结束**时执行；如果循环中途被 `break` 打断，就不执行（见 1-2 题）。

逐步执行，输入 `1`：

1. `num=1`，`a=num-1=0`。
2. 判断 `while a>1`：0 > 1 不成立，**循环体一次都没有执行**。
3. 循环没有被 `break` 打断，属于“条件变假而结束”，所以执行 `else`，打印 `是素数`，选 B。

对比一下输入 `6` 的情况：`a` 从 5 开始往下减，减到 3 时 `6 % 3 == 0`，打印“不是素数”并 `break`，`else` 被跳过。只有一路试到 `a` 变成 1 都没有整除，才会走到 `else`。

**需要注意：** 数学上 1 不是素数，但这段程序对 1 输出了“是素数”。原因是它只靠“没有找到因数”来判断素数，而 1 根本不会进入循环，漏掉了小于 2 的情况。严格的写法需要先判断 `num < 2`。

**易错点：** 容易以为循环一次都没执行就“没有输出”（选 C）。其实 `else` 只看循环是怎么结束的，与循环体是否执行过无关。

</div>

:::

::::

<h2 id="blank" class="quiz-group">填空题<span>11 QUESTIONS</span></h2>

:::: question blank-1 | 4-1 填空题

下面程序运行后，位于最后一行的最后一个数字是_____。

```python
for i in range(1,5):
    j=0
    while j<i:
       print(j,end=" ")
       j+=1
    print()
```

<div class="question-tags"><span class="question-tag">循环边界</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`3`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这是外层 `for` 套内层 `while` 的结构，要分清两个循环各自负责什么：

- 外层 `for i in range(1,5)`：`i` 取 1、2、3、4，每一轮输出**一行**。
- 内层 `while j<i`：每轮先把 `j` 重置为 0，只要 `j` 小于 `i` 就打印 `j` 并加 1，所以这一行会打印 `0` 到 `i-1`。
- 内层结束后的 `print()` 不带内容，作用是**换行**，让下一轮从新的一行开始。

逐行写出来：

| 外层 i | 内层 j 依次取值（满足 `j<i`） | 这一行的输出 |
| --- | --- | --- |
| 1 | 0 | `0` |
| 2 | 0、1 | `0 1` |
| 3 | 0、1、2 | `0 1 2` |
| 4 | 0、1、2、3 | `0 1 2 3` |

最后一行是 `0 1 2 3`，最后一个数字是 **3**。

**易错点：** 容易答成 4。`i` 的最大值是 4，但内层条件是 `j<i`，`j` 到 3 就停了，4 打印不出来。

</div>

:::

::::

:::: question blank-2 | 4-2 填空题

下面程序运行后，倒数第二行打印出_____。

```python
i=5
while i>=1:
    num=1
    for j in range(1,i+1):
        print(num,end="xxx")
        num*=2
    print()
    i-=1
```

<div class="question-tags"><span class="question-tag">格式化输出</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`1xxx2xxx`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先看三个关键点：

- 外层 `while i>=1`：`i` 从 5 开始，每轮结束 `i-=1`，所以 `i` 依次为 5、4、3、2、1，共输出 5 行。
- 内层 `for j in range(1,i+1)`：这一行要打印 `i` 个数。
- `print(num,end="xxx")`：`end` 指定打印完后接什么。默认接换行，这里改成接 `xxx`，所以同一行的内容连在一起，数字后面都跟着 `xxx`。内层结束后的 `print()` 才负责换行。

每一行开头 `num` 都重置为 1，打印一个数后乘 2，所以每行的数依次是 1、2、4、8、16……

逐行写出来：

| 外层 i | 这一行打印几个数 | 这一行的输出 |
| --- | --- | --- |
| 5 | 5 | `1xxx2xxx4xxx8xxx16xxx` |
| 4 | 4 | `1xxx2xxx4xxx8xxx` |
| 3 | 3 | `1xxx2xxx4xxx` |
| 2 | 2 | `1xxx2xxx` |
| 1 | 1 | `1xxx` |

共 5 行，**倒数第二行**是 `i = 2` 那一行，输出 `1xxx2xxx`。

**易错点：** 注意 `xxx` 是跟在每个数字的**后面**，包括最后一个数字，所以结尾是 `2xxx`，不是 `2`。另外，倒数第二行对应的是 `i = 2`，不是 `i = 4`，因为 `i` 是从大往小变的。

</div>

:::

::::

:::: question blank-3 | 4-3 填空题

下面程序运行后，最后一行有______个“G”。 _____

```python
i=1
while i<=5:
    num=1
    for j in range(1,i+1):
        print(num,end="G")
        num+=2
    print()
    i+=1
```

<div class="question-tags"><span class="question-tag">循环次数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`5`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先看三个关键点：

- 外层 `while i<=5`：`i` 从 1 开始，每轮结束 `i+=1`，所以 `i` 依次为 1、2、3、4、5，共输出 5 行。
- 内层 `for j in range(1,i+1)`：`j` 取 1 到 `i`，所以这一行**打印 `i` 个数**。
- `print(num,end="G")`：打印完数字后接一个 `G`（而不是换行）。**每打印一个数，就多一个 G**，所以一行里 G 的个数等于这一行打印的数的个数。内层结束后的 `print()` 负责换行。

每一行开头 `num` 重置为 1，打印一个数后加 2，所以每行的数依次是 1、3、5、7、9……

逐行写出来：

| 外层 i | 这一行打印几个数 | 这一行的输出 | G 的个数 |
| --- | --- | --- | --- |
| 1 | 1 | `1G` | 1 |
| 2 | 2 | `1G3G` | 2 |
| 3 | 3 | `1G3G5G` | 3 |
| 4 | 4 | `1G3G5G7G` | 4 |
| 5 | 5 | `1G3G5G7G9G` | 5 |

最后一行是 `i = 5` 那一行，输出 `1G3G5G7G9G`，共有 **5** 个 G。

**易错点：** 数的是**字母 G 的个数**，不是数字的大小。每个数字后面都跟一个 G，包括最后一个数字 9，所以 5 个数就有 5 个 G。

</div>

:::

::::

:::: question blank-4 | 4-4 填空题

下面程序运行后输出是_____。

```python
a = [1, 2, 3, 4, [5, 6], [7, 8, 9]]
s = 0
for row in a:
       if type(row)==list:
            for elem in row:
               s += elem
       else:
            s+=row
print(s)
```

<div class="question-tags"><span class="question-tag">嵌套列表</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`45`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先看列表 `a` 的结构：它一共有 **6 个元素**，前 4 个是整数 `1、2、3、4`，后 2 个是子列表 `[5,6]` 和 `[7,8,9]`。

外层 `for row in a` 每次取出一个元素，用 `type(row)==list` 判断它是不是列表：

- 是列表：再用内层 `for elem in row` 把里面的数逐个加到 `s`。
- 不是列表（即整数）：直接 `s+=row`。

逐步走一遍：

| 外层取到的 `row` | 是否列表 | 操作 | 操作后 `s` |
| --- | --- | --- | --- |
| 1 | 否 | `s+=1` | 1 |
| 2 | 否 | `s+=2` | 3 |
| 3 | 否 | `s+=3` | 6 |
| 4 | 否 | `s+=4` | 10 |
| `[5,6]` | 是 | 依次加 5、6 | 21 |
| `[7,8,9]` | 是 | 依次加 7、8、9 | 45 |

最后输出 `45`。

**快速验证：** 子列表被“展开”后，每个数恰好都加了一次，相当于 1 + 2 + …… + 9，用公式 9 × 10 ÷ 2 = 45 也能得到同一个结果。

</div>

:::

::::

:::: question blank-5 | 4-5 填空题

下面程序运行后输出是_____。

```python
l3=[i+j for i in range(1,6) for j in range(1,6)]
print(sum(l3))
```

<div class="question-tags"><span class="question-tag">列表推导式</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`150`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先把列表推导式还原成普通的嵌套循环，它等价于：

```python
l3 = []
for i in range(1, 6):
    for j in range(1, 6):
        l3.append(i + j)
```

也就是说，**`for` 从左到右依次对应嵌套循环从外到内**：左边的 `i` 是外层，右边的 `j` 是内层。`i` 取 1 到 5，`j` 也取 1 到 5，一共 5 × 5 = **25** 项，每项是 `i + j`。

前几项依次是：

| i | j 依次取 1~5 | 这 5 项的值 | 这 5 项的和 |
| --- | --- | --- | --- |
| 1 | 1、2、3、4、5 | 2、3、4、5、6 | 20 |
| 2 | 1、2、3、4、5 | 3、4、5、6、7 | 25 |
| 3 | 1、2、3、4、5 | 4、5、6、7、8 | 30 |
| 4 | 1、2、3、4、5 | 5、6、7、8、9 | 35 |
| 5 | 1、2、3、4、5 | 6、7、8、9、10 | 40 |

五行相加：20 + 25 + 30 + 35 + 40 = **150**。

**简便算法：** 总和可以拆成“所有 i 的和”加“所有 j 的和”。1 到 5 的和是 15，每个 `i` 出现 5 次，所以 `i` 部分是 5 × 15 = 75；`j` 同理也是 75。合计 75 + 75 = 150，与上面的结果一致。

</div>

:::

::::

:::: question blank-6 | 4-6 填空题

下面程序运行后输出是_____。

```python
l3=[[(i,j) for i in range(1,6)] for j in range(1,6)]
print(l3[2][1][0])
```

<div class="question-tags"><span class="question-tag">多层下标</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`2`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先还原这个列表推导式。外层 `for j in range(1,6)` 每取一个 `j` 生成**一行**，内层 `for i in range(1,6)` 生成这一行里的 5 个元组 `(i,j)`：

```python
l3 = []
for j in range(1, 6):
    row = []
    for i in range(1, 6):
        row.append((i, j))
    l3.append(row)
```

所以 `l3` 一共有 5 行，每行 5 个元组。每一行里 `j` 固定不变，`i` 从 1 变到 5：

| 行下标 | 对应的 j | 这一行的内容 |
| --- | --- | --- |
| 0 | 1 | `(1,1)`、`(2,1)`、`(3,1)`、`(4,1)`、`(5,1)` |
| 1 | 2 | `(1,2)`、`(2,2)`、`(3,2)`、`(4,2)`、`(5,2)` |
| 2 | 3 | `(1,3)`、`(2,3)`、`(3,3)`、`(4,3)`、`(5,3)` |
| 3 | 4 | `(1,4)`、……、`(5,4)` |
| 4 | 5 | `(1,5)`、……、`(5,5)` |

`l3[2][1][0]` 要从左到右一层一层取：

1. `l3[2]`：取下标 2 的那一行，也就是 `j = 3` 的一行。
2. `l3[2][1]`：再取这一行下标 1 的元素，是 `(2,3)`。
3. `l3[2][1][0]`：最后取元组下标 0 的项，也就是第一项 `2`。

所以输出 `2`。

**易错点：** 下标从 0 开始，`l3[2]` 是第 **3** 行，不是第 2 行。另外元组里是 `(i,j)`，第一项是 `i`，不是 `j`，所以最后得到的是 2，而不是 3。

</div>

:::

::::

:::: question blank-7 | 4-7 填空题

下面程序运行后，最后一行输出是_____。

```python
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
    print(a[0][2])
```

<div class="question-tags"><span class="question-tag">二维列表</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`0`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

先看程序在做什么：`a=[0]*n` 先得到一个只有 3 个元素的列表 `[0,0,0]`，每个元素都是整数 0。然后循环 3 轮，每轮把 `a[i]` 换成一个新的、含 4 个 0 的列表，最终 `a` 就成了 3 行 4 列的二维列表。

注意 `print(a[0][2])` **缩进在 `for` 循环里面**，所以每一轮都会打印一次，一共输出 3 行。题目问的是最后一行，也就是第 3 次打印的结果。

逐轮走一遍：

| 轮次 | `i` | 执行 `a[i]=[0]*m` 后的 `a` | `print(a[0][2])` 的输出 |
| --- | --- | --- | --- |
| 1 | 0 | `[[0,0,0,0], 0, 0]` | 0 |
| 2 | 1 | `[[0,0,0,0], [0,0,0,0], 0]` | 0 |
| 3 | 2 | `[[0,0,0,0], [0,0,0,0], [0,0,0,0]]` | 0 |

第 1 轮就把 `a[0]` 换成了 `[0,0,0,0]`，所以 `a[0][2]` 取的是这一行下标 2 的元素，值为 0。后两轮只修改 `a[1]` 和 `a[2]`，不影响 `a[0]`，每次打印的都是 0。

最后一行输出 `0`。

**易错点：** 每轮里先赋值再打印，所以第 1 轮打印时 `a[0]` 已经是列表了。如果顺序反过来，先打印 `a[0][2]`，此时 `a[0]` 还是整数 0，对整数取下标会报错。

</div>

:::

::::

:::: question blank-8 | 4-8 填空题

下面程序的输出是 _____ 。

```python
row=[0]*3
data=[row,row,row]
data[2][2]=7
print(data[0][2])
```

<div class="question-tags"><span class="question-tag">列表引用</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`7`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这题考的也是列表的“引用”（和 1-8 题原理相同）：列表是可变对象，放进另一个列表时，放进去的是它的“地址”，不是一份拷贝。

逐步看：

1. `row=[0]*3`：创建**一个**列表 `[0,0,0]`，变量 `row` 指向它。
2. `data=[row,row,row]`：`data` 的三个位置放的都是 `row` 这同一个列表的地址，并没有造出 3 个新列表。

```text
data[0] ─┐
data[1] ─┼─→ row：[0, 0, 0]
data[2] ─┘
```

3. `data[2][2]=7`：先取 `data[2]`，也就是 `row`，再把它下标 2 的元素改成 7，`row` 变成 `[0,0,7]`。
4. `print(data[0][2])`：`data[0]` 也是 `row`，它下标 2 的元素现在是 7，所以输出 `7`。

此时 `data` 打印出来是 `[[0,0,7],[0,0,7],[0,0,7]]`，三行同时变了。

**易错点：** 容易以为只改了第三行，`data[0][2]` 还是 0。只要几行指向的是同一个列表，改其中一行就等于改了所有行。

</div>

:::

::::

:::: question blank-9 | 4-9 填空题

下面程序的输出是 _____ 。

```python
data=[[0]*3] *3
data[2][2]=7
print(data[0][2])
```

<div class="question-tags"><span class="question-tag">列表重复</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`7`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这题和 1-8、4-8 的原理相同：用 `*` 重复列表时，复制的是元素的“地址”，不是元素本身。

分两步看 `data=[[0]*3] *3`：

1. 先算内层 `[0]*3`，得到**一个**新列表 `[0,0,0]`，记作行 A。
2. 再算外层 `[行A]*3`，只是把“行 A 的地址”重复了 3 份，并没有造出 3 个新列表。

```text
data[0] ─┐
data[1] ─┼─→ 行 A：[0, 0, 0]
data[2] ─┘
```

接着执行 `data[2][2]=7`：取出 `data[2]`（就是行 A），把它下标 2 的元素改成 7，行 A 变成 `[0,0,7]`。

`data[0]` 也指向行 A，所以 `data[0][2]` 读到的是 7，输出 `7`。此时整个 `data` 是 `[[0,0,7],[0,0,7],[0,0,7]]`。

**易错点：** 容易以为只改了第三行，`data[0][2]` 还是 0。`*` 对数字、字符串这类不可变对象没有问题，但对列表这类可变对象，重复出来的是同一个对象。要得到互相独立的行，应当用循环或推导式分别创建（见 4-10 题）。

</div>

:::

::::

:::: question blank-10 | 4-10 填空题

下面程序的输出是 _____ 。

```python
data=[]
for i in range(3):
    data.append([0]*3)
data[2][2]=7
print(data[0][2])
```

<div class="question-tags"><span class="question-tag">独立的列表行</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`0`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这题是 4-9 的“正确写法”对照：关键在于 `[0]*3` 写在**循环里面**，每一轮都会重新执行一次，每次都生成一个**全新的**列表。

逐轮走一遍：

| 轮次 | `i` | 本轮新建的列表 | 追加后的 `data` |
| --- | --- | --- | --- |
| 1 | 0 | 新列表 A：`[0,0,0]` | `[A]` |
| 2 | 1 | 新列表 B：`[0,0,0]` | `[A,B]` |
| 3 | 2 | 新列表 C：`[0,0,0]` | `[A,B,C]` |

A、B、C 虽然内容一样，但是**三个不同的列表**，各占各的位置：

```text
data[0] ─→ A：[0, 0, 0]
data[1] ─→ B：[0, 0, 0]
data[2] ─→ C：[0, 0, 0]
```

执行 `data[2][2]=7` 时，只修改列表 C，C 变成 `[0,0,7]`，A 和 B 不受影响。

`data[0]` 是 A，`print(data[0][2])` 读到的仍是 0，输出 `0`。

**对比 4-9：** 4-9 的 `[[0]*3]*3` 里 `[0]*3` 只执行了一次，三行是同一个列表；这里执行了三次，三行是三个列表。创建二维列表时，要让每一行都单独创建。

</div>

:::

::::

:::: question blank-11 | 4-11 填空题

下面程序的输出是 _____ 。

```python
mat=[[i*3+j+1 for j in range(3)] for i in range(5)]
mattrans=[[row[col] for row in mat] for col in range(3)]
print(mattrans[1][3])
```

<div class="question-tags"><span class="question-tag">矩阵转置</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

`11`

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**第一步：搞清楚 `mat` 长什么样。** 外层 `for i in range(5)` 生成 5 行，内层 `for j in range(3)` 让每行有 3 个数，每个数的值是 `i*3+j+1`：

| 行下标 i | 这一行的内容 |
| --- | --- |
| 0 | `[1, 2, 3]` |
| 1 | `[4, 5, 6]` |
| 2 | `[7, 8, 9]` |
| 3 | `[10, 11, 12]` |
| 4 | `[13, 14, 15]` |

所以 `mat` 是 **5 行 3 列**。

**第二步：转置是什么意思。** `mattrans=[[row[col] for row in mat] for col in range(3)]` 的意思是：外层 `col` 取 0、1、2，每个 `col` 生成新的一行，这一行由 `mat` 每一行的第 `col` 个数组成，也就是把原来的**一列**变成**一行**。

```text
mattrans[0] = [1, 4, 7, 10, 13]    ← mat 的第 0 列
mattrans[1] = [2, 5, 8, 11, 14]    ← mat 的第 1 列
mattrans[2] = [3, 6, 9, 12, 15]    ← mat 的第 2 列
```

转置后是 **3 行 5 列**。

**第三步：取值。** `mattrans[1][3]` 就是第 1 行（`[2, 5, 8, 11, 14]`）下标 3 的元素，也就是 `11`。

**快速算法：** 转置后行列下标互换，`mattrans[1][3]` 对应 `mat[3][1]`，即 `mat` 第 3 行 `[10, 11, 12]` 的下标 1，同样是 `11`。代入公式 `i*3+j+1` 也得到 3 × 3 + 1 + 1 = 11。

**易错点：** 注意 `mattrans` 只有 3 行，但每行有 5 个数，所以第二个下标 3 不会越界。如果误以为转置后还是 5 行 3 列，就会觉得 `[1][3]` 越界了。

</div>

:::

::::

<h2 id="programming" class="quiz-group">编程题<span>22 QUESTIONS</span></h2>

:::: question programming-1 | 7-1 生成输入数的乘方表

输入一个非负数和正整数n，3&lt;=n&lt;=9，生成一张输入数的乘方表。

#### 输入格式:

在一行输入一个非负数和正整数n。

#### 输出格式:

按照幂的递增顺序输出n+1行，计算结果保留2位小数。

#### 输入样例1:

```text
2.5 3
```

#### 输出样例1:

```text
2.5**0=1.00
2.5**1=2.50
2.5**2=6.25
2.5**3=15.62
```

#### 输入样例2:

```text
4 6
```

#### 输出样例2:

```text
4.0**0=1.00
4.0**1=4.00
4.0**2=16.00
4.0**3=64.00
4.0**4=256.00
4.0**5=1024.00
4.0**6=4096.00
```

<div class="question-tags"><span class="question-tag">幂运算</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
base, n = input().split()
base = float(base)
for power in range(int(n) + 1):
    print(f'{base}**{power}={base ** power:.2f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 读入底数和 n，让指数从 0 依次取到 n，每个指数输出一行。

**逐句解释代码：**

1. `base, n = input().split()`：`input()` 读入一整行，如 `"2.5 3"`，`split()` 按空格把它切成两段 `["2.5", "3"]`，分别赋给 `base` 和 `n`。此时两个变量还都是**字符串**。
2. `base = float(base)`：把底数转成浮点数。这样输入 `4` 时 `base` 是 `4.0`，输出里的底数就会按样例显示成 `4.0`。
3. `for power in range(int(n) + 1)`：`n` 还是字符串，要先用 `int` 转成整数。指数要取 0 到 n，共 n+1 个数，而 `range` 不包含终点，所以写 `n + 1`。
4. `print(f'{base}**{power}={base ** power:.2f}')`：f-string 中花括号里的内容会被替换成变量的值。
   - `{base}`、`{power}`：直接输出底数和指数，不做格式处理。
   - `{base ** power:.2f}`：先计算乘方，冒号后的 `.2f` 表示**保留 2 位小数**。

**用样例 1（输入 `2.5 3`）走一遍：**

| power | 输出 |
| --- | --- |
| 0 | `2.5**0=1.00` |
| 1 | `2.5**1=2.50` |
| 2 | `2.5**2=6.25` |
| 3 | `2.5**3=15.62` |

共 n+1 = 4 行，与样例一致。

**易错点：**

- 只有等号**右边**的结果要保留两位小数，左边的底数不能加 `.2f`，否则 `2.5` 会显示成 `2.50`，和样例不符。
- 15.625 输出成 `15.62` 而不是 `15.63`：15.625 恰好在 15.62 和 15.63 的正中间，Python 的 `.2f` 遇到这种情况会取**末位为偶数**的结果（2 是偶数），和手算的“四舍五入”不同。直接用上面的写法，输出就与样例一致，不需要自己处理。

</div>

:::

::::

:::: question programming-2 | 7-2 判断素数

判断一个给定的正整数是否素数

#### 输入格式:

输入在第一行给出一个正整数N（≤ 10），随后N行，每行给出一个小于1000000 的需要判断的正整数

#### 输出格式:

对每个需要判断的正整数，如果它是素数，则在一行中输出Yes，否则输出No

#### 输入样例:

在这里给出一组输入。例如：

```text
2
11
111
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
Yes
No
```

<div class="question-tags"><span class="question-tag">试除法</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
count = int(input())
for _ in range(count):
    n = int(input())
    prime = n >= 2
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            prime = False
            break
        divisor += 1
    print('Yes' if prime else 'No')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**素数的定义：** 只能被 1 和它自己整除、且大于 1 的整数。所以 0、1 都不是素数。

**思路：** 如果 `n` 不是素数，就一定能找到一个除了 1 和 n 以外的因数。逐个试除，只要有一个能整除，就说明不是素数。

**为什么只试到平方根：** 因数总是成对出现的，例如 36 = 2 × 18 = 3 × 12 = 4 × 9 = 6 × 6。每一对因数里，较小的那个一定不超过平方根（√36 = 6）。所以只要试到平方根还没找到因数，后面就不可能再找到了。代码里的 `divisor * divisor <= n` 就是“`divisor` 不超过 √n”的写法，这样避免了开方运算。

**逐句解释代码：**

1. `count = int(input())`：读入有几个数要判断。
2. `for _ in range(count)`：重复 `count` 次。`_` 表示这个循环变量后面用不到。
3. `prime = n >= 2`：先假设 `n` 是素数。如果 `n` 小于 2，一开始就是 `False`。
4. `divisor = 2`：从 2 开始试除。
5. `while divisor * divisor <= n`：只要 `divisor` 没超过平方根就继续。
6. 如果 `n % divisor == 0`（能整除），说明找到了因数，把 `prime` 改成 `False`，并用 `break` 立即退出，后面不用再试。
7. `print('Yes' if prime else 'No')`：`prime` 为真输出 `Yes`，否则输出 `No`。

**用样例走一遍：**

- `n = 11`：`divisor` 为 2 时 4 ≤ 11，11 % 2 = 1，不整除；为 3 时 9 ≤ 11，11 % 3 = 2，不整除；为 4 时 16 > 11，循环结束。`prime` 仍是 `True`，输出 `Yes`。
- `n = 111`：`divisor` 为 2 时 111 % 2 = 1，不整除；为 3 时 111 % 3 = 0，整除，`prime` 变 `False` 并 `break`，输出 `No`（111 = 3 × 37）。

**易错点：** 输入 1 时，`prime = n >= 2` 直接是 `False`，循环也不会执行，输出 `No`。如果漏掉这一句，1 会被误判成素数（参见 2-7 题）。

</div>

:::

::::

:::: question programming-3 | 7-3 猴子吃桃问题

一只猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半加一个。到第$N$天早上想再吃时，见只剩下一个桃子了。问：第一天共摘了多少个桃子？

#### 输入格式:

输入在一行中给出正整数$N$（$1<N\le 10$）。

#### 输出格式:

在一行中输出第一天共摘了多少个桃子。

#### 输入样例:

```text
3
```

#### 输出样例:

```text
10
```

<div class="question-tags"><span class="question-tag">逆向递推</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
peaches = 1
for _ in range(n - 1):
    peaches = (peaches + 1) * 2
print(peaches)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 题目告诉的是“最后一天剩几个”，要求的是“第一天有几个”，所以要**倒着推**：已知后一天的桃子数，求前一天的桃子数。

**怎么倒推：** 设某天早上有 x 个桃子，吃掉“一半加一个”，第二天剩下：

剩下 = x − (x/2 + 1) = x/2 − 1

也就是“第二天的数量 = 前一天的一半减一”。反过来：

前一天 = (第二天 + 1) × 2

这就是代码里 `peaches = (peaches + 1) * 2` 的来源：**先加一，再乘二**。

**逐句解释代码：**

1. `n = int(input())`：读入天数 N。
2. `peaches = 1`：第 N 天早上只剩 1 个桃子，从这里开始倒推。
3. `for _ in range(n - 1)`：从第 N 天倒推回第 1 天，需要推 N−1 次（例如第 3 天推回第 1 天，要推 2 次）。`_` 表示循环变量用不到。
4. 每次执行 `peaches = (peaches + 1) * 2`，得到前一天的数量。
5. 最后 `print(peaches)` 输出第一天的数量。

**用样例走一遍（输入 `3`，要推 2 次）：**

| 倒推次数 | 对应哪一天 | 计算 | 桃子数 |
| --- | --- | --- | --- |
| 开始 | 第 3 天早上 | 题目已知 | 1 |
| 第 1 次 | 第 2 天早上 | (1 + 1) × 2 | 4 |
| 第 2 次 | 第 1 天早上 | (4 + 1) × 2 | 10 |

输出 `10`，与样例一致。

**验证：** 第 1 天有 10 个，吃一半加一个，即 5 + 1 = 6 个，剩 4 个；第 2 天吃 2 + 1 = 3 个，剩 1 个，正好与第 3 天一致。

**易错点：** 循环次数是 N−1，不是 N。第 N 天的 1 个桃子是已知条件，不需要再推一次。

</div>

:::

::::

:::: question programming-4 | 7-4 求分数序列前N项和

本题要求编写程序，计算序列 2/1+3/2+5/3+8/5+... 的前N项之和。注意该序列从第2项起，每一项的分子是前一项分子与分母的和，分母是前一项的分子。

#### 输入格式:

输入在一行中给出一个正整数N。

#### 输出格式:

在一行中输出部分和的值，精确到小数点后两位。题目保证计算结果不超过双精度范围。

#### 输入样例:

```text
20
```

#### 输出样例:

```text
32.66
```

<div class="question-tags"><span class="question-tag">分数递推</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
top, bottom = 2, 1
total = 0
for _ in range(n):
    total += top / bottom
    top, bottom = top + bottom, top
print(f'{total:.2f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 每一项的分子、分母都由前一项推出来：新分子 = 旧分子 + 旧分母，新分母 = 旧分子。用两个变量 `top`（分子）和 `bottom`（分母）保存当前这一项，循环 N 次，每次先把当前项加进总和，再更新成下一项。

**先写出前几项：**

| 第几项 | 分子 top | 分母 bottom | 这一项的值 |
| --- | --- | --- | --- |
| 1 | 2 | 1 | 2/1 = 2.0 |
| 2 | 2+1 = 3 | 2 | 3/2 = 1.5 |
| 3 | 3+2 = 5 | 3 | 5/3 ≈ 1.667 |
| 4 | 5+3 = 8 | 5 | 8/5 = 1.6 |

与题目的 2/1、3/2、5/3、8/5 一致。

**逐句解释代码：**

1. `top, bottom = 2, 1`：第 1 项的分子和分母。
2. `total = 0`：总和从 0 开始。
3. `for _ in range(n)`：重复 N 次，每次处理一项。
4. `total += top / bottom`：把当前项加到总和里。
5. `top, bottom = top + bottom, top`：同时更新分子和分母。Python 会**先把右边两个值都算出来**，再一起赋给左边，所以右边用的都是旧的 `top` 和 `bottom`。
6. `print(f'{total:.2f}')`：输出总和，`.2f` 表示保留 2 位小数。

**易错点：** 更新不能拆成两行：

```python
top = top + bottom   # top 先变了
bottom = top         # 此时的 top 已经是新值，bottom 就错了
```

第二行用到的是已经改过的 `top`，得到的分母不是旧分子。用同时赋值的写法就不会出错。

另外要先加当前项、再更新，顺序反过来会漏掉第 1 项 2/1。

</div>

:::

::::

:::: question programming-5 | 7-5 运输打折问题

某运输公司对用户计算运费。路程（S）越远，每公里运费越低。标准如下：

![运输里程对应的折扣表](/images/problems/9fb0fa20ca7a.png)  
其中基本运输费用为每吨每公里1元，现请你帮助该运输公司设计自动计费程序，帮助会计人员计算运输费用。

#### 输入格式:

输入每次运输的载重（吨）、里程（公里）。

#### 输出格式:

输出其运输费用，精确到元。

#### 输入样例:

在这里给出一组输入。例如：

```text
1 200
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
200
```

#### 输入样例:

在这里给出一组输入。例如：

```text
10  2500
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
22500
```

<div class="question-tags"><span class="question-tag">分段计费</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
weight, distance = map(float, input().split())
if distance < 250:
    rate = 1
elif distance < 500:
    rate = 0.98
elif distance < 1000:
    rate = 0.95
elif distance < 2000:
    rate = 0.92
elif distance < 3000:
    rate = 0.90
else:
    rate = 0.85
print(f'{weight * distance * rate:.0f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 运费 = 载重 × 里程 × 折扣系数。里程越远折扣越大，所以先根据里程判断落在哪一档，得到系数 `rate`，最后一次算出运费。

**档位对应关系（来自题目的表格）：**

| 里程 distance | 系数 rate |
| --- | --- |
| 小于 250 | 1（无折扣） |
| 250 以上，小于 500 | 0.98 |
| 500 以上，小于 1000 | 0.95 |
| 1000 以上，小于 2000 | 0.92 |
| 2000 以上，小于 3000 | 0.90 |
| 3000 及以上 | 0.85 |

**为什么每个条件只写上界：** `if / elif` 从上到下依次判断，只要前一个条件成立，后面的就不再检查。所以走到 `elif distance < 500` 时，已经说明 `distance < 250` 不成立，即里程至少是 250，不用再写 `250 <= distance < 500`。边界值要看清：恰好 250 公里时 `distance < 250` 不成立，会落进第二档。

**逐句解释代码：**

1. `weight, distance = map(float, input().split())`：`input().split()` 把一行切成两段字符串，`map(float, ...)` 把每段转成浮点数，分别赋给载重和里程。
2. 一组 `if / elif / else` 判断档位，给 `rate` 赋值。
3. `print(f'{weight * distance * rate:.0f}')`：`.0f` 表示保留 0 位小数，即输出整数，符合“精确到元”。

**用样例走一遍：**

- 输入 `1 200`：200 < 250，`rate = 1`，运费 1 × 200 × 1 = 200，输出 `200`。
- 输入 `10 2500`：2500 不小于 250、500、1000、2000，但小于 3000，所以 `rate = 0.90`，运费 10 × 2500 × 0.90 = 22500，输出 `22500`。

**易错点：** 判断顺序不能打乱。如果把 `distance < 3000` 放到最前面，200 公里也会满足它，得到错误的折扣。

</div>

:::

::::

:::: question programming-6 | 7-6 最大公约数和最小公倍数

本题要求两个给定正整数的最大公约数和最小公倍数。

#### 输入格式:

输入在一行中给出两个正整数M和N（$\le 1000$）。

#### 输出格式:

在一行中顺序输出M和N的最大公约数和最小公倍数，两数字间以1空格分隔。

#### 输入样例:

```text
511 292
```

#### 输出样例:

```text
73 2044
```

**鸣谢安阳师范学院段晓云老师和软件工程五班李富龙同学补充测试数据！**

<div class="question-tags"><span class="question-tag">辗转相除法</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m, n = map(int, input().split())
a, b = m, n
while b != 0:
    a, b = b, a % b
print(a, m * n // a)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**两个概念：**

- 最大公约数：能同时整除两个数的最大整数。
- 最小公倍数：能同时被两个数整除的最小正整数。
- 两者的关系：**最小公倍数 = 两数乘积 ÷ 最大公约数**。所以只要求出最大公约数，最小公倍数就能算出来。

**辗转相除法：** 用大数除以小数，再用“除数”除以“余数”，如此重复，直到余数为 0，这时最后一个除数就是最大公约数。代码里用 `a, b = b, a % b` 完成每一步：`a` 变成原来的 `b`（除数），`b` 变成 `a % b`（余数）。右边两个值会先算好再同时赋值，所以不会互相干扰。

**逐句解释代码：**

1. `m, n = map(int, input().split())`：读入两个整数。
2. `a, b = m, n`：复制一份给 `a`、`b` 去做运算，**原来的 `m`、`n` 保留不动**，最后算最小公倍数还要用。
3. `while b != 0`：余数不为 0 就继续。
4. `a, b = b, a % b`：更新为“除数、余数”。
5. 循环结束时 `a` 就是最大公约数。
6. `print(a, m * n // a)`：输出最大公约数和最小公倍数。`//` 是整除，结果仍是整数。

**用样例走一遍（输入 `511 292`）：**

| 轮次 | 计算前的 a、b | 计算 `a % b` | 计算后的 a、b |
| --- | --- | --- | --- |
| 1 | 511、292 | 511 % 292 = 219 | 292、219 |
| 2 | 292、219 | 292 % 219 = 73 | 219、73 |
| 3 | 219、73 | 219 % 73 = 0 | 73、0 |

此时 `b` 为 0，循环结束，最大公约数是 `a = 73`。

最小公倍数 = 511 × 292 ÷ 73 = 149212 ÷ 73 = 2044。输出 `73 2044`，与样例一致。

**易错点：**

- 如果直接对 `m`、`n` 做辗转相除，循环结束后 `m * n` 就不是原来的乘积了，所以要另外用 `a`、`b`。
- 不用担心输入时第一个数比第二个小：例如 `a=292, b=511`，第一轮就会变成 `511、292`，自动交换过来。

</div>

:::

::::

:::: question programming-7 | 7-7 求满足条件的斐波那契数

斐波那契数，亦称之为斐波那契数列，指的是这样一个数列：1、1、2、3、5、8、13、21、……，这个数列从第3项开始，每一项都等于前两项之和。求大于输入数的最小斐波那契数。

#### 输入格式:

在一行输人一个正整数n(n>=10)。

#### 输出格式:

在一行输出大于n的最小斐波那契数。

#### 输入样例:

在这里给出一组输入。例如：

```text
10
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
13
```

<div class="question-tags"><span class="question-tag">斐波那契数列</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
a, b = 1, 1
while b <= n:
    a, b = b, a + b
print(b)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 从头开始依次生成斐波那契数，一直生成到某一项**大于** n 为止，这一项就是答案。

**逐句解释代码：**

1. `n = int(input())`：读入整数 n。
2. `a, b = 1, 1`：`a`、`b` 保存相邻的两项，一开始是第 1、2 项，都是 1。`b` 是当前最新的一项。
3. `while b <= n`：只要最新一项还没超过 n，就继续生成下一项。
4. `a, b = b, a + b`：向后滚动一步。新的 `a` 是旧的 `b`，新的 `b` 是旧的 `a + b`，也就是下一项。右边先算好再同时赋值，不会互相干扰。
5. 循环结束时 `b` 第一次大于 n，`print(b)` 输出它。

**用样例走一遍（输入 `10`）：**

| 轮次 | 判断前的 a、b | `b <= 10`？ | 更新后的 a、b |
| --- | --- | --- | --- |
| 1 | 1、1 | 是 | 1、2 |
| 2 | 1、2 | 是 | 2、3 |
| 3 | 2、3 | 是 | 3、5 |
| 4 | 3、5 | 是 | 5、8 |
| 5 | 5、8 | 是 | 8、13 |
| 6 | 8、13 | 否，循环结束 | — |

输出 `b = 13`，与样例一致。

**为什么条件要带等号：** 题目要的是“**大于** n 的最小斐波那契数”。如果 n 本身就是斐波那契数，比如输入 13，那么 13 不满足“大于 13”，要继续往后找。写成 `b <= n`，`b` 等于 13 时会继续循环，最终输出 21。如果写成 `b < n`，`b` 等于 13 时循环就停了，会错误地输出 13。

</div>

:::

::::

:::: question programming-8 | 7-8 求误差小于输入值的e的近似值

自然常数e可以用级数1+1/1!+1/2!+⋯+1/n!来近似计算。ei代表前i项求和。输入误差范围error,当  
ei+1-ei&lt;error,则表示e的近似值满足误差范围。

#### 输入格式:

在一行输入误差范围,误差至少小于等于0.01。

#### 输出格式:

在一行输出e的近似值（保留6位小数）。

#### 输入样例1:

在这里给出一组输入。例如：

```text
0.01
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
2.716667
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
0.000000001
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
2.718282
```

<div class="question-tags"><span class="question-tag">级数求和</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
error = float(input())
total = term = 1.0
n = 1
while True:
    term /= n
    total += term
    if term < error:
        break
    n += 1
print(f'{total:.6f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** e ≈ 1 + 1/1! + 1/2! + 1/3! + ……。每一项都能由前一项得到：

第 n 项 = 第 n−1 项 ÷ n（例如 1/3! = (1/2!) ÷ 3）

所以不用每次重新算阶乘，只要用变量 `term` 保存当前项，每轮除以 n 就得到下一项。

题目说“相邻两次部分和的差小于误差”就停止。相邻部分和的差，正好就是**新加入的这一项**，所以判断条件就是 `term < error`。

**逐句解释代码：**

1. `error = float(input())`：读入误差。
2. `total = term = 1.0`：`total` 是部分和，`term` 是当前项。一开始只有第 0 项 1，所以两者都是 1.0。
3. `n = 1`：下一项是第 1 项（1/1!）。
4. `while True`：一直循环，直到遇到 `break`。
5. `term /= n`：算出新的一项。
6. `total += term`：先把新项加进总和。
7. `if term < error: break`：新项已经小于误差就退出。
8. `n += 1`：准备下一项。
9. `print(f'{total:.6f}')`：保留 6 位小数输出。

**用样例 1 走一遍（误差 `0.01`）：**

| n | term | total | term < 0.01？ |
| --- | --- | --- | --- |
| 1 | 1/1! = 1 | 2 | 否 |
| 2 | 1/2! = 0.5 | 2.5 | 否 |
| 3 | 1/3! ≈ 0.1667 | 2.6667 | 否 |
| 4 | 1/4! ≈ 0.04167 | 2.70833 | 否 |
| 5 | 1/5! ≈ 0.008333 | 2.716667 | 是，停止 |

输出 `2.716667`，与样例一致。

**易错点：** 要**先加**这一项，**再判断**是否停止，最后那个小于误差的项也在总和里。如果先判断再加，结果会少一项，得到 2.708333，与样例不符。

</div>

:::

::::

:::: question programming-9 | 7-9 求π的近似值

用公式求$\pi$的近似值：$\pi^{2}$/6=1+1/$2^{2}$+1/$3^{2}$+1/$4^{2}$+。。。  
当求和项小于误差时,结束求和。

#### 输入格式:

在一行输入误差范围

#### 输出格式:

在一行输出$\pi$的近似值（保留6位小数）。

#### 输入样例:

在这里给出一组输入。例如：

```text
0.00000001
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
3.141497
```

<div class="question-tags"><span class="question-tag">级数求和</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
import math

error = float(input())
n = 1
total = 0
while 1 / (n * n) >= error:
    total += 1 / (n * n)
    n += 1
print(f'{math.sqrt(6 * total):.6f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 公式是 π²/6 = 1 + 1/2² + 1/3² + 1/4² + ……，右边第 n 项是 1/n²。

1. 先用循环算出右边的和，记作 `total`。
2. 公式左边是 π²/6，所以 π² ≈ 6 × `total`，π ≈ √(6 × `total`)。

**逐句解释代码：**

1. `import math`：导入数学模块，后面要用 `math.sqrt` 开平方。
2. `error = float(input())`：读入误差。
3. `n = 1`、`total = 0`：从第 1 项开始，总和从 0 开始。
4. `while 1 / (n * n) >= error`：只要当前项不小于误差，就继续累加。
5. `total += 1 / (n * n)`：把当前项加进总和。
6. `n += 1`：换到下一项。
7. `print(f'{math.sqrt(6 * total):.6f}')`：先乘 6，再开平方，保留 6 位小数。

**用一个小例子走一遍（假设误差为 `0.1`）：**

| n | 当前项 1/n² | 是否 ≥ 0.1 | 操作 |
| --- | --- | --- | --- |
| 1 | 1 | 是 | 加入，total = 1 |
| 2 | 0.25 | 是 | 加入，total = 1.25 |
| 3 | 约 0.1111 | 是 | 加入，total ≈ 1.3611 |
| 4 | 0.0625 | 否 | 停止，**这一项不加** |

此时 π ≈ √(6 × 1.3611) ≈ 2.8577。误差设得越小，加的项越多，结果越接近 3.14159。

**和 7-8 的区别：** 7-8 是先把新的一项加进总和，再判断是否小于误差，所以停止的那一项**加了**。这一题的条件写在 `while` 里，先判断、再累加，停止的那一项**没有加**。题目样例 `3.141497` 是按这种写法得到的。

**易错点：** 最后别忘了乘 6 再开平方。直接输出 `total` 得到的是 π²/6，约 1.64，不是 π。

</div>

:::

::::

:::: question programming-10 | 7-10 水仙花数（20 分）

水仙花数是指一个N位正整数（N≥3），它的每个位上的数字的N次幂之和等于它本身。  
例如：153=1×1×1+5×5×5+3×3×3。

本题要求编写程序,计算所有N位水仙花数。

#### 输入格式:

输入在一行中给出一个正整数N（3≤N≤5）

#### 输出格式:

按递增顺序输出所有N位水仙花数，每个数字占一行。

#### 输入样例:

在这里给出一组输入。例如：

```text
3
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
153
370
371
407
```

<div class="question-tags"><span class="question-tag">枚举</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
for number in range(10 ** (n - 1), 10 ** n):
    total = 0
    for digit in str(number):
        total += int(digit) ** n
    if total == number:
        print(number)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 把所有 N 位数逐个检查一遍（这种方法叫“枚举”）：对每个数，求出各位数字的 N 次方之和，如果等于它本身，就是水仙花数。

**N 位数的范围：** N 位数的最小值是 10 的 N−1 次方，最大值比 10 的 N 次方小 1。

| N | 最小的 N 位数 | 最大的 N 位数 | 对应的 range |
| --- | --- | --- | --- |
| 3 | 100 | 999 | `range(100, 1000)` |
| 4 | 1000 | 9999 | `range(1000, 10000)` |
| 5 | 10000 | 99999 | `range(10000, 100000)` |

`range` 不包含终点，所以终点正好写 `10 ** n`，起点写 `10 ** (n - 1)`。

**逐句解释代码：**

1. `n = int(input())`：读入位数 N。
2. `for number in range(10 ** (n - 1), 10 ** n)`：依次取出每个 N 位数。
3. `total = 0`：每检查一个数，总和都要重新从 0 开始。
4. `for digit in str(number)`：`str(number)` 把数字转成字符串，例如 `153` 变成 `"153"`，遍历时依次得到字符 `"1"`、`"5"`、`"3"`。
5. `total += int(digit) ** n`：`int(digit)` 把字符转回整数，再算 N 次方并累加。
6. `if total == number: print(number)`：相等就输出。

**用 153 走一遍（N = 3）：**

| digit | int(digit) | 它的 3 次方 | total |
| --- | --- | --- | --- |
| `"1"` | 1 | 1 | 1 |
| `"5"` | 5 | 125 | 126 |
| `"3"` | 3 | 27 | 153 |

`total` 等于 153，所以输出 153。再看 154：1 + 125 + 64 = 190，不等于 154，不输出。

**易错点：** `total = 0` 必须写在外层循环里面、内层循环前面。如果写在整个程序最前面，上一个数的和会带到下一个数，结果就全错了。

</div>

:::

::::

:::: question programming-11 | 7-11 找出不是公共的元素

给定两行输入，每行代表一组元素。每行的元素间用空格分开。求两组中非公共的元素。

#### 输入格式:

输入分别在两行中给出两组元素，每行每个元素只出现一次。

#### 输出格式:

在一行中按照元素的输入顺序输出不是两组共有的元素，以空格分隔，题目保证至少存在一个这样的元素。

#### 输入样例:

在这里给出一组输入。例如：

```text
10 3 -5 2 8 0 5 -15 9 100
10 6 4 8 2 -5 9 0 100 1
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
3 5 -15 6 4 1
```

<div class="question-tags"><span class="question-tag">成员判断</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
first = input().split()
second = input().split()
result = []
for value in first:
    if value not in second:
        result.append(value)
for value in second:
    if value not in first:
        result.append(value)
print(*result)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 要找“只出现在一组里”的元素，并且按输入顺序输出。做法是遍历两次：

1. 遍历第一组，把**不在第二组里**的元素放进结果。
2. 遍历第二组，把**不在第一组里**的元素放进结果。

两组共有的元素，在两次遍历里都会被跳过。

**逐句解释代码：**

1. `first = input().split()`：读入第一行，按空格切成一个字符串列表，例如 `"10 3 -5"` 变成 `["10", "3", "-5"]`。第二行同理。
2. `result = []`：准备一个空列表，存放结果。
3. `if value not in second`：`in` 判断元素是否在列表里，`not in` 就是不在。
4. `result.append(value)`：把元素追加到结果末尾。
5. `print(*result)`：`*` 把列表拆开，各元素之间用空格隔开输出，行末没有多余空格。

**用样例走一遍：**

- 第一组：`10 3 -5 2 8 0 5 -15 9 100`
- 第二组：`10 6 4 8 2 -5 9 0 100 1`

| 遍历 | 不在对方组里的元素 |
| --- | --- |
| 第一组 | 3、5、-15 |
| 第二组 | 6、4、1 |

依次放进结果，输出 `3 5 -15 6 4 1`，与样例一致。

**说明：** 这里的元素一直是字符串，没有转成整数。因为题目只要求判断“是否相同”并原样输出，不需要计算，所以不用转换。

</div>

:::

::::

:::: question programming-12 | 7-12 找完数

所谓完数就是该数恰好等于除自身外的因子之和。例如：6=1+2+3，其中1、2、3为6的因子。本题要求编写程序，找出任意两正整数$m$和$n$之间的所有完数。

#### 输入格式：

输入在一行中给出2个正整数$m$和$n$（$1<m\le n \le 10000$），中间以空格分隔。

#### 输出格式：

逐行输出给定范围内每个完数的因子累加形式的分解式，每个完数占一行，格式为“完数 = 因子1 + 因子2 + ... + 因子k”，其中完数和因子均按递增顺序给出。若区间内没有完数，则输出“None”。

#### 输入样例：

```text
2 30
```

#### 输出样例：

```text
6 = 1 + 2 + 3
28 = 1 + 2 + 4 + 7 + 14
```

<div class="question-tags"><span class="question-tag">因子枚举</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m, n = map(int, input().split())
found = False
for number in range(m, n + 1):
    factors = [1]
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            other = number // divisor
            if other != divisor:
                factors.append(other)
        divisor += 1
    if sum(factors) == number:
        found = True
        factors.sort()
        print(number, '=', ' + '.join(map(str, factors)))
if not found:
    print('None')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**完数的定义：** 一个数恰好等于它的所有因子（不含自己）之和。例如 6 的因子是 1、2、3，1 + 2 + 3 = 6，所以 6 是完数。

**思路：** 对区间内每个数，找出它的全部因子（不含自己），求和后与它本身比较。

**怎么高效地找因子：** 因子总是成对出现的。例如 28 = 2 × 14 = 4 × 7，找到小因子 2 的同时，就得到了大因子 14。所以只要试除到平方根，每次整除时把**除数和商**一起收集，就不用再试到 28 本身。

**逐句解释代码：**

1. `m, n = map(int, input().split())`：读入区间两端。
2. `found = False`：记录区间里有没有找到完数，最后决定要不要输出 `None`。
3. `for number in range(m, n + 1)`：依次检查区间内每个数，`n + 1` 是为了包含 n。
4. `factors = [1]`：1 是任何数的因子，先放进去。
5. `divisor = 2`，`while divisor * divisor <= number`：从 2 试到平方根。
6. `if number % divisor == 0`：整除，说明 `divisor` 是因子，追加它；`other = number // divisor` 是配对的大因子。
7. `if other != divisor`：完全平方数（如 36 = 6 × 6）两个因子相同，只记一次，避免重复。
8. `if sum(factors) == number`：因子之和等于它本身，就是完数。`factors.sort()` 把因子从小到大排序后，用 `' + '.join(map(str, factors))` 拼成“1 + 2 + 3”的形式输出。
9. `if not found: print('None')`：整个区间都没有完数才输出 `None`。

**用 28 走一遍：**

| divisor | divisor² ≤ 28？ | 28 % divisor | 收集后的 factors |
| --- | --- | --- | --- |
| 2 | 4 ≤ 28 | 0，整除，商 14 | `[1, 2, 14]` |
| 3 | 9 ≤ 28 | 1，不整除 | `[1, 2, 14]` |
| 4 | 16 ≤ 28 | 0，整除，商 7 | `[1, 2, 14, 4, 7]` |
| 5 | 25 ≤ 28 | 3，不整除 | `[1, 2, 14, 4, 7]` |
| 6 | 36 > 28 | 循环结束 | `[1, 2, 14, 4, 7]` |

因子之和 1 + 2 + 14 + 4 + 7 = 28，等于它本身，排序后输出 `28 = 1 + 2 + 4 + 7 + 14`。

**易错点：**

- 收集时大小因子是交替加入的，顺序是乱的，所以输出前一定要 `sort()`。
- 输入范围要求 m > 1，因此不用处理 1。如果区间里有 1，`factors=[1]` 的和等于 1，会把 1 误判成完数。

</div>

:::

::::

:::: question programming-13 | 7-13 猴子选大王

一群猴子要选新猴王。新猴王的选择方法是：让N只候选猴子围成一圈，从某位置起顺序编号为1~N号。从第1号开始报数，每轮从1报到3，凡报到3的猴子即退出圈子，接着又从紧邻的下一只猴子开始同样的报数。如此不断循环，最后剩下的一只猴子就选为猴王。请问是原来第几号猴子当选猴王？

#### 输入格式：

输入在一行中给一个正整数N（$\le$1000）。

#### 输出格式：

在一行中输出当选猴王的编号。

#### 输入样例：

```text
11
```

#### 输出样例：

```text
7
```

<div class="question-tags"><span class="question-tag">循环报数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
monkeys = list(range(1, n + 1))
index = 0
while len(monkeys) > 1:
    index = (index + 2) % len(monkeys)
    monkeys.pop(index)
print(monkeys[0])
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 把猴子的编号放进列表，每次找出报到 3 的那只猴子，把它从列表里删掉，直到只剩一只。

**关键点：**

- `index` 表示**当前这一轮报 1 的猴子**在列表中的下标。
- 从报 1 的位置数起，报到 3 的猴子在往后第 2 个位置，所以 `index + 2`。
- 圈是首尾相连的，数到列表末尾要绕回开头，用 `% len(monkeys)` 取余实现。
- 用 `pop(index)` 删除后，后面的猴子整体左移一位，下一只猴子正好落在 `index` 这个位置，它就是下一轮报 1 的猴子，所以 `index` 不用再改。

**逐句解释代码：**

1. `monkeys = list(range(1, n + 1))`：生成编号 1 到 n 的列表。
2. `index = 0`：第一轮从第 1 只（下标 0）开始报 1。
3. `while len(monkeys) > 1`：还剩多于一只就继续。
4. `index = (index + 2) % len(monkeys)`：算出报到 3 的猴子的下标。
5. `monkeys.pop(index)`：把它删除。
6. `print(monkeys[0])`：输出最后剩下的编号。

**用较小的例子走一遍（N = 5）：**

| 轮次 | 删除前的列表 | 计算 index | 被淘汰的编号 | 删除后的列表 |
| --- | --- | --- | --- | --- |
| 1 | `[1,2,3,4,5]` | (0+2) % 5 = 2 | 3 | `[1,2,4,5]` |
| 2 | `[1,2,4,5]` | (2+2) % 4 = 0 | 1 | `[2,4,5]` |
| 3 | `[2,4,5]` | (0+2) % 3 = 2 | 5 | `[2,4]` |
| 4 | `[2,4]` | (2+2) % 2 = 0 | 2 | `[4]` |

只剩 4，输出 `4`。

**易错点：** 每轮要用**当前**列表的长度取余，因为列表每轮都会变短。如果用原来的 n，下标会越界。

</div>

:::

::::

:::: question programming-14 | 7-14 特定矩阵元素和

给定一个n×n的方阵，本题要求计算该矩阵主、副对角线上的所有元素之和。主对角线为从矩阵的左上角至右下角的连线,副对角线为从矩阵的右上角至左下角的连线。。

#### 输入格式:

输入第一行给出正整数n（1&lt;n≤10）；随后n行，每行给出n个数，其间以空格分隔。

#### 输出格式:

在一行中给出该矩阵主、副对角线的所有元素之和,保留两位小数。

#### 输入样例1:

在这里给出一组输入。例如：

```text
4
2 3 4 1
5 6 1 1
7 1 8 1
1 1 1 1
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
21.00
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
3
1 2 3
4 5 6
7 8 9
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
25.00
```

<div class="question-tags"><span class="question-tag">对角线</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
total = 0
for i in range(n):
    row = list(map(float, input().split()))
    total += row[i]
    if i != n - 1 - i:
        total += row[n - 1 - i]
print(f'{total:.2f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 方阵的行和列下标都从 0 开始。对第 i 行来说，主对角线和副对角线各经过这一行的一个位置：

- 主对角线（左上到右下）：第 i 行的第 **i** 列。
- 副对角线（右上到左下）：第 i 行的第 **n−1−i** 列。

以 3 阶矩阵为例：

| 行 i | 主对角线列号 i | 副对角线列号 n−1−i |
| --- | --- | --- |
| 0 | 0 | 2 |
| 1 | 1 | 1 |
| 2 | 2 | 0 |

**注意中心元素：** n 为奇数时，中间那一行的两个列号相同（这里第 1 行都是第 1 列），是**同一个元素**，只能加一次。

**逐句解释代码：**

1. `n = int(input())`：读入阶数。
2. `total = 0`：总和从 0 开始。
3. `for i in range(n)`：每轮读入并处理一行，i 同时是行号。
4. `row = list(map(float, input().split()))`：把这一行的 n 个数转成浮点数列表。
5. `total += row[i]`：加上主对角线元素。
6. `if i != n - 1 - i`：两个列号不同，才加副对角线元素 `row[n - 1 - i]`；相同就是中心元素，已经加过了。
7. `print(f'{total:.2f}')`：保留 2 位小数输出。

**用样例 2 走一遍（3 阶）：**

| 行 i | 这一行 | 加主对角线 | 加副对角线 | total |
| --- | --- | --- | --- | --- |
| 0 | 1 2 3 | +1 | +3 | 4 |
| 1 | 4 5 6 | +5 | 不加（中心） | 9 |
| 2 | 7 8 9 | +9 | +7 | 25 |

输出 `25.00`，与样例一致。

**易错点：** 漏掉 `i != n - 1 - i` 的判断，中心元素 5 会被加两次，结果变成 30。

</div>

:::

::::

:::: question programming-15 | 7-15 矩阵行、列、对角线和的最大值

求一个`3*3`矩阵每行、每列及对角线和的最大值。

#### 输入格式:

在一行输入9个整数。

#### 输出格式:

在一行输出每行、每列及对角线和的最大值。

#### 输入样例:

在这里给出一组输入。例如：

```text
3 6 5 9 8 2 1 4 5
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
19
```

<div class="question-tags"><span class="question-tag">矩阵求和</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
values = list(map(int, input().split()))
matrix = [values[0:3], values[3:6], values[6:9]]
sums = []
for i in range(3):
    sums.append(sum(matrix[i]))
    sums.append(matrix[0][i] + matrix[1][i] + matrix[2][i])
sums.append(matrix[0][0] + matrix[1][1] + matrix[2][2])
sums.append(matrix[0][2] + matrix[1][1] + matrix[2][0])
print(max(sums))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 3×3 矩阵一共有 3 行、3 列、2 条对角线，共 **8 个和**。把它们全部算出来放进列表，再取最大值。

**逐句解释代码：**

1. `values = list(map(int, input().split()))`：一行输入的 9 个数转成整数列表。
2. `matrix = [values[0:3], values[3:6], values[6:9]]`：切片 `values[0:3]` 取下标 0、1、2 的三个数，不含 3。三段切片依次是第 1、2、3 行，这样 9 个数就变成了 3 行 3 列。
3. `sums = []`：准备存放 8 个和。
4. `for i in range(3)`：每轮算两个和。
   - `sum(matrix[i])`：第 i 行的和。
   - `matrix[0][i] + matrix[1][i] + matrix[2][i]`：第 i 列的和，列固定，行下标 0、1、2 依次取。
5. 主对角线 `matrix[0][0] + matrix[1][1] + matrix[2][2]`，副对角线 `matrix[0][2] + matrix[1][1] + matrix[2][0]`。
6. `print(max(sums))`：输出 8 个和里最大的。

**用样例走一遍（输入 `3 6 5 9 8 2 1 4 5`）：**

矩阵为：

```text
3 6 5
9 8 2
1 4 5
```

| 类型 | 计算 | 和 |
| --- | --- | --- |
| 第 1 行 | 3+6+5 | 14 |
| 第 2 行 | 9+8+2 | 19 |
| 第 3 行 | 1+4+5 | 10 |
| 第 1 列 | 3+9+1 | 13 |
| 第 2 列 | 6+8+4 | 18 |
| 第 3 列 | 5+2+5 | 12 |
| 主对角线 | 3+8+5 | 16 |
| 副对角线 | 5+8+1 | 14 |

最大值是 19，输出 `19`，与样例一致。

**易错点：** `sums` 不要用 0 作初始最大值再比较。如果所有数都是负数，和也都是负的，初始值 0 会比它们都大，得到错误结果。先收集全部和再取 `max` 就没有这个问题。

</div>

:::

::::

:::: question programming-16 | 7-16 判断三角矩阵

本题要求编写程序，判断一个给定的方阵是否是三角矩阵。三角矩阵包含上三角矩阵和下三角矩阵两种。

上三角矩阵指主对角线以下的元素都为0的矩阵；下三角矩阵指主对角线以上的元素都为0的矩阵；主对角线为从矩阵的左上角至右下角的连线。

输入矩阵是三种情况之一(上三角矩阵、下三角矩阵或都不是)。

#### 输入格式:

输入第一行给出一个正整数T，为待测矩阵的个数。接下来给出T个矩阵的信息：每个矩阵信息的第一行给出一个不超过10的正整数n。随后n行，每行给出n个整数，其间以空格分隔。

#### 输出格式:

每个矩阵的判断结果占一行。如果输入的矩阵是上三角矩阵，输出“upper triangular matrix”，如果输入的矩阵是下三角矩阵，输出“lower triangular matrix”，都不是输出“no”。

#### 输入样例:

在这里给出一组输入。例如：

```text
3
3
1 2 3
0 4 5
0 0 6
2
1 0
-8 2
4
1 2 4 0
56 5 7 9
3 4 8 9
0 0 0 0
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
upper triangular matrix
lower triangular matrix
no
```

<div class="question-tags"><span class="question-tag">三角矩阵</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
count = int(input())
for _ in range(count):
    n = int(input())
    upper = lower = True
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if i > j and row[j] != 0:
                upper = False
            if i < j and row[j] != 0:
                lower = False
    if upper:
        print('upper triangular matrix')
    elif lower:
        print('lower triangular matrix')
    else:
        print('no')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**两个概念：**

- 上三角矩阵：主对角线**以下**的元素全是 0。
- 下三角矩阵：主对角线**以上**的元素全是 0。

**怎么用下标区分区域：** 行号用 `i`，列号用 `j`，都从 0 开始。

| 条件 | 位置 | 说明 |
| --- | --- | --- |
| `i > j` | 主对角线下方 | 行号大于列号 |
| `i < j` | 主对角线上方 | 列号大于行号 |
| `i == j` | 主对角线上 | 不做要求 |

**思路：** 用两个标记 `upper`、`lower`，一开始都假设成立（`True`）。逐个检查元素：

- 下方（`i > j`）出现非 0，说明不是上三角，`upper = False`。
- 上方（`i < j`）出现非 0，说明不是下三角，`lower = False`。

检查完整个矩阵后，先看 `upper`，再看 `lower`，都不成立输出 `no`。

**逐句解释代码：**

1. `count = int(input())`：读入矩阵个数。
2. `for _ in range(count)`：每轮处理一个矩阵。
3. `n = int(input())`：读入这个矩阵的阶数。
4. `upper = lower = True`：每个矩阵开始前都要重新设成 `True`。
5. 外层 `for i in range(n)` 每轮读入一行，内层 `for j in range(n)` 检查这一行的每个元素。
6. 检查完后用 `if / elif / else` 输出结果。

**用样例走一遍：**

| 矩阵 | 下方是否有非 0 | 上方是否有非 0 | upper | lower | 输出 |
| --- | --- | --- | --- | --- | --- |
| `1 2 3 / 0 4 5 / 0 0 6` | 无 | 有（2、3、5） | True | False | `upper triangular matrix` |
| `1 0 / -8 2` | 有（-8） | 无 | False | True | `lower triangular matrix` |
| 4 阶那个 | 有 | 有 | False | False | `no` |

**易错点：**

- 必须把当前矩阵的每一行都读完再输出。如果提前结束，没读完的行会被当成下一个矩阵的输入，数据就错位了。
- 全是 0 的矩阵（或只有对角线非 0 的矩阵）上下三角都成立，代码先判断 `upper`，所以输出 `upper triangular matrix`。

</div>

:::

::::

:::: question programming-17 | 7-17 打印九九口诀表

下面是一个完整的下三角九九口诀表：

```text
1*1=1   
1*2=2   2*2=4   
1*3=3   2*3=6   3*3=9   
1*4=4   2*4=8   3*4=12  4*4=16  
1*5=5   2*5=10  3*5=15  4*5=20  5*5=25  
1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36  
1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49  
1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64  
1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81  
```

本题要求对任意给定的一位正整数`N`，输出从`1*1`到`N*N`的部分口诀表。

#### 输入格式：

输入在一行中给出一个正整数`N`（1$\le$`N`$\le$9）。

#### 输出格式：

输出下三角`N*N`部分口诀表，其中等号右边数字占4位、左对齐。

#### 输入样例：

```text
4
```

#### 输出样例：

```text
1*1=1   
1*2=2   2*2=4   
1*3=3   2*3=6   3*3=9   
1*4=4   2*4=8   3*4=12  4*4=16  
```

<div class="question-tags"><span class="question-tag">嵌套循环</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f'{j}*{i}={j * i:<4}', end='')
    print()
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 口诀表是下三角形：第 i 行有 i 个算式，每个算式是 `j*i=乘积`，其中 j 从 1 取到 i。外层循环控制行，内层循环控制一行里的算式，一行打印完再换行。

**逐句解释代码：**

1. `n = int(input())`：读入 N。
2. `for i in range(1, n + 1)`：i 取 1 到 N，每轮输出一行。
3. `for j in range(1, i + 1)`：j 取 1 到 i，所以第 i 行恰好有 i 个算式。
4. `print(f'{j}*{i}={j * i:<4}', end='')`：
   - `{j}*{i}=`：直接输出算式的左半部分。
   - `{j * i:<4}`：先算乘积，冒号后的 `<4` 表示**左对齐、总共占 4 个字符**，不足 4 个字符的部分用空格补在右边。
   - `end=''`：打印后不换行，让同一行的算式连在一起。
5. 内层结束后的 `print()`：只负责换行。

**`:<4` 的效果：**

| 乘积 | 输出（`□` 代表空格） | 补了几个空格 |
| --- | --- | --- |
| 6 | `6□□□` | 3 |
| 12 | `12□□` | 2 |

所以每个算式都占相同宽度，各列能对齐，行末也会留下空格，这和样例是一致的。

**用 N = 3 走一遍：**

| i | j 依次取值 | 这一行的输出 |
| --- | --- | --- |
| 1 | 1 | `1*1=1□□□` |
| 2 | 1、2 | `1*2=2□□□2*2=4□□□` |
| 3 | 1、2、3 | `1*3=3□□□2*3=6□□□3*3=9□□□` |

**易错点：**

- 算式写的是 `j*i`（小数在前），不是 `i*j`。第 2 行是 `1*2`、`2*2`，不是 `2*1`。
- `print()` 要缩进在外层循环里、内层循环外面。缩进到内层里面，每个算式后都会换行。

</div>

:::

::::

:::: question programming-18 | 7-18 求矩阵的局部极大值

给定$M$行$N$列的整数矩阵$A$，如果$A$的非边界元素$A[i][j]$大于相邻的上下左右4个元素，那么就称元素$A[i][j]$是矩阵的局部极大值。本题要求给定矩阵的全部局部极大值及其所在的位置。

#### 输入格式：

输入在第一行中给出矩阵$A$的行数$M$和列数$N$（$3\le M, N\le 20$）；最后$M$行，每行给出$A$在该行的$N$个元素的值。数字间以空格分隔。

#### 输出格式：

每行按照“元素值 行号 列号”的格式输出一个局部极大值，其中行、列编号从1开始。要求按照行号递增输出；若同行有超过1个局部极大值，则该行按列号递增输出。若没有局部极大值，则输出“None 总行数 总列数”。

#### 输入样例1：

```text
4 5
1 1 1 1 1
1 3 9 3 1
1 5 3 5 1
1 1 1 1 1
```

#### 输出样例1：

```text
9 2 3
5 3 2
5 3 4
```

#### 输入样例2：

```text
3 5
1 1 1 1 1
9 3 9 9 1
1 5 3 5 1
```

#### 输出样例2：

```text
None 3 5
```

<div class="question-tags"><span class="question-tag">相邻元素</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m, n = map(int, input().split())
matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().split())))
found = False
for i in range(1, m - 1):
    for j in range(1, n - 1):
        value = matrix[i][j]
        if value > max(matrix[i-1][j], matrix[i+1][j],
                       matrix[i][j-1], matrix[i][j+1]):
            print(value, i + 1, j + 1)
            found = True
if not found:
    print('None', m, n)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 局部极大值只可能出现在**非边界**位置，因为边界元素没有完整的上下左右四个邻居。所以只检查中间的元素，每个元素和它的上、下、左、右四个邻居比较，比四个都大才输出。

**为什么范围是 `range(1, m - 1)`：** 行下标 0 到 m−1。第一行（下标 0）和最后一行（下标 m−1）是边界，要排除，所以行从 1 取到 m−2；因为 `range` 不含终点，写成 `range(1, m - 1)`。列同理，写成 `range(1, n - 1)`。

**逐句解释代码：**

1. `m, n = map(int, input().split())`：读入行数和列数。
2. `for _ in range(m): matrix.append(list(map(int, input().split())))`：读入 m 行，每行转成整数列表，组成二维列表。
3. `found = False`：记录有没有找到局部极大值。
4. 双重循环遍历所有非边界位置，`value = matrix[i][j]`。
5. `max(上, 下, 左, 右)` 取四个邻居中最大的，`value >` 它，就说明比四个邻居都**严格大**。
6. `print(value, i + 1, j + 1)`：题目的行列号从 1 开始，而下标从 0 开始，所以各加 1。
7. 没找到时输出 `None m n`。

**用样例 1 走一遍：**

```text
1 1 1 1 1
1 3 9 3 1
1 5 3 5 1
1 1 1 1 1
```

| 位置（下标） | 值 | 四个邻居 | 比较 | 输出 |
| --- | --- | --- | --- | --- |
| (1,1) | 3 | 1、5、1、9 | 3 不大于 9 | 不输出 |
| (1,2) | 9 | 1、3、3、3 | 9 > 3 | `9 2 3` |
| (1,3) | 3 | 1、5、9、1 | 3 不大于 9 | 不输出 |
| (2,1) | 5 | 3、1、1、3 | 5 > 3 | `5 3 2` |
| (2,2) | 3 | 9、1、5、5 | 3 不大于 9 | 不输出 |
| (2,3) | 5 | 3、1、3、1 | 5 > 3 | `5 3 4` |

与样例输出一致。

**易错点：**

- 必须**严格大于**，等于不算。样例 2 里有相等的数，所以输出 `None 3 5`。
- 输出的行列号要加 1，下标不能直接输出。

</div>

:::

::::

:::: question programming-19 | 7-19 矩阵转置

从键盘输入一个m(2&lt;=m&lt;=6)*n(2&lt;=n&lt;=6)阶的矩阵，编程输出它的转置矩阵。

#### 输入格式:

在第一行输入矩阵的行数m和列数n的值，在第二行按照矩阵格式输入矩阵的数据，同行数据之间用空格隔开。

#### 输出格式:

矩阵格式输出，同行数据之间用一个空格隔开。

#### 输入样例:

```text
3 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

#### 输出样例:

```text
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
```

<div class="question-tags"><span class="question-tag">矩阵转置</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m, n = map(int, input().split())
matrix = []
for _ in range(m):
    matrix.append(input().split())
for j in range(n):
    row = []
    for i in range(m):
        row.append(matrix[i][j])
    print(*row)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**转置是什么：** 把原矩阵的**列**变成新矩阵的**行**。原矩阵 m 行 n 列，转置后是 n 行 m 列。

**思路：** 先把整个矩阵读进二维列表，再按“一列一列”的顺序读出来，每读完一列就打印一行。

**逐句解释代码：**

1. `m, n = map(int, input().split())`：读入行数和列数。
2. `matrix = []`，然后 `for _ in range(m): matrix.append(input().split())`：读入 m 行，每行按空格切成字符串列表，追加进 `matrix`。这里不用转成整数，因为只是原样输出。
3. `for j in range(n)`：外层循环固定**原矩阵的列号** j，共 n 轮，每轮输出新矩阵的一行。
4. `row = []`：准备存放这一列的元素。
5. `for i in range(m)`：内层循环让行号 i 从上到下，`matrix[i][j]` 取出第 j 列的第 i 个元素，追加进 `row`。
6. `print(*row)`：`*` 把列表拆开，元素之间用一个空格隔开，行末没有多余空格。

**用样例走一遍（3 行 5 列）：**

```text
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

| j（原列号） | 从上到下取到的元素 | 打印的一行 |
| --- | --- | --- |
| 0 | `matrix[0][0]`、`matrix[1][0]`、`matrix[2][0]` = 1、1、1 | `1 1 1` |
| 1 | 2、2、2 | `2 2 2` |
| 2 | 3、3、3 | `3 3 3` |
| 3 | 4、4、4 | `4 4 4` |
| 4 | 5、5、5 | `5 5 5` |

输出 5 行，每行 3 个数，与样例一致。

**易错点：** 外层循环次数是 **n**（原列数），内层是 **m**（原行数），不要搞反。搞反会出现下标越界。

</div>

:::

::::

:::: question programming-20 | 7-20 显示直角数字图形

本题目要求输入行数，输出指定行数的图形。

#### 输入格式:

输入行数n,1&lt;=n&lt;=10

#### 输出格式:

输出图形。

#### 输入样例1:

在这里给出一组输入。例如：

```text
2
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
A
AB
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
7
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
A
AB
ABC
ABCD
ABCDE
ABCDEF
ABCDEFG
```

<div class="question-tags"><span class="question-tag">字符串累加</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
row = ''
for letter in 'ABCDEFGHIJ'[:n]:
    row += letter
    print(row)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 观察样例：第 1 行是 `A`，第 2 行是 `AB`，第 3 行是 `ABC`……每一行都是**上一行末尾再加一个字母**。所以用一个字符串 `row` 保存当前行，每轮往后追加一个字母，然后打印。

**逐句解释代码：**

1. `n = int(input())`：读入行数。
2. `row = ''`：当前行，一开始是空字符串。
3. `'ABCDEFGHIJ'[:n]`：切片，取字符串的前 n 个字符。`[:n]` 表示从开头取到下标 n 之前。例如 n = 3 得到 `'ABC'`。题目 n 最大为 10，所以准备 10 个字母。
4. `for letter in 'ABCDEFGHIJ'[:n]`：依次取出这 n 个字母，所以循环恰好执行 n 次，输出 n 行。
5. `row += letter`：把这个字母接到当前行末尾。
6. `print(row)`：打印当前行，`print` 自带换行。

**用样例 1 走一遍（输入 `2`）：**

| 轮次 | letter | 追加后的 row | 打印 |
| --- | --- | --- | --- |
| 1 | `A` | `A` | `A` |
| 2 | `B` | `AB` | `AB` |

输出两行，与样例一致。输入 7 时同理，循环 7 轮，最后一行是 `ABCDEFG`。

**易错点：** `row += letter` 要写在 `print` 之前。如果先打印再追加，第一行会打印出空行，并且每行都比应有的少一个字母。

</div>

:::

::::

:::: question programming-21 | 7-21 显示菱形图形

显示菱形图形，每行的宽度是11。

#### 输入格式:

输入显示的行数，行数在`1,3,5,7,9,11`中取值

#### 输出格式:

菱形图形，每行的宽度是11

#### 输入样例1:

在这里给出一组输入。例如：

```text
5
```

#### 输出样例1:

在这里给出相应的输出。例如：

```text
     *     
    ***    
   *****   
    ***    
     *     
```

#### 输入样例2:

在这里给出一组输入。例如：

```text
11
```

#### 输出样例2:

在这里给出相应的输出。例如：

```text
     *     
    ***    
   *****   
  *******  
 ********* 
***********
 ********* 
  *******  
   *****   
    ***    
     *     
```

<div class="question-tags"><span class="question-tag">居中对齐</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
for i in range(n):
    stars = n - 2 * abs(i - n // 2)
    padding = ' ' * ((11 - stars) // 2)
    print(padding + '*' * stars + padding)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 菱形一共 n 行，中间那一行星号最多（n 个），往上、往下每远离中间一行，星号就少 2 个。每一行的总宽度固定为 11，星号放在正中间，左右各补空格。

**公式怎么来的：**

- 中间行的下标是 `n // 2`（`//` 是整除）。例如 n = 5 时是 2。
- 第 i 行离中间行有 `abs(i - n // 2)` 行远，`abs` 是绝对值，上下对称。
- 每远一行少 2 个星号，所以 `stars = n - 2 * abs(i - n // 2)`。
- 剩下的空格是 11 − stars 个，左右平分，每边 `(11 - stars) // 2` 个。

**逐句解释代码：**

1. `n = int(input())`：读入行数。
2. `for i in range(n)`：i 取 0 到 n−1，每轮输出一行。
3. `stars = n - 2 * abs(i - n // 2)`：这一行的星号数。
4. `padding = ' ' * ((11 - stars) // 2)`：字符串乘整数是重复，得到一侧的空格。
5. `print(padding + '*' * stars + padding)`：左空格、星号、右空格拼起来。右侧空格也要输出，因为每行宽度必须是 11。

**用样例 1 走一遍（输入 `5`，中间行下标 2）：**

| i | abs(i−2) | stars | 每侧空格 (11−stars)//2 | 输出（`□` 代表空格） |
| --- | --- | --- | --- | --- |
| 0 | 2 | 1 | 5 | `□□□□□*□□□□□` |
| 1 | 1 | 3 | 4 | `□□□□***□□□□` |
| 2 | 0 | 5 | 3 | `□□□*****□□□` |
| 3 | 1 | 3 | 4 | `□□□□***□□□□` |
| 4 | 2 | 1 | 5 | `□□□□□*□□□□□` |

与样例一致。

**易错点：** 行数 n 是奇数时才能对称，题目保证 n 取 1、3、5……11。宽度 11 是固定值，不是 n。

</div>

:::

::::

:::: question programming-22 | 7-22 显示Pascal三角形

输入行数n,显示n行Pascal三角形。数字间有一个空格。每行最后一个数字后有一个空格。

#### 输入格式:

在一行中输入行数n。

#### 输出格式:

输出n行Pascal三角形。

#### 输入样例:

在这里给出一组输入。例如：

```text
4
```

#### 输出样例:

在这里给出相应的输出。例如：

```text
1 
1 1 
1 2 1 
1 3 3 1 
```

<div class="question-tags"><span class="question-tag">逐行递推</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
row = [1]
for _ in range(n):
    for value in row:
        print(value, end=' ')
    print()
    next_row = [1]
    for j in range(1, len(row)):
        next_row.append(row[j - 1] + row[j])
    next_row.append(1)
    row = next_row
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**Pascal 三角形的规则：** 每一行的两端都是 1，中间的每个数等于**上一行相邻两个数之和**。

```text
1
1 1
1 2 1        ← 中间的 2 = 1 + 1
1 3 3 1      ← 中间的 3 = 1 + 2，3 = 2 + 1
```

**思路：** 用列表 `row` 保存当前要打印的一行。每轮先打印 `row`，再根据它算出下一行，替换 `row`。

**逐句解释代码：**

1. `n = int(input())`：读入行数。
2. `row = [1]`：第 1 行只有一个 1。
3. `for _ in range(n)`：重复 n 轮，每轮输出一行。
4. `for value in row: print(value, end=' ')`：逐个打印当前行的数，每个数后面跟一个空格。题目要求每行最后一个数字后也有一个空格，所以用 `end=' '`，而不是 `print(*row)`。
5. `print()`：换行。
6. `next_row = [1]`：下一行的第一个数是 1。
7. `for j in range(1, len(row))`：`j` 从 1 取到 `len(row) - 1`，每次把上一行的 `row[j-1]` 和 `row[j]` 相加，追加到 `next_row`，这就是中间的数。
8. `next_row.append(1)`：下一行的最后一个数是 1。
9. `row = next_row`：把下一行变成当前行，进入下一轮。

**用样例走一遍（输入 `4`）：**

| 轮次 | 打印的 row | 算出的 next_row | 计算过程 |
| --- | --- | --- | --- |
| 1 | `1` | `[1, 1]` | 只有 1 个数，没有中间项，两端各一个 1 |
| 2 | `1 1` | `[1, 2, 1]` | 中间：1 + 1 = 2 |
| 3 | `1 2 1` | `[1, 3, 3, 1]` | 中间：1 + 2 = 3，2 + 1 = 3 |
| 4 | `1 3 3 1` | `[1, 4, 6, 4, 1]` | 最后一轮也会算，但不会再打印 |

输出四行，与样例一致。

**易错点：**

- 第 1 行 `row = [1]` 只有一个数，`range(1, 1)` 是空的，循环不执行，`next_row` 变成 `[1, 1]`，所以第 2 行是 `1 1`，不需要单独处理。
- 行末要有一个空格，不能省。

</div>

:::

::::
