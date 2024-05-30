from serveurs import TestServeuse

if __name__ == "__main__":
    test_serveuse = TestServeuse()
    
    test_serveuse.ajouter_plat_creperie("Galette Super", "Super galette avec tout", False, 15.50)
    test_serveuse.ajouter_plat_cafeteria("Salade César", "Salade avec poulet et parmesan", False, 13.00)
    
    test_serveuse.tester_afficher_menu()