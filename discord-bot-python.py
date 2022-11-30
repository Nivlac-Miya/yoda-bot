import discord
from discord.ext import commands
from discord.ext.commands import bot
import keys

intents = discord.Intents.all()
bot = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix='!', intents=intents)
is_bot_running = False

@bot.event
async def on_ready():
    global is_bot_running

    if not is_bot_running:
        is_bot_running = True
        print(f"Bot {bot.user.name} initialising...")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    await bot.process_commands(message)
    
@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

@bot.command(aliases= ["you have been terminated"])
async def terminate(ctx):
    return ctx.send("terminating...")
    await bot.close()


bot.run(keys.TOKEN)