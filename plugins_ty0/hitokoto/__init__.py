from core import *
import requests
from core import event
from plugins.h import h



@on.message_created
def _hitokoto(event: Event):
   if event.message.content == 'salt一言':
      event.message_create(content=f"{h.quote(event.message.id)}{msg()}")


def msg():
   response = requests.get("https://v1.hitokoto.cn")
   hitokoto = response.json()["hitokoto"]
   return hitokoto