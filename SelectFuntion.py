import requests
import discord
import os
import json
from discord.ext import commands


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
