from core import *
import requests
from PIL import Image
from plugins.h import h

@on.message_created
def _setu(event: Event):
    if event.message.content == '色图':
       event.message_create(content=f'{h.quote(event.message.id)}哼，色批{h.image(save_image())}')


def apisetu():
    url = 'https://iw233.cn/api.php?sort=random'
    response = requests.post(url)
    return response.content

def save_image():
    image_data = apisetu()
    with open('image.jpg', 'wb') as f:
        f.write(image_data)
    image = Image.open('image.jpg')
    return image