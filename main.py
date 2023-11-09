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
from ButtonFuntion import Meeting_Check
from Select_place import SelectPlace
import ButtonFuntion


token = variable_manager.bot_token
id = variable_manager.server_id

meetingCount = ButtonFuntion.meetingCount
# variable_meeting = variable()

MyGuild = discord.Object(id=id)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


# tree = app_commands.CommandTree(bot)
@bot.event
async def on_ready():
    print(f"{bot.user}is ready")


@bot.tree.command(name="select", description="select", guild=MyGuild)
async def meeting_place(interaction: Interaction):
    select = ui.Select
    view = SelectPlace()

    async def select_callback(self, interaction: Interaction):
        if interaction.data["values"][0] == "1":
            await interaction.response.send_message("1번 선택!")
        elif interaction.data["values"][0] == "2":
            await interaction.response.send_message("2번 선택!")
        elif interaction.data["values"][0] == "3":
            await interaction.response.send_message("3번!")
        elif interaction.data["values"][0] == "4":
            await interaction.response.send_message("4번!")
        elif interaction.data["values"][0] == "5":
            interaction.response.send_message("5번!")
        # await interaction.response.send_message(f"{interaction.data['values'][0]}")

    select.callback = select_callback
    await interaction.response.send_message(view=view)


@bot.tree.command(
    guild=MyGuild,
    name="button",
    description="button 만들기",
)
async def mkbutton(
    interaction: Interaction,
):
    button = ui.Button(style=ButtonStyle.green, label="안녕하세요", disabled=False)
    view = Meeting_Check()

    async def button_callback(interaction: Interaction):
        await bot.tree.get_command("select").callback(interaction)

    button.callback = button_callback
    await interaction.response.send_message(view=view)


@bot.tree.command(name="test", description="as", guild=MyGuild)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("ㅎㅇ")


@bot.tree.command(
    name="챤하",
    description="회의 시작하기",
    guild=MyGuild,
)
async def meeting(interaction: discord.Interaction):
    user = interaction.user
    await interaction.response.send_message(f"{user.mention} 챤하!")


@bot.tree.command(name="오회보", description="오늘 회의 보여줘의 준말", guild=MyGuild)
async def meeting_log(interaction: discord.Interaction):
    # meeting_cnt = meetingCount.meeting_count
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


# @bot.tree.command(name="embed", description="엠베드", guild=MyGuild)
# async def profile(interaction: discord.Interaction, member: discord.Member = None):
#     if member == None:
#         member = interaction.author

#     name = member.display_name
#     pfp = member.display_avatar

#     embed = discord.Embed(
#         title="난 짬뽕이오", description="머 으쯔라구요 ㅡㅡ", color=discord.Colour.random()
#     )
#     embed.set_author(
#         name=f"{name}",
#         url="https://blog.msg-team.com/",
#         icon_url="https://ibb.co/TbRXSbz",
#     )
#     embed.set_thumbnail(url=f"{pfp}")
#     embed.add_field(name="this is 1 field", value="this is just a value")
#     embed.add_field(name="this is 1 field", value="this is just a value", inline=True)
#     embed.add_field(name="this is 1 field", value="this is just a value", inline=False)
#     embed.set_footer(text=f"{name}Made this Embed")

#     await interaction.response.send_message(embed=embed)


bot.run(token)
