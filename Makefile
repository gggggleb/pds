build:
		pip wheel .
		rm -r pds.egg-info/ build/
		mkdir package
		mv *.whl package
test:
		python pds_test.py
install:
		pip install .
		rm -r pds.egg-info/ build/