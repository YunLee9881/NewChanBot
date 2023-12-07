import requests
import discord
import os
import json
from discord.ext import commands
import re
from discord.utils import get


class MentionTo:
    def __init__(self, bot):
        self.bot = bot

    async def find_members_with_role(self, ctx, role_name: str):
        role = get(ctx.guild.roles, name=role_name)
        if not role:
            return f"역할 {role_name}을 찾을 수 없습니다."  # 역할을 찾지 못한 경우 메시지 반환

        members_with_role = [
            member for member in ctx.guild.members if role in member.roles
        ]

        if members_with_role:
            members_list = "\n".join(
                [f"- {member.name}" for member in members_with_role]
            )
            return f"역할 {role.name}이 있는 멤버:\n{members_list}"
        else:
            return f"역할 {role_name}이 있는 멤버가 없습니다."  # 해당 역할을 가진 멤버가 없는 경우 메시지 반환
