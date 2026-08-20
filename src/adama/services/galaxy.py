from adama.models.galaxy import Galaxy
from adama.repositories.base import BaseRepository
from adama.services.base import BaseService


class GalaxyService(BaseService):
	def __init__(self, repo: BaseRepository[Galaxy]) -> None:
		self.repo = repo
