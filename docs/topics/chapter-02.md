---
title: 第2章 用Python语言编写程序
eyebrow: CHAPTER 02
chapter: true
code: 第2章
---

<div class="chapter-source">依据第2章课件（79 页）整理。2.7 位运算不在所给考试范围内，仍保留知识说明。</div>

## 2.1 数字类型

| 类型 | 示例 | 要点 |
| --- | --- | --- |
| 整数 int | `12`、`-7`、`0xA` | 可表示大整数，实际受内存限制 |
| 浮点数 float | `3.14`、`2.3e2` | 科学计数法的指数必须是整数；计算可能有舍入误差 |
| 复数 complex | `3+4j`、`1J` | `j` 或 `J` 表示虚数单位 |

```python
print(10 / 4)          # 2.5
print(10 // 4)         # 2
print(-3 // 2)         # -2
print(2 ** 3)          # 8
print(2.1 - 2.0 == .1) # False
z = 3 + 4j
print(z.real, z.imag, abs(z))  # 3.0 4.0 5.0
```

`/` 是普通除法；`//` 向下取整；`%` 求余；`**` 乘方。整除只要有浮点操作数，结果通常也是浮点数。乘方优先于左侧单目负号，且连续乘方从右向左结合：`-2**4 == -16`，`3**2**3 == 6561`。

### math 库

```python
import math
print(math.sqrt(9))    # 3.0
print(math.ceil(2.1))  # 3
print(math.floor(2.9)) # 2
print(math.sin(math.radians(30)))
```

`math` 的三角函数使用弧度。`import math as t` 后通过 `t.sqrt()` 访问；若此前未定义 `math`，不能再直接使用名称 `math`。

## 2.2 字符串类型

字符串使用单引号、双引号或三引号，属于不可变序列。Python 没有独立的 `char` 类型，单个字符也是长度为 1 的字符串。

```python
print('Py' + 'thon')   # Python
print('23' * 3)        # 232323
print('smith\\exam1\\test.txt')
print(r'smith\exam1\test.txt')
```

`\n` 为换行、`\t` 为制表符、`\\` 为真实反斜杠。`'age'+23` 有合法语法，但运行时因类型不匹配引发 `TypeError`。Python 字符串不以 `\0` 标志结束。

## 2.3 布尔类型、空值和列表类型

`True`、`False` 的首字母必须大写；`None` 表示空值。`False`、`None`、数值 0 和空容器在条件中为假。

```python
print(int(True))       # 1
print(bool([]))        # False
print(bool(None))      # False
print(3 and 0 and 5)   # 0
print(0 or 'default')  # default
```

`not` 返回布尔值；`and`、`or` 短路求值，返回参与运算的操作数，不保证结果为 `bool`。优先级为比较运算、`not`、`and`、`or`。

列表用 `[]` 表示，有序、可变，允许混合类型：`[123, 'abc', True]`。

## 2.4 内置转换函数

| 函数 | 示例结果 | 注意 |
| --- | --- | --- |
| `int()` | `int('20',16)` → `32` | 指定基数时参数必须是字符串等受支持文本类型 |
| `float()` | `float('10.0')` → `10.0` | 读取小数 |
| `str()` | `str(23)` → `'23'` | 数值转文本 |
| `bool()` | `bool('False')` → `True` | 非空字符串为真 |
| `list()` | `list('ab')` → `['a','b']` | 拆分可迭代对象 |
| `chr()` / `ord()` | `chr(65)` → `'A'` | 字符与码点转换 |

## 2.5 语句

### 赋值与拆包

```python
a, b = 3, 4
a, b = b, a
x = y = 4
t = 1
t, a = 2, t + 1
print(a)  # 2
```

先计算整个右侧，再从左到右赋值。`a,b=34` 不能把整数拆成数字；`a,b='3 4'` 因右侧有 3 个字符而失败。`i*=3+5` 等价于 `i=i*(3+5)`。

### if 与 for

```python
x = -2
if x > 0:
    result = x
elif x == 0:
    result = 0
else:
    result = -x

for i in range(1, 4):
    print(i)
```

冒号后使用一致的缩进。`range(start, stop, step)` 不含终点，`range(10,0,-2)` 产生 `10,8,6,4,2`。Python 的 `++i` 不是自增运算，而是两次一元正号。

### 列表推导式

```python
squares = [i * i for i in range(1, 6)]
evens = [i for i in range(10) if i % 2 == 0]
```

## 2.6 格式化输出

```python
print('{:8s}'.format('this'))   # 字符串默认左对齐
print('{:8d}'.format(1234))     # 数值默认右对齐
print(f'{14.345:08.2f}')        # 00014.35
print('{1}+{0}={2}'.format(2, 3, 5))  # 3+2=5
```

`<` 左对齐、`>` 右对齐、`^` 居中，宽度是最小宽度。`d` 为十进制整数，`s` 为字符串，`.2f` 保留两位小数。`0>8s` 表示字符串左侧补零到宽度 8。格式化小数的结果也可能受浮点表示影响，不能机械地按十进制“逢 5 必进”判断。

## 2.7 位运算

本节不在所给考试范围内。`&` 按位与、`|` 按位或、`^` 按位异或、`~` 按位取反，`<<` 和 `>>` 为移位。

```python
print(5 & 3, 5 | 3, 5 ^ 3)  # 1 7 6
print(~9)                   # -10
```

负数位运算可按无限符号扩展的补码理解，`~x == -x-1`。`^` 不表示乘方，乘方使用 `**`。

<div class="chapter-links"><a href="../assignments/homework-02.html">第2章作业 →</a><a href="../quizzes/quiz-01.html">第一次上机小测 →</a><a href="./chapter-03.html">第3章 →</a></div>
