import discord
from discord.ext import commands
import aiohttp
import asyncio
from bs4 import BeautifulSoup


bot = commands.Bot(command_prefix='!', )

@bot.event
async def on_ready():
    print('Logged in as: '+bot.user.name)
    print('Bot ID: '+bot.user.id)
    print('Invite Link Below')
    print('------')
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
    print('------')
    for server in bot.servers:
        print("Connected to server: {}".format(server))
    print('------')


async def connect():
    print('Logging in...')
    while not bot.is_closed:
        try:
            await bot.start('tokenhere')
        except:
            await asyncio.sleep(5)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

@bot.command(pass_context=True)
async def weather():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://www.fiveringsonline.com/weather/')
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find_all("div", {"class": "entry-content"})
        infotext = info[0].text
        with open('output.text', 'r+') as data:
            data.write(infotext)

        split = str(infotext).replace('\n', '').replace('\t', '')
        split = split.split('|')

        temp = split[0]
        forecast = split[1]
        wind = split[2]
        notes = split[3]

        embed = discord.Embed(colour=discord.Colour(0x608f30), url="https://discordapp.com",
                              description="```" + temp + '\n' +forecast + '\n' +wind + '\n' +notes + "```")
        await bot.say(
            content="**Weather in the Empire**",
            embed=embed)


bot.loop.run_until_complete(connect())
