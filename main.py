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

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

token = variable_manager.bot_token
id = variable_manager.server_id

meetingCount = variable()
# variable_meeting = variable()

MyGuild = discord.Object(id=id)


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
    guild=discord.Object(id=1148901619765874718),
    name="button",
    description="button 만들기",
)
async def mkbutton(interaction: Interaction):
    button = ui.Button(style=ButtonStyle.green, label="안녕하세요", disabled=False)
    view = ui.View()
    view.add_item(button)

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
