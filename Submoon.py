import discord
from discord.ext import commands
###more import stuff goes here

### invite Substar: https://discordapp.com/oauth2/authorize?client_id=CLIENTID&scope=bot&permissions=8 ###

TOKEN = 'TOKENGOESHERE'

description = '''Substarters' bot Submoon.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print(bot.user.name + ' is running.')
    
# Add stuff here

bot.run(TOKEN)
