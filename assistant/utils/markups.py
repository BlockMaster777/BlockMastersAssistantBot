# coding=utf8
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from assistant.utils.schemas import FAQSchema, MainSchema, UtilsSchema


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


def __back_button_keyboard(data: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[[
        InlineKeyboardButton(text="Back", callback_data=data)]])


main_keyboard = __keyboard_generator(MainSchema, add_back_button=False)

faq_keyboard = __keyboard_generator(FAQSchema, "faq")

utils_keyboard = __keyboard_generator(UtilsSchema, "utils")

back_faq_keyboard = __back_button_keyboard("main:faq")

back_report_keyboard = __back_button_keyboard("main:report")

back_utils_keyboard = __back_button_keyboard("main:utils")
