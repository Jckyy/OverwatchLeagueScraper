import requests


api_player_stats = requests.get('https://api.overwatchleague.com/stats/players?stage_id=regular_season&season=2019').json()
player_stats = api_player_stats['data']


player_dictionary = {}

for player in player_stats:
    player_name = player['name']
    player_information = player['team'],player['time_played_total']
    player_dictionary[player_name] = player_information
    # for information in player_stats:

print(player_dictionary)