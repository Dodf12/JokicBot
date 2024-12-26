from responses import Responses, command_outputter
import discord

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

    embed.set_thumbnail
    # Add footer
    embed.set_footer(text= str(embed.timestamp) + "|Data fetched live")
    return embed