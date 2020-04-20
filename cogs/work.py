from discord import Member
from discord.ext import commands


class Work(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{ member } has joined the server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{ member } has left the server.')

    # Commands
    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, context, amount=10):
        await context.channel.purge(limit=amount+1)

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def kick(self, context, member: Member, *, reason=None):
        await member.kick(reason=reason)
        await context.send(f'Kicked { member.mention }')

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def ban(self, context, member: Member, *, reason=None):
        await member.ban(reason=reason)
        await context.send(f'Banned { member.mention }')

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def unban(self, context, *, member):
        banned_users = await context.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await context.guild.unban(user)
                await context.send(f'Unbanned { user.mention }')
                return

        await context.send(f'Could not find a banned user with that name!')


def setup(client):
    client.add_cog(Work(client))
