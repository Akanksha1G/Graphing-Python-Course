
import matplotlib.pyplot as graph
import numpy as array
import math
#assuming length of pendulum is equal to g
theta=array.arange(0,math.pi/2,0.01)
dt=0.001
time=array.arange(0,70,dt)
def timer(the):
	w=0
	o=the
	for t in time:
		w=w+math.sin(o)*dt
		o=o-w*dt
		if(o<=0):
			return 4*t
period=[]
tet=[]
for x in theta:
	period.append(timer(x))
	tet.append(math.degrees(x))
graph.xlabel("theta")
graph.ylabel("time")
graph.plot(tet,period)
graph.show()