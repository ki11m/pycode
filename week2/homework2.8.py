def leibniz_pi(iterations):
    pi_approx = 0
    for i in range(iterations):
        pi_approx += (-1) ** i / (2 * i + 1)
    return pi_approx * 4

# 计算π的近似值
pi_approximation_leibniz = leibniz_pi(1000000)
print(f"莱布尼兹级数法计算的π近似值: {pi_approximation_leibniz:.10f}")

def wallis_pi(iterations):
    pi_approx = 1
    for i in range(1, iterations + 1):
        pi_approx *= (4 * i ** 2) / (4 * i ** 2 - 1)
    return pi_approx * 2

# 计算π的近似值
pi_approximation_wallis = wallis_pi(1000000)
print(f"Wallis公式计算的π近似值: {pi_approximation_wallis:.10f}")

import random

def monte_carlo_pi(iterations):
    inside_circle = 0
    total_points = 0
    for _ in range(iterations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            inside_circle += 1
        total_points += 1
    return (inside_circle / total_points) * 4

# 计算π的近似值
pi_approximation_monte_carlo = monte_carlo_pi(1000000)
print(f"蒙特卡洛模拟计算的π近似值: {pi_approximation_monte_carlo:.10f}")

'''
    比较这三种方法的效率取决于所需的迭代次数。
    一般来说，蒙特卡洛模拟需要较多的随机点以获得相似的精度。
    通常，级数法（如莱布尼兹级数法和Wallis公式）可以更快地获得精确度，
    但也取决于所需的项数。要在小数点后保留十位精度，需要更多的迭代次数。
'''