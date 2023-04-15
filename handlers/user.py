from datetime import date
import random
from aiogram.types import Message
from bot import *
from keyboards.reply import *
from keyboards.inline import *
from aiogram.dispatcher import FSMContext
from states.states import UserStates

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()_-'

async def cmd_start(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    if db.check_ban(message.from_user.id) == 1:
        await message.answer('❌ Вы заблокированы')
    else:
        await message.answer("🔥 Привет! Ты попал в бота, в котором ты сможешь сгенерировать пароль любой сложности!\n\n"
                            f"<b>Мы не сохраняем ваши пароли!</b> Проект Open-Source!\n",
                            reply_markup=kb_user)

async def info(message: Message):
    user_stats = db.user_stats(message.from_user.id)
    stats = db.stats()
    if date.today() != stats[2]:
        db.update_date(date.today())
        db.refresh_data()
    await message.answer(f'{message.from_user.username} (<code>{message.from_user.id}</code>)\n'
                         f'Вы сгенерировали <code>{user_stats[1]}</code> паролей\n\n'
                         f'Всего пользователей в боте: <code>{db.count_users()[0][0]}</code>\n'
                         f'Всего сгенерировано паролей: <code>{stats[0]}</code>\n'
                         f'Сгенерировано паролей сегодня: <code>{stats[1]}</code>', reply_markup=info_kb)

async def gen_password(message: Message):
    if db.check_ban(message.from_user.id) == 1:
        await message.answer('❌ Вы заблокированы')
    else:
        await message.answer('Укажите сложность пароля:', reply_markup=kb_choices)
        await UserStates.set_difficulty.set()

async def set_difficulty(message: Message, state: FSMContext):
    password = ''
    if message.text == '◀️ Назад':
        await state.reset_state(with_data=True)
        await message.answer('Вы были возвращены в меню',
                             reply_markup=kb_user)
    else:
        if message.text == '🍏 Легкий':
            for i in range(random.randint(5, 12)):
                password += random.choice(symbols)
            await message.answer(f'🔑 Ваш пароль: {password}',
                                 reply_markup=kb_user)


        elif message.text == '🍊 Средний':
            for i in range(random.randint(10, 17)):
                password += random.choice(symbols)
            await message.answer(f'🔑 Ваш пароль: {password}',
                                 reply_markup=kb_user)

        elif message.text == '♦️ Сложный':
            for i in range(random.randint(20, 35)):
                password += random.choice(symbols)
            await message.answer(f'🔑 Ваш пароль: {password}',
                                 reply_markup=kb_user)

        db.add_count(message.from_user.id)
        db.add_today()
        db.add_all_count()
        await message.answer('😊 Вежливым тоном было бы написать благодарность под темой на форуме LOLZTEAM',
                                 reply_markup=review_kb)

    await state.finish()



