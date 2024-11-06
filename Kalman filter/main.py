import matplotlib.pyplot as plt
from ODE_Systems import *
from NI_Methods import *
from KalmanFilter import KF

# Getting the noizy data from file
noisyData = []
with open("Kalman filter/data/data3.txt", "r") as file:
    for line in file:
        noisyData.append([float(x) for x in line.split()])
noisyData = np.array(noisyData)

# System simulation
ode = Sprott()
numIntegrator = euler

step = ode.stepSize()
num_steps = len(noisyData)

xyzs = np.empty((num_steps, 3))
xyzs[0] = ode.initConditions()

for i in range(num_steps - 1):
    xyzs[i + 1] = numIntegrator(ode.integrate, xyzs[i], step)

# Kalman filter usage
kf = KF(0.2, 0.5, 1.2)

# Plot
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*noisyData.T, lw=0.5)
ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

if isinstance(ode, Sprott):
    ax.set_title("Sprott Case I Attractor") 
elif isinstance(ode, Lorenz):
    ax.set_title("Lorenz Attractor") 

plt.show()