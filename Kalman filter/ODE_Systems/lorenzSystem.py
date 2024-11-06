from .baseODE import * 
import numpy as np

class Lorenz(baseODE):
    def initConditions(self):
        return (3, 1.5, 15)
    
    def stepSize(self):
        return 0.01
    
    def integrate(self, xyz: list[float], *, s=10, r=28, b=2.667) -> list[float]:
        x, y, z = xyz
        return np.array([s*(y - x), 
                         r*x - y - x*z, 
                         x*y - b*z])
