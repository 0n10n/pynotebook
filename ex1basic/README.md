## 笔记

- 多行字符串：

```python
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
```

- 字符串不可被改变

单引号和双引号同样用法，没有差异。没有char类型。

- 格式化

  ```python
  age = 20
  name = 'Swaroop'
  
  print('{0} was {1} years old when he wrote this book'.format(name, age))
  print('Why is {0} playing with that python?'.format(name))
  ```

关于格式化更多细节： https://docs.python.org/3/library/string.html#formatspec 

 https://docs.python.org/zh-cn/3/library/string.html#formatspec 

相关源代码：[str_format.py](./str_format.py)

- print()默认后面自动换行，如果不需要换行，可以这么做：

```python
print('a', end='')
print('b', end='')
```

如果希望拼接空格，可以写成：

```python
print('a', end=' ')
print('b', end=' ')
print('c')
```

- 转义

`\` 字符作为转义符；` 'What\'s your name?' `

中间换行：`'This is the first line\nThis is the second line' `

行末的 `\`，代表不换行，接着一行写。

```python
"This is the first sentence. \
This is the second sentence."
```

- Raw string：字符串前名加 `r`

```python
r"Newlines are indicated by \n"
```

