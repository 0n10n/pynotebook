age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

##可以不用数字编号
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

##还可以对参数做命名，更好懂易记
print('- {name!r} was {age} years old when he wrote this book'.format(name=name, age=age))
print('- Why is {name1!s} playing with that python?'.format(name1=name))

##Python3.6开始的 "f-strings"命名方式，在整个字符串前名加了'f'标记：
print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string

##格式化的本质，是把参数的值，按照指定的规范，替换进字符串里。更复杂的写法如下。
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))