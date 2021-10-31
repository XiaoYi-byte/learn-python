# -*- coding: UTF-8 -*-

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 遍历枚举类型
for name, member in Month.__members__.items():
    print(name, '---------', member, '----------', member.value)

# 直接引用一个常量
print('\n', Month.Jan)


def triangles():  # 杨辉三角形
    L = [1]
    while True:
        yield L
        L.append(0)
        print(L[-1])
        L = [L[i - 1] + L[i] for i in range(len(L))]


n = 0
for t in triangles():  # 直接修改函数名即可运行
    print(t)
    n = n + 1
    if n == 10:
        break


class MyClass:
    _var1 = 'abc'

    def __init__(self):
        self.__var1 = '123'

# https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
    @classmethod
    def method(cls):
        print(cls.__var1)


print(MyClass._var1)


# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attrs):
    """
      Return a class object, with the list of its attribute turned
      into uppercase.
    """
    # pick up any attribute that doesn't start with '__' and uppercase it
    uppercase_attrs = {
        attr if attr.startswith("__") else attr.upper(): v
        for attr, v in future_class_attrs.items()
    }

    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attrs)


__metaclass__ = upper_attr  # this will affect all classes in the module


class Foo():  # global __metaclass__ won't work with "object" though
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    bar = 'bip'
