import json

# json由字典和列表组成

data = {
    "name": ["jerry", "nikename"],
    "age": 24,
    "gender": "female"
}

print(type(data))
data1 = json.dumps(data)  # 把json数据类型转成字符串
print(data1)
print(type(data1))

data2 = json.loads(data1)  # 把字符串转成json
print(type(data2))

json.dump()  # 把json数据类型转成字符串并存储在文件中

json.load()  # 把文件打开，把里面的字符转换成json数据类型
