
all: profile

profile:
	pytest -k real --durations=0

test:
	pytest -q -k 'not slow'

flake:
	find . -name "*.py" | grep -v template | xargs pyflakes

clean:
	find . -name "__pycache__" -o -name ".pytest_cache" -o -name "to_do.sh" | xargs rm -rf
