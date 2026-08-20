.PHONY: format lint test deps docs clean clean-docs clean-win clean-docs-win

format:
	ruff format .
	ruff check . --fix

lint:
	ruff check .
	mypy src

test:
	pytest

deps:
	pydeps src/adama -o dependencies.png -T png --noshow --rankdir LR --only "adama" --exclude "adama.utils*" "adama.constants" "*.base"

docs:
	sphinx-apidoc -f -o docs/source src/adama/
	sphinx-build -b html docs/source docs/build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".coverage" -delete
	rm -rf build dist

clean-docs:
	rm -rf docs/build
	rm -f docs/source/modules.rst
	rm -f docs/source/*.rst

clean-win:
	powershell -Command "Get-ChildItem -Recurse -Include __pycache__ | Remove-Item -Recurse -Force"
	powershell -Command "if (Test-Path '.mypy_cache') { Remove-Item '.mypy_cache' -Recurse -Force }"
	powershell -Command "if (Test-Path '.pytest_cache') { Remove-Item '.pytest_cache' -Recurse -Force }"
	powershell -Command "if (Test-Path '.ruff_cache') { Remove-Item '.ruff_cache' -Recurse -Force }"
	powershell -Command "Get-ChildItem -Recurse -Include *.egg-info | Remove-Item -Recurse -Force"
	powershell -Command "Remove-Item *.pyc -Recurse -Force"
	powershell -Command "Remove-Item *.coverage -Recurse -Force"

clean-docs-win:
	echo "Not Implemented"
