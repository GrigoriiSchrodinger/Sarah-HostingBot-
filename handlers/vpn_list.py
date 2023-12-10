from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from api.api_hosting import APIHosting
from handlers.state.vpn_form import VPNForm
from utils.config import dp


@dp.message(Command("vpn"))
async def command_vpn(message: Message, state: FSMContext) -> None:
    vpn_list = APIHosting().vpn_list(user_id=str(message.from_user.id))
    keyboard = [
        [KeyboardButton(text=f"{vpn['name']} - {vpn['id']}")] for vpn in vpn_list
    ]
    await state.set_state(VPNForm.id)
    await state.update_data(list=vpn_list)
    await message.answer(
        text=f"Какой vpn показать?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=keyboard,
            resize_keyboard=True,
        ),
    )


@dp.message(VPNForm.id)
async def output_vpn_info(message: Message, state: FSMContext):
    id_vpn = message.text
    vpn_list = await state.get_data()

    for vpn in vpn_list.get("list"):
        if f"{vpn['name']} - {vpn['id']}" == id_vpn:
            text = (f"<b>Информация:</b>\n"
                    f"id - {vpn['id']}\n"
                    f"Название - {vpn['name']}\n"
                    f"Локация - {vpn['location']}\n"
                    f"IP - {vpn['ip']}\n\n"
                    f"<b>Состояние:</b>\n"
                    f"Статус - {vpn['status']}\n"
                    f"{vpn['uptime']}\n"
                    f"ЦПУ - {vpn['cpu']}\n"
                    f"Диск - {vpn['drive']}\n\n"
                    f"<b>Оплачен до - {vpn['next_charge']}</b>")
            await message.reply(
                text=text,
                parse_mode='HTML',
                reply_markup=ReplyKeyboardRemove()
            )
        else:
            await message.reply(
                text="Что то не так(( не смогла найти нужный vpn",
                reply_markup=ReplyKeyboardRemove()
            )

