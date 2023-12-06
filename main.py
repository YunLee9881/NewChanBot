import requests
import discord
import os
import json
from discord.ext import commands

import variable_manager

token = variable_manager.bot_token
id = variable_manager.server_id

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


class Myview(discord.ui.View):
    @discord.ui.button(label="눌러!", style=discord.ButtonStyle.primary)
    async def button_callback(self, button: discord.ui.Button, interaction):
        await interaction.response.send_message("눌렀네?")


@bot.event
async def on_ready():
    print(f"{bot.user}is ready")


@bot.command(name="챤하")
async def button(ctx):
    await ctx.send("버튼 입니다", view=Myview())


bot.run(token)
