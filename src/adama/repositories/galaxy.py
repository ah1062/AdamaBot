from adama.models.galaxy import Galaxy
from adama.repositories.base import BaseRepository


class GalaxyRepository(BaseRepository[Galaxy]):
	def save(self, entity: Galaxy) -> bool:
		return super().save(entity)

	def load(self, id: str) -> Galaxy | None:
		return super().load(id)
