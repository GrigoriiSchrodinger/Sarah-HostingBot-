from aiogram.filters.state import StatesGroup, State


class Form(StatesGroup):
    email = State()
    password = State()
    ready = State()
