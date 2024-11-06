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
realX = 0.0
measVariance = 0.1 ** 2
realV = 0.5

kf = KF(0.0, 1.0, 1.5)
dt = 0.1
nSteps = 1000
measEverySteps = 20

mus = []
covs = []
realXs = []
realVs = []

# KF init
kf = KF(initialX=0.1, initialV=0.0, accelVariance=1.0)
filtered_states = []

for measurement in noisyData:
    kf.predict(dt=ode.stepSize())
    kf.correct(measedValue=measurement[0], measedVariance=0.01)
    filtered_states.append(kf.mean)

filtered_states = np.array(filtered_states)

# Plot
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*noisyData.T, lw=0.5)
#ax.plot(*xyzs.T, lw=0.5)
ax.plot(*filtered_states.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

if isinstance(ode, Sprott):
    ax.set_title("Sprott Case I Attractor") 
elif isinstance(ode, Lorenz):
    ax.set_title("Lorenz Attractor") 
    
plt.show()
