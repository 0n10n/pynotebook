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

相关源代码：

- [str_format.py](./str_format.py)