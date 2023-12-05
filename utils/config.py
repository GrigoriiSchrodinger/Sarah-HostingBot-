from os import getenv

from aiogram import Dispatcher

from database.manager import DataBaseManager

TOKEN = getenv("BOT_TOKEN", "6887297309:AAH8D3nQ1zyF7gA2OtIVVhAVXYYpcnBYyO4")

dp = Dispatcher()
db = DataBaseManager()
