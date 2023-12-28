from discord.ext import commands
from discord.utils import get


class MentionTo:
    def __init__(self, bot):
        self.bot = bot

    async def find_members_with_role(self, ctx, role_name1, role_name2):
        role1 = get(ctx.guild.roles, name=role_name1)
        role2 = get(ctx.guild.roles, name=role_name2)
        if not role1 or not role2:
            return f"역할 {role_name1} 또는 {role_name2}을 찾을 수 없습니다.\n오타가 있는지 확인해주세요."

        members_with_role = [
            member
            for member in ctx.guild.members
            if role1 in member.roles and role2 in member.roles
        ]

        if members_with_role:
            members_list_str = ", ".join(
                [f"{member.mention}" for member in members_with_role]
            )
            return f"\n[{members_list_str}]"
        else:
            return f"멤버가 없습니다."
