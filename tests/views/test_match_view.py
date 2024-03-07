from Views.MatchView import MatchView
from io import StringIO


def test_get_user_choice(monkeypatch):
    match_view = MatchView()
    monkeypatch.setattr('sys.stdin', StringIO('2\n'))

    assert match_view.get_user_choice() == 2


import unittest
from Views.MatchView import MatchView
from io import StringIO


class TestMatchView(unittest.TestCase):
    def test_get_user_choice(self, monkeypatch):
        # Teste la méthode get_user_choice pour vérifier si elle renvoie le bon choix de l'utilisateur
        match_view = MatchView()
        monkeypatch.setattr('sys.stdin', StringIO('2\n'))  # Simulation de l'entrée utilisateur '1'

        assert match_view.get_user_choice() == 1

if __name__ == '__main__':
    unittest.main()
