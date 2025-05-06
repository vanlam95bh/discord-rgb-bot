import discord
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

ROLE_ID = int(os.getenv("ROLE_ID"))
GUILD_ID = int(os.getenv("GUILD_ID"))
DELAY = 2

@bot.event
async def on_ready():
    print(f"Bot đã online: {bot.user}")
    bot.loop.create_task(rainbow_role())

async def rainbow_role():
    await bot.wait_until_ready()
    guild = bot.get_guild(GUILD_ID)
    role = guild.get_role(ROLE_ID)
    r, g, b = 255, 0, 0

    while True:
        color = discord.Color.from_rgb(r, g, b)
        await role.edit(color=color)
        r = (r + 25) % 256
        g = (g + 40) % 256
        b = (b + 60) % 256
        await asyncio.sleep(DELAY)

bot.run(os.getenv("DISCORD_TOKEN"))
