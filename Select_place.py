from discord import app_commands, Interaction, ui, ButtonStyle, SelectOption
import discord


class selectPlace(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)

    @discord.ui.select()
    async def Select():
        select = ui.Select(placeholder="select")
        select.ui.add_option(label="hi", value=1, description="hihi")
        select.ui.add_option(label="bye", value=2, description="byebye")
