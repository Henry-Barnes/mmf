# Functions go here
def int_check(question):
    """"Checks that users enter an integer  that is more than zero
    (or the optional exit code)"""

    error = "Oops - please enter an integer more than zero."

    while True:
        response = input(question).lower()

        if response == "xxx":
            return response

        try:
            # change the response to an integer and check that it's more than zero
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


# Main Routine goes here

# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# loop for testing purposes
while True:
    print()

    # ask user for their name (and check it's not blank)
    name = not_blank("Name: ")

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child ticket price is $7.50
    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket ($10.50)
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    # Senior Citizen ticket ($6.50)
    elif 65 <= age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method ( cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # calculate total payable...
    total_to_pay = ticket_price + surcharge

    print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}\n")
