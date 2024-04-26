# import os
# from channels.routing import ProtocolTypeRouter
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'English_conversation_app.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
# })


# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # your_app은 웹소켓 경로를 정의할 앱 이름으로 변경

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'English_conversation_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns  # WebSocket URL을 관리하는 라우팅 설정
        )
    ),
})
