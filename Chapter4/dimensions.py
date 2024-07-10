# 元组 是一个不可改变的列表 相当于列表的常量
# 元组不可以改变某个值，但是可以重新定义整个元组 达到改变的目的。

foods = ('ice','p','v','h','o')

for value in foods:
    print(value)

foods[0] = 'a'