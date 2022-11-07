import aiogram
from preferences import bot_change_settings as bot_pref

# Присвоили токен переменной
token = bot_pref.return_bot_token(bot_pref.preferences_path)
# Создал экземпляр бота
bot = aiogram.Bot(token)
# Создал экземпляр диспетчера
bot_dp = aiogram.Dispatcher(bot)
