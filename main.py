import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode

from handlers.registration import command_registration
from utils.config import TOKEN, dp
from handlers.start import command_start_handler


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.message.register(command_start_handler)
    dp.message.register(command_registration)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
