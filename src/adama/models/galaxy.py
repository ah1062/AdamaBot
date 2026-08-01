from dataclasses import dataclass

@dataclass
class Galaxy:
	id: int

	next: int | None = None
