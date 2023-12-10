import requests
import discord
import os
import json
from discord.ext import commands
import asyncio
import variable_manager


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
        self.variable_manager = variable_manager

    async def callback(self, interaction: discord.Interaction):
        self.selected_value = self.values[0]

        for option in self.options:
            if option.value == self.selected_value:
                self.selected_label = option.label
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        new_data = {f"place{self.variable_manager.count}": f"{self.selected_label}"}
        merged_data = {**data, **new_data}
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=4)
        self.variable_manager.count += 1
        await interaction.response.send_message(f"선택한 위치: {self.selected_label}")


class SelectView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.dropdown = Dropdown()
        self.add_item(self.dropdown)
