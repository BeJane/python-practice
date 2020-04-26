import numpy as np
import matplotlib.pyplot as plt

x = np.random.exponential(scale = 100, size = 10000)
pillar = 25
a = plt.hist(x, pillar, color = 'g')
plt.plot(a[1][0:pillar], a[0],'r')
plt.grid()
plt.show()