import discord
from discord.ext import commands
from discord import Intents
from config import token
from manager import DataBase


default_intents = discord.Intents.default()
default_intents.members = True

bot = commands.Bot(command_prefix="!",help_command=None,intents=Intents.all())
database = DataBase()
@bot.event
async def on_ready():
    print(f"{bot.user.name} est connecté !")


@bot.command()
async def create_account(ctx):
    await database.new_account(ctx,ctx.author)

@bot.command()
async def account(ctx):
    await database.open_account(ctx,ctx.author)


bot.run(token)