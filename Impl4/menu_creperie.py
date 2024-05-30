from typing import List
from menu import Menu, Plat

class MenuCreperie(Menu):
    def __init__(self) -> None:
        self.plats: List[Plat] = []
        self._ajouter_plats_initiaux()

    def _ajouter_plats_initiaux(self) -> None:
        plats_initiaux = [
            ("Galette Annie", 11.90, False, "Jambon blanc, emmental"),
            ("Galette Jeannette", 13.50, False, "Jambon blanc, œuf, emmental"),
            ("Galette Paulette", 14.50, False, "Jambon blanc, œuf, emmental, champignons à la crème"),
            ("Galette Germaine", 12.90, True, "Légumes au choix : fondue de poireaux, épinards, ratatouille Maison selon la saison ou champignons à la crème")
        ]
        for nom, prix, vegetarien, description in plats_initiaux:
            self.ajouter_plat(nom, description, vegetarien, prix)

    def ajouter_plat(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        plat = Plat(nom, description, vegetarien, prix)
        self.plats.append(plat)

    def get_plats(self) -> List[Plat]:
        return self.plats

    def creer_iterateur(self):
        return iter(self.plats)
