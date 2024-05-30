class Plat():
    """Class plat"""
    def __init__(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        self._nom = nom
        self._description = description
        self._vegetarien = vegetarien
        self._prix = prix

    # Getters
    def get_nom(self) -> str:
        return self._nom

    def get_description(self) -> str:
        return self._description

    def get_vegetarien(self) -> bool:
        return self._vegetarien

    def get_prix(self) -> float:
        return self._prix

    # Setters
    def set_nom(self, nom: str) -> None:
        self._nom = nom

    def set_description(self, description: str) -> None:
        self._description = description

    def set_vegetarien(self, vegetarien: bool) -> None:
        self._vegetarien = vegetarien

    def set_prix(self, prix: float) -> None:
        self._prix = prix

    # __str__ method
    def __str__(self) -> str:
        vegetarien_str = "Oui" if self._vegetarien else "Non"
        return (
            f"Nom: {self._nom}\n"
            f"Description: {self._description}\n"
            f"Végétarien: {vegetarien_str}\n"
            f"Prix: {self._prix:.2f} €"
        )