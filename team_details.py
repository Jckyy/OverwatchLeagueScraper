# TODO player search with stats
import requests
import json
# from player_stats import get_player_stats


# team_dictionary {
#         "Boston Uprising": players,
#         "NYXL": players,
#         "ding": "piing"
# }

# team_dictionary["NYXL"] #players
# team_dictionary["ding"] = "piing"


# for team in web_page_teams
#       if team[name] == teamname
#                for player in team
#                       append player

def get_teams_players():
        web_page = requests.get("https://api.overwatchleague.com/teams?expand=team.content&locale=en_US").json()
        web_page_teams = web_page['competitors']

        team_dictionary = {}
        team_dictionary_abb = {}
        for team in web_page_teams:
                team_name = team['competitor']['name'].upper()
                team_dictionary[team_name] = team['competitor']['players']

                team_name_abb = team['competitor']['abbreviatedName'].upper()
                team_dictionary_abb[team_name_abb] = team_name
                
                team_player_names = []
                for player in team_dictionary[team_name]:
                        team_player_names.append(player['player']['name'])
                        team_dictionary[team_name] = team_player_names
        return team_dictionary, team_dictionary_abb

def print_team_players():
        teams_players, team_dictionary_abb = get_teams_players()
        user_input = input(f"{team_dictionary_abb}\nName: ").upper()
        if len(user_input) < 4:
                result = teams_players[team_dictionary_abb[user_input]]
                print("The players on the {} are: {}".format(team_dictionary_abb[user_input], result))
        else:
                result = teams_players[user_input]
                print("The players on the {} are : {}".format(user_input, result))



# print_team_players()

# print(get_player_stats('Decay'))

# print(team_dictionary)

