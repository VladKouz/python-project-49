install:
	uv sync

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl