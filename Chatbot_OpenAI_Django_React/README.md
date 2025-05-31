 Database to Django with Postgres and Docker

How to add a Database to Django with Postgres and Docker.


# some importanbd user:
```bash
docker compose run --rm backend python manage.py createsuperuser
```
you must create superuser to access the admin panel.


now run the server:
```bash
docker compose up
```


 docker compose run --rm backend sh -c "python manage.py makemigrations"
