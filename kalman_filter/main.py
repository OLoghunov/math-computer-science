from ode_systems import *
from ni_methods import *
from kalman_filter.KalmanFilter import KalmanFilter
from kalman_filter.view import view

ODE = Lorenz()
INTEGRATOR = AdamsBashforth2()

def main():  
    # Getting noisy measurments from a file
    noisyData = []
    if isinstance(ODE, Sprott):
        path = "kalman_filter/data/data3.txt"
    elif isinstance(ODE, Lorenz):
        path = "kalman_filter/data/data2.txt"
        
    with open(path, "r") as file:
        for line in file:
            noisyData.append([float(x) for x in line.split()])
    noisyData = np.array(noisyData)
    
    # System simulation
    step = ODE.stepSize
    num_steps = len(noisyData)

    simulatedData = np.empty((num_steps, 3))
    simulatedData[0] = ODE.initConditions

    for i in range(num_steps - 1):
        simulatedData[i + 1] = INTEGRATOR.integrate(ODE.calculate, simulatedData[i], step)
        
    # KF usage
    processNoise = 1e-3
    measurementNoise = 0.02
    initState = np.array([0.1, 0.1, 0.1])

    # Filter initalization
    kf = KalmanFilter(processNoise, measurementNoise, initState, ODE, INTEGRATOR)

    # Filtering process
    filteredData = []
    for measurement in noisyData:
        kf.predict()
        kf.correct(measurement)
        filteredData.append(kf.state)

    filteredData = np.array(filteredData)

    # Gather parameters for view
    xRange = []
    for i in range(num_steps):
        xRange.append(ODE.stepSize * i)
        
    if isinstance(ODE, Sprott):
        label1 = "Sprott Case I Attractor"
        label2 = "Sprott Case I System"
    elif isinstance(ODE, Lorenz):
        label1 = "Lorenz Attractor"
        label2 = "Lorenz System"
        
    # Visualization
    view(noisyData, filteredData, simulatedData, xRange, label1, label2)
    
if __name__ == '__main__':
    main()