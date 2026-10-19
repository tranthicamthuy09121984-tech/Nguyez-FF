import os, random, discord
from discord.ext import commands
import google.generativeai as genai
from keep_alive import keep_alive

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.5-flash")
user_chats = {}

intents = discord.Intents.default()
intents.message_content = True

class ContinuousChatBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    async def setup_hook(self):
        await self.tree.sync()

bot = ContinuousChatBot()

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

@bot.tree.command(name="ping", description="Check ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong {round(bot.latency*1000)}ms")

# ===== 5 GAME NGUYEZ FF STYLE =====
@bot.tree.command(name="ban", description="🔫 Nguyez FF ban headshot")
async def ban_game(interaction: discord.Interaction):
    ti_le = random.choice(["💥 HEADSHOT!", "💥 HEADSHOT x