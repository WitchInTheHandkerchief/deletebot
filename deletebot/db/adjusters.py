from aiogram.types import Message

from deletebot.db.services import adjust


def save_telegram_id(msg: Message) -> None:
    adjust(f"INSERT INTO admins(telegram_id) VALUES ({msg.from_user.id})")


def save_channel_id(msg: Message) -> None:
    adjust(f"INSERT INTO channels(channel_id, admin_id) VALUES ('{msg.text}', (SELECT telegram_id FROM admins "
           f"WHERE telegram_id = {msg.from_user.id}))")


def update_channel_id(msg: Message) -> None:
    adjust(f"UPDATE channels SET channel_id = '{msg.text}' WHERE admin_id = {msg.from_user.id}")
