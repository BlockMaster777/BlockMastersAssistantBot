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

from assistant.utils.utils import check_dash_health

rt = aio.Router(name=__name__)


@rt.inline_query()
async def handle_inline_dash_status(query: aio.types.InlineQuery):
    await query.answer(
        results=[
            aio.types.InlineQueryResultArticle(
                id="dash_status",
                title="Check DashBlocks Status",
                input_message_content=aio.types.InputTextMessageContent(
                    message_text=check_dash_health()[1]
                ),
            ),
        ]
    )
