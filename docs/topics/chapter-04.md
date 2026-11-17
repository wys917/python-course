---
title: 第4章 条件、循环和其他语句
eyebrow: CHAPTER 04
chapter: true
code: 第4章
---

<div class="chapter-source">依据第4章课件（75 页）整理。</div>

## 4.1 条件语句

`if` 在条件为真时执行语句块；`elif` 按顺序判断其他条件；`else` 处理其余情况。同一组 `if-elif-else` 最多执行一个分支，多个独立 `if` 则可能都执行。

```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
```

比较使用 `==`，赋值使用 `=`。条件表达式的格式是 `真值 if 条件 else 假值`。

```python
x = -3
absolute = x if x >= 0 else -x
```

嵌套条件中，`else` 与相同缩进的 `if` 对应。比较端点时留意 `>` 与 `>=` 的区别。

## 4.2 while 循环

`while` 每次先判断条件；条件为假时结束。循环内要使状态逐步接近结束条件。

```python
n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.insert(0, remainder)
print(remainders)  # [1, 0, 0, 1, 1, 1]
```

- `break`：结束当前最内层循环。
- `continue`：跳过本轮剩余语句，开始下一轮。
- 循环的 `else`：正常迭代结束或条件变假时执行；通过 `break` 结束则不执行。

```python
numbers = [1, 3, 5]
for value in numbers:
    if value % 2 == 0:
        print('找到偶数')
        break
else:
    print('没有偶数')
```

## 4.3 for 循环

`for` 逐项遍历可迭代对象，不局限于整数。`range(a,b,s)` 不包含 b，s 可以为负但不能为 0。

```python
for i in range(10, 0, -2):
    print(i, end=' ')  # 10 8 6 4 2
print()
for index, value in enumerate(['a', 'b']):
    print(index, value)
```

循环不创建独立块级作用域；非空循环结束后，循环变量通常保留最后一次的值。遍历期间删改同一列表容易跳过元素，宜构造新列表或遍历副本。

## 4.4 搜索和排序

### 线性搜索与最值

逐个检查元素，找到后立即返回位置；未找到返回约定的标记。空列表没有最大值，使用 `max()` 前需确认输入非空。

```python
def linear_search(items, target):
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1
```

### 二分搜索

二分搜索要求数据**已经有序**。每次检查中间元素并缩小范围。

```python
def binary_search(items, target):
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 选择排序与冒泡排序

选择排序每轮从未排序部分选出最小元素，放到该部分开头。冒泡排序每轮比较相邻元素并交换，将较大元素逐步移向末尾。

```python
def selection_sort(items):
    for i in range(len(items) - 1):
        minimum = i
        for j in range(i + 1, len(items)):
            if items[j] < items[minimum]:
                minimum = j
        items[i], items[minimum] = items[minimum], items[i]

def bubble_sort(items):
    for end in range(len(items) - 1, 0, -1):
        changed = False
        for j in range(end):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                changed = True
        if not changed:
            break
```

一般题目可用 `sorted()`；需要按指定算法完成时再手写排序。

## 4.5 多维列表

二维列表用嵌套列表存储，通过 `matrix[row][column]` 访问。每行可以有不同长度，遍历时按实际行长度处理。

```python
matrix = [[0 for _ in range(3)] for _ in range(2)]
matrix[0][1] = 5
for row in matrix:
    print(*row)
```

不要使用 `[[0]*3]*2` 创建需要独立修改的行，因为它重复的是同一个内部列表的引用。

<div class="chapter-links"><a href="./chapter-03.html">← 第3章</a><a href="./chapter-05.html">第5章 →</a></div>
