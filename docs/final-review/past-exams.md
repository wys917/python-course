---
title: 期末上机真题
eyebrow: PAST EXAMS
description: 往届期末上机编程题、参考代码与解析。
code: Past Exams
questionGroups:
  - [2025-26 春夏 第一场, spring-2526-1, 3]
  - [2025-26 秋冬 第二场, autumn-2526-2, 3]
  - [2025-26 秋冬 第三场, autumn-2526-3, 3]
  - [2024-25 秋冬 第三场, autumn-2425-3, 2]
  - [2024 秋冬 第三场, autumn-24-3, 2]
  - [2022 春夏, spring-22, 1]
  - [样题, sample, 2]
---

<div class="editor-note">

本页收录往届期末上机编程题，共 **16 题**。大部分题目来自考后回忆，题干和样例可能与原卷略有出入，标注“回忆版”的题目尤其如此。参考代码都是自己写的，并用题目给出的样例（或自己构造的样例）逐条跑通。

</div>

<h2 id="spring-2526-1" class="quiz-group">2025-26 春夏 第一场<span>3 QUESTIONS</span></h2>

:::: question spring-2526-1-1 | 春夏第一场 第1题 分数序列求和

输入一个正整数 n，计算并输出如下分数序列的前 n 项之和：

1 + 1/3 + 1/5 + …… + 1/(2n-1)

#### 输入格式:

输入一个正整数 n。

#### 输出格式:

输出该序列的和，结果保留两位小数，并占 10 个字符宽度，右对齐。

#### 输入样例（自拟）:

```text
3
```

#### 输出样例（自拟，`□` 表示空格）:

```text
□□□□□□1.53
```

<div class="question-tags"><span class="question-tag">累加</span><span class="question-tag">格式化输出</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / (2 * i - 1)
print('{:10.2f}'.format(total))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 第 i 项的分母是 2i−1（i = 1、2、3 时分别是 1、3、5），用循环把每一项加到 `total` 里。

**格式 `{:10.2f}`：** 冒号后面是格式说明。`10` 表示总共占 10 个字符宽，不够时在**左边**补空格，也就是右对齐；`.2f` 表示保留 2 位小数。

**用 n = 3 走一遍：**

| i | 分母 2i−1 | 这一项 | total |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 2 | 3 | 0.3333 | 1.3333 |
| 3 | 5 | 0.2 | 1.5333 |

`1.53` 只有 4 个字符，左边补 6 个空格，凑成 10 个字符宽。

**易错点：** 循环 `range(1, n + 1)` 要包含 n；分母写成 `2 * i - 1`，写成 `2 * i + 1` 会多算一项。

</div>

:::

::::

:::: question spring-2526-2 | 春夏第一场 第2题 字符串加密（回忆版）

输入一行字符串，按下面的规则加密并输出结果：

- 大写字母做字母表对称转换：A→Z，B→Y，……，Z→A。
- 小写字母向后移动三位，超过 z 后从 a 重新开始：a→d，……，x→a，y→b，z→c。
- 数字字符变成 10 减该数字的结果，其中 0 仍为 0。例如 3→7，8→2。
- 其他字符保持不变。

#### 输入样例（自拟）:

```text
Ab xyz 038
```

#### 输出样例（自拟）:

```text
Ze abc 072
```

<div class="question-tags"><span class="question-tag">字符串遍历</span><span class="question-tag">chr / ord</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
result = ''
for ch in s:
    if ch.isupper():
        result += chr(ord('Z') - (ord(ch) - ord('A')))
    elif ch.islower():
        result += chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))
    elif ch.isdigit():
        result += str((10 - int(ch)) % 10)
    else:
        result += ch
print(result)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 逐个字符判断类型，按规则变换后拼到 `result` 末尾。`isupper`、`islower`、`isdigit` 分别判断大写、小写、数字。`ord` 把字符变成编码数字，`chr` 把编码变回字符。

**大写对称：** `ord(ch) - ord('A')` 是这个字母在字母表中的位置（A 为 0）。对称转换就是从 Z 往回数同样的位置：`ord('Z') - 位置`。例如 B 的位置是 1，对应 `Z` 往回 1 位，得到 Y。

**小写后移：** 位置加 3 之后对 26 取余，超过 z 就绕回 a。例如 y 的位置是 24，(24+3) % 26 = 1，对应 b。

**数字：** `(10 - 数字) % 10`。`% 10` 是为了让 0 变成 0，而不是 10。

**用样例走一遍（`Ab xyz 038`）：**

| 字符 | 类型 | 结果 |
| --- | --- | --- |
| A | 大写 | Z |
| b | 小写 | e |
| 空格 | 其他 | 空格 |
| x、y、z | 小写 | a、b、c |
| 0、3、8 | 数字 | 0、7、2 |

输出 `Ze abc 072`。

</div>

:::

::::

:::: question spring-2526-3 | 春夏第一场 第3题 外卖搭配推荐（回忆版）

外卖平台记录了若干用户的历史点餐记录，每条记录是一名用户一次购买的所有食品。给定一个目标食品，要为用户推荐最常与它一起出现的其他食品。

- 只统计包含目标食品的记录。
- 在这些记录中统计除目标食品以外的各食品出现次数，推荐次数最多的。
- 次数并列最多时，按字典序升序输出，用一个空格分隔。
- 没有包含目标食品的记录，或这些记录里没有其他食品，输出 `NONE`。

#### 输入格式:

第一行是一个二维列表，表示历史点餐记录；第二行是目标食品。

#### 输入样例:

```text
[['炸鸡', '薯条', '可乐'], ['炸鸡', '薯条'], ['可乐', '薯条'], ['炸鸡', '薯条']]
薯条
```

#### 输出样例:

```text
炸鸡
```

<div class="question-tags"><span class="question-tag">eval</span><span class="question-tag">字典计数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
history = eval(input())
target = input()
count = {}
for record in history:
    if target in record:
        for item in record:
            if item != target:
                count[item] = count.get(item, 0) + 1
if not count:
    print('NONE')
else:
    best = max(count.values())
    names = sorted(name for name in count if count[name] == best)
    print(' '.join(names))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 用字典 `count` 记录“食品 → 和目标一起出现的次数”。

1. `eval(input())` 把输入的列表字面量直接变成 Python 列表。
2. 遍历每条记录，只处理包含目标的记录（`target in record`）。
3. 对这条记录里**不是目标**的食品，次数加 1。`count.get(item, 0)` 表示取不到时当 0。
4. 字典为空，说明没有可推荐的食品，输出 `NONE`。
5. 否则先求最大次数，再取出所有等于最大次数的名字，排序后用空格连接。`' '.join(...)` 不会在末尾留空格。

**用样例走一遍（目标 `薯条`）：**

| 记录 | 含薯条？ | 计数后的 count |
| --- | --- | --- |
| 炸鸡、薯条、可乐 | 是 | 炸鸡 1，可乐 1 |
| 炸鸡、薯条 | 是 | 炸鸡 2，可乐 1 |
| 可乐、薯条 | 是 | 炸鸡 2，可乐 2 |
| 炸鸡、薯条 | 是 | 炸鸡 3，可乐 2 |

最大次数是 3，只有炸鸡，输出 `炸鸡`。

**易错点：** 并列时要全部输出并排序；没有可推荐的食品要输出 `NONE`，不是空行。

</div>

:::

::::

<h2 id="autumn-2526-2" class="quiz-group">2025-26 秋冬 第二场<span>3 QUESTIONS</span></h2>

:::: question autumn-2526-2-1 | 秋冬第二场 第1题 能被3整除但不能被2整除的数之和（回忆版）

输入正整数 n，求 1 到 n 中所有**能被 3 整除但不能被 2 整除**的整数的和，输出时占 8 位、右对齐。

#### 输入样例:

```text
10
```

#### 输出样例（`□` 表示空格）:

```text
□□□□□□12
```

<div class="question-tags"><span class="question-tag">条件累加</span><span class="question-tag">格式化输出</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 3 == 0 and i % 2 != 0:
        total += i
print('{:8d}'.format(total))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 遍历 1 到 n，两个条件同时满足才累加：`i % 3 == 0`（能被 3 整除）并且 `i % 2 != 0`（不能被 2 整除，即奇数）。

**格式 `{:8d}`：** `d` 表示整数，`8` 表示总宽度 8，不足时左边补空格，即右对齐。

**用 n = 10 走一遍：** 1 到 10 中能被 3 整除的有 3、6、9，其中 6 是偶数，被排除，剩下 3 和 9，和为 12。`12` 只有 2 个字符，左边补 6 个空格。

**易错点：** 两个条件要用 `and` 连接，不能写成 `or`。

</div>

:::

::::

:::: question autumn-2526-2-2 | 秋冬第二场 第2题 选课推荐（回忆版）

学校提供了学长学姐的过往选课表。先输入一个二维列表（每个子列表是一位学长或学姐的选课列表），再输入一个字符串 s，表示某位同学已经选的课程。

从选了 s 的学长学姐的课表中，找出 s 以外的其他课程，统计出现次数，推荐次数最多的课程。多门课程次数并列时，按字母顺序从小到大全部输出，用空格隔开。如果没有人选 s，或者选了 s 的人没有选其他课程，输出 `NONE`。

#### 输入样例1:

```text
[['physics','maths','chemistry'],['physics','maths']]
maths
```

#### 输出样例1:

```text
physics
```

#### 输入样例2:

```text
[['physics','chemistry'],['maths']]
biology
```

#### 输出样例2:

```text
NONE
```

**说明：** 原回忆卷的第二个样例没有写出第二行输入，这里补了一个没人选过的课程 `biology`，结果同样是 `NONE`（已用代码验证）。

<div class="question-tags"><span class="question-tag">eval</span><span class="question-tag">字典计数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
history = eval(input())
target = input()
count = {}
for courses in history:
    if target in courses:
        for course in courses:
            if course != target:
                count[course] = count.get(course, 0) + 1
if not count:
    print('NONE')
else:
    best = max(count.values())
    names = sorted(name for name in count if count[name] == best)
    print(' '.join(names))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

这道题和春夏第一场的“外卖搭配推荐”是同一类题，做法完全一样：只统计包含目标的记录，数其余元素出现的次数，取最大值，并列时排序后输出，一个都没有就输出 `NONE`。

**用样例 1 走一遍（目标 `maths`）：**

| 课表 | 含 maths？ | 计数后的 count |
| --- | --- | --- |
| physics、maths、chemistry | 是 | physics 1，chemistry 1 |
| physics、maths | 是 | physics 2，chemistry 1 |

最大次数是 2，只有 physics，输出 `physics`。

样例 2 中没有任何课表含 `biology`，`count` 一直为空，输出 `NONE`。

</div>

:::

::::

:::: question autumn-2526-2-3 | 秋冬第二场 第3题 提取八进制字符（回忆版）

输入一个字符串，取出其中所有可以当作八进制数字的字符（`'0'` 到 `'7'`），按原顺序拼成一个八进制数字串，再把它转换成十进制整数输出。如果一个这样的字符都没有，输出 `NONE`。

#### 输入样例1:

```text
8&9
```

#### 输出样例1:

```text
NONE
```

#### 输入样例2（原卷作者说明这个样例是 AI 给的）:

```text
a1b2c7d8e
```

#### 输出样例2:

```text
87
```

<div class="question-tags"><span class="question-tag">字符串筛选</span><span class="question-tag">进制转换</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
digits = ''
for ch in s:
    if ch in '01234567':
        digits += ch
if digits == '':
    print('NONE')
else:
    print(int(digits, 8))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 先筛选，再转换。

1. 遍历字符串，字符属于 `'01234567'` 就接到 `digits` 后面。注意 `8` 和 `9` 不是八进制数字。
2. 一个都没筛出来（`digits` 仍是空串），输出 `NONE`。
3. 否则用 `int(digits, 8)`：第二个参数 8 表示把字符串当作**八进制**解析，结果是十进制整数。

**用样例 2 走一遍：** `a1b2c7d8e` 中属于 0 到 7 的字符依次是 1、2、7，拼成 `"127"`。八进制 127 转十进制：1×64 + 2×8 + 7 = 87。

**样例 1：** `8&9` 里的 8 和 9 都不是八进制数字，没有可用字符，输出 `NONE`。

**易错点：** `int("", 8)` 会报错，所以空串必须先判断。

</div>

:::

::::

<h2 id="autumn-2526-3" class="quiz-group">2025-26 秋冬 第三场<span>3 QUESTIONS</span></h2>

:::: question autumn-2526-3-1 | 秋冬第三场 第1题 交错求和

输入一个正整数 m，计算并输出交错求和：

1 - 2 + 3 - 4 + 5 - 6 + …… ± m

从 1 开始为正号，之后正负交替。

#### 输入格式:

一行，一个正整数 m。

#### 输出格式:

输出交错求和的结果（整数）。

#### 输入样例:

```text
5
```

#### 输出样例:

```text
3
```

<div class="question-tags"><span class="question-tag">交替符号</span><span class="question-tag">累加</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m = int(input())
total = 0
for i in range(1, m + 1):
    if i % 2 == 1:
        total += i
    else:
        total -= i
print(total)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 奇数项为正、偶数项为负，遍历 1 到 m，奇数加、偶数减。

**用 m = 5 走一遍：**

| i | 奇偶 | 操作 | total |
| --- | --- | --- | --- |
| 1 | 奇 | +1 | 1 |
| 2 | 偶 | −2 | −1 |
| 3 | 奇 | +3 | 2 |
| 4 | 偶 | −4 | −2 |
| 5 | 奇 | +5 | 3 |

输出 `3`。m 为偶数时结果是负数，例如 m = 6 得到 −3。

</div>

:::

::::

:::: question autumn-2526-3-2 | 秋冬第三场 第2题 早餐卡路里筛选与排序（回忆版）

给定一个卡路里字典（回忆卷自造，仅用于理解题意）：鸡蛋 90，牛奶 120，面包 80，咖啡 30，油条 250，豆浆 110，燕麦 150，酸奶 140，果汁 100，培根 200。

输入一个二维列表 L，`L[i]` 是第 i+1 类早餐包含的食物名称；第二行输入目标卡路里 m。

计算每类早餐的总卡路里，找出总卡路里**严格小于** m 的类别序号（从 1 开始），按总卡路里升序输出；总卡路里相同时按序号升序。没有满足的类别输出 `NONE`。

#### 输入样例:

```text
[["鸡蛋","牛奶"],["面包","咖啡"],["油条","豆浆"],["燕麦","酸奶","果汁"],["培根","鸡蛋","牛奶"]]
250
```

#### 输出样例:

```text
2 1
```

<div class="question-tags"><span class="question-tag">字典查值</span><span class="question-tag">多关键字排序</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
cal = {'鸡蛋': 90, '牛奶': 120, '面包': 80, '咖啡': 30, '油条': 250,
       '豆浆': 110, '燕麦': 150, '酸奶': 140, '果汁': 100, '培根': 200}
L = eval(input())
m = int(input())
result = []
for index in range(len(L)):
    total = 0
    for name in L[index]:
        total += cal[name]
    if total < m:
        result.append((total, index + 1))
result.sort()
if result:
    print(*[item[1] for item in result])
else:
    print('NONE')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 算每类的总卡路里，把满足条件的存成 `(总卡路里, 序号)` 元组，排序后只输出序号。

**为什么存元组：** 元组排序时先比较第一项（总卡路里），相同再比较第二项（序号），正好符合“先按卡路里升序，相同按序号升序”。

**用样例走一遍：**

| 序号 | 食物 | 总卡路里 | 小于 250？ |
| --- | --- | --- | --- |
| 1 | 鸡蛋、牛奶 | 90+120 = 210 | 是 |
| 2 | 面包、咖啡 | 80+30 = 110 | 是 |
| 3 | 油条、豆浆 | 250+110 = 360 | 否 |
| 4 | 燕麦、酸奶、果汁 | 150+140+100 = 390 | 否 |
| 5 | 培根、鸡蛋、牛奶 | 200+90+120 = 410 | 否 |

结果列表是 `[(210, 1), (110, 2)]`，排序后变成 `[(110, 2), (210, 1)]`，输出 `2 1`。

**易错点：** 条件是严格小于，等于 m 的不算；序号从 1 开始，要用 `index + 1`。

</div>

:::

::::

:::: question autumn-2526-3-3 | 秋冬第三场 第3题 十六进制字符筛选、逆序、转十进制

输入一个字符串 s，从左往右筛选出属于十六进制字符集合的字符（`0-9`、`a-f`、`A-F`），按出现顺序组成新串，再把新串**逆序**，当作十六进制数，输出对应的十进制整数。没有任何十六进制字符时输出 `NONE`。

#### 输入样例1:

```text
xxabZ19
```

#### 输出样例1:

```text
37306
```

#### 输入样例2:

```text
GHI-xyz
```

#### 输出样例2:

```text
NONE
```

<div class="question-tags"><span class="question-tag">字符串筛选</span><span class="question-tag">进制转换</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
kept = ''
for ch in s:
    if ch in '0123456789abcdefABCDEF':
        kept += ch
if kept == '':
    print('NONE')
else:
    print(int(kept[::-1], 16))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 筛选、逆序、转换三步。

1. 遍历字符串，属于十六进制字符集合的就接到 `kept` 后面。
2. `kept[::-1]` 是切片写法，步长 −1 表示从后往前取，得到逆序字符串。
3. `int(字符串, 16)` 把字符串当作十六进制数转成十进制。

**用样例 1 走一遍：** `xxabZ19` 中属于十六进制的字符依次是 a、b、1、9（x、Z 不是），拼成 `ab19`；逆序得 `91ba`；十六进制 91ba = 9×4096 + 1×256 + 11×16 + 10 = 37306。

**样例 2：** `GHI-xyz` 里没有十六进制字符，输出 `NONE`。

**易错点：** 大小写字母 a-f、A-F 都要算；空串要先判断，否则 `int('', 16)` 会报错。

</div>

:::

::::

<h2 id="autumn-2425-3" class="quiz-group">2024-25 秋冬 第三场<span>2 QUESTIONS</span></h2>

:::: question autumn-2425-3-1 | 2024-25 秋冬第三场 第1题 求数列前 n 项和（回忆版）

输入一个正整数 n，计算数列 1/2 + 1/6 + 1/10 + …… 的前 n 项之和，在一行中输出结果，保留 2 位小数。

#### 输入样例:

```text
3
```

#### 输出样例:

```text
0.77
```

<div class="question-tags"><span class="question-tag">累加</span><span class="question-tag">找规律</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
total = 0
for i in range(n):
    total += 1 / (4 * i + 2)
print(f'{total:.2f}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**找规律：** 分母依次是 2、6、10，每次加 4，所以第 k 项（k 从 1 开始）的分母是 4k−2。代码里 `i` 从 0 开始，对应分母 `4 * i + 2`。

**用 n = 3 走一遍：**

| i | 分母 | 这一项 | total |
| --- | --- | --- | --- |
| 0 | 2 | 0.5 | 0.5 |
| 1 | 6 | 0.1667 | 0.6667 |
| 2 | 10 | 0.1 | 0.7667 |

保留 2 位小数得 `0.77`。

</div>

:::

::::

:::: question autumn-2425-3-2 | 2024-25 秋冬第三场 第2题 判断马尔可夫矩阵（回忆版）

马尔可夫矩阵满足三个条件：

1. 是方阵（n×n）。
2. 所有元素非负。
3. 每一行的和等于 1。

给定一个矩阵，是马尔可夫矩阵输出 `yes`，否则输出 `no`。

#### 输入格式:

第一行一个正整数 n，随后 n 行，每行给出 n 个数，以空格分隔。

#### 输入样例1:

```text
3
0 0 1
0.5 0.5 0
0.3 0.5 0.2
```

#### 输出样例1:

```text
yes
```

#### 输入样例2（自拟，有负数且行和不为 1）:

```text
4
0.1 0.4 0.5 0
1 0 0 0
-0.5 0.5 1 0
0.2 0.8 0 0
```

#### 输出样例2:

```text
no
```

<div class="question-tags"><span class="question-tag">矩阵</span><span class="question-tag">浮点数比较</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
ok = True
for _ in range(n):
    row = list(map(float, input().split()))
    if len(row) != n:
        ok = False
    for x in row:
        if x < 0:
            ok = False
    if abs(sum(row) - 1) > 1e-9:
        ok = False
print('yes' if ok else 'no')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 用标记 `ok` 先假设成立，逐行检查，一旦发现违反条件就改成 `False`，但**要把 n 行都读完**再输出，避免输入错位。

**逐项检查：**

- 方阵：每行元素个数 `len(row)` 应等于 n。
- 非负：行内有 `x < 0` 就不是。
- 行和为 1：不能直接写 `sum(row) == 1`，因为浮点数有误差（例如 0.1+0.2 不恰好等于 0.3），所以用 `abs(sum(row) - 1) > 1e-9` 判断“差得太多”。

**用样例 1 走一遍：** 三行的和分别是 1、1、1.0，元素都非负，每行 3 个数，输出 `yes`。

**样例 2：** 第 3 行有 −0.5，输出 `no`。

**说明：** 回忆卷里的第二个样例是 4 行、每行 3 个数，本身不是方阵，所以这里改成了自拟的方阵样例。

</div>

:::

::::

<h2 id="autumn-24-3" class="quiz-group">2024 秋冬 第三场<span>2 QUESTIONS</span></h2>

:::: question autumn-24-3-1 | 2024 秋冬第三场 第1题 统计字符（回忆版）

输入一个字符串，统计其中小写字母、大写字母、数字和其他字符的个数。

#### 输入样例（类似）:

```text
abCD& 123
```

#### 输出样例（类似）:

```text
小写 2
大写 2
数字 3
其他 2
```

<div class="question-tags"><span class="question-tag">字符分类</span><span class="question-tag">计数</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
s = input()
lower = upper = digit = other = 0
for ch in s:
    if 'a' <= ch <= 'z':
        lower += 1
    elif 'A' <= ch <= 'Z':
        upper += 1
    elif '0' <= ch <= '9':
        digit += 1
    else:
        other += 1
print('小写', lower)
print('大写', upper)
print('数字', digit)
print('其他', other)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 遍历每个字符，用 `if / elif / else` 分成四类，各自计数。`'a' <= ch <= 'z'` 是链式比较，判断字符是否落在 a 到 z 之间。

**用样例走一遍（`abCD& 123`）：** a、b 是小写（2）；C、D 是大写（2）；1、2、3 是数字（3）；`&` 和空格是其他（2）。

**易错点：** 空格也算“其他”，不要漏数。

</div>

:::

::::

:::: question autumn-24-3-2 | 2024 秋冬第三场 第2题 矩阵中的素数（回忆版）

输入一个 n，再输入一个 n×n 的矩阵。矩阵中恰有一个素数（所有数都大于 2），并且它不在边界上。输出这个素数的行号、列号（从 0 开始）和它本身，再输出它周围八个数的和。

#### 输入样例:

```text
4
4 4 4 4
4 4 4 4
4 4 37 4
4 4 4 4
```

#### 输出样例:

```text
(2,2):37
32
```

<div class="question-tags"><span class="question-tag">素数</span><span class="question-tag">二维列表</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if is_prime(matrix[i][j]):
            around = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di != 0 or dj != 0:
                        around += matrix[i + di][j + dj]
            print(f'({i},{j}):{matrix[i][j]}')
            print(around)
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 遍历非边界位置，找到素数后，把它周围 3×3 范围内除自己以外的 8 个数加起来。

**周围八个数：** 行偏移 `di` 和列偏移 `dj` 各取 −1、0、1，共 9 种组合，去掉 `(0, 0)`（自己）剩 8 个。因为素数不在边界，这 8 个位置一定不越界。

**判断素数：** 自定义函数 `is_prime`，试除到平方根（见作业 7-2）。

**用样例走一遍：** 4 阶矩阵的非边界位置是 (1,1)、(1,2)、(2,1)、(2,2)。只有 (2,2) 的 37 是素数（4 不是素数）。它周围 8 个数都是 4，和为 32，输出 `(2,2):37` 和 `32`。

**易错点：** 行号列号从 0 开始，直接输出下标即可；循环范围 `range(1, n - 1)` 排除了边界。

</div>

:::

::::

<h2 id="spring-22" class="quiz-group">2022 春夏<span>1 QUESTIONS</span></h2>

:::: question spring-22-1 | 2022 春夏 沙漏图形（回忆版）

输入一个 n（1≤n≤30），打印沙漏形状的图形。每个数字前后都要有空格，每一行末尾也有一个空格。

#### 输入样例1:

```text
5
```

#### 输出样例1（`□` 表示空格）:

```text
□3□4□5□4□3□
□□3□4□4□3□
□□□3□4□3□
□□□□3□3□
□□□□□3□
□□□□3□3□
□□□3□4□3□
□□3□4□4□3□
□3□4□5□4□3□
```

#### 输入样例2:

```text
6
```

#### 输出样例2（`□` 表示空格）:

```text
□3□4□5□5□4□3□
□□3□4□5□4□3□
□□□3□4□4□3□
□□□□3□4□3□
□□□□□3□3□
□□□□□□3□
□□□□□3□3□
□□□□3□4□3□
□□□3□4□4□3□
□□3□4□5□4□3□
□3□4□5□5□4□3□
```

**说明：** 样例 2 共 11 行，下半部分是按图形的上下对称性整理的，原回忆卷里只给出了完整的 n=7 输出。

<div class="question-tags"><span class="question-tag">图形输出</span><span class="question-tag">对称</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())

def line(k):
    nums = [str(3 + min(j, k - 1 - j)) for j in range(k)]
    return ' ' * (n - k + 1) + ' '.join(nums) + ' '

rows = [line(k) for k in range(n, 0, -1)] + [line(k) for k in range(2, n + 1)]
print('\n'.join(rows))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**观察图形：** 上半部分从第 n 行的 n 个数逐行减少到 1 个数，下半部分再逐行增加回 n 个数，中间那一行（1 个数）只出现一次。所以行的“长度”依次是 n、n−1、……、2、1、2、……、n。

**每一行的数字：** 一行有 k 个数，从两端往中间依次是 3、4、5……，到中间不再增大，左右对称。第 j 个位置（j 从 0 开始）的值是 `3 + min(j, k-1-j)`：`j` 是到左端的距离，`k-1-j` 是到右端的距离，取较小的就是“离最近一端有多远”。

**每一行前面的空格：** 每缩短一个数，前面多一个空格，所以第 k 个数的行前面有 `n - k + 1` 个空格。

**拼接一行：** `' '.join(nums)` 在数字之间放一个空格，最后加上末尾的一个空格。

**上下两半：** 上半是 `range(n, 0, -1)`（n 到 1），下半是 `range(2, n + 1)`（2 到 n），中间的 1 个数那一行不重复。

**用 n = 5 走一遍（部分）：**

| k | 数字 | 前导空格数 |
| --- | --- | --- |
| 5 | 3 4 5 4 3 | 1 |
| 4 | 3 4 4 3 | 2 |
| 1 | 3 | 5 |
| 2 | 3 3 | 4 |

**易错点：** 最宽一行前面也有 1 个空格；中间一行不能打印两次。

</div>

:::

::::

<h2 id="sample" class="quiz-group">样题<span>2 QUESTIONS</span></h2>

:::: question sample-1 | 样题 7-1 求平方与倒数序列的近似和

对 m ≤ n，计算 m² + 1/m + (m+1)² + 1/(m+1) + …… + n² + 1/n，近似和取“小于序列和的最大整数”（向下取整）。

#### 输入格式:

一行输入两个正整数 m 和 n（m ≤ n）。

#### 输出格式:

按 `sum = S` 的格式输出，等号两侧各有一个空格。

#### 输入样例:

```text
5 10
```

#### 输出样例:

```text
sum = 355
```

<div class="question-tags"><span class="question-tag">累加</span><span class="question-tag">取整</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
m, n = map(int, input().split())
total = 0
for i in range(m, n + 1):
    total += i * i + 1 / i
print(f'sum = {int(total)}')
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 通项是 `i*i + 1/i`，i 从 m 取到 n，全部加起来再取整。

**取整：** `int()` 对正数是直接舍去小数部分，等于向下取整。

**用样例走一遍（5 到 10）：** 平方和 25+36+49+64+81+100 = 355；倒数和 1/5+1/6+…+1/10 约 0.846；总和约 355.846，取整得 355，输出 `sum = 355`。

**易错点：** 输出格式里 `sum = ` 等号两侧都有空格。

</div>

:::

::::

:::: question sample-2 | 样题 7-2 逆时针蛇形矩阵

输入一个正整数 N（1≤N≤20），输出 N×N 的逆时针蛇形矩阵：数字 1 到 N×N 从左上角出发，先向下，再向右，再向上，再向左，一圈圈往里收。每个数占 4 位。

#### 输入样例:

```text
5
```

#### 输出样例:

```text
   1  16  15  14  13
   2  17  24  23  12
   3  18  25  22  11
   4  19  20  21  10
   5   6   7   8   9
```

<div class="question-tags"><span class="question-tag">螺旋填数</span><span class="question-tag">二维列表</span></div>

::: answer

<div class="answer-section-label">参考答案 <span>ANSWER</span></div>

```python
n = int(input())
grid = [[0] * n for _ in range(n)]
num = 1
top, bottom, left, right = 0, n - 1, 0, n - 1
while top <= bottom and left <= right:
    for i in range(top, bottom + 1):
        grid[i][left] = num
        num += 1
    left += 1
    for j in range(left, right + 1):
        grid[bottom][j] = num
        num += 1
    bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            grid[i][right] = num
            num += 1
        right -= 1
    if top <= bottom:
        for j in range(right, left - 1, -1):
            grid[top][j] = num
            num += 1
        top += 1
for row in grid:
    print(''.join(f'{x:4d}' for x in row))
```

<div class="explanation">

<div class="section-label">解析 <span>EXPLANATION</span></div>

**思路：** 一圈一圈填。用 `top`、`bottom`、`left`、`right` 表示还没填的矩形范围，每圈按“下、右、上、左”四段填，填完一段就把对应的边界往里收一格。

**四段：**

1. 沿左边一列向下填（行 `top` 到 `bottom`），然后 `left += 1`。
2. 沿底边一行向右填（列 `left` 到 `right`），然后 `bottom -= 1`。
3. 沿右边一列向上填（行 `bottom` 到 `top`），然后 `right -= 1`。
4. 沿顶边一行向左填（列 `right` 到 `left`），然后 `top += 1`。

**为什么第 3、4 段要先判断：** 范围收到只剩一行或一列时，前面的段已经把数填完了，再填会重复覆盖，所以先用 `if` 检查范围是否还有效。

**用 N = 5 走一遍：**

| 圈 | 填的数字 |
| --- | --- |
| 最外圈 | 1 到 5 向下，6 到 9 向右，10 到 13 向上，14 到 16 向左 |
| 中间圈 | 17 到 19 向下，20 到 21 向右，22 到 23 向上，24 向左 |
| 中心 | 25 |

**输出格式：** `f'{x:4d}'` 让每个数占 4 位右对齐，`''.join(...)` 把一行拼起来。

</div>

:::

::::
