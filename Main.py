# Shopping Script
# Item list
import datetime as dt
def grocery():
    menu = {"Pencil": 10.00,
            "Sharpener": 5.00,
            "Paper": 30.00,
            "Eraser": 5.00,
            "Backpack": 100.00
            }

    # Prints item list
    print("---------ITEMS---------")

    for key, value in menu.items():
        print(f"{key:11}: PHP {value:.2f}")

    print("-----------------------")

    # Loop to fill the shopping cart
    cart = []
    total = 0
    shopOpen = True

    while shopOpen:
        userInput = input("Enter the items that you wanna add to your cart \n(Press Q to finish) (Press R to remove an item): ").capitalize()

        # Conditionals to check if user wants to exit or if the provided input is in the menu or if they want to remove something
        if userInput == "Q":
            break
        elif menu.get(userInput) is not None:
            print(f"{userInput.capitalize()} has been added to your cart")
            cart.append(userInput)
        elif userInput == "R":
            while True:
                removedItems = input("What would you like to remove (Press Q to exit)? ").capitalize()
                if removedItems in cart:
                    cart.remove(removedItems)
                    print(f"{removedItems} is removed from your cart")
                elif removedItems == "Q":
                    break
                else:
                    print("Invalid item")
                    continue
        else:
            print("Invalid item")
            continue

        # Shows every bought items
        print("---------CART----------")
        for userInput in cart:
            price = menu[userInput]
            print(f"{userInput.title()}: PHP {price:.2f}") # .title() is just like .capitalize() but instead it makes the first letter of each word capitalized
        print("-----------------------")

    # Totals and reviews the bought items
    print("---------TOTAL---------")
    for userInput in cart:
        price = menu[userInput]
        print(f"{userInput.title()}: PHP {price:.2f}")
        total += menu.get(userInput)
    print("-----------------------")

    # Finished transaction
    print(f"Your total: PHP {total}")
    print("-----------------------")

def Gcash():
    # User Information Variables
    gcashOpen = False
    userName = "Spenzer"
    userBalance = 1500.00
    mpin = 4567

    # Login Variables
    wrongTries = 0
    loginSuccess = False

    # Checks if the user is the owner of the account. By confirming the MPIN
    print("----------------GCASH-----------------")

    while wrongTries < 3:
        try:
            userInp = int(input("Enter your MPIN: "))
            if userInp == mpin:
                loginSuccess = True
                break  # Exit the loop immediately if MPIN is correct
            else:
                print("Incorrect MPIN. Try Again")
                print("-------------------------------------")
                wrongTries += 1
        except ValueError:
            print("Invalid MPIN. Try again.")
            print("-------------------------------------")
            continue

    # Opens Gcash if the MPIN is correct
    if loginSuccess:
        gcashOpen = True
        while gcashOpen:
            # Error handling for non-integer inputs and negative/zero amounts
            print("-----------------SEND-----------------")
            try:
                sendingAmt = int(input("Enter amount to send: "))
            except ValueError:
                print("Invalid Amount. Try again.")
                continue
            if sendingAmt <= 0 or sendingAmt > userBalance:
                print("Amount must be greater than 0 and\nless than your balance. Try again.")
                continue

            receiverNum = input("Enter receivers number: ")

            # Checks if the receiver number is valid (only digits and not empty)
            # You can also use len(receiverNum) == 11 to check if the number has 11 digits
            if receiverNum != "" and receiverNum.isdigit():
                # Gets Current Date and Time
                currentDate = dt.datetime.now()
                receipt = f"{userName} sent ${sendingAmt:.2f} to {receiverNum}"
                print("---------------RECEIPT----------------")
                print(receipt)
                print(f"Date: {currentDate:%Y-%m-%d}\nTime: {currentDate:%H:%M:%S}")
                print("---------------------------------------")
                userBalance -= sendingAmt
            else:
                print("Invalid Number. Try again.")
                continue
            break # Exit the while loop after a successful transaction. You can remove this if you want to allow multiple transactions in one session.
    else:
        print("Failed login attempt. Account Temporarily suspended")

Gcash()