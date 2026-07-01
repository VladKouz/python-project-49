install:
	uv sync

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games