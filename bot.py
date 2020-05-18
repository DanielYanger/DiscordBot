import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@client.command()
async def test(ctx, arg):
    await ctx.send(arg)


@client.command()
async def display(ctx, arg1, arg2):
    channel = ctx.message.channel
    embed = discord.Embed(
        title=arg1,
        description=arg2,
        colour=discord.Color.green()
    )
    await channel.send(embed=embed)


client.run('NzExMzg5Nzc1ODQ4MDEzODQ1.XsFw3w.24LsNuW7p1bORtMxSb-MHY7OpZw')
