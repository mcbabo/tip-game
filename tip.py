import discord
from discord.ext import commands
import csv
import datetime
import api

TOKEN = api.TOKEN
bot = commands.Bot(command_prefix = "!")

@bot.command()
async def nextgame(ctx):
    with open('games.csv', mode='r') as games_file:
        reader = csv.reader(games_file)
        line = str(next(reader))
        remove_char = ["[", "]"]
        for character in remove_char:
            line = line.replace(character, "")
    await ctx.send(f"Nächstes Spiel ist am {line}")

@bot.command()
async def tip(ctx, game_tip):
    with open('tip.csv', mode='w') as tip_file:
        reader = csv.reader(tip_file, delimiter=',')
        for row in reader:
            for field in row:
                if field == ctx.author:
                    await ctx.send("Du bist schon im Tippspiel")
        tip_writer = csv.writer(tip_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tip_writer.writerow([ctx.author, game_tip])

bot.run(TOKEN)