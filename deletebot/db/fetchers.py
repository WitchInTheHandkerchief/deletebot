from typing import List

from aiogram.types import Message

from deletebot.db.services import fetch_all


def fetch_channel_id(msg: Message) -> List[tuple]:
    return fetch_all(f"SELECT channel_id FROM channels WHERE admin_id = {msg.from_user.id};")
