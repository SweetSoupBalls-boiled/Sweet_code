# 1 正则表达式

## 1.1 概述

正则表达式,又称规则表达式,通常用来检索 替换那些符合某个模式(规则)的文本

正则表达式是对字符串操作的一种逻辑公式,就是用事先定义好的一些特定字符 及这些特定字符的组合,组成一个"规则字符串"  过滤逻辑

给定一个正则表达式和另一个字符串, 可以达到如下的目的

* 给定的字符串是否符合正则表达式的 匹配 "过滤逻辑"
* 通过正则表达式 从文本字符串中获取我们想要的特定部分("过滤")

## 1.2 re模块

导入 re模块 `import re`

`result = re.match(正则表达式,要匹配的字符串)`  match 匹配

`result.group()  ` 提取数据  group 组的 一群

## 1.3 匹配单个字符

| 字符   | 功能                    |
| ---- | --------------------- |
| .    | 匹配任意1个字符（除了\n）        |
| [ ]  | 匹配[ ]中列举的字符           |
| \d   | 匹配数字，即0-9             |
| \D   | 匹配非数字，即不是数字           |
| \s   | 匹配空白，即空格，tab键         |
| \S   | 匹配非空白                 |
| \w   | 匹配单词字符，即a-z、A-Z、0-9、_ |
| \W   | 匹配非单词字符               |

### 1.3.1 点

. : 任意字符 除了\n

```
import re

ret = re.match(".","M")
print(ret.group())

```

### 1.3.2 []

[ ] :取的是里面内容任一的字符 只占一个

示例代码：

```
import re

# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h","hello Python") 
print(ret.group())

# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H","Hello Python") 
print(ret.group())

# 大小写h都可以的情况
ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[hH]","Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python","Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]Hello Python","7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python","7Hello Python")
print(ret.group())

ret = re.match("[0-35-9]Hello Python","7Hello Python")
print(ret.group())

# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python","4Hello Python")
# print(ret.group())

```

### 1.3.3 \d

\d : 数字0-9

```
ret = re.match("嫦娥\d号","嫦娥2号发射成功") 
print(ret.group())
```

## 1.4 匹配多个字符

| 字符     | 功能                          |
| ------ | --------------------------- |
| *      | 匹配前一个字符出现0次或者无限次，即可有可无      |
| +      | 匹配前一个字符出现1次或者无限次，即至少有1次     |
| ?      | 匹配前一个字符出现1次或者0次，即要么有1次，要么没有 |
| {m}    | 匹配前一个字符出现m次                 |
| {m, n} | 匹配前一个字符出现从m到n次              |

### 1.4.1 匹配多个字符

```
import re

# 需求:匹配出,一个字符串第一个字母为大小字符,后面都是小写字母并且这些小写字母可有可无

# buf = ["a", "A", "AAA", "Aa", "Aabc", "A12345", "a12344", "1111", "__", "$"]

# for tmp in buf:
#     result = re.match(r"\D\d{3}|[A-Z][a-z]", tmp)
#     if result:
#         print(result.group(), "符合要求")
#     else:
#         print(tmp, "不符合要求")

ret = re.match("[1-9]?\d$|100","00")
print(ret.group())
```

### 1.4.2 匹配变量名是否有效

```
import re

# 匹配变量名是否有效
# 不能以数字开头,以后的组合为字母,数字,下划线

buf = ["a", "A", "AAA", "Aa", "Aabc", "A12345", "a12344", "1111", "__", "$"]

for tmp in buf:
    # [^a]取反,只要不是a都可以
    # ^a: 以a开头
    result = re.match(r"[A-Za-z_]\w*$", tmp)
    if result:
        print(result.group(), "符合要求")
    else:
        print(tmp, "不符合要求")
```

### 1.4.3 匹配数字

```
import re

# 需求: 匹配出数字0-99 不能以0开头除个位数
buf = ["23", "09", "2", "234"]

for tmp in buf:
    # print(tmp)
    # result = re.match(r"\d{1,2}$", tmp)
    result = re.match(r"[1-9]?\d$", tmp)
    if result:
        print(result.group(), "符合要求")
    else:
        print(tmp, "不符合要求")
```

### 1.4.4 匹配多少位数密码

```
import re

ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
print(ret.group())
```

### 1.4.5 匹配邮箱

```
import re

# 需求: 匹配163邮箱

buf = ["mike@163.com", "lily@163.comheihei", ".com.mikejiang@qq.com", "aabbcc@163acom"]

for tmp in buf:
    result = re.match(r"\w{4,15}@163\.com$", tmp)
    if result:
        print(result.group(), "符合要求")
    else:
        print(tmp, "不符合要求")


```

## 1.5 匹配开头结尾

| 字符   | 功能      |
| ---- | ------- |
| ^    | 匹配字符串开头 |
| $    | 匹配字符串结尾 |

```
import re

# 需求: 匹配163, qq, 126邮箱

buf = ["mike@163.com", "lily@163.comheihei", ".com.mikejiang@qq.com", "aabbcc@163acom", "asfdgsd@126.com"]

for tmp in buf:
    result = re.match(r"\w{4,15}@(163|qq|126)\.com$", tmp)
    if result:
        print(result.group(), "符合要求")
    else:
        print(tmp, "不符合要求")


```

## 1.6 匹配分组

| 字符         | 功能                 |
| ---------- | ------------------ |
| \|         | 匹配左右任意一个表达式        |
| (ab)       | 将括号中字符作为一个分组       |
| \num       | 引用分组num匹配到的字符串     |
| (?P<name>) | 分组起别名              |
| (?P=name)  | 引用别名为name分组匹配到的字符串 |

```
import re

# buf = re.match(r"<(\w*)><(\w*)>.*</\2></\1>","<a><b>hello</b></a>").group()
buf = re.match(r"<(?P<as>\w*)><(?P<bs>\w*)>.*</(?P=bs)></(?P=as)>","<a><b>hello</b></a>").group()
print(buf)
```

## 1.7 re模块的高级用法

### 1.7.1 search 搜寻

```
import re


# result = re.match(r"\d+", "99")
# result = re.match(r"\d+", "asdfss99")
# 默认是从开头找起 只要一个一个对 匹配
# result = re.search(r"\d+","agdfg666") 搜寻
result = re.search(r"\d+","agdfg666, dgfgf77")
# search 会全部找一遍 只要找到合适的 只能提取一次
print(result.group())
```

### 1.7.2 findall 发现所有

```
import re

# findall匹配所有的 把所有符合条件的以列表返回,无需调用group 发现所有
result = re.findall("\d+", "fsdfd=23,asdf=45,dfas=354")
print(result)
```

### 1.7.3 sub替换

```
import re

# re.sub(r"正则表达式","替换的内容","匹配的字符串")
# 和findall一样,找所有的 多一个功能,替换
# 返回后的结果 替换后的字符串
result = re.sub(r"\d+", "66","fdfg=5454,afgf=65,fsd=45")
print(result)
```

```
import re

# re.sub(r"正则表达式",函数名字,"匹配的字符串")
# 函数必须有参数,就是一个正则对象
# 函数的返回值,字符串,就是替换的内容

def change(tmp):
    print(tmp.group())  # 取出匹配后的内容
    a = int(tmp.group()) + 10  # 字符串转换为整型 +10

    # str(a)整型转换为字符串
    return str(a)

# 返回的结果, 替换后的字符串
result = re.sub(r"\d+", change, "python=3, af=23, d=5")
print(result)
```

### 1.7.4 职位信息提取

```
import re

buf = """
<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
"""
# 画个标签，就不可以了
# result = re.sub(r"<div>|<p>|</p>|</div>|&nbsp|<br>|\s", "", buf)
# result = re.sub(r"</?\w*>|&nbsp;|\s", "", buf)
# 只要不是右尖括号，就要
result = re.sub(r"<[^>]*>|&nbsp;", "", buf)
print(result)  # 把所有不是中文的取出来用空替换


```

### 1.7.5 split 分离

```
import re

#以:或者空格切割
ret = re.split(r":| ","info:mike 18 shenzhen")
print(ret)
```



## 1.8 贪婪和非贪婪

Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；非贪婪则相反，总是尝试匹配尽可能少的字符。

**在"\*", "?", "+", "{m,n}"后面加上？，使贪婪变成非贪婪。**

## 1.9 r 的作用

```
import re
# r raw 原生字符串
# 不加r的话2个代表1个\
path = "C:\\Users\\superman\\Desktop\\code\\python\\11期\\9day"

# 2个代表1个，4个才能匹配上上面的2个
# result = re.match("C:\\\\Users\\\\superman\\\\Desktop\\\\code\\\\python\\\\11期\\\\9day", path)
result = re.match(r"C:\\Users\\superman\\Desktop\\code\\python\\11期\\9day", path)
print(result.group())
```

