import discord
from discord.ext import commands

from apis import *

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print ("I'm Ready!")

bot.run(TOKEN)