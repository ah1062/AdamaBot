import tomllib
from dataclasses import dataclass
from pathlib import Path

from adama.constants import CONFIG_PATH


@dataclass
class DiscordConfig:
	TOKEN: str
	PREFIX: str = "."

@dataclass
class DatabaseConfig:
	DB_PATH: str = "src/adama/db/adama.sqlite"

@dataclass
class GlobalConfig:
	discord: DiscordConfig
	database: DatabaseConfig

def load_config(file: Path):
	with open(file, "rb") as f:
		data = tomllib.load(f)

	config = GlobalConfig(
		discord=DiscordConfig(**data.get("discord", {})),
		database=DatabaseConfig(**data.get("database", {}))
	)

	return config


config = load_config(CONFIG_PATH)
