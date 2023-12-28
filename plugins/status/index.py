import psutil
import time
from bridge.tomorin import *

@on_event.message_created
def _status(session: SessionExtension):
        session.function.register(['saltstatus'])
        session.function.description = '获取系统运行状态'
        session.action(
                {
                        None: saltstatus,
                }
        )

def saltstatus(session):
        session.send(f'当前CPU占用:{CPUPercent()}%\n已使用内存:{MemUsed()}%')


def CPUPercent():
        psutil.cpu_percent(None) # 第一次返回的结果是0
        time.sleep(0.5)
        CPU = psutil.cpu_percent(None)
        return CPU

def MemUsed():
        mem = psutil.virtual_memory().percent
        return mem