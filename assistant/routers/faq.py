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

from assistant.routers.general import main_menu
from assistant.utils.markups import back_faq_keyboard, faq_keyboard
from assistant.utils.schemas import FAQSchema

rt = aio.Router(name=__name__)


@rt.callback_query(aio.F.data == "main:faq")
async def handle_faq_menu(query: aio.types.CallbackQuery):
    if isinstance(query.message, aio.types.Message):
        await query.message.edit_text(
            "Here is the FAQ section. Please choose a topic:", reply_markup=faq_keyboard
        )


@rt.callback_query(aio.F.data == "faq:back")
async def back_to_main(query: aio.types.CallbackQuery):
    if isinstance(query.message, aio.types.Message):
        await main_menu(query.message)


@rt.callback_query(aio.F.data.startswith("faq:"))
async def handle_faq_topic(query: aio.types.CallbackQuery):

    if isinstance(query.data, str) and isinstance(query.message, aio.types.Message):
        topic = query.data.split(":")[1]
        for el in FAQSchema:
            if el["c"] == topic:
                await query.message.edit_text(
                    el["a"],
                    reply_markup=back_faq_keyboard,
                    parse_mode=aio.enums.ParseMode.MARKDOWN_V2,
                    disable_web_page_preview=True,
                )
                break
