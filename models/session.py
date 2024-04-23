import sqlite3
from .base_model import AbstractBaseModel
import os

PATH_TO_DB = os.path.join(
    os.path.dirname(__file__),
    "db.sqlite"
)

class Session(AbstractBaseModel):
    TABLE_NAME = "session"

    def __init__(self, id=None, start_date=None, end_date=None):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
      
    def save(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if self.id:
                query = f"UPDATE {self.__class__.TABLE_NAME} SET start_date=?, end_date=? WHERE id=?"
                cursor.execute(query, (self.start_date, self.end_date, self.id))
            else:
                query = f"INSERT INTO {self.__class__.TABLE_NAME} (start_date, end_date) VALUES (?, ?)"
                cursor.execute(query, (self.start_date, self.end_date))

                self.id = cursor.lastrowid

    @staticmethod
    def read(id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT id, start_date, end_date FROM {Session.TABLE_NAME} WHERE id=?"
                result = cursor.execute(query, (id,)).fetchone()
                if result:
                    sess = Session(start_date=result[1], end_date=result[2])
                    sess.id = result[0]
                    return sess
            else:
                query = f"SELECT id, start_date, end_date FROM {Session.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                sessions = []
                for result in results:
                    sess = Session(start_date=result[1], end_date=result[2])
                    sess.id = result[0]
                    sessions.append(sess)
                return sessions
    
    def delete(self):
        if self.id:
            with sqlite3.connect(PATH_TO_DB) as connection:
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE id=?", (self.id,))