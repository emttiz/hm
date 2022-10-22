from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
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

# @dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    question = "Сколько в мире океан? "
    answers = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]


    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="ИЗИ",
        open_period=10,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")