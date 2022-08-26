"""
WSGI config for visu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
from waitress import serve
import os
import django
app = django(__name__)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visu.settings')

application = get_wsgi_application()
if __name__ == "__main__":
    #app.run('0.0.0.0',port=server_port)
    serve(app)
serve(app, host='0.0.0.0', port=8080)