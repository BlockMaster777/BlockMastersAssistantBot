# coding=utf8
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from assistant.utils.schemas import MainSchema, FAQSchema

def __keyboard_generator(schema: list[dict[str, str]], prefix: str = "main") -> (
        InlineKeyboardMarkup):
    return InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=list(
                                    [InlineKeyboardButton(text=item["l"],
                                                          callback_data=
                                                          prefix + ":" + item["c"])]
                                    for item in schema))


faq_keyboard = __keyboard_generator(FAQSchema, "faq")

back_keyboard = __keyboard_generator([{"l": "Back", "c": "back"}])

main_keyboard = __keyboard_generator(MainSchema)
