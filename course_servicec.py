from course_db import commit,cursor,add_course
from course_colorama import print_red,print_cyan,print_yellow


def menu():

    print_yellow("List Course -------- (1)")
    print_yellow("Add Course --------- (2)")
    print_yellow("Update Course --------- (3)")
    print_yellow("Delete Course --------- (4)")
    print_yellow("Get Course --------- (5)")
    print_yellow("Quit ----------- (6)")
    return input("Choice : ")

@commit
def all_course_query():

    for  course in cursor.execute("""

        select * from course 

    """).fetchall():
        print(course)

def get_course_query():

    all_course_query()
    get = int(input(" --->"))
    kurs = cursor.execute(f""" select * from course where id = {get}""").fetchone()
    if not kurs:
        print_red("Wrong choice")
    else:
        print(kurs)



@commit
def add_course_query():

    title = input("Title : ")
    description = input("Description : ")
    mentor = input("Mentor : ")
    during = input("During : ")
    price = input("Price: ")
    completed = input("Completed: ")


    query_param = (title,description,mentor,during,price,completed)
    cursor.execute(add_course,query_param)



@commit

def update_course_query():

    all_course_query()
    id = int(input(" --->"))

    kurs = cursor.execute(f""" select * from course where id = {id}""").fetchone()

    if not kurs:
        print_red("Wrong choice")

    else:
        title = str(input("Title : "))
        description = str(input("description : "))
        mentor = str(input("mentor : "))
        during = input("during : ")
        price = input("price: ")
        completed = str(input("completed: "))

        cursor.execute(f"""

        update course set  title = "{title}",
         description = "{description}",
         mentor = "{mentor}",
         during = "{during}",
         price = '{price}',
         completed = "{completed}"
         where id = {id}


        """)
        print_cyan("Saccesfully update")



@commit
def delete_course_query():
    all_course_query()
    id = int(input(" --->"))

    kurs = cursor.execute(f""" select * from course where id = {id}""").fetchone()

    if not kurs:
        print_red("Wrong choice")

    else:
        cursor.execute(f"""

        delete from course where id = {id}

        """)
        print_cyan("Saccessfully delete")
