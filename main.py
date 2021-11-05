import aiohttp, discord
from discord.ext import commands

bot = commands.Bot(command_prefix="s.", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print('Bot is online')

@bot.command()
async def smile(ctx, user: discord.User = None):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.siesta.red:4444/smile") as response:
            image = await response.text()
    if user:
        embed = discord.Embed(title=f'{ctx.author.name} smiled {user.name}')
    else:
        embed = discord.Embed(title=f'{ctx.author.name} smiled someone')
    embed.set_image(url=image)
    await ctx.send(embed=embed)

bot.run('Bot-Token')
