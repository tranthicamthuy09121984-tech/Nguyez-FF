# -*- coding: utf-8 -*-
import os
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    async def setup_hook(self):
        await self.tree.sync()
        print("Da sync lenh slash!")

bot = Bot()

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user} - San sang MP40 Mang Xa!")

@bot.tree.command(name="ban", description="Ban sung FF")
async def ban_game(interaction: discord.Interaction):
    vu_khi = random.choice(["MP40 Mang Xa", "M1887 Vu Tru", "M1014 Huy Diet"])
    await interaction.response.send_message(f"{interaction.user.mention} cam {vu_khi} HEADSHOT!")

@bot.tree.command(name="quay", description="Quay sung VIP")
async def quay(interaction: discord.Interaction):
    qua = random.choice(["MP40 Mang Xa LVL 7", "M1887 Vu Tru LVL 7", "9999 Kim Cuong"])
    await interaction.response.send_message(f"{interaction.user.mention} quay trung: {qua}!")

@bot.tree.command(name="ping", description="Check ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong {round(bot.latency*1000)}ms")

bot.run(os.getenv("DISCORD_TOKEN"))