from bridge.tomorin import on_activator, on_event, h, admin_list, SessionExtension

@on_event.message_created
def _help(session: SessionExtension):
    session.function.register(['help']) #自定义回复示例
    session.function.description = '帮助'
    session.action(
        {
            None: help,
        }
    )

def help (session):
    session.send(f'{helps}')

helps = """
SorutoBot帮助
===========
help 呼出帮助
saltpeek 偷窥开发者的屏幕
saltstatus 获取bot的运行状态
saltjrrp 获取今日人品
salt早/salt晚 跟可爱猫猫道安
============
"""