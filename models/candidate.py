import sqlite3

from models.base_model import AbstractBaseModel

class Candidate(AbstractBaseModel):
    TABLE_NAME = "candidate"

    def __init__(self, id=None, name=None, picture=None, session=None, position=None, max_vote=None) -> None:
        self.id = id
        self.name = name
        self.picture = picture
        self.session = session
        self.position = position
        self.max_vote = max_vote 

    def save(self):
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET name=?,picture=?,session=?,position=?,max_vote=? WHERE id=?"
            
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.id, self.name, self.picture, self.session, self.postion, self.max_vote))
        else:
            # save into the database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (name, picture, session, position,max_vote) VALUES(?,?,?,?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.name, self.picture, self.session, self.position,self.max_vote
                ))

                new_instance_id = cursor.execute(f"SELECT MAX(id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.id = new_instance_id

    def read(id=None):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT (id,name, picture, session, position,max_vote) FROM {self.__class__.TABLE_NAME} WHERE id=?"

                result = cursor.execute(query, (id, )).fetchone()

                votes = __class__(name=result[1], picture=result[2], session=result[3], position=result[4], max_vote=result[5])
                votes.id = result[0]

                return votes
            else:
                query = f"SELECT (id,name, picture, session, position,max_vote) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                votes = []

                for result in results:
                    votes = __class__(name=result[1], picture=result[2], session=result[3], position=result[4], max_vote=result[5])
                    votes.id = result[0]

                    vote.append(votes)
                
                return vote
    
    def delete(self):
        if self.id:
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE id=?", (self.id, ))