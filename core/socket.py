import socketio

import django.conf import settings

#create a socketio server instance

socket = socketio.Server(
    cors_allowed_origins= settings.CORS_ALLOWED_ORIGINS
)