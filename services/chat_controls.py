"""В модуле те методы и функции, которые дергаются по несколько раз"""
from aiogram import types
from preferences.bot_authorization import bot


def check_chat_is_group(chat_type: str):
    """Check group type. Return True if chat is public, False - if private"""
    return chat_type.upper() == 'GROUP' or chat_type.upper() == 'SUPERGROUP'


async def check_member_is_admin(message: types.Message):
    """Проверка на наличие админки у юзера, возвращает True/False"""
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return member.status.lower() == 'creator' or member.status.lower() == 'administrator' or \
                                    member.status.lower() == 'owner'
