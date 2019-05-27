start:
	docker-compose build
	docker-compose up -d
	docker-compose exec web python manage.py db init
	docker-compose exec web python manage.py db migrate --message 'initial database migration'
	docker-compose exec web python manage.py db upgrade

stop:
	docker-compose down