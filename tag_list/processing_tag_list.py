from aiogram import types
from services import chat_controls
from services import database_controls
import tag_list.tag_list_database_queries as tl_db_queries



def add_member_in_tag_list(message: types.Message):
    """Метод добавляет юзера в тег лист. Возвращает сообщение, если связь юзер-чат есть. Апдейтит инфо о чате и
    юзере. """
    # Чат не групповой
    if not chat_controls.check_chat_is_group(str(message.chat.type)):
        return 'Tag list is only used in group chats!'
    # Чат групповой
    # Связи по таблице тег листа нет
    if not tl_db_queries.return_taglist_intersection(str(message.from_user.id),
                                                     str(message.chat.id)):
        # Юзера нет
        if not database_controls.return_user_lastname(str(message.from_user.id)):
            database_controls.write_member_information(str(message.from_user.id),
                                                       str(message.from_user.username),
                                                       str(message.from_user.first_name),
                                                       str(message.from_user.last_name),
                                                       str(message.from_user.is_premium))
        # Юзер есть
        else:
            database_controls.update_member_information(str(message.from_user.id),
                                                        str(message.from_user.username),
                                                        str(message.from_user.first_name),
                                                        str(message.from_user.last_name),
                                                        str(message.from_user.is_premium))
        # Чата нет
        if not database_controls.return_chat_name(str(message.chat.id)):
            database_controls.write_chat_information(str(message.chat.id),
                                                     str(message.chat.title),
                                                     str(message.chat.type))
        # Чат есть
        else:
            database_controls.update_chat_information(str(message.chat.id),
                                                      str(message.chat.title),
                                                      str(message.chat.type))
        # Создать связь
        tl_db_queries.add_taglist_intersection(str(message.from_user.id),
                                               str(message.chat.id))
        return 'User was added in tag list.'
    # Связь по тег листу есть
    else:
        database_controls.update_member_information(str(message.from_user.id),
                                                    str(message.from_user.username),
                                                    str(message.from_user.first_name),
                                                    str(message.from_user.last_name),
                                                    str(message.from_user.is_premium))
        database_controls.update_chat_information(str(message.chat.id),
                                                  str(message.chat.title),
                                                  str(message.chat.type))
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
