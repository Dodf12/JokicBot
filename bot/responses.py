import string
import re
from api.playerFantasyStats import getPlayerPPG, getOtherPlayerStats


def command_outputter(arr):
  if (arr[0] == "fppg"):
    print(arr[1])
    return getPlayerPPG(arr[1])
  return getOtherPlayerStats(arr[1],arr[0])
  return "Not a valid command"

class Responses:
  def __init__(self):
    self.command= ""
    self.arguments = ""
  
  def getCommand(self):
    return self.command
  
  def getArguments(self):
    return self.arguments
  
  def evaluate_response(self, lowered):

    pattern = r"^!(\w+%?)(.*)"
    match = re.match(pattern, lowered)

    if match: 
      self.command = match.group(1)
      print("command " + self.command)
      self.arguments = match.group(2).strip()
      information = command_outputter([self.command, self.arguments])
      return information
    return "That is not a viable command"





  # print(lowered)
  # if lowered == '':
  #   return "Arei Bhai, kuch bhol na"
