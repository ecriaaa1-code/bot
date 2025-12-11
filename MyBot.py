import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is online!")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    await msg.channel.send("Interesting message!")
    await bot.process_commands(msg)

bot.run(TOKEN)

