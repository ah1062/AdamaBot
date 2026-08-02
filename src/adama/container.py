from dataclasses import dataclass, field

from adama.repositories.game import GameRepository
from adama.services.game import GameService

@dataclass
class Repositories():
	game: GameRepository = field(default_factory=GameRepository)

@dataclass
class Services():
	game: GameService = field(default=GameService(GameRepository()))

@dataclass
class Container():
	repos: Repositories = field(default_factory=Repositories)
	services: Services = field(default_factory=Services)
