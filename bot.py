from discord import Game
from discord.ext import commands
from os import listdir

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    await client.change_presence(activity=Game('Wii Tennis'))
    print('We are cocked and loaded!')


@client.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandNotFound):
        error_message = 'Are you having a stroke?'

    elif isinstance(error, commands.MissingPermissions):
        error_message = "I'm sorry Dave, I'm afraid I can't do that."

    elif isinstance(error, commands.MissingRequiredArgument):
        error_message = 'You left out some information on that command!'

    else:
        error_message = "Great work. Now there's a fire in the server room."
        print(error)

    await context.send(error_message)


@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def load(context, extension):
    client.load_extension(f'cogs.{ extension }')
    await context.send(f'Loaded extension { extension }')


@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def unload(context, extension):
    client.unload_extension(f'cogs.{ extension }')
    await context.send(f'Unloaded extension { extension }')


@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def reload(context, extension):
    client.unload_extension(f'cogs.{ extension }')
    client.load_extension(f'cogs.{ extension }')
    await context.send(f'Reloaded extension { extension }')


def main():
    for filename in listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{ filename[:-3] }')

    # Pass your special key in here
    client.run()


if __name__ == '__main__':
    main()
