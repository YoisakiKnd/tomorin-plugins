from core import on
from plugins.h import h
import random


@on.message_created
def jrrp(event):
    if event.message.content == 'saltjrrp':
        jrrp_num: int = random.randint(0,100) #随机0－100
        event.message_create(f'{h.quote(event.message.id)}{h.at(event.user.id)} 您今日的人品是{jrrp_str}喵！')

#TODO: 增加人品反馈消息
