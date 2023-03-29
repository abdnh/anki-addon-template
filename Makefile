.PHONY: all zip ankiweb fix mypy pylint clean

all: zip ankiweb

zip:
	python -m ankibuild --type package --qt all --exclude user_files/**/

ankiweb:
	python -m ankibuild --type ankiweb --qt all --exclude user_files/**/

fix:
	python -m black src tests --exclude="forms|vendor"
	python -m isort src tests

mypy:
	python -m mypy src tests

pylint:
	python -m pylint src tests

clean:
	rm -rf build/
