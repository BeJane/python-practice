import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
p = 0.4
n = 10
x = np.linspace(1,n,n)
y = p*(1-p)**(x-1)
print(x)
print(y)
z = 0
for i in y:
	z = z +i

print(z)
plt.scatter(x,y)
plt.grid(True)
plt.show()