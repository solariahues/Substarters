import discord
from discord.ext import commands
import tokens
import strings
###more import stuff goes here

### invite Subsolar: https://discordapp.com/oauth2/authorize?client_id=632130255427207178&scope=bot&permissions=8 ###

description = '''Substarters' bot Subsolar.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print(bot.user.name + ' is running.')
    
# This stuff works

@bot.command()
async def hello(ctx):
    await ctx.send(strings.hellosolar)
    
        
# Creates a temporary role and channel

@bot.command(help="Adds a temporary channel and exclusive role.")
@commands.has_permissions(administrator=True)
async def add(ctx, request):
  guild = ctx.guild

  if request == "temp":
    temprole = await guild.create_role(name="Temp Role")
    modsow = {
    guild.default_role: discord.PermissionOverwrite(read_messages=False),
    temprole: discord.PermissionOverwrite(read_messages=True)
    }
    temp = await guild.create_text_channel("temp-channel", overwrites=modsow)

bot.run(tokens.Subsolar)
