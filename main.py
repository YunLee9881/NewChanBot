import discord
from discord.ext import commands
import re
import variable_manager
import asyncio
import SelectFunction
import ButtonFunction
from discord.utils import get
import MnM
import json


token = variable_manager.bot_token


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
mention_to = MnM.MentionTo(bot)


@bot.slash_command(name="button", description="잡다잡다한 버튼")
async def button(ctx):
    await ctx.response.defer()
    await ctx.followup.send(
        content=f"안녕하세요, {ctx.author.name}님!", view=ButtonFunction.Button()
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
    await ctx.send("무엇을 하시겠어요?", view=ButtonFunction.Meet_Button())
    mode = ButtonFunction.Meet_Button()


@bot.command()
async def members(ctx):
    members = ctx.guild.members


@bot.command()
async def time(ctx):
    await ctx.send("시간을 입력하세요 단 형식은 00:00으로 입력해주셔야해요!")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_input = await bot.wait_for("message", timeout=15.0, check=check)
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        new_data = {f"time{variable_manager.count}": f"{user_input.content}"}
        merged_data = {**data, **new_data}
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=4)
        await ctx.send(f"입력하신 시간은 {user_input.content}입니다.")
        await selectPlace(ctx)
    except asyncio.TimeoutError:
        await ctx.send("15초 동안 입력이 없어 기능이 비활성화되었습니다.")


@bot.command()
async def selectPlace(ctx: commands.Context):
    view = SelectFunction.SelectView()
    await ctx.send("회의를 진행할 장소를 선택해주세요:", view=view)


@bot.command()
async def selectName(ctx, oppName: str):
    opponent = ctx.guild.get_member_named(oppName)
    # await ctx.send(f"{ctx.author.mention}, {opponent.mention}")

    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    new_data = {f"name{variable_manager.count}": f"{oppName}"}
    merged_data = {**data, **new_data}
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)


@bot.command()
async def ono(ctx, oppName: str):
    await selectName(ctx, oppName)
    await time(ctx)


bot.run(token)
