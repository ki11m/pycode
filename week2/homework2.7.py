def newton_cubic_root(c, initial_guess=1.0, epsilon=1e-6, max_iterations=100):
    x = initial_guess
    iterations = 0

    while iterations < max_iterations:
        # 计算函数值和导数值
        f = x ** 3 - c
        df = 3 * x ** 2

        # 更新迭代值
        x = x - f / df

        if abs(f) < epsilon:
            return x
        iterations += 1

    return None  # 如果达到最大迭代次数仍未达到精度要求，返回None


# 设置不同的c值进行测试
c_values = [10]

for c in c_values:
    result = newton_cubic_root(c)
    if result is not None:
        print(f"{c} 的三次方根的近似值为: {result}")
    else:
        print(f"{c} 未能在指定的迭代次数内达到精度要求。")
