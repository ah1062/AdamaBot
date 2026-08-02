import logging

from adama.models import Game
from adama.services.base import BaseService

logger = logging.getLogger(__name__)

class GameService(BaseService):
	def __init__(self, repo) -> None:
		self.repo = repo
		self.games: dict[str, Game] = {g.id: g for g in self.repo.all()}

	def create_game(self, server_id: int, name: str):
		game = Game(server_id=server_id, name=name)
		self.repo.save(game)

		return game

	def load_game(self, server_id: int):
		raise NotImplementedError

	def delete_game(self, game_id: str):
		if game_id not in self.games:
			return False

		game = self.games[game_id]
		self.repo.delete(game)

		del self.games[game_id]

	def purge_game(self, game_id: str):
		if game_id not in self.games:
			return False

		game: Game = self.games[game_id]
		self.repo.purge(game)

		if game.galaxy is not None:
			curr = game.galaxy
			while curr.prev is not None:
				# TODO: create galaxy_repo

				#galaxy_repo.purge(curr)
				curr = curr.prev
