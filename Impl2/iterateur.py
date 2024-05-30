from abc import ABC, abstractmethod

class Iterateur(ABC):
    @abstractmethod
    def encore(self) -> bool:
        pass

    @abstractmethod
    def suivant(self):
        pass
