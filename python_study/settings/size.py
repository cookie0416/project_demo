_width = 800
_height = 800
def change(w,h):
    global _width   #全局变量
    _width = w     #重新给宽度赋值
    global _height  #全局变量
    _height = h     #重新给高度赋值

def getwidth():
    global _width
    return _width

def getheight():
    global _height
    return _width
