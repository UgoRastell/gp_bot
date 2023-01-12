import discord
import json

bot = discord.Bot()

@bot.command(description="Sends the bot's latency.") 
async def ping(ctx): 
    await ctx.respond(f"Pong! Latency is {bot.latency}")


bot.run("MTA2MzA2NjAyMzY1OTU4MTQ1MA.GnQpWR.B7VcCepxr47dOgLeB6bpgWwNLqsbcsMRpvQBm0")

