from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    idMessage = State()
    updateID = State()
    channelMessage = State()
