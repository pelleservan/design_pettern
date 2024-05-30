from typing import Dict
from plat import Plat

class MenuCafeteria:
    """Class menu cafeteria"""
    MAX_PLATS: int = 5

    def __init__(self) -> None:
        self.plats: Dict[int, Plat] = {}
        self.nombrePlats: int = 0

        self.ajouter_plat(nom="Salade Forez", prix=12.50, vegetarien=False, description="Saucisson chaud lyonnais artisanal, Râpées de pommes de terre maison")
        self.ajouter_plat(nom="Salade bergère", prix=12.50, vegetarien=False, description="Fourme fondue, Crottin de chèvre chaud")
        self.ajouter_plat(nom="Salade bien-être", prix=12.50, vegetarien=True, description="Assortiment de crudités")

    def ajouter_plat(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        if self.nombrePlats < self.MAX_PLATS:
            plat = Plat(nom, description, vegetarien, prix)
            self.plats[self.nombrePlats] = plat
            self.nombrePlats += 1
        else:
            print("Le nombre maximum de plats a été atteint.")

    def __str__(self) -> str:
        return "\n\n".join(str(plat) for plat in self.plats.values())