import discord
from discord.ext import commands
from to import Token
import time

file = open('/Users/ryan/dev/ics31/chrome_extension/schedule.txt')
lines = file.readlines()
file.close()

bot=commands.Bot(command_prefix='./')

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
    line = f"Bot Commands: \n\n$due : check assignments due\n\n$full_schedule : check full schedule\n\n$resources : check resources\n\n$lecture : Link to zoom lecture and password"
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
        #hour2 = x[2]
        #minute2 = x[3]
        for i in lines:
            j = i.split(',')
            k = j[0].split("/")
            l = j[2].split(":")
            month1 = k[0]
            day1 = k[1]
            #hour1 = l[0]
            #minute1 = l[1]
            if int(month1) >= int(month2):
                if int(day1) == int(day2)+1:
                    await message.channel.send(f"{j[1]} tomorrow at {j[2]}")
                if int(day1) == int(day2):
                    await message.channel.send(f"**{j[1]} today at {j[2]}**")

    if message.content.startswith('$full_schedule'):
        x = check_time()
        month2 = x[0]
        day2 = x[1]
        #hour2 = x[2]
        #minute2 = x[3]
        for i in lines:
            j = i.split(',')
            k = j[0].split("/")
            l = j[2].split(":")
            month1 = k[0]
            day1 = k[1]
            #hour1 = l[0]
            #minute1 = l[1]
            if int(month1) >= int(month2):
                if int(day1) >= int(day2):
                    await message.channel.send(f"{j[1]} in {j[0]}at {j[2]}")

    if message.content.startswith('$resources'):
        link = 'https://drive.google.com/drive/folders/1m5orJ4toWhjMmbQsje_znq7B_gbUoZ-z?usp=sharing'
        await message.channel.send(link)

    if message.content.startswith('$lecture'):
        zoom = 'https://uci.zoom.us/j/97605655948?pwd=WmhQK3NNQ01tSFZWVG92Nk9oTmdYZz09'
        await message.channel.send(f"zoom link to lecture is {zoom}. Password is DeBug")
    
bot.run(Token)