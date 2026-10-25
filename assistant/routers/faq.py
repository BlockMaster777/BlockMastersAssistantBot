# coding=utf8
import aiogram as aio

from assistant.utils.markups import faq_keyboard
from assistant.routers.general import main_menu

rt = aio.Router(name=__name__)


@rt.callback_query(aio.F.data == "main:faq")
async def handle_faq_menu(query: aio.types.CallbackQuery):
    await faq_menu(query)


async def faq_menu(query: aio.types.CallbackQuery):
    await query.message.edit_text("Here is the FAQ section. Please choose a topic:",
                                  reply_markup=faq_keyboard)


@rt.callback_query(aio.F.data == "faq:back")
async def back_to_main(query: aio.types.CallbackQuery):
    # noinspection bad-argument-type
    await main_menu(query.message)
