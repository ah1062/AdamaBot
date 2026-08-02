from adama.models import Game
from adama.repositories.base import Repository

class GameRepository(Repository[Game]):
	def __init__(self) -> None:
		super().__init__()

	def save(self, entity: Game) -> bool:
		cursor = self.conn.cursor()
		return True

	def load(self, id: str) -> Game | None:
		cursor = self.conn.cursor()
		cursor.execute(
			"SELECT id, server_id, galaxy_id FROM games WHERE id = ?",
			(id,)
		)
	
		row = cursor.fetchone() 
		if row is None:
			return None

		# TODO: Load Game and Galaxies

	def delete(self, entity: Game):
		cursor = self.conn.cursor()
		cursor.execute(
			"""
			UPDATE games 
			SET active=0,archived_at=CURRENT_TIMESTAMP,galaxy_id=NULL
			WHERE id=?
			""",
			(entity.id,)
		)

	def purge(self, entity: Game):
		cursor = self.conn.cursor()
		cursor.execute("DELETE FROM games WHERE id = ?", (entity.id,))

	def all(self) -> list[Game]:
		return []
