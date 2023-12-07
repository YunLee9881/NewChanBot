import requests
import discord
import os
import json
from discord.ext import commands
import re
import variable_manager
import asyncio


token = variable_manager.bot_token
lsm_id = variable_manager.lsm_id

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


class LinkButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(
            discord.ui.Button(
                label="OpenAI",
                url="https://www.openai.com",
                style=discord.ButtonStyle.link,
            )
        )


class Myview(discord.ui.View):
    @discord.ui.button(label="회의목록", style=discord.ButtonStyle.primary)
    async def button1_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.send_message("")

    @discord.ui.button(label="잡담", style=discord.ButtonStyle.success)
    async def button2_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.send_message("나랑 잡담할 시간에 공부해!")

    @discord.ui.button(label="Issue", style=discord.ButtonStyle.danger)
    async def button3_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.send_message(f"이쪽으로! <@{lsm_id}>")


class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="4층 홈베", value="1"),
            discord.SelectOption(label="3층 홈베", value="2"),
            discord.SelectOption(label="2층 홈베", value="3"),
            discord.SelectOption(label="Complex Zone", value="4"),
            discord.SelectOption(label="기숙사", value="5"),
        ]
        super().__init__(
            placeholder="선택하세요", min_values=1, max_values=1, options=options
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"선택한 항목: {self.values[0]}")


class SelectView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())


@bot.event
async def on_ready():
    print(f"{bot.user}is ready")


@bot.command(name="챤하")
async def button(ctx):
    await ctx.send("버튼 입니다", view=Myview())


@bot.command()
async def time(ctx):
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


@bot.command(name="ㅅㅌ")
async def select(ctx: commands.Context):
    view = SelectView()
    await ctx.send("회의를 진행할 장소를 선택해주세요:", view=view)


bot.run(token)
