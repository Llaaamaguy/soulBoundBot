import discord
from discord.ext import commands, tasks
from pretty_help import DefaultMenu, PrettyHelp
import os
import requests

TOKEN = os.environ["DISCORD_AUTH"]
bot = commands.Bot(command_prefix="sb.", intents=discord.Intents.all())


# When the bot is turned on, print out bot has connected
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord")
    check_server.start()


# Every 2.5 minutes, check the web server for new badge earns
@tasks.loop(seconds=120)
async def check_server():
    # Define the channel to send updates in
    channel = bot.get_channel(826939307390402623)
    # Get the data
    r = requests.get("https://soulbound.llaamaguy.repl.co/data")
    # Parse and send the data to the defined channel
    data = r.json()
    data = data["response"]
    for k, v in data.items():
        k = k.split()
        await channel.send(k[0] + ": " + str(v))


bot.run(TOKEN)
