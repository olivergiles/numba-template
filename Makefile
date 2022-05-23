test:
	@pytest

install:
	@pip install -e .

clean:
	@rm -rf **.egg-info 
	@find . -type d -name __pycache__ -exec rm -r {} \+
