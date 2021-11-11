import discord
import random
from random import *
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
import praw
import tensorflow as tf
import gpt_2_simple as gpt2
import codecs
import tweepy

#client = discord.Client()
prefix = 's!'
desc = "Bot created by Vhou#2462."
bot = Bot(command_prefix=prefix, description=desc)
bot.remove_command('help')
vpfp = 'https://i.imgur.com/JuqlXQa.jpg'
version= 'v1.5.6'
#Reddit API
reddit = praw.Reddit(client_id='client_id',
                     client_secret='client_secret',
                     user_agent='user_agent')
#Twitter App - Flippy's Office. This was used to post tweets directly to the Toontown Facts account with a discord command.
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#On startup
@bot.event
async def on_ready():
    print('------')
    print('Spook time!'.format(bot))
    print('Logged in as...')
    print('USER: SpookBot#4794')
    print('ID: 650883667203194880')
    print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    print('------')
    await bot.change_presence(activity=discord.Game(name='in Hell'))
    
#GPT2 - The files to allow this to work have been deleted.
class Log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    global sess
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run8')
        
    @commands.command(name='gnu', help='Generates hell')
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def gnu(self, ctx, heehoo=""):
        print('Generating hell...')
        print('{} has called for Hell.'.format(ctx.author.name))
        print("Prompt: {}".format(heehoo))
        async with ctx.channel.typing():
            hell = gpt2.generate(sess, 
                run_name='run8',
                length=150,
                temperature=.8,
                prefix=heehoo,
                nsamples=1,
                batch_size=1,
                return_as_list=True)[0]
            await ctx.channel.send(hell)
        print(hell)
    
    @commands.command(name='log', help='Logs messages')
    async def log(self, ctx):
        await ctx.channel.send('**SLOG** | SLOG has been temporarily disabled. LAST SLOG: 5-2-2020')
        counter = []
        '''async for message in ctx.channel.history(limit=None):
            print('Logging messages...')
            logtxt = open("misc/log.txt", 'a+', encoding="utf8")
            counter.append(message)
            #messages = msg = await ctx.channel.history(limit=1).get()
            logtxt.write(str(message.content) + "\n")'''

#Bot commands
class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command(name='ping', help='Pong') 
    async def ping(self, ctx):
        print('Pong at {:%Y-%m-%d %H:%M:%S}!'.format(datetime.datetime.now()))
        await ctx.channel.send(':ping_pong:|Pong at {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        
    @commands.command(name='invite', help="Invite the bot to your server")
    async def invite(self, ctx):
        print("Invite requested.")
        embed = discord.Embed(title="Invite SpookBot!", description="Invite me to your server!", color=0x771c85)
        embed.set_thumbnail(url="https://i.imgur.com/MTmbIpO.jpg")
        embed.add_field(name="Link:", value="[Click here!](https://discordapp.com/api/oauth2/authorize?client_id=650883667203194880&permissions=392256&scope=bot)", inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command(name='help', help='Shows this command.')
    async def help(self, ctx):
        print("Sent help")
        embed = discord.Embed(title="Help", description="Prefix is `s!`", color=0x771c85)
        embed.add_field(name=":robot:Bot Commands:", value='''`ahelp`: Admin help.
`help`: Shows this command. 
`info`: Information about the bot.
`invite`: Invite the bot to your server! 
`ping`: Pong.''', inline=False)
        embed.add_field(name=":game_die:Fun Commands:", value='''`cringe`: Uh, bro, you just posted cringe.
`gnu [prompt]`: Generates a funny with GPT2. **(20 second cooldown)**
`nolaugh`: Not funny, didn't laugh.
`roll [#]`: Rolls a die.
`sadcat`: Finds a random post from r/sadcats.''', inline=False)
        embed.add_field(name="<:rathalos:657007621055840283>Monster Hunter Commands:", value='''`localemhw`: Chooses a random locale from Monster Hunter World.
`monmhw`: Chooses a random monster from Monster Hunter World.
`weaponmhw`: Chooses a random weapon from Monster Hunter World.''', inline=False)
        embed.add_field(name="<:tewtow:657007812471291918>Toontown Commands:", value='''`coghp [#]`: Evaluates cog health from levels 1-12.
`flippy`: Toontask
`makeatoon`: It's time to make a new toon!
`namett`: Generates a random toon name.
`randcogboss`: Chooses a random cog boss from Toontown.''', inline=False)
        await ctx.channel.send(embed=embed)
        
    @commands.command(name='info', help='Information about the bot!')
    async def info(self, ctx):
        print("Sent info")
        servers = str(len(bot.guilds))
        embed = discord.Embed(title="About Spookbot", description="Spook time!", color=0x771c85)
        embed.set_thumbnail(url=vpfp)
        embed.add_field(name="Creator:", value="Vhou#2462", inline=False)
        embed.add_field(name="ID", value='650883667203194880', inline=False)
        embed.add_field(name="Creation date:", value="December 2nd, 2019", inline=False)
        embed.add_field(name="Number of servers:", value=servers, inline=False)
        embed.add_field(name="Version:", value=version)
        await ctx.channel.send(embed=embed)

#Toontown commands
class Toontown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command(name='coghp', help='Evaluates cog health from levels 1-12')
    async def coghp(self, ctx, lvl):
        lvl = int(lvl)
        if lvl > 0 and lvl < 12:
            hp = (lvl+1)*(lvl+2)
            print('Cog health evaluated! Cog health:{}'.format(hp))
            await ctx.channel.send('The cog has {} health.'.format(hp))
        if lvl > 11 and lvl < 13:
            print('Cog health evaluated! Cog health: 200')
            await ctx.channel.send('Level 12 cogs always have 200 health.')
        if lvl < 1:
            await ctx.channel.send('Please send a different number.')
        if lvl > 12:
            await ctx.channel.send('Please send a different number.')
            
    @commands.command(name='randcogboss', help='Chooses a random cog boss from Toontown.')
    async def randcogboss(self, ctx):
        embed = discord.Embed(title="Let's go fight the cogs!", description=" ", color=0xDECD9F)
        embed.set_author(name='Flippy',
        icon_url="https://i.imgur.com/XQvuCmn.png")
        bosses = ['vp', 'cfo', 'cj', 'ceo']
        chosen = choice(bosses)
        if chosen == 'vp':
            embed.add_field(name="Let's go fight the VP!", value="Sellbot", inline=False)
            embed.set_image(url="https://i.imgur.com/F6lznzP.jpg")
        if chosen == 'cfo':
            embed.add_field(name="Let's go fight the CFO!", value="Cashbot", inline=False)
            embed.set_image(url="https://i.imgur.com/HFTG7re.jpg")
        if chosen == 'cj':
            embed.add_field(name="Let's go fight the CJ!", value="Lawbot", inline=False)
            embed.set_image(url="https://i.imgur.com/ybfXcY6.jpg")
        if chosen == 'ceo':
            embed.add_field(name="Let's go fight the CEO!", value="Bossbot", inline=False)
            embed.set_image(url="https://i.imgur.com/w4qVrPX.jpg")
        print("Randcogboss chose {}".format(chosen))
        await ctx.channel.send(embed=embed)
        
    @commands.command(name='makeatoon', help='Creates a random toon!')
    async def createatoon(self, ctx):
        embed = discord.Embed(title="Time to make a new toon!", description=" ", color=0xDECD9F)
        embed.set_author(name='Flippy',
        icon_url="https://i.imgur.com/XQvuCmn.png")    
        sp = ['Cat', 'Dog', 'Pig', 'Bear', 'Monkey', 'Crocodile', 'Deer', 'Mouse', 'Duck', 'Horse', 'Rabbit']
        species = choice(sp)
        embed.add_field(name="Species:", value=species)
        gend = ['Boy', 'Girl']
        gen = choice(gend)
        embed.add_field(name="Gender:", value=gen)
        gags1 = ['Toon-up', 'Trap', 'Lure', 'Sound', 'Drop']
        gags2 = ['Toon-up', 'Trap', 'Lure', 'Sound', 'Throw', 'Squirt', 'Drop']
        nogag = choice(gags1)
        orggag = choice(gags2)
        if nogag == orggag:
            nogag = choice(gags1)
            orggag = choice(gags2)
        embed.add_field(name="They will be:", value="{}less".format(nogag), inline=False)
        embed.add_field(name="They will have:", value="Organic {}".format(orggag), inline=False)
        sizes1 = ['1', '2', '3', '4']
        sizes2 = ['Long', 'Medium', 'Small']
        if species == 'Mouse':
            sizes1 = ['1', '2']
        headstyle = choice(sizes1)
        bodysize = choice(sizes2)
        legsize = choice(sizes2)
        embed.add_field(name="Head style:", value=headstyle)
        embed.add_field(name='Body size:', value=bodysize)
        embed.add_field(name='Leg size:', value=legsize)
        croll = ['full color', 'legs different', 'mixed']
        crolla = choice(croll)
        colors = ['Peach','Bright Red','Red','Maroon','Sienna','Brown','Tan','Coral','Orange','Yellow','Cream','Citrine','Lime','Sea green','Green','Light blue','Aqua','Blue','Periwinkle','Royal blue',
        'Slate blue','Purple','Lavender','Pink','Rose pink','Ice blue','Mint green','Emerald','Teal','Apricot','Amber','Crimson red','Forest green','Steel blue','Beige','Bubblegum'
        #All colors as of 12-18-2019
        ]
        if crolla == 'full color':
            fullcolor = choice(colors)
            embed.add_field(name="Toon color:", value=fullcolor)
        if crolla == 'legs different':
            headtorso = choice(colors)
            legs = choice(colors)
            embed.add_field(name="Head and torso color:", value=headtorso)
            embed.add_field(name="Leg color:", value=legs)
        if crolla == 'mixed':
            head = choice(colors)
            torso = choice(colors)
            legs = choice(colors)
            embed.add_field(name='Head color:', value=head)
            embed.add_field(name='Torso color:', value=torso)
            embed.add_field(name='Leg color:', value=legs)
        await ctx.channel.send(embed=embed)
        print("Made a new toon!")
        
    @commands.command(name='namett', help='Chooses a random cog boss from Toontown.')
    async def namett(self, ctx):
            g = ['m', 'f']
            gender = choice(g)
            if gender == 'm':
                title = ['Baron','Big','Cap\'n','Captain','Chef','Chief','Coach','Colonel','Cool','Count','Crazy','Daring','Deputy','Dippy','Doctor','Dr.','Duke','Fat','Good ol\'','Grand ol\'',
                'Grumpy','Judge','King','Little','Loopy','Loud','Lucky','Master','Mister','Mr.','Noisy','Prince','Prof.','Sergeant','Sheriff','Silly','Sir','Skinny','Super','Ugly','Weird'] 
                #God I hope TTR doesn't add anymore names, I haven't even done the rest yet and this is horrible
                first = ["Albert","Alvin","Arnold","Astro","B.D.","Banjo","Barney","Bart","Batty","Beany","Bebop","Bentley","Beppo","Bert","Billy","Bingo","Binky","Biscuit","Bizzy","Blinky","Bob",
                "Bonbon","Bongo","Bonkers","Bonzo","Boo Boo","Boots","Bouncey","Bruce","Bud","Buford","Bumpy","Bunky","Buster","Butch","Buzz","C.J.","C.W.","Casper","Cecil","Chester","Chewy","Chip",
                "Chipper","Chirpy","Chunky","Clancy","Clarence","Cliff","Clyde","Coconut","Comet","Cookie","Corky","Corny","Cranky","Crazy","Cricket","Crumbly","Cuckoo","Curly","Curt","Daffy","Dave",
                "Davey","David","Dinky","Dizzy","Domino","Dot","Drippy","Droopy","Dudley","Duke","Dusty","Dynamite","Elmer","Ernie","Fancy","Fangs","Felix","Finn","Fireball","Flapjack","Flappy",
                "Fleabag","Flint","Flip","Fluffy","Freckles","Fritz","Frizzy","Funky","Furball","Gale","Garfield","Gary","Giggles","Goopy","Graham","Grouchy","Gulliver","Gus","Hans","Harvey","Harry",
                "Hector","Huddles","Huey","J.C.","Jack","Jacques","Jake","Jazzy","Jellyroll","Jester","Jimmy","Johan","John","Johnny","Kippy","Kit","Knuckles","Lancelot","Lefty","Leo","Leonardo",
                "Leroy","Lionel","Lloyd","Lollipop","Loony","Loopy","Louie","Lucky","Mac","Max","Maxwell","Mildew","Milton","Moe","Monty","Murky","Ned","Nutty","Olaf","Orville","Oscar","Oswald",
                "Ozzie","Pancake","Peanut","Peppy","Pickles","Pierre","Pinky","Phil","Poe","Popcorn","Poppy","Presto","Reggie","Rhubarb","Ricky","Rocco","Rodney","Roger","Rollie","Romeo","Roscoe",
                "Rover","Rusty","Salty","Sammie","Scooter","Skids","Skimpy","Skip","Skipper","Skippy","Slappy","Slippy","Slumpy","Smirky","Snappy","Sniffy","Snuffy","Soupy","Spiffy","Spike","Spotty",
                "Spunky","Squeaky","Star","Stinky","Stripey","Stubby","Teddy","Tex","Tom","Tricky","Tubby","von","Wacko","Wacky","Waldo","Wally","Wesley","Whiskers","Wilbur","William","Winky","Yippie",
                "Z.Z.","Zany","Ziggy","Zilly","Zippety","Zippy","Zowie"]
                t = choice(title)
                f = choice(first)
            if gender == 'f':
                title = ["Aunt","Big","Cap'n","Captain","Colonel","Cool","Crazy","Deputy","Dippy","Doctor","Fat","Good ol'","Granny","Lady","Little","Loopy","Loud","Miss","Noisy","Princess","Prof.",
                "Queen","Sheriff","Silly","Skinny","Super","Ugly","Weird"]
                first = ["Blinky","Bongo","Bonkers","Bonnie","Boo Boo","Bouncey","Bubbles","Bumpy","C.J.","C.W.","Candy","Chirpy","Chunky","Clover","Coconut","Comet","Corky","Corny","Cranky","Crazy",
                "Cricket","Crumbly","Cuckoo","Cuddles","Curly","Daffodil","Daffy","Daphne","Dee Dee","Dinky","Dizzy","Domino","Dottie","Drippy","Droopy","Dusty","Dynamite","Fancy","Fangs","Fireball",
                "Flapjack","Flappy","Fleabag","Flip","Fluffy","Freckles","Frizzy","Furball","Ginger","Goopy","Gwen","Huddles","J.C.","Jazzy","Jellyroll","Kippy","Kit","Ladybug","Lefty","Lily","Lollipop",
                "Loony","Loopy","Lucky","Marigold","Maxie","Melody","Mildew","Mo Mo","Murky","Nutmeg","Nutty","Olive","Pancake","Peaches","Peanut","Pearl","Penny","Peppy","Petunia","Pickles","Pinky",
                "Popcorn","Poppy","Presto","Rainbow","Raven","Rhubarb","Robin","Rosie","Roxy","Sadie","Sally","Salty","Sandy","Scooter","Skids","Skimpy","Slappy","Slippy","Slumpy","Smirky","Snappy",
                "Sniffy","Snuffy","Soupy","Spiffy","Spotty","Spunky","Squeaky","Star","Stripey","Stubby","Taffy","Tricky","Trixie","Tubby","Ursula","Valentine","Vicky","Violet","von","Wacko","Wacky",
                "Whiskers","Willow","Winky","Yippie","Z.Z.","Zany","Ziggy","Zilly","Zippety","Zippy","Zowie"]
                t = choice(title)
                f = choice(first)
            last1 = ["Bagel","Banana","Bean","Beanie","Biggen","Bizzen","Blubber","Boingen","Bumber","Bumble","Bumpen","Cheezy","Crinkle","Crumble","Crunchen","Crunchy","Dandy","Dingle","Dizzen",
            "Dizzy","Doggen","Dyno","Electro","Feather","Fiddle","Fizzle","Flippen","Flipper","Frinkel","Fumble","Funny","Fuzzy","Giggle","Glitter","Google","Grumble","Gumdrop","Huckle","Hula",
            "Jabber","Jeeper","Jinx","Jumble","Kooky","Lemon","Loopen","Mac","Mc","Mega","Mizzen","Nickel","Nutty","Octo","Paddle","Pale","Pedal","Pepper","Petal","Pickle","Pinker","Poodle",
            "Poppen","Precious","Pumpkin","Purple","Rhino","Robo","Rocken","Ruffle","Smarty","Sniffle","Snorkle","Sour","Spackle","Sparkle","Squiggle","Super","Thunder","Toppen","Tricky","Tweedle",
            "Twiddle","Twinkle","Wacky","Weasel","Whisker","Whistle","Wild","Witty","Wonder","Wrinkle","Ziller","Zippen","Zooble"]
            last2 = ["batch","bee","berry","blabber","bocker","boing","boom","bop","bounce","bouncer","brains","bubble","bumble","bump","bumper","burger","butter","chomp","corn","crash","crumbs",
            "crump","crunch","dazzle","doodle","dorf","face","fidget","fink","fish","flap","flapper","flinger","flip","flipper","foot","fuddy","fussen","gabber","gadget","gargle","gloop","glop",
            "glow","goober","goose","grin","grooven","grump","hoffer","hopper","jinks","klunk","knees","loop","loose","marble","mash","masher","melon","mew","monkey","mooch","mouth","muddle",
            "muffin","mush","nerd","noodle","nose","nugget","paws","phew","phooey","pocket","poof","pop","pounce","pow","pretzel","quack","roni","scooter","screech","smirk","snooker","snoop",
            "snout","socks","speed","son","song","sparkles","speed","spinner","splat","sprinkles","sprocket","squeak","sticks","stink","swirl","tail","teeth","thud","toes","ton","toon","tooth",
            "twist","whatsit","whip","whirl","wicket","wig","wiggle","wire","woof","zaner","zap","zapper","zilla","zoom","zoop"]
            l1 = choice(last1)
            l2 = choice(last2)
            nametypes = ['titlefirst', 'first', 'titlelast', 'firstlast', 'last', 'all']
            nametype = choice(nametypes)
            if nametype == 'titlefirst':
                name = (t + " " + f)
            if nametype == 'first':
                name = (f)
            if nametype == 'firstlast':
                name = (f + " " + l1 + l2)
            if nametype == 'titlelast':
                name = (t + " " + l1 + l2)
            if nametype == 'last':
                name = (l1 + l2)
            if nametype == 'all':
                name = (t + " " + f + " " + l1 + l2)
            await ctx.channel.send("Your randomly generated name is: {}".format(name))
            print("Generated name: {}".format(name))
            
    @commands.command(name='flippy', help="Toontask")
    async def flippy(self, ctx):
        embed = discord.Embed(title="Toontask", color=0xFFFFBF)
        embed.set_author(name='Flippy',
        icon_url="https://i.imgur.com/XQvuCmn.png")
        await ctx.channel.send(embed=embed)
        print('Flippy Toontask')
       
    @commands.command(name='dmgtt', help="Evaluates combo damage.")
    async def dmgtt(self, ctx, lure="unlured", g1=0, g2=0, g3=0, g4=0):
        #EXPLANATION: lure will add a 20% bonus to damage, it is necessary to note if the cog is lured or not.
        #G1-G4 represent how much damage a gag does. If you memorize how much damage each gag does, this is useful. If you don't, oh no.
        #I can probably create a variable system for gag names, that would be interesting. But for now, this will be the command.
        print("Evaluating gag damage....")
        if lure == "unlured":
            print("COG is unlured.")
            raw = (g1+g2+g3+g4)
            print("RAW DAMAGE: {}".format(raw))
            total = (raw+(20%(raw)))
            print("TOTAL DAMAGE: {}".format(total))
            await ctx.channel.send("The total damage for this turn is: {}".format(total))
        if lure == "lured": #Does not work with sound
            print("COG is lured.")
            raw = (g1+g2+g3+g4)
            print("RAW DAMAGE: {}".format(raw))
            total = (raw+(20%(raw))+(50%(raw)))
            print("TOTAL DAMAGE: {}".format(total))
            await ctx.channel.send("The total damage for this turn is: {}".format(total))
        if lure != "unlured" and lure != "lured":
            print("It was not specified if the cog was lured or unlured.")
            await ctx.channel.send("Please make sure to specify whether the cog is lured or not.")
            
    #Toontown lists?!
            
#Monster Hunter commands
class MonsterHunter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='monmhw', help="Chooses a random monster from Monster Hunter World", category="Monster Hunter")
    async def randmonster1(self, ctx):
        embed = discord.Embed(title="Wanna fight a meownster?", description="Your meownster is:", color=0x771c85)
        embed.set_author(name='Palico',
        icon_url="https://i.imgur.com/DLiK3dA.png")
        all_images = ["https://i.imgur.com/sWJGHF1.png", #Zinogre,
        "https://i.imgur.com/eppblI5.png", #Yian Garuga
        "https://i.imgur.com/IBR4DNn.png", #Banbaro
        "https://i.imgur.com/WGeJmw6.png", #Tigrex
        "https://i.imgur.com/5xoop0G.png", #Rajang
        "https://i.imgur.com/TKog8EJ.png", #Deviljho
        "https://i.imgur.com/N2T9r5D.png", #Odogaron
        "https://i.imgur.com/5tbvqVK.png", #Acidic Glavenus
        "https://i.imgur.com/M2uNBbe.png", #Anjanath
        "https://i.imgur.com/CJnvuiz.png", #Azure Rathalos
        "https://i.imgur.com/xKBE6Dj.png", #Barioth
        "https://i.imgur.com/p1npCfR.png", #Barroth
        "https://i.imgur.com/zDzsYZl.png", #Bazelgeuse
        "https://i.imgur.com/aQIlazX.png", #Beotodus
        "https://i.imgur.com/ja2QZuH.png", #Black Diablos
        "https://i.imgur.com/oSFpnR5.png", #Blackveil Vaal Hazak
        "https://i.imgur.com/yx4l5NQ.png", #Brachydios
        "https://i.imgur.com/2v67kV0.png", #Brute Tigrex
        "https://i.imgur.com/HUVAFXa.png", #Coral Pukei-Pukei
        "https://i.imgur.com/3hogwHZ.png", #Diablos
        "https://i.imgur.com/bLW8Oxi.png", #Dodogama
        "https://i.imgur.com/VQnT3FN.png", #Ebony Odogaron
        "https://i.imgur.com/wq52tcg.png", #Fulgur Anjanath
        "https://i.imgur.com/CwyKuUG.png", #Glavenus
        "https://i.imgur.com/HAex2iE.png", #Gold Rathian
        "https://i.imgur.com/8CSUXZn.png", #Great Girros
        "https://i.imgur.com/Ngbsqiu.png", #Great Jagras
        "https://i.imgur.com/X4vVQP1.png", #Jyuratodus
        "https://i.imgur.com/Mm5l6hz.png", #Kirin
        "https://i.imgur.com/1eUUiqU.png", #Kulu Ya-Ku
        "https://i.imgur.com/nyO86fR.png", #Kulve Taroth
        "https://i.imgur.com/aLn7mZf.png", #Kushala Daora
        "https://i.imgur.com/WoF63sQ.png", #Lavasioth
        "https://i.imgur.com/2dRWCna.png", #Legiana
        "https://i.imgur.com/MPcBrPt.png", #Lunastra
        "https://i.imgur.com/fC6RX57.png", #Namielle
        "https://i.imgur.com/6BtWHJv.png", #Nargacuga
        "https://i.imgur.com/6XX17Br.png", #Nergigante
        "https://i.imgur.com/1AYC5mU.png", #Nightshade Paolumu
        "https://i.imgur.com/knFSYkz.png", #Paolumu
        "https://i.imgur.com/1ex73Sd.png", #Pink Rathian
        "https://i.imgur.com/mJ3x9Kp.png", #Pukei-Pukei
        "https://i.imgur.com/Z6C5k91.png", #Radobaan
        "https://i.imgur.com/TUvW8lb.png", #Rathalos
        "https://i.imgur.com/RuJyy2r.png", #Rathian
        "https://i.imgur.com/Stjv833.png", #Ruiner Nergigante
        "https://i.imgur.com/Cdr8jcE.png", #Safi'Jiiva
        "https://i.imgur.com/aZmNfFx.png", #Savage Deviljho
        "https://i.imgur.com/cADIsUb.png", #Scarred Yian Garuga
        "https://i.imgur.com/3qNP6NZ.png", #Seething Bazelgeuse
        "https://i.imgur.com/XsoYYRi.png", #Shara Ishvalda
        "https://i.imgur.com/46XlpZS.png", #Shrieking Legiana
        "https://i.imgur.com/oYNEyoe.png", #Silver Rathalos
        "https://i.imgur.com/ozZoa8v.png", #Stygian Zinogre
        "https://i.imgur.com/6FkyvQj.png", #Teostra
        "https://i.imgur.com/PkwrvzT.png", #Tobi-Kadachi
        "https://i.imgur.com/hxxqCxz.png", #Tzitzi Ya-Ku
        "https://i.imgur.com/3eZtmuH.png", #Urugaan
        "https://i.imgur.com/Q2cS7R4.png", #Vaal Hazak
        "https://i.imgur.com/fQCjbGm.png", #Velkhana
        "https://i.imgur.com/6mT3ILQ.png", #Viper Tobi-Kadachi
        "https://i.imgur.com/qrPSToa.png", #Xeno'Jiiva
        "https://i.imgur.com/MhIu77b.png", #Zorah Magdaros
        "https://vignette.wikia.nocookie.net/monsterhunter/images/6/6d/MHWI-Alatreon_Icon.png", #Alatreon
        "https://vignette.wikia.nocookie.net/monsterhunter/images/6/6a/MHWI-Furious_Rajang_Icon.png", #Furious Rajang
        "https://vignette.wikia.nocookie.net/monsterhunter/images/6/68/MHWI-Raging_Brachydios_Icon.png", #Raging Brachydios
        ]
        chosen = choice(all_images)
        embed.set_image(url=chosen)
        print("Randmonster chose {}".format(chosen))
        await ctx.channel.send(embed=embed)
        
    @commands.command(name='weaponmhw', help='Chooses a random weapon from Monster Hunter World.')
    async def weaponmhw(self, ctx):
        weaponlist = ['Sword and Shield!<:sns:657013172732952576>', 'Dual Blades!<:db:657012868285333534>', 'Greatsword!<:gs:657012887239393280>', 'Longsword!<:ls:657013124423221248>',
        'Hammer!<:hm:657012981556838410>', 'Bow!<:mhbow:657012914477203467>', 'Light Bowgun!<:lbg:657013097537732625>', 'Heavy Bowgun!<:hbg:657013016570888221>',
        'Hunting Horn!<:hh:657013036183191582>', 'Lance!<:l_:657013076448641058>', 'Gunlance!<:gl:657012959154798650>', 'Insect Glaive!<:ig:657013054713757718>', 'Chargeblade!<:cb:657012935671152690>',
        'Switchaxe!<:sax:657013157570674698>']
        weapon = choice(weaponlist)
        print("Weaponmhw chooses {}!".format(weapon))
        await ctx.channel.send("Let's play {}".format(weapon))
        
    @commands.command(name='localemhw', help='Chooses a random locale from Monster Hunter World.')
    async def localemhw(self, ctx):
        locales = ['Ancient Forest', 'Wildspire Waste', 'Coral Highlands', 'Rotten Vale', 'Everstream', 'Confluence of Fates', 'Hoarfrost Reach', 'Caverns of El Dorado', 'Guiding Lands',
        'Secluded Valley', 'Origin Isle']
        chosen = choice(locales)
        print('Chosen locale: {}'.format(chosen))
        embed = discord.Embed(title="Let's go somewhere!", description="Let's visit the {}!".format(chosen), color=0x771c85)
        embed.set_author(name='Palico',
        icon_url="https://i.imgur.com/DLiK3dA.png")
        if chosen == 'Ancient Forest':
            embed.set_image(url='https://i.imgur.com/MCgyIbJ.jpg')
        if chosen == 'Wildspire Waste':
            embed.set_image(url='https://i.imgur.com/C5OlxhP.jpg')
        if chosen == 'Coral Highlands':
            embed.set_image(url='https://i.imgur.com/8HqSMZE.jpg')
        if chosen == 'Rotten Vale':
            embed.set_image(url='https://i.imgur.com/5J4x8GN.jpg')
        if chosen == 'Everstream':
            embed.set_image(url='https://i.imgur.com/dTYVyqD.png')
        if chosen == 'Confluence of Fates':
            embed.set_image(url='https://i.imgur.com/clsZUUS.jpg')
        if chosen == 'Hoarfrost Reach':
            embed.set_image(url='https://i.imgur.com/n3HddqE.jpg')
        if chosen == 'Caverns of El Dorado':
            embed.set_image(url='https://i.imgur.com/7eWqB6h.jpg')
        if chosen == 'Guiding Lands':
            embed.set_image(url='https://i.imgur.com/A1YWq8o.jpg')
        if chosen == 'Secluded Valley':
            embed.set_image(url='https://i.imgur.com/8DYLZFD.jpg')
        if chosen == 'Origin Isle':
            embed.set_image(url="https://i.imgur.com/Nt5mmOP.png")
        await ctx.channel.send(embed=embed)
            
#Fun commands
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command(name='nolaugh', help="Not funny, didn't laugh.")
    async def nolaugh(self, ctx):
        print("Not funny, didn't laugh.")
        await ctx.channel.send(file=discord.File('images/notfunny.gif'))

    @commands.command(name='roll', help='Rolls a die')
    async def roll(self, ctx, arg):
        arg = int(arg)
        die = randint(1, arg)
        print("Rolled a {}".format(die))
        await ctx.channel.send('You rolled a {}!'.format(die))
    
    @commands.command(name='cringe', help="Bro, you just posted cringe!")
    async def cringe(self, ctx):
        print("Uh, bro, you just posted cringe...")
        await ctx.channel.send(file=discord.File('videos/bro.mp4'))
        
    @commands.command(name='sadcat', help='Finds a sad cat!')
    async def sadcat(self, ctx):
        print("Finding a sad cat...")
        subreddit = reddit.subreddit('sadcats').top()
        limit = randint(1, 100)
        for i in range(0, limit):
            submission = next(x for x in subreddit if not x.stickied)
        embed = discord.Embed(title=submission.title, description=submission.url, color=0x771c85)
        embed.set_author(name='r/sadcats',
        icon_url="https://i.imgur.com/zhNJqKD.png")
        embed.set_image(url=submission.url)
        await ctx.channel.send(embed=embed)
        print("Sad Cat found! {}".format(submission.url))
        print("Submission #{}".format(limit))
        
#FR commands
class FR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
            
    @commands.command(name='localefr', help='Chooses a random locale from Flight Rising.')
    async def localefr(self, ctx):
        print("Choosing FR locale...")
        locales = ['Training Fields', 'Woodland Path', 'Scorched Forest', 'Sandswept Delta', 'Blooming Grove', 'Forgotten Cave', 'Bamboo Falls', 'Thunderhead Savanna', 'Redrock Cove', 'Waterway',
        'Arena', 'Volcanic Vents', 'Rainsong Jungle', 'Boreal Wood', 'Crystal Pools', 'Harpy\'s Roost', 'Ghostlight Ruins', 'Mire', 'Golem Workshop', 'Kelp Beds']
        phrases = ["Why not visit the {}?", "Let's go grind at the {}!", "I think you should spend a couple hours at the {}.", "There may not be good loot, but you'll have a blast at the {}.",
        "Let's check out the {}!", "Look, I know it's a hard locale but you really should check out the {}.", "I've heard some wacky tales about great loot at the {}.", 
        "There is no locale besides the {}.", "{} is a pretty easy locale.", "{} is gonna be a blast to grind at!"
        ]
        phrase = choice(phrases)
        locale = choice(locales)
        visit = (phrase.format(locale))
        print(visit)
        await ctx.channel.send(visit)        

#ADMIN
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    async def is_owner(ctx):
        return ctx.author.id == 143423810014674945
    
    @commands.command(name='amiadmin', help='It\'s like a vibe check, but worse.')
    @commands.check(is_owner)
    async def amiadmin(self, ctx):
        print("An admin was checked: {}".format(ctx.author.name))
        await ctx.channel.send("You are an admin!")
    @amiadmin.error
    async def amiadmin_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')
            
    @commands.command(name='tweetfact', help='Tweets to the Toontown Facts account.')
    @commands.check(is_owner)
    async def tweetfact(self, ctx, tweet):
        print("A tweet has been posted by Toontown Facts: {}".format(tweet))
        api.update_status(status=tweet)
        await ctx.channel.send("Tweeted '{}'".format(tweet))
    @tweetfact.error
    async def tweetfact_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')
            
    @commands.command(name='ahelp', help="Help, but for admins.")
    @commands.check(is_owner)
    async def ahelp(self, ctx):
        print("Admin help sent!")
        embed = discord.Embed(title="Admin Help", description="It's like normal help, but for admins.", color=0x771c85)
        embed.set_author(name='Spookbot',
        icon_url="https://i.imgur.com/O5UsZ8G.png")
        embed.add_field(name="<:glaceon:657315337879945256>Commands:", value='''`ahelp`: Help, but for admin commands.
`amiadmin`: It's like a vibe check, but so much worse.
`dmuser [user id] [message]`: Send a DM to a specified user.
`msgsend [channel id] [message]`: Send a message to a specified channel.
`tweetfact [tweet]`: Tweets a fact as @FactsToontown.''', inline=False)
        await ctx.channel.send(embed=embed)
    @ahelp.error
    async def ahelp_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')
            
    @commands.command(name='msgsend', help="Sends a message as bot to a specified channel.")
    @commands.check(is_owner)
    async def msgsend(self, ctx, cnl, msg):
        print("Message sent to another channel: {}".format(msg))
        channel = bot.get_channel(int(cnl))
        await channel.send(msg)
    @msgsend.error
    async def msgsend_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')
        else:
            raise error

    @commands.command(name='dmuser', help="Sends a DM to a specified user.")
    @commands.check(is_owner)
    async def dmuser(self, ctx, usr, msg):
        print("DM sent to {}:".format(usr) + " {}".format(msg))
        user = bot.get_user(int(usr))
        await user.send("{}".format(msg))
    @msgsend.error
    async def msgsend_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            print("Someone used an admin command: {}".format(ctx.author.name))
            await ctx.channel.send('You are not an admin.')
        else:
            raise error
            
#Add cogs
bot.add_cog(Bot(bot))
bot.add_cog(Toontown(bot))
bot.add_cog(MonsterHunter(bot))
bot.add_cog(Fun(bot)) 
bot.add_cog(FR(bot)) 
bot.add_cog(Log(bot))
bot.add_cog(Admin(bot))

bot.run('token')