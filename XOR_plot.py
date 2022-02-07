import numpy as np
import matplotlib.pyplot as plt
X=np.random.random((1000,2))*2-1
y=np.zeros(1000)
for i in range(1000):
    x1,x2=X[i]
    if (x1>0 and x2<=0) or (x1<=0 and x2>0):
        y[i]=1
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()