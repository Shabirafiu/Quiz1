"""
Define a function named which_day.

It will ask for any of the capital letters: F, M, S, T, W

These are the first letters of the day names in a week.

The function will decide which day by the first letter.

It may ask additional questins if needed?

Days:

Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

Additional questions by letter:

S:
"first day of weekend" or
"last day of weekend"

T:

"at the beginning of the week" or
"at the middle of the week"

Expected Output:
Please enter any of the capital letters: F, M, S, T, W :  T
Is it at the beginning of the week? Yes - No? No
Your day: THURSDAY


"""

def which_day():
    letter = input("Please enter any of the capital letters: F, M, S, T, W : ")

    days = " "

    if not (letter == "F" or letter == "M" or letter == "S" or letter == "T" or letter == "W"):
        print("Wrong input")


    else:

        if letter =="M":
            days = "Monday"
        elif letter == "T":
            question = input("Is it at the beginning of the week? Yes - No? ")
            if question == "Yes":
                days = "Tuesday"
            else:
                days = "Thursday"
        elif letter == "W":
            days = "Wednesday"
        elif letter == "F":
            days = "Friday"
        elif letter == "S":
            question = input("first day of weekend? Yes - No? ")
            if question == "Yes":
                days = "Saturday"
            else:
                days = "Sunday"


        print(f"Your day is : {days}")


which_day()












