# 1 pyhon提高1

## 1.1 GIL

### 1.1.1 并发和并行

并发 : **交替**处理多个任务的能力

并行 : **同时**处理多个任务的能力

多任务: 提高运行速度,目的是达到并行的效果

vi - ON  同时打开多个程序

pass  实现略过的功能 需要占用资源

htop  查看进程使用情况

### 1.1.2 GIL 全局解释器锁

概念  每个线程在执行的过程都需要先获取GIL 保证同一时刻只有一个线程可以执行代码

原因 因为在CPYTHON解释器中难以移除GIL  源代码几千万行 改不了

使用方法 

1 科学计算 这类需要持续使用CPU的任务时候 单线程会比多线程快

2 网络通信 有IO阻塞的这类任务时 多线程会比单线程快好多

解决办法

1 更换解释器 换成JPYTHON这样的解释器

2 使用多进程完成多任务的处理

3 使用其他语言的调用 比如C语言

## 1.2 深拷贝 浅拷贝

### 1.2.1 引用

优点  省内存  省时间

缺点  没办法保证数据独立性

引用和浅拷贝的区别

```
a=10
b=a
id(a)=id(b)
a=10
b=copy.copy(a)
id(a)!=id(b)
```



### 1.2.2 深拷贝 浅拷贝 另行开辟一个内存空间

1. 没有嵌套的普通数据类型

   深拷贝和浅拷贝一样 保证数据独立性

2. 有嵌套的 复杂数据类型

   浅拷贝 仅拷贝最上面一层的内容 拷贝引用地址 没有数据独立性

   深拷贝 拷贝对象所有层次 另行开辟一个空间  保证数据独立性

3. 不可变类型 如元组 字符串

   浅拷贝只会关注最顶层的数据类型 直接引用 指向

   深拷贝 拷贝对象所有层次 只要有可变的 就另行开辟空间 保证数据独立性

4. 切片拷贝和字典拷贝

   一般都是浅拷贝 为了保证数据独立性 使用深拷贝

## 1.3 私有化

- xx: 公有变量
- _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
- __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
- __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:`__init__` , __ 不要自己发明这样的名字
- xx_:单后置下划线,用于避免与Python关键词的冲突

`d.__dict__`     查看名字重置后的

`a.__class__` 查看是什么创建的  一切皆对象 Type 是老大

- 父类中属性名为`__名字`的，子类不继承，子类不能访问
- 如果在子类中向`__名字`赋值，那么会在子类中定义的一个与父类相同名字的属性
- `_名`的变量、函数、类在使用`from xxx import *`时都不会被导入

## 1.4 import 导入模块

### 1.4.1 import 搜索路径

- 从上面列出的目录里依次查找要导入的模块文件
- '' 表示当前路径
- 列表中的路径的先后顺序代表了python解释器在搜索模块时的先后顺序

```
sys.path.append('/home/itcast/xxx')
sys.path.insert(0, '/home/itcast/xxx')  # 可以确保先搜索这个路径
```

### 1.4.2 重新导入模块

模块被导入后，`import module`不能重新导入模块，重新导入需用`reload`

### 1.4.3 多模块开发时的注意点

`from xxx import *`  拷贝xxx数据

`import xxx` 指向 引用地址

遇见多模块尽量使用import导入

## 1.5 再议 封装 继承 多态

封装 继承 多态是面向对象的3大特性

### 1.5.1 封装

把函数放入类中  代码划分清晰 变量管理 方便使用全局变量

### 1.5.2 继承

提高代码复用率  子类继承父类 子类使用父类的方法属性时  想要就要 不用就重写

### 1.5.3 多态

面试一般问的多态是其他语言的多态

1. 发生继承
2. 父类的方法被子类重写
3. 被重写的方法被调用

# 2 python提高2

## 2.1 多继承以及mro顺序

### 2.1.1 参数拆包组包

```
def a(*args,**kwargs):
	print(args)
	print(kwargs)
	
def b(*args,**kwargs)
	a(*args,**kwargs)
b(1,2,3,"name"="1","age"="2"
```

### 2.1.2 super继承父类

```
class Parent(object):
    def __init__(self, name):
        self.name = name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        self.age = age
        super().__init__(name,*args, **kwargs)
        print('Son1的init结束被调用')

class Son2(Parent):
    def __init__(self, name, gender,*args, **kwargs):
        self.gender = gender
        super().__init__(name,*args, **kwargs)
        print('Son2的init结束被调用')

class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


print(Grandson.__mro__)
g = Grandson("123", 18, "nan")
```

使用super会进入继承链mro顺序表中

```
(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)

```

总结

1. super().__init__相对于类名.__init__，在单继承上用法基本无差
2. 但在多继承上有区别，super方法能保证每个父类的方法只会执行一次，而使用类名的方法会导致方法被执行多次，具体看前面的输出结果
3. 多继承时，使用super方法，对父类的传参数，应该是由于python中super的算法导致的原因，必须把参数全部传递，否则会报错
4. 单继承时，使用super方法，则不能全部传递，只能传父类方法所需的参数，否则会报错
5. 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍, 而使用super方法，只需写一句话便执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因

## 2.2 再论静态方法和类方法

![内存](.\内存.png)

实例对象中默认有--class--记住创建的对象的地址

实例属性属于对象

​	实例属性在每个对象中都要保存一份

类属性属于类

​	类属性在内存中只保存一份

实例方法 静态方法和类方法都放在类的内存中

* 实例方法 由对象调用  self传递实例对象的地址
* 类方法 由类调用 cls传递类的地址
* 静态方法 由类调用 无默认参数

## 2.3 property属性

property更方便快捷的使用私有属性

定义的时候是方法,调用的时候用属性的方式调用

私有属性作用  增加逻辑判断 保证数据的正确性

```
class Good(object):
    def __init__(self):
        self.org_price = 1000
        self.discount = 0.7

    @property
    def price(self):
        val = self.org_price * self.discount
        return val

    @price.setter
    def price(self,new_val):
        self.org_price = new_val

    @price.deleter
    def price(self):
        del self.discount

g = Good()

print(g.price)

g.price = 2000
print(g.price)

del g.price
print(g.price)
```

类属性方式

```
# property属性的第二种定义方式:类属性定义方式
class Goods(object):

    def get_price(self):
        print("get price...")
        return 100

    def set_price(self, value):
        """必须两个参数"""
        print("set price...")
        print(value)

    def del_price(self):
        print("del price")

    price = property(get_price, set_price, del_price, "相关描述...")

obj = Goods()

obj.price  # 自动调用第一个参数中定义的方法：get_price
obj.price = "价格"  # 自动调用第二个参数中定义的方法：set_price方法，并将“价格”当作参数传入
desc = Goods.price.__doc__  # 自动获取第四个参数中设置的值："相关描述..."
print(desc)
del obj.price  # 自动调用第三个参数中定义的方法：del_price方法
```

property方法中有个四个参数

- 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
- 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
- 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
- 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息

固定格式

总结

- 定义property属性共有两种方式，分别是【装饰器】和【类属性】，而【装饰器】方式针对经典类和新式类又有所不同。
- 通过使用property属性，能够简化调用者在获取数据的流程

## 2.4 魔法属性

### 1. __doc__

- 表示类的描述信息

```
class Foo:
    """ 描述类信息，这是用于看片的神奇 """
    def func(self):
        pass

print(Foo.__doc__)
#输出：类的描述信息

```

### 2. __module__ 和 __class__

- __module__ 表示当前操作的对象在那个模块
- __class__ 表示当前操作的对象的类是什么

`test.py`

```
# -*- coding:utf-8 -*-

class Person(object):
    def __init__(self):
        self.name = 'laowang'

```

`main.py`

```
from test import Person

obj = Person()
print(obj.__module__)  # 输出 test 即：输出模块
print(obj.__class__)  # 输出 test.Person 即：输出类

```

### 3. __dict__

- 类或对象中的所有属性

类的实例属性属于对象；类中的类属性和方法等属于类，即：

```
class Province(object):

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')

# 获取类的属性，即：类属性、方法、
print(Province.__dict__)
# 输出：{'__dict__': <attribute '__dict__' of 'Province' objects>, '__module__': '__main__', 'country': 'China', '__doc__': None, '__weakref__': <attribute '__weakref__' of 'Province' objects>, 'func': <function Province.func at 0x101897950>, '__init__': <function Province.__init__ at 0x1018978c8>}

obj1 = Province('山东', 10000)
print(obj1.__dict__)
# 获取 对象obj1 的属性
# 输出：{'count': 10000, 'name': '山东'}

obj2 = Province('山西', 20000)
print(obj2.__dict__)
# 获取 对象obj2 的属性
# 输出：{'count': 20000, 'name': '山西'}

```

### 4. __init__

init 不是构造方法 构造方法是 1 创建空间 2 初始化数据

- 初始化方法，通过类创建对象时，自动触发执行

```
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 18


obj = Person('laowang')  # 自动执行类中的 __init__ 方法

```

### 5. __del__

- 当对象在内存中被释放时，自动触发执行。

注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，__del__的调用是由解释器在进行垃圾回收时自动触发执行的。

```
class Foo:
    def __del__(self):
        pass

```

### 6. __str__

- 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。

```
class Foo:
    def __str__(self):
        return 'laowang'


obj = Foo()
print(obj)
# 输出：laowang

```

### 7. __call__(了解)

- 对象后面加括号，触发执行。

注：__init__方法的执行是由创建对象触发的，即：`对象 = 类名()` ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：`对象()` 或者 `类()()`

```
class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')


obj = Foo()  # 执行 __init__
obj()  # 执行 __call__

```

### 8、__getitem__、__setitem__、__delitem__(了解)

- 用于索引操作，如字典。以上分别表示获取、设置、删除数据

```
# -*- coding:utf-8 -*-

class Foo(object):

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']      # 自动触发执行 __getitem__
obj['k2'] = 'laowang'   # 自动触发执行 __setitem__
del obj['k1']           # 自动触发执行 __delitem__

```

### 9、__getslice__、__setslice__、__delslice__(了解)

getslice 在python2.2之前才能使用

- 该三个方法用于分片操作，如：列表

```
# -*- coding:utf-8 -*-

class Foo(object):

    def __getslice__(self, i, j):
        print('__getslice__', i, j)

    def __setslice__(self, i, j, sequence):
        print('__setslice__', i, j)

    def __delslice__(self, i, j):
        print('__delslice__', i, j)

obj = Foo()

obj[-1:1]                   # 自动触发执行 __getslice__
obj[0:1] = [11,22,33,44]    # 自动触发执行 __setslice__
del obj[0:2]                # 自动触发执行 __delslice__
```

## 2.5 面向对象设计

- 继承 - 是基于Python中的属性查找(如X.name)
- 多态 - 在X.method方法中，method的意义取决于X的类型
- 封装 - 方法和运算符实现行为，数据隐藏默认是一种惯例
- 学习大牛代码方式 注释的重要性 利己利人

## 2.6 with 与"上下文管理器"

对于系统资源如文件 数据库连接 socket 而言 ,应用程序打开这些资源并执行完业务逻辑后,必须做的一件事就是要关闭(断开)该资源

一个进程中最多打开文件个数两千多个

2B青年

```
def m2():
    f = open("output.txt", "w")
    try:
        f.write("python之禅")
    except IOError:
        print("oops error")
    finally:
        f.close()
```

文艺青年

```
def m3():
    with open("output.txt", "w") as f:
        f.write("Python之禅")
```

上下文管理器

任何实现了 __enter__() 和 __exit__() 方法的对象都可称之为上下文管理器，上下文管理器对象可以使用 with 关键字。显然，文件（file）对象也实现了上下文管理器。

那么文件对象是如何实现这两个方法的呢？我们可以模拟实现一个自己的文件类，让该类实现 __enter__() 和 __exit__() 方法。

```
class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()

```

__enter__() 方法返回资源对象，这里就是你将要打开的那个文件对象，__exit__() 方法处理一些清除工作。

因为 File 类实现了上下文管理器，现在就可以使用 with 语句了。

```
with File('out.txt', 'w') as f:
    print("writing")
    f.write('hello, python')

```

这样，你就无需显示地调用 close 方法了，由系统自动去调用，哪怕中间遇到异常 close 方法也会被调用。

### 实现上下文管理器的另外方式

Python 还提供了一个 contextmanager 的装饰器，更进一步简化了上下文管理器的实现方式。通过 yield 将函数分割成两部分，yield 之前的语句在 __enter__ 方法中执行，yield 之后的语句在 __exit__ 方法中执行。紧跟在 yield 后面的值是函数的返回值。

```
from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

```

调用

```
with my_open('out.txt', 'w') as f:
    f.write("hello , the simplest context manager")

```

### 总结

Python 提供了 with 语法用于简化资源操作的后续清除操作，是 try/finally 的替代方法，实现原理建立在上下文管理器之上。此外，Python 还提供了一个 contextmanager 装饰器，更进一步简化上下管理器的实现方式。

# 3 闭包 装饰器

## 3.1 闭包

函数在内存中是有空间的 函数名就可以记录这个空间地址 函数名()代表执行这片空间代码

```
def func01():
    print("func01 is show")

print(func01)

func02 = func01

func02()

#func  0x11
def test(func):
    func()

# func01 0x11
test(func01)
```

函数参数 函数名当做参数使用

闭包 提高代码复用率,节省系统资源

格式 1 函数嵌套

​	 2 外层函数的返回值是内层函数的引用(地址/函数名)

​	 3 外层函数需要有参数(内层函数使用到)

def 外层函数(func):

​	def 内层函数():

​		pass

​	return 内层函数

一个函数使用另一个函数的局部变量

内层函数使用外层函数的局部变量

```
def func_out(func):
    a = 10

    def func_in():
        nonlocal a
        print(a)
        print(func)
        a = 1000

    return func_in


test = func_out(100)
test()

```

## 3.2装饰器

装饰器  是一种语法糖 在不改变源代码功能前提下 新增加的功能  遵循开放封闭原则 是种语法

写代码要遵循`开放封闭`原则，虽然在这个原则是用的面向对象开发，但是也适用于函数式编程，简单来说，它规定已经实现的功能代码不允许被修改，但可以被扩展，即：

- 封闭：已实现的功能代码块
- 开放：对扩展开发

```
def func_out(func):
    def func_in():
        print("验证")
        func()

    return func_in

@func_out   # login=func_out(login)
def login():
    print("登录")

login()
```

return返回值  就是程序中函数完成一件事情后,最后给调用者的结果

使用一个变量名接收函数的返回值

```
def func_out(func):
    def func_in():
        return func()

    return func_in


@func_out  # login=func_out(login)
def login():
    return 100


ret = login()
print(ret)

```

参数 *args  **kwargs

```
def func_out(func):
    def func_in(a):
        func(a)

    return func_in


@func_out  # login=func_out(login)
def login(a):
    print(a)


login(1)
```

既有返回值又有参数

```
def func_out(func):
    def func_in(*args, **kwargs):
        return func(*args, **kwargs)

    return func_in


@func_out
def login(*args, **kwargs):
    print(args)
    print(kwargs)
    return 100


ret = login(1, 2, 3, name="1", age="2")
print(ret)

```

类装饰器了解

```
class Foo(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("验证")
        self.func()


@Foo
def login():
    print("登录")


# login=Foo(login)
login()
```

秋裤大法

```
def func_out01(func01):
    print("func_out01 is show")

    def func_in01():
        print("func_in01 is show")
        func01()

    return func_in01


def func_out02(func02):
    print("func_out02 is show")

    def func_in02():
        print("func_in02 is show")
        func02()

    return func_in02


@func_out02
@func_out01
def test():
    print("test is show")


test()

```

![多个装饰器](.\多个装饰器.png)

![秋裤](.\秋裤.png)

装饰器功能

1. 引入日志
2. 函数执行时间统计
3. 执行函数前预备处理
4. 执行函数后清理功能
5. 权限校验等场景
6. 缓存