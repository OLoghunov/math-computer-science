from .baseODE import * 
import numpy as np

class Sprott(baseODE):
    
    @property
    def initConditions(self):
        return (0.1, 0, 0)
    
    @property
    def stepSize(self):
        return 0.1

    @classmethod
    def calculate(self, xyz: list[float]) -> list[float]:
        x, y, z = xyz
        return np.array([-0.2 * y, 
                         x + z, 
                         x + y**2 - z])
    
    @classmethod
    def jacobian(self, xyz: list[float]) -> list[float]:
        x, y, z = xyz.flatten()
        return np.array([[0, -0.2,  0], 
                         [1,  0,    1], 
                         [1,  2*y, -1]])