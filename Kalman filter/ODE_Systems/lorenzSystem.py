from .baseODE import * 
import numpy as np

class Lorenz(baseODE):
    def initConditions(self):
        return (5, 5, 5)
    
    def stepSize(self):
        return 0.01
    
    @classmethod  
    def calculate(cls, xyz: list[float], s=10, r=28, b=2.667) -> list[float]:
        x, y, z = xyz
        return np.array([s*(y - x), 
                         x*(r - z) - y, 
                         x*y - b*z])
    
    @classmethod    
    def jacobian(cls, xyz: list[float], s=10, r=28, b=2.667) -> list[float]:
        x, y, z = xyz.flatten()
        return np.array([[s*y, s*x, 0],
                         [r-z, 1, x],
                         [y, 0, b]])