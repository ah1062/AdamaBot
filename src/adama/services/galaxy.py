import logging

from adama.models.galaxy import Galaxy
from adama.repositories.base import BaseRepository
from adama.services.base import BaseService

logger = logging.getLogger(__name__)

class GalaxyService(BaseService):
	def __init__(self, repo: BaseRepository[Galaxy]) -> None:
		self.repo = repo

	def close(self):
		logger.info("Closing GalaxyService!")
		self.repo.conn.close()
