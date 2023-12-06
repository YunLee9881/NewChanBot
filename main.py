import requests
import discord
import os
import json
from discord.ext import commands
import re
import variable_manager
import asyncio

token = variable_manager.bot_token


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


@bot.command(name="선택")
async def select(ctx):
    await ctx.send("시간을 입력하세요 단 형식은 00:00으로 입력해주셔야해요!.")

    def check(m):
        email_regex = r"\b[0-9]+:[0-9]{2,}\b"
        return (
            m.author == ctx.author
            and m.channel == ctx.channel
            and re.fullmatch(email_regex, m.content)
        )

    try:
        msg = await bot.wait_for("message", check=check, timeout=15)
        await ctx.send(f"입력된 시간: {msg.content}")
    except asyncio.TimeoutError:
        await ctx.send("30초 동안 입력이 없어 기능이 비활성화되었습니다.")


bot.run(token)
