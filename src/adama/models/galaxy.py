from dataclasses import field

from adama.models.player import Player
from adama.models.ship import Ship
from adama.models.shuttle import Shuttle


class Galaxy:
	id: str

	players: dict[str, Player] = field(default_factory=dict)
	ships: dict[str, Ship] = field(default_factory=dict)
	shuttles: dict[str, Shuttle] = field(default_factory=dict)

	prev: str | None = None
