import unittest
from Views.Menu import Menu
from io import StringIO


class TestMenu(unittest.TestCase):
    def test_main_menu(self, monkeypatch):
        # Teste la méthode main_menu pour vérifier si elle renvoie le bon choix du menu principal
        menu = Menu()
        monkeypatch.setattr('sys.stdin', StringIO('2\n'))  # Simulation de l'entrée utilisateur '2'

        assert menu.main_menu() == '2'

    def test_report_menu(self, monkeypatch):
        # Teste la méthode report_menu pour vérifier si elle renvoie le bon choix du menu de rapport
        menu = Menu()
        monkeypatch.setattr('sys.stdin', StringIO('3\n'))  # Simulation de l'entrée utilisateur '3'

        assert menu.report_menu() == '3'

if __name__ == '__main__':
    unittest.main()
