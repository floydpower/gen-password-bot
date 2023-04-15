from bot import *
from keyboards.reply import *
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from states.states import AdminStates

async def cmd_admin(message: Message):
    if message.from_user.id == int(admin_id):
        await message.answer('Админ-меню', reply_markup=kb_admin)
    else:
        pass

async def cmd_rass(message: Message):
    if message.from_user.id == admin_id:
        await message.answer('Введите текст рассылки:', reply_markup=kb_back)
        await AdminStates.set_text.set()
    else:
        pass

async def rass(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {
            'text': text
        }
    )
    if message.text == '◀️ Назад':
        await state.reset_state(with_data=True)
        await message.answer('Главное меню', reply_markup=kb_admin)
    else:
        await message.answer('🖼 Теперь отправьте картинку:\nЕсли вы желаете отправить рассылку без картинки, отправьте любое слово')
        await AdminStates.set_pic.set()

async def pic(message: Message, state: FSMContext):
    counter = 0
    counter_unsended = 0
    data = await state.get_data()
    text = data.get('text')
    await state.finish()
    if message.text == '◀️ Назад':
        await state.reset_state(with_data=True)
        await message.answer('Главное меню', reply_markup=kb_admin)

    elif not message.text:
            photo_id = message.photo[0].file_id
            for row in db.all_users():
                try:
                    await bot.send_photo(row[0], photo=photo_id, caption=text)
                    counter += 1
                except:
                    counter_unsended += 1
    else:
        for row in db.all_users():
            try:
                await bot.send_message(row[0], text=text)
                counter += 1
            except:
                counter_unsended += 1

    await message.answer('📪 Рассылка успешно завершена!\n'
                             f'👤 Всего пользователей в боте: <code>{db.count_users()[0][0]}</code>\n'
                             f'✅ Получили рассылку: <code>{counter}</code>\n'
                             f'❌ Не получили: <code>{counter_unsended}</code>', reply_markup=kb_admin)

async def cmd_ban(message: Message):
    if message.from_user.id == int(admin_id):
        await message.answer('Введите USERID пользователя:')
        await AdminStates.get_userid.set()
    else:
        pass

async def set_ban(message: Message, state: FSMContext):
    try:
        user_id = int(message.text)
        if not db.user_exists(user_id):
            await message.answer('❌ Юзер в базе не найден')
        else:
            db.set_ban(user_id)
            await message.answer('✅ Юзер был забанен')

    except:
        await message.answer('Вы ввели не число!')

    finally:
        await state.finish()




