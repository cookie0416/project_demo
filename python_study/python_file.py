# 文件读取：1、打开文件，获取文件描述符 2、操作文件描述符（读|写） 3、关闭文件
# 注意：文件读写操作完成后，应该及时关闭

# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
# file:文件名字 mode：操作的参数，读r写w追加a，默认为r buffering：寄存区缓存，默认不需要设置 encoding：编码格式

# print(open('data.txt'))

# f = open('data.txt')

# print(f.readable())   #文件是否是可读的
# print(f.readlines())    #读取文件里所有的数据，转化成列表的形式，每一行末尾都有回车
# print(f.readline())        #按行读取，一行一行读
# print(f.readline())        #按行读取
# print(f.readline())        #按行读取

# f.close()

# with语句块，可以将文件打开之后，操作完毕，自动关闭这个文件

# with open('data.txt') as f:
#     print(f.readlines())


# with open('data.txt') as f:
#     while True:
#         line = f.readline()
#         if line:
#             print(line)
#         else:
#             break

# 正常的文本，可以使用rt，也就是默认格式
# 图片读取需要使用rb，读取二进制模式

with open('data.jpg', 'rb') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
