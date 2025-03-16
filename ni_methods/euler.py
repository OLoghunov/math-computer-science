from typing import Callable, List

class Euler:
    @classmethod
    def integrate(cls, f: Callable, x: List[int], h: int) -> List[int]:
        dx = f(x)
        return x + dx * h