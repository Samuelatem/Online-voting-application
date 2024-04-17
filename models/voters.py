import sqlite3

from .base_model import AbstractBaseModel

class voters(AbstractBaseModel):
    TABLE_NAME = "voters"

    def __init__(self, id=None, candidate_id=None) -> None:
        self.id = id
        self.candidate_id = candidate_id
      
    def save(self):
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET candidate_id=? WHERE id=?"
            
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.id, self.candidate_id))
        else:
            # save into the database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (candidate_id) VALUES(?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.candidate_id))

                new_instance_id = cursor.execute(f"SELECT MAX(id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.id = new_instance_id

    def read(id=None):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT (id,candidate_id) FROM {self.__class__.TABLE_NAME} WHERE id=?"

                result = cursor.execute(query, (id, )).fetchone()

                voters = __class__(candidate_id=result[1])
                voters.id = result[0]

                return voters
            else:
                query = f"SELECT (id,candidate_id ) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                voters = []

                for result in results:

                   voters = __class__(candidate_id=result[1])
                   voters.id = result[0]

                   voter.append(voters)
                
                return voter
    
    def delete(self):
        if self.id:
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE id=?", (self.id, ))