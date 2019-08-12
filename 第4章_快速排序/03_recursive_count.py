# 练习4.2
## 递归求列表元素个数
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1, 2, 3, 4]))