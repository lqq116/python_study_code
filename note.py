#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''退出交互窗口的时候：exit()'''
print('hello world')
#------------------------------------------------------
#1.利用input从窗口输入内容
name=input("input your name:")    #运行结果：input your name:（等待键盘输入）
print("my name is :",name)   #输出内容：my name is : cindy
print("1024*768=",1024*768)    #输出结果：1024*768= 786432


#-----------------------------------------------------
#2.数据类型
print("\\i\'m a girl")   #转义字符\ ：\i'm a girl
print(r"i'm a girl\n")   #使用r""的形式默认不转义：i'm a girl\n
print('''line1
line2
line3''')        #使用'''string'''的形式来保持字符串格式输出

True and False   #布尔值True/False之间进行逻辑运算

#------------------------------------------------------
#3.变量赋值：理解变量在内存中的表示
a='ABC'  #Python解释器干了两件事情：在内存中创建了一个'ABC'的字符串；在内存中创建了一个名为a的变量，并把它指向'ABC'。
b=a   #这个操作实际上是把变量b指向变量a所指向的数据（变量a变化不影响b的值）

#------------------------------------------------------
#4.运算符
print(4/2)  #/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：2.0
print(10/3)  #结果：3.3333333333333335
print(10//3) #//称为地板除，两个整数的除法仍然是整数:3
print(10%3)  #余数运算，得出余数


#------------------------------------------------------
#5.编码和解码：字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。
'''
ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节
本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
在最新的Python 3版本中，字符串是以Unicode编码的
'''
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord('A')  #获取单个字符的整数表示：65
ord('中')  #整数表示：20013
chr(65)          #获取整数的字符表示：'A'
chr(20013)     #字符表示：'中'

#多个字符组成的str和字节为单位的bytes转换(encode   decode)
'中文'.encode('utf-8')  #str编码为bytes：b'\xe4\xb8\xad\xe6\x96\x87'(前面的b表示为bytes类型)
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore')  #解码：'中文'

#计算str包含多少个字符
len('中文')   #输出字符串包含的字符个数：2
len('abc')  #输出3

#如果是编码后的字符，则输入包含的字节数
len('中文'.encode('utf-8'))   #输出字符串包含的字节数：6

#------------------------------------------------------
#6.格式化输出：
# 通过占位符%x
print("%4d-%04d" % (3,3))  #输出整数，有4位：   3-0003（第一个数前面有4个空格，第二个数用0填充）
print("%.4f" % 3.1415926)   #输出浮点数，小数点后4位：3.1416
print("age:%s,name:%s" % (30,'cindy'))  #不知道用什么的时候，用%s（将所有类型以str输出）
print("percent:%d%%" % 30)         #字符串里的%是普通字符（仅仅对于%）：percent:30%

s1=72
s2=85
r=s2-s1
perc=r/s1*100
print("Promotion percentage:%.1f%%" % perc)  #输出18.1%

#------------------------------------------------------
#7.列表和元组：list和tuple
#list：创建、访问、数组长度、修改值、插入值、列表末尾添加值、末尾删除值、特定位置删除值
list1=[0,1,2] #创建
print(list1[0])   #通过索引访问：0
print(len(list1))  #输出数组长度:3
list1[0]='00'  #修改值
print(list1[0])    
print(list1)  #输出：['00', 1, 2]

list1.insert(0,0)  #插入值
print(list1)   #输出值：[0, '00', 1, 2]

list1.append(3)  #末尾添加值
print(list1)  #输出：[0, '00', 1, 2, 3]

list1.pop()  #删除最后一个值：3
print(list1)  #输出：[0, '00', 1, 2]

list1.pop(1)  #删除指定位置的值
print(list1)  #输出：[0, 1, 2]

#tuple：一旦初始化就不能修改，创建、访问、长度、只有一个值的元组、元组中有一个值是list类型
t=(0,1,2)
t1=(1,)  #如果为t1=(1)，则会认为是整数1
print(t[0])  #通过索引访问值，输出：0
print(len(t))  #输出元组长度：3
t2=(0,[0,1])  #此时元组t2一个内存块，值（0,[0,1])一个内存块
t2[1][0]='00'  #修改的只是指向的值，并未修改tuple
print(t2)    #输出：(0, ['00', 1])

#------------------------------------------------------
#8.条件语句
#if-else：条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。
# #输入1.61/50  输出：“19.29：正常”
height=float(input("请输入你的身高："))
weight=float(input("请输入你的体重："))
bmi=weight/height**2
if bmi<18.5 and bmi>=10:
    print("%.2f:过轻" % bmi)
elif bmi>=18.5 and bmi<25:
    print("%.2f:正常" % bmi)
elif bmi>=25 and bmi<28:
    print("过重")
elif bmi>=28 and bmi<32:
    print("肥胖")
elif bmi>=32:
    print("严重肥胖")
else:
    print("there is something wrong!")


#------------------------------------------------------
#9.循环
#for x in x:....
sum=0
for i in range(101):  #range()生成一个整数序列
    sum+=i
print(sum)       #输出：5050

#while循环
names=['cindy','lily','lucy']
i=0
while i<3:
    print("hello,%s\n" % names[i])
    i+=1

#break:提前退出整个循环
#continue：退出最近的一层循环
for i in range(11):
    if i==3:
        continue  #0-10中除了3外都打印（跳出该层循环）
        #break    #打印出0,1,2之后便退出循环

    print(i)

#------------------------------------------------------
#10.字典和集合：dict和set
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#dict：创建、访问、添加值、删除key-value
d={'cindy':30,'lily':20}  #初始化创建字典
print(d['cindy'])  #通过key访问value
d['lucy']=10    #加入值后输出：{'cindy': 30, 'lily': 20, 'lucy': 10}
print(d)

#判断key是否存在
'elsa' in d    #交互环境输出：False
d.get('elsa','not exist') #交互环境输出：如果存在，则输出对应的value，否则输出'not exist'（输出内容可以自己定义）

#删除key-value
d.pop('cindy')  #必须写入key，否则报错

#字典的key值必须为不可变对象：这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了

#set：集合创建、访问、添加、删除
s=set([0,1,2])
print(s)  #输出：{0, 1, 2}
s.add(3)  #添加到集合中：无序的，如果添加相同值，则会被过滤：{0, 1, 2, 3}
print(s)

s.remove(3)  #删除掉一个值：{0, 1, 2}


#set：数学意义上的交集、并集等操作
s1=set([0,1,2,3,4])
print(s&s1)  #计算交集：{0, 1, 2}
print(s | s1)  #计算并集：{0,1,2,3,4}

#------------------------------------------------------
#11.函数：一种最基本的代码抽象方式

#调用函数：需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数
#查看函数介绍：可以在交互式命令行通过help(abs)查看abs函数的帮助信息“help(abs)”

#内置的常见函数
abs(-1)   #只需要一个参数：返回绝对值
max(1,2,3)  #可以任意多个参数：返回最大的值

isinstance('a',(int,float))   #数据类型检查可以用内置函数isinstance()实现：因为'a'为str，所以返回False
isinstance('a',(str))    #此时返回True

#数据类型转换
int(2.252) #转化为整数：只取整数部分，不会四舍五入
float(3)  #转化为浮点数：3.0
str(123)  #转化为字符串：'123'
bool(1)  #转化为布尔值：非0为True，0（空值等）为False
hex(2)   #将整数转为十六进制表示的字符串：'0x2'

#定义函数：定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_name(x):    #函数要素：def、函数名称、()、:
    x=input("input your name:")   
    print("my name is:%s" % x)   #函数体：函数完成的功能
    #pass                       #如果暂时无操作，可以使用pass作为占位符（否则无操作的函数可能会报错）
    return x,x      #！请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回(可返回多个值)

#空函数：如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass  #pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来

#函数的参数：调用者只需要知道如何传递正确的参数，以及函数返回什么样的值即可，内部逻辑无需了解
#参数类型：必填参数、默认参数、可变参数、关键字参数

#可变参数（*argument）：允许传入0个或任意个参数，这些可变参数调用时自动组装为一个tuple。
def calc(x,*numbers):   #必填参数，可变参数：可以使任意多个参数（相当于numbers接受到一个tuple）
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum+x

result=calc(1,1,2)   #除了必填参数取1，后面的‘1,2’都放入可变参数numbers
print(result)  #输出6

#关键字参数（**argument）：允许传入0个或任意多个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict
def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)
#调用函数，输出：name: cindy age: 30 other: {'city': 'shanghai', 'job': 'student'}
person("cindy",30,city="shanghai",job="student")

#递归函数：函数在内部调用自身本身，则这个函数就是递归函数
#递归函数需要注意防止栈溢出：逻辑简单清晰，但是过深的调用会导致栈溢出
'''
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
RuntimeError: maximum recursion depth exceeded in comparison(最大递归深度超过了)
'''
#------------------------------------------------------
#12.迭代：通过for循环遍历称为迭代（iteration）
#Python通过'for ... in'来完成，而其他语言是通过下标完成：for(i=0;i<10;i++)
#判断是否为可迭代对象：通过collections模块的Iterable来判断
from collections import Iterable
isinstance('abc',Iterable)  #字符串是否可迭代：True
isinstance([1,2,3],Iterable)  #数组是否可迭代：True
isinstance(123,Iterable)  #整数是否可迭代：False


#迭代器：Iterator(迭代器)
#可用于for的都是Iterable类型，可以用于next()的是Iterator
from collections import Iterator
isinstance([1,2],Iterator)  #False:数组是可迭代的，但不是迭代器类型（迭代器是一个数据流）
isinstance(iter([1,2]),Iterator)  #用函数iter()将数组转化为Iterator类型
list1=[0,1,2]
list101=iter(list1)  #将Iterable转化为Iterator  
type(list101)  #输出：<class 'list_iterator'>
list102=list(list101)  #将Iterator转化为Iterable（列表）
type(list102)   #输出：<class 'list'>

#------------------------------------------------------
#13.列表生成式：内置的创建list的生成式
#执行顺序：最前面写操作，后面需要判断的条件依次排列
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]  #将L1中的字符串值变为小写输出
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

#------------------------------------------------------
#14.生成器：通过列表生成式直接生成列表，如果值较多，会浪费内存；
#          通过生成器（generator）一边循环一边计算生成列表中值
#将列表生成式中的[]换成()即可：g=(x*x for x in range(10))
L1 = ['Hello', 'World', 18, 'Apple', None]
g = (s.lower() for s in L1 if isinstance(s,str))  #创建生成器
#访问生成器中内容
for i in g:
    print(i)

#------------------------------------------------------
#15.函数式编程：把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
def add(x,y,f):  #函数名字也是变量，也可以赋值给变量
    return f(x)+f(y)
print(add(-5,6,abs))    #输出11


#函数式编程/高阶函数/map()
#map()接受两个参数：一个函数，一个Iterable（将传入的函数依次作用在序列的每个元素，并把结果作为新的Iterator返回）
r=map(abs,[-1,1])
print(r)          #输出：<map object at 0x0000000002EDE358>
print(type(r))     #输出：<class 'map'>
r1=list(r)       
print(r1)         #输出：[1, 1]
#reduce()函数：函数作用在一个序列上（序列中的两个数相加结果，继续和下一个参数相加....），求出和
from functools import reduce
def add(x, y):
    return x + y

result=reduce(add,[1,3,5])
print(result)       #输出结果：9


#filter()从一个序列中筛选出符合条件的元素：filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n%2==1   #判断奇数、偶数：奇数输出True  偶数输出False

list1=list(filter(is_odd,[0,1,2,3,4]))  #筛选出返回True的值
print(list1)  #输出：[1, 3]

#sorted()排序算法：通过key赋值内容进行自定义排序
a=sorted(['ab','ac','Ab'],key=str.lower,reverse=True)  #首先对比第一个，一样的话，再对比第二个
print(a)  #输出：['ac', 'ab', 'Ab']


#匿名函数：只有一个表达式，不用谢return，返回值就是该表达式的结果
# 不用担心函数名称重复（lambda x:x*x）
L=list(filter(lambda n:n%2==1,[0,1,2,3]))

#装饰器（decorator）：在代码运行期间动态增加功能的方式
# （比如在执行函数前后自动打印日志，但不希望修改函数的定义）
#好复杂，看不懂！！：
#定义装饰器
import functools

def log(text):  #带参数的装饰器
    def decorator(func):

        #把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
        @functools.wraps(func)    
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#编写好后，借助"Python的@语法，把decorator置于函数的定义处"
@log
def now():
    print('2015-3-25')



#------------------------------------------------------
#16.模块：为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，采用这种组织代码的方式
#在Python中，一个.py文件就称之为一个模块（module）
#自定义模块、Python内置模块、第三方模块
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
'''
请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的
否则，Python就把这个目录当成普通目录，而不是一个包。
__init__.py可以是空文件，也可以有Python代码
因为__init__.py本身就是一个模块，而它的模块名就是mycompany(包名)
'''

#使用模块：用sys模块为例
#下面是模块的模板：不同内容开始前用空行隔开
#--------------------------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'    #模块中的第一个字符串都被视为文档注释

__author__='cindy'     #内置变量，开源的话告知作者

import sys              #导入模块

def test():             #模块真正代码部分
    print("绑定到实例中")

if __name__=='__main__':  
    test()
#------------------------------------

#安装第三方模块：
#a.通过包管理工具pip完成(pip install package_name)
#b.安装常用模块：Anaconda，内置了许多非常有用的第三方库（直接下载GUI安装包即可）

#模块搜索路径
#默认搜索当前目录、所有已安装的内置模块、第三方库（搜索路径存放在sys.path中）
#添加自己的搜索目录：便于用的时候可以搜索到位置，避免报错
#a.import sys      sys.path.append('绝对地址')
#b.设置环境变量PYTHONPATH：添加自己的模块路径到此


#-------------------------------------------------------------------------
#17.面向对象编程（OOP：object oriented programming）
#把对象作为程序的基本单元，一个对象包含：数据和操作数据的函数（属性和功能）
#设计思想是：抽象出class，根据class创建instance（实例）
#三大特点：封装、继承、多态
#创建class:可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.__score=score  #私有变量，不可外部访问（通过实例修改什么的）

    def get_score(self):   #类中函数与普通函数区别是：一定要包含self，且放在第一个
        print('%s:%s' %(self.name,self.__score))

    def update_score(self,score):
        self.__score=score

#实例一个对象
student1=Student('cindy',80)
#访问限制，因为__score是私有变量，只能通过类中变量修改
student1.update_score(100)
student1.get_score()


#继承：继承父类的特性
#多态：一个实例可以是多个类型（属于父类，也属于自己类）

#获取对象信息：获取类型、有哪些方法
type(student1)              #判断对象类型：<class '__main__.Student'>
isinstance(student1,Student)  #输出True
dir(student1)  #获取对象所有属性和方法

#实例属性和类属性:类定义中的属性、实例化时，自己添加自己的属性
class Student1(object):
    count=0    #类属性：属于该类的属性都可以访问
    def __init__(self,name):
        self.name=name

#实例一个对象
student1=Student1('cindy')
student1.score=100   #实例化后定义自己的属性：实例属性score
print(student1.score)


#给实例增加实例函数：from types import MethodType
from types import MethodType

def test1(self,name1):        #因为是给类实例增加函数，需要有self变量
    self.name1=name1      #一定要先通过赋值创建变量，后面才可调用
    print("绑定到类的实例中:%s" % self.name1)

student1.test1=MethodType(test1,student1)   #给实例绑定一个方法
student1.test1('cindy')    #输出（放在Python中可执行成功）：绑定到类的实例中:cindy




#-------------------------------------------------------------------------
#18.面向对象高级编程

#使用@property装饰器：负责把一个方法变成属性调用
#@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Student2(object):

    @property                             #把get方法变为属性
    def birth(self):
        return self._birth           #！！！注意：self后的变量一定跟get函数名称一样，且加上"_",否则会报“递归错误”

    @birth.setter      #@property本身又创建了一个@score.setter：负责将setter方法变成属性
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth     #定义只读属性，只定义getter方法，不定义setter方法

#多重继承：一个子类就可以同时获得多个父类的所有功能（基于该中形式的设计叫做MixIn）


#-------------------------------------------------------------------------
#19.错误、调试和测试

#错误分类
#a.程序编写错误：必须修复
#b.用户输入错误：不合设定规则（给出合理提示）
#c.无法预测的错误：硬件、软件、网络等（称为异常，必须处理）

#Python内置一套异常处理机制，来帮助处理错误
#a.返回错误码：一般出错返回-1（众多-1返回，需要回溯查找哪里报错）
#b.使用内置的try...except...finally...错误处理机制
#不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了（main函数，被调用函数）
#！！！出错的时候，一定要分析错误的调用栈信息（报错的一系列信息，最终输出错误的是本质），才能定位错误的位置。
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:   #try子句出错才执行
    print('except:', e)
else:
    print('no error !')         #无错误时执行
finally:
    print('finally...')             #始终执行
print('END')
#记录错误：
# 不捕获的话，最终解释器打印出错误堆栈，但是程序也结束了。
#         最好自己捕获，打印出错误堆栈并分析原因，同时，让程序继续执行
#Python内置的logging模块可以非常容易地记录错误信息：
import logging         #通过配置：logging可把错误记录到日志文件，方便时候排查

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:    #自己捕获，打印出错误，且程序会继续执行，不会直接退出
        logging.exception(e)

main()
print('END')
#抛出错误：raise


#调试:
# 跟踪程序的执行（Python的pdb可以让我们以单步方式执行代码）
#a.用print函数打印出可能出错的内容（不推荐：后续还要删除）
#b.asset断言：断言失败，则会抛出AssertionError
#c.logging可以将错误输出到文件！！终极武器！！！
import logging
logging.basicConfig(level=logging.WARNING)  #指定信息的级别：debug，info，warning，error
s = '0'
n = int(s)
logging.info('n = %d' % n)   #输出：INFO:root:n = 0（上面信息级别设置为WARNING后，该句不起作用）
print(10 / n)
#d.使用pdb（Python的调试器）：让程序单步方式运行，随时查看运行状态
#命令窗口执行代码的命令：$ python -m pdb err.py  （输入命令1查看代码；输入n单步执行代码；输入‘p 变量名’查看变量；输入q结束调试，退出）
#e.支持调试功能的IDE（visual studio code）

#测试：测试驱动开发（TDD）
#单元测试：对一个模块、一个函数或者一个类来进行正确性校验的测试工作
'''
比如对函数abs()，我们可以编写出以下几个测试用例：

1.输入正数，比如1、1.2、0.99，期待返回值与输入相同；

2.输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；

3.输入0，期待返回0；

4.输入非数值类型，比如None、[]、{}，期待抛出TypeError。

把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest  #a.导入单元测试框架

from mydict import Dict  #b.导入要测试的模块

#e.开始写测试用例集合
class TestAbs(unittest.TestCase):  #c.导入框架unittest
    #d.初始化环境和清理环境：每个用例的开始和结束都会执行一遍
    def setUp(self):  
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_Positive(self):
        self.assertEqual(abs(1), 1)
        self.assertEqual(abs(1.2),1.2)

    def test_Negative(self):
        self.assertEqual(abs(-1), 1)
        self.assertEqual(abs(-1.2),1.2)

    def test_Zero(self):
        self.assertEqual(abs(0), 0)

    '''
    #下面这个直接出发错误的不会写
    def test_Notn(self):
        with self.assertRaises(TypeError):
            print(abs(*))
            print(abs(a))
    '''

#f.执行用例集合
if __name__ == '__main__':
    unittest.main()

#文档测试：'''括住部分，是对函数的解释（告知期望输入、输出），严格按照交互模式输出内容展示
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

#-------------------------------------------------------------------------
#20.IO编程
'''
IO在计算机中指Input/Output，也就是输入和输出
由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，
涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口
IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动

CPU和内存速度远远高于外设速度，在IO编程中，则存在速度严重不匹配的问题
a.CPU等待IO执行结果的模式称为“同步IO”
b.CPU不等待IO执行结果，同时去干别的事，称为“异步IO”
'''
#------------------
#文件的读写：
# 在磁盘上读写文件的功能都是由操作系统提供的
#打开一个文本
f=open('D:/学习/python学习/python_study_code/test.txt','a')   #填写文件地址、打开模式'r/w/a'(记得一个)
f.write('this is a test:我\n')    #文档中增加内容
f.close()                #操作结束记得关闭：会占用资源；而且可能只保存在了内存缓存中，并未写入磁盘
#读取文件内容
f=open('D:/学习/python学习/python_study_code/test.txt','r')
content=f.read()  #read(n):读取n字符             readline()：读取一行  readlines():读取所有行，保存为列表
print(content)

f.close()
print(f.closed)    #判断是否关闭状态：True
#简化方法（为了避免忘记关闭文件导致耗费资源或内容未保存）
with open('path','r') as f:
    print(f.read())     #不必调用f.close()，自动调用


#StringIO和BytesIO:在内存中读写内容
#StringIO:内存中读写str
#BytesIO：内存中读写字节
from io import StringIO
from io import BytesIO
f=StringIO("在内存中直接写入内容")
f.write('cindy')
print(f.getvalue(),f.read(5))

f1=BytesIO()
f1.write('写入字节'.encode('utf-8'))
print(f1.getvalue(),f1.read(5))

#-----------------------
#操作文件和目录：
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
#查看、创建和删除目录
import os
#nowpath=os.path.abspath('.')    #获取当前绝对地址
#os.path.join('D:/学习/python学习/python_study_code','newdir')
os.mkdir('D:/学习/python学习/python_study_code/newdir')   #创建目录
#os.path.join(nowpath,'newdir')  #合成新地址：按照系统正确处理不同的路径分隔符
#os.path.split('D:/学习/python学习/python_study_code/newdir')  ：拆分路径
#os.mkdir(nowpath+'/newdir')  #创建目录
os.rmdir('D:/学习/python学习/python_study_code/newdir')  #删除目录
os.rename('test.txt','test.py')  #重命名文件
os.remove('test.py')   #删除文件

[x for x in os.listdir('.') if os.path.isdir(x)]#过滤当前目录下的文件夹：['newdir', '__pycache__']
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']#过滤当前目录下的Python文件
#------------------------
#序列化：
##将变量从内存中变成可存储或传输的过程：序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
#反序列化：将序列化的内容重新读到内存里
#  程序运行过程中，所有变量都是在内存中，一旦程序结束，内存将被收回，如果修改没及时保存到磁盘，则恢复
#a.利用pickle序列化
import pickle  #适宜保存不重要的数据
d=dict(name='cindy',age=30)
dd=pickle.dumps(d)  #序列化为bytes
print(dd)
dd1=pickle.loads(dd)  #反序列化出对象
print(dd1)

#方法2：直接写入文件中
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f=open('dump.txt','rb')
ddd=pickle.load(f)   #反序列化对象
f.close()
print(ddd)

#b.序列化为XML和JSON：适应不同编程语言之间传递对象，更符合Web标准
#Python内置的json模块提供了完善的JSON格式的转化（JSON是标准的JavaScript对象）
#序列化为JSON
import json 
d1=dict(name='cindy',age=30)
str01=json.dumps(d1)   #序列化为json对象
print(str01,type(str01))    #输出：{"name": "cindy", "age": 30} <class 'str'>

json01=json.loads(str01)   #反序列化为json
print(json01,type(json01))  #输出：{'name': 'cindy', 'age': 30} <class 'dict'>

#-------------------------------------------------------------------------
#21.进程和线程
'''
对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个Word就启动了一个Word进程。

有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情:在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。

由于每个进程至少要干一件事，所以，一个进程至少有一个线程。
当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。
当然，真正地同时执行多线程需要多核CPU才可能实现。

线程是最小的执行单元，而进程由至少一个线程组成。
如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。
'''

#a.多进程（multiprocessing）
import os
print('process(%s) start...' % os.getpid())
pid=os.fork()  #Windows系统不支持fork，只在Unix和Mac系统
#有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务
if pid==0:
    print('i am child process (%s) and my parent is %s' % (os.getpid(),os.getppid()))
else:
    print('i (%s) just created a child process (%s)' % (os.getpid(),pid))


#进程较少时候:Process模块
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    '''
    创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    用start()方法启动，这样创建进程比fork()还要简单。
    join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    '''
    p=Process(target=run_proc,args=('test',))  #并未运行执行参数？？？
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')


#有批量进程时候：用进程池的方式创建子进程，Pool模块
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

'''
Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：

p = Pool(5),就可以同时跑5个进程。
由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
'''

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)   #进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


#进程间的通信：Queue、Pipes等多种方式来交换数据
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


#b.多线程
import time, threading

# 新线程执行的代码:Python的线程是真正的Posix Thread，而不是模拟出来的线程（使用threading模块）
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
#threading模块有个current_thread()函数，它永远返回当前线程的实例。
#主线程实例的名字叫MainThread
def loop():
    print('thread %s is running...' % threading.current_thread().name) 
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n)) #子线程
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)  #主线程名称MainThread
t = threading.Thread(target=loop, name='LoopThread')  #创建thread实例
t.start()  #调用线程开始执行
t.join()  #等待线程自动结束
print('thread %s ended.' % threading.current_thread().name)

#c.lock
'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
#使用锁：一个线程在操作某个对象时，给该对象上锁（此时，别的线程只能等待，锁释放后才可操作该对象）
'''
def change_it(n):
    pass

balance = 0
lock = threading.Lock()  #创建锁

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()  #获得锁：才能获得执行资格
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()  #释放锁：否则会成为死线程


#d.多核CPU：一个死循环线程会100%占用一个CPU
#要想把N核CPU核心全部跑满，必须启动N个死循环线程（Python因为有GIL锁，无法实现全部占用）
'''
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
'''

#d.一个ThreadLocal变量虽然是全局变量
#创建的全局变量为一个dict，而绑定的属性则是局部变量
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


#e.分布式进程:multiprocessing模块的子模块managers支持把多进程分配到多态机器上（调度者+任务执行者）
'''
在Thread和Process中，应当优选Process，因为Process更稳定，
而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上
'''
#源码：https://github.com/michaelliao/learn-python3/blob/master/samples/multitask/task_master.py
#源码:https://github.com/michaelliao/learn-python3/blob/master/samples/multitask/task_worker.py


#---------------------------------------------------------------------------------------
#22.正则表达式：用来匹配字符串的强有力的武器
#定义一个规则（正则表达式）；去匹配用户输入，判断是否合法

#a.正则基础
'''
精确匹配字符：\d(匹配一个数字)  \w（匹配一个字母或数字） .（匹配任意一个字符）
匹配变长的字符： *（任意多个字符） +（至少一个字符）  ？（0或1个字符）  {n}（n个字符）  {n,m}（n-m个字符） 
更精确第匹配： A|B(匹配A或B)   ^x（表示行以x开头）  x$（表示以x结尾）  
'''

#b.re模块：包含所有正则表达式的功能（加上r，不必考虑转移问题）
import re
#匹配
re.match(r'regular expression','string')  #判断正则表达式是否匹配（输入的string是否匹配：返回Match对象或None）

#切分字符串
re.split(r'[\s\,\;]+','a,b c;d')#切分字符串(以正则表达式切分string,返回数组：['a', 'b', 'c', 'd'])

#分组：用()表示的就是要提取的分组group(首先判断有符合规则的字符串，后面才能在字符串中查找提取内容)
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')     #分别定义了两个组
print(m.group(0))   #输出：010-12345（group(0)永远是原始字符串）
print(m.group(1))   #输出：010（#group(1)、group(2)……表示第1、2、……个子串）
print(m.group(2))   #输出：12345

#贪婪匹配：正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
re.match(r'^(\d+)(0*)$', '102300').groups()  #输出：('102300', '') 由于第一个贪婪匹配将字符串全部匹配了
#非贪婪匹配模式：提取的分组后面直接加上？（找到第一个匹配的则结束）
re.match(r'^(\d+?)(0*)$', '102300').groups()  #输出：('1023', '00')

#编译：正则使用时，re内部做两件事（编译正则表达式；用编译后的表达式去匹配字符串）
#预编译
re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')  #预编译生成Regular Expression对象
re_telephone.match('010-12345').groups()  #('010', '12345')



#---------------------------------------------------------------------------------------
#常见内建模块：无需额外安装和配置，即可直接使用。
#a.处理日期和时间的标准库：datetime（需要的时候在查看）
#b.集合模块，提供很多有用的集合类：collections（需要时候查看）
#c.省略几个（需要时查找）
#d.提供操作URL的功能：urllib
#  get请求
'''
    request.urlopen(url,data=None,timeout=...)
    #Open the URL url, which can be either a string or a Request object
'''
from urllib import request

#模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
req = request.Request('http://www.douban.com/')  #创建request对象
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen('http://www.douban.com/') as f:   #请求内容和响应内容都包含在f中
    data=f.read()   
    print('status:',f.status,f.reason)   #获取响应返回码和说明
    for k,v in f.getheaders():          #获取响应头
        print('%s:%s' % (k,v))
    print('data:',data.decode('utf-8'))   #对内容进行解码

#  post请求：只需要把参数data以bytes形式传入
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
print(login_data)    #编码为username=xxx&password=xxx这种样式传入URL
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
#  Handler:如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理

#e.XML
'''
操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

正常情况下，优先考虑SAX，因为DOM实在太占内存。

在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

举个例子，当SAX解析器读到一个节点时：

<a href="/">python</a>
会产生3个事件：

start_element事件，在读取<a href="/">时；

char_data事件，在读取python时；

end_element事件，在读取</a>时。
'''
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)












































    












    







