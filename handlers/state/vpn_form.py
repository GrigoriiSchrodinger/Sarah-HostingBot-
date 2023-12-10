from aiogram.filters.state import StatesGroup, State


class VPNForm(StatesGroup):
    list = State()
    id = State()
