import numpy as np
import matplotlib.pylab as plt
import math as m
u=38
ang=np.arange(0,90,1)
_range=[]
for angle in ang:
    _range.append(((u*u)*(m.sin(2*(m.radians(angle))))))
    
plt.plot(ang,_range)
plt.show()