# coding=utf8
import aiogram as aio
from aiogram.filters.command import Command

from assistant.utils.markups import main_keyboard, faq_keyboard

rt = aio.Router(__name__)

@rt.message(Command(commands=["start", "help"]))
async def handle_info(message: aio.types.Message):
    return message.answer("Hello! I am an assistant bot. How can I help you?",
                          reply_markup=main_keyboard)


@rt.callback_query(lambda c: c.data.startswith("main:"))
async def handle_main_callback(callback_query: aio.types.CallbackQuery):
    data = callback_query.data.split(":")[1]
    match data:
        case "faq":
            await callback_query.message.edit_text(
                    "FAQ section. Please select a topic.",
                    reply_markup=faq_keyboard)
        case "report":
            await callback_query.message.edit_text(
                    "Please describe the issue you are facing.",
                    reply_markup=main_keyboard)
        case _:
            await callback_query.message.edit_text(
                    "Unknown option selected. This is an error. Please select "
                    "again.",
                    reply_markup=main_keyboard)
