from aiogram import types, Dispatcher
from config import bot, dp, admins
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.bot_db import sql_command_all, sql_command_delete


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in admins:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан забанил пользователя "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")


async def delete_data(message: types.Message):
    if message.from_user.id not in admins:
        await message.answer("Ты не мой босс!")
    else:
        users = await sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id, f"{user[0]}"
                                                         f"{user[1]}, {user[2]}, {user[3]}, "
                                                         f"{user[4]}")
            reply_markup = InlineKeyboardMarkup().add(
                InlineKeyboardButton(f"delete {user[1]}",
                                     callback_data=f"delete {user[0]}"))




async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='Удалено с БД', show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith('delete'))