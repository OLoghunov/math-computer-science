from .baseODE import * 
import numpy as np

class Sprott(baseODE):
    def initConditions(self):
        return (0.1, 0, 0)
    
    def stepSize(self):
        return 0.1

    def calculate(self, xyz: list[float]) -> list[float]:
        x, y, z = xyz
        return np.array([-0.2 * y, 
                x + z, 
                x + y**2 - z])
    
    def jacobian(self, xyz: list[float]) -> list[float]:
        y = xyz[1]
        return np.array([[0, -0.2, 0], 
                         [1, 0, 1], 
                         [1, 2*y, -1]])