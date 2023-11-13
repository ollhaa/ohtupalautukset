#import requests
#from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

#lisäys
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    
    print("Players from FIN\n")

    for player in players:
        print(player)


    


    

if __name__ == "__main__":
    main()
