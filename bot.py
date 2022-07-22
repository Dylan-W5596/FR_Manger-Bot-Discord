import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="FR!")  #這個機器人


@bot.event
async def on_ready():
    print("████████████████████████████████|")
    print("SETTINGS ALL DONE")
    print("->> BOT ALREADY ONLINE <<-")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(999968465517543434) #channel ID
    await channel.send(F"@{member} has join the Server!")

@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(999968465517543434) #channel ID
    await channel.send(F"@{member} has leave the Server!")

bot.run("") #Discord bot Token
