from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


common_router = Router()


@common_router.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text='Привет, это бот переводчик, тебе нужно написать мне код языка\n'
                              'на который нужно перевести текст, вот основные коды:\n'
                              'ru - Русский\n'
                              'en - Английский\n'
                              'es - Испанский\n'
                              'pt - Португальский\n'
                              'zh- Китайский\n'
                              'Вот ссылка со всеми кодами:https://ru.wikipedia.org/wiki/Коды_языков\n'
                              'Для начала введите команду\n /translate')
