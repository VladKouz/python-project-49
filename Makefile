install:
	uv sync

build:
	uv build

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

reinstall:
	uv tool install --force dist/*.whl

uninstall:
	uv tool uninstall dist/*.whl