import numpy as np

class KalmanFilter:
    def __init__(self, processVar, measurementVar, init_state) -> None:
        # Filter parameters
        self._state = init_state.reshape(3, 1) # initial state [x, y, z]
        
        self._F = np.eye(3) # transition matrix
        self._H = np.eye(3) # observation matrix
        self._P = np.eye(3) # covariance matrix

        self._Q = np.eye(3) * processVar  # covariance of the process noise
        self._R = np.eye(3) * measurementVar  # covariance of the observation noise
    
    def predict(self) -> None:
        # x = F*x
        # P = F*P*F.T + Q
        
        # Predict new state
        self._state = np.dot(self._F, self._state)
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
        y = measurement - np.dot(self._H, self._state)  # measuring fault

        # Update the state
        self._state = self._state + np.dot(K, y)
        # Update the covariance fault
        I = np.eye(self._P.shape[0])  # unit matrix of dimention as P
        self._P = (I - np.dot(K, self._H)).dot(self._P)
    
    @property
    def state(self) -> np.array:
        return self._state.flatten()