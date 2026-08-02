import logging
import random

from discord.ext import commands

from adama.bot import AdamaBot

logger = logging.getLogger()


class GeneralCommands(commands.Cog):
	def __init__(self, bot: AdamaBot):
		self.bot = bot

	@commands.command(name="ping", brief="Say hello to the bot!")
	async def ping(self, ctx: commands.Context):
		await ctx.send(f"Hello, {ctx.author.mention}!")

	@commands.command(name="roll", brief="Roll a dice!")
	async def roll(self, ctx: commands.Context, dice: str = "6"):
		dice = dice.removeprefix("d")

		try:
			dice_int: int = int(dice)
			d_val = random.randint(1, dice_int)
			await ctx.send(f"You rolled a: {d_val}")
		except ValueError:
			await ctx.send(f"Failed to roll the dice '{dice}'")


async def setup(bot: AdamaBot):
	cog = GeneralCommands(bot)
	await bot.add_cog(cog)
