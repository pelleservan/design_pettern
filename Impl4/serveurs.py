from menu_creperie import MenuCreperie
from menu_cafeteria import MenuCafeteria

class Serveuse:
    def __init__(self, menu_creperie: MenuCreperie, menu_cafeteria: MenuCafeteria) -> None:
        self.menu_creperie = menu_creperie
        self.menu_cafeteria = menu_cafeteria

    def afficher_menu(self) -> None:
        print("Menu Crêperie:\n")
        for plat in self.menu_creperie.get_plats():
            print(plat)
            print("-" * 40)

        print("\nMenu Cafétéria:\n")
        for plat in self.menu_cafeteria.get_plats().values():
            print(plat)
            print("-" * 40)

class TestServeuse:
    """Class pour implémenter"""
    def __init__(self) -> None:
        self.menu_creperie = MenuCreperie()
        self.menu_cafeteria = MenuCafeteria()
        self.serveuse = Serveuse(self.menu_creperie, self.menu_cafeteria)

    def tester_afficher_menu(self) -> None:
        self.serveuse.afficher_menu()

    def ajouter_plat_creperie(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        self.menu_creperie.ajouter_plat(nom, description, vegetarien, prix)

    def ajouter_plat_cafeteria(self, nom: str, description: str, vegetarien: bool, prix: float) -> None:
        self.menu_cafeteria.ajouter_plat(nom, description, vegetarien, prix)
