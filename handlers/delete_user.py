from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from handlers.state.user import Form
from utils.config import dp, db


@dp.message(Command("delete"))
async def command_delete_user(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.ready)
    await message.answer(
        text=f"Ты уверен?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Да"),
                    KeyboardButton(text="Нет"),
                ]
            ],
            resize_keyboard=True,
        )
    )


@dp.message(Form.ready)
async def process_finish(message: Message, state: FSMContext):
    requests_message = message.text

    if requests_message == "Да":
        db.delete_user(
            id_user=message.from_user.id,
        )
        await message.answer(
            text=f"Удалила!",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.clear()
    else:
        await state.clear()
        await message.answer(
            text="Ну и правильно",
            reply_markup=ReplyKeyboardRemove()
        )
