from core import on, Event


@on.message_created
def _help(event: Event):
    if event.message.content == 'help': #简易help，可自行修改
        helps_content = """ 
SorutoBot帮助
===========
help 呼出帮助
saltpeek 偷窥开发者的屏幕
saltstatus 获取bot的运行状态
saltjrrp 获取今日人品
salt早/salt晚 跟可爱猫猫道安
salt一言 获取一言
saltsetu 获取美图/色图(API来源:iw233.cn)
============
"""
        event.message_create(content=helps_content)