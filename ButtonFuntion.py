import discord
from variable_manager import variable

meetingCount = variable()


class Meeting_Check(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)
        self.add_item(
            discord.ui.Button(
                label="Click Here", url="https://github.com/YunLee9881/NewChanBot"
            )
        )

    @discord.ui.button(label="회의", style=discord.ButtonStyle.success, row=1)
    async def button1(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message("회의를 누르셨습니다")
        meetingCount.increase_meeting()

    @discord.ui.button(label="강한 공지", style=discord.ButtonStyle.danger, row=1)
    async def button2(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message("secondary 누르셨습니다")
