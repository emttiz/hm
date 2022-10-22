from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("TOKEN")
admins = [1057749292]
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)