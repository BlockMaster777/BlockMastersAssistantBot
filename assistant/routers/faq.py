# coding=utf8
import aiogram as aio

from assistant.routers.general import main_menu
from assistant.utils.markups import back_faq_keyboard, faq_keyboard
from assistant.utils.schemas import FAQSchema

rt = aio.Router(name=__name__)


@rt.callback_query(aio.F.data == "main:faq")
async def handle_faq_menu(query: aio.types.CallbackQuery):
    await query.message.edit_text("Here is the FAQ section. Please choose a topic:",
                                  reply_markup=faq_keyboard)


@rt.callback_query(aio.F.data == "faq:back")
async def back_to_main(query: aio.types.CallbackQuery):
    # noinspection bad-argument-type
    await main_menu(query.message)


@rt.callback_query(aio.F.data.startswith("faq:"))
async def handle_faq_topic(query: aio.types.CallbackQuery):
    topic = query.data.split(":")[1]
    for el in FAQSchema:
        if el["c"] == topic:
            await query.message.edit_text(el["a"], reply_markup=back_faq_keyboard,
                                          parse_mode=aio.enums.ParseMode.MARKDOWN_V2,
                                          disable_web_page_preview=True)
            break
