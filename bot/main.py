import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
from api.playerFantasyStats import find_player_obj, getPlayerPPG, getOtherPlayerStats, league
from UI.gui import Gui

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Discord TOKEN is not set! Check your .env file and make sure TOKEN=your_token is present.")


# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name="stats", description="Get a player's NBA basketball stats")
@app_commands.describe(
    player="The player's name (e.g., 'LeBron James')",
    stat="The stat you want to see (e.g., 'ppg', 'rpg', 'apg', 'spg', 'bpg')"
)
async def stats(interaction: discord.Interaction, player: str, stat: str = "ppg"):
    """Get NBA basketball stats for a player"""
    await interaction.response.defer()
    
    try:
        # Create GUI object
        gui = Gui()
        
        # Get player stats - always use getOtherPlayerStats for real NBA stats
        result = getOtherPlayerStats(player, stat)
        
        # Create embed with the stats
        embed = gui.playerStatsGUI(player, result, stat)
        
        await interaction.followup.send(embed=embed)
        
    except Exception as e:
        error_embed = discord.Embed(
            title="Error",
            description=f"Failed to get stats for {player}: {str(e)}",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=error_embed)

@bot.tree.command(name="fantasyppg", description="Get a player's fantasy basketball points")
@app_commands.describe(
    player="The player's name (e.g., 'LeBron James')"
)
async def fantasy(interaction: discord.Interaction, player: str):
    """Get fantasy basketball points for a player"""
    await interaction.response.defer()
    
    try:
        # Create GUI object
        gui = Gui()
        
        # Get fantasy points
        result = getPlayerPPG(player)
        
        # Create embed with the fantasy points
        embed = gui.fantasyPointsGUI(player, result)
        
        await interaction.followup.send(embed=embed)
        
    except Exception as e:
        error_embed = discord.Embed(
            title="Error",
            description=f"Failed to get fantasy points for {player}: {str(e)}",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=error_embed)

@bot.tree.command(name="player", description="Get detailed player information")
@app_commands.describe(
    player="The player's name (e.g., 'LeBron James')"
)
async def player(interaction: discord.Interaction, player: str):
    """Get detailed player information"""
    await interaction.response.defer()
    
    try:
        # Find the player object
        player_obj = find_player_obj(player)
        
        if player_obj:
            embed = discord.Embed(
                title=f"🏀 {player_obj.name}",
                color=discord.Color.blue()
            )
            
            # Add player stats
            embed.add_field(
                name="📊 Season Stats",
                value=f"**Fantasy PPG:** {player_obj.avg_points}\n"
                      f"**Team:** {player_obj.proTeam}\n"
                      f"**Position:** {player_obj.position}",
                inline=False
            )
            
            # Add available stats
            if hasattr(player_obj, 'stats') and '2025_total' in player_obj.stats:
                stats = player_obj.stats['2025_total']['avg']
                stats_text = "\n".join([f"**{stat.upper()}:** {value}" for stat, value in stats.items()])
                embed.add_field(name="📈 Available NBA Stats", value=stats_text, inline=False)
            
            embed.set_footer(text="Use /stats <player> <stat> for NBA stats or /fantasyppg <player> for fantasy points")
            
        else:
            embed = discord.Embed(
                title="❌ Player Not Found",
                description=f"Could not find player: {player}",
                color=discord.Color.red()
            )
        
        await interaction.followup.send(embed=embed)
        
    except Exception as e:
        error_embed = discord.Embed(
            title="Error",
            description=f"Failed to get player info: {str(e)}",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=error_embed)

@bot.tree.command(name="help", description="Show available commands and stats")
async def help_command(interaction: discord.Interaction):
  
    embed = discord.Embed(
        title="🏀 JokicBot Commands",
        description="Here are the available commands:",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="/stats <full player name> [stat]",
        value="Get NBA basketball stats for a player\n"
              "**Example:** `/stats LeBron James ppg`\n"
              "**Available stats:** ppg, rpg, apg, spg, bpg, fg%, ft%, 3pm, etc.",
        inline=False
    )
    
    embed.add_field(
        name="/fantasyppg <player>",
        value="Get fantasy basketball points for a player\n"
              "**Example:** `/fantasyppg LeBron James`",
        inline=False
    )
    
    embed.add_field(
        name="/player <player>",
        value="Get all player information\n"
              "**Example:** `/player LeBron James`",
        inline=False
    )

    embed.add_field(
        name="/teams",
        value="Get a list of all teams in your league",
        inline=False
    )
    
    embed.add_field(
        name="/help",
        value="Show this help message",
        inline=False
    )
    
    embed.set_footer(text="Powered by ESPN Fantasy Basketball API")
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ping", description="Check if the bot is responsive")
async def ping(interaction: discord.Interaction):
    """Check bot latency"""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong",
        description=f"Bot latency: {latency}ms",
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="teams", description="Get a list of all teams in your league")
async def teams(interaction: discord.Interaction):

    await interaction.response.defer()
    embed = discord.Embed(
        title="🏀 Teams in Your League",
        description="Here are the teams in your league:",
        color=discord.Color.blue()
    )
            # Get all teams from the league
    team_list = []
    for team in league.teams:
        # Create team info string
        wins = team.wins if hasattr(team, 'wins') else 'N/A'
        losses = team.losses if hasattr(team, 'losses') else 'N/A'
        record = f"{wins}-{losses}"
        
        team_info = f"**{team.team_name}** - Record: {record}"
        team_list.append(team_info)
    
    # Add teams to embed
    if team_list:
        teams_text = "\n".join(team_list)
        embed.add_field(name="Teams", value=teams_text, inline=False)
    else:
        embed.add_field(name="No Teams Found", value="Could not load teams from the league.", inline=False)


    await interaction.followup.send(embed=embed)

@bot.tree.command(name="matchups", description="Current matchups in your league or for specific team")
@app_commands.describe(
    team="The team's name (optional)"
)
async def matchups(interaction: discord.Interaction, team: str = None):
    await interaction.response.defer()  # Add this!
    
    try:
        embed = discord.Embed(
            title="🏀 Current Matchups",
            description="Here are the current matchups in your league:",
            color=discord.Color.red()
        )

        # Get current week's matchups
        current_week = league.current_week
        matchups_list = []
        
        # Get matchups for current week
        for matchup in league.box_scores(current_week):
            # Get team objects properly
            home_team = matchup.home_team
            away_team = matchup.away_team
            
            # If teams are IDs, get the actual team objects
            if isinstance(home_team, int):
                home_team = league.get_team(home_team)
            if isinstance(away_team, int):
                away_team = league.get_team(away_team)
            
            # Skip if we can't get team objects
            if not home_team or not away_team:
                continue
                
            # If specific team requested, filter for that team
            if team:
                team_lower = team.lower()
                if (home_team.team_name.lower() != team_lower and 
                    away_team.team_name.lower() != team_lower):
                    continue
            
            # Get scores
            home_score = getattr(matchup, 'home_score', 'N/A')
            away_score = getattr(matchup, 'away_score', 'N/A')
            
            matchups_list.append(f"{home_team.team_name} vs {away_team.team_name}")
            
            embed.add_field(
                name=f"{home_team.team_name} vs {away_team.team_name}",
                value=f"**{home_team.team_name}:** {home_score} points\n"
                      f"**{away_team.team_name}:** {away_score} points\n"
                      f"**Week:** {current_week}",
                inline=False
            )
        
        if not matchups_list:
            if team:
                embed.add_field(
                    name="No Matchups Found", 
                    value=f"No matchups found for team: {team}", 
                    inline=False
                )
            else:
                embed.add_field(
                    name="No Matchups Found", 
                    value="No matchups available for this week.", 
                    inline=False
                )
        
        embed.set_footer(text=f"Week {current_week} Matchups")
        
        await interaction.followup.send(embed=embed)
        
    except Exception as e:
        error_embed = discord.Embed(
            title="Error",
            description=f"Failed to get matchups: {str(e)}",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=error_embed)

@bot.tree.command(name="roster", description="View the roster for a specific team")
@app_commands.describe(
    team="The team's name is required"
)
async def roster(interaction: discord.Interaction, team: str):
    """View the roster for a specific team"""
    await interaction.response.defer()
    
    # Find the team object by searching through all teams
    team_obj = None
    for t in league.teams:
        if t.team_name.lower() == team.lower():
            team_obj = t
            break
    
    if not team_obj:
        # Try partial matching if exact match fails
        for t in league.teams:
            if team.lower() in t.team_name.lower():
                team_obj = t
                break
    
    if not team_obj:
        # Show available teams if team not found
        available_teams = [t.team_name for t in league.teams]
        teams_list = "\n".join(available_teams)
        
        embed = discord.Embed(
            title="❌ Team Not Found",
            description=f"Could not find team: **{team}**\n\n**Available teams:**\n{teams_list}",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=embed)
        return
    
    # Create embed for the roster
    embed = discord.Embed(
        title=f"🏀 {team_obj.team_name} Roster",
        description=f"Current roster for {team_obj.team_name}",
        color=discord.Color.blue()
    )
    
    # Add players to the embed using team.roster (not team.players)
    if hasattr(team_obj, 'roster') and team_obj.roster:
        players_list = []
        for player in team_obj.roster:
            # Get player info
            name = player.name if hasattr(player, 'name') else 'Unknown'
            position = player.position if hasattr(player, 'position') else 'N/A'
            pro_team = player.proTeam if hasattr(player, 'proTeam') else 'N/A'
            
            players_list.append(f"**{name}** - {position} ({pro_team})")
        
        if players_list:
            # Split into chunks if too long for Discord
            players_text = "\n".join(players_list)
            if len(players_text) > 1024:  # Discord embed field limit
                # Split into multiple fields
                chunks = [players_list[i:i+10] for i in range(0, len(players_list), 10)]
                for i, chunk in enumerate(chunks):
                    field_name = f"Players {i*10+1}-{i*10+len(chunk)}" if i > 0 else "Players"
                    embed.add_field(
                        name=field_name, 
                        value="\n".join(chunk), 
                        inline=False
                    )
            else:
                embed.add_field(name="Players", value=players_text, inline=False)
        else:
            embed.add_field(name="No Players Found", value="This team has no players.", inline=False)
    else:
        embed.add_field(name="No Roster Data", value="Could not load roster for this team.", inline=False)
    
    # Add team record if available
    if hasattr(team_obj, 'wins') and hasattr(team_obj, 'losses'):
        embed.add_field(
            name="Record", 
            value=f"{team_obj.wins}-{team_obj.losses}", 
            inline=True
        )
    
    embed.set_footer(text="Powered by ESPN Fantasy Basketball API")
    
    await interaction.followup.send(embed=embed)
        
# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)