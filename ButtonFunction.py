import requests
import discord
import os
import json
from discord.ext import commands
import variable_manager


lsm_id = variable_manager.lsm_id


class Button(discord.ui.View):
    @discord.ui.button(label="회의목록", style=discord.ButtonStyle.primary)
    async def button1_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.send_message("glg")
        button.disabled = True  # 버튼 비활성화

    @discord.ui.button(label="잡담", style=discord.ButtonStyle.success)
    async def button2_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        user_id = interaction.user.id
        await interaction.response.send_message(
            f"<@{user_id}>님, 나랑 잡담할 시간에 공부해!",
            allowed_mentions=discord.AllowedMentions(users=True),
        )
        button.disabled = True  # 버튼 비활성화

    @discord.ui.button(label="Call", style=discord.ButtonStyle.danger)
    async def button3_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.send_message(f"이쪽으로! <@{lsm_id}>")
        button.disabled = True  # 버튼 비활성화


class Meet_Button(discord.ui.View):
    @discord.ui.button(label="커피챗", style=discord.ButtonStyle.primary)
    async def button1_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.send_message("커피챗을 진행할 상대를 골라주세요!")
        return 1

    @discord.ui.button(label="1on1", style=discord.ButtonStyle.success)
    async def button2_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        user_id = interaction.user.id
        await interaction.response.send_message("1on1을 진행할 상대를 골라주세요!")
        return 2

    @discord.ui.button(label="회의", style=discord.ButtonStyle.danger)
    async def button3_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.send_message(f"회의 멤버를 골라주세요!")
        return 3
