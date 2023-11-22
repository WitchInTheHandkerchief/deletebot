from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

token = config('TOKEN_API')

bot = Bot(token)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)