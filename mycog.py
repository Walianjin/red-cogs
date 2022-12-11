import discord
from redbot.core import commands

from random import randint as rnd

from bs4 import BeautifulSoup as bs
import requests

url = "https://74.ru/horoscope/daily/"
r = requests.get(url)
funnygifs = [
    "https://tenor.com/view/jinx-the-cat-jinx-jinx-cat-cat-computer-gif-25786466",
    "https://tenor.com/view/%D1%81%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D1%82%D1%91%D0%BD%D0%BE%D0%BA-%D1%81%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9%D0%BA%D0%BE%D1%82%D1%91%D0%BD%D0%BE%D0%BA-%D0%BF%D0%BE%D1%80%D0%B0%D1%81%D0%BF%D0%B0%D1%82%D1%8C-cat-gif-17009684",
    "https://tenor.com/view/capybara-ok-he-pull-up-capybaras-car-meme-gif-25675731",
    "https://tenor.com/view/angry-cat-unhappy-cat-cat-unhappy-cat-mad-mad-cat-gif-21993656",
    "https://tenor.com/view/cat-%D0%BB%D0%B0%D0%B4%D0%BD%D0%BE-cat-meme-gif-26417117",
    "https://tenor.com/view/dripped-cock-swagging-out-gif-26186543",
    "https://tenor.com/view/livingintheh-gif-24229783"
]

def getgif():
    return funnygifs[rnd(0,len(funnygifs)-1)]

class horoscope(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, arg):
        await ctx.send(arg)

    @commands.command()
    async def changenick(self, ctx, member: discord.Member, *, nickname):
        if str(ctx.author) == "Savely_Chercov#0210":
            await member.edit(nick=nickname)
            await ctx.send("Ник "+str(member)+" изменен на "+nickname)

    @commands.command()
    async def gif(self, ctx):
        await ctx.send(getgif())

    @commands.command()
    async def гороскоп(self, ctx, arg="none"):
        preds = {}
        soup = bs(r.text, 'html.parser')
        for s in soup.select(".IjM3t"):
            for ln in s.select(".IGRa5"):
                sign = str(ln.select("h3")[0].text)
                pred = str(ln.select("div")[1].text)
                preds[sign.lower()] = sign+" - "+pred
        if arg == "none":
            msg = ""
            for i in preds:
                msg = msg+preds[i]+"\n\n"
                if len(msg) >= 1500:
                    await ctx.send(msg)
                    msg = ""
            if msg != "":
                await ctx.send(msg)
        elif arg: await ctx.send(preds.get(str(arg).lower(),getgif()))
#    @commands.command()
#    async def mycom(self, ctx):
#        """This does stuff!"""
#        # Your code will go here
#        await ctx.send("I can do stuff!")
