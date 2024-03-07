import unittest
from io import StringIO
from ..views import PlayerView


class TestPlayerView(unittest.TestCase):
    def test_get_player_info_input(self):
        # Teste que la méthode get_player_info récupère correctement les informations du joueur à partir de l'entrée utilisateur
        player_view = PlayerView()
        with unittest.mock.patch('sys.stdin', StringIO('Jane\nDoe\n01/01/1992\nCD54321\n')):
            result = player_view.get_player_info()
        self.assertEqual(result, ('Jane', 'Doe', '01/01/1992', 'CD54321'))

    def test_select_player_input(self):
        # Teste que la méthode select_player sélectionne le joueur correct dans une liste en fonction de l'entrée utilisateur
        player_view = PlayerView()
        players = [
            {'first_name': 'Alice', 'last_name': 'Wonder',
             'birth_date': '10/05/1988', 'national_chess_id': 'XY98765'},
        ]
        with unittest.mock.patch('sys.stdin', StringIO('1\n')):
            result = player_view.select_player(players)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
