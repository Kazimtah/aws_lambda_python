import sqlite3

course = [(456,"Js Coursse", 235, 50),(234, "Java Course", 452, 20),(567, "Node.js", 735,70)]
DB_Name = 'sqlite_db.db'
with sqlite3.connect(DB_Name) as sqllite_conne:
    sql_request = "INSERT INTO Course VALUES(?,?,?,?)"
    sqllite_conne.execute(sql_request,[i for i in course])
    sqllite_conne.commit()



# with sqlite3.connect(DB_Name) as sqllite:
#     sql_request = "SELECT * FROM Course WHERE review_qnty >=30"
#     sql_curser = sqllite.execute(sql_request)
#     for record in sql_curser:
#         print(record)
# with sqlite3.connect(DB_Name) as sqllite3_dabase:
#     sql_request = "INSERT INTO Course VALUES(?,?,?,?)"
#     sqllite3_dabase.execute(sql_request,(251, "ptyhon course", 100, 30))
#     sqllite3_dabase.commit()

# """
# with sqlite3.connect(DB_Name) as sqllite:
#     sql_request = """ CREATE TABLE IF NOT EXISTS
#     Course(id integer PRIMARY KEY,
#     title text not NULL,
#     student_qnty integer,
#     review_qnty integer 
#     #);
#     """
#     sqllite.execute(sql_request)
# """


#with sqlite3.connect(DB_Name) as sqllite:
 #   print(sqllite)
