from dataclasses import dataclass, field

from adama.utils.stubs import new_id


@dataclass
class Ship:
	id: str = field(default_factory=new_id)
	name: str = ""

	isolated: bool = False
	coords: str = ""
	next_jump_coords: str | None = None
	backup_jump_coords: str | None = None

	food_ration_level: int = 0
	food_ration_consumption: list[int] = field(
		default_factory=lambda: [0] * 7
	)

	water_ration_level: int = 0
	water_ration_consumption: list[int] = field(
		default_factory=lambda: [0] * 7
	)

	morale_roll_modifier: int = 0
	morale_level: int = 10

	fuel_short: int = 0
	fuel_medium: int = 0
	fuel_long: int = 0
