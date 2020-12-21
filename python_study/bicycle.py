class Bicycle:
    def run(self,km):
        #字面量插值传递km参数，km是一个变量
        print(f"用脚一共骑行了{km}km，累")

#再写一个电动自行车类EBicycle继承自Bicycle
class Ebicycle(Bicycle):
    #类属性：类体内，方法之外
    #volume = 1000
    #构造方法
    #添加电池电量valume属性,valume只在init里面可用，想要在整个类里面都能用，需要在前面加self.
    def __init__(self,valume):
        #实例属性：类体内，方法内，并且以“self.变量名”的方式去定义的变量
        self.valume =   valume
        #普通属性：类体内，方法内，局部变量(只在当前方法内有用）
        #valume = valume

    def fill_charge(self,vol):

        print(f"电动车已充电{vol}度")
        print(f"充完电之后还有{vol+self.valume}")

    def run(self,km):
        #有电的时候能骑到的公里数
        e_km = self.valume*10
        print("电动车的最大公里数",e_km)
        #当电量耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
        if km <= e_km:
            print(f"用电一共骑了{km}km")
        else:
            print(f"用电一共骑了{e_km}km")
            #第一种调用父类的方法，和普通实例化类，调用方法相同
            # bike = Bicycle()
            # bike.run(km - e_km)
            #第二种调用父类的方法
            super().run(km - e_km)
            #不调用父类输出的情况
            # print(f"用脚骑了{km - e_km}km")



#实例化子类
#继承之后，子类就可以调用父类的属性和方法
#构造方法的参数，需要在实例化类的时候传递
ebike = Ebicycle(100)
#当子类中有和父类重名的方法或属性，首先选择的是子类的
ebike.run(10000)


#类在实例化的时候需要加括号
# bick = Bicycle()
# bick.run(100)