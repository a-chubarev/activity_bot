import sqlite3
from aiogram import types
from invalid_message import invalid_messages_database_queries as inv_db_queries
import services.chat_controls
from services import controls
import re


def return_message_template_match(msg_reply_text: str,
                                  msg_del: str,
                                  msg_pattern: str):
    # TODO: надо подумать над логикой, не уверен что это правильное решение
    """Возвращает true/false в зависимости от полного совпадения данных"""
    invalid_message_template = inv_db_queries.return_message_template_id_by_pattern_info(msg_reply_text,
                                                                                         msg_del,
                                                                                         msg_pattern)
    if type(invalid_message_template) is list and controls.is_int(invalid_message_template[0]):
        return True
    else:
        return False


def return_message_delete_confirm(symbol: str):
    """Возвращает true/false в зависимости от переданного значения (+ / остальные символы)"""
    if symbol == '+':
        return True
    else:
        return False


# TODO: проверить на действие
def select_invalid_message_command(message: types.Message):
    """Выбор команды для обработки шаблона"""
    # Добавить шаблон
    if message.text.strip().startswith('#msg_temp#add'):
        # Проверяем на валидность шаблона:
        """$excp = sadhjk $rm = stop spam! $delm = y"""
        if re.match(r'[#msg_temp]\s*[#del]\s*[$excp]\s*[\w|\W]*\s*[$rmsg]\s*[\w|\W]*\s*[$delm]\s*[\w|\W]*') is not None:
            pass
            # TODO: получить наличие шаблона
            # TODO: удалить связь
        else:
            return 'Check if the template is correct.'
    else:
        return 'Please, check the correctness of the command.'

    # Удалить шаблон
    if message.text.strip().startswith('#msg_temp#del'):
        pass


# TODO: проверка на шаблон
def return_template_is_correct(message: types.Message):
    """Метод проверяет текст на совпадение с шаблоном"""
    pass


# TODO: добавить шаблон
# TODO: вернуть шаблоны
# TODO: сформировать шаблоны в сообщение
# TODO: удалить шаблон
# TODO: добавить шаблон
# TODO: вернуть счетчик шаблонов для чата
# TODO: вернуть шаблон в чат


def return_invalid_message_reply_info(message: types.Message):
    """Возвращает список с необходимостью удаления сообщения и текстом ответа на невалидное сообщение"""
    message_pattern = inv_db_queries.return_message_patterns_by_chat_id(message.chat.id)
    message_text = message.text
    answer_data_list = []
    for elements in message_pattern:
        pattern = elements[0]
        will_message_deleted = elements[1]
        reply_text = elements[2]
        message_text = message_text.lower()
        pattern = pattern.lower()
        if elements is not None:
            if message_text.find(pattern) != -1:
                answer_data_list.append(will_message_deleted)
                answer_data_list.append(reply_text)
                return answer_data_list
            if message_text.replace(' ', '').find(pattern) != -1:
                answer_data_list.append(will_message_deleted)
                answer_data_list.append(reply_text)
                return answer_data_list


def return_invalid_message_intersection(message: types.Message):
    """Возвращает true/false в зависимости от найденных пересечений в сводной таблице шаблонов невалидных сообщений"""
    if int(inv_db_queries.return_count_intersection_by_chat_id(str(message.chat.id))) > 0:
        return True
    else:
        return False



"""def message_from_chat_processing(message: types.Message):
    if services.chat_controls.check_chat_is_group(message.chat.type) and return_invalid_message_intersection(message):
        message_reply_info = return_invalid_message_reply_info(message)
        if message_reply_info is not None:"""


