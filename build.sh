#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py migrate

python manage.py shell << END
from django.contrib.auth.models import User

username = "admin"

password = "admin123"

email = "admin@gmail.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )

    print("Superuser created")

else:
    print("Superuser already exists")

END