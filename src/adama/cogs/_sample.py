import logging

from discord.ext import commands

logger = logging.getLogger()


class SampleCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


async def setup(bot):
	cog = SampleCommands(bot)
	await bot.add_cog(cog)
