from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from database.bot_db import sql_command_random

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.message_id)
    else: message.answer('сообщение должно быть ответом')

# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo = open("pic_1e848ca661ae53311bb74529ea0470ff.png", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)

# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Столица Австралии?"
    answers = [
        "Сидней",
        "Канберра",
        "Брисбен",
        "Осло",
        "Оттава"
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="легко",
        open_period=15,
        reply_markup=markup

    )


async def get_random_user(message:types.Message):
    await sql_command_random(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
