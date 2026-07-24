import datetime
import logging

from adama.constants import LOGS_DIR

LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = ""
LOGGING_DATEFMT = "%Y/%M/%S %H:%m:%s"


def setup_logging():
	now = datetime.datetime.now(datetime.UTC).replace(microsecond=0)
	filename = LOGS_DIR / f"adama_{now}.log"

	logging.basicConfig(
		filename=filename,
		level=LOGGING_LEVEL,
		format=LOGGING_FORMAT,
		datefmt=LOGGING_DATEFMT,
	)

	root = logging.getLogger()
	root.addHandler(logging.StreamHandler())
