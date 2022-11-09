import sqlite3

db_path = f'../file_storage/db_storage.db'
member_db = sqlite3.connect(f'{db_path}')
cur = member_db.cursor()


def write_message_template(msg_reply_text: str, msg_del: str, msg_pattern: str):
    """Добавить запись в БД. Записывает шаблон, надо удалять или нет, текст ответа. ID устанавливается автоматически"""
    cur.execute(f'''
                        INSERT INTO invalid_message_templates 
                               (message_pattern, 
                               reply_text, 
                               will_message_deleted)
                        VALUES ("{msg_pattern}", 
                                "{msg_reply_text}", 
                                "{msg_del}")
                        ''')
    member_db.commit()


def remove_message_template_by_id(msg_template_id: str):
    """Удаляет запись. Поиск по ID шаблона"""
    cur.execute(f'''
                            DELETE FROM invalid_message_templates 
                            WHERE invalid_message_templates_id = {msg_template_id}
                            ''')
    member_db.commit()


def return_message_template_id_by_pattern(msg_pattern: str):
    """Возвращает ID записи"""
    cur.execute(f'''
                            SELECT 
                                invalid_message_templates_id
                            FROM 
                                invalid_message_templates 
                            WHERE 
                                message_pattern = "{msg_pattern}"
            ''')
    member_db.commit()
    return cur.fetchone()


def return_message_template_reply_text_by_id(msg_template_id: str):
    """Возвращает текст ответа на шаблон по ID записи"""
    cur.execute(f'''
                            SELECT 
                                reply_text
                            FROM 
                                invalid_message_templates 
                            WHERE 
                                invalid_message_templates_id = "{msg_template_id}"
            ''')
    member_db.commit()
    return cur.fetchone()


# TODO: нужен метод в invalid_message_db_processing,
#  который будет возвращать булево значение в зависимости от переданного значения
def return_message_delete_confirm_by_id(msg_pattern: str):
    """Возвращает необходимость удаления сообщения юзера по ID записи.
    + для удаляемых сообщений, остальные значения для неудаляемых."""
    cur.execute(f'''
                            SELECT 
                                will_message_deleted
                            FROM 
                                invalid_message_templates 
                            WHERE 
                                message_pattern = "{msg_pattern}"
            ''')
    member_db.commit()
    return cur.fetchone()


def return_message_pattern_by_id(msg_pattern: str):
    """Возвращает шаблон поиска сообщения по ID записи"""
    cur.execute(f'''
                            SELECT 
                                message_pattern
                            FROM 
                                invalid_message_templates 
                            WHERE 
                                message_pattern = "{msg_pattern}"
            ''')
    member_db.commit()
    return cur.fetchone()


def add_chat_invalid_message_intersection(chat_id: str, msg_pattern: str):
    """Добавляет в сводную таблицу запись исключения"""
    cur.execute(f'''
                        INSERT INTO invalid_messages (chat_information_id, exception_id)
                        VALUES(
                            (SELECT chat_information_id FROM chat_information WHERE chat_id = "{chat_id}"),
                            (SELECT invalid_message_templates_id FROM invalid_message_templates 
                                                                WHERE message_pattern = "{msg_pattern}")
                            )
            ''')
    member_db.commit()


def remove_chat_invalid_message_intersection(chat_id: str, msg_pattern: str):
    """Удаляет из сводной таблицы запись исключения"""
    cur.execute(f'''
                    DELETE FROM invalid_messages 
                    WHERE(
                        (SELECT chat_information_id FROM chat_information WHERE chat_id = "{chat_id}")
                            = chat_information_id 
                    AND
                        (SELECT invalid_message_templates_id FROM invalid_message_templates 
                                                                WHERE message_pattern = "{msg_pattern}")
                            = exception_id
                            )     
            ''')
    member_db.commit()


def return_chat_invalid_message_intersection(chat_id: str, msg_pattern: str):
    """Возвращает из сводной таблицы запись исключения"""
    cur.execute(f'''
                    SELECT * FROM invalid_messages 
                    WHERE(
                        (SELECT chat_information_id FROM chat_information WHERE chat_id = "{chat_id}")
                            = chat_information_id 
                    AND
                        (SELECT invalid_message_templates_id FROM invalid_message_templates 
                                                                WHERE message_pattern = "{msg_pattern}")
                            = exception_id
                            )     
            ''')
    member_db.commit()
    return cur.fetchone()
