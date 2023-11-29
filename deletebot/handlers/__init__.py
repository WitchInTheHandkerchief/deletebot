from aiogram import Dispatcher

from deletebot.handlers.send_message import send_message
from deletebot.handlers.start import start
from deletebot.handlers.update import update


def setup(dp: Dispatcher):
    dp.register_inline_handler(start)
    dp.register_inline_handler(update)
    dp.register_inline_handler(send_message)
