import sqlite3

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from handlers.state.registration_form import RegistrationForm
from utils.config import dp, db


@dp.message(Command("registration"))
async def command_registration(message: Message, state: FSMContext) -> None:
    await state.set_state(RegistrationForm.email)
    await message.answer(
        text=f"Отправь мне спой логин",
    )


@dp.message(RegistrationForm.email)
async def process_email(message: Message, state: FSMContext):
    user_email = message.text
    await state.update_data(email=user_email)
    await state.set_state(RegistrationForm.password)
    await message.answer(
        text=f"Отлично! {message.from_user.first_name}, Теперь отправь мне свой пароль",
    )


@dp.message(RegistrationForm.password)
async def process_password(message: Message, state: FSMContext):
    user_password = message.text
    await state.update_data(password=user_password)
    await state.set_state(RegistrationForm.ready)
    data = await state.get_data()
    await message.answer(
        text=f"Так, твой email - {data.get('email')}\npassword - {data.get('password')}\nВерно?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Да"),
                    KeyboardButton(text="Нет"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@dp.message(RegistrationForm.ready)
async def process_finish(message: Message, state: FSMContext):
    requests_message = message.text
    data = await state.get_data()

    if requests_message == "Да":
        try:
            db.insert_user(
                id_user=message.from_user.id,
                email=data.get("email"),
                password=data.get("password")
            )
            await message.reply(
                text=f"Сохранила!",
                reply_markup=ReplyKeyboardRemove()
            )
        except sqlite3.IntegrityError:
            await message.reply(
                text=f"Ты уже зареган, мальчик мой",
                reply_markup=ReplyKeyboardRemove()
            )
        await state.clear()
    else:
        await state.clear()
        await message.reply(
            text="Ну давай заново) Отправь мне свой email.",
            reply_markup=ReplyKeyboardRemove()
        )
