import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.all_players  = []


        for player_dict in self.response:
            player = Player(player_dict)
            self.all_players.append(player)

    def get_players(self):
        return self.all_players
