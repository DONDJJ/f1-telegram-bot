

def get_or_save_user(chat_id, cursor, conn):
    cursor.execute(f'SELECT * FROM "users" WHERE chatid={chat_id};')
    temp_list=[x for x in cursor]
    (_id, chatid, chosen_year) = temp_list[0] if temp_list else (None, None, None)
    if chatid:
        return "", chosen_year
    else:
        cursor.execute(f'INSERT INTO users (chatid,chosen_year) VALUES ({chat_id}, 2021);')
        conn.commit()
        cursor.execute(f'SELECT * FROM "users" WHERE chatid={chat_id};')
        (_id, chatid, chosen_year) = [x for x in cursor][0]
        return "Добро пожаловать!", chosen_year


def change_chosen_year(chat_id, new_year, cursor, conn):
    cursor.execute(f"UPDATE users SET chosen_year={new_year} WHERE chatid={chat_id}")
    conn.commit()


def create_table(cursor, conn):
    cursor.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, chatid integer, chosen_year integer)")
    conn.commit()
