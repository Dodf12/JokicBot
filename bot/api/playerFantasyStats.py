import sys
import string
sys.path.append('/opt/anaconda3/lib/python3.12/site-packages')
import difflib

#Load in data from .env file
import os
from dotenv import load_dotenv, dotenv_values

from espn_api.basketball import League

#Load environment variables
load_dotenv()

# Get credentials from environment variables
LEAGUE_ID = os.getenv("LEAGUE_ID")
ESPN_S2 = os.getenv("ESPN_S2")
ESPN_SWID = os.getenv("ESPN_SWID")

try:
    league = League(league_id=int(LEAGUE_ID), year=2025, espn_s2=ESPN_S2, swid=ESPN_SWID)
    
    # Print all player names for debugging
    print("=== All player names in league ===")
    for team in league.teams:
        for player in team.roster:
            print(repr(player.name))
    print("==================================")

except Exception as e:
    print(f"An error occurred: {e}")

# Example in playerFantasyStats.py
import difflib

def find_player_obj(playerName):
    playerName = playerName.strip().lower()
    all_players = [(player.name.strip().lower(), player) for team in league.teams for player in team.roster]
    all_names = [name for name, _ in all_players]
    match = difflib.get_close_matches(playerName, all_names, n=1, cutoff=0.5)
    print(f"Looking for: {playerName}, Match found: {match}")
    if match:
        for name, player in all_players:
            if name == match[0]:
                return player
    return None


def getPlayerPPG(playerName):
    playerName = playerName.strip().lower()
    all_names = [player.name.strip().lower() for team in league.teams for player in team.roster]
    match = difflib.get_close_matches(playerName, all_names, n=1, cutoff=0.5)
    if match:
        for team in league.teams:
            for player in team.roster:
                if player.name.strip().lower() == match[0]:
                    return player.avg_points
    return "This player does not exist. Please enter another player"

def getBigFive(playerName):
    playerName = playerName.title()
    for team in league.teams:
        for player in team.roster:
            if player.name == playerName:
                return player.avg_points
    return "This player does not exist. Please enter another player"

def getOtherPlayerStats(playerName, command):

    playerFound = False
    # if command not in playerName.stats:
    #     return "This is not a valid command. Please enter another command"
    #playerName = playerName.title()
    command = command.upper()

    for team in league.teams:
        for player in team.roster:
            if player.name == playerName:
                try:
                    return player.stats['2025_total']['avg'][command]
                except KeyError:
                    return "Sorry, your player is valid, but not your command. Please re-enter your command"
    return "Your player and/or command is incorrect. Please make sure your player name is correct and command is in the list of available commands"

    # elif (playerFound == False and command not in playerName.stats):
    #     return "This player does not exist. Please enter another player. This is also not a valid command. Please enter another command "
    # return "This player does not exist. Please enter another player"

#print(getOtherPlayerStats("Damian Lillard",'rmg'))
#print(getPlayerPPG("Lebron James"))
        