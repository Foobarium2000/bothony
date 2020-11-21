import discord
import random
import asyncio
import os
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands.cooldowns import BucketType

client = commands.Bot(command_prefix = "a$")
client.remove_command("help")
status = cycle(["to get help", "type a$commands"])

@client.event
async def on_ready():
     change_status.start()
     print("Bot is ready!")

@tasks.loop(seconds=4)
async def change_status():
     await client.change_presence(activity=discord.Game(next(status)))         

@client.event
async def on_member_join(member):
      print(f"{member} has joined a server!")

@client.event
async def on_member_remove(member):
     print(f"{member} has left a server!")

@client.event
async def on_member_update(before, after):
     n = after.nick
     if n:
         if n.lower().count("Anthonyjrvill") > 0:
             last = before.nick
             if last :
                 await after.edit(nick=last)    
             else:
                 await after.edit(nick="can you don't")  

@client.command()
async def load(ctx, extension):
     client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
     client.unload_extension(f'cogs.{extension}')

@client.command()
async def ping(ctx):
     await ctx.send(f"Pong! Your latency is {round(client.latency * 1000)}ms")

@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, question):
     author = ctx.message.author

     responses = ["It is certain.","Shit idk.","Why don't you ask later?","Yes! why would you ask me that?","Definitely not!","The law requires me to say no.","I think most likely.","Error cannot answer now!","Could you repeat that again?","Hell No!"]
     
     embed = discord.Embed(colour = discord.Colour.orange())
     
     embed.set_author(name="8ball")
     embed.add_field(name=f'{question}', value = "The 8ball says " + f'{random.choice(responses)}', inline = False)
     
     await ctx.send(author, embed=embed)

@client.command()
async def imagine(ctx):
     hypos = ["dying", "going to sleep", "being a bot", "destroying LMG07", "using RC24", "listening to me", "using the official discord app", "uhh hmm well I have no idea what to give you to imagine", "using this command instead of any other commands", "eating or drinking or doing any bodily functions", "cheese"]
     await ctx.send("imagine " + f'{random.choice(hypos)}')

@client.command(aliases=["help", "commands"])
async def _help(ctx):
      emoji = '✔️'
      author = ctx.message.author

      embed = discord.Embed(colour = discord.Colour.green())

      embed.set_author(name="Commands")
      embed.add_field(name="a$botinfo", value="Shows information about Bothony", inline=False)
      embed.add_field(name="a$suggest (command) (description)", value="Send in a command suggestion to be added into the bot!", inline=False)
      embed.add_field(name="a$ping", value="Returns the latency", inline=False)
      embed.add_field(name="a$8ball (question)", value="Give it a question and the 8ball will answer", inline=False)
      embed.add_field(name="a$say (text)",value="Makes the bot say whatever you want!", inline=False)
      embed.add_field(name="a$rnumber", value="Gives a random number between 1-10000",inline=False)
      embed.add_field(name="a$imagine", value="Gives you something to imagine", inline=False)
      embed.add_field(name="a$tts", value="Say something under the gTTS module", inline=False)
      embed.add_field(name="a$join/a$connect", value="Joins a voice channel", inline=False)
      embed.add_field(name="a$leave/a$end", value="Leaves the voice channel", inline=False)
      embed.add_field(name="a$play (song)", value="Plays a song", inline=False)
      embed.add_field(name="a$skip", value="Gives a voting system to skip a song", inline=False)
      embed.add_field(name="a$now/playing", value="Shows what song is currently playing", inline=False)
      embed.add_field(name="a$queue", value="Shows a queue for songs", inline=False)
      embed.add_field(name="a$tgt", value="Play Tails Gets Trolled The Game", inline=False)
      embed.add_field(name="a$terminal", value="Runs the self-made terminal", inline=False)
      embed.add_field(name="a$term_help", value="Dms you a help page for terminal", inline=False)

      await ctx.message.add_reaction(emoji)
      await author.send(author, embed=embed)
      
@client.command(aliases=["Say"])
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.send(mesg)
    await ctx.message.delete()
    
@client.command()
async def rnumber(ctx):
    r=random.randint(1,10000)
    await ctx.send("Your number is " + str(r))

@client.command()
async def botinfo(ctx):
     embed = discord.Embed(colour = discord.Colour.green())
     embed.set_author(name="Information")
     embed.add_field(name="Bothony", value="a Python bot runned by Anthonyjrvill", inline=False)
     embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/738310483920027679/bb972886d6053530acb1c534763a2baa.webp?size=512")  
     embed.add_field(name="Running in: ", value="Termux (Android 9)", inline=False)
     embed.add_field(name="Coded in: ", value="Code-Server", inline=False)
     embed.add_field(name="Recent Update: ", value="INSERT UPDATED DATE HERE", inline=False)

     await ctx.send(embed=embed)
 
#@client.command(aliases=["nuke", "dnuke"], name="dailynuke")
#@has_permissions(administrator=True)
#@has_permissions(manage_messages=True)
#async def _dailynuke(ctx, amount=99):
            #await ctx.send("NOW PREPARING NUKE...")
            #await asyncio.sleep(5)
            #await ctx.send("PREPARE SUCCESS!")
            #await asyncio.sleep(3)
            #await ctx.send("Launch in T minus 10")
            #await asyncio.sleep(1)
            #await ctx.send("9")
            #await asyncio.sleep(1)
            #await ctx.send("8")
            #await asyncio.sleep(1)
            #await ctx.send("7")
            #await asyncio.sleep(1)
            #await ctx.send("6")
            #await asyncio.sleep(1)
            #await ctx.send("5")
            #await asyncio.sleep(1)
            #await ctx.send("4")
            #await asyncio.sleep(1)
            #await ctx.send("3")
            #await asyncio.sleep(1)
            #await ctx.send("2")
            #await asyncio.sleep(1)
            #await ctx.send("1")
            #await asyncio.sleep(1)
            #await ctx.send("Time to start anew")
            #await asyncio.sleep(2)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)
            #await asyncio.sleep(1.7)
            #await ctx.channel.purge(limit=amount)

@client.command(aliases=["nuke", "dnuke"], name="dailynuke")
@commands.cooldown(1, 30, commands.BucketType.user)
async def _dailynuke(ctx):
           await ctx.send("NOW PREPARING NUKE...")
           await asyncio.sleep(5)
           await ctx.send("PREPARE SUCCESS!")
           await asyncio.sleep(3)
           await ctx.send("Launch in T minus 10")
           await asyncio.sleep(1)
           await ctx.send("9")
           await asyncio.sleep(1)
           await ctx.send("8")
           await asyncio.sleep(1)
           await ctx.send("7")
           await asyncio.sleep(1)
           await ctx.send("6")
           await asyncio.sleep(1)
           await ctx.send("5")
           await asyncio.sleep(1)
           await ctx.send("4")
           await asyncio.sleep(1)
           await ctx.send("Wait... Didn't we make an agreement with NTS to not nuke about a thousand years ago?")

@_dailynuke.error
async def dailynuke_error(error, ctx):    
       if isinstance(error, MissingPermissions):
           text = "{} You're not allowed to do that, lao".format(ctx.message.author)
           await ctx.send(text)      

for filename in os.listdir('./cogs'):
     if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ENTER TOKEN HERE')