build:
		pip wheel .
		rm -r pds.egg-info/ build/
		mkdir package
		mv *.whl package
test:
		python pds/__init__.py test
install:
		pip install .