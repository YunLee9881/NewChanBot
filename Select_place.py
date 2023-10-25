from discord import app_commands, Interaction, ui, ButtonStyle, SelectOption
import discord


class SelectPlace(discord.ui.View):
    def __init__(self):
        super().__init__()

        select = discord.ui.Select(placeholder="Select")
        select.add_option(label="2층 홈베", value="1", description="")
        select.add_option(label="3층 홈베", value="2", description="")
        select.add_option(label="4층 홈베", value="3", description="")
        select.add_option(label="Complex Zone", value="4", description="")
        select.add_option(label="기숙사 자습실", value="5", description="")

        self.add_item(select)
