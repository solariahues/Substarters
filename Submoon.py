import discord
from discord.ext import commands
import tokens
import strings
###more import stuff goes here

### invite Submoon: https://discordapp.com/oauth2/authorize?client_id=632130020495589376&scope=bot&permissions=8 ###

description = '''Substarters' bot Submoon.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print(bot.user.name + ' is running.')
    
# Add stuff here

bot.run(tokens.Submoon)

