import discord

from discord.ext import commands


from apis import *

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print ("I'm Ready!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am your master troubleshooter")

@bot.command()
async def ass(ctx):
    await ctx.send("Bend over and give it to me")

@bot.command()
async def dumbo(ctx):
    await ctx.send("It's what you are")


bot.run (TOKEN)