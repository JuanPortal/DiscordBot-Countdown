from discord.ext import commands
import discord
import time

client = commands.Bot(command_prefix="$")

client.remove_command("help")


@client.event
async def on_ready():
    print("Countdown's ready to go!")


global continuar
continuar = True


@client.command(pass_context=True)
async def cd(ctx, arg):
    global continuar
    continuar = True

    if ":" in arg:
        segundos = int(arg[-2:])
        minutos = int(arg[:len(arg) - 3])
        cuenta = minutos * 60 + segundos

    else:
        cuenta = int(arg) * 60

    while cuenta >= 0 and continuar:
        m, s = divmod(cuenta, 60)
        h, m = divmod(m, 60)
        time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2) + "\n"
        time.sleep(1)
        await ctx.channel.send(time_left)
        cuenta -= 1


@client.command(pass_context=True)
async def stop():
    global continuar
    continuar = False


@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description="mm:ss or just type the minutes\n\n***$cd*** starts the countdown\n\n***$stop*** stops \
         the countdown"
    )
    await ctx.send(embed=em)


client.run("TOKEN")
