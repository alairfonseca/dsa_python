"""
Write a Python program that can “make change.” Your program should take two
numbers as input, one that is a monetary amount charged and the other that
is a monetary amount given. It should then return the number of each kind
of bill and coin to give back as change for the difference between the
amount given and the amount charged. The values assigned to the bills
and coins can be based on the monetary system of any current or former
government. Try to design your program so that it returns as few bills
and coins as possible.
"""

BILLS = {
    "200": 20000,
    "100": 10000,
    "50": 5000,
    "20": 2000,
    "10": 1000,
    "5": 500,
    "2": 200
}
COINS = {
    "1": 100,
    "0.50": 50,
    "0.25": 25,
    "0.10": 10,
    "0.05": 5
}


def to_cents(amount):
    return int(amount * 100)


def make_change(charge_amount, given_amount):
    if given_amount < charge_amount:
        return 0

    charge_amount = to_cents(charge_amount)
    given_amount = to_cents(given_amount)

    result = {}
    change = given_amount - charge_amount

    for (bill, value) in BILLS.items():
        if change >= value:
            result[bill] = int(change / value)
            change = change % value

    for (bill, value) in COINS.items():
        if change >= value:
            result[bill] = int(change / value)
            change = change % value

    return result


if __name__ == "__main__":
    print(make_change(34, 50))
    print(make_change(17.90, 20))
    print(make_change(17.85, 20))
    print(make_change(240, 250))
