from discord import Intents, Client, Message  
import responses 
import os
from dotenv import load_dotenv, dotenv_values

#Load token
load_dotenv()
TOKEN = os.getenv("TOKEN")
  


#print(TOKEN)
#Token is working properl

#SETTING UP THE BOT

#1. Activing the intents
#permission the bot needs to see the messages and respond

#Allow the bot to respond to input
intents = Intents.default()
#Allowing bot to asnwer questions
intents.message_content = True
#Client connection to discord API and websocket
Client = Client(intents=intents)

#2. Message Functionality

"""
async is a feature that allows a program to execute
many tasks concurrently
"""

async def sendMessage(message, user_message):
  if user_message == "":
    print("Intent not enabled")

  if user_message[0] == '?':
    user_message = user_message[1:]

  """
  A try block lets us test a block of code 
  for errors and except block lets us handle them
  """
  #Sees if user wants a private message in channel or public message
  try:
    response = responses.evaluate_response(user_message)
    await message.author.send(response) if user_message[0] == '?' else await message.channel.send(response)
  except Exception as e:
    print(e)


#3. Handling the Startup for Bot
#This section is to make sure we can see that the bot is up and running

"""
A decorator is like a function in another function.
It is used to give more behavior to the function with
out needing to add to it, or use another function to get to it

"""
@Client.event #This is a decorator functin
async def on_ready():
  print("Client user is now running")


#4 Handling INCOMING MESSAGES
#Makes sure bot is not just talking to itself like a pyscho
@Client.event
async def on_message(message):
  #THe bot is the one to write the message and shouldnt reply to itself
  if message.author == Client.user:
    return

  username = str(message.author)
  user_message = message.content
  channel = message.channel

  #print(channel + " " + user_message)
  await sendMessage(message, user_message)


#5. MAIN POINT
def main():
  Client.run(token=TOKEN)

if __name__ == "__main__":
  main()