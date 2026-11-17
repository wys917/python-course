---
title: 第6章 函数
eyebrow: CHAPTER 06
chapter: true
code: 第6章
---

<div class="chapter-source">依据第6章课件（82 页）整理。</div>

## 6.1 函数的定义和调用

`def` 定义函数，调用时使用函数名和圆括号。定义时不执行函数体，调用时才执行。

```python
def square(x):
    return x * x

print(square(5))  # 25
```

函数名称也是对象的引用。`square` 是函数对象，`square(5)` 是调用结果。

## 6.2 函数参数

### 位置、关键字和默认值参数

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))                 # 9
print(power(3, 3))              # 27
print(power(exponent=3, base=2)) # 8
```

普通调用中，位置参数写在关键字参数之前；同一参数不能重复赋值。默认值在函数定义时计算一次，不宜用可变列表作为需要每次新建的默认值。

```python
def collect(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items
```

### 不定长参数与可变对象

```python
def total(*numbers):
    return sum(numbers)

def describe(**fields):
    return fields
```

`*args` 收集为元组，`**kwargs` 收集为字典。调用时 `f(*seq)` 展开位置参数，`f(**mapping)` 展开关键字参数。函数参数绑定到传入对象：对列表原地修改会影响调用方，给参数重新赋值则不会重新绑定调用方变量。

## 6.3 函数返回值

`return` 立即结束函数；没有 `return` 或只写 `return` 时返回 `None`。逗号分隔的多个返回值实际打包为元组。

```python
def bounds(items):
    return min(items), max(items)

low, high = bounds([3, 1, 8])
print(low, high)  # 1 8
```

`print()` 只负责输出，不等于把结果返回给调用者。

## 6.4 命名空间和作用域

名称通常按局部、外层函数、全局、内置（LEGB）的顺序查找。函数内赋值通常建立局部变量；读取前局部变量尚未绑定会引发 `UnboundLocalError`。

```python
count = 10

def next_count(value):
    return value + 1

count = next_count(count)
```

需要重绑定全局名称时用 `global`，重绑定外层函数名称时用 `nonlocal`。日常计算优先通过参数和返回值传递数据，便于检查。

## 6.5 递归

递归函数调用自身，必须有终止条件，并让问题规模逐步减小。

```python
def factorial(n):
    if n < 0:
        raise ValueError('n 必须非负')
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

没有终止条件或规模未减小会无限递归，最终达到解释器递归深度限制。递归不一定优于循环，应根据问题结构选择。

## 6.6 内置函数

| 函数 | 用途 | 示例 |
| --- | --- | --- |
| `sorted()` | 返回排序后的新列表 | `sorted(['aaa','b'], key=len)` |
| `map()` | 对各元素应用函数 | `list(map(int, ['3','4']))` |
| `zip()` | 按位置配对，默认在最短输入处结束 | `list(zip([1,2], ['a','b']))` |
| `all()` | 所有元素为真 | `all([True, 1])` |
| `any()` | 至少一个元素为真 | `any([0, 3])` |
| `eval()` | 求表达式值 | `eval('3+4')` |
| `exec()` | 执行语句代码 | 无有用返回值 |

`map()`、`zip()` 在 Python 3 中返回迭代器。`all([])` 为 `True`，`any([])` 为 `False`。`eval()`、`exec()` 会执行传入代码，不能处理不可信输入；普通数值输入使用 `int()`、`float()` 和 `split()`。

```python
records = [('Li', 85), ('Wang', 92)]
print(sorted(records, key=lambda item: item[1], reverse=True))
```

## 6.7 程序结构

模块是可导入的 Python 文件，包用于组织模块。`import math` 后使用 `math.sqrt()`；`from math import sqrt` 后直接使用 `sqrt()`。

```python
import sys

def main():
    print(sys.version_info.major)

if __name__ == '__main__':
    main()
```

`__name__` 判断可使模块被导入时不自动运行主流程。`sys.argv` 提供命令行参数，`sys.stdin`、`sys.stdout` 对应标准输入输出。

## 课件补充：回调函数

课件 6.8 补充了回调函数：将一个函数作为参数传入，由接收方在需要时调用。排序中的 `key` 就是这种用法。

```python
def apply_twice(function, value):
    return function(function(value))

print(apply_twice(lambda x: x + 1, 3))  # 5
```

<div class="chapter-links"><a href="./chapter-05.html">← 第5章</a><a href="./chapter-07.html">第7章 →</a></div>
