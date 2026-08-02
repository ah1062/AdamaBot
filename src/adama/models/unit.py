from dataclasses import dataclass


@dataclass
class Unit:
	id: int
	name: str

	damaged: bool = False
	exhausted: bool = False
