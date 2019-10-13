import discord
from discord.ext import commands
import sbs_tokens as token
import sbs_ids as sbsid

### invite Subcomet: https://discordapp.com/oauth2/authorize?client_id=632130163664093184&scope=bot&permissions=8 ###

description = '''Substarters' bot Subcomet.'''
bot = commands.Bot(command_prefix='!', description=description)

### General bot stuff ###
@bot.event
async def on_ready():
    print(bot.user.name + ' is running.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass

### Subcommands ###
def getText(name):
    with open("text/{}.txt".format(name), encoding="utf8") as f:
        return f.read()
    
# this stuff works

@bot.command(help="Say hello.")
async def hello(ctx):
    await ctx.send(getText("hellocomet"))
    
@bot.command(help="Fill out a survey.")
async def survey(ctx):
    await ctx.send(getText("survey"))
    
### Welcoming new members ###
'''Send (anonymous) feedback.'''
@bot.command(help="Give (anonymous) feedback.")
async def feedback(ctx, *, message):
    await ctx.send("Feedback sent!")
    await bot.get_channel(sbsid.feedback).send("\n\n <:blank:631946877604200469>**Feedback:** \n\n {} \n\n <:blank:631946877604200469>".format(message))

bot.run(token.Subcomet)
