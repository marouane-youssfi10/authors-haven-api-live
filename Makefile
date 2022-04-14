build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show_logs:
	docker compose -f local.yml logs

migrate:
	compose -f local.yml run --rm api python3 manage.py migrate

makemigrations:
	compose -f local.yml run --rm api python3 manage.py makemigrations

collectstatic:
	compose -f local.yml run --rm api python3 manage.py collectstatic --no-input --clear

superuser:
	compose -f local.yml run --rm api python3 manage.py createsuperuser