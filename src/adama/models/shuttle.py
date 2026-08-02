from dataclasses import dataclass, field

from adama.utils.stubs import new_id


@dataclass
class Shuttle:
	id: str = field(default_factory=new_id)
	resources: dict[str, int] = field(default_factory=dict)

	intercepted: bool = False
