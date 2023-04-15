from aiogram.dispatcher.filters.state import State, StatesGroup

class UserStates(StatesGroup):
    set_difficulty = State()

class AdminStates(StatesGroup):
    rass_choice = State()
    set_text = State()
    set_pic = State()
    get_userid = State()