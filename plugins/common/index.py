from bridge.tomorin import *

@on_event.guild_member_added
def _gmadd (session: SessionExtension):
    session.send(f'{h.at(session.user.id)} 欢迎新用户加入本群！')

@on_event.guild_member_removed
def _gmdel(session: SessionExtension):
    session.send(f'{session.user.name}({session.user.id})退出了本群')


@on_event.message_created
def _zao(session: SessionExtension):
        session.function.register(['salt早'])
        session.function.description = '跟可爱猫猫道早'
        session.action(
                {
                        None: saltzao,
                }
        )

def saltzao(session):
     session.send(f'早上好，{session.user.name}!')

@on_event.message_created
def _wan(session: SessionExtension):
        session.function.register(['salt晚'])
        session.function.description = '跟可爱猫猫道晚'
        session.action(
                {
                        None: saltwan,
                }
        )

def saltwan(session):
     session.send(f'晚安，{session.user.name}!')