import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NzExMzg5Nzc1ODQ4MDEzODQ1.XsFw3w.24LsNuW7p1bORtMxSb-MHY7OpZw')
