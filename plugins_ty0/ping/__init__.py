from core import *
from plugins.h import h


@on.message_created
def _ping(event: Event):
    if event.message.content == 'saltping':
            event.message_create(content=f'{h.quote(event.message.id)}pong!')
