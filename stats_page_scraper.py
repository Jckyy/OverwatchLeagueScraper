# TODO automate the creation of the dictionary using a for loop
# TODO get the list of players when calling a team abbreviation in the dictionary

# TODO the loop for the teams starting ln 15 work. But the players are still getting all their social media added in as well

import requests
from bs4 import BeautifulSoup
import json

web_page = requests.get("https://api.overwatchleague.com/teams?expand=team.content&locale=en_US").json()
web_page_teams = web_page['competitors']

team_dictionary = {}

for team in web_page_teams:
    team_name = team['competitor']['name']
    # team_dictionary[team_name] = team['competitor']['players']
    team_dictionary[team_name] = ""team['competitor']['players']""
    for player in team['competitor']['players']
        player_name = player['player']['name']




print(team_dictionary)




# team = 'NYXL'
# team_dictionary[team] = players



# web_page['competitors'][4]['competitor']['players']




# team_dictionary = {
#     "DAL" : web_page['competitors'][0]['competitor']['name'],
#     "PHI" : web_page['competitors'][1]['competitor']['name'],
#     "HOU" : web_page['competitors'][2]['competitor']['name'],
#     "BOS" : web_page['competitors'][3]['competitor']['name'],
#     "NYE" : web_page['competitors'][4]['competitor']['name'],

# }

# print(team_dictionary["NYE"])


