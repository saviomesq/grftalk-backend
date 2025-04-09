import os
from django.core.wsgi import get_wsgi_application
from core.socket import socket
import socketio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Cria a aplicação WSGI padrão do Django
django_application = get_wsgi_application()

# Integra o servidor Socket.IO com a aplicação WSGI do Django
application = socketio.WSGIApp(socket, django_application)