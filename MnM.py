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

    async def find_members_with_role(self, ctx, role_name1: str, role_name2: str):
        role1 = get(ctx.guild.roles, name=role_name1)
        role2 = get(ctx.guild.roles, name=role_name2)
        if not role1:
            return f"역할 {role_name1}을 찾을 수 없습니다."  # 역할을 찾지 못한 경우 메시지 반환

        members_with_role = [
            member for member in ctx.guild.members if role1 in member.roles
        ]

        if members_with_role:
            members_list_str = "\n".join(
                [f"- {member.name}" for member in members_with_role]
            )

        role_and_role = [
            member for member in members_with_role if role2 in member.roles
        ]

        if role_and_role:
            final_members_list = "\n".join(
                [f"- {member.name}" for member in role_and_role]
            )
            return f"멤버:\n{final_members_list}"
        else:
            return f"멤버가 없습니다."
