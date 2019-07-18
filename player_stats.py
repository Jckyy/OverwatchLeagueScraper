import requests
#from team_details import print_team_players


### this one updates the dictionary until the if statement is true, else last person in the json
# def get_player_stats(name):
#         api_player_stats = requests.get('https://api.overwatchleague.com/stats/players?stage_id=regular_season&season=2019').json()
#         api_player_stats = api_player_stats['data']
#         for player in api_player_stats:
#                 player_information = {
#                         'team' : player['team'],
#                         'role' : player['role'],
#                         'elims_per_10m' : round(player['eliminations_avg_per_10m'], 2),
#                         'damage_per_10m' : round(player['hero_damage_avg_per_10m'], 2),
#                         'healing_per_10m' : round(player['healing_avg_per_10m'], 2),
#                         'time_played' : round(player['time_played_total'], 2),
#                 }
#                 if player['name'].lower() == name.lower():
#                         break 
#         return player_information

### this one only creates a dictionary if the if statement is true
def get_player_stats2(name):
        api_player_stats = requests.get('https://api.overwatchleague.com/stats/players?stage_id=regular_season&season=2019').json()
        api_player_stats = api_player_stats['data']
        for player in api_player_stats:
                if player['name'].lower() == name.lower():
                        return {'team' : player['team'],
                                'role' : player['role'],
                                'elims_per_10m' : round(player['eliminations_avg_per_10m'], 2),
                                'damage_per_10m' : round(player['hero_damage_avg_per_10m'], 2),
                                'healing_per_10m' : round(player['healing_avg_per_10m'], 2),
                                'time_played' : round(player['time_played_total'], 2)}


# print(get_player_stats(player))

#print_team_players()
