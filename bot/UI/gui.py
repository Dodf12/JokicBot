from responses import Responses, command_outputter
import discord

from datetime import datetime
from zoneinfo import ZoneInfo

class Gui:
  def __init__(self):
    self.req = ""

  def playerStatsGUI(self, u_msg):
    obj = Responses()
    response = obj.evaluate_response(u_msg)
    embed = discord.Embed(
        title= response,
        description="" + obj.getArguments() + "'s " + obj.getCommand(),
        color=discord.Color.purple()
    )

    embed.set_thumbnail(url="https://raw.githubusercontent.com/Dodf12/JokicBot/blob/main/assets/jokicBotLogo.png")

    # Add footer

    # Specify the time zone
    timezone = ZoneInfo("America/Los_Angeles")

    # Get the current time in the specified time zone
    local_time = datetime.now(timezone)


    embed.set_footer(text="Data fetched live | " + str(local_time))
    return embed
  

    #   localTime = str(datetime.now(ZoneInfo("America/Los_Angeles")))
    # footer =  " " localTime + "|Data fetched live"