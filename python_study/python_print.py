#字面量插值：将变量和常量通过一种方式组合起来，变成我们想要的字符串的格式
#一、格式化输出——%d的用法,此方法比较麻烦，必须指定类型且类型不能出错
print("my name is hogwarts")

name = "hogwarts"
print('my name is %s'%name)

age = 3
print('my name is %s,my age is %d'%(name,age))

print('my name is %s,my age is %d,num is %f'%(name,age,3.1415))

print('my name is %s,my age is %d,num is %.2f'%(name,age,3.1415))

#二、string.format()方法,不需要指定类型，可以引用多次
print('my name is {},age is {}'.format(name,age))
print('my name is {0},age is {1}'.format(name,age))
print('my name is {1},age is {0}'.format(name,age))
print('my name is {1},age is {0}，{0}{1}'.format(name,age))

list1 = [1,2,3]
dic1 = {'name':'tom','gender':'male'}
print('my list is {0},dict is {1}'.format(list1,dic1))

#想将列表的内容一个一个传进去时，需要通过*星号对列表或字典解包
namelist = ['lili','tom','jerry']
print('our name : {}、{}、{}'.format(*namelist))
print('my name is {name},gender is {gender}'.format(**dic1))

#三、F-strings,字符串格式化机制，最推荐，3.6版本以上支持,不需要解包，使用方式最简洁，推荐
print(f'my name is {name}\n,age is {age},my list is {list1[0]},my dict is {dic1["gender"]}')

#大括号里可以是表达式或函数，但是大括号里不支持转义，如果需要在大括号里加冒号或斜杠，则需要加上括号括起来
print(f'result is {(lambda x:x+1)(2)}')
print(f'my age is {11}')
