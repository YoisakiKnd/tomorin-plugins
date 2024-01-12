
from core import *
import requests
from PIL import Image
from plugins.h import h
@on.message_created
def _httpcat(event: Event):
   if event.message.content.startswith("状态码猫图 "):
      url = "https://http.cat/{}".format(event.message.content[5:])
      response = requests.get(url)
      img = Image.open(BytesIO(response.content))
      event.message_create(content=f'{h.image(img)}')

from io import BytesIO


