---
title: 第5章 集合和字典
eyebrow: CHAPTER 05
chapter: true
code: 第5章
---

<div class="chapter-source">依据第5章课件（62 页）整理。</div>

## 5.1 集合

集合 `set` 保存不重复的可哈希元素，不提供索引或切片，也不承诺遍历顺序。空集合用 `set()`，`{}` 是空字典。

```python
a = {1, 2, 3}
b = {3, 4}
a.add(5)
a.discard(9)   # 不存在时不报错
print(3 in a)  # True
```

`remove(x)` 在元素不存在时报错；`discard(x)` 不报错。列表、字典和集合本身不可作为集合元素；只含可哈希元素的元组可以。

| 运算 | 含义 |
| --- | --- |
| `a & b` | 交集 |
| `a \| b` | 并集 |
| `a - b` | 差集，仅在 a 中 |
| `a ^ b` | 对称差，在两者之一中 |
| `a <= b` | a 是否为 b 的子集 |
| `a < b` | a 是否为 b 的真子集 |

```python
print({1, 2} & {2, 3})  # {2}
print({1, 2} - {2, 3})  # {1}
print(len(set('banana')))  # 3
```

集合适合去重和成员判断；需要保留首次出现顺序时，单独使用列表记录输出顺序。

## 5.2 字典

字典 `dict` 保存键值映射，键唯一且必须可哈希；值可以是任意对象。同一键再次赋值会覆盖原值。Python 3.7 起字典保持插入顺序，但不会自动按键排序。

```python
scores = {'Li': 90, 'Wang': 85}
scores['Chen'] = 92
scores['Li'] = 95
print(scores.get('Zhao', 0))  # 0
```

`scores[key]` 在键不存在时引发 `KeyError`；`get(key, default)` 返回默认值。`key in scores` 判断的是键，不是值。

```python
for name, score in scores.items():
    print(name, score)

print(list(scores.keys()))
print(list(scores.values()))
scores.pop('Wang')
```

`keys()`、`values()`、`items()` 返回视图。遍历期间不要改变字典大小；若要删除，先收集要删的键或遍历副本。

## 5.3 嵌套结构

```python
students = {
    '001': {'name': 'Li', 'scores': [90, 85]},
    '002': {'name': 'Wang', 'scores': [88, 92]},
}
print(students['001']['scores'][0])  # 90
```

先确定外层结构，再逐层取值。字典和列表的浅拷贝都不会递归复制内部对象；需要完全独立的嵌套副本时可用 `copy.deepcopy()`。

## 5.4 集合和字典的应用实例

### 字符计数

```python
counts = {}
for char in 'banana':
    counts[char] = counts.get(char, 0) + 1
print(counts)  # {'b': 1, 'a': 3, 'n': 2}
```

### 保持顺序去重

```python
seen = set()
result = []
for value in [3, 1, 3, 2]:
    if value not in seen:
        seen.add(value)
        result.append(value)
print(result)  # [3, 1, 2]
```

集合负责查重，列表负责保存首次出现的顺序。对字符串做不区分大小写的查重时，可将 `char.lower()` 用作查重键，原字符用于输出。

<div class="chapter-links"><a href="./chapter-04.html">← 第4章</a><a href="./chapter-06.html">第6章 →</a></div>
