from responses import Responses, command_outputter
import discord
from datetime import datetime
from zoneinfo import ZoneInfo

class Gui:
    def __init__(self):
        self.req = ""

    def playerStatsGUI(self, u_msg):
        print( "message" + u_msg)
        obj = Responses()
        response = obj.evaluate_response(u_msg)
        logo_url = "https://raw.githubusercontent.com/Dodf12/JokicBot/main/assets/jokicBotLogo.png"

        embed = discord.Embed(
            title=f"🏀 {obj.getCommand()} {response} 🏀",
            description="**Welcome to JokicBot!**\nGet live NBA player stats and more.",
            color=discord.Color.from_rgb(128, 0, 255)  # Vibrant purple
        )

        # Author icon (small circle)
        embed.set_author(
            name="JokicBot",
            icon_url=logo_url
        )

        # Thumbnail (large square on the right)
        embed.set_thumbnail(url=logo_url)

        # Example fields for player info
        embed.add_field(name="Player", value=f"`{obj.getArguments()}`", inline=True)
        embed.add_field(name="Command", value=f"`{obj.getCommand()}`", inline=True)
        embed.add_field(name="Tip", value="Type `@JokicBot help` for all commands!", inline=False)

        # Optional: Add a banner or gradient image (if you have one)
        # embed.set_image(url="https://your-banner-or-gradient-image-url.png")

        # Footer with timestamp
        timezone = ZoneInfo("America/Los_Angeles")
        local_time = datetime.now(timezone)
        embed.set_footer(text=f"Data fetched live | {local_time}")

        return embed