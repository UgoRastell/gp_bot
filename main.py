import discord
import asyncio
from discord.ext import commands
import interactions

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')

@client.event
async def on_message(message):
    print(message.author.name)


@client.command(
name="my_first_command",
description="This is the first command I made!",
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")


client.run("MTA2MzA2NjAyMzY1OTU4MTQ1MA.GEG0rX.Wb3n9e0X30umNxJyPkqIyWSPNknrhzJSkxQdfs")

