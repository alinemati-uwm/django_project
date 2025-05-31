
<div align="center">
    <a href="https://londonappdeveloper.com" target="_blank">
        <img src="https://londonappdeveloper.com/wp-content/uploads/2024/11/banner.svg" alt="Banner image" />
    </a>
</div>

<div align="center">
    <p>Full-Stack Consulting and Courses.</p>
    <a href="https://londonapp.dev" target="_blank">Website</a> |
    <a href="https://londonapp.dev/courses" target="_blank">Courses</a> |
    <a href="https://londonapp.dev/tutorials" target="_blank">Tutorials</a> |
    <a href="https://londonapp.dev/consulting" target="_blank">Consulting
</div>

<br /><br >

# Add a Database to Django with Postgres and Docker

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