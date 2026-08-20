from pathlib import Path

DEBUG_MODE = True

CONFIG_PATH = Path("config.toml")
if not CONFIG_PATH.exists():
	raise RuntimeError("Could not find 'config.toml' file")

SRC_DIR = Path("src")
PACKAGE_DIR = SRC_DIR / "adama"

_BOT_EXTENSION_DIRECTORY = PACKAGE_DIR / "cogs"
_BOT_EXTENSION_MODULE = "adama.cogs"

_DATABASE_SCHEMA_LOCATION = PACKAGE_DIR / "db" / "schema.sql"
