#冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)-1):             #第一层for表示循环的次数
        for j in range(len(arr)-1-i):       #第二层for表示具体表示哪两个元素
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print(i,j,arr)
    return arr
list1 = [34,35,12,13,66,11]
bubble_sort(list1)
