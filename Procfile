web: waitress-serve --port=$PORT wsgi:application
worker: celery --app=taskapp worker --pool=gevent --loglevel=info --scheduler=django
release: python manage.py migrate
