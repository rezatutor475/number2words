install:
	pip install -r requirements.txt

format:
	black .

lint:
	flake8 number2words tests

test:
	pytest --cov=number2words --cov-report=term-missing

docs:
	mkdocs build

clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache htmlcov dist build *.egg-info

run:
	python usage_example.py

build:
	python setup.py sdist bdist_wheel

publish:
	twine upload dist/*

ci: lint test
