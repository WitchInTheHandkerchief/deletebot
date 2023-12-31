import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from deletebot.config import dp, bot
from deletebot.db.fetchers import fetch_channel_id
from deletebot.middlewares.scheduler import loop, run_at, delete_message
from deletebot.states import Form


@dp.message_handler(commands=['send_message'], state='*')
async def send_message(msg: Message, state: FSMContext) -> None:
    await state.finish()
    await msg.answer("Отправьте текст, который вы хотите отправить в ваш телеграм-канал")
    await Form.channelMessage.set()


@dp.message_handler(state=Form.channelMessage, content_types=['text'])
async def message_to_send(msg: Message, state: FSMContext) -> None:
    await state.finish()
    channel_id = fetch_channel_id(msg)[0][0]
    sent_msg = await bot.send_message(channel_id, msg.text)
    await loop.create_task(run_at(delete_message(sent_msg)))
    loop.run_forever()
