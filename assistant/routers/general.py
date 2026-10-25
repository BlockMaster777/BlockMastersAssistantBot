# coding=utf8
import aiogram as aio
from aiogram.filters.command import Command

from assistant.utils.markups import main_keyboard

rt = aio.Router(name=__name__)

@rt.message(Command(commands=["start", "help"]))
async def handle_main_menu(message: aio.types.Message):
    await message.answer("Hello! I am an assistant bot. How can I help you?",
                          reply_markup=main_keyboard)


async def main_menu(message: aio.types.Message):
    await message.edit_text("How can I help you?", reply_markup=main_keyboard)
