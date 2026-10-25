import asyncio
import logging
import os
import sys

import aiogram as aio
import aiogram.client.session.aiohttp
import aiogram.client.telegram

from assistant.routers import faq, general, inlines, utils


async def main_func(log: logging.Logger):
    log.log(logging.WARNING, "Starting bot...")
    log.log(logging.INFO, "Creating DP...")
    dp = aio.Dispatcher()
    
    log.log(logging.INFO, "Registering routers...")
    dp.include_routers(general.rt,
                       faq.rt,
                       utils.rt,
                       inlines.rt)
    
    log.log(logging.INFO, "Creating bot session...")
    # noinspection argument-list,bad-argument-type
    session = aio.client.session.aiohttp.AiohttpSession(
            api=aio.client.telegram.TelegramAPIServer.from_base(
                os.environ.get("MIRROR_URL")))
    
    log.log(logging.INFO, "Creating bot...")
    # noinspection bad-argument-type
    bot = aio.Bot(token=os.environ.get("BOT_TOKEN"), session=session)
    
    log.log(logging.INFO, "Starting polling...")
    try:
        await dp.start_polling(bot)
    finally:
        log.log(logging.WARNING, "Closing bot session...")
        await bot.session.close()
        log.log(logging.WARNING, "Stopping bot...")
        sys.exit(0)


if __name__ == "__main__":
    log = logging.getLogger(__name__)
    asyncio.run(main_func(log))
