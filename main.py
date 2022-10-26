from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, fsmAdminMentor, notifications
from database.bot_db import sql_create
import asyncio

async def on_startup(_):
    asyncio.create_task(notifications.schedule())
    sql_create()

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)
notifications.register_handlers_notification(dp)
extra.register_handlers_extra(dp)

from config import bot, dp
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)