from aiogram import types
from services import chat_controls
from services import database_controls
import tag_list_database_queries as tl_db_queries


def add_member_in_tag_list(message: types.Message):
    """Метод добавляет юзера в тег лист. Если чат не групповой - возвращает сообщение с ошибкой"""
    # Чат групповой?
    if not chat_controls.check_chat_is_group(str(message.chat.type)):
        return 'Tag list is only used in group chats!'
    # Связь юзер/чат в summary есть?
    if not tl_db_queries.return_taglist_intersection(str(message.from_user.id),
                                                     str(message.chat.id)):
        # Пользователь есть?
        if not database_controls.return_user_primary_key(str(message.from_user.id)):
            # Апдейт юзера
            database_controls.update_member_information(str(message.from_user.id),
                                                        str(message.from_user.username),
                                                        str(message.from_user.first_name),
                                                        str(message.from_user.last_name),
                                                        str(message.from_user.is_premium))
        else:
            database_controls.write_member_information(str(message.from_user.id),
                                                       str(message.from_user.username),
                                                       str(message.from_user.first_name),
                                                       str(message.from_user.last_name),
                                                       str(message.from_user.is_premium))
        # Чат есть?
        if not database_controls.return_chat_name(str(message.chat.id)):
            # Апдейт чата
            database_controls.update_chat_information(str(message.chat.id),
                                                      str(message.chat.title),
                                                      str(message.chat.type))
        # Создать чат
        else:
            database_controls.write_chat_information(str(message.chat.id),
                                                     str(message.chat.title),
                                                     str(message.chat.type))
        # Добавить связь в summary
        tl_db_queries.add_taglist_intersection(str(message.from_user.id),
                                               str(message.chat.id))
        return 'User was added in tag list.'
    else:
        return 'The user is already in the list.'


def remove_member_from_tag_list(message: types.Message):
    """Удаляет запись из сводной таблицы tag_list. Не удаляет запись чата и юзера из соответствующих таблиц"""
    # Чат групповой?
    if not chat_controls.check_chat_is_group(str(message.chat.type)):
        return 'Tag list is only used in group chats!'
    # Апдейт юзера
    database_controls.update_member_information(str(message.from_user.id),
                                                str(message.from_user.username),
                                                str(message.from_user.first_name),
                                                str(message.from_user.last_name),
                                                str(message.from_user.is_premium))
    # Апдейт чата
    database_controls.update_chat_information(str(message.chat.id),
                                              str(message.chat.title),
                                              str(message.chat.type))
    # Проверить наличие связи юзер-чат
    if tl_db_queries.return_taglist_intersection(str(message.from_user.id),
                                                 str(message.chat.id)) is not False:
        # Удаление связи
        tl_db_queries.remove_taglist_intersection(str(message.from_user.id),
                                                  str(message.chat.id))
        return 'User removed from tag list.'
    else:
        return 'User is not in the tag list'


def return_tag_list(message: types.Message):
    """Метод возвращает тег лист для чата. Если у юзера username == none возвращает firstname"""
    # Чат групповой?
    if not chat_controls.check_chat_is_group(message.chat.type):
        return 'Tag list is only used in group chats!'
    # Связь чат-юзер есть?
    if tl_db_queries.return_taglist_intersection(str(message.from_user.id),
                                                 str(message.chat.id)) is not False:
        # Получить всех пользователей
        if tl_db_queries.return_full_tag_list(str(message.from_user.id),
                                              str(message.chat.id)) == '':
            return 'Only you in tag list.'
        else:
            return tl_db_queries.return_full_tag_list(str(message.from_user.id),
                                                      str(message.chat.id))
    else:
        return 'Only users from tag list can call users'
