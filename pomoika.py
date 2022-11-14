import sqlite3
def add_member_in_tag_list(message: types.Message):
   """Метод добавляет юзера в тег лист. Если чат не групповой - возвращает сообщение с ошибкой"""
    # Чат групповой?
    if not chat_controls.check_chat_is_group(str(message.chat.type)):
        return 'Tag list is only used in group chats!'
    # Связь юзер/чат в summary есть?
    if not tl_db_queries.return_taglist_intersection(str(message.from_user.id),
                                                     str(message.chat.id)):
        # Пользователь есть?
        if not database_controls.return_user_primary_key(str(message.from_user.id)):
            # Апдейт юзера
            database_controls.update_member_information(str(message.from_user.id),
                                                        str(message.from_user.username),
                                                        str(message.from_user.first_name),
                                                        str(message.from_user.last_name),
                                                        str(message.from_user.is_premium))
        else:
            database_controls.write_member_information(str(message.from_user.id),
                                                       str(message.from_user.username),
                                                       str(message.from_user.first_name),
                                                       str(message.from_user.last_name),
                                                       str(message.from_user.is_premium))
        # Чат есть?
        if not database_controls.return_chat_name(str(message.chat.id)):
            # Апдейт чата
            database_controls.update_chat_information(str(message.chat.id),
                                                      str(message.chat.title),
                                                      str(message.chat.type))
        # Создать чат
        else:
            database_controls.write_chat_information(str(message.chat.id),
                                                     str(message.chat.title),
                                                     str(message.chat.type))
        # Добавить связь в summary
        tl_db_queries.add_taglist_intersection(str(message.from_user.id),
                                               str(message.chat.id))
        return 'User was added in tag list.'
    else:
        return 'The user is already in the list.'


print(r'[#msg_temp][\s]*[#del][\s]*[$][\s]*[\w|\W]*[\s]*[$][\s]*[\w|\W]*[\s]*[$][\s]*[\w|\W]*')


db_path = f'./file_storage/db_storage.db'
member_db = sqlite3.connect(f'{db_path}')
cur = member_db.cursor()
def return_all_chat_where_user_is_admin(user_id: str):
    """Возвращает все chat_id, chat_name, где юзер - админ"""
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
    result = (cur.fetchall())
    return result


print(return_all_chat_where_user_is_admin('227839513'))