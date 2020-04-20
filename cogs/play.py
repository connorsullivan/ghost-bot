from discord.ext import commands
from random import choice


class Play(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description='A random saying, rooted in ancient wisdom.')
    async def saying(self, context):
        responses = [
            'We are cocked and loaded!',
            'Whip it out!',
            'The avocados are particularly turbulent this evening!',
            'Dab and skeet!',
            'Tony Fellatio!',
            'I make big sex for good price!',
            'Turbocopter coming in for a landing!'
        ]

        await context.send(f'{ choice(responses) }')


def setup(client):
    client.add_cog(Play(client))
