import logging

from discord.ext import commands

logger = logging.getLogger()


class GeneralCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="ping", brief="Say hello to the bot!")
	async def ping(self, ctx: commands.Context):
		await ctx.send(f"Hello, {ctx.author.mention}!")


async def setup(bot):
	cog = GeneralCommands(bot)
	await bot.add_cog(cog)
