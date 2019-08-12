# item为待查找的值
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        # guess为剩余list的中间值
        guess = list[mid]
        # 找到item，直接返回
        if guess == item:
            return mid
        # 中间值guess比查找值item大
        if guess > item:
            high = mid - 1
        # 中间值guess比查找值item小
        else:
            low = mid + 1
    # 查找值item不存在		
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None