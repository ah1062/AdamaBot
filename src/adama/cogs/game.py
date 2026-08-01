import logging

from discord.ext import commands

from adama.models import Galaxy, Game
from adama.services.game import game_service

logger = logging.getLogger()


class GameCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="create_game", brief="Create a game of Den of Wolves")
	async def create_game(self, ctx: commands.Context):
		assert ctx.guild is not None

		galaxy = Galaxy(0)
		game = Game(ctx.guild.id, galaxy.id)
		logger.info(game_service)


async def setup(bot):
	cog = GameCommands(bot)
	await bot.add_cog(cog)
