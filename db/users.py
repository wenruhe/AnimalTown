from db.mongo import connection

def check_username(username):
    database_names = connection.list_database_names()
    print(database_names)
    if username in database_names:
        return True
    else:
        return False

def create_new_user(username):
    db = connection[username]
    db['init'].insert_one({'Created': True})