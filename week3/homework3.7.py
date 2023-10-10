def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 例子
num1 = int(input())
num2 = int(input())

result = gcd(num1, num2)
print(f"{num1} 和 {num2} 的最大公约数是 {result}")
