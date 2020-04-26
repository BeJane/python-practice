推荐阅读：[如何理解概率分布函数和概率密度函数](https://www.jianshu.com/p/b570b1ba92bb)
@[toc]
# 正态分布(Nomal Distribution)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200425232049903.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzUzNzc4,size_16,color_FFFFFF,t_70)

```python
import numpy as np
import matplotlib.pyplot as plt
import math
# 均值
u = 0
#标准差 
sig = math.sqrt(0.2)

x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2) / (math.sqrt(2 * math.pi) * sig))
plt.plot(x,y_sig,"r-",linewidth=2)
plt.grid(True)
plt.show()
```
正态分布概率密度函数曲线

<img src="https://img-blog.csdnimg.cn/20200425230229773.png" width=50%>

# 两点分布 /伯努利分布(Two Point Distribution)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200427001852473.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzUzNzc4,size_16,color_FFFFFF,t_70)

```py
import numpy as np
import matplotlib.pyplot as plt
p = 0.7
x = [0,1]
y = [1-p, p]
plt.scatter(x,y) # 散点图
plt.grid(True)
plt.show()
```
<img src="https://img-blog.csdnimg.cn/20200427002013463.png" width=50%>

# 二项分布 (Binomial Distribution)
二项分布，即重复n次的伯努利试验，用ξ表示随机试验的结果。如果事件发生的概率是p,则不发生的概率q=1-p，N次独立重复试验中发生K次的概率是
P(ξ=K)= C(n,k) * p^k * (1-p)^(n-k)，其中C(n, k) =n!/(k!(n-k)!). 那么就说这个属于二项分布。其中P称为成功概率。记作ξ~B(n,p)
期望：Eξ=np；
方差：Dξ=npq, 其中q=1-p
```py
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
p = 0.4
n = 10
x = np.linspace(0,n,n+1)
y = comb(n,x)*p**x*(1-p)**(n-x)
print(x)
print(y)
plt.scatter(x,y)
plt.grid(True)
plt.show()
```
<img src="https://img-blog.csdnimg.cn/20200427011421398.png" width=70%>

# 几何分布 (Geometric Distribution) 
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020042701234624.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzUzNzc4,size_16,color_FFFFFF,t_70)
```py
import numpy as np
import matplotlib.pyplot as plt
p = 0.4
n = 10
x = np.linspace(1,n,n)
y = p*(1-p)**(x-1)
print(x)
print(y)
plt.scatter(x,y)
plt.grid(True)
plt.show()
```
<img src="https://img-blog.csdnimg.cn/20200427012937573.png" width=70%>

# 泊松分布（Possion Distribution)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200427013655323.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzUzNzc4,size_16,color_FFFFFF,t_70)
```py
import numpy as np
import matplotlib.pyplot as plt

x = np.random.poisson(lam = 5, size = 10000)
pillar = 15
a = plt.hist(x, pillar, color = 'g')
plt.plot(a[1][0:pillar], a[0],'r')
plt.grid()
plt.show()
```
<img src="https://img-blog.csdnimg.cn/20200427014823920.png" width=70%>

# 均匀分布 (Uniform Distribution)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200427002525421.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzUzNzc4,size_16,color_FFFFFF,t_70)
```py
import numpy as np
import matplotlib.pyplot as plt
a = 3
b = 5
x = np.linspace(a, b, 50)
y = []
for i in range(0,50):
	y.append(1 / (b - a))
plt.plot(x,y,"r-",linewidth=2)
plt.grid(True)
plt.show()
```
<img src="https://img-blog.csdnimg.cn/20200427003157879.png" width = 51%>

# 指数分布 (Exponential Distribution)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200427020319350.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzUzNzc4,size_16,color_FFFFFF,t_70)
```py
import numpy as np
import matplotlib.pyplot as plt

x = np.random.exponential(scale = 100, size = 10000)
pillar = 25
a = plt.hist(x, pillar, color = 'g')
plt.plot(a[1][0:pillar], a[0],'r')
plt.grid()
plt.show()
```
<img src="https://img-blog.csdnimg.cn/20200427022026285.png" width=70%>


