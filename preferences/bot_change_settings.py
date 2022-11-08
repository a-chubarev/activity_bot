import os
import configparser

preferences_path = './file_storage/bot preferences.ini'


def checking_preferences_file(pref_path):
    """Возвращает True если есть файл с настройками бота"""
    file_availability = os.path.isfile(pref_path)
    return file_availability


def return_first_launch_message():
    """Вывод сообщения если файл настроек не создан"""
    first_launch_text = "At the next step, enter the necessary information about the bot for further work"
    return first_launch_text


def create_preferences_file(pref_path):
    """Создание ini файла с шаблоном настроек бота"""
    config = configparser.ConfigParser()
    config.add_section('Preferences')
    config.set('Preferences', 'Name', '')
    config.set('Preferences', 'Token', '')
    with open(pref_path, 'w') as config_file:
        config.write(config_file)


def write_bot_name(pref_path):
    """Записать имя бота в файл конфигурации"""
    config = configparser.ConfigParser()
    if not checking_preferences_file(pref_path):
        create_preferences_file(pref_path)
    config.read(pref_path)
    bot_name = input('Enter the name of the bot: ')
    config.set('Preferences', 'Name', f'{bot_name}')
    with open(pref_path, 'w') as config_file:
        config.write(config_file)


def write_bot_token(pref_path):
    """Записать токен бота в файл конфигурации"""
    config = configparser.ConfigParser()
    if not checking_preferences_file(pref_path):
        create_preferences_file(pref_path)
    config.read(pref_path)
    bot_token = input('Enter the bot token: ')
    config.set('Preferences', 'Token', f'{bot_token}')
    with open(pref_path, 'w') as config_file:
        config.write(config_file)
    pass


def return_bot_name(pref_path):
    """Возвращает имя бота"""
    config = configparser.ConfigParser()
    if checking_preferences_file(pref_path):
        config.read(pref_path)
        bot_name = config.get('Preferences', 'Name')
        if bot_name != '':
            return bot_name
        else:
            return 'The bot name is not set'
    else:
        return 'Something went wrong: preferences file not exist!'


def return_bot_token(pref_path):
    """Возвращает токен"""
    config = configparser.ConfigParser()
    if checking_preferences_file(pref_path):
        config.read(pref_path)
        bot_token = config.get('Preferences', 'Token')
        if bot_token != '':
            return bot_token
        else:
            return 'The bot token is not set'
    else:
        return 'Something went wrong: preferences file not exist!'


def change_bot_config(pref_path):
    """Изменение конфига бота"""
    print(return_first_launch_message())
    write_bot_name(pref_path)
    write_bot_token(pref_path)


def return_welcome_message(pref_file):
    """Возвращает приветственное сообщение с именем бота если существует файл конфигурации"""
    if checking_preferences_file(pref_file):
        bot_name = return_bot_name(pref_file)
        bot_token = return_bot_token(pref_file)
        welcome_text = f'Welcome to {bot_name}! \n' \
                       f'Bot token: {bot_token}'
        return welcome_text


def checking_agreement_with_configuration():
    """Проверяет согласие юзера с выбранным конфигом бота"""
    print('Are you agreement with the bot configuration?')
    user_input = input('y - yes/ n - no: ')
    if user_input == 'у' or user_input == 'Y' or user_input == 'y' or user_input == 'e' or user_input == 'E' or \
            user_input == 'н' or user_input == 'Н' or user_input == 'У':
        return False
    else:
        return True


def initial_check():
    """Проверка настроек и изменение при запуске"""
    # TODO: по идее надо переписывать логику
    if not checking_preferences_file(preferences_path):
        create_preferences_file(preferences_path)
        change_bot_config(preferences_path)
    print(return_welcome_message(preferences_path))
    x = checking_agreement_with_configuration()
    if x:
        change_bot_config(preferences_path)
    else:
        print('Start')
