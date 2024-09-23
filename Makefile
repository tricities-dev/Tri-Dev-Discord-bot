intial-setup:
	python3 -m venv venv
	cp .env.example .env
	docker compose up -d
	pip install -r requirements.txt
db-migrate:
	python main.py --setup
make run:
	python main.py