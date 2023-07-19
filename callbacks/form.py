from aiogram.filters.callback_data import CallbackData


class LangCallbackData(CallbackData, prefix='lang'):
    from_lang: str
    to_lang: str

