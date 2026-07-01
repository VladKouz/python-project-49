install:
	uv sync

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

reinstall:
	uv tool install --force dist/hexlet_code-0.1.0.tar.gz