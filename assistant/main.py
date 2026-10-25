# coding=utf8
import asyncio

import aiogram as aio
import aiogram.client.session.aiohttp
import aiogram.client.telegram

import os
import logging

from assistant.routers import faq, general


async def main():
    logging.log(logging.INFO, "Creating DP...")
    dp = aio.Dispatcher()
    
    logging.log(logging.INFO, "Registering routers...")
    dp.include_routers(general.rt, faq.rt)
    
    logging.log(logging.INFO, "Creating bot session...")
    # noinspection argument-list,bad-argument-type
    session = aio.client.session.aiohttp.AiohttpSession(
            api=aio.client.telegram.TelegramAPIServer.from_base(os.environ.get("MIRROR_URL")))
    
    logging.log(logging.INFO, "Creating bot...")
    # noinspection bad-argument-type
    bot = aio.Bot(token=os.environ.get("BOT_TOKEN"), session=session)
    
    logging.log(logging.INFO, "Starting polling...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
