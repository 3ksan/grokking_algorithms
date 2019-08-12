def countdown(i):
    # 基线条件(base case)
    if i <= 0:
        return 0
    # 递归条件(recursive cases)
    else:
        print(i)
        return countdown(i-1)

countdown(5)