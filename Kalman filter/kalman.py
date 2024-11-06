import matplotlib.pyplot as plt
from ODE_Systems import *
from NI_Methods import *

ode = Sprott()
numIntegrator = euler

step = ode.stepSize()
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = ode.initConditions()

for i in range(num_steps):
    xyzs[i + 1] = numIntegrator(ode.integrate, xyzs[i], step)


# Plot
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

if isinstance(ode, Sprott):
    ax.set_title("Sprott Case I Attractor") 
elif isinstance(ode, Lorenz):
    ax.set_title("Lorenz Attractor") 

plt.show()