.PHONY: all zip ankiweb vendor fix mypy pylint lint test sourcedist clean

all: zip ankiweb

UV_RUN = uv run --

zip:
	$(UV_RUN) python -m ankiscripts.build --type package --qt all --exclude user_files/**/*

ankiweb:
	$(UV_RUN) python -m ankiscripts.build --type ankiweb --qt all --exclude user_files/**/*

vendor:
	$(UV_RUN) python -m ankiscripts.vendor

fix:
	$(UV_RUN) pre-commit run -a black
	$(UV_RUN) pre-commit run -a isort
mypy:
	-$(UV_RUN) pre-commit run -a mypy

pylint:
	-$(UV_RUN) pre-commit run -a pylint

lint: mypy pylint

test:
	$(UV_RUN) python -m  pytest --cov=src --cov-config=.coveragerc

sourcedist:
	$(UV_RUN) python -m ankiscripts.sourcedist

clean:
	rm -rf build/
