from aiogram.types import ReplyKeyboardMarkup
from .buttons import *

kb_user = ReplyKeyboardMarkup(resize_keyboard=True).add(
    gen_pass_btn, info_btn
)

kb_choices = ReplyKeyboardMarkup(resize_keyboard=True).add(
    easy_btn, medium_btn, hard_btn
).row(
    back_btn
)

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(
    rass_btn, ban_btn
)

kb_rass_choices = ReplyKeyboardMarkup(resize_keyboard=True).add(
    without_pic, with_pic
).row(
    back_btn
)

kb_back = ReplyKeyboardMarkup(resize_keyboard=True).add(
    back_btn
)
