# DAY 5: DATA STRUCTURES (VERY IMPORTANT FOR AI)
# 🧪 DAY 5 PROJECTS

from day5_functions import (
    take_student_details,
    store_student,
    get_all_students,
    get_last_id,
    take_student_contact_details,
    store_student_contact,
    find_student_by_email,
)


# 1. Student Management System
def main():
    students = [
        {
            "id": 1,
            "prn_no": 1001,
            "name": "Divy Modi",
            "marks": [30, 40, 60, 30, 60],
            "grade": "B+",
        },
        {
            "id": 2,
            "prn_no": 1002,
            "name": "John Doe",
            "marks": [30, 40, 20, 30, 60],
            "grade": "C+",
        },
        {
            "id": 3,
            "prn_no": 1003,
            "name": "Ram charan",
            "marks": [70, 60, 80, 80, 90],
            "grade": "A",
        },
    ]
    student_contacts = [
        {
            "id": 1,
            "student_id": 3,
            "phone": "7990675566",
            "email": "ramcharan123@gmail.com",
        }
    ]
    while True:
        print(
            "1.Student Management System\n2.Get All Students records\n3.Student Contact book\n4.Search Students\n5.Exit"
        )
        user_input = input("Choose option: ")
        match user_input:
            case "1":
                id = get_last_id(students) + 1  # Get last record id
                student = take_student_details(id)
                if student == "PRN_EXIST":
                    print("This PRN is already Exist")
                    return
                students = store_student(students, student)
                print("New record added\n")
                print(students[len(students) - 1])
            case "2":
                get_all_students(students)
            case "3":
                id = get_last_id(student_contacts) + 1  # Get last record id
                contact = take_student_contact_details(id,students)
                store_student_contact(student_contacts, contact)
                print("New contact added\n")
                print(student_contacts[len(student_contacts) - 1])

            case "4":
                user_email = input("Enter student email: ")
                data = find_student_by_email(user_email,students,student_contacts)
                print(data)

            case "5":
                break
            case _:
                print("Please choose only 1 to 4 only")


main()
