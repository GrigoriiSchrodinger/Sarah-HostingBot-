from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from handlers.state.delete_form import DeleteForm
from utils.config import dp, db


@dp.message(Command("delete"))
async def command_delete_user(message: Message, state: FSMContext) -> None:
    await state.set_state(DeleteForm.ready)
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


@dp.message(DeleteForm.ready)
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
