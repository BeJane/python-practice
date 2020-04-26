import numpy as np
import matplotlib.pyplot as plt

a = 3
b = 5
x = np.linspace(a, b, 50)
y = []
for i in range(0,50):
	y.append(1 / (b - a))
print(x)
print("=" * 20)
print(y)
plt.plot(x,y,"r-",linewidth=2)
plt.grid(True)
plt.show()