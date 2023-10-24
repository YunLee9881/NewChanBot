import requests
import discord
import random
import os
import json
import meeting
from discord.ext import commands
from discord import app_commands

import variable_manager
from variable_manager import variable
from discord import app_commands, Interaction, ui, ButtonStyle, SelectOption


token = variable_manager.bot_token
id = variable_manager.server_id

meetingCount = variable()
# variable_meeting = variable()

MyGuild = discord.Object(id=id)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)


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


class ButtonFunction(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)
        self.add_item(
            discord.ui.Button(label="Click Here", url="http://aochfl.tistory.com")
        )

    @discord.ui.button(label="primary", style=discord.ButtonStyle.primary, row=1)
    async def button1(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message("primary 누르셨습니다")

    @discord.ui.button(label="secondary", style=discord.ButtonStyle.secondary, row=1)
    async def button2(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message("secondary 누르셨습니다")

    @discord.ui.button(label="success", style=discord.ButtonStyle.success, row=2)
    async def button3(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message("success 누르셨습니다")

    @discord.ui.button(label="danger", style=discord.ButtonStyle.danger, row=2)
    async def button4(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message("danger 누르셨습니다")


@tree.command(
    guild=MyGuild,
    name="button",
    description="button 만들기",
)
async def mkbutton(interaction: Interaction):
    button = ui.Button(style=ButtonStyle.green, label="안녕하세요", disabled=False, row=2)
    view = ButtonFunction()

    async def button_callback(interaction: Interaction):
        await interaction.response.send_message(content="버튼 눌러짐!")

    button.callback = button_callback
    await interaction.response.send_message(view=view)


@tree.command(
    name="챤하",
    description="회의 시작하기",
    guild=MyGuild,
)
async def meeting(interaction: discord.Interaction):
    user = interaction.user
    await interaction.response.send_message(f"{user.mention} 챤하!")
    meetingCount.increase_meeting()


@tree.command(name="오회보", description="오늘 회의 보여줘의 준말", guild=MyGuild)
async def meeting_log(interaction: discord.Interaction):
    if meetingCount.meeting_count == 0:
        await interaction.response.send_message(f"오늘 회의는 없어요!")
    elif meetingCount.meeting_count == 1:
        await interaction.response.send_message(f"오늘은 회의가 한 개!")
    elif meetingCount.meeting_count == 2:
        await interaction.response.send_message(f"오늘은 회의가 두개지요...")
    else:
        await interaction.response.send_message(
            f"오늘은! {meetingCount.meeting_count}개에요 다들 힘내요!"
        )


bot.run(token)
