import discord, time
from discord.ext import commands
from auth import bot_token
import datetime

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_typing(channel, user, time):
    # Will have to make a register so that people who are being watched for a message cant trigger this.

    startTime = time.time() # Using time module for length so that theyre in the same format.
    print(f'{user.display_name}#{user.discriminator} is typing in #{channel.name} - {channel.guild.name} at {time}')

    def check(m):
        return m.channel == channel and m.author == user
    try:
        msg = await client.wait_for("message", check=check, timeout=20.0)
    except asyncio.TimeoutError:
        print("{0.display_name}#{0.discriminator} didn\'t send a message".format(user))
        return

    endTime = time.time()
    durationTime = endTime - startTime

    # Check for nitro with author.nitro, if its false we can iterate through guild.emoji to see if theyve used any emotes in their message
    # If they do have nitro, we'll have to use a regex to see if theyve sent an emote
    # if bool(re.search("<:(.*):(.*)>", msg.content)) or bool(re.search("<a:(.*):(.*)>", msg.content)):

    print("{0.author.display_name} took {1} seconds to send the message \"{0.content}\"".format(msg, durationTime))

@bot.event
async def on_message(message):
    pass

@bot.event
async def on_ready():
    print(f'Ready - Logged in as {bot.user.name}#{bot.user.discriminator}')

bot.run(bot_token)