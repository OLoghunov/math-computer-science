from typing import Callable
import numpy as np

class AdamsBashforth2:
    def __init__(self):
        self.previous_f = None

    def integrate(self, f: Callable, x: np.ndarray, h: float) -> np.ndarray:
        x = x.flatten()
        dx = f(x).flatten()
        if self.previous_f is None:
            x_next = x + h * dx
        else:
            x_next = x + h * (1.5 * dx - 0.5 * self.previous_f)
        self.previous_f = dx
        
        return x_next
