import discord
from discord.ext import commands
import csv
import API
from pathlib import Path

data_folder = Path("tip-game/")

file_to_open = data_folder / "tips.csv"

TOKEN = API.TOKEN
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
    with open(file_to_open, mode='a', newline='', encoding='utf-8') as tip_file:
        tip_writer = csv.writer(tip_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tip_writer.writerow([ctx.author, game_tip])
        await ctx.send(f"@{ctx.author} hat {game_tip} gewettet")
        
bot.run(TOKEN)