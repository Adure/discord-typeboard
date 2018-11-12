import discord, time, re
from discord.ext import commands
from auth import bot_token

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_typing(channel, user, time):
    # Will have to make a register so that people who are being watched for a message cant trigger this.
    # We can set their watched status to True here (1/3)
    startTime = time.time() # Using time module for length so that theyre in the same format.
    print(f'{user.display_name}#{user.discriminator} is typing in #{channel.name} - {channel.guild.name} at {time}')

    def check(m):
        return m.channel == channel and m.author == user
    try:
        msg = await client.wait_for("message", check=check, timeout=20.0)
    except asyncio.TimeoutError:
        print("{0.display_name}#{0.discriminator} didn\'t send a message".format(user))
        # Set their watched status to false when we know they didnt send a message (3/3)
        return

    endTime = time.time()
    durationTime, formattedMsg = (endTime - startTime), msg.content

    # Using reg to remove emotes so that they dont inflate the word count
    if bool(re.search("<:(.*):(.*)>", msg.content)) or bool(re.search("<a:(.*):(.*)>", msg.content)):
        formattedMsg = re.sub("<:(.*):(.*)>", "",formattedMsg)
        formattedMsg = re.sub("<a:(.*):(.*)>", "",formattedMsg)

    print("{0.author.display_name}#{0.author.discriminator} took {1} seconds to send the message \"{2}\"".format(msg, durationTime, formattedMsg))

    #Use two JSON formatted files, one to store the final average for each user and one to store all their previous scores
    #the one that stores their scores would be used to make the average, and the final average file would be for ease of reading their latest
    #If we make the leaderboard thing dynamic, we can add new statboards whenever we want

@bot.event
async def on_message(message):
    # If we make a register for people who are typing, whenever we get a message here we can set their status to not being watched. (2/3)
    pass

@bot.event
async def on_ready():
    print(f'Ready - Logged in as {bot.user.name}#{bot.user.discriminator}')

bot.run(bot_token)