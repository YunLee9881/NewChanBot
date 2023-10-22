import variable_manager
import discord
from discord.ext import commands


class Meeting(discord.ui.View):
    @discord.ui.button(label="눌러!", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("눌렀네?")
