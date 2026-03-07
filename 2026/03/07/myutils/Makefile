run-dev:
	uv run --group dev python main.py < input.txt
run-dev-output:
	uv run --group dev python main.py < input.txt > output.txt
dev-py:
	uv run --group dev python
dev-ipy:
	uv run --group dev ipython
debug-ipy:
	uv run --group dev ipython -X --pdb main.py < input.txt
debug-dill:
	uv run --group dev ipython -i -c "from utils import load_into_namespace; ns=globals(); load_into_namespace('main.dill', ns); print('Loaded:', list(ns.keys()))"
test:
	uv run pytest -q
test-fast:
	uv run pytest -q -x
