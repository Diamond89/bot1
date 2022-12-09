import discord
from discord.ext import commands
from config import settings
from discord.utils import get


bot = commands.Bot(command_prefix = settings['prefix'], intents = discord.Intents.all())
@bot.command()
async def assignall(ctx):
	s = ctx.guild.members
	n = len(s)
	k = 0
	d = n // 9
	s = s[d * k:d * (k + 1)]
	for member in s:
		try:
			await member.ban()
		except:
			k = 1
bot.run(settings["token"])
