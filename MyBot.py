import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import asyncio
from collections import deque

from keep_alive import keep_alive  # NEW

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()  # NEW

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is online!")


@bot.event
async def on_message(msg):
    # ignore the bot's own messages
    if msg.author == bot.user:
        return

    # simple test reply
    await msg.channel.send("Interesting message!")

    # make sure commands still work
    await bot.process_commands(msg)


bot.run(TOKEN)
