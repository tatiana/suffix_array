clean:
	@echo "Cleaning pyc and vim swap files..."
	@find . -name "*.pyc" -delete
	@find . -name "*.sw[a-z]" -delete

setup:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

test: clean
	@echo "Running all tests..."
	@nosetests -s --with-coverage --cover-erase --cover-inclusive --cover-package=suffix_array --tests=tests
