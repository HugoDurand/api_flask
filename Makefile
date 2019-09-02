start:
	docker-compose build
	docker-compose up -d
	docker-compose exec web python manage.py db init
	docker-compose exec web python manage.py db migrate --message 'initial database migration'
	docker-compose exec web python manage.py db upgrade
	docker-compose exec web python manage.py seed
	@echo ========== visit: 'http://localhost:5000' ==========

test:
	docker-compose exec web python manage.py test

stop:
	docker-compose down
	sudo find ./ -type d -name '__pycache__' -prune -exec rm -rf {} +
	sudo find ./ -type d -name 'migrations' -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

restart:
	make stop
	make start

log:
	docker-compose up