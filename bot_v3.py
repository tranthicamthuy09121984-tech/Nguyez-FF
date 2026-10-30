# -*- coding: utf-8 -*-
import os
import discord
from discord.ext import commands
import random
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Meo meo maoooo!! Bot UP - nguyez-ff.onrender.com".encode('utf-8'))

def start_web():
    HTTPServer(('0.0.0.0', PORT), Handler).serve_forever()

threading.Thread(target=start_web, daemon=True).start()

intents = discord.Intents.default()
intents.message_content = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    async def setup_hook(self):
        await self.tree.sync()
        print("Đã sync lệnh slash!")

bot = Bot()

# LƯU SÚNG CỦA TỪNG NGƯỜI - ĐIỀU 1
sung_hien_tai = {}

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user} - Sẵn sàng!")

@bot.tree.command(name="quay", description="Quay súng VIP")
async def quay(interaction: discord.Interaction):
    danh_sach_sung = ["MP40 - Tia Chớp Tử Thần", "M1014 - Huyết Hỏa", "M1887 - Vũ Trụ Quỷ Diệt", "AVM - Hắc Ảnh Tinh Hà", "AUG - Hỏa Phượng Thần Tiễn", "M60 - Sát Thần Săn Mộng", "P90 - Hoàng Kim Bất Diệt", "G18 - Chinh Phục", "Parafal - Cuồng Long", "Chim Gõ Kiến - Mãnh Hổ Oai Hùng", "Groza - Địa Chắn Sắc Màu", "Thomson - Hắc Thạch Long", "AN94 - Tiếng Hú Ác Quỷ", "Tay - Long Trảo Quyền", "M4A1 - Hỏa Ngục", "MP5 - Thiên Thần Bạch Kim", "Famas - Dạ Xoa", "UMP - Phong cách", "XM8 - Lôi Thần", "M1014 - Long Tộc", "MP40 - Mãng Xà", "Scar - Cá Mập Đen", "AK47 - Rồng Xanh"]
    qua = random.choice(danh_sach_sung)
    sung_hien_tai[interaction.user.id] = qua
    await interaction.response.send_message(f"{interaction.user.mention} quay trúng: **{qua}**!\nĐã trang bị! Giờ dùng /ban để bắn!")

@bot.tree.command(name="ban", description="Bắn súng FF - bắn cây vừa quay")
async def ban_game(interaction: discord.Interaction):
    vu_khi = sung_hien_tai.get(interaction.user.id)
    if not vu_khi:
        await interaction.response.send_message(f"{interaction.user.mention} chưa có súng! Dùng /quay trước đã!")
        return
    await interaction.response.send_message(f"{interaction.user.mention} cầm **{vu_khi}** HEADSHOT! 💥")

@bot.tree.command(name="ping", description="Check ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong {round(bot.latency*1000)}ms")

bot.run(os.getenv("DISCORD_TOKEN"))