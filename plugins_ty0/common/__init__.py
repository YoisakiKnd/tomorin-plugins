from core import on, Event
from plugins.h import h


@on.guild_member_added
def gm_add(event: Event):
    event.message_create(content=f'{h.at(event.user.id)} 欢迎新用户加入本群！')




@on.message_created
def _zao(event: Event):
    if event.message.content == 'salt早':
        if event.user.name != '':
            name_ = '，' + event.user.name
        else:
            name_ = ''
        event.message_create(content=f'早安{name_}!')


@on.message_created
def _wan(event: Event):
    if event.message.content == 'salt晚':
        if event.user.name != '':
            name_ = '，' + event.user.name
        else:
            name_ = ''
        event.message_create(content=f'晚安{name_}!')
