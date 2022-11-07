import sqlite3

db_path = f'../file_storage/db_storage.db'
member_db = sqlite3.connect(f'{db_path}')
cur = member_db.cursor()


# TODO: добавить строку с шаблоном
def add_message_pattern(message_pattern, reply_text, del_message):
    cur.execute(f'''
                    INSERT INTO "invalid message templates" ("message pattern", "reply text", "will message deleted")
                    VALUES ("{message_pattern}", "{reply_text}", "{del_message}")
                    ''')
    member_db.commit()


# TODO: изменить строку с шаблоном
def update_message_pattern():
    pass


# TODO: удалить строку с шаблоном
def delete_message_pattern():
    pass


# TODO: вернуть id шаблона
def return_uuid_message_pattern():
    pass


# TODO: вернуть текст шаблона
def return_reply_message_pattern():
    pass


# TODO: вернуть шаблон
def return_message_pattern():
    pass


# TODO: вернуть необходимость удаления сообщения
def return_was_deleted_message_pattern():
    pass


# TODO: добавить пересечение в сводную таблицу
# TODO: удалить пересечение из сводной таблицы
# TODO: вернуть пересечение из сводной таблицы
