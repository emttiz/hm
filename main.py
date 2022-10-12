from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, dp
import logging

@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo = open("pic_1e848ca661ae53311bb74529ea0470ff.png", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler(commands=['quiz'])
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

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Мой любимый перс?"
    answers = [
        "Harry Potter",
        "Satoru Gojo",
        "Itachi Uchiha",
        "Nightwing",
        "1, 2, 3",
        "2, 3",
        "2, 4",
        "3, 4"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="ИЗИ",
        open_period=10,
        reply_markup=markup
    )

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)