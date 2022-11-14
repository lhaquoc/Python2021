# Functions and Variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")


def main():
    print("We can just give the function numbers directly:")
    cheese_and_crackers(10, 20)
    print("OR, we can use variables from your script:")
    amount_of_cheese = 15
    amount_of_crackers = 40
    cheese_and_crackers(amount_of_cheese, amount_of_crackers)
    print("We can even do math inside too:")
    cheese_and_crackers(10 + 15, 7 + 12)
    print("And we can combine the two, variables and math:")
    cheese_and_crackers(amount_of_cheese + 23, amount_of_crackers + 15)


if __name__ == '__main__':
    main()
