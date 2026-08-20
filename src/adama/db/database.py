import sqlite3

from adama.config import config
from adama.constants import DEBUG_MODE, _DATABASE_SCHEMA_LOCATION

_conn = None


def get_connection(*, debug: bool = False) -> sqlite3.Connection:
	global _conn
	if _conn is not None: 
		return _conn
	
	if debug:
		_conn = sqlite3.connect(":memory:")
	else:
		_conn = sqlite3.connect(config.database.DB_PATH)

	with open(_DATABASE_SCHEMA_LOCATION) as f:
		schema = f.read()
		_conn.executescript(schema)

	return _conn

_conn = get_connection(debug=DEBUG_MODE)
