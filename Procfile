# web: waitress-serve --listen=$PORT visu.wsgi:application
web: gunicorn --bind 127.0.0.1:8000 wsgi:application
web: bundle exec thin start -p $POR