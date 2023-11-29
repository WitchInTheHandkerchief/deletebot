from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from deletebot.config import dp
from deletebot.db import adjusters
from deletebot.states import Form


@dp.message_handler(commands=['update'], state='*')
async def update(msg: Message, state: FSMContext) -> None:
    await state.finish()
    await msg.answer("Отправьте обновленную ссылку на телеграм канал")
    await Form.updateID.set()


@dp.message_handler(state=Form.updateID, content_types=['text'])
async def updateID(msg: Message, state: FSMContext) -> None:
    await state.finish()
    adjusters.update_channel_id(msg)
