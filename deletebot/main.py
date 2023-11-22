from aiogram.utils import executor

from deletebot.config import dp

if __name__ == '__main__':
    executor.start_polling(dp)
