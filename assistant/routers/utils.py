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

rt = aio.Router(name=__name__)
from assistant.routers.general import main_menu
from assistant.utils.markups import back_utils_keyboard, utils_keyboard
from assistant.utils.utils import check_dash_health, generate_secret_key


@rt.callback_query(aio.F.data == "main:utils")
async def handle_utils(query: aio.types.CallbackQuery):
    if isinstance(query.message, aio.types.Message):
        await query.message.edit_text("Utils menu:", reply_markup=utils_keyboard)


@rt.callback_query(aio.F.data == "utils:back")
async def back_to_main(query: aio.types.CallbackQuery):
    if isinstance(query.message, aio.types.Message):
        await main_menu(query.message)


@rt.callback_query(aio.F.data == "utils:check_dash")
async def handle_check_dash(query: aio.types.CallbackQuery):
    if isinstance(query.message, aio.types.Message):
        _, message = check_dash_health()
        await query.message.edit_text(message, reply_markup=back_utils_keyboard)


@rt.callback_query(aio.F.data == "utils:generate_key")
async def handle_gen_key(query: aio.types.CallbackQuery):
    if isinstance(query.message, aio.types.Message):
        await query.message.edit_text(
            f"Your key is: `{generate_secret_key()}`",
            reply_markup=back_utils_keyboard,
            parse_mode=aio.enums.ParseMode.MARKDOWN_V2,
        )
