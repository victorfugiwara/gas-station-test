DJANGO_CMD = python problem2/manage.py

install:
	@pip install -r requirements.pip

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

run: clean
	@$(DJANGO_CMD) runserver 0.0.0.0:8000
