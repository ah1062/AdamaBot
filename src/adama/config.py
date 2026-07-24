import tomllib
from dataclasses import dataclass
from pathlib import Path

from adama.constants import CONFIG_PATH


@dataclass
class GlobalConfig:
	discord: DiscordConfig


@dataclass
class DiscordConfig:
	TOKEN: str
	PREFIX: str = "."


def load_config(file: Path):
	with open(file, "rb") as f:
		data = tomllib.load(f)

	config = GlobalConfig(discord=DiscordConfig(**data["discord"]))
	return config


config = load_config(CONFIG_PATH)
