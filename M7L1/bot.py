import discord
from discord.ext import commands
import os
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)  # Klasör yoksa oluştur

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def clear(ctx):
     if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = os.path.join(IMAGE_DIR,file_name)
            await attachment.save(file_path)
            await ctx.send(f"{file_name}görseliniz başarılı şekilde kaydedildi")
            try:
                class_name, skor = get_class(image=file_path)
                await ctx.send(f"Görsel sınıfı: {class_name}, tahmin skoru: {skor}")
                if class_name == "kopek":
                    await ctx.send("Bu bir köpek görseli! 🐶")
                elif class_name == "kedi":
                    await ctx.send("Bu bir kedi görseli! 🐱")
                else:
                    await ctx.send("Bu bir kuş görseli! 🐦")
            except Exception as e:
                await ctx.send(f"Görsel işleme sırasında bir hata oluştu: {e}")
     else:
        await ctx.send("Lütfen bir görsel ekleyin.")

bot.run("TOKEN")