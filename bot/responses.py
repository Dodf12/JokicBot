import string
import re
from api.playerFantasyStats import getPlayerPPG, getOtherPlayerStats


def evaluate_response(lowered):

  pattern = r"^!(\w+%?)(.*)"


  match = re.match(pattern, lowered)

  if match: 
    command = match.group(1)
    print("command " + command)
    arguments = match.group(2).strip()
    information = command_outputter([command,arguments])
    return information
  return "That is not a viable command"

def command_outputter(arr):
  if (arr[0] == "fppg"):
    print(arr[1])
    return getPlayerPPG(arr[1])
  return getOtherPlayerStats(arr[1],arr[0])
  return "Not a valid command"




  # print(lowered)
  # if lowered == '':
  #   return "Arei Bhai, kuch bhol na"
