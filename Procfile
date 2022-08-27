# web: waitress-serve --listen=$PORT visu.wsgi:application
web: gunicorn --workers=2 visu.wsgi:application
web: bundle exec thin start -p $PORT