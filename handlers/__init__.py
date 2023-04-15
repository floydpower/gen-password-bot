from aiogram import Dispatcher
from handlers.user import *
from handlers.admin import *

def setup(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(gen_password, lambda msg: msg.text == '🤖 Сгенерировать пароль')
    dp.register_message_handler(set_difficulty, state=UserStates.set_difficulty)
    dp.register_message_handler(cmd_admin, commands='admin')
    dp.register_message_handler(cmd_rass, lambda msg: msg.text == '📪 Рассылка')
    dp.register_message_handler(rass, state=AdminStates.set_text)
    dp.register_message_handler(pic, state=AdminStates.set_pic, content_types=['photo', 'text'])
    dp.register_message_handler(cmd_ban, lambda msg: msg.text == '❌ Бан')
    dp.register_message_handler(set_ban, state=AdminStates.get_userid)
    dp.register_message_handler(info, lambda msg: msg.text == 'ℹ️ Инфо')