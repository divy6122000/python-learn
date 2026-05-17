from day5_functions import (
    add_category,
    list_of_cat,
    update_category,
    delete_category,
    get_category_by_index,
    income_expense,
    show_dashboard,
    calculate_total_income,
    calculate_total_expense,
)


def main():
    categories = {"Accountant", "IT"}
    income_expense_data = [
        {
            "id": 1,
            "type": "INCOME",
            "amount": 200,
            "date": "12-05-2026",
            "category": "Accountant",
        },
        {
            "id": 2,
            "type": "INCOME",
            "amount": 2090,
            "date": "12-05-2026",
            "category": "Accountant",
        },
        {
            "id": 1,
            "type": "EXPENSE",
            "amount": 200,
            "date": "12-05-2026",
            "category": "Accountant",
        }
    ]
    print(
        "1.Dashboard\n2.Add Category\n3.Update Category\n4.Delete Category\n5.Income - Expense"
    )
    while True:
        user_input = input("Choose any: ")
        match user_input:
            case "1":
                print("Dashboard")
                show_dashboard(
                    calculate_total_income(income_expense_data),
                    calculate_total_expense(income_expense_data),
                )
            case "2":
                cat = input("Enter Category: ")
                categories = add_category(categories, cat)
                print("Category added successfully")
            case "3":
                list_of_cat(categories)
                cat_index = int(input("which category want to update?: "))
                new_cat = input("Enter update Category: ")
                new_updated_index = cat_index = -1
                update_category(categories, new_cat, new_updated_index)
                print("Category updated successfully")
            case "4":
                cat = input("Enter delete Category name: ")
                delete_category(categories, cat)
            case "5":
                type = input("1. Income\n2. Expense: ")
                list_of_cat(categories)
                cat_index = int(input("choose category: "))
                new_cat_index = cat_index - 1
                category = get_category_by_index(categories, new_cat_index)
                amount = float(input("Enter amount: "))
                date = input("Enter date (DD-MM-YYYY): ")
                in_type = "INCOME" if type == "1" else "EXPENSE"
                data = {
                    "type": in_type,
                    "amount": amount,
                    "category": category,
                    "amount": amount,
                    "date": date,
                }
                income_expense(income_expense_data, data)
                print("Record added successfully")


main()
