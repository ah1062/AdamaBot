from dataclasses import dataclass

@dataclass
class ResourcesContainer:
	food: int = 0
	fuel: int = 0
	materials: int = 0
	ore: int = 0
	water: int = 0
