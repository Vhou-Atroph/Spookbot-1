import discord
import random
from random import *
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
import praw

vhou = '143423810014674945'

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='mons', help='Your pokemon!')
    async def mons(self, ctx):
        id = ctx.message.author.id
        name = ctx.message.author.name
        monlist = ("lists/" + str(id))
        list('```' + monlist + '```')

'''class Drilbur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
            
    @commands.command(name='drilcatch', help='invisible command: chance to catch drilbur at full health with a beast ball')
    async def drilcatch(self, ctx):
        catchrate = 45
        rng = randint(1, 1000)
        if rng > catchrate:
            await ctx.channel.send("<:drilbur:657312699541225502>Drilbur was not caught!")
            print("POKEFUN: Catch number was {}".format(rng))
        if rng < catchrate:
            await ctx.channel.send("<:drilbur:657312699541225502>Drilbur was caught! Congratulations on your new Drilbur!")
            member = ctx.message.author
            drilfile = open("misc/dril.txt",'a')
            drilfile.write("\nDrilbur caught on {:%Y-%m-%d %H:%M:%S} ".format(datetime.datetime.now()) + "by {}".format(member))
            drilfile.close()
            print("POKEFUN: Catch number was {}".format(rng))
            
    @commands.command(name='pokefun', help='commands for pokefun')
    async def dril(self, ctx):
        print("Sent pokefun help")
        embed = discord.Embed(title="Pokefun Help", description="Prefix is `s!`", color=0x771c85)
        embed.add_field(name="General commands:", value=`pokefun`: Shows this command.)
        embed.add_field(name="<:drilbur:657312699541225502>Drilbur Commands:", value=`drilcatch`: Try to catch a drilbur at full health with a Beast Ball!, inline=False)
        embed.add_field(name="<:glaceon:657315337879945256>Glaceon Commands:", value=`glaccatch`: Try to catch a glaceon at full health with a Beast Ball!, inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command(name='glaccatch', help='invisible command: chance to catch drilbur at full health with a beast ball')
    async def glaccatch(self, ctx):
        catchrate = 22
        rng = randint(1, 1000)
        if rng > catchrate:
            await ctx.channel.send("<:glaceon:657315337879945256>Glaceon was not caught!")
            print("POKEFUN: Catch number was {}".format(rng))
        if rng < catchrate:
            await ctx.channel.send("<:glaceon:657315337879945256>Glaceon was caught! Congratulations on your new Glaceon!")
            member = ctx.message.author
            glacfile = open("misc/glac.txt",'a')
            glacfile.write("\nGlaceon caught on {:%Y-%m-%d %H:%M:%S} ".format(datetime.datetime.now()) + "by {}".format(member))
            glacfile.close()
            print("POKEFUN: Catch number was {}".format(rng))'''