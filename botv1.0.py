import discord
from discord.ext import commands

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print("Online.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping is: {round(client.latency * 1000)} ms')

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clean(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount)

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"{member} has been banned")
    print(f'{member} has been banned by {ctx.message.author}')


@ban.error
async def clear_error(ctx, error):
    id = ctx.message.author.id
    author = ctx.message.author
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
        print(f'{author} id: {id} attempted to ban someone')

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"{member} has been kicked")
    print(f'{member} has been kicked by {ctx.message.author}')


@kick.error
async def clear_error(ctx, error):
    id = ctx.message.author.id
    author = ctx.message.author
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{author} You cant do that!")
        print(f'{author} id: {id} attempted to ban someone')

@client.event
async def on_ready():
    print("Online.")

@client.command()
async def shutdown(ctx):
    id = ctx.message.author.id
    author = ctx.message.author
    if id == #your id here:
        await ctx.bot.logout()
        print("bot shutdown")
    else:
        await ctx.send(f'<@{id}> You dont own this bot please dont try to shut it down')
        print(f'{author} id: {id} attempted to shutdown bot')

client.run('token')