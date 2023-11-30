import asyncio
import datetime

from aiogram.types import Message

from deletebot.config import bot


async def wait_24hours():
    await asyncio.sleep(datetime.timedelta(hours=24).total_seconds())


async def run_at(coro):
    await wait_24hours()
    return await coro


async def delete_message(msg: Message) -> None:
    await bot.delete_message(msg.from_id, msg.message_id)


loop = asyncio.get_event_loop()
