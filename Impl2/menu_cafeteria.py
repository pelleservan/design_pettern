from typing import Dict
from menu import Menu, Plat
from iterateur import Iterateur

class MenuCafeteria(Menu):
    MAX_PLATS: int = 5

    def __init__(self) -> None:
        self.plats: Dict[str, Plat] = {}
        self.nombrePlats: int = 0
        self._ajouter_plats_initiaux()

    def _ajouter_plats_initiaux(self) -> None:
        plats_initiaux = [
            ("Salade du Forez", 12.50, False, "Saucisson chaud lyonnais artisanal, Râpées de pomme de terre maison"),
            ("Salade bergère", 12.50, False, "Fourme fondue, Crottin de chèvre chaud"),
            ("Salade bien-être", 12.50, True, "Assortiment de crudités")
        ]
        for nom, prix, vegetarien, description in plats_initiaux:
            self.ajouter_plat(nom, description, vegetarien, prix)

    def ajouter_plat(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        if self.nombrePlats < self.MAX_PLATS:
            plat = Plat(nom, description, vegetarien, prix)
            self.plats[nom] = plat
            self.nombrePlats += 1
        else:
            print("Le nombre maximum de plats a été atteint.")

    def get_plats(self) -> Dict[str, Plat]:
        return self.plats

    def creer_iterateur(self) -> Iterateur:
        return IterateurMenuCafeteria(self.plats)

class IterateurMenuCafeteria(Iterateur):
    def __init__(self, plats: Dict[str, Plat]) -> None:
        self._plats = list(plats.values())
        self._index = 0

    def encore(self) -> bool:
        return self._index < len(self._plats)

    def suivant(self) -> Plat:
        if self.encore():
            plat = self._plats[self._index]
            self._index += 1
            return plat
        else:
            raise StopIteration
