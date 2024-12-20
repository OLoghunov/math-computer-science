from typing import Callable, List

class RK2:
    @classmethod
    def integrate(cls, f: Callable, x: List[int], h: int) -> List[int]:
        k1 = f(x)
        k2 = f(x + k1*h/2)
        return x + k2 * h