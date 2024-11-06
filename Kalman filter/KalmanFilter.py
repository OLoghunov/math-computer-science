import numpy as np
class KF:
    def __init__(self, initialX: float, 
                       initialV: float,
                       accelVariance: float) -> None:
        # Mean of state
        self._x = np.array([initialX, initialV])
        
        self._accelVariance = accelVariance
        # Covariance of state
        self._P = np.eye(2) 
    
    def predict(self, dt: float) -> None:
        F = np.array([1, dt], [0, 1])
        newX = F.dot(self._x)
        G = np.array([0.5 * dt**2, dt]).reshape((2, 1))
        newP = F.dot(self._P).dot(F.T) + G.dot(G.T) * self._accelVariance
        
        self._x = newX
        self._P = newP
      
    @property
    def cov(self) -> np.array:
        return self._P  
    
    @property
    def mean(self) -> np.array:
        return self._x  
        
    @property    
    def pos(self) -> float:
        return self._x[0]
    
    @property
    def vel(self) -> float:
        return self._x[1]