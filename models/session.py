import sqlite3

from base_model import AbstractBaseModel

class session(AbstractBaseModel):
    TABLE_NAME = "session"

    def __init__(self, id=None,  start_date=None,  end_date=None) -> None:
        self.id = id
        self. start_date = start_date
        self.end_date = end_date
        
      
    def save(self):
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET start_date=?,end_date=?  WHERE id=?"
            
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.start_date, self.end_date))
        else:
            # save into the database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (start_date, end_date) VALUES(?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.start_date, self.end_date))

                new_instance_id = cursor.execute(f"SELECT MAX(id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.id = new_instance_id

    def read(id=None):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT (id,start_date, end_date) FROM {self.__class__.TABLE_NAME} WHERE id=?"

                result = cursor.execute(query, (id, )).fetchone()

                sess = __class__(start_date=result[1],end_date=result[2])
                sess.id = result[0]

                return sess
            else:
                query = f"SELECT (id,start_date, end_date ) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                sess = []

                for result in results:

                  sess = __class__(start_date=result[1],end_date=result[2])
                  sess.id = result[0]

                  ses.append(sess)
                
                  return ses
    
    def delete(self):
        if self.id:
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE id=?", (self.id, ))