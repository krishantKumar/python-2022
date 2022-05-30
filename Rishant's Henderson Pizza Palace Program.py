from collections import namedtuple
import time

# Empty lists to store the orders of user
order_list = []
topping = []

# empty variable for total cost
order_cost = 0

# empty dictionary for Contact information for delivery
user_info = {}

# Dictionary Pizza to price, key = pizza, value = price
pizza_to_price = {
    "Classic Cheese": 8.50,
    "Classic Veggie": 8.50,
    "Pepperoni": 8.50,
    "Margherita": 8.50,
    "Spicy Paneer": 8.50,
    "Tandoori Chicken": 13.50,
    "Peri Peri Chicken": 13.50,
    "BBQ Chicken": 13.50,
    "Garlic Prawn": 13.50,
    "Americano": 8.50,
    "Supreme": 8.50,
    "Spicy Lamb": 13.50,
}

# Index of pizza to price
index_to_price = {
    "1": 8.50,
    "2": 8.50,
    "3": 8.50,
    "4": 8.50,
    "5": 8.50,
    "6": 8.50,
    "7": 8.50,
    "8": 13.50,
    "9": 13.50,
    "10": 13.50,
    "11": 13.50,
    "12": 13.50,
}

# Index to pizza
index_to_pizza = {
    "1": "\n- Classic Cheese",
    "2": "\n- Classic Veggie",
    "3": "\n- Pepperoni",
    "4": "\n- Margherita",
    "5": "\n- Spicy Paneer",
    "6": "\n- Americano",
    "7": "\n- Supreme",
    "8": "\n- BBQ Chicken",
    "9": "\n- Garlic Prawn",
    "10": "\n- Tandoori Chicken",
    "11": "\n- Peri Peri Chicken",
    "12": "\n- Spicy Lamb",
}

# defining namedtuple for pizza menu
menu_entry = namedtuple("menu_entry", ["index", "pizza", "price"])
pizza_options = []

# appends pizza options to named tuple
pizza_options.append(menu_entry(1, "Classic Cheese", "$8.50"))
pizza_options.append(menu_entry(2, "Classic Veggie", "$8.50"))
pizza_options.append(menu_entry(3, "Pepperoni", "$8.50"))
pizza_options.append(menu_entry(4, "Margherita", "$8.50"))
pizza_options.append(menu_entry(5, "Spicy Paneer", "$8.50"))
pizza_options.append(menu_entry(6, "Americano", "$8.50"))
pizza_options.append(menu_entry(7, "Supreme", "$8.50"))
pizza_options.append(menu_entry(8, "BBQ Chicken", "$13.50"))
pizza_options.append(menu_entry(9, "Garlic Prawn", "$13.50"))
pizza_options.append(menu_entry(10, "Tandoori Chicken", "$13.50"))
pizza_options.append(menu_entry(11, "Peri Peri Chicken", "$13.50"))
pizza_options.append(menu_entry(12, "Spicy Lamb", "$13.50"))

# toppings to price list
index_to_topping = {
    "1": " + Extra Cheese",
    "2": " + Extra Onions",
    "3": " + Extra Mushroom",
    "4": " + Extra Pepperoni",
    "5": " + Extra Olives",
    "6": " + Extra Chicken",
}

# defining namedtuple for Toppings Menu
topping_entry = namedtuple("topping_entry", ["index", "topping", "price"])
topping_options = []

# appends topping options to named tuple
topping_options.append(topping_entry(1, "Extra Cheese", "$0.50"))
topping_options.append(topping_entry(2, "Extra Onion", "$0.50"))
topping_options.append(topping_entry(3, "Extra Mushroom", "$0.50"))
topping_options.append(topping_entry(4, "Extra Pepperoni", "$0.50"))
topping_options.append(topping_entry(5, "Extra Olives", "$0.50"))
topping_options.append(topping_entry(6, "Extra Chicken", "$0.50"))


# prints and formats the pizza menu
def pizza_menu():
    print("\n\033[4;34m\033[1;94mOur selection of pizzas:\033[0m")
    for entry in pizza_options:
        index = str(getattr(entry, "index")).ljust(5)
        pizza = getattr(entry, "pizza").ljust(25)
        price = getattr(entry, "price").ljust(7)
        time.sleep(0.01)
        print("\033[1;92m{}\033[0m\033[1;34m{}\033[0m\033[1;91m{}\033[0m".format(index, pizza, price))


# Prints and formats the topping menu
def topping_menu():
    print("\n\033[4;34m\033[1;94mOur selection of toppings:\033[0m")
    for entry in topping_options:
        index = str(getattr(entry, "index")).ljust(5)
        topping = getattr(entry, "topping").ljust(25)
        price = getattr(entry, "price").ljust(7)
        time.sleep(0.01)
        print("\033[1;92m{}\033[0m\033[1;34m{}\033[0m\033[1;91m{}\033[0m".format(index, topping, price))


# Menu function prints out the instructions for the user so they can use a mode
# option for the Henderson Pizza Palace service.
def main_menu():
    """Prints out the instructions for the user so they can use an action option
    to use the Henderson Pizza Palace service."""
    print("\n\033[1;97mType: \n")
    print("'1' to view pizza menu\n")
    print("'2' to order pizza\n")
    print("'3' to cancel ordering\033[0m\n")


# Menu function prints out the instructions for the user so they can use a
# service option for the Henderson Pizza Palace service.
def servicing_menu(order_cost):
    """Prints out the instructions for the user so they can use a service option
    for the Henderson Pizza Palace service."""
    print("\n\033[1;97mHow would you like to receive your pizza?\n")
    print("'1' Delivery ($3 Delivery charge)\n")
    print("'2' Pick-up\n")
    print("'3' Go back to main menu\n\033[0m")
    global service_option
    service_repeat = True
    while service_repeat:
        service_option = input("\033[1;92m\nInput number here: \033[0m").strip()
        # Asks the user to input address and phone number
        # Will ask if contact information is correct
        # Will remove contact information and repeat if user inputs "no"
        contact_repeat = True

        if service_option == "1":
            print("\n\033[0;93mService Option: Delivery\033[0m\n")
            time.sleep(1)
            # adds $3 to user order cost as delivery has $3 charge
            order_cost += 3

            while contact_repeat:
                # error prevention
                try:
                    phone_number = int(
                        input("\033[1;92mPlease state your phone number: \033[0m").strip()
                    )
                except ValueError:
                    # tells user to enter an appropriate integer and goes back
                    # to phone number input
                    print("\n\033[1;91m\033[40mPlease input integers only!\033[0m\n")
                    continue
                # adds user phone number to user_info dictionary
                user_info["Phone number"] = phone_number

                address = input(
                    "\033[1;92m"
                    "\nPlease enter your delivery address: \033[0m"
                    ).strip()
                user_info["Address"] = address.title()

                name = input("\n\033[1;92mPlease enter your name: \033[0m").strip()
                user_info["Name"] = name.title()

                if len(name) <= 0 and len(address) <= 0:
                    print(
                        "\n\033[1;91m\033[40m"
                        "You have entered no name and no address! "
                        "Please enter them for contacting purposes.\033[0m\n"
                    )
                    continue

                elif len(name) <= 0:
                    print(
                        "\033[1;91m\033[40m"
                        "\nYou have entered no name! "
                        "Please enter them for contacting purposes.\033[0m\n"
                    )
                    continue

                elif len(address) <= 0:
                    print(
                        "\033[1;91m\033[40m"
                        "\nYou have entered no address! "
                        "Please enter them for contacting purposes.\033[0m\n"
                    )
                    continue

                else:
                    print("\n\033[1;97mYour Contact Information:\033[0m\033[1;96m")
                    # prints user info dictionary
                    for key, value in user_info.items():
                        print(key, ":", value)

                while True:
                    print("\033[0m\n\033[1;92mIs the contact information shown above correct?\033[0m")
                    correct_info = (
                        input("\033[1;92mAnswer ('yes' or 'no'): \033[0m").strip().lower()
                    )

                    if correct_info == "no" or correct_info == "n":
                        print("\n\033[1;91mPlease resubmit your contact information\033[0m\n")
                        time.sleep(1)
                        contact_repeat = True
                        break

                    # when the user enters 'yes'
                    elif correct_info == "yes" or correct_info == "y":
                        # exit loops
                        contact_repeat = False
                        break

                    # if user does not say either 'yes' or 'no'
                    else:
                        print(
                            "\033[1;91m\033[40m"
                            "\nPlease enter a valid response "
                            "('yes' or 'no')!\033[0m"
                        )
                        continue

        elif service_option == "2":
            print("\n\033[0;93mService Option: Pick-up\033[0m\n")
            time.sleep(1)

            while contact_repeat:
                name = input("\n\033[1;92mPlease enter your name: \033[0m").strip()
                # adds users name to dictionary
                user_info["Name"] = name.title()
                # prints user info
                if len(name) <= 0:
                    print(
                        "\033[0m\033[1;91m\033[40m"
                        "You have entered no name! "
                        "Please enter one for contating purposes.\033[0m"
                    )
                    continue

                else:
                    print('\033[1;96m')
                    for key, value in user_info.items():
                        print(key, ":", value)

                while True:
                    print("\033[0m\n\033[1;92mIs the contact information shown above correct?\033[0m")
                    correct_info = (
                        input("\033[1;92mAnswer ('yes' or 'no'):  \033[0m").strip().lower()
                    )

                    if correct_info == "no" or correct_info == "n":
                        print(
                            "\033[1;91mPlease resubmit your name for "
                            "contacting purposes!\n\033[0m"
                        )
                        time.sleep(1)
                        contact_repeat = True
                        break

                    elif correct_info == "yes" or correct_info == "y":
                        # exit loops
                        contact_repeat = False
                        break

                    else:
                        print(
                            "\n\033[1;91m\033[40mPlease enter a valid response ('yes' or 'no')!"
                            "\033[0m"
                            )
                        continue

        # heads back to main menu by exiting loop when user enters '3'
        elif service_option == "3":
            print("\033[0;93mHeading back to Main menu...\033[0m")
            time.sleep(1)
            main_menu()
            break

        else:
            print("\n\033[1;91m\033[40mPlease input a valid number ('1', '2' or '3'))\033[0m\n")
            continue

        service_repeat = False

    time.sleep(1)


# Function that takes in the users orders
def order(order_cost, topping):
    order_loop = 0
    ordering = True
    while ordering:
        order_loop += 1
        pizza_menu()
        print("\n\033[0;95mOrder using the number next to the name of the pizza.")
        time.sleep(0.5)
        print("To finish ordering, type 'end'.")
        time.sleep(0.5)
        print("To cancel ordering, type 'cancel'.\033[0m")
        time.sleep(0.5)
        new_order = input("\n\033[1;92mInput Pizza number here: \033[0m")
        # when user enters 'end' or ordering loops 5 times, prints users order,
        # cost, user info and also confirms order
        if new_order == "end" or order_loop > 5:
            
            print("\n\033[1;97mContact Information:\033[0m\n\033[1;96m")
            for key, value in user_info.items():
                print(key, ":", value)
            # shows the user their order
            print("\033[0m\n\033[1;97mYour order is:\033[0m")
            view_order()
            print("\n\033[1;91mTotal cost of this order is: ${}\033[0m".format(order_cost))

            correct_order = (
                input(
                    "\033[1;92m"
                    "\nIs your order correct? (Please input 'yes' or 'no'): "
                    "\033[0m"
                    )
                .strip()
                .lower()
            )
            # when the user confirms order, then
            if correct_order == "yes" or correct_order == "y":
                print(
                    "\033[46m"
                    "\nYour order will be ready soon! "
                    "Thanks for ordering at Henderson Pizza Palace!\n"
                    "\033[0m"
                )
                break

            # if the order is incorrect, the order list will be cleared
            elif correct_order == "no" or correct_order == "n":
                print("\n\033[0;33mTime to reorder your pizza...")
                time.sleep(1)
                order_list.clear()
                print("Previous order list cleared...\033[0m")
                order_loop = 0
                continue

            else:
                print("\033[1;91m\033[40mPlease enter 'yes' or 'no'\033[0m")

        # if number in index_to_pizza dictionary,
        # then pizza name is appended to order_list
        elif new_order in index_to_pizza:
            order_list.append(index_to_pizza.get(new_order))
            # if the number entered by user is associate with a pizza,
            # then price will be added and will move on to toppings
            if new_order in index_to_price:
                # adds cost of pizza to order_cost
                order_cost += index_to_price.get(new_order)
                topping_menu()
                time.sleep(1)
                print(
                    "\033[0;95m"
                    "\nAdd toppings using the number next to the "
                    "name of the topping."
                )
                time.sleep(1)
                print("To finish adding toppings, type 'end'.\033[0m")

                while True:
                    topping = input("\n\033[1;92mInput topping number here: \033[0m").strip()
                    if topping in index_to_topping:
                        order_list.append(index_to_topping.get(topping))
                        order_cost += 0.5
                    elif topping == "end":
                        print(
                            "\n\033[1;97m\033[0;101m"
                            "Current total cost of order is: ${}\033[0m".format(order_cost)
                        )
                        break
                    else:
                        print("\n\033[1;91m\033[40mThat is not one of the topping options!\033[0m\n")

        # when user enters 'cancel', they will be sent back to the main menu
        # and order_list will be cleared
        elif new_order == "cancel":
            order_list.clear()
            print("\033[0;93mOrder cleared!\033[0m\n\033[0;93mHeading back to Main menu...\033[0m")
            time.sleep(1)
            main_menu()
            break

        else:
            print("\n\033[1;91m\033[40mSorry, that is not one of the pizza options!\033[0m")
            continue

    print("\033[1;97m\033[0;101mYou ordered is:\033[0m")
    view_order()
    print("\n\033[1;97mTotal cost of order: \n${:.2f}\033[0m".format(order_cost))

    return order_cost


# Function that shows current orders in the order_list
def view_order():
    if len(order_list) > 0:
        for order in order_list:
            print("\033[1;96m{}\033[0m".format(order, topping))

    else:
        print("\033[1;91m\033[40mYou have no orders yet!\033[0m")


# Running main program loop (calling functions etc)
print("\033[1;37m\033[4;37m\nHenderson Pizza Palace\n")
print(
    "\nHello, Welcome to Henderson Pizza Palace text-based ordering system."
    "\nBelow is our Main menu, "
    "please enter a number associated with your required service.\033[0m"
)

time.sleep(2)
# Prints main menu
main_menu()

repeat = True
while repeat:
    # Ask user for number input
    main_menu_option = input("\n\033[1;92mInput number Here: \033[0m").strip()

    # Checking input and calls appropriate function -
    # this one calls the food menus
    if main_menu_option == "1":
        pizza_menu()
        time.sleep(1)
        topping_menu()
        time.sleep(1)
        main_menu()

    # this one calls the food menus
    elif main_menu_option == "2":
        time.sleep(1)
        servicing_menu(order_cost)
        if service_option == "3":
            continue
        order(order_cost, topping)

    elif main_menu_option == "3":

        if len(order_list) > 0:
            print(
                "\033[46m"
                "Thanks for purchasing from Henderson Pizza Palace! "
                "\nHope to see you again!\033[0m"
            )
            # clears order list
            order_list.clear()

        else:
            print("\033[46mThanks for visiting!\033[0m")
        repeat = False

    else:
        print("\033[1;91m\033[40m'{}' wasn't an option\033[0m\n".format(main_menu_option))