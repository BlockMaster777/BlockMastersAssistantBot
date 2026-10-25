# coding=utf8
import aiogram as aio

rt = aio.Router(name=__name__)
from assistant.utils.markups import utils_keyboard, back_utils_keyboard
from assistant.routers.general import main_menu
from assistant.utils.utils import check_dash_health, generate_secret_key


@rt.callback_query(aio.F.data == "main:utils")
async def handle_utils(query: aio.types.CallbackQuery):
    await query.message.edit_text("Utils menu:", reply_markup=utils_keyboard)


@rt.callback_query(aio.F.data == "utils:back")
async def back_to_main(query: aio.types.CallbackQuery):
    # noinspection bad-argument-type
    await main_menu(query.message)

@rt.callback_query(aio.F.data == "utils:check_dash")
async def handle_check_dash(query: aio.types.CallbackQuery):
    status, message = check_dash_health()
    await query.message.edit_text(message,
                                   reply_markup=back_utils_keyboard)


@rt.callback_query(aio.F.data == "utils:generate_key")
async def handle_gen_key(query: aio.types.CallbackQuery):
    await query.message.edit_text(f"Your key is: `{generate_secret_key()}`",
                                   reply_markup=back_utils_keyboard,
                                   parse_mode=aio.enums.ParseMode.MARKDOWN_V2)
