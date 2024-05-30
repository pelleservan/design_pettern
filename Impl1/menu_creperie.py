from typing import List
from plat import Plat

class MenuCreperie:
    """Class menue creprerie"""
    def __init__(self) -> None:
        self.plats: List[Plat] = []
        self.ajouter_plat(nom="Galette Annie", prix=11.90, vegetarien=False, description="Jambon blanc, emmental")
        self.ajouter_plat(nom="Galette Jannette", prix=13.50, vegetarien=False, description="Jambon blanc, oeuf, emmental")
        self.ajouter_plat(nom="Galette Paulette", prix=14.50, vegetarien=False, description="Jambon blanc, oeuf, emmental, champignons à la crème")
        self.ajouter_plat(nom="Galette Germaine", prix=12.90, vegetarien=False, description="Légumes au choix : fondue de poireaux, épinards, ratatouille Maison selon la saison ou champignon à la crème")

    def ajouter_plat(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        plat = Plat(nom, description, vegetarien, prix)
        self.plats.append(plat)

    def __str__(self) -> str:
        return "\n\n".join(str(plat) for plat in self.plats)