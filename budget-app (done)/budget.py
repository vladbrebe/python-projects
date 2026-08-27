"""built at freeCodeCamp

A `Category` holds a ledger:list of deposits and withdrawals, supports transfers
between categories. `create_spend_chart` renders the
share of total *withdrawals* for each category as a bar chart.
"""


class Category:

    # name: category name
    # ledger: keeps track of transactions in the form {'amount': amount, 'description': description}
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Deposit an amount in the ledger
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})

    # Withdraw an amount from the ledger
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    # Returns the net balance in the ledger
    def get_balance(self) -> float:
        total = 0
        for dictionary in self.ledger:
            total += dictionary['amount']
        return total

    # Transfers from a starting category to an end category
    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    # checks if there is at least 'amount' net money in the ledger
    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title_line = self.name.center(30,"*")
        body = [title_line]

        for item in self.ledger:
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"[:7]
            body.append(f"{desc:<23}{amount:>7}")

        body.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(body)


# Creates a spending chart to view all the SPENDINGS for a list of categories, grouped by category
def create_spend_chart(categories: list[Category]) -> str:
    lines = "Percentage spent by category"

    categories_total = []
    total = 0
    # finds all the spendings in a category
    for category in categories: 
        running_category_total = 0   
        for item in category.ledger: 
            if item['amount'] < 0:
                running_category_total += item['amount']
                total += item['amount']
        categories_total.append((category.name, running_category_total))

    # creates the bar chart, starting from the top and working down
    # example row: 90 | o  o  
    for level in range(100, -1, -10):
        row = f"\n{level:>3}| "
        for _name, amount in categories_total:
            if amount/total > level/100:
                row += "o  "
            else:
                row += "   "
        lines += row
    lines += "\n    -" + 3*"-"*len(categories)

    # labels each bar with the category name
    longest = max([len(name) for name, _ in categories_total])
    titles  = [f"{name:<{longest}}" for name, _ in categories_total]

    for level in range(longest):
        lines += "\n     "
        for title in titles:
            lines += title[level] + "  "
    return(lines)           

# example
def main() -> None:

    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")

    clothing = Category("Clothing")
    food.transfer(50, clothing)
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing.withdraw(13, "shirt")

    entertainment = Category("Entertainment")
    entertainment.deposit(200, "initial deposit")
    entertainment.withdraw(35.50, "cinema")

    print(food)
    print()
    print(clothing)
    print()
    print(create_spend_chart([food, clothing, entertainment]))


if __name__ == "__main__":
    main()
