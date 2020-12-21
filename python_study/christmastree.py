pinetree = '我是一颗松树'
def fun_christmastree():
    '''
    功能：一个梦
    无返回值
    '''
    pinetree = "挂上彩灯、礼物……我变成一颗圣诞树\n"
    print(pinetree)
#***************函数体外*****************
#判断是否以主程序的形式执行
if __name__ == "__main__":
    print("\n下雪了……\n")
    print("===========开始做梦……===========")
    fun_christmastree()
    print("===========梦醒了……===========")
    pinetree = "我身上落满雪花，" + pinetree
    print(pinetree)
