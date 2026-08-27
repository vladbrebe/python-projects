from budget import Category, create_spend_chart


def test_deposit_and_balance():
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    assert food.get_balance() == 1000


def test_transfer_refused_without_funds():
    food = Category("Food")
    clothing = Category("Clothing")
    food.deposit(10)
    assert food.transfer(40, clothing) is False
    assert clothing.get_balance() == 0


def test_spend_chart_rounds_down_to_nearest_ten():
    food = Category("Food")
    food.deposit(900)
    food.withdraw(105.55)
    business = Category("Business")
    business.deposit(900)
    business.withdraw(720.00)
    entertainment = Category("Entertainment")
    entertainment.deposit(900)
    entertainment.withdraw(315.00)

    chart = create_spend_chart([business, food, entertainment])
    expected = (
        "Percentage spent by category\n"
        "100|          \n"
        " 90|          \n"
        " 80|          \n"
        " 70|          \n"
        " 60| o        \n"
        " 50| o        \n"
        " 40| o        \n"
        " 30| o        \n"
        " 20| o     o  \n"
        " 10| o     o  \n"
        "  0| o  o  o  \n"
        "    ----------\n"
        "     B  F  E  \n"
        "     u  o  n  \n"
        "     s  o  t  \n"
        "     i  d  e  \n"
        "     n     r  \n"
        "     e     t  \n"
        "     s     a  \n"
        "     s     i  \n"
        "           n  \n"
        "           m  \n"
        "           e  \n"
        "           n  \n"
        "           t  "
    )
    assert chart == expected
