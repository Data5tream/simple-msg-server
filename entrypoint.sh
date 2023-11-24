python manage.py migrate --noinput
nginx -g 'daemon on;'
gunicorn --bind=0.0.0.0:8001 simple_msg.wsgi:application
