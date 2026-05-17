from day5_functions import (
    add_user,
    view_users,
    search_user,
    get_user_by_id,
    delete_user,
)


def main():
    users = [{"id": 1, "name": "Divy"}]
    print("1.Add User\n2.View User\n3.Search Users\n4.Delete User\n4.Exit\n")
    while True:
        user_input = input("Choose any operation: ")
        match user_input:
            case "1":
                name = input("Enter user name: ")
                user = {"name": name}
                users = add_user(users, user)
            case "2":
                view_users(users)
            case "3":
                term = input("Enter user's name for searching: ")
                search_user(users, term)
            case "4":
                user_id = int(input("Enter user ID for delete: "))
                confirm = input("Are you sure want to delete this?(Y/N): ")
                if confirm == "Y":
                    delete_user(users, user_id)
                else:
                    print("This operation is not perform\n")
            case "5":
                print("Good Bye!")
                break
            case _:
                print("Please choose only 1 to 4 only")


main()
