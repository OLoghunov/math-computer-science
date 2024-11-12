import numpy as np
from ODE_Systems import Lorenz
from NI_Methods import Euler

class KalmanFilter:
    def __init__(self, processNoise, measurementNoise, init_state) -> None:
        # Filter parameters
        self._state = init_state.reshape(3, 1) # initial state [x, y, z]
        
        self._F = np.eye(3) # transition matrix
        # self._F = Lorenz.jacobian(self._state)
        self._H = np.eye(3) # observation matrix
        self._P = np.eye(3) # covariance matrix

        self._Q = np.eye(3) * processNoise  # covariance of the process noise
        self._R = np.eye(3) * measurementNoise  # covariance of the observation noise
        self._ODE = Lorenz()
    
    def predict(self) -> None:
        # x = F*x
        # P = F*P*F.T + Q
        
        # Predict new state
        self._state = np.dot(self._F, self._state)
        # self._state = Euler.integrate(self._ODE.calculate, self._state, self._ODE.stepSize)
        
        # Predict covariance fault
        self._P = np.dot(self._F, np.dot(self._P, self._F.T)) + self._Q
        
    def correct(self, measurement):
        # y = z - H*x
        # S = H*P*H.T + R
        # K = P*H*S^(-1)
        # x = x + K*y
        # P = (I - K*H)*P
        
        # Make a measurement column-like
        measurement = measurement.reshape(3, 1)

        # Calculate Kalman gain matrix
        S = np.dot(self._H, np.dot(self._P, self._H.T)) + self._R  # observating fault
        K = np.dot(self._P, np.dot(self._H.T, np.linalg.inv(S)))  # Kalman gain matrix
        
        # Calculate the remainder
        y = measurement - np.dot(self._H, self._state)  # measuring error
        # Update the state
        self._state = self._state + np.dot(K, y)
        # Update the covariance fault
        I = np.eye(self._P.shape[0])  # unit matrix of dimention as P
        self._P = (I - np.dot(K, self._H)).dot(self._P)
        
        # K = np.dot(self._P, np.linalg.inv(self._P + self._R))  # Kalman gain matrix
        # self._state = self._state + K.dot(measurement-Lorenz.calculate(self._state))
        # I = np.eye(self._P.shape[0])  # unit matrix of dimention as P
        # self._P = (I - K).dot(self._P)
        
    
    @property
    def state(self) -> np.array:
        return self._state.flatten()