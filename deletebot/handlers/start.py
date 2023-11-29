from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.types import Message

from deletebot.config import dp
from deletebot.db import adjusters
from deletebot.states import Form


@dp.message_handler(commands=['start'], state='*')
async def start(msg: Message, state: FSMContext) -> None:
    await msg.answer("Введите ваш id канала и добавьте бота в редакторы")
    await state.finish()
    await Form.idMessage.set()


@dp.message_handler(content_types=['text'], state=Form.idMessage)
async def channelIDMessage(msg: Message, state: FSMContext) -> None:
    await state.finish()
    adjusters.save_telegram_id(msg)
    adjusters.save_channel_id(msg)
