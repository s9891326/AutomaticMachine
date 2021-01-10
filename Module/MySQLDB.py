from datetime import datetime
from configparser import ConfigParser
import MySQLdb


class Mysql:
    def __init__(self):
        cfg = ConfigParser()
        cfg.read('Resource/resource.ini')

        host = cfg.get("database", "host")
        user = cfg.get("database", "user")
        password = cfg.get("database", "password")
        db = cfg.get("database", "db")

        self.db = MySQLdb.connect(host=host, user=user, password=password, db=db, charset="utf8")
        self.cursor = self.db.cursor()

    def insert(self, url, address, message, create_time):
        data = {"url": url, "address": address, "message": message, "create_time": create_time}
        self.cursor.execute(
            "insert into api_process_log (url, address, message, create_time) values (%(url)s, %(address)s, %(message)s, %(create_time)s)",
            data)
        self.db.commit()
        return self.cursor.lastrowid

    def update(self, query_time, id):
        data = {"query_time": query_time, "id": id}
        self.cursor.execute("update api_process_log set query_time = %(query_time)s where id = %(id)s", data)
        self.db.commit()

    def close(self):
        self.db.close()

# if __name__ == "__main__":
#     db = Mysql()
#     time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     db.insert("123", "456", "123", time)
#     db.close()
