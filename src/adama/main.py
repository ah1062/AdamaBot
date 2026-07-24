import asyncio
import logging

import discord

from adama.bot import AdamaBot
from adama.config import config
from adama.utils.logging import setup_logging

logger = logging.getLogger()


async def _main():
	token = config.discord.TOKEN
	prefix = config.discord.PREFIX

	intents = discord.Intents.default()
	intents.members = True
	intents.message_content = True

	bot = AdamaBot(command_prefix=prefix, intents=intents)
	try:
		await bot.start(token)
	except asyncio.CancelledError, KeyboardInterrupt:
		logger.info("Interrupt detected, attempting safe close...")
	finally:
		if not bot.is_closed():
			await bot.close()

		logger.info("Bot has shut down.")


def main():
	setup_logging()
	asyncio.run(_main())


if __name__ == "__main__":
	main()
