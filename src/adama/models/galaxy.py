from __future__ import annotations
from dataclasses import dataclass, field

from adama.models.coordinates import CoordState
from adama.models.ship import Ship
from adama.utils.stubs import new_id

@dataclass
class Galaxy:
	id: str = field(default_factory=new_id)
	
	coords: dict[str, CoordState] = field(default_factory=dict)
	ships: dict[str, Ship] = field(default_factory=dict)

	prev: Galaxy | None = None
	next: Galaxy | None = None
