import discord
from discord.ext import commands
import sbs_tokens as token
import sbs_ids as sbsid

### invite Subsolar: https://discordapp.com/oauth2/authorize?client_id=632130255427207178&scope=bot&permissions=8 ###

description = '''Substarters' bot Subsolar.'''
bot = commands.Bot(command_prefix='!', description=description)

### General bot stuff ###
@bot.event
async def on_ready():
    print(bot.user.name + ' is running.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(discord.ext.commands.errors.CommandNotFound):
        pass

### Subcommands ###
def getText(name):
    with open("text/{}.txt".format(name), encoding="utf8") as f:
        return f.read()

# Say hello
@bot.command(help="Say hello.")
async def hello(ctx):
    await ctx.send(getText("hellosolar"))
        
bot.run(token.Subsolar)
