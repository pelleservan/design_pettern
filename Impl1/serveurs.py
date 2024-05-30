from menu_creperie import MenuCreperie
from menu_cafeteria import MenuCafeteria

class Serveuse:
    """Classe serveuse"""
    def __init__(self, menu_creperie: MenuCreperie, menu_cafeteria: MenuCafeteria) -> None:
        self.menu_creperie = menu_creperie
        self.menu_cafeteria = menu_cafeteria

    def afficher_menu(self) -> None:
        print("Menu Crêperie:\n")
        for i in range(len(self.menu_creperie.plats)):
            print(self.menu_creperie.plats[i])
            print("-" * 40)

        print("\nMenu Cafétéria:\n")
        for cle in self.menu_cafeteria.plats:
            print(self.menu_cafeteria.plats[cle])
            print("-" * 40)

class TestServeuse:
    """Class pour implémenter"""
    def __init__(self) -> None:
        menu_creperie = MenuCreperie()
        menu_cafeteria = MenuCafeteria()
        self.serveuse = Serveuse(menu_creperie, menu_cafeteria)

    def tester_afficher_menu(self) -> None:
        self.serveuse.afficher_menu()
