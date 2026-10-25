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


import asyncio
import logging
import os
import sys

import aiogram as aio
import aiogram.client.session.aiohttp
import aiogram.client.telegram

from assistant.routers import faq, general, inlines, utils


async def main_func(log: logging.Logger):

    MIRROR_URL = os.environ.get("MIRROR_URL")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    if not isinstance(MIRROR_URL, str):
        raise TypeError("No MIRROR_URL env variable specified")
    if not isinstance(BOT_TOKEN, str):
        raise TypeError("No BOT_TOKEN env variable specified")

    log.log(logging.WARNING, "Starting bot...")
    log.log(logging.INFO, "Creating DP...")
    dp = aio.Dispatcher()

    log.log(logging.INFO, "Registering routers...")
    dp.include_routers(general.rt, faq.rt, utils.rt, inlines.rt)

    log.log(logging.INFO, "Creating bot session...")
    # noinspection argument-list
    session = aiogram.client.session.aiohttp.AiohttpSession(
        api=aiogram.client.telegram.TelegramAPIServer.from_base(MIRROR_URL)
    )

    log.log(logging.INFO, "Creating bot...")
    # noinspection bad-argument-type
    bot = aio.Bot(token=BOT_TOKEN, session=session)

    log.log(logging.INFO, "Starting polling...")
    try:
        await dp.start_polling(bot)
    finally:
        log.log(logging.WARNING, "Closing bot session...")
        await bot.session.close()
        log.log(logging.WARNING, "Stopping bot...")
        sys.exit(0)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    asyncio.run(main_func(logger))
