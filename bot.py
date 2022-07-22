import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="FR!")  #這個機器人


@bot.event
async def on_ready():
    print("|████████████████████████████████|")
    print("SETTINGS ALL DONE")
    print("->> BOT ALREADY ONLINE <<-")

bot.run("OTkyMzU0MTc0MzcxMTEwOTIz.G0cEzn.k0AoRB4gbYg1UQZsehBZDiOYmznEGNVVVEXHow")