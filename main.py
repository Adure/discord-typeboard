import discord
from discord.ext import commands
from auth import bot_token
import datetime

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_typing(channel, user, time):
    print(f'{user.name}#{user.discriminator} is typing in #{channel.name} - {channel.guild.name} at {time}')

@bot.event
async def on_message(message):
    pass

@bot.event
async def on_ready():
    print(f'Ready - Logged in as {bot.user.name}#{bot.user.discriminator}')

bot.run(bot_token)