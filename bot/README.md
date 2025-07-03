# JokicBot - Discord Slash Commands

A Discord bot that provides fantasy basketball stats using ESPN's API with modern slash commands.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file:**
   ```bash
   # Copy the template and rename to .env
   cp env_template.txt .env
   ```

3. **Add your Discord bot token to `.env`:**
   ```
   TOKEN=your_discord_bot_token_here
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

## Available Commands

- `/stats <player> [stat]` - Get fantasy basketball stats for a player
  - Example: `/stats LeBron James ppg`
  - Available stats: ppg, rpg, apg, spg, bpg, fg%, ft%, 3pm, etc.

- `/player <player>` - Get detailed player information
  - Example: `/player LeBron James`

- `/help` - Show available commands and usage

- `/ping` - Check bot latency

## Features

- Modern slash command interface
- Real-time ESPN fantasy basketball data
- Player stat lookups
- Error handling and user-friendly messages
- Automatic command syncing

## Environment Variables

- `TOKEN` - Your Discord bot token
- `LEAGUE_ID` - ESPN fantasy league ID
- `ESPN_S2` - ESPN S2 authentication token
- `ESPN_SWID` - ESPN SWID authentication token 