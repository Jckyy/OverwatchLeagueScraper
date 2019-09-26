from team_details import print_team_players
from player_stats import get_player_stats2
import csv

# print_team_players()

player = 'Mano'	
# print(get_player_stats2(player))

player_stats = get_player_stats2(player)
print(type(player_stats))





# make this a function
keys = player_stats.keys()
print(keys)
with open('player stats.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, delimiter=',', fieldnames=keys)
    dict_writer.writeheader()
    #dict_writer.writerow(player_stats)
    #dict_writer.writerows([player_stats, player_stats, player_stats, player_stats])





