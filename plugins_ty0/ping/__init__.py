from core import *
from plugins.h import h


@on.message_created
def _ping(event: Event): #简单的自动回复检测机器人在线状态
    if event.message.content == 'saltping':
            event.message_create(content=f'{h.quote(event.message.id)}pong!')
