from adama.models import Game
from adama.repositories.base import Repository

class GameRepository(Repository[Game]):
	def __init__(self) -> None:
		super().__init__()

game_repo = GameRepository()
