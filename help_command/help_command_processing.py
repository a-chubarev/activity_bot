from aiogram import types
from services import chat_controls
from administrator_functionality import administrator_database_queries as admin_db


def return_help_text_message_in_group_chat(message: types.Message):
    return_text = 'This bot can:\n1. Call users from the list\n2. Reply to unwanted messages and delete them\n3. ' \
                  'Send a vote for activity in the chat '
    chat_controls.add_or_update_chat_and_user(message)
    if admin_db.return_admin_table_intersection(str(message.from_user.id), str(message.chat.id)) is not None:
        admin_db.update_admin_table_intersection(message)
    else:
        admin_db.add_admin_table_intersection(message)
    return return_text


def return_help_text_message_in_private_chat_without_intersection(message: types.Message):
    return_text = "This bot can:\n1. Call users from the list\n2. Reply to unwanted messages and delete them\n3. " \
                  "Send a vote for activity in the chat. \n I'm sorry, I don't have any information in which chats " \
                  "you are the administrator. Please use the /help command in the group chat to identify "
    return return_text


def return_help_text_message_in_private_chat_with_intersection(message: types.Message):
    """Возвращает текст со списком чатов, где юзер - админ"""
    return_text = 'Chats where you are the administrator:\n'
    chat_controls.add_or_update_user(message)
    chat_list = admin_db.return_all_chat_where_user_is_admin(message.from_user.id)
    for chat in chat_list:
        chat_id = chat[0]
        chat_name = chat[1]
        return_text += f'{chat_id} {chat_name}\n'
    return return_text


def choice_help_text_message(message: types.Message):
    """Выбор какое сообщение вернуть в зависимости от типа чата и наличия связи юзер-админ"""
    if chat_controls.check_chat_is_group(message):
        return return_help_text_message_in_group_chat(message)
    else:
        if admin_db.return_user_is_admin_in_least_chat(message.from_user.id):
            return return_help_text_message_in_private_chat_with_intersection(message)
        else:
            return return_help_text_message_in_private_chat_without_intersection(message)

