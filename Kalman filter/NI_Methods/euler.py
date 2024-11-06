from typing import Callable, List

def euler(f: Callable, x: List[int], h: int) -> List[int]:
    dx = f(x)
    return x + dx * h