import nextcord
import config
import os
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.event
async def on_ready():
    print(f'Hello, I am your personal Master OAS Troubleshooter')
    print('______________________________________________________')















bot.run(config.TOKEN)