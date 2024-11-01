import discord
from discord.ext import commands
from logic import id

intents = discord.Intents.default()
intents.message_content = True

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
async def check(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            filename = i.filename
            url = i.url
            await i.save(f'./images/{i.filename}')
            name,percent = (id(models='keras_model_bird.h5', label='labels_bird.txt', img=(f'./images/{i.filename}')))
            if name.strip() and percent>0.8:
                await ctx.send('''Это голубь
                                Зерновые смеси. Норма зерна на одну птицу составляет 10% от живой массы голубя (от 30 до 50 г корма на одну голову). Примерный состав зерновой смеси: пшеница — 25–30%, просо — 20–25%, ячмень — 15–20%, кукуруза — 35–40%, горох — 10–15%, подсолнечник — 5–6%. 2
                                Зелёный корм. Пророщенное зерно, мелко нарезанная зелень или небольшое количество капусты, салата, измельчённая трава, тёртая морковь. 
                                Фрукты. Практически все виды голубей едят фрукты, а для некоторых они составляют основу рациона. Чаще всего используются сладкие яблоки, персики, вишня, абрикосы и виноград. ''')
    else:
        await ctx.send('No image')

bot.run("")