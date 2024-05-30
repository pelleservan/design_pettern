from menu_creperie import MenuCreperie
from menu_cafeteria import MenuCafeteria

class Serveuse:
    def __init__(self, menu_creperie: MenuCreperie, menu_cafeteria: MenuCafeteria) -> None:
        self.menu_creperie = menu_creperie
        self.menu_cafeteria = menu_cafeteria

    def afficher_menu(self) -> None:
        print("Menu Crêperie:\n")
        iterateur_creperie = self.menu_creperie.creer_iterateur()
        while iterateur_creperie.encore():
            print(iterateur_creperie.__next__())
            print("-" * 40)

        print("\nMenu Cafétéria:\n")
        iterateur_cafeteria = self.menu_cafeteria.creer_iterateur()
        while iterateur_cafeteria.encore():
            print(iterateur_cafeteria.__next__())
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

