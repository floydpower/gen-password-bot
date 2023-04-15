import os
from aiogram import Bot, Dispatcher
from database.database import Database
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=os.getenv('TOKEN'), parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database('database\\database.db')
admin_id = os.getenv('USERID')
