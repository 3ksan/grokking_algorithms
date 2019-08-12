# 练习4.1
## 递归求和
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum([1, 2, 3, 4]))