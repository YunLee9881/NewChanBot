import requests
import discord
import random
import os


from discord.ext import commands
from discord import app_commands


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

MyGuild = discord.Object(id=1148901619765874718)


class Chan(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=MyGuild)
        self.synced = True
        print(f"{bot.user} is ready")


bot = Chan()
tree = app_commands.CommandTree(bot)


@tree.command(
    name="챤하",
    description="회의 등록하기",
    guild=MyGuild,
)
async def meeting(interaction: discord.Interaction):
    user = interaction.user
    await interaction.response.send_message(f"{user.mention} 챤하!")


bot.run("MTE2MzM5MDY5NTE1NTk3ODMyMA.G_Hfry.6zreIMvz2Oaism1K1d3sBYGWYm9AbzqgHaI4EI")
