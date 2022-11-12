from preferences import bot_change_settings as bot_pref
from aiogram.utils import executor
from preferences.bot_authorization import bot_dp
from aiogram import types
from tag_list import processing_tag_list
from invalid_message import processing_invalid_message

"""Инициализация при запуске"""
bot_pref.initial_check()


@bot_dp.message_handler(commands=['add_self_in_tag_list'])
async def add_user_in_tag_list(message: types.Message):
    await message.reply(processing_tag_list.add_member_in_tag_list(message))


@bot_dp.message_handler(commands=['remove_yourself_from_tag_list'])
async def remove_user_in_tag_list(message: types.Message):
    await message.reply(processing_tag_list.remove_member_from_tag_list(message))


@bot_dp.message_handler(commands=['call_users_from_tag_list'])
async def remove_user_in_tag_list(message: types.Message):
    await message.answer(processing_tag_list.return_tag_list(message), parse_mode='HTML')
    await message.delete()


# TODO: handler: open_keyboard
# TODO: handler: select_activity
# TODO: handler: admin_settings
# TODO: handler: main_keyboard
# TODO: handler: activity_inline_keyboard
# TODO: handler: admin_settings_keyboard
# TODO: handler: exception_message
@bot_dp.message_handler()
async def except_message(message: types.Message):
    reply_message_info = processing_invalid_message.return_invalid_message_reply_info(message)
    if reply_message_info is not None:
        if reply_message_info[0] == '+':
            await message.delete()
            if reply_message_info[1] != '':
                await message.answer(reply_message_info[1])
        else:
            if reply_message_info[1] != '':
                await message.reply(reply_message_info[1])



"""Пропуск сообщений, отправленных при отключенном боте"""
executor.start_polling(bot_dp, skip_updates=True)
