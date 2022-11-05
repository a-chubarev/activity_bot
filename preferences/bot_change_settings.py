import os
import configparser

preferences_path = '../file_storage/bot preferences.ini'


# возвращает True если есть файл с настройками бота
def checking_preferences_file(pref_path):
    file_availability = os.path.isfile(preferences_path)
    return file_availability


# Вывод сообщения если файл настроек не создан
def return_first_launch_message(pref_path):
    if not checking_preferences_file(pref_path):
        first_launch_text = "Greetings, at the next step, enter the necessary " \
                            "information about the bot for further work"
        return first_launch_text


# Создание ini файла с шаблоном настроек бота
def create_preferences_file(pref_path):
    config = configparser.ConfigParser()
    config.add_section('Preferences')
    config.set('Preferences', 'Name', '')
    config.set('Preferences', 'Token', '')
    with open(pref_path, 'w') as config_file: config.write(config_file)


# Записать имя бота в файл конфигурации
def write_bot_name(pref_path):
    config = configparser.ConfigParser()
    if not checking_preferences_file(pref_path):
        create_preferences_file(pref_path)
    bot_name = input('Enter the name of the bot: ')
    config.set('Preferences', 'Name', f'{bot_name}')
    with open(pref_path, 'w') as config_file: config.write(config_file)


# Записать токен бота в файл конфигурации
def write_bot_token(pref_path):
    config = configparser.ConfigParser()
    if not checking_preferences_file(pref_path):
        create_preferences_file(pref_path)
    bot_token = input('Enter the bot token: ')
    config.set('Preferences', 'Token', f'{bot_token}')
    with open(pref_path, 'w') as config_file: config.write(config_file)
    pass


def return_bot_name(pref_path):
    config = configparser.ConfigParser()
    if checking_preferences_file(pref_path):
        bot_name = config.get('Preferences', 'Name')
        if bot_name != '':
            return bot_name
        else:
            return 'The bot name is not set'
    else:
        return 'Something went wrong: preferences file not exist!'


def return_bot_token(pref_path):
    config = configparser.ConfigParser()
    if checking_preferences_file(pref_path):
        bot_token = config.get('Preferences', 'Token')
        if bot_token != '':
            return bot_token
        else:
            return 'The bot token is not set'
    else:
        return 'Something went wrong: preferences file not exist!'


# Возвращает приветственное сообщение с именем бота если существует файл конфигурации
def return_welcome_message():
    if checking_preferences_file(preferences_path):
        bot_name = return_bot_name(preferences_path)
        welcome_text = f'Welcome to {bot_name}!'
    return welcome_text


print(checking_preferences_file())
create_preferences_file(preferences_path)
