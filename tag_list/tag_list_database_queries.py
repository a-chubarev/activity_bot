import sqlite3
from services import database_controls

db_path = f'./file_storage/db_storage.db'
member_db = sqlite3.connect(f'{db_path}')
cur = member_db.cursor()


def add_taglist_intersection(user_id: str, chat_id: str):
    """Добавить запись в сводную таблицу тег листа с PK чата, юзера"""
    user_pk = database_controls.return_user_primary_key(user_id)
    if user_pk is not False:
        user_pk = user_pk[0]
    else:
        user_pk = user_pk
    chat_pk = database_controls.return_chat_primary_key(chat_id)
    if chat_pk is not False:
        chat_pk = chat_pk[0]
    else:
        chat_pk = chat_pk
    try:
        cur.execute(f'''
                        INSERT INTO tag_list (chat_information_id, members_information_id)
                        VALUES ("{chat_pk}", "{user_pk}")
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.tag_list_database_queries'
              f'.add_taglist_intersection')


def remove_taglist_intersection(user_id: str, chat_id: str):
    """Удаляет запись из сводной таблицы тег листа"""
    user_pk = database_controls.return_user_primary_key(user_id)
    if user_pk is not False:
        user_pk = user_pk[0]
    else:
        user_pk = user_pk
    chat_pk = database_controls.return_chat_primary_key(chat_id)
    if chat_pk is not False:
        chat_pk = chat_pk[0]
    else:
        chat_pk = chat_pk
    try:
        cur.execute(f'''
                        DELETE FROM 
                            "tag_list" 
                        WHERE
                            "chat_information_id" = "{chat_pk}" 
                        AND
                            "members_information_id" = "{user_pk}"
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.tag_list_database_queries'
              f'.remove_taglist_intersection')


def return_taglist_intersection(user_id: str, chat_id: str):
    """Проверяет и возвращает chat information id, members information id если есть запись в сводной таблице.
    Возвращает False если нет записи"""
    try:
        cur.execute(f'''
                        SELECT tag_list.members_information_id, tag_list.chat_information_id
                        FROM members_information
                        INNER JOIN tag_list ON members_information.members_information_id = 
                                                                tag_list.members_information_id
                        INNER JOIN chat_information ON chat_information.chat_information_id =
                                                                tag_list.chat_information_id
                        WHERE chat_information.chat_id = "{chat_id}" AND 
                              members_information.user_id = "{user_id}" 
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.tag_list_database_queries'
              f'.return_taglist_intersection')


def return_full_tag_list(user_id: str, chat_id: str):
    """Метод возвращает всех пользователей из тег-листа кроме пользователя, переданного в user_id"""
    try:
        cur.execute(f'''
                        SELECT members_information.user_nickname, 
                               members_information.user_first_name,
                               members_information.user_id,
                               members_information.user_last_name
                        FROM members_information
                        INNER JOIN tag_list ON members_information.members_information_id = 
                                                                tag_list.members_information_id
                        INNER JOIN chat_information ON chat_information.chat_information_id =
                                                                tag_list.chat_information_id
                        WHERE chat_information.chat_id = "{chat_id}" 
                    ''')
        result = cur.fetchall()
        user_list = ''
        for user_information in result:
            if user_information[2] == user_id:
                continue
            else:
                if user_information[0] != 'None':
                    user_list += f'@{user_information[0]}\n'
                else:
                    user_list += f'<a href="tg://user?id={user_information[2]}">' \
                                 f'{user_information[1]} {user_information[3]}</a>'
        return user_list
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: tag_list.tag_list_database_queries'
              f'.return_full_tag_list')
