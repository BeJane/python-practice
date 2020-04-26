import numpy as np
import matplotlib.pyplot as plt
import math
# 均值
u = 0
#标准差 
sig = math.sqrt(0.2)
x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2) / (math.sqrt(2 * math.pi) * sig))
print(x)
print("=" * 20)
print(y_sig)
plt.plot(x,y_sig,"r-",linewidth=2)
plt.grid(True)
plt.show()