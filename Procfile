# web: waitress-serve --listen=$PORT visu.wsgi:application
web: gunicorn --workers=2 visu:application
web: bundle exec thin start -p $PORT