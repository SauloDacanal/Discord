import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready():
    print(f'estou pronto e logado como {bot.user}')

@bot.command()
async def dado(ctx, numero):
    variavel = random.randint(1,int(numero))
    await ctx.send(f'O número que saiu no dado é {variavel}')

















bot.run('')