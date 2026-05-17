from day6.functions import add_contact, view_contact, search_contact, delete_contact

# 1. Persistent Contact Book


def main():
    print("1.Add Contact\n2.View Contacts\n3.Search Contacts\n4.Delete Contacts\n")
    while True:
        user_input = input("Choose operation: ")
        match user_input:
            case "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter Email address: ")
                contact = {"name": name, "phone": phone, "email": email}
                add_contact("day6/contacts.json", contact)
            case _:
                print("Please only enter 1 to 5 operations only")


main()
