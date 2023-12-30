import psutil
import time
from core import on, Event


def cpu_percent() -> float: #获取CPU使用状态
        psutil.cpu_percent(None) # 第一次返回的结果是0
        time.sleep(0.5)
        cpu_msg = psutil.cpu_percent(None)
        return cpu_msg


def used_memory() -> int: #获取内存使用状态
    mem = psutil.virtual_memory().percent
    return mem


@on.message_created
def _status(event: Event):
        if event.message.content == 'saltstatus':
                        event.message_create(content=f'当前CPU占用:{cpu_percent()}%\n已使用内存:{used_memory()}%')



