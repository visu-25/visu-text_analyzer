# web: waitress-serve --listen=$PORT visu.wsgi:application
web: gunicorn visu.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
python manage.py collectstatic --noinput
python manage.py migrate