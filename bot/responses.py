import string
import re



def get_response(user_input): #makes user input all howercase
  lowered = user_input.lower()
  return lowered

def evaluate_response(lowered):
  if lowered == "!hello":
    return "flying"
  return "bombulu"

  print("happy 2")



  # print(lowered)
  # if lowered == '':
  #   return "Arei Bhai, kuch bhol na"
