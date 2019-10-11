import discord
from discord.ext import commands
import asyncio
import tokens
import strings
import channels
import roles
###more import stuff goes here

### invite Substar: https://discordapp.com/oauth2/authorize?client_id=632129851704475648&scope=bot&permissions=8 ###

description = '''Substarters' bot Substar.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print(bot.user.name + ' is running.')
    
### Don't touch these, they work! ###

@bot.command()
async def hello(ctx):
    await ctx.send(strings.hellostar)

### Cleaning up the server ###

def checkPinned(m):
    return not m.pinned
    
@bot.command(help="Remove X unpinned messages.")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amt: int):
    message = await ctx.send(strings.askRemove.format(amt))
    await message.add_reaction(strings.yes)
    await message.add_reaction(strings.no)

    def check(r, u):
        return u.id == ctx.author.id and r.message.id == message.id

    reaction = await bot.wait_for("reaction_add", check=check)

    if reaction[0].emoji == strings.no:
        return

    amt += 1
    count = 0
    while amt > 0:
        next = min(1000, amt)
        deleted = await ctx.message.channel.purge(limit=next, check=checkPinned)
        amt -= next
        count += len(deleted)

    message = await ctx.send(strings.removedMsgs.format(count - 1))
    await asyncio.sleep(5)
    await message.delete()

@bot.command(help="Removes all unpinned messages.")
@commands.has_permissions(manage_messages=True)
async def nuke(ctx):
    message = await ctx.send(strings.askNuke)
    await message.add_reaction(strings.yes)
    await message.add_reaction(strings.no)

    def check(r, u):
        return u.id == ctx.author.id and r.message.id == message.id

    reaction = await bot.wait_for("reaction_add", check=check)

    if reaction[0].emoji == strings.no:
        return

    amt = 1000
    amt += 1
    count = 0
    while amt > 0:
        next = min(1000, amt)
        deleted = await ctx.message.channel.purge(limit=next, check=checkPinned)
        amt -= next
        count += len(deleted)

    await ctx.message.channel.purge(limit=1000, check=checkPinned)

    message = await ctx.send(strings.nukedMsgs.format(count - 1))
    await asyncio.sleep(5)
    await message.delete()


###
bot.run(tokens.Substar)
