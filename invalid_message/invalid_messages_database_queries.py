import sqlite3

db_path = f'./file_storage/db_storage.db'
member_db = sqlite3.connect(f'{db_path}')
cur = member_db.cursor()


def write_message_template(msg_reply_text: str, msg_del: str, msg_pattern: str):
    """Добавить запись в БД. Записывает шаблон, надо удалять или нет, текст ответа. ID устанавливается автоматически"""
    try:
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
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.invalid_messages_database_queries')


def remove_message_template_by_id(msg_template_id: str):
    """Удаляет запись. Поиск по ID шаблона"""
    try:
        cur.execute(f'''
                        DELETE FROM invalid_message_templates 
                        WHERE invalid_message_templates_id = {msg_template_id}
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.remove_message_template_by_id')


def return_message_template_id_by_pattern(msg_pattern: str):
    """Возвращает ID записи"""
    try:
        cur.execute(f'''
                        SELECT 
                            invalid_message_templates_id
                        FROM 
                            invalid_message_templates 
                        WHERE 
                            message_pattern = "{msg_pattern}"
                ''')
        return cur.fetchone()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_message_template_id_by_pattern')


def return_message_template_reply_text_by_id(msg_template_id: str):
    """Возвращает текст ответа на шаблон по ID записи"""
    try:
        cur.execute(f'''
                        SELECT 
                            reply_text
                        FROM 
                            invalid_message_templates 
                        WHERE 
                            invalid_message_templates_id = "{msg_template_id}"
                    ''')
        return cur.fetchone()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_message_template_reply_text_by_id')


# TODO: нужен метод в invalid_message_db_processing,
#  который будет возвращать булево значение в зависимости от переданного значения
def return_message_delete_confirm_by_id(msg_pattern: str):
    """Возвращает необходимость удаления сообщения юзера по ID записи.
    + для удаляемых сообщений, остальные значения для неудаляемых."""
    try:
        cur.execute(f'''
                        SELECT 
                            will_message_deleted
                        FROM 
                            invalid_message_templates 
                        WHERE 
                            message_pattern = "{msg_pattern}"
                ''')
        return cur.fetchone()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_message_delete_confirm_by_id')


def return_message_template_id_by_pattern_info(msg_reply_text: str, msg_del: str, msg_pattern: str):
    """Возвращает id шаблона по всей инфо из шаблона"""
    try:
        cur.execute(f'''
                        SELECT 
                            invalid_message_templates_id
                        FROM 
                            invalid_message_templates 
                        WHERE 
                            message_pattern = "{msg_pattern}"
                            AND
                            reply_text = "{msg_reply_text}"
                            AND
                            will_message_deleted = "{msg_del}"                                
                    ''')
        return cur.fetchone()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_message_template_id_by_pattern_info')


def return_all_message_pattern_by_id(msg_template_id: str):
    """Возвращает все шаблоны поиска сообщения по ID записи"""
    try:
        cur.execute(f'''
                                SELECT 
                                    message_pattern
                                FROM 
                                    invalid_message_templates 
                                WHERE 
                                    invalid_message_templates_id = "{msg_template_id}"
                ''')
        return cur.fetchone()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_all_message_pattern_by_id')


def return_message_pattern_by_id(msg_template_id: str):
    """Возвращает ПЕРВЫЙ шаблон поиска сообщения по ID записи"""
    try:
        cur.execute(f'''
                                SELECT 
                                    message_pattern
                                FROM 
                                    invalid_message_templates 
                                WHERE 
                                    invalid_message_templates_id = "{msg_template_id}"
                ''')
        return cur.fetchone()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_message_pattern_by_id')



def add_chat_invalid_message_intersection(chat_id: str, msg_pattern: str):
    """Добавляет в сводную таблицу запись исключения"""
    try:
        cur.execute(f'''
                        INSERT INTO invalid_messages (chat_information_id, exception_id)
                        VALUES(
                            (SELECT chat_information_id FROM chat_information WHERE chat_id = "{chat_id}"),
                            (SELECT invalid_message_templates_id FROM invalid_message_templates 
                                                                WHERE message_pattern = "{msg_pattern}")
                            )
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.add_chat_invalid_message_intersection')


def remove_chat_invalid_message_intersection(chat_id: str, msg_pattern: str):
    """Удаляет из сводной таблицы запись исключения"""
    try:
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
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.remove_chat_invalid_message_intersection')


def return_chat_invalid_message_intersection(chat_id: str, msg_pattern: str):
    """Возвращает из сводной таблицы запись исключения"""
    try:
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
        return cur.fetchone()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_chat_invalid_message_intersection')


def return_message_patterns_by_chat_id(chat_id: str):
    """Возвращает все шаблоны и необходимость удаления для исключений по chat_id"""
    try:
        cur.execute(f'''
                        SELECT invalid_message_templates.message_pattern, 
                               invalid_message_templates.will_message_deleted, 
                               invalid_message_templates.reply_text,
                               invalid_message_templates.invalid_message_templates_id
                        FROM invalid_message_templates
                        INNER JOIN invalid_messages ON 
                            invalid_messages.exception_id = invalid_message_templates.invalid_message_templates_id
                        INNER JOIN chat_information ON
                            invalid_messages.chat_information_id = chat_information.chat_information_id
                        WHERE chat_information.chat_id = "{chat_id}"
                    ''')
        return cur.fetchall()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_message_patterns_by_chat_id')


def return_count_intersection_by_chat_id(chat_id: str):
    """Возвращает количество записей из сводной таблицы с chat_id =..."""
    try:
        cur.execute(f'''
                        SELECT COUNT
                            (invalid_messages.chat_information_id)
                        FROM 
                            invalid_messages 
                        INNER JOIN 
                            chat_information ON invalid_messages.chat_information_id = 
                            chat_information.chat_information_id
                        WHERE 
                            chat_information.chat_id = "{chat_id}"
                    ''')
        return cur.fetchone()[0]
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.invalid_message'
              f'.return_count_intersection_by_chat_id')
