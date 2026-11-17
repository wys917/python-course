---
title: 第8章 类和对象
eyebrow: CHAPTER 08
chapter: true
code: 第8章
---

<div class="chapter-source">依据第8章课件（45 页）整理。理论范围包含 8.1、8.2，不含 8.3、8.4、8.5；编程考试范围为第 1–6 章。</div>

## 8.1 类和对象的概念

类定义一类对象的数据和行为；对象是类的实例。列表、字符串、字典等内置类型也是类，`append()`、`lower()` 等是对象提供的方法。

```python
items = [1, 2]
items.append(3)
print(type(items))  # <class 'list'>
```

访问成员使用点号：`对象.属性`、`对象.方法()`。取得方法引用与调用方法不同，调用需要圆括号。

## 8.2 类和对象的创建

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def passed(self):
        return self.score >= 60

student = Student('Li', 85)
print(student.name)      # Li
print(student.passed())  # True
```

- `class` 定义类，类体使用缩进。
- 调用类创建实例；`__init__` 初始化已创建的实例，通常不返回值。
- `self` 是实例方法第一个参数的惯用名称，代表当前实例。
- `student.passed()` 会自动把 `student` 作为 `self` 传入。
- `student.score = 90` 修改该实例属性，不会修改所有其他实例。

### 实例属性与类属性

```python
class Course:
    language = 'Python'  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

a = Course('A')
b = Course('B')
a.language = 'Python 3'
print(b.language)  # Python
```

从实例读取属性时通常先查实例，再查类。给 `a.language` 赋值会建立实例属性，不能理解为必然修改类属性。可变类属性可能被多个实例共享，实例独立数据应在 `__init__` 中创建。

## 8.3 使用对象编写程序

本节不在所给考试范围内。课件通过 BMI 和向量类说明将数据与操作封装为对象的方式。可先确定对象保存哪些数据，再定义相应方法，避免把所有处理都放进初始化方法。

## 8.4 封装

本节不在所给考试范围内。封装把相关数据和操作组织到同一个类中。

- `_name` 是内部使用约定，不会阻止外部访问。
- `__name` 在类内部触发名称改写，主要用于减少子类命名冲突，并非绝对不可访问。
- `@classmethod` 的首个参数通常为 `cls`，操作类相关状态。
- `@staticmethod` 不自动接收实例或类参数。

## 8.5 继承和多态

本节不在所给考试范围内。子类可继承并重写父类行为，`super()` 可调用继承体系中的方法。

```python
class Animal:
    def speak(self):
        return '...'

class Cat(Animal):
    def speak(self):
        return 'meow'

for animal in [Animal(), Cat()]:
    print(animal.speak())
```

相同的方法调用可产生不同对象的行为，这体现了多态。`__add__` 等特殊方法可以定义运算符行为，具体实现需符合类型的含义。

<div class="chapter-links"><a href="./chapter-07.html">← 第7章</a><a href="./">全部章节 →</a></div>
