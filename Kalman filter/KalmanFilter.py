import numpy as np
iX = 0
iV = 1
NUMVARS = iV + 1

class KF:
    def __init__(self, initialX: float, 
                       initialV: float,
                       accelVariance: float) -> None:
        # Mean of state
        self._x = np.zeros(NUMVARS)
        self._x[iX] = initialX
        self._x[iV] = initialV
        
        self._accelVariance = accelVariance
        
        # Covariance of state
        self._P = np.eye(NUMVARS) 
    
    def predict(self, dt: float) -> None:
        # x = F*x
        # P = F*P*F.T + G*G*T*a
        F = np.eye(NUMVARS)
        F[iX, iV] = dt
        newX = F.dot(self._x)
        
        G = np.zeros((2, 1))
        G[iX] = 0.5 * dt**2
        G[iV] = dt
        newP = F.dot(self._P).dot(F.T) + G.dot(G.T) * self._accelVariance
        
        self._x = newX
        self._P = newP
        
    def correct(self, measedValue: float, measedVariance):
        # y = z - H*x
        # S = H*P*H.T + R
        # K = P*S^(-1)
        # x = x + K*y
        # P = (I - K*H)*P
        
        z = np.array([measedValue])
        R = np.array([measedVariance])
        
        H = np.zeros((1, NUMVARS))
        H[0, iX] = 1
        
        y = z - H.dot(self._x)
        S = H.dot(self._P).dot(H.T) + R
        K = self._P.dot(H.T).dot(np.linalg.inv(S))
        
        newX = self._x + K.dot(y)
        newP = (np.eye(2) - K.dot(H)).dot(self._P)
        
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
        return self._x[iX]
    
    @property
    def vel(self) -> float:
        return self._x[iV]