import discord
from discord.ext import commands


from apis import *

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print ("I'm Ready!")

if message.content.startswith('!hello'):
    await message.channel.send('Hello bro!')

bot.run (TOKEN)