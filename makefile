make install:
	pip install -r requirements.txt

make migration setup:
	flask db init

make migration:
	flask db migrate -m "Initial migration."

make apply migration:
	flask db upgrade


