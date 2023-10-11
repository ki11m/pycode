# 初始猜测值
g = 1.0
# 定义允许的误差范围
epsilon = 1e-6
# 开始循环，直到满足精度要求
while True:
    # 使用牛顿迭代法来逼近根号2的值
    new_g = 0.5 * (g + 2 / g)

    # 如果新猜测值与旧猜测值之间的差小于允许的误差范围，就退出循环
    if abs(new_g - g) < epsilon:
        break
    g = new_g

print(f"根号2的近似值为: {g}")
