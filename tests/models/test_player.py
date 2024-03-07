import unittest
from unittest.mock import patch
from Models.Player import Player
import json
import os

class TestPlayer(unittest.TestCase):

    @patch('Models.Player.Player.get_new_id', return_value=1)
    def test_save_player(self, mock_get_new_id):
        # Crée une instance de Player pour le test
        test_player = Player("John", "Doe", "2000-01-01", "123456789")

        # Exécute la méthode save_player
        test_player.save_player()

        # Vérifie que le fichier players.json a été créé avec le joueur ajouté
        with open('data/players.json', 'r') as file:
            players = json.load(file)
            self.assertEqual(len(players), 1)
            self.assertEqual(players[0]['first_name'], "John")
            self.assertEqual(players[0]['last_name'], "Doe")
            self.assertEqual(players[0]['birth_date'], "2000-01-01")
            self.assertEqual(players[0]['national_chess_id'], "123456789")

    def test_get_players_file_not_found(self):
        # Teste le cas où le fichier players.json n'existe pas
        test_player = Player("John", "Doe", "2000-01-01", "123456789")
        result = test_player.get_players()
        self.assertEqual(result, "Fichier players.json introuvable")

    def test_get_players_file_found(self):
        # Crée un fichier players.json fictif avec un joueur
        with open('data/players.json', 'w') as file:
            player_data = [{"first_name": "John", "last_name": "Doe", "birth_date": "2000-01-01", "national_chess_id": "123456789"}]
            json.dump(player_data, file)

        # Teste le cas où le fichier players.json existe
        test_player = Player("Jane", "Smith", "1990-01-01", "987654321")
        result = test_player.get_players()
        self.assertEqual(result, player_data)

if __name__ == '__main__':
    unittest.main()
