# -----------------------------------------------------------------------------------
#  BlockMastersAssistantBot
#  Copyright (C) 2026  BlockMaster
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------------
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from assistant.utils.schemas import FAQSchema, MainSchema, UtilsSchema


def __keyboard_generator(
    schema: list[dict[str, str]], prefix: str = "main", add_back_button: bool = True
) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=el["l"], callback_data=f"{prefix}:{el['c']}")]
        for el in schema
    ]

    buttons.append(
        [InlineKeyboardButton(text="Back", callback_data=f"{prefix}:back")]
    ) if add_back_button else None

    return InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)


def __back_button_keyboard(data: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data=data)]],
    )


main_keyboard = __keyboard_generator(MainSchema, add_back_button=False)

faq_keyboard = __keyboard_generator(FAQSchema, "faq")

utils_keyboard = __keyboard_generator(UtilsSchema, "utils")

back_faq_keyboard = __back_button_keyboard("main:faq")

back_report_keyboard = __back_button_keyboard("main:report")

back_utils_keyboard = __back_button_keyboard("main:utils")
