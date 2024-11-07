from typing import Callable, List

class Euler:
    def integrate(self, f: Callable, x: List[int], h: int) -> List[int]:
        dx = f(x)
        return x + dx * h