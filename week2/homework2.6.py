def newton_sqrt(c, epsilon=1e-6, max_iterations=100):
    # guess = c/4
    # guess = c/2
    guess = c
    iterations = 0

    while iterations < max_iterations:
        new_guess = 0.5 * (guess + c / guess)
        if abs(new_guess - guess) < epsilon:
            return new_guess
        guess = new_guess
        iterations += 1

    return None  # 如果达到最大迭代次数仍未达到精度要求，返回None


# 设置不同的c值进行测试
c_values = [2, 2000]

for c in c_values:
    result = newton_sqrt(c)
    if result is not None:
        print(f"sqrt({c}) 的近似值为: {result}")
    else:
        print(f"sqrt({c}) 未能在指定的迭代次数内达到精度要求。")