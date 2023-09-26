# 使用数学方法，将n拆分为若干个整数，使他们的乘积最大，就要将n拆分成更多的3和更少的2，那么如果n = 2001，就把2001拆成667个3和一个2。
def list(n):
    if n <= 1:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [3]
    list = []
    while n > 4:
        list.append(3)
        n -= 3

    list.append(n)  # 添加最后一个数，可能是2或3
    return list

n = int(input())
result = list(n)
print(result)
