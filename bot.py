from unittest import async_case
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
intents.presences = True


bot = commands.Bot(command_prefix="!-", intents=intents)  #this bot


@bot.event #-------------------Bot ready return
async def on_ready():
    print("████████████████████████████████")
    print("SETTINGS ALL DONE")
    print("->> BOT ALREADY ONLINE <<-")

@bot.event #-------------------User join msg
async def on_member_join(member):
    channel = bot.get_channel(999968465517543434)
    print(f'{member} has join the server.')
    await channel.send(f'{member} has join the server !') #Send MSG on server channel.

@bot.event #-------------------User remove msg
async def on_member_remove(member):
    channel = bot.get_channel(999968465517543434)
    print(f'{member} has leave the server.')
    await channel.send(f'{member} has leave the server !') #Send MSG on server channel.

@bot.event #-------------------Text return
async def on_message(message):
    if message.content == "Work?": #Bot working check
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send("Work")
        await message.channel.send(">100<")
        await message.channel.send("∣████████████████████████████████∣")

@bot.command() #-------------------Command
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} [ms/毫秒]')

async def say(ctx):
    await ctx.send(f'hello')


bot.run("") #Discord bot Token.
