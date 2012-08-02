clean:
	@find . -name "*.pyc" -delete

test: clean
	@echo "Running tests..."
	@python test_suffix.py

