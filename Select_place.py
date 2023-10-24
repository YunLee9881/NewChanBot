from discord import app_commands, Interaction, ui, ButtonStyle, SelectOption
import discord


class SelectPlace(discord.ui.View):
    def __init__(self):
        super().__init__()

        select = discord.ui.Select(placeholder="Select")
        select.add_option(label="hi", value="1", description="hihi")
        select.add_option(label="bye", value="2", description="byebye")

        self.add_item(select)
