import discord
from datetime import datetime
from zoneinfo import ZoneInfo

class Gui:
    def __init__(self):
        self.logo_url = "https://raw.githubusercontent.com/Dodf12/JokicBot/main/assets/jokicBotLogo.png"

    def playerStatsGUI(self, player_name, stat_result, statName):
        """Create an embed for player stats"""
        embed = discord.Embed(
            title=f"🏀 {player_name.title()} {statName}",
            description=f"**{stat_result}**",
            color=discord.Color.from_rgb(128, 0, 255)  # Vibrant purple
        )

        # Author icon (small circle)
        embed.set_author(
            name="JokicBot",
            icon_url=self.logo_url
        )

        # Thumbnail (large square on the right)
        embed.set_thumbnail(url=self.logo_url)

        # Add fields for player info
        embed.add_field(name="Player", value=f"`{player_name.title()}`", inline=True)
        embed.add_field(name="Stat", value=f"`{stat_result}`", inline=True)
        embed.add_field(name="Tip", value="Use `/help` for all commands!", inline=False)

        # Footer with timestamp
        timezone = ZoneInfo("America/Los_Angeles")
        local_time = datetime.now(timezone)
        embed.set_footer(text=f"Data fetched live | {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

        return embed

    def fantasyPointsGUI(self, player_name, fantasy_points):
        embed = discord.Embed(
            title=f"🎯 {player_name.title()} Fantasy Points",
            description=f"**{fantasy_points}** fantasy points per game",
            color=discord.Color.from_rgb(255, 165, 0)  # Orange for fantasy
        )

        embed.set_author(
            name="JokicBot",
            icon_url=self.logo_url
        )

        # Thumbnail (large square on the right)
        embed.set_thumbnail(url=self.logo_url)

        # Add fields for player info
        embed.add_field(name="Player", value=f"`{player_name.title()}`", inline=True)
        embed.add_field(name="Fantasy PPG", value=f"`{fantasy_points}`", inline=True)
        embed.add_field(name="Tip", value="Use `/stats <player> <stat>` for NBA stats!", inline=False)

        # Footer with timestamp
        timezone = ZoneInfo("America/Los_Angeles")
        local_time = datetime.now(timezone)
        embed.set_footer(text=f"Fantasy data fetched live | {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

        return embed

    def errorGUI(self, error_message):
        """Create an embed for error messages"""
        embed = discord.Embed(
            title="❌ Error",
            description=error_message,
            color=discord.Color.red()
        )

        embed.set_author(
            name="JokicBot",
            icon_url=self.logo_url
        )

        embed.set_footer(text="Use /help for available commands")

        return embed

    def successGUI(self, title, message):
        """Create an embed for success messages"""
        embed = discord.Embed(
            title=f"✅ {title}",
            description=message,
            color=discord.Color.green()
        )

        embed.set_author(
            name="JokicBot",
            icon_url=self.logo_url
        )

        return embed