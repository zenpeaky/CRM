# CRM


Install the required packages
```python
pipenv install
```

Copy the .env_example to .env
```python
cd src && cp .env_example .env
```

Move to the root folder and do migration
```python
python manage.py migrate
```

Create Superuser
```python
python manage.py createsuperuser
```

Run the app
```python
python manage.py runserver
```