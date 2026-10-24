# coding=utf8
import asyncio

import aiogram as aio
import aiogram.client.session.aiohttp
import aiogram.client.telegram

import os
import logging

from assistant.routers import general


async def main():
    dp = aio.Dispatcher()
    dp.include_router(general.rt)
    
    # noinspection argument-list,bad-argument-type
    session = aio.client.session.aiohttp.AiohttpSession(
            api=aio.client.telegram.TelegramAPIServer.from_base(os.environ.get("MIRROR_URL")))
    
    # noinspection bad-argument-type
    bot = aio.Bot(token=os.environ.get("BOT_TOKEN"), session=session)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
