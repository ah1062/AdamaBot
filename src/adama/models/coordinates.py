from dataclasses import dataclass


@dataclass
class CoordState:
	locked_down: bool = False
