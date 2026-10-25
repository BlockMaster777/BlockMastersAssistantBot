# coding=utf8
import aiogram as aio

from assistant.utils.utils import check_dash_health

rt = aio.Router(name=__name__)

@rt.inline_query()
async def handle_inline_dash_status(query: aio.types.InlineQuery):
    await query.answer(results=[
        aio.types.InlineQueryResultArticle(
            id="dash_status",
            title="Check DashBlocks Status",
            input_message_content=aio.types.InputTextMessageContent(
                message_text=check_dash_health()[1]
            ),
        ),
        ])
