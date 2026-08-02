from pathlib import Path

from adama.models import Galaxy


def create_galaxy(setup_script: str | Path) -> Galaxy:
	if isinstance(setup_script, str):
		setup_script = Path(setup_script)

	if not setup_script.exists():
		raise FileNotFoundError(f"Can't find setup script at: '{setup_script}'")
	if setup_script.suffix != ".dow.json":
		raise ValueError(f"Can't create a galaxy from file type '{setup_script.suffix}'")

	# TODO: Create Galaxy from a bootstrap datastructure

	return Galaxy()
