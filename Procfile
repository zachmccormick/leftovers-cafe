web: ddtrace-run waitress-serve --port=$PORT wsgi:application
worker: ddtrace-run celery --app=taskapp worker --pool=gevent --loglevel=info --scheduler=django
release: ddtrace-run python manage.py migrate
