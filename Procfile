# web: waitress-serve --listen=$PORT visu.wsgi:application
web: gunicorn --bind 0.0.0.0:$PORT visu:app
web: bundle exec thin start -p $PORT