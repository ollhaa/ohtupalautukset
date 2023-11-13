from player_reader import PlayerReader

class PlayerStats:

    def __init__(self, player_reader:PlayerReader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self,country):
        selected_players = []

        for player in self.player_reader.get_players():
            if player.nationality == country:
                selected_players.append(player)

        selected_players.sort(key=lambda x: x.goals+x.assists, reverse=True)
        
        return selected_players


        