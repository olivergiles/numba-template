test:
	@pytest

install:
	@pip install .

clean:
	@rm -rf **.egg-info 
	@find . -type d -name __pycache__ -exec rm -r {} \+
