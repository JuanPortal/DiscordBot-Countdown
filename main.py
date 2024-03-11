import discord
from discord.ext import commands
import time
import os

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())
client.remove_command("help")


@client.event
async def on_ready():
    print("Timer's ready to go!")


global keep_going
keep_going = True


@client.command(pass_context=True)
async def cd(ctx, arg):
    global keep_going
    keep_going = True

    if ":" in arg:
        seconds = int(arg[-2:])
        minutes = int(arg[:len(arg) - 3])
        count = minutes * 60 + seconds

    else:
        count = int(arg) * 60

    while count >= 0 and keep_going:
        m, s = divmod(count, 60)
        h, m = divmod(m, 60)
        time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2) + "\n"
        time.sleep(1)
        await ctx.channel.send(time_left)
        count -= 1


@client.command(pass_context=True)
async def stop(ctx):
    global keep_going
    keep_going = False


@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description="$mm:ss or just type the minutes\n\n***$cd*** starts the timer\n\n***$stop*** stops the timer"
    )
    await ctx.send(embed=em)


client.run(os.environ["TOKEN"])
