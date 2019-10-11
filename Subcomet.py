import discord
from discord.ext import commands
import tokens
import strings
###more import stuff goes here

### invite Subcomet: https://discordapp.com/oauth2/authorize?client_id=632130163664093184&scope=bot&permissions=8 ###

description = '''Substarters' bot Subcomet.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print(bot.user.name + ' is running.')
    
# Add stuff here

@bot.command()
async def hello(ctx):
    await ctx.send(strings.hellocomet)
    
@bot.command()
async def survey(ctx):
    await ctx.send(strings.survey)

bot.run(tokens.Subcomet)
