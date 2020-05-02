import sqlite3
from datetime import datetime

db_path = "autoMachine.db"

class ConnectDB:
    def __init__(self):
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("CREATE TABLE if not exists api_process_log (id INTEGER primary key AUTOINCREMENT, url varchar, address varchar, "
                           "message varchar, query_time time , create_time current_date )")
        except sqlite3.Error as error:
            print("connect DB init error ", error)
        finally:
            if conn:
                self.close_connect(conn)

    def insert(self, url, address, message, create_time):
        try:
            conn = sqlite3.connect("../" + db_path)
            c = conn.cursor()
            data = (url, address, message, create_time)
            c.execute("insert into api_process_log (url, address, message, create_time) values (?, ?, ?, ?)", data)
        except sqlite3.Error as error:
            print("connect DB insert error ", error)
        finally:
            if conn:
                self.close_connect(conn)

        return c.lastrowid

    def update(self, query_time, id):
        try:
            conn = sqlite3.connect("../" + db_path)
            c = conn.cursor()
            data = (query_time, id)
            c.execute("update api_process_log set query_time = ? where id = ?", data)
        except sqlite3.Error as error:
            print("update db error ", error)
        finally:
            if conn:
                self.close_connect(conn)

    @staticmethod
    def close_connect(conn):
        conn.commit()
        conn.close()

# if __name__ == "__main__":
#     db = ConnectDB()
#     db.insert("2222", datetime.now())

