from dataclasses import dataclass, field

from adama.repositories import GameRepository
from adama.services import GameService

@dataclass
class Repositories():
	game: GameRepository = field(default_factory=GameRepository)

@dataclass
class Services():
	game: GameService

@dataclass
class Container():
	repos: Repositories = field(default_factory=Repositories)
	services: Services = field(init=False)

	def __post_init__(self):
		self.services = Services(
			game=GameService(self.repos.game)
		)
