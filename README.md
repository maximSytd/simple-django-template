```bash
uv run python manage.py makemigrations & python manage.py migrate & python manage.py runserver

python manage.py createsuperuser # root root@localhost root
```

## Install uv on Windows (unnecessary)
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```