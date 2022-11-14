"""В модуле те методы и функции, которые дергаются по несколько раз"""
from aiogram import types
from preferences.bot_authorization import bot
from services import database_controls


def check_chat_is_group(message: types.Message):
    """Check group type. Return True if chat is public, False - if private"""
    if message.chat.type.upper() == 'GROUP' or message.chat.type.upper() == 'SUPERGROUP':
        return True
    else:
        return False


async def check_member_is_admin(message: types.Message):
    """Проверка на наличие админки у юзера, возвращает True/False"""
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if member.status.lower() == 'creator' or member.status.lower() == 'administrator' or \
            member.status.lower() == 'owner':
        return True
    else:
        return False


async def delete_message_from_chat(message: types.Message):
    """Удалить сообщение"""
    await message.delete()


def add_or_update_chat_and_user(message: types.Message):
    """Добавляет или апдейтит инфо о юзере и чате"""
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
    if check_chat_is_group(message):
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


def add_or_update_user(message: types.Message):
    """Создает или апдейтит запись юзера в БД"""
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
