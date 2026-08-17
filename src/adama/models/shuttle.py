from dataclasses import dataclass, field

from adama.models.resources import ResourcesContainer

@dataclass
class Shuttle:
	id: str
	name: str

	intercepted: bool = False
	clearance: bool = False
	resources: ResourcesContainer = field(default_factory=ResourcesContainer)
