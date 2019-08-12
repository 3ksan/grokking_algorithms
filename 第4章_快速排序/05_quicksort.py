def quicksort(array):
	# 只有1个或0个元素时返回
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        # <=pivot的值的集合
        less = [i for i in array[1:] if i <= pivot]
        # >pivot的值的集合
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))