#计算BMI指数

def fun_bmi(person,height,weight):
    '''功能：根据身高和体重计算BMI指数
    person：姓名
    height：身高，单位：米
    weight：体重，单位：千克
    '''
    print(person+"的身高："+str(height)+"\t"+person+"的体重："+str(weight))
    bmi=weight/(height*height)
    print(person+"的BMI指数为："+str(bmi))
    #判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻")
    if bmi >= 18.5 and bmi < 24.9:
        print("正常范围")
    if bmi >= 24.9 and bmi <29.9:
        print("您的体重过重")
    if bmi >= 29.9:
        print("肥胖")