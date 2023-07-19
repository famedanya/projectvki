from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.handlers import message

from aiogram.types import Message, CallbackQuery
from translate import Translator

from callbacks.form import LangCallbackData

tran_router = Router()


# translator = Translator(from_lang='Russian', to_lang='English')


@tran_router.message(Command('translate'))
async def handle_translate(message: Message):
    await message.answer('Напиши код языка на который нужно перевести слово.')


@tran_router.callback_query(F.text, LangCallbackData.filter())
async def handle_lang(query: CallbackQuery, callback_data: LangCallbackData):
    # await query.message.answer('На какой язык вы хотите перевести?',
    #                            reply_markup=en_rus_keyboard)
    if callback_data.from_lang == 'en':
        translator = Translator(from_lang='English', to_lang='Russian')
    else:
        translator = Translator(from_lang='Russian', to_lang='English')

    text = translator.translate(query.message.text)
    await query.message.answer(text)

# @tran_router.message(F.text)
# async def trans_name(message: Message):
#     if callback_data.from_lang == 'en':
#         ...
#
#     text_eng = translator.translate(message.text)
#     await message.answer(text_eng)
