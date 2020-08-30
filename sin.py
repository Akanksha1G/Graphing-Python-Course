import matplotlib.pyplot as plt 
import numpy as np 

x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)

#naming x-axis and y-axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.plot(x,y)
plt.show()