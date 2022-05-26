import discord
from discord.ext import commands
from to import Token
import links
import time
from petr.return_a_petr import read_n_pick_petr

file = open('scheduled.txt')
lines = file.readlines()
file.close()

bot=commands.Bot(command_prefix='$')

def check_time():
    """month,day,hr,min"""
    lst = []
    current_time = list(time.localtime())
    hour = current_time[3]
    month = current_time[1]
    day = current_time[2]
    minute = current_time[4]
    lst.append(month)
    lst.append(day)
    lst.append(hour)
    lst.append(minute)
    return lst


def bot_command():
    line = f"Bot Commands: \n\n**$help** : list of bot commands\n\n**$due** : check assignments due\n\n**$full_schedule** : check full schedule\n\n**$resources** : check resources\n\n**$lecture** : Link to zoom lecture and password\n\n**$office_hour** : Office hour zoom link\n\n**$grade** : Link to grade estimator"
    return line
@bot.event
async def on_ready():
    print('Connecting ')
    print(f"Connecting to {bot.user.name} BOT")
    print('Connection Success')
    await bot.change_presence(status=discord.Status.online, activity=None)
@bot.event
async def initial_message():
    print("Bot Commands")
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$help'):
        await message.channel.send(bot_command())

    if message.content.startswith('$due'):
        x = check_time()
        month2 = x[0]
        day2 = x[1]
        for i in lines:
            j = i.split(',')
            k = j[0].split("/")
            l = j[2].split(":")
            month1 = k[0]
            day1 = k[1]
            if int(month1) >= int(month2):
                if int(day1) == int(day2)+1:
                    await message.channel.send(f"{j[1]} tomorrow at {j[2]}")
                if int(day1) == int(day2):
                    await message.channel.send(f"**{j[1]} today at {j[2]}**")

    if message.content.startswith('$full_schedule'):
        x = check_time()
        month2 = x[0]
        day2 = x[1]
        for i in lines:
            j = i.split(',')
            k = j[0].split("/")
            l = j[2].split(":")
            month1 = k[0]
            day1 = k[1]
            if int(month1) >= int(month2):
                if int(day1) >= int(day2):
                    await message.channel.send(f"{j[1]} in {j[0]} at {j[2]}")

    if message.content.startswith('$resources'):
        link = links.resource_link
        await message.channel.send(link)

    if message.content.startswith('$lecture'):
        zoom = links.zoom_lec
        await message.channel.send(f"zoom link to lecture is {zoom}. Password is DeBug")
    
    if message.content.startswith('$office_hour'):
        oh = links.oh_link
        await message.channel.send(f"zoom link to office hours: {oh}")
    if message.content.startswith('$ohhhhhh'):
        await message.channel.send(f"https://c.tenor.com/Yjx_r38x1aYAAAAd/mind-blown-explosion.gif")
    
    if message.content.startswith('$grade'):
        grade = links.grade_link
        await message.channel.send(f"Link to grade estimator: {grade}")

    if message.content.startswith('$lakers'):
        await message.channel.send(f"Lakers in 5!\n")
        await message.channel.send('https://tenor.com/view/snoop-dogg-lakers-dance-gif-21628249')


    if message.content.lower() in ("$peter", "$petr"):
        petr = read_n_pick_petr("./petr/petrs.csv")
        github_url = "https://github.com/printSANO/ics31_bot/petr/"
        image_suffix = "?raw=true"
        await message.channel.send(f"{github_url}{petr}{image_suffix}")
    
    
bot.run(Token)
