import matplotlib.pyplot as plt
import numpy as np

n = 1024
x1 = np.random.normal(0, 1, n)
y1 = np.random.normal(0, 1, n)
plt.scatter(x1, y1)
plt.show()

x2 = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c,s = np.cos(x2), np.sin(x2)
plt.plot(x2, c)
plt.plot(x2, s)
plt.show()

def f(x, y):return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

m = 256
x3 = np.linspace(-3, 3, m)
y3 = np.linspace(-3, 3, m)
x3, y3 = np.meshgrid(x3, y3)

plt.contour(x3, y3, f(x3, y3), 8, alpha = .75, cmap = 'jet')
C = plt.contour(x3, y3, f(x3, y3), 8, colors = 'black', linecache = .5)
plt.show()