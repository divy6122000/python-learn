import json
from pathlib import Path, PosixPath


# file_path = "project/details/contact.json"
# path = Path(file_path)
# print(path.suffix)
def read_file(file_path):
    data = None
    with open(file_path, "r") as file:
        path = Path(file_path)
        if path.suffix == ".json":
            data = json.load(file)
        else:
            data = file.read()
    return data


def append_file(file_path, data):
    with open(file_path, "a") as file:
        path = Path(file_path)
        if path.suffix == ".json":
            json.dump(data, file)
        else:
            file.write(data)


def get_last_id(file_path):
    data = read_file(file_path)
    contacts = list(data)
    ids = []
    for contact in contacts:
        ids.append(contact["id"])
    return max(ids)


def add_contact(file_path, contact):
    path = Path(file_path)
    if not path.exists():
        path.touch()
    contact["id"] = get_last_id(file_path) + 1
    append_file(file_path, contact)
    print("Contact added successfully")


def view_contact(file_path):
    return read_file(file_path)


def search_contact(file_path, term):
    data = read_file(file_path)
    searched_contacts = []
    for i in data:
        # if i["name"] == term or i["phone"] == term or i["email"] == term:
        if term in [i["name"], i["phone"], i["email"]]:
            searched_contacts.append(i)
    print(f"{len(searched_contacts)} contacts found")
    return search_contact


def get_contact_by_id(file_path, contact_id):
    data = read_file(file_path)
    contact = {}
    for i in data:
        if i["id"] == contact_id:
            contact = i
            break
    return contact


def delete_contact(file_path, contact_id):
    contact = get_contact_by_id(contact_id)
    if len(contact) == 0:
        print("No contact found for delete\n")
        return False
    data = read_file(file_path)
    contacts = list(data)
    contacts.remove(contact)
    with open(file_path, "w") as file:
        json.dumps(contacts, file)
    print(f"id:{contact["id"]} name:{contact["name"]} Deleted successfully")
