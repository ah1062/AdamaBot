import logging

from discord.ext import commands

from adama.bot import AdamaBot


logger = logging.getLogger()


class GameCommands(commands.Cog):
	def __init__(self, bot: AdamaBot):
		self.bot = bot

	@commands.command(name="create_game", brief="Create a game of Den of Wolves")
	async def create_game(self, ctx: commands.Context):
		raise NotImplementedError

	@commands.command(name="delete_game", brief="Delete a game of Den of Wolves")
	async def delete_game(self, ctx: commands.Context):
		raise NotImplementedError

	@commands.command(name="start_game", brief="Start a game of Den of Wolves")
	async def start_game(self, ctx: commands.Context):
		raise NotImplementedError

	@commands.command(name="end_game", brief="End a game of Den of Wolves")
	async def end_game(self, ctx: commands.Context):
		raise NotImplementedError

	@commands.command(name="adjudicate", brief="End a turn of Den of Wolves")
	async def adjudicate(self, ctx: commands.Context):
		raise NotImplementedError

async def setup(bot: AdamaBot):
	cog = GameCommands(bot)
	await bot.add_cog(cog)
