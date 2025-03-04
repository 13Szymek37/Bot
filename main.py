

import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format musi wyglądać tak NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} dołączył {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Tak, {ctx.subcommand_passed} jest sigmą')


@bot.command()
async def author(ctx):
    await ctx.send(f"Autorem bota jest Szymon Adamczyk ")
@bot.command()
async def description(ctx):
    await ctx.send(f"Jestem bot Testowy_1 i zostałem stworzony aby testować ciekawe komendy :)")
@bot.command()
async def commandlist(ctx):
    await ctx.send(f'Lista komend to: add, roll, choose, repeat, joined, cool, author, description, commandlist.Jeśli chcesz się dowiedzieć co robią poszczegulne komendy napisz:  ?(komenda)info')
@bot.command()
async def addinfo(ctx):
    await ctx.send(f'Na przykład ?add 1 2 dodaje dwie liczby (w tym wypadku napisze 3)')
@bot.command()
async def rollinfo(ctx):
    await ctx.send(f'Np. ?roll 2d6 pozwala symulowac rzucenie kostką. Wiadomość musi być w formacie NdN gdzie pierwsze N to liczba rzutów, d oddziela dwie liczby a drugie N to maksymalna liczba jaka może wypaść.')
@bot.command()
async def chooseinfo(ctx):
    await ctx.send(f'Np. ?choose jałko gruszka banan.Ta komenda pozwala mi wybrać jeden z wyrazów które napisałeś ')
@bot.command()
async def repeatinfo(ctx):
    await ctx.send(f'Np. ?repeat heh 10.Ta komenda spowoduje, że wypisze 10 razy słowo heh w miejscu heh moze być jaiekolwiek słowo a 10 to liczba powtórzeń')
@bot.command()
async def joinedinfo(ctx):
    await ctx.send(f'?joined (nazwa użytkownika). Ta komenda sprawi, że napisze kiedy członek serwera do nas dołączył')
@bot.command()
async def coolinfo(ctx):
    await ctx.send(f'Np. ?cool (nazwa użytkownika).Ta komenda sprawdza czy nadawca wiadomości jest dobrą mordą')
@bot.command()
async def authorinfo(ctx):
    await ctx.send(f'Dzięki tej komendzie dowiesz się kto mnie napisał')
@bot.command()
async def descriptioninfo(ctx):
    await ctx.send(f'Ta komensa sprawi, że krótko się opiszse')
@bot.command()
async def commandlistinfo(ctx):
    await ctx.send(f'To po prostu lista komend(nie zapomnij użyć przed każdą -> ? <-)')
bot.run('token')
