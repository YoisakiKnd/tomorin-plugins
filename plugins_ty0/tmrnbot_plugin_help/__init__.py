from core import on, Event
from plugins.h import h
from plugins.text_to_image import text2img
@on.message_created
def _help(event: Event):
    if event.message.content == 'help':
        helps_content = """
SorutoBot帮助
===========
help 呼出帮助
saltpeek 偷窥开发者的屏幕
状态 获取bot的运行状态
今日人品 获取今日人品
salt早/salt晚 跟可爱猫猫道安
一言 获取一言
色图 获取美图/色图(API来源:iw233.cn)
状态码猫图 [http状态码] 获取相应状态码的猫图
网页截图 [链接] 截图相应网页
猜数字 猜数字小游戏
============
"""
        help_image = text2img(helps_content)
        event.message_create(content=f'{h.quote(event.message.id)}{h.image(help_image)}')