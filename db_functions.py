

def get_or_save_user(chat_id):
    pass


def change_chosen_year(chat_id, new_year):
    pass

def create_table(cursor, conn):
    cursor.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, chatid integer, chosen_year integer)")
    conn.commit()
