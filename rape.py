import discord
from discord.ext import commands
from datetime import *
from colorama import *
import json
import threading
from tkinter import messagebox
import tkinter
root = tkinter.Tk()
root.withdraw()
from discord.ext import tasks
import psutil
import asyncio
import time
import os
import sys
from pyfiglet import Figlet
import requests
import random
from discord.ext.commands import CommandNotFound
from pypresence import Presence
import psutil 
import ctypes
import cryptography


from discord.ext import commands, tasks

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class rape:
    def setup():
        if not os.path.exists('./config.json'):
            clear()
            with open('./config.json', 'w') as fp:
                print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTWHITE_EX}] {Fore.LIGHTRED_EX}Welcome to the setup.")
                setup_token = input(Fore.LIGHTWHITE_EX +'>' + Fore.LIGHTRED_EX + ' Enter token: ' + Fore.LIGHTWHITE_EX)
                setup_data = {
                    "token": setup_token,
                    "prefix": ">",
                    "color": "0x6495ed",
                    "del_after": 10,
                    "footer": "rape v2",
                    "presense": "True"
                }
                json.dump(setup_data, fp, indent=4)
                time.sleep(3)
            clear()
            Fore.RESET
        else:
            pass

if not os.path.exists('./config.json'):
    rape.setup()

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
color = config.get('color')
del_after = config.get('del_after')
footer = config.get('footer')
rich_presence = config.get('presense')

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(Fore.MAGENTA + f' ██████   █████  ██████  ███████ '.center(os.get_terminal_size().columns))
    print(Fore.MAGENTA + f' ██   ██ ██   ██ ██   ██ ██      '.center(os.get_terminal_size().columns))
    print(Fore.MAGENTA + f' ██████  ███████ ██████  █████   '.center(os.get_terminal_size().columns))
    print(Fore.MAGENTA + f' ██   ██ ██   ██ ██      ██      '.center(os.get_terminal_size().columns))
    print(Fore.MAGENTA + f' ██   ██ ██   ██ ██      ███████  '.center(os.get_terminal_size().columns))
    print(Fore.MAGENTA)
    print(Fore.MAGENTA)
    print(Fore.BLUE + f' credit: https://github.com/moronnnn '.center(os.get_terminal_size().columns))
    print(Fore.BLUE + f' originally developed by: https://github.com/i3gaps '.center(os.get_terminal_size().columns))
    for i in range(os.get_terminal_size().columns):
        print(Fore.LIGHTWHITE_EX + '─', end='')
    
    print('\n')

@bot.event
async def on_command(ctx):
    dt = datetime.utcfromtimestamp(time.time())
    current_time = dt.strftime("%H:%M")
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.CYAN}{current_time}{Fore.LIGHTWHITE_EX}] {Fore.CYAN}command used {Fore.LIGHTWHITE_EX}| {Fore.CYAN}{ctx.command.name}')

@bot.event
async def on_ready():
    bot.loop.create_task(title())
    banner()
    

async def title():
    while True:
        cpuavg = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()[2]  
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Rape V1] connected to {bot.user.name} | MOTD: Fuck Niggers LOL | CPU @ {cpuavg}% | Memory @ {mem}%')
        await asyncio.sleep(3)

@bot.command()
async def clear(ctx):
    await ctx.message.delete()
    os.system("cls")
    banner()

@bot.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url='https://www.twitch.tv/r4p3',
    )
    await bot.change_presence(activity=stream)

@bot.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await bot.change_presence(activity=game)


@bot.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@bot.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@bot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.BLUE}error{Fore.LIGHTWHITE_EX}] {Fore.BLUE} seems you can\'t run this command due to missing permissions')
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.BLUE}error{Fore.LIGHTWHITE_EX}] {Fore.BLUE} missing argument(s){Fore.WHITE}: {Fore.BLUE}{error}')
    elif isinstance(error, discord.errors.Forbidden):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.BLUE}error{Fore.LIGHTWHITE_EX}] {Fore.BLUE} not allowed{Fore.WHITE}: {Fore.BLUE}{error}')
    else:
        return

@bot.command()
async def help(ctx, help):
    await ctx.message.delete()
    try:
        embed= discord.Embed(color= 0x34495E, title= "Commands",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url="https://i.imgur.com/t6NHYp5.jpeg")
        embed.set_footer(text=" RapeV1")
        embed.add_field(name="messages", value= "purge, deleteall", inline=False)
        embed.add_field(name="malicious", value="webhookinfo, delhook, sendhook", inline=False)
        embed.add_field(name="networking", value="iplookup, ping", inline=False)
        embed.add_field(name="Fun", value="kiss, hug, dafloppa, btc, mommy, leet", inline=False)
        embed.add_field(name="NSFW", value="hentai, lesbian", inline=False)
        embed.add_field(name="selfbot", value="clear, restart", inline=False)
        embed.add_field(name="Moderation", value="ban, kick, unban", inline=False)
        embed.add_field(name="Info", value="Made by https://github.com/moronnnn ", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Error: this command does not have embed permissions check the console for the list")
        os.system("cls")
        print("""
        Help commands in the console for you aswell

        Information:
        Fun:
        - kiss
        - hug
        - dafloppa
        - btc
        - mommy
        Moderation:
        - purge
        - shutdown
        - ban
        - kick
        - unban
        selfbot:
        - clear
        - restart
        """)
        input()
        show_on()
strbtc = 0 

    

@bot.command()
async def hookinfo(ctx, webhook):
    await ctx.message.delete()
    r = requests.get(webhook).json()
    embed = discord.Embed(title='webhook info', description=f'name: {r["name"]}\navatar: {r["avatar"]}\nID: {r["id"]}\nchannel id: {r["channel_id"]}\nguild id: {r["guild_id"]}\ntoken: {r["token"]}', color=0x6495ED)
    await ctx.send(embed=embed, delete_after=def_after)

@bot.command()
async def info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Info on RapeV!', description="RapeV1 was developed by https://github.com/moronnnn")
    await ctx.send(embed=embed, delete_after=def_after)

@bot.command()
async def kiss(ctx): 
    await ctx.message.delete()
    r = requests.get("https://neko-love.xyz/api/v1/kiss")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def hug(ctx): 
    await ctx.message.delete()
    r = requests.get("https://neko-love.xyz/api/v1/hug")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

    
@bot.command(usage="mommy", description="mommy? sorry.")
async def mommy(rape, amount: int):
    await rape.message.delete()
    mommy = await rape.send('Mommy?')
    for x in range(amount):
      await asyncio.sleep(1)
      await mommy.edit(content='Sorry.')
      await asyncio.sleep(1)
      await mommy.edit(content='Mommy?')

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    try:
        embed= discord.Embed(color= 0x34495E, title=f"Pong",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=" RapeV1")
        before = time.monotonic()
        message = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        ping = (time.monotonic() - before) * 1000
        embed= discord.Embed(color= green_light, title=f"Ping: {int(ping)}ms",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=" RapeV1")
        await message.edit(embed=embed)

    except discord.HTTPException:
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Ping: `{int(ping)}ms`")

@bot.command()
async def iplookup(ctx, ip: str=None):
    await ctx.message.delete()
    if ip is None: await ctx.send("Please sepcify an IP address");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    await ctx.send("Invalid IP address")
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(color= 0x34495E, title=f"INFO",timestamp=datetime.utcfromtimestamp(time.time()))
                        embed.set_thumbnail(url="https://i.imgur.com/XZz9ZPo.jpg")
                        embed.add_field(name=f'IP', value=f'{ip}', inline=False)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=False)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=False)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=False)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=False)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=False)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=False)
                        embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=False)
                        embed.set_footer(text=" RapeV1")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")

@bot.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command(usage='dafloppa', description='Sends cool DaFloppa')
async def dafloppa(rape):
    await rape.message.delete()
    message = await rape.send('''fuck bitches get floppa''')
    await rape.send('https://pbs.twimg.com/media/Epe8jZ2WwAMSk2b.jpg')
    await ctx.send(embed=embed)

@bot.command(usage='btc')
async def btc(rape):
    await rape.message.delete()
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    r = r.json()
    usd = r["USD"]
    embed = discord.Embed(description=f"```${str(usd)}```", color=RandomColor())
    embed.set_author(name="Bitcoin", icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
    await rape.send(embed=embed)

@bot.command()
async def leet(ctx, *, message: str=None):
    
    if message is None:
        await ctx.send("Insert message sir")
    else:
        try:
            word = message
            leetmsg = word
            leetwords = "aeioutsyou"
            for letter in word:
                if letter in leetwords:
                    leetmsg = leetmsg.replace('a', str(4))
                    leetmsg = leetmsg.replace('e', str(3))
                    leetmsg = leetmsg.replace('i', str(1))
                    leetmsg = leetmsg.replace('o', str(0))
                    leetmsg = leetmsg.replace('t', str(7))
                    leetmsg = leetmsg.replace('s', '2')
                    leetmsg = leetmsg.replace('you', 'j00')

            embed= discord.Embed(color= 0x6495ED, title="1337 Haxor", description=f"{leetmsg.upper()}",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/TR2cv3C.jpg")
            embed.set_footer(text=" RapeV1")
            await ctx.send(embed=embed)
        except discord.HTTPException:
            word = message
            leetmsg = word
            leetwords = "aeioutsyou"
            for letter in word:
                if letter in leetwords:
                    leetmsg = leetmsg.replace('a', str(4))
                    leetmsg = leetmsg.replace('e', str(3))
                    leetmsg = leetmsg.replace('i', str(1))
                    leetmsg = leetmsg.replace('o', str(0))
                    leetmsg = leetmsg.replace('t', str(7))
                    leetmsg = leetmsg.replace('s', '$')
                    leetmsg = leetmsg.replace('you', 'j00')
            await ctx.send(f"{leetmsg.upper()}")

@bot.command()
async def hentai(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    embed = discord.Embed()
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member=None, *, reason: str=None):
    if user is None:
        await ctx.send("who would you like to ban?")
        return
    elif user == ctx.author:
        await ctx.send("cant ban yourself bro :sob: ")
        return
    else:pass
    try:
        await user.ban(reason=reason)
        await ctx.send(f"User {user.mention}({user.id}) has been banned for reason: {reason}")
    except Exception as e:
        await ctx.send(f"{e}")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):

         await ctx.send(f"Error: {error}")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member=None, *, reason: str=None):
    if user is None:
        await ctx.send("who would you like to kick?")
        return
    elif user == ctx.author:
        await ctx.send("cant kick yourself bro :sob: ")
        return
    else:pass
    try:
        await user.ban(reason=reason)
        await ctx.send(f"User {user.mention}({user.id}) has been kicked for reason: {reason}")
    except Exception as e:
        await ctx.send(f"{e}")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")


@bot.command()
async def sendhook(ctx, webhook, *, message):
    await ctx.message.delete()
    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        embed = discord.Embed(description=f"webhook not valid.", color=0x6495ED)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description=f"sucessfully sent {message} to {webhook}", color=0x6495ED)
        await ctx.send(embed=embed)

@bot.command()
async def restart(ctx):
    await ctx.message.delete()
    clear()
    os.system('python "' + os.getcwd() + "\\" + sys.argv[0] + '"')

@bot.command(aliases=["deleteall"])
async def d(ctx, limit: int=None):
    await ctx.message.delete()
    dt = datetime.datetime.now()
    current_time = dt.strftime("%H:%M:%S")
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1

@bot.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.channel.history(limit=amount):
        if message.author == bot.user:
            await message.delete()
        else:
            pass

@bot.command()
async def delhook(ctx, webhook: str):
    await ctx.message.delete()
    if not webhook:
        return
    else:
        r = requests.delete(webhook)
        if (r.status_code == 204):
            embed = discord.Embed(description=f"webhook was deleted successfully.", color=0x6495ED)
        else:
            embed = discord.Embed(description=f"failed to delete webhook. possibly deleted already or invalid.", color=0x6495ED)
            await ctx.send(embed=embed, delete_after=del_after)

@bot.command()
async def createdm(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    else:
        await member.create_dm()

if rich_presence:
    try:
        rpc = Presence(client_id='900216197000359986')
        rpc.connect()
        rpc.update(details='RapeV1 made by Xraq.', large_image='avatar')
    except Exception as e:
        print(f'')
        time.sleep(1)
    
        

bot.run(token, bot=False)
