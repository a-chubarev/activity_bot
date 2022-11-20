import sqlite3

from services import database_controls
from aiogram import type


db_path = f'./file_storage/db_storage.db'
member_db = sqlite3.connect(f'{db_path}')
cur = member_db.cursor()


def add_admin_table_intersection(message: types.Message, user_is_admin=False):
    """Добавить запись в сводную таблицу тег листа с PK чата, юзера, отметкой админ или нет"""
    user_pk = database_controls.return_user_primary_key(str(message.from_user.id))[0]
    chat_pk = database_controls.return_chat_primary_key(str(message.chat.id))[0]
    if user_is_admin:
        # chat_controls.check_member_is_admin(message):
        user_is_admin = '+'
    else:
        user_is_admin = '-'
    try:
        cur.execute(f'''
                        INSERT INTO user_is_admin (members_information_id, chat_information_id, user_admin)
                        VALUES ("{user_pk}", "{chat_pk}", "{user_is_admin}")
        ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: administrator_functionality'
              f'.administrator_database_queries.add_admin_table_intersection')


def remove_admin_table_intersection(message: types.Message):
    """Удаляет запись из сводной таблицы админов"""
    user_pk = database_controls.return_user_primary_key(message.from_user.id)[0]
    chat_pk = database_controls.return_chat_primary_key(message.chat.id)[0]
    try:
        cur.execute(f'''
                        DELETE FROM 
                            user_is_admin 
                        WHERE
                            "chat_information_id" = "{chat_pk}" 
                            AND
                            "members_information_id" = "{user_pk}"
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: administrator_functionality'
              f'.administrator_database_queries.remove_admin_table_intersection')


def return_admin_table_intersection(user_id: str,
                                    chat_id: str):
    """Проверяет и возвращает chat information id, members information id если есть запись в сводной таблице.
        Возвращает None если нет записи"""
    user_pk = database_controls.return_user_primary_key(user_id)[0]
    chat_pk = database_controls.return_chat_primary_key(chat_id)[0]
    try:
        cur.execute(f'''
                        SELECT members_information_id, chat_information_id, user_admin
                        FROM user_is_admin
                        WHERE members_information_id = "{user_pk}" AND 
                              chat_information_id = "{chat_pk}" 
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return None
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: administrator_functionality'
              f'.administrator_database_queries.return_admin_table_intersection')



def return_all_chat_where_user_is_admin(user_id: str):
    """Возвращает все chat_id, chat_name, где юзер - админ"""
    try:
        cur.execute(f'''
                        SELECT 
                            chat_information.chat_id, chat_information.chat_name
                        FROM
                            chat_information
                        INNER JOIN user_is_admin ON user_is_admin.chat_information_id =
                                                       chat_information.chat_information_id
                        INNER JOIN members_information ON members_information.members_information_id = 
                                                          user_is_admin.members_information_id
                        WHERE
                            members_information.user_id = "{user_id}"
                        AND 
                            user_is_admin.user_admin = "+"
                            
                    ''')
        result = cur.fetchall()
        if result is not None:
            return result
        else:
            return None
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: administrator_functionality'
              f'.administrator_database_queries.return_all_chat_where_user_is_admin')


def update_admin_table_intersection(message: types.Message, user_is_admin=True):
    """Апдейт инфо об админке юзера"""
    user_pk = database_controls.return_user_primary_key(message.from_user.id)[0]
    chat_pk = database_controls.return_chat_primary_key(message.chat.id)[0]
    #if user_is_admin:
    # TODO: я хуй пойми че тут должно быть
    if services.chat_controls.check_member_is_admin(message):
        user_admin = '+'
    else:
        user_admin = '-'
    try:
        cur.execute(f'''
                        UPDATE 
                            user_is_admin
                        SET
                            user_admin = "{user_admin}"
                        WHERE
                            user_is_admin.members_information_id = "{user_pk}"
                        AND 
                            user_is_admin.chat_information_id = "{chat_pk}"
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: administrator_functionality'
              f'.administrator_database_queries.update_admin_table_intersection')



def return_user_is_admin_in_least_chat(user_id: str):
    """Возвращает true если юзер - админ хоть в одном чате"""
    try:
        cur.execute(f'''
                        SELECT 
                            chat_information.chat_id
                        FROM
                            chat_information
                        INNER JOIN user_is_admin ON user_is_admin.chat_information_id =
                                                       chat_information.chat_information_id
                        INNER JOIN members_information ON members_information.members_information_id = 
                                                          user_is_admin.members_information_id
                        WHERE
                            members_information.user_id = "{user_id}"
                        AND 
                            user_is_admin.user_admin = "+"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return True
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: administrator_functionality'
              f'.administrator_database_queries.return_user_is_admin_in_least_chat')
