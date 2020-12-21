# nickname = "哈哈哈"
# print(type(nickname))

# nickname = 1024
# print(type(nickname))

# a = 10
# b = 6
# print(a,b)

# fp = open(r'D:\test\mot.txt','a+')
# print("命运给予我们的不是失望之酒，而是机会之杯。",file=fp)
# fp.close()

# money = input("欢迎使用充值业务，请输入充值金额：")
# print("充值成功，您本次充值:"+money+"元")

# height1 = float(input("请输入父亲的身高："))
# height2 = float(input("请输入母亲的身高："))
# height = (height1+height2)*0.54
# print("预测儿子的身高为："+str(height))


#if语句

# print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
# number = int(input("请输入您认为符合的数："))
# if number%3 == 2 and number%5 == 3 and number%7 == 2:
#     print(number,"符合条件")

#if...else...语句

# a = -9
# if a > 0:
#     b = a
# else:
#     b = -a
# print(b)


# print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
# number = int(input("请输入您认为符合的数："))
# if number%3 == 2 and number%5 == 3 and number%7 == 2:
#     print(number,"符合条件")
# else:
#     print(number, "不符合条件")

# a = 10
# if a >= 0:
#     if a > 0:
#         print("a大于0")
#     else:
#         print("a等于0")
# else:
#     print("a小于0")


#if...elif...else语句

# print("在古希腊神话中，玫瑰集美丽与爱情于一身，所以人们常常用玫瑰来表达爱意。")
# print("但是，不同数量的玫瑰代表的含义是不同的。\n")
# # 获取用户输入的数量，并转换成整型
# number = int(input("输入您想送几朵玫瑰花，小默会告诉您含义："))
# if number == 1:
#     print("1朵：你是我的唯一！")
# elif number == 3:
#     print("3朵：我爱你！")
# elif number == 10:
#     print("10朵：十全十美")
# elif number == 99:
#     print("99朵：天长地久")
# else:
#     print("小默也不知道了")

#if语句的嵌套

# print("为了您和他人的安全，严禁酒驾。")
# proof = int(input("请输入每100毫升血液的酒精含量："))
# if proof < 20:
#     print("您还不构成饮酒行为。")
# else:
#     if proof < 80:
#         print("已经达到酒后驾驶标准，请不要开车！")
#     else:
#         print("已经达到醉酒驾驶标准，千万不要开车！")

# 条件表达式

# a = 10
# b = 20
# r =a if a > b else b
# print(r)

#while循环

# print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
# none = True
# number = 0
# while none:
#     number +=1
#     if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
#         print(number)
#         none = False


#for 循环

# print("计算1+2+...+100的结果为：")
# result = 0
# for i in range(101):
#     result +=i
# print(result)

# print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
# for number in range(1000):
#     if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
#         print(number)

# for i in range(1,10,2):
#     print(i,end = ' ')

# string = '元气满满'
# for i in string:
#     print(i)

#在python3.x中，使用print（）函数时，如果想让print语句输出的内容在一行上显示，不能直接加逗号，需要加上“，end=‘分隔符’，并且该分隔符为一个空格
#如果在连续输出时不需要用分隔符隔开，也可以不加分隔符

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(j)+"x"+str(i)+"="+str(i*j)+"\t",end='')
#     print('')                                               #换行

# print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
# for number in range(1000):
#     if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
#         print(number)
#         break

# total = 99
# for number in range(1,100):
#     if number % 7 == 0:
#         continue
#     else:
#         string = str(number)
#         if string.endswith('7'):        #判断是否以数字7结尾
#             continue
#     total -=1
# print("从1到99共拍腿次数：",total)


# total = 0
# for number in range(1,100):
#     if number % 7 == 0:
#         total += 1
#     else:
#         string = str(number)
#         if string.endswith('7'):        #判断是否以数字7结尾
#             total += 1
# print("从1到99共拍腿次数：",total)

#序列——列表

# list1 = list(range(10,20,2))
# print(list1)

# team = [1,3,4]
# del team

# import datetime                                                 #导入日期时间类
# #定义一个列表
# mot = ["今天星期一：\n坚持下去不是因为我很坚强，而是因为我别无选择。",
#        "今天星期二：\n含泪播种的人一定能笑着收货。",
#        "今天星期三：\n做对的事比把事情做对重要。",
#        "今天星期四：\n命运给予我们的不是失望之酒，而是机会之杯。",
#        "今天星期五：\n不要等到明天，明天太遥远，今天就行动。",
#        "今天星期六：\n求知若饥，虚心若愚。",
#        "今天星期日：\n成功将属于那些从不说“不可能”的人。"]
# day=datetime.datetime.now().weekday()      #获取当前星期
# print(day)
# print(mot[day])
# print(mot[6])

# phone = ["联想","小米"]
# phone.append("iPhone")
# print(phone)

# verse = ["长亭外","古道边","芳草碧连天"]
# verse[2] = "思乡"
# print(verse)

# verse = ["长亭外","古道边","芳草碧连天"]
# del verse[2]
# print(verse)

# verse = ["长亭外","古道边","芳草碧连天"]
# verse.remove("长亭外")
# print(verse)

# grade = [89,97,33,98,89,77]
# print("原列表",grade)
# grade.sort()                    #进行升序排列
# print("升序",grade)
# grade.sort(reverse=True)       #进行降序排列
# print("降序",grade)

# grade = [89,97,33,98,89,77]
# grade_as = sorted(grade)
# print("升序",grade_as)
# grade_des = sorted(grade,reverse=True)
# print("降序",grade_des)
# print("原序列",grade)

# import random
# randomnumber = [random.randint(10,100) for i in range(10)]
# print("生成的随机数为：",randomnumber)

# price = [100,30,20,800]
# sale = [int(x*0.5) for x in price]
# print(sale)


# price = [100,30,20,800]
# sale = [x for x in price if x>50]
# print(sale)

#集合的交集、并集和差集运算

# python = set(['张三','李四','王五','lana'])
# c = set(['张三','李四','王五','lisa','lily'])
# print('交集运算：',python & c)
# print('并集运算：',python | c)
# print('差集运算：',python - c)
# print('差集运算：',c - python)


# str1 = '人，a'
# length = len(str1)
# print(length)


#不区分大小写验证会员名是否唯一

# username1 = '|MINGUI|jgdjb|hhhhs|jsbij|JDHsj|'
# username2 = username1.lower()
# regname1 = input('请输入要注册的会员名称：')
# regname2 = '|'+regname1.lower()+'|'
# if regname2 in username2:
#     print("会员名已经存在")
# else:
#     print('会员名可以注册')


import math
#以货币的形式显示
# print('1251+3950的结果是（以货币的形式显示）：￥{:,.2f}元'.format(1251+3950))


# def everyday_tips():
#     import datetime                                                 #导入日期时间类
#     #定义一个列表
#     mot = ["今天星期一：\n坚持下去不是因为我很坚强，而是因为我别无选择。",
#            "今天星期二：\n含泪播种的人一定能笑着收货。",
#            "今天星期三：\n做对的事比把事情做对重要。",
#            "今天星期四：\n命运给予我们的不是失望之酒，而是机会之杯。",
#            "今天星期五：\n不要等到明天，明天太遥远，今天就行动。",
#            "今天星期六：\n求知若饥，虚心若愚。",
#            "今天星期日：\n成功将属于那些从不说“不可能”的人。"]
#     day =datetime.datetime.now().weekday()                     #获取当前星期
#     print(mot[day])
# #*****调用函数****#
# everyday_tips()

#定义函数
# def demo(obj):
#     print("原值:",obj)
#     obj += obj
# #调用函数
# print("========值传递========")
# mot = "奔跑"
# print("函数调用前：",mot)
# demo(mot)
# print("函数调用后：",mot)
# print("========引用传递=======")
# list = ['ayi','啊二']
# print("函数调用前：",list)
# demo(list)
# print("函数调用后：",list)

#计算BMI指数
# def fun_bmi(person,height,weight):
#     print(person+"的身高："+str(height)+"\t"+person+"的体重："+str(weight))
#     bmi=weight/(height*height)
#     print(person+"的BMI指数为："+str(bmi))
# fun_bmi("boy",1.83,65)
# fun_bmi("girl",1.63,53)
# fun_bmi(person="uuu",weight=60,height=1.63)

# def fun_bmi(height,weight,person="路人"):
#     print(person+"的身高："+str(height)+"\t"+person+"的体重："+str(weight))
#     bmi=weight/(height*height)
#     print(person+"的BMI指数为："+str(bmi))
# fun_bmi(1.83,65,"jgg")
# fun_bmi(1.83,65)

# message = "坚持下去不是因为我很坚强，而是因为我别无选择。"
# print("函数体外：message=",message)
# def f_demo():
#     global message
#     message = "含泪播种的人一定能笑着收获。"
#     print("函数体内：message=",message)
# f_demo()
# print("函数体外：message=",message)


# import bmi
# bmi.fun_bmi("yiyi",1.75,60)


# import bmi as m
# m.fun_bmi("yiyi",1.75,60)

# import sys
# print(sys.path)

# import christmastree
# print("全局变量的值为："+christmastree.pinetree)

# import random
# print(random.randint(1,100))


#类

# class Geese:
#     "大雁类"
#     def __init__(self):                 #构造方法
#         print("我是大雁类！")
# wildgoose = Geese()                     #创造大雁类实例
# print(wildgoose)


# class Geese:
#     "大雁类"
#     def __init__(self,beak,wing,claw):                 #构造方法
#         print("我是大雁类！我有以下特征：")
#         print(beak)
#         print(wing)
#         print(claw)
#     def fly(self,state):                              #定义飞行方法
#         print(state)
# "*******************调用方法*******************"
# beak_1 = "长喙"
# wing_1 = "大翅膀"
# claw_1 = "小爪子"
# wildgoose = Geese(beak_1,wing_1,claw_1)               #创建大雁类实例
# wildgoose.fly("结伴飞行")

#冒泡排序
# def mp_sort(ssq):
#     for i in range(len(ssq)-1):
#         for j in range(len(ssq)-1-i):
#             if ssq[j] > ssq[j+1]:
#                 ssq[j],ssq[j+1] = ssq[j+1],ssq[j]
#     print(ssq)
# list1 = [10,9,8,7,6,0]
# mp_sort(list1)

# def findtg(nums,target):
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 print(nums[i],nums[j])
#                 print(str(nums[i])+'+'+str(nums[j])+'='+str(target))
# nums1 = [2,7,11,15]
# target1 = 9
# findtg(nums1,target1)

# def removeduplicates(nums):
#     n = len(set(nums))
#     i = 0
#     while i < n - 1:
#         if nums[i] == nums[i + 1]:
#             temp = nums[i + 1]
#             nums[i + 1:len(nums) - 1] = nums[i + 2:]
#             nums[-1] = temp
#             print(i)
#             # continue
#         else:
#             i += 1
#         # print(nums[0:len(set(nums))])
#         print(nums)
#     return n

def removeduplicates(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] == nums [i]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
            j += 1
    print(i+1)
    print(nums)
    print(nums[:i+1])
    return i+1
removeduplicates(nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
           记录【今天之前买入的最小值】
           计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
           比较【每天的最大获利】，取最大值即可
        '''
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            profit = price - minprice
            maxprofit = max(maxprofit, profit)
        return maxprofit












