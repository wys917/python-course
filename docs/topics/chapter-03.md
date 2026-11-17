---
title: 第3章 使用字符串、列表和元组
eyebrow: CHAPTER 03
chapter: true
code: 第3章
---

<div class="chapter-source">依据第3章课件（70 页）整理，按教材 3.1–3.4 组织。</div>

## 3.1 序列的访问及运算符

字符串、列表、元组都是序列。索引从 0 开始，负索引从末尾计算：`-1` 表示最后一个元素。

```python
a = [12, -5, -22, -10, -26, 35, 0, 49, 3, -21]
print(a[1::2])   # [-5, -10, 35, 49, -21]
print(a[3:8:2])  # [-10, 35, 49]
print(a[::-1])   # 生成逆序的新列表
print(a[100:])   # []
```

切片 `seq[start:stop:step]` 包含起点、不含终点，步长不能为 0。切片边界越界会截断，单元素索引越界会引发 `IndexError`。

| 操作 | 含义 | 示例 |
| --- | --- | --- |
| `x in seq` | 成员判断 | `'34' in '1234'` 为真 |
| `seq1 + seq2` | 同类序列拼接 | `[1]+[2]` → `[1,2]` |
| `seq * n` | 重复元素 | `[4,5]*3` → `[4,5,4,5,4,5]` |
| `len(seq)` | 元素个数 | `len('ab')` → `2` |
| `min()` / `max()` | 最小值 / 最大值 | `max((3,5,7))` → `7` |

`"34" in "1234" == True` 是链式比较，等价于 `("34" in "1234") and ("1234" == True)`，结果为假。只需判断子串时直接写 `"34" in "1234"`。

## 3.2 字符串使用

字符串不可原地修改。`s.lower()` 等方法返回新字符串；`s.lower` 只是取得方法对象，必须带 `()` 才会调用。

| 方法 | 用途 | 注意 |
| --- | --- | --- |
| `find(sub, start)` | 查找首次匹配位置 | 未找到返回 -1 |
| `index(sub)` | 查找位置 | 未找到时报错 |
| `split(sep)` | 拆分字符串 | 指定分隔符会保留连续分隔符产生的空项 |
| `sep.join(items)` | 连接字符串 | 只在相邻元素间添加分隔符 |
| `strip()` | 去除两端空白 | 不影响中间空白 |
| `lstrip()` / `rstrip()` | 只清理左端 / 右端 | 需要保留另一端空格时使用 |
| `replace(old,new)` | 替换子串 | 返回新字符串 |
| `lower()` / `upper()` | 大小写转换 | 原字符串不变 |
| `isalpha()` / `isdigit()` / `isalnum()` | 判断字母 / 数字 / 字母或数字 | 空字符串返回假，按 Unicode 字符规则判断 |

```python
print('3//11//2018'.split('/'))  # ['3', '', '11', '', '2018']
print(' a  b '.split())          # ['a', 'b']
print(' '.join(['12', '12']))    # 12 12
print(repr('12 ' * 2))          # '12 12 '，末尾空格保留
```

不要用 `if s.find(x)` 判断是否找到：位置 0 为假，未找到的 -1 反而为真。使用 `x in s` 更直接。

### 计数与序列拆包

```python
print('banana'.count('an'))  # 2，不重叠计数
first, *middle, last = [1, 2, 3, 4]
print(first, middle, last)   # 1 [2, 3] 4
```

带星号的接收变量得到列表；一次拆包最多有一个星号接收项。列表还支持切片赋值：`a[1:3]=[8,9]`。`del a[i]` 删除指定位置，`del a[1:3]` 删除一个区间。

### f 字符串

```python
name, score = 'Li', 92.5
print(f'{name}: {score:.1f}')  # Li: 92.5
print(f'{31:08b}')            # 00011111
```

花括号内写表达式，冒号后写格式要求。需要输出字面花括号时使用两个连续的左花括号或右花括号。

## 3.3 列表和元组使用

### 列表修改与返回值

```python
a = [3, 1, 2]
a.append(4)          # 追加单个对象
a.extend([5, 6])     # 逐个追加元素
a.insert(0, 9)       # 在下标 0 之前插入
x = a.pop()          # 删除并返回末尾元素
a.remove(3)          # 删除首个值为 3 的元素
a.sort()             # 原地排序，返回 None
```

`append()`、`extend()`、`sort()`、`reverse()` 修改原列表并返回 `None`。`sorted(a)` 返回新列表，`a[::-1]` 返回逆序的新列表。因此不能用 `for x in a.sort()` 遍历排序结果。

### 赋值、浅拷贝与嵌套引用

```python
a = [[1], [2]]
b = a
c = a.copy()
print(a is b, a is c)  # True False
a[0].append(3)
print(c)              # [[1, 3], [2]]
```

`a.copy()`、`a[:]` 只复制最外层列表，内部可变对象仍共享。`[[0]*3]*2` 的两行也是同一列表；独立行用 `[[0]*3 for _ in range(2)]`。

### 字符串和列表的互转

```python
chars = list('Python')
text = ''.join(chars)
numbers = list(map(int, '3 4 5'.split()))
```

`join()` 的元素必须都是字符串。列表可变不代表列表中每个元素都支持相同运算。

### 元组与拆包

```python
point = (3, 4)
single = (3,)  # 一个元素仍需逗号
x, y = point
students = [(3180102988, '褚好'), (3170102465, '王凯亮')]
for student_id, name in students:
    print(student_id, name)
```

元组不能重新给单个位置赋值，但若元素是列表，该内部列表仍可修改。按行访问用 `students[i]`，再以 `[0]`、`[1]` 选字段。

## 3.4 随机函数库 random

```python
import random
print(random.random())        # [0, 1) 浮点数
print(random.randint(10, 99))  # 两端都包含
print(random.randrange(10, 100))  # 不含 100
items = [1, 2, 3]
random.shuffle(items)         # 原地打乱，返回 None
print(random.choice(items))   # 随机选择一个元素
print(random.sample(items, 2)) # 无放回抽样
random.seed(2)                # 固定伪随机序列的初始状态
```

`int(random.random()*90)+10` 的范围是 10～99；随机生成整数时直接使用 `randint()` 或 `randrange()` 更清楚。

<div class="chapter-links"><a href="../assignments/homework-03.html">第3章作业 →</a><a href="../quizzes/quiz-02.html">第二次上机小测 →</a><a href="./chapter-04.html">第4章 →</a></div>
