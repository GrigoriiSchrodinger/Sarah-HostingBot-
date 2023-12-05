from aiogram.filters.state import StatesGroup, State


class RegistrationForm(StatesGroup):
    email = State()
    password = State()
    ready = State()
