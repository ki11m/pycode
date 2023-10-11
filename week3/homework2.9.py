def constructProductArray(A):
    n = len(A)
    Left = [1] * n
    Right = [1] * n
    B = [1] * n

    # 计算Left数组，其中Left[i]存储A[0] * A[1] * ... * A[i-1]
    product = 1
    for i in range(1, n):
        Left[i] = product
        product *= A[i - 1]

    # 计算Right数组，其中Right[i]存储A[i+1] * A[i+2] * ... * A[n-1]
    product = 1
    for i in range(n - 2, -1, -1):
        Right[i] = product
        product *= A[i + 1]

    # 构建B数组，B[i] = Left[i] * Right[i]
    for i in range(n):
        B[i] = Left[i] * Right[i]

    return B

# 示例用法
A = [1, 2, 3, 4, 5, 6, 7]
B = constructProductArray(A)
print(B)
