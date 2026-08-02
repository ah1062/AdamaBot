from pathlib import Path

CONFIG_PATH = Path("config.toml")
if not CONFIG_PATH.exists():
	raise RuntimeError("Could not find 'config.toml' file")

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

SRC_DIR = Path("src")
PACKAGE_DIR = SRC_DIR / "adama"

_BOT_EXTENSION_DIRECTORY = PACKAGE_DIR / "cogs"
_BOT_EXTENSION_MODULE = "adama.cogs"

_DATABASE_SCHEMA_LOCATION = PACKAGE_DIR / "db" / "schema.sql"
