from aiogram.utils import executor

from deletebot import handlers
from deletebot.config import dp
from deletebot.utils import init_db

if __name__ == '__main__':
    init_db()
    handlers.setup(dp)
    executor.start_polling(dp)
