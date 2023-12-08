import requests
import discord
import os
import json
from discord.ext import commands
import re
import variable_manager
import asyncio
import SelectFuntion
import ButtonFuntion
from discord.utils import get
import MnM


token = variable_manager.bot_token


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
mention_to = MnM.MentionTo(bot)


@bot.slash_command(name="button", description="잡다잡다한 버튼")
async def button(ctx):
    await ctx.response.defer()
    await ctx.followup.send(
        content=f"안녕하세요, {ctx.author.name}님!", view=ButtonFuntion.Button()
    )


@bot.slash_command(name="mention", description="모두가 기다리던 && 멘션!")
async def mnm(ctx, role_name1: str, role_name2: str):
    await ctx.defer()
    result = await mention_to.find_members_with_role(ctx, role_name1, role_name2)
    await ctx.followup.send(content=result)


@bot.event
async def on_ready():
    print(f"{bot.user}is ready")


@bot.command(name="챤하")
async def meeting(ctx):
    await ctx.send("무엇을 하시겠어요?", view=ButtonFuntion.Meet_Button())
    mode = ButtonFuntion.Meet_Button()


@bot.command()
async def members(ctx):
    members = ctx.guild.members  # 서버의 모든 멤버를 가져옵니다.


@bot.command()
async def time(ctx):
    await ctx.send("시간을 입력하세요 단 형식은 00:00으로 입력해주셔야해요!")

    def check(m):
        time_regex = r"\b[0-9]+:[0-9]{2,}\b"
        return (
            m.author == ctx.author
            and m.channel == ctx.channel
            and re.fullmatch(time_regex, m.content)
        )

    try:
        msg = await bot.wait_for("message", check=check, timeout=15)
        await ctx.send(f"입력된 시간: {msg.content}")
        await select(ctx)
    except asyncio.TimeoutError:
        await ctx.send("15초 동안 입력이 없어 기능이 비활성화되었습니다.")


@bot.command(name="ㅅㅌ")
async def select(ctx: commands.Context):
    view = SelectFuntion.SelectView()
    await ctx.send("회의를 진행할 장소를 선택해주세요:", view=view)


bot.run(token)
