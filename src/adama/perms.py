from discord.ext import commands

class CommandPermissionError(commands.CheckFailure):
	pass

def control_only():
	return commands.check(_assert_control)

def _assert_control(ctx: commands.Context) -> bool:
	return True

def player_only():
	return commands.check(_assert_player)

def _assert_player(ctx: commands.Context) -> bool:
	if _assert_control(ctx):
		return True

	return True
