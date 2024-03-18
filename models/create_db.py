import os
import sqlite3

PATH_TO_DB = os.path.join(
    os.path.dirname(__file__),
    "db.sqlite"
)

create_candidate_table_query = "CREATE TABLE candidate (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, session integer, position interger, max_vote interger, picture varchar(255) not null,  FOREIGN KEY(session) REFERENCES session(id))";

create_session_table_query = "CREATE TABLE session(id INTEGER PRIMARY KEY AUTOINCREMENT, start_date DATETIME, end_date DATETIME)";



create_voters_table_query = "CREATE TABLE voters(id INTEGER PRIMARY KEY AUTOINCREMENT, candidate_id ,FOREIGN KEY(candidate_id) REFERENCES candidate(id))"

with sqlite3.connect(PATH_TO_DB) as connection:
    cursor = connection.cursor()

    for query in [create_candidate_table_query, create_session_table_query, create_voters_table_query]:
        cursor.execute(query)    