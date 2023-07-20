from aiogram.fsm.state import StatesGroup, State


class FormStatesGroup(StatesGroup):
    handle_from = State()
    handle_to = State()
    handle_world = State()
