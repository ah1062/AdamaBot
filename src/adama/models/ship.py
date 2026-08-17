from dataclasses import dataclass, field

from adama.models.resources import ResourcesContainer

@dataclass
class ShipCoordinates:
	coordinates: int
	next_coordinates: int
	sabotage_coordinates: int 

@dataclass
class ShipMorale:
	level: int
	temp_roll_modifier: int
	perm_roll_modifier: int
	fleet_temp_roll_modifier: int
	fleet_perm_roll_modifier: int

@dataclass
class ShipRationLevel:
	food: int
	water: int

@dataclass
class ShipRations:
	luxurious: ShipRationLevel
	increased: ShipRationLevel
	normal: ShipRationLevel
	low: ShipRationLevel
	minimum: ShipRationLevel
	critical: ShipRationLevel

@dataclass
class ShipFuelConsumption:
	short: int
	medium: int
	long: int

@dataclass
class Ship:
	id: str
	name: str

	coordinates: ShipCoordinates
	morale: ShipMorale
	rations: ShipRations
	resources: ResourcesContainer
	fuel_consuption: ShipFuelConsumption

	players: set[str] = field(default_factory=set)
	stations: set[str] = field(default_factory=set)
