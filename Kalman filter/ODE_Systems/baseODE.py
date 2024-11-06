from abc import ABC, abstractmethod

class baseODE(ABC):
    @property
    @abstractmethod
    def initConditions(self) -> tuple:
        pass
    
    @property
    @abstractmethod
    def stepSize(self) -> float:
        pass

    @abstractmethod
    def integrate(self, xyz: list[float], **kwargs) -> list[float]:
        pass