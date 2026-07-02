install:
	uv sync

build:
	uv build

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games

reinstall:
	uv tool install --force dist/*.whl

uninstall:
	uv tool uninstall --all