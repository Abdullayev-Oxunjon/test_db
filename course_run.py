from course_servicec import all_course_query,menu
from course_servicec import delete_course_query,update_course_query
from course_servicec import add_course_query,get_course_query
from course_colorama import print_red


def run():

    while True:
        choice =menu()

        if choice == "1":
            all_course_query()

        elif choice == "2":
            add_course_query()

        elif choice == "3":
            update_course_query()

        elif choice == "4":
            delete_course_query()

        elif choice == "5":
            get_course_query()

        elif choice == "6":
            break
        else:
            print_red("Wrong choice ")


run()





