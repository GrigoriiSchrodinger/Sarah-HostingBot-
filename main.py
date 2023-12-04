import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode

from database.sql_queries.create import CREATE_TABLE_USERS
from handlers.registration import command_registration
from handlers.start import command_start_handler
from utils.config import TOKEN, dp, db
from utils.logger import logger
from utils.text import LOGO


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.message.register(command_start_handler)
    dp.message.register(command_registration)
    db.create_table(query=CREATE_TABLE_USERS)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logger.info(LOGO)
        asyncio.run(main())
    except Exception as error:
        logger.warning(error)
