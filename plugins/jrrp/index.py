from bridge.tomorin import *
import random


@on_event.message_created
def _jrrp(session: SessionExtension):
        session.function.register(['saltjrrp'])
        session.function.description = '获取今日人品'
        session.action(
                {
                        None: saltjrrp,
                }
        )

def rp ():
       jrrp = random.randint(0,100)
       return jrrp

def saltjrrp (session):
        session.send(f'{h.quote(session.message.id)}{h.at(session.user.id)} 您今日的人品是{rp()}喵！')

