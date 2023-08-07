import discord
from discord.ext import commands

client = commands.bot(command_prefix = '!')

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("----------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am your personal Master Troubleshooter")


client.run('MTEzNzk0NzQ3NDA5MTMxNTI1Mg.GC-Z2E.e9FJIDqdrpkr0wP18F5rdjwg_EVGdf5AJ5uens')