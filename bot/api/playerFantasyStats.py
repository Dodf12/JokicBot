import sys
import string
sys.path.append('/opt/anaconda3/lib/python3.12/site-packages')

#Load in data from .env file
import os
from dotenv import load_dotenv, dotenv_values

from espn_api.basketball import League


import os
from dotenv import load_dotenv, dotenv_values

#Load token
load_dotenv()
espn_S2 = os.getenv("S2")
try:
    league = League(league_id=72275173, year=2025, espn_s2='AECgpnX9ZmdraJJt6QbCNoG8rOXBMoltHPtbIlWNnunavnIliz9fXVhv8zGyJyT17f1EAVrZ6rWNS%2Fo2yTWk%2BdTI4jV7JYcUcshHt03D%2Fz1wuhP9b%2B6dPC3q%2FtnokyOFsjxefDq5qkqBzs9cDB6Hwu6EhUFOxazOYrXRXIARj%2FjZNYjitRV06HjtDu5lo1YXenZojXZNr8IiU388eY10a%2FjTAdxGA%2BIbNdW7K4rn%2FNdqElS0vzGYW0J9usqcTxD0YzJvSqjkE4U6anO9%2BAsbkSna',
                    swid='{E1BBCCED-47B5-4B49-B1C0-176BCE0A1992}')
    
    # if league.teams:
    #     team = league.teams[0]
    #     print("hi)")
    #     print(team.roster)
    # else:
    #     print("No teams found in the league.")

except Exception as e:
    print(f"An error occurred: {e}")


def getPlayerPPG(playerName):
    playerName = playerName.title()
    for team in league.teams:
        for player in team.roster:
            if player.name == playerName:
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
    playerName = playerName.title()
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
        