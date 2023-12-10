import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode

from handlers.delete_user import command_delete_user
from handlers.registration import command_registration
from handlers.start import command_start_handler
from handlers.vpn_list import command_vpn
from utils.config import TOKEN, dp, db
from utils.logger import logger
from utils.text import LOGO

commands_handlers = [
    command_start_handler,
    command_registration,
    command_delete_user,
    command_vpn,
]


async def main(bot: Bot) -> None:
    for handler in commands_handlers:
        dp.message.register(handler)

    db.create_table_user()
    await dp.start_polling(bot)


if __name__ == "__main__":
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    try:
        logger.info(LOGO)
        asyncio.run(main(bot))
    except Exception as error:
        logger.warning(error)

