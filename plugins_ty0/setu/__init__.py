from core import *
import requests
from PIL import Image
from plugins.h import h

@on.message_created
def _setu(event: Event):
    if event.message.content == 'saltsetu':
       event.message_create(content=f'{h.quote(event.message.id)}哼，色批{h.image(save_image())}')


def apisetu():
    url = 'https://iw233.cn/api.php?sort=random' #API来源(iw233.cn)
    response = requests.post(url)
    return response.content

def save_image(): #获取图片并返回
    image_data = apisetu()
    with open('image.jpg', 'wb') as f:
        f.write(image_data)
    image = Image.open('image.jpg')
    return image