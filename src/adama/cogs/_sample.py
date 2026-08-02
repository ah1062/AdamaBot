import logging

from discord.ext import commands

from adama.bot import AdamaBot

logger = logging.getLogger()


class SampleCommands(commands.Cog):
	def __init__(self, bot: AdamaBot):
		self.bot = bot
		self.container = bot.container


async def setup(bot: AdamaBot):
	cog = SampleCommands(bot)
	await bot.add_cog(cog)
