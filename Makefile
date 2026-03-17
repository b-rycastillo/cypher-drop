format:
	black .

lint:
	ruff check .

test:
	pytest

check: format lint test