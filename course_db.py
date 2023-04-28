import sqlite3

connection = sqlite3.connect("course.db")
cursor = connection.cursor()

cursor.execute("""

    create table if not exists course(

    id integer primary key ,
    title varchar ,
    description varchar ,
    mentor varchar ,
    during integer  ,
    price float ,
    completed varchar 
    
    )
""")

add_course = """
     insert into course (title,description,mentor,during,price,completed) values (? , ? , ?, ?, ?, ?)


    """




def commit(func):
    def wrapper(*args, **kwargs):
        responce = func(*args, **kwargs)
        connection.commit()
        return responce

    return wrapper


