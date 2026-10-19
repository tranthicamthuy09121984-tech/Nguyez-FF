# -*- coding: utf-8 -*-
import os
import discord
from discord.ext import commands
import google.generativeai as genai
import random

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
user_chats = {}

intents = discord.Intents.default()
intents.message_content = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    async def setup_hook(self):
        await self.tree.sync()
        print("Đã sync lệnh!")

bot = Bot()

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

@bot.tree.command(name="ban", description="Bắn súng FF VIP có dấu")
async def ban_game(interaction: discord.Interaction, sung: str = None):
    vu_khi = sung if sung else random.choice(["MP40 Mãng Xà", "M1887 Vũ Trụ", "M1014", "AK Rồng Lửa"])
    hieu_ung = random.choice(["HEADSHOT", "HEADSHOT x2", "1 viên 1 mạng", "1vs4 Nguyez Style", "FULL ĐỒ"])
    await interaction.response.send_message(f"{interaction.user.mention} cầm {vu_khi} bắn {hieu_ung}!")

@bot.tree.command(name="quay", description="Vòng quay súng VIP FF")
async def quay(interaction: discord.Interaction):
    qua = random.choice([
        "MP40 Mãng Xà LVL 7",
        "M1887 Vũ Trụ LVL 7", 
        "M1014 Hủy Diệt",
        "UMP Ngày Đen",
        "9999 Kim Cương"
    ])
    await interaction.response.send_message(f"{interaction.user.mention} quay trúng: {qua}!")

@bot.tree.command(name="sosanh", description="So sánh 2 khẩu súng")
async def sosanh(interaction: discord.Interaction):
    msg = (
        "**MP40 Mãng Xà**: Tốc độ bắn nhanh, sát thủ tầm gần\n"
        "**M1887 Vũ Trụ**: 1 viên 1 mạng, bá chủ tầm gần\n"
        f"=> {interaction.user.mention} thích khẩu nào hơn?"
    )
    await interaction.response.send_message(msg)

@bot.tree.command(name="taixiu", description="Tài xỉu kim cương")
async def taixiu(interaction: discord.Interaction, chon: str):
    x1 = random.randint(1,6)
    x2 = random.randint(1,6)
    x3 = random.randint(1,6)
    tong = x1+x2+x3
    kq = "tài" if tong >= 11 else "xỉu"
    await interaction.response.send_message(f"{x1}-{x2}-{x3}={tong} ({kq}) - Bạn chọn {chon}")

@bot.tree.command(name="ping", description="Check ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong {round(bot.latency*1000)}ms")

bot.run(os.getenv("DISCORD_TOKEN"))
