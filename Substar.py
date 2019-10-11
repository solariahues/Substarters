import discord
from discord.ext import commands
import tokens
import strings
###more import stuff goes here

### invite Substar: https://discordapp.com/oauth2/authorize?client_id=632129851704475648&scope=bot&permissions=8 ###

description = '''Substarters' bot Substar.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print(bot.user.name + ' is running.')
    
# Add stuff here

@bot.command()
async def hello(ctx):
    await ctx.send("Hi there! I'm Substar!")

bot.run(tokens.Substar)
