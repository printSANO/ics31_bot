import discord
from discord.ext import commands
from to import Token

file = open('scheduled.txt')
lines = file.readlines()
file.close()

bot=commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('Connecting ')
    print(f"Connecting to {bot.user.name} BOT")
    print('Connection Success')
    await bot.change_presence(status=discord.Status.online, activity=None)
    
@bot.command()
async def test(ctx, arg):
    print("test")
    await ctx.send(arg)
# def bot_command():
#     line = f"Bot Commands: \n\n**$help** : list of bot commands\n\n**$due** : check assignments due\n\n**$full_schedule** : check full schedule\n\n**$resources** : check resources\n\n**$lecture** : Link to zoom lecture and password\n\n**$office_hour** : Office hour zoom link\n\n**$grade** : Link to grade estimator"
#     return line
# @bot.event
# async def help(ctx,arg):
#     await ctx.send(bot_command())
bot.run(Token)
