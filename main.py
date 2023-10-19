import requests
import discord
import random
import os
import json

from discord.ext import commands
from discord import app_commands


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

with open("Resource.Json") as config_file:
    config = json.load(config_file)

bot_token = config["bot_token"]
server_id = config["server_id"]

MyGuild = discord.Object(id=server_id)


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
    description="회의 시작하기",
    guild=MyGuild,
)
async def meeting(interaction: discord.Interaction):
    user = interaction.user
    await interaction.response.send_message(f"{user.mention} 챤하!")


bot.run(bot_token)
