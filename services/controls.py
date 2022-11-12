from aiogram import types


def is_int(x):
    """Возвращает true - если целочисленное, false для всех остальных значений"""
    try:
        int(x)
        return True
    except ValueError:
        return False


# TODO: дописать условие для шаблона
def select_message_action(message: types.Message):
    """Выбрать действие для сообщения.
    #msg_temp - шаблон для действия с сообщением"""
    if message.text.strip().startswith('#'):
        pass
