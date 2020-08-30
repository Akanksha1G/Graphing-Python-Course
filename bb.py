import matplotlib.pyplot as plt
from numpy import *

y1 = 10		# initial height
ydot_0 = 0 		# initial velocity
yddot = -9.81	# accel due to gravity
x_0 = 0
xdot_0 = 1
xddot_0 = 0
dt = 0.01		# delta time
COR = .8 	#coefficient of restitution <1 is realistic-ish elastic with some energy loss


time = arange(0,20,dt)
y = zeros(size(time))
y[0] = y1
y_prev = 0
t_local = 0
cntr = 0

for idx, t in enumerate(time) :
	t_local = dt*cntr
	
	y[idx] = y1 + ydot_0*t_local + yddot*t_local**2/2

	if (y[idx] <= 0.0):
		ydot_0 = COR*(y_prev - y[idx])/dt
		y1 = 0 		# must be at edge, reset height to this value
		t_local = 0 	# reset time
		cntr = 0 		# reset counter
		
	
	#calculate position
	
	y_prev = y[idx] 	# store previous time value
	cntr = cntr + 1 		# increment counter
	

plt.plot(time, y)
plt.ylabel("Height [m]")
plt.xlabel("Time [sec]")
plt.title("Bouncing Ball Trajectory dt = %0.2f sec" % dt )
plt.show()