from db.mongo import mongo_connection
import hashlib

class UserSettings:
    def __init__(self, username, pwd):
        self.USERNAME = username
        self.PASSWORD = pwd
        if self.check_credentials():
            print(f"User Name: {self.USERNAME}\nUserID: {self.USERID}")
    
    # 查看用户名和密码对不对，没有的话创建
    def check_credentials(self) -> bool:
        up_collection = mongo_connection["credentials"]["users_pwds"] # credential collection in MongoDB
        user_record = up_collection.find_one({"username": self.USERNAME})
        hashed_password = hashlib.sha256(self.PASSWORD.encode()).hexdigest()

        if not user_record:
            print(f"User '{self.USERNAME}' does not exist, creating new database and updating credentials.")
            new_db = mongo_connection[self.USERNAME]
            new_db.create_collection("init_collection")
            
            up_collection.insert_one({
                "username": self.USERNAME,
                "password": hashed_password
            })

            # USERID会用来在云端和角色、物品、事件等object相连合
            self.USERID = hashlib.sha256(f"{self.USERNAME}:{self.PASSWORD}".encode()).hexdigest()
            self.MONGO_DATABASE_NAME = hashlib.md5(f"{self.USERNAME}:{self.PASSWORD}".encode()).hexdigest()
            return True
        
        else:
            if user_record["password"] != hashed_password:
                print("Password is incorrect.")
                return False
            else:
                self.USERID = hashlib.sha256(f"{self.USERNAME}:{self.PASSWORD}".encode()).hexdigest()
                self.MONGO_DATABASE_NAME = hashlib.md5(f"{self.USERNAME}:{self.PASSWORD}".encode()).hexdigest()
                print("Found User Record. Logged In.")
                return True

user_credentials = UserSettings("he525", "12345")