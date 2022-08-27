# web: waitress-serve --listen=$PORT visu.wsgi:application
web: gunicorn app:app --log-file=-
web: bundle exec thin start -p $PORT