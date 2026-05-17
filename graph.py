import matplotlib.pyplot as plt


def demo_graph():
    languages = ["Python", "JS", "PHP"]
    votes = [90, 70, 40]
    plt.bar(languages, votes)
    plt.title("Programming Languages")
    plt.show()


def income_expense_graph(total_income, total_expense):
    types = ["Income", "Expense"]
    results = [total_income, total_expense]
    plt.bar(types, results)
    plt.title("Icome Expense Graph")
    plt.show()


# income_expense_graph(30000,2000)