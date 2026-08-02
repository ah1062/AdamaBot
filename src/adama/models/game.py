from dataclasses import dataclass, field

from adama.models.galaxy import Galaxy
from adama.utils.stubs import new_id

@dataclass
class Game:
	id: str = field(default_factory=new_id)
	name: str = ""

	server_id: int = 0
	galaxy: Galaxy | None = None
		
	active: bool = True
