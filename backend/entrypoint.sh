#!/bin/sh
echo "$PWD"

python manage.py makemigrations
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput

echo "from users.models import CustomUser; CustomUser.objects.create_superuser('admin@example.com', 'admin')" | python manage.py shell
python manage.py create_data

python manage.py runserver 0.0.0.0:8000

exec "$@"
