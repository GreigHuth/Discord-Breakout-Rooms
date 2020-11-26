import discord
import random
from config import *

intents = discord.Intents(members=True, voice_states=True, messages=True, guilds=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in')

@client.event
async def on_message(message):

    args = message.content.split()
    command = args[0]
    
    #default number of groups is 3
    try: 
        groups = int(args[1])
    except IndexError: 
        groups = 3
    
    if command.startswith('/breakout') and message.author.id == ME:

        #all members in same vc as me
        victims = message.author.voice.channel.members

        #list of all voice channels
        channels = message.guild.voice_channels

        #remove channels that arent in the specified category
        channels = [x for x in channels if x.category_id == CATEGORY]

        #random indexes corresponding to all_channels
        rooms = random.sample(range(0, len(channels) ), groups)

        i = 0
        for v in victims:
            index = i % groups
            print ("moving %s to %s" % (v, index))
            await v.edit(voice_channel=channels[rooms[index]])    
            i = i+1

client.run(TOKEN)
