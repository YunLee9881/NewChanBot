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
