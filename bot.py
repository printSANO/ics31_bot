import discord
from discord.ext import commands
from to import Token

bot=commands.Bot(command_prefix='./')

@bot.event
async def on_ready():
    print('Connecting ')
    print(f"Connecting to {bot.user.name} BOT")
    print('Connedtion Success')
    await bot.change_presence(status=discord.Status.online, activity=None)
    
bot.run(Token)