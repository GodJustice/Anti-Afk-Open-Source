import discord
import json
import colorama
import random
import asyncio
import datetime
import time
import os
import requests
from colorama import Fore, init
import os
from colorama import Fore as C
from discord.ext import commands

prefix = "."

client = discord.Client()
client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command('help') 

init(convert=True)
clear = lambda: os.system('cls')

os.system("title [ANTI-AFK] By Iheb")

def starter():
    clear()
print(f'''
                                  
                                  {Fore.BLUE}██▓ ██░ ██ ▓█████  ▄▄▄▄   
                                  ▓██▒▓██░ ██▒▓█   ▀ ▓█████▄ 
                                  ▒██▒▒██▀▀██░▒███   ▒██▒ ▄██
                                  ░██░░▓█ ░██ ▒▓█  ▄ ▒██░█▀  
                                  ░██░░▓█▒░██▓░▒████▒░▓█  ▀█▓
                                  ░▓   ▒ ░░▒░▒░░ ▒░ ░░▒▓███▀▒
                                    ▒ ░ ▒ ░▒░ ░ ░ ░  ░▒░▒   ░ 
                                    ▒ ░ ░  ░░ ░   ░    ░    ░ 
                                    ░   ░  ░  ░   ░  ░ ░    ░{Fore.BLUE} 
''')


print(f'''{Fore.BLUE}The Bot Will React/Answer at 43 Seconds With Random Words Everytime someone mention you.{Fore.BLUE}
''')
print(f'''{Fore.BLUE}Have fun with antiafk.{Fore.BLUE}
''')
print(f'''{Fore.BLUE}The reason why it's exe file Because some people don't know how to deal with it{Fore.BLUE}
''')
print(f'''{Fore.BLUE}discord.gg/chiefjustice and dm Iheb (element#5555) for source code.{Fore.BLUE}
''')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
      time.sleep(43)
      await message.channel.send(random.choice(['wtf', 'son', 'jtd', 'L','nope', 'lol', 'stfu', 'focus','idc','1','.',';','noep','tf','ok','nig','lo','sjc','a','b','?','no','sudusb','??','ewr','j6te','6trhj','4y5h','ehyh yr','ik','ky75','uyt','u7k','sdu' ]))        

with open('./config.json')as f:
  config = json.load(f)

token = config.get('token')
client.run(token, bot=False)