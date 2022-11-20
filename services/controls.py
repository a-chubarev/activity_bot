from aiogram import types
import sqlite3


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


def print_exception_error(exception_name, exception_type, method_name):
    print(f'Exception: {exception_name}; Type: {exception_type}; Method: {method_name}')
