from core import on, Event
from plugins.h import h

import requests
from PIL import Image
import io

@on.message_created
def saltpeek(event: Event):
        response = requests.get("http://127.0.0.1:1919/my/screen")
        img = Image.open(io.BytesIO(response.content))
        if event.message.content == 'saltpeek':
                event.message_create(content=f'{h.quote(event.message.id)}ty0是笨蛋{h.image(img)}')