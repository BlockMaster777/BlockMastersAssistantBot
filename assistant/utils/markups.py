# coding=utf8
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from assistant.utils.schemas import MainSchema, FAQSchema, UtilsSchema

def __keyboard_generator(schema: list[dict[str, str]],
                         prefix: str = "main",
                         add_back_button: bool = True) -> InlineKeyboardMarkup:
    buttons = list([
        InlineKeyboardButton(text=el["l"],
                             callback_data=f"{prefix}:{el['c']}")]
        for el in schema)
    
    buttons.append([
        InlineKeyboardButton(text="Back", callback_data=f"{prefix}:back")]) \
        if add_back_button else None
    
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)


main_keyboard = __keyboard_generator(MainSchema, add_back_button=False)

faq_keyboard = __keyboard_generator(FAQSchema, "faq")

utils_keyboard = __keyboard_generator(UtilsSchema, "utils")
