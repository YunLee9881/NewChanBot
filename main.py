import discord
from discord.ext import commands
from discord import Embed
import re
import variable_manager
import asyncio
import SelectFunction
import ButtonFunction
from discord.utils import get
import MnM
import json
import time
from datetime import datetime, timedelta


token = variable_manager.bot_token


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
mention_to = MnM.MentionTo(bot)


@bot.slash_command(name="button", description="잡다잡다한 버튼")
async def button(ctx):
    await ctx.response.defer()
    await ctx.followup.send(content=f"안녕하세요, {ctx.author.name}님!")
    await ctx.send(view=ButtonFunction.Button())


@bot.slash_command(name="mention", description="모두가 기다리던 && 멘션!")
async def mnm(ctx, role_name1: str, role_name2: str):
    await ctx.response.defer()
    result = await mention_to.find_members_with_role(ctx, role_name1, role_name2)

    await ctx.followup.send(content="와주세요!")
    await ctx.send(content=result)


@bot.slash_command(name="help", description="챤봇 사용법!")
async def help(ctx):
    await ctx.defer()
    embed = Embed(title="챤봇 사용설명서", description="", color=0x00FF00)
    embed.add_field(
        name="멘션&&멘션!", value="role_name에 @를 빼고 역할 이름을 넣어주세요!", inline=False
    )
    embed.set_footer(text="")
    embed.add_field(name="회의!", value="!챤하를 통해 사용하실 수 있어요!", inline=False)
    embed.set_footer(text="이 기능은 개발중이에요 ㅠㅠ")
    embed.add_field(
        name="잡다 버튼", value="개발자 부르기, 회의 목록 확인 및 대화를 할 수 있어요!", inline=False
    )
    embed.set_footer(text="")
    await ctx.followup.send(embed=embed)


@bot.event
async def on_ready():
    print(f"{bot.user}is ready")


# @bot.command(name="챤하")
# async def meeting(ctx):
#     await ctx.send("무엇을 하시겠어요?", view=ButtonFunction.Meet_Button())
#     mode = ButtonFunction.Meet_Button()


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
        target_time = datetime.strptime(user_input.content, "%H:%M")
        asyncio.create_task(notify_before_five_minutes(target_time, ctx.channel))
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
    me = ctx.author.name

    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    new_data = {f"Oname{variable_manager.count}": f"{oppName}"}
    new_data = {f"Mname{variable_manager.count}": f"{me}"}
    merged_data = {**data, **new_data}
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)


@bot.command()
async def ono(ctx, oppName: str):
    await selectName(ctx, oppName)
    await time(ctx)


def read_times_from_json():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    times = []
    for key, value in data.items():
        if key.startswith("time"):
            times.append(datetime.strptime(value, "%H:%M"))
    return times


# async def set_reminder(ctx, *, time: str):
#     target_time = datetime.strptime(time, "%H:%M")
#     asyncio.create_task(notify_before_five_minutes(target_time, ctx.channel))


async def notify_before_five_minutes(target_time, channel):
    target_time = datetime.now().replace(
        hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0
    )
    target_time = target_time - timedelta(minutes=5)
    while True:
        now = datetime.now().replace(second=0, microsecond=0)
        if now >= target_time:
            await channel.send(f"{target_time + timedelta(minutes=5)}까지 5분 남았습니다!")
            break
        await asyncio.sleep(30)


bot.run(token)
