import discord
from discord.ext import commands
import asyncio
import sbs_emoji as emoji
import sbs_tokens as token
import sbs_ids as sbsid
###more import stuff goes here

### invite Substar: https://discordapp.com/oauth2/authorize?client_id=632129851704475648&scope=bot&permissions=8 ###

description = '''Substarters' bot Substar.'''
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
        
def checkRoles(member, id):
    for role in member.roles:
        if role.id == id:
            return True
    return False

def checkPinned(m):
    return not m.pinned
    
### Testing ###


### Say hello! ###
@bot.command(help="Say hello.")
async def hello(ctx):
    await ctx.send(getText("hellostar"))

### Welcoming new members ###
'''on member join, send message in #welcome + traffic log'''
@bot.event
async def on_member_join(member):
    await bot.get_channel(sbsid.welcome).send(getText("welcome").format(member.mention))
    await bot.get_channel(sbsid.traffic).send("{} ({}) joined Substarters!".format(member.name, member.mention))

'''on member reddify verification, send message in #general + traffic log'''
@bot.event
async def on_member_update(before, after):
    if not checkRoles(before, sbsid.verified) and checkRoles(after, sbsid.verified):
        await bot.get_channel(sbsid.general).send(getText("verified").format(after, sbsid.intro, sbsid.general, sbsid.botspam))
        return

'''on member leave, send message in traffic log'''
@bot.event
async def on_member_remove(member):
    await bot.get_channel(sbsid.traffic).send("{} ({}) left Substarters!".format(member.name, member.mention))

### Cleaning up the server ###
@bot.command(help="Remove X unpinned messages.")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amt: int):
    message = await ctx.send(getText("askRemove").format(amt))
    await message.add_reaction(emoji.yes)
    await message.add_reaction(emoji.no)

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

@bot.command(help="Remove all unpinned messages.")
@commands.has_permissions(manage_messages=True)
async def nuke(ctx):
    message = await ctx.send(getText("askNuke"))
    await message.add_reaction(emoji.yes)
    await message.add_reaction(emoji.no)

    def check(r, u):
        return u.id == ctx.author.id and r.message.id == message.id

    reaction = await bot.wait_for("reaction_add", check=check)

    if reaction[0].emoji == emoji.no:
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

    message = await ctx.send(getText("removedMsgs").format(count - 1))
    await asyncio.sleep(5)
    await message.delete()

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

###
bot.run(token.Substar)
