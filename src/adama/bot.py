import logging

import discord
from discord.ext import commands

from adama.constants import _BOT_EXTENSION_DIRECTORY, _BOT_EXTENSION_MODULE
from adama.container import Container

logger = logging.getLogger()


class AdamaBot(commands.Bot):
	def __init__(self, command_prefix, intents=discord.Intents.default(), container=Container()):
		super().__init__(command_prefix=command_prefix, intents=intents)

		self.epoch = discord.utils.utcnow()
		self.container = container

	async def setup_hook(self):
		self.before_invoke(self.before_command)
		self.before_invoke(self.after_command)

		for ext in self.get_all_extensions():
			await self.load_extension(ext)

	async def on_ready(self):
		logger.info(f"Logged in as: {self.user}")

	async def close(self):
		logger.info("Closing down the bot...")

	async def before_command(self, ctx: commands.Context):
		assert ctx.command is not None

		try:
			await ctx.message.add_reaction("👍")
		except discord.HTTPException:
			pass

		if ctx.command:
			cmd_log = f"{ctx.author.name} invoked {ctx.command.name}"
			logger.info(cmd_log)

	async def after_command(self, ctx: commands.Context):
		assert ctx.command is not None
		now = discord.utils.utcnow()

		if ctx.command:
			cmd_log = f"{ctx.command.name} took {now - ctx.message.created_at}s"
			logger.info(cmd_log)

	async def on_command_error(self, ctx: commands.Context, exc):
		if isinstance(exc, commands.CommandNotFound):
			return

		assert ctx.guild is not None
		assert ctx.command is not None
		assert self.user is not None

		try:
			await ctx.message.remove_reaction("👍", self.user)
			await ctx.message.add_reaction("❌")
		except discord.HTTPException:
			pass

	@staticmethod
	def get_all_extensions():
		"""Gets all cog extensions."""
		for file in _BOT_EXTENSION_DIRECTORY.glob("*"):
			# ignore non py files
			# ignore private files e.g. '_private.py'
			if not file.suffix == ".py" or file.name.startswith("_"):
				continue

			yield f"{_BOT_EXTENSION_MODULE}.{file.name[:-3]}"

	# add logging to base extension functions
	async def load_extension(self, name: str, *, package: str | None = None):
		"""Loads a cog extension."""
		try:
			start = discord.utils.utcnow()
			await super().load_extension(f"{name}", package=package)
			end = discord.utils.utcnow()
			logger.info(
				"Successfully loaded Cog: %s in %s",
				name,
				end - start,
			)
		except commands.ExtensionError as e:
			logger.info("Failed to load Cog %s", name)
			raise e

	async def unload_extension(self, name: str, *, package: str | None = None) -> None:
		"""Unloads a cog extension."""
		try:
			start = discord.utils.utcnow()
			await super().unload_extension(f"{name}", package=package)
			end = discord.utils.utcnow()
			logger.info(
				"Successfully unloaded Cog: %s in %s",
				name,
				end - start,
			)
		except commands.ExtensionError as e:
			logger.info("Failed to unload Cog %s", name)
			raise e

	async def reload_extension(self, name: str, *, package: str | None = None) -> None:
		"""Reloads a cog extension. Will roll back to the previous version if it fails to load."""
		try:
			start = discord.utils.utcnow()
			await super().reload_extension(f"{name}", package=package)
			end = discord.utils.utcnow()
			logger.info(
				"Successfully reloaded Cog: %s in %s",
				name,
				end - start,
			)
		except commands.ExtensionError as e:
			logger.info("Failed to reload Cog %s", name)
			raise e
