from db.mongo import connection

def check_username(username):
    database_names = connection.list_database_names()
    if username in database_names:
        return True
    else:
        return False
