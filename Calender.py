""" This program is meant to perform as a Command Line Calendar.
Users should be able to 1) View the Calendar, 2) Add an event to the calendar, 3) Update an existing event, 4) Delete an existing Event """

""" The program should behave in the following way: """

""" Print a welcome message to the user
Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit. """

from time import sleep, strftime

USER_NAME = input("What's your name?")
calendar = {}


def welcome():
    print("Hey " + USER_NAME + ", welcome to your calendar! It's like a visual representation of the rest of your life..")
    sleep(1)
    print("Calendar booting...")
    print("Today is " + strftime("%A, %B %d %Y"))
    print("The time is " + strftime("%H:%M:%S"))
    sleep(1)
    print("What would you like to do?")


def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print ("Calendar is empty.")
            else:
                print(calendar)
        elif user_choice == "U":
            date = input("What date? (MM/DD/YYY): ")
            update = input("Enter the update: ")
            calendar[date] = update
            print("Update Successful")
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            if len(date) > 10 or int(date[6:10]) < int(strftime("%Y")):
                print("Invalid Date Entered")
                try_again = input("Try again? Y or N: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print("Event Successfully Added")
                print(calendar)
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print("Calendar is Empty")
            else:
                event = input("What event?")
                for date in list(calendar):
                    if event == calendar[date]:
                        del calendar[date]
                        print("Event Successfully Deleted")
                        print(calendar)
        elif user_choice == "X":
            print("Exiting Program")
            start = False
        else:
            print ("TRASH!")


start_calendar()
