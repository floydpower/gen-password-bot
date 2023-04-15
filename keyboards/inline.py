from aiogram.types import InlineKeyboardMarkup
from .buttons import *

review_kb = InlineKeyboardMarkup().add(
    link_lzt
)

info_kb = InlineKeyboardMarkup(row_width=1).add(
    link_lzt, author_bot, repository_github
)