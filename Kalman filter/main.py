import matplotlib.pyplot as plt
from ODE_Systems import *
from NI_Methods import *
from KalmanFilter import KalmanFilter

ODE = Sprott()
INTEGRATOR = Euler()

def main():    
    # Getting noisy measurments from a file
    noisyData = []
    if isinstance(ODE, Sprott):
        path = "Kalman filter/data/data3.txt"
    elif isinstance(ODE, Lorenz):
        path = "Kalman filter/data/data2.txt"
        
    with open(path, "r") as file:
        for line in file:
            noisyData.append([float(x) for x in line.split()])
    noisyData = np.array(noisyData)
    
    # System simulation
    step = ODE.stepSize()
    num_steps = len(noisyData)

    xyzs = np.empty((num_steps, 3))
    xyzs[0] = ODE.initConditions()

    for i in range(num_steps - 1):
        xyzs[i + 1] = INTEGRATOR.integrate(ODE.calculate, xyzs[i], step)
        
    # KF usage
    processVar = 1e-3  # process noise
    measurementVar = 0.02  # measurment noise
    initState = np.array([0.1, 0.1, 0.1])

    # Filter initalization
    kf = KalmanFilter(processVar, measurementVar, initState)

    # Filtering process
    filtered_positions = []
    for measurement in noisyData:
        kf.predict()
        kf.correct(measurement)
        filtered_positions.append(kf.state)

    filtered_positions = np.array(filtered_positions)

    # Visualization
    ax = plt.figure().add_subplot(projection = "3d")

    ax.plot(*noisyData.T, "r-")
    ax.plot(*filtered_positions.T, "b-")
    ax.plot(*xyzs.T, "g-")
    
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    if isinstance(ODE, Sprott):
        ax.set_title("Sprott Case I Attractor") 
    elif isinstance(ODE, Lorenz):
        ax.set_title("Lorenz Attractor") 
        
    plt.show()

if __name__ == '__main__':
    main()