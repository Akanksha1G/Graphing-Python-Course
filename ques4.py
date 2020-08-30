from math import sqrt
import matplotlib.pyplot as plt

h0 = 10       
v = 0          
g = 9.81       
t = 0          
dt = 0.01     
rho = 0.8     
tau = 0.1   
hmax = h0      
h = 0
hstop = 0.01   
ff = True 
t_last = -sqrt(2*h0/g) 
vmax = sqrt(2 * hmax * g)
H = []
T = []
while(hmax > hstop):
  if(ff):
    hnew = h + v*dt - 0.5*g*dt*dt
    if(hnew<0):
      t = t_last + 2*sqrt(2*hmax/g)
      ff = False
      t_last = t + tau
      h = 0
    else:
      t = t + dt
      v = v - g*dt
      h = hnew
  else:
    t = t + tau
    vmax = vmax * rho
    v = vmax
    ff = True
    h = 0
  hmax = 0.5*vmax*vmax/g
  H.append(h)
  T.append(t)



plt.figure()

plt.xlabel('time')
plt.ylabel('height')
plt.plot(T,H)
plt.show()