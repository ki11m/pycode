import random
import math


def monte_carlo_integration(func, a, b, num_samples):
    integral = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        integral += func(x)

    integral *= (b - a) / num_samples
    return integral


# 被积函数 f(x) = x^2 + 4*x*sin(x)
def func(x):
    y = math.sin(x)
    return x ** 2 + 4 * x * y


a = 2  # 积分下限
b = 3  # 积分上限
num_samples = 1000000  # 采样点数，可以根据需要调整

estimated_integral = monte_carlo_integration(func, a, b, num_samples)
print(f"函数 f(x) = x^2 + 4*x*sin(x) 在区间 [{a}, {b}] 上的定积分的估计值为: {estimated_integral:.6f}")
