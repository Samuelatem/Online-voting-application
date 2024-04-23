import sqlite3
import os
from models.base_model import AbstractBaseModel

PATH_TO_DB = os.path.join(
    os.path.dirname(__file__),
    "db.sqlite"
)

class Candidate(AbstractBaseModel):
    TABLE_NAME = "candidate"

    def __init__(self, id=None, name=None, picture=None, session=None, position=None, max_vote=None):
        self.id = id
        self.name = name
        self.picture = picture
        self.session = session
        self.position = position
        self.max_vote = max_vote

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if self.id:
                query = f"UPDATE {self.TABLE_NAME} SET name=?, picture=?, session=?, position=?, max_vote=? WHERE id=?"
                cursor.execute(query, (self.name, self.picture, self.session, self.position, self.max_vote, self.id))
            else:
                query = f"INSERT INTO {self.TABLE_NAME} (name, picture, session, position, max_vote) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(query, (self.name, self.picture, self.session, self.position, self.max_vote))
                self.id = cursor.lastrowid

    @classmethod
    def read(cls, id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT id, name, picture, session, position, max_vote FROM {cls.TABLE_NAME} WHERE id=?"
                result = cursor.execute(query, (id,)).fetchone()
                if result:
                    return cls(id=result[0], name=result[1], picture=result[2], session=result[3], position=result[4], max_vote=result[5])
            else:
                query = f"SELECT id, name, picture, session, position, max_vote FROM {cls.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                candidates = []
                for result in results:
                    candidate = cls(id=result[0], name=result[1], picture=result[2], session=result[3], position=result[4], max_vote=result[5])
                    candidates.append(candidate)
                return candidates

    def delete(self):
        if self.id:
            with sqlite3.connect(PATH_TO_DB) as connection:
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", (self.id, ))