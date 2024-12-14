import string
import re



def get_response(user_input): #makes user input all howercase
  lowered = user_input.lower()
  return lowered

def evaluate_response(lowered):

  pattern = r"^!(\w+)(.*)"

  match = re.match(pattern, lowered)

  if match: 
    command = match.group(1)
    arguments = match.group(2).strip()
    return command + " " + arguments
  return "That is not a viable command"



  # print(lowered)
  # if lowered == '':
  #   return "Arei Bhai, kuch bhol na"
