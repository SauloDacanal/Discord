import io
import discord
from discord.ext import commands
from discord import app_commands
import random

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync()
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(name = 'teste', description='Testando') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Estou funcionando!", ephemeral = True)


@tree.command(name = 'dado', description='Dado_de_15_lados') 
async def slash3(interaction: discord.Interaction):
    variavel = random.randint(1,15)
    await interaction.response.send_message(f"O valor é: {variavel}", ephemeral = True)

aclient.run('')