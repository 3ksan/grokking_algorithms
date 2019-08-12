# 找到数组的最小值并返回该值的下标index
def findSmallest(arr):
    # 保存最小值
    smallest = arr[0]
    # 保存最小值的下标
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 选择排序主函数
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # 找到最小值的下标
        smallest_index = findSmallest(arr)
        # pop(index) 根据下标index弹出最小值
        # append() 将最小值添加到新数组的尾部
        newArr.append(arr.pop(smallest_index))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))