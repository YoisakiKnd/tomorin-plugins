from core import on
from plugins.h import h
import random


@on.message_created
def jrrp(event):
    if event.message.content == '今日人品':
       jrrp_num: int = random.randint(0,100)
       if jrrp_num < 10 :
          event.message_create(f'{h.quote(event.message.id)}{h.at(event.user.id)} 您今日的人品是{jrrp_num}喵！杂鱼❤️~杂鱼❤️~')
       elif jrrp_num >= 10 and jrrp_num < 30 :
          event.message_create(f'{h.quote(event.message.id)}{h.at(event.user.id)} 您今日的人品是{jrrp_num}喵！运气不是很好呢…')
       elif jrrp_num >= 30 and jrrp_num < 50 :
          event.message_create(f'{h.quote(event.message.id)}{h.at(event.user.id)} 您今日的人品是{jrrp_num}喵！运气…一般般？')
       elif jrrp_num >= 50 and jrrp_num < 70 :        
          event.message_create(f'{h.quote(event.message.id)}{h.at(event.user.id)} 您今日的人品是{jrrp_num}喵！运气还可以诶')
       elif jrrp_num >= 70 and jrrp_num < 90 :        
          event.message_create(f'{h.quote(event.message.id)}{h.at(event.user.id)} 您今日的人品是{jrrp_num}喵！运气真不错！')
       elif jrrp_num > 90 :        
          event.message_create(f'{h.quote(event.message.id)}{h.at(event.user.id)} 您今日的人品是{jrrp_num}喵！喵喵喵！运气大爆发！')
       else :
          None
