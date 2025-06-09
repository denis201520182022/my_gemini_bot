# bot.py

import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import main_handler

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(main_handler.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
