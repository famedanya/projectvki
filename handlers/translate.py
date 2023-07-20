from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from aiogram.types import Message
from translate import Translator

from states.form import FormStatesGroup

tran_router = Router()


@tran_router.message(Command('translate'))
async def handle_translate(message: Message, state: FSMContext):
    lang_from_message = message.text
    await state.update_data(lang=lang_from_message)
    await state.update_data()
    await message.answer('С какого языка переводить?')
    await state.set_state(FormStatesGroup.handle_from)


@tran_router.message(StateFilter(FormStatesGroup.handle_from))
async def handle_en(message: Message, state: FSMContext):
    lang_from_message = message.text
    await state.update_data(lang_from=lang_from_message)
    await message.answer('Хорошо, а теперь введите язык на который будем переводить.')
    await state.set_state(FormStatesGroup.handle_to)


@tran_router.message(StateFilter(FormStatesGroup.handle_to))
async def handle_wrld(message: Message, state: FSMContext):
    lang_to_message = message.text
    await state.update_data(lang_to=lang_to_message)
    await message.answer('Теперь введите ваше слово.')
    await state.set_state(FormStatesGroup.handle_world)


@tran_router.message(StateFilter(FormStatesGroup.handle_world))
async def handle_word(message: Message, state: FSMContext):
    state_data = await state.get_data()

    lang_from = state_data['lang_from']
    lang_to = state_data['lang_to']
    translator = Translator(from_lang=lang_from, to_lang=lang_to)
    text = translator.translate(message.text)
    await message.answer(text)


