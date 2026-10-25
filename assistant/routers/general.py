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
import aiogram as aio
from aiogram.filters.command import Command

from assistant.utils.markups import main_keyboard

rt = aio.Router(name=__name__)


# noinspection argument-list
@rt.message(Command(commands=["start", "help"]))
async def handle_main_menu(message: aio.types.Message):
    await message.answer(
        "Hello! I am an assistant bot. How can I help you?", reply_markup=main_keyboard
    )


async def main_menu(message: aio.types.Message):
    await message.edit_text("How can I help you?", reply_markup=main_keyboard)


@rt.callback_query(aio.F.data == "main:close")
async def handle_close(query: aio.types.CallbackQuery):
    if isinstance(query.message, aio.types.Message):
        await query.message.delete()
