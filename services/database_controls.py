import sqlite3

db_path = f'./file_storage/db_storage.db'
member_db = sqlite3.connect(f'{db_path}')
cur = member_db.cursor()


def write_member_information(user_id: str, nickname: str, firstname: str, lastname: str, premium: str):
    """Создать запись в БД с информацией о юзере"""
    try:
        cur.execute(f'''
                        INSERT INTO members_information (user_id, user_nickname, user_first_name, 
                        user_last_name, user_is_premium)
                        VALUES ("{user_id}", "{nickname}", "{firstname}", "{lastname}", "{premium}")
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.write_member_information')


def update_member_information(user_id: str, nickname: str, firstname: str, lastname: str, premium: str):
    """Обновить запись в БД с информацией о юзере"""
    try:
        cur.execute(f'''
                        UPDATE members_information 
                        SET
                            user_nickname = "{nickname}",
                            user_first_name = "{firstname}",
                            user_last_name = "{lastname}",
                            user_is_premium = "{premium}"
                        WHERE
                            user_id = "{user_id}"
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.update_member_information')


def return_member_information_by_userid(user_id: str):
    """Вернуть запись с информацией о юзере из БД по user id"""
    try:
        cur.execute(f'''
                        SELECT user_id, user_nickname, user_first_name, user_last_name, user_is_premium
                        FROM members_information 
                        WHERE user_id = "{user_id}"
                    ''')
        return cur.fetchone()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_member_information_by_userid')


def return_member_information_by_primary_key(member_inf_id: str):
    """Вернуть запись с информацией о юзере из БД по PK таблицы"""
    try:
        cur.execute(f'''
                        SELECT user_id, user_nickname, user_first_name, user_last_name, user_is_premium
                        FROM members_information 
                        WHERE members_information_id = "{member_inf_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_member_information_by_primary_key')



def return_user_id_by_primary_key(member_inf_id: str):
    """Вернуть user id из БД по PK таблицы"""
    try:
        cur.execute(f'''
                        SELECT user_id
                        FROM members_information 
                        WHERE members_information_id = "{member_inf_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_user_id_by_primary_key')



def return_user_nickname(user_id: str):
    """Вернуть никнейм из БД по user id"""
    try:
        cur.execute(f'''
                        SELECT user_nickname
                        FROM members_information 
                        WHERE user_id = "{user_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_user_nickname')



def return_user_firstname(user_id: str):
    """Вернуть имя из БД по user id"""
    try:
        cur.execute(f'''
                        SELECT user_first_name
                        FROM members_information 
                        WHERE user_id = "{user_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_user_firstname')



def return_user_lastname(user_id: str):
    """Вернуть фамилию из БД по user id"""
    try:
        cur.execute(f'''
                        SELECT user_last_name
                        FROM members_information
                        WHERE user_id = "{user_id}"
                ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_user_lastname')



def return_user_is_premium(user_id: str):
    """Вернуть статус прем акка юзера по user id"""
    try:
        cur.execute(f'''
                        SELECT user_is_premium
                        FROM members_information 
                        WHERE user_id = "{user_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_user_is_premium')



def return_user_primary_key(user_id: str):
    """Вернуть id записи юзера по user id"""
    try:
        cur.execute(f'''
                        SELECT members_information_id
                        FROM members_information 
                        WHERE user_id = "{user_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_user_primary_key')


def write_chat_information(chat_id: str, chat_name: str, chat_type: str):
    """Создать запись в БД с информацией о чате"""
    try:
        cur.execute(f'''
                        INSERT INTO chat_information (chat_id, chat_name, chat_type)
                        VALUES ("{chat_id}", "{chat_name}", "{chat_type}")
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.write_chat_information')


def update_chat_information(chat_id: str, chat_name: str, chat_type: str):
    """Обновить запись в БД с информацией о чате"""
    try:
        cur.execute(f'''
                        UPDATE chat_information 
                        SET
                            chat_name = "{chat_name}",
                            chat_type = "{chat_type}"
                        WHERE
                            chat_id = "{chat_id}"
                    ''')
        member_db.commit()
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.update_chat_information')


def return_chat_primary_key(chat_id: str):
    """Возвращает id записи о чате из БД (Primary key)"""
    try:
        cur.execute(f'''
                        SELECT chat_information_id
                        FROM chat_information 
                        WHERE chat_id = "{chat_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_chat_primary_key')


def return_chat_id_by_primary_key(chat_pk: str):
    """Возвращает id чата из БД по Primary key"""
    try:
        cur.execute(f'''
                        SELECT chat_id
                        FROM chat_information
                        WHERE chat_information_id = "{chat_pk}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_chat_id_by_primary_key')


def return_chat_type(chat_id: str):
    """Возвращает id чата из БД по chat_id"""
    try:
        cur.execute(f'''
                        SELECT chat_type
                        FROM chat_information 
                        WHERE chat_id = "{chat_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_chat_type')


def return_chat_name(chat_id: str):
    """Возвращает имя чата из БД по chat_id"""
    try:
        cur.execute(f'''
                        SELECT chat_name
                        FROM chat_information 
                        WHERE chat_id = "{chat_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_chat_name')



def return_chat_information(chat_id):
    """Возвращает информацию о чате из БД по chat_id"""
    try:
        cur.execute(f'''
                        SELECT chat_name, chat_type
                        FROM chat_information 
                        WHERE chat_id = "{chat_id}"
                    ''')
        result = cur.fetchone()
        if result is not None:
            return result
        else:
            return False
    except Exception:
        print(f'{Exception=}; Type: {type(Exception)}; Method: services.database_controls'
              f'.return_chat_information')

