from aiogram.filters.state import StatesGroup, State


class DeleteForm(StatesGroup):
    ready = State()
