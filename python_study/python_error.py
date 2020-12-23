# python 错误与异常
# 错误与异常的区别：异常可以被捕获和处理
# 常见的异常类型：除零异常，名称异常，索引异常，键异常，值异常，属性异常等

# 相除——除零异常
# def div(a,b):
#     return a / b
#
# print(div(1, 0))

# 索引异常——IndexError
list1 = [0, 1, 2]

# print(list1[3])

# 键异常——KeyError
dic1 = {'name': 'tom'}

# print(dic1['age'])

# 值异常——ValueError：类型转换时
num = 'aaa'


# print(int(num))

# 捕获异常操作
# def div(a,b):
#     return a / b
#
# try:
#     print(div(1,0))
# except:
#     print("这里有一个异常")

# 可以专门去捕获异常，对异常进行收集
# def div(a,b):
#     return a / b
#
# try:
#     print(div(1,0))
# except ZeroDivisionError as e:
#     print(e)
#     print("这里有一个异常")

# def div(a,b):
#     return a / b
#
# try:
#     print(div(1,1))
#     list1 = [0, 1, 2]
#     print(list1[3])
# except Exception as e:
#     print(e)
#     print("这里有一个异常")

# finally,程序会从try开始一条一条执行，遇到异常，后面的语句就不执行了，会接着去执行except里面的语句，捕获完异常之后，会执行finally
# 如果执行try的时候没有出现异常，except部分就不执行了，也会接着执行finally
# finally最终都会被执行，无论有异常还是没有异常
# 通常在执行文件操作时，会把close（）放在finally语句块里

# def div(a,b):
#     return a / b
#
# try:
#     print(div(1,1))
#     list1 = [0, 1, 2]
#     print(list1[3])
#
# except Exception as e:
#     print(e)
#     print("这里有一个异常")
#
# finally:
#     print("finally最终都会被执行，无论有异常还是没有异常")

# except是发生异常的时候执行的，else是没有异常的时候执行的，两者互斥，try...except...else用的时候比较少，一般只用try...except
# try：执行代码，遇异常会中断；except：发生异常时执行的代码；else：没有异常时执行的代码；finally：不管有没有异常都会执行的代码

# def div(a,b):
#     return a / b
#
# try:
#     print(div(1,1))
#     list1 = [0, 1, 2]
#     print(list1[0])
#
# except Exception as e:
#     print(e)
#     print("这里有一个异常")
#
# else:
#     print("没有异常的时候执行")
#
# finally:
#     print("finally最终都会被执行，无论有异常还是没有异常")

# 使用raise抛出异常——手动触发异常:一般是开发的时候用
# def set_age(num):
#     if num <= 0 or num >200:
#         raise ValueError(f"值错误：{num}")
#     else:
#         print(f"设置的年龄为{num}")
#
# set_age(80)
# set_age(-1)

# 自定义异常
class MyException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常：{msg}")


def set_age(num):
    if num <= 0 or num > 200:
        raise MyException(f"值错误：{num}")
    else:
        print(f"设置的年龄为{num}")


set_age(-1)
