import sqlite3
import os

from .base_model import AbstractBaseModel

PATH_TO_DB = os.path.join(os.path.dirname(__file__), "db.sqlite")

class Voters(AbstractBaseModel):
    TABLE_NAME = "voters"

    def __init__(self, id=None, candidate_id=None):
        self.id = id
        self.candidate_id = candidate_id
      
    def save(self):
        if self.id:
            query = f"UPDATE {self.TABLE_NAME} SET candidate_id=? WHERE id=?"
            params = (self.candidate_id, self.id)
        else:
            query = f"INSERT INTO {self.TABLE_NAME} (candidate_id) VALUES(?)"
            params = (self.candidate_id,)
        
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            if not self.id:
                self.id = cursor.lastrowid

    @classmethod
    def read(cls, id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT id, candidate_id FROM {cls.TABLE_NAME} WHERE id=?"
                result = cursor.execute(query, (id,)).fetchone()
                if result:
                    return cls(id=result[0], candidate_id=result[1])
            else:
                query = f"SELECT id, candidate_id FROM {cls.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                voters_list = []
                for result in results:
                    voter = cls(id=result[0], candidate_id=result[1])
                    voters_list.append(voter)
                return voters_list
    
    def delete(self):
        if self.id:
            with sqlite3.connect(PATH_TO_DB) as connection:
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", (self.id, ))
