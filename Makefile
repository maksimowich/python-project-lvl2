reinstall-local:
	poetry run python3 -m pip install --force-reinstall dist/*.whl

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

make lint:
	poetry run flake8 gendiff

make install:
	poetry install
