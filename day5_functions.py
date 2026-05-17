from graph import income_expense_graph


def is_valid_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def get_grade(avg):
    if avg > 95:
        return "A+"
    elif avg > 85:
        return "A"
    elif avg > 80:
        return "B+"
    elif avg > 75:
        return "B"
    elif avg > 60:
        return "C"
    elif avg > 40:
        return "D"
    else:
        return "Failed"


def sum_of_array(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total


def calculate_average(total, number_of_subjects):
    return total / number_of_subjects


def format_student(id, name, marks=[], PRN_num=0):
    total_marks = sum_of_array(marks)
    avg = calculate_average(total_marks, len(marks))
    grade = get_grade(avg)
    return {"id": id, "prn_no": PRN_num, "name": name, "marks": marks, "grade": grade}


def is_PRN_number_exist(PRN_num, students):
    is_exist = False
    for stu in students:
        if stu["prn_no"] == PRN_num:
            is_exist = True
    return is_exist


def take_student_details(id):
    name = input("Enter student name: ")
    PRN_num = int(input("Enter Student PRN NO: "))
    is_prn_num_exist = is_PRN_number_exist(PRN_num)
    if is_prn_num_exist:
        return "PRN_EXIST"
    number_of_subjects = int(input("How many subjects? :"))
    marks = []
    for i in range(number_of_subjects):
        mark = int(input(f"Enter marks of subject {i+1}: "))
        marks.append(mark)
    return format_student(id, name, marks, PRN_num)


def store_student(students, student):
    students.append(student)
    return students


def get_all_students(students):
    print("ID\tNAME\t\t\tMARKS\t\tTOTAL\tGRADE")
    for s in students:
        print(
            f"{s["id"]}\t{s["name"]}\t{s["marks"]}\t{sum_of_array(s["marks"])}\t{s["grade"]}"
        )


def find_student_by_prn(PRN_num, students):
    student = []
    for stu in students:
        if stu["prn_no"] == PRN_num:
            student = stu
            break
    return student


def get_last_id(obj):
    return 1 if len(obj) == 0 else obj[len(obj) - 1]["id"]


def take_student_contact_details(id, students):
    PRN_Number = int(input("Enter student PRN Number: "))
    is_exist = is_PRN_number_exist(PRN_Number, students)
    if not is_exist:
        return "PRN_NOT_EXIST"
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    student = find_student_by_prn(PRN_Number, students)
    return {"id": id, "student_id": student["id"], "phone": phone, "email": email}


def store_student_contact(student_contacts, student_contact):
    student_contacts.append(student_contact)
    return student_contacts


def get_student_details_id(student_id, students):
    student = {}
    for i in students:
        if i["id"] == student_id:
            student = i
    return student


def find_student_by_email(email, students, contacts):
    student = {}
    contact_details = []
    for contact in contacts:
        if contact["email"] == email:
            contact_details.append(contact)
    if len(contacts) > 0:
        student = get_student_details_id(contact_details[0]["student_id"], students)

    student["contact_details"] = contact_details
    return student


# Income Expense
def add_category(categories, category):
    categories.add(category)
    return categories


def update_category(categories, category, edit_index):
    list_cat = list(categories)
    get_remove_cat = list_cat[edit_index]
    categories.remove(get_remove_cat)
    categories.add(category)
    return categories


def list_of_cat(categories):

    cat = ""
    index = 0

    for category in list(categories):
        index += 1
        cat += str(index) + ". " + category + "\n"

    print(cat)


def get_category_by_index(categories, index):
    list_cat = list(categories)
    return list_cat[index]


def delete_category(categories, category):
    categories.remove(category)
    return categories


def income_expense(income_expense_data, data={}):
    income_expense_data.append(data)


def calculate_total_income(income_expense_data):
    total = 0
    for i in income_expense_data:
        if i["type"] == "INCOME":
            total = +i["amount"]
    return total


def calculate_total_expense(income_expense_data):
    total = 0
    for i in income_expense_data:
        if i["type"] == "EXPENSE":
            total = +i["amount"]
    return total


def show_dashboard(total_income, total_expense):
    income_expense_graph(total_income, total_expense)


# Mini Database System Functions


def add_user(users, user):
    id = get_last_id(users)
    user["id"] = id + 1
    users.append(user)
    print(f"{user["name"]} added successfully\n")
    return users


def view_users(users):
    print("total rows: ", len(users), "\n")
    for user in users:
        print(user, "\n")


def search_user(users, term):
    searched_users = []
    for user in users:
        if user["name"] == term:
            searched_users.append(user)
    print("total rows found: ", len(searched_users), "\n")
    for user in searched_users:
        print(user, "\n")


def get_user_by_id(users, user_id):
    single_user = {}
    for user in users:
        if user["id"] == user_id:
            single_user = user
            break
    return single_user


def delete_user(users, deleted_user_id):
    user = get_user_by_id(users, deleted_user_id)
    users.remove(user)
    print("1 user deleted successfully\n")
    return users
