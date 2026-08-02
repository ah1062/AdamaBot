import sqlite3
from pathlib import Path

from adama.config import config
from adama.constants import _DATABASE_SCHEMA_LOCATION

_conn = None
DEBUG_OVERWRITE = True

def get_connection() -> sqlite3.Connection:
	db_path = Path(config.database.DB_PATH)

	global _conn
	if _conn is not None: 
		return _conn

	if DEBUG_OVERWRITE:
		db_path.unlink(missing_ok=True)

	_conn = sqlite3.connect(config.database.DB_PATH)
	with open(_DATABASE_SCHEMA_LOCATION) as f:
		schema = f.read()
		_conn.executescript(schema)

	return _conn
