from dataclasses import dataclass, field

from adama.repositories import GalaxyRepository
from adama.services import GalaxyService

@dataclass
class Repositories():
	galaxy: GalaxyRepository = field(default_factory=GalaxyRepository)

@dataclass
class Services():
	galaxy: GalaxyService

@dataclass
class Container():
	repos: Repositories = field(default_factory=Repositories)
	services: Services = field(init=False)

	def __post_init__(self):
		self.services = Services(
			galaxy=GalaxyService(self.repos.galaxy)
		)
