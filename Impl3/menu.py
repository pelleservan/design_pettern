from abc import ABC, abstractmethod
from typing import List
from collections.abc import Iterator

class Plat:
    def __init__(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        self._nom = nom
        self._description = description
        self._vegetarien = vegetarien
        self._prix = prix

    def __str__(self) -> str:
        vegetarien_str = "Oui" if self._vegetarien else "Non"
        return (
            f"Nom: {self._nom}\n"
            f"Description: {self._description}\n"
            f"Végétarien: {vegetarien_str}\n"
            f"Prix: {self._prix:.2f} €"
        )

class Menu(ABC):
    @abstractmethod
    def ajouter_plat(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        pass

    @abstractmethod
    def get_plats(self) -> List[Plat]:
        pass

    @abstractmethod
    def creer_iterateur(self) -> Iterator:
        pass
