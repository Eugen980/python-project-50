install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8

test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml
	poetry run coverage report
