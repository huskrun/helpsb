class ServerNuker():
    __version__ = 1

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, pokepy
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
from randomuser import RandomUser
from pythonping import ping as pyping

ctypes.windll.kernel32.SetConsoleTitleW(f'[Husk Nuker v{ServerNuker.__version__}] | Loading in...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('pass')
prefix = config.get('prefix')

print(f'''{Fore.RESET}
                     {Fore.YELLOW}▄████  ▄▄▄       ███▄    █   ▄████   ██████ ▄▄▄█████▓ █    ██  ██░ ██  ██░ ██ 
                     {Fore.YELLOW}██▒ ▀█▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▒██    ▒ ▓  ██▒ ▓▒ ██  ▓██▒▓██░ ██▒▓██░ ██▒
                     {Fore.YELLOW}▒██░▄▄▄░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░░ ▓██▄   ▒ ▓██░ ▒░▓██  ▒██░▒██▀▀██░▒██▀▀██░
                     {Fore.YELLOW}░▓█  ██▓░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓  ▒   ██▒░ ▓██▓ ░ ▓▓█  ░██░░▓█ ░██ ░▓█ ░██ 
                     {Fore.YELLOW}░▒▓███▀▒ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██████▒▒  ▒██▒ ░ ▒▒█████▓ ░▓█▒░██▓░▓█▒░██▓
                     {Fore.YELLOW} ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▒▓▒ ▒ ▒  ▒ ░░▒░▒ ▒ ░░▒░▒
                     {Fore.YELLOW}  ░   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░ ░▒  ░ ░    ░    ░░▒░ ░ ░  ▒ ░▒░ ░ ▒ ░▒░ ░
                     {Fore.YELLOW}░ ░   ░   ░   ▒      ░   ░ ░ ░ ░   ░ ░  ░  ░    ░       ░░░ ░ ░  ░  ░░ ░ ░  ░░ ░
                     {Fore.YELLOW}      ░       ░  ░         ░       ░       ░              ░      ░  ░  ░ ░  ░  ░
                                
                        {Fore.RED}Logged In As ==> {Fore.WHITE}{Ioxide.user.name}#{Ioxide.user.discriminator}{Fore.WHITE}
                        {Fore.RED}ID ==> {Fore.WHITE}{Ioxide.user.id}
                        {Fore.RED}Anti-AFK ==> {Fore.WHITE}{antiafk}
                        {Fore.RED}Version ==> {Fore.WHITE} v{ServerNuker.__version__}
                    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.WHITE}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Ioxide.run(token, bot=False, reconnect=True)
            os.system(f'title [ Husk SelfBot ] - Version {ServerNuker.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.WHITE}[ERROR] {Fore.YELLOW}Sure this is a token? lol"+Fore.RESET)
            os.system('pause >NUL')

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

colorama.init()
Ioxide = discord.Client()
Ioxide = commands.Bot(
    description='Flash Bot',
    command_prefix=prefix,
    self_bot=True
)

Ioxide.remove_command('help') 

@Ioxide.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.WHITE}Error: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Ioxide.event
async def on_message_edit(before, after):
    await Ioxide.process_commands(after)

                   
        

 
