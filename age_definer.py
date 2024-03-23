# We need to write a code that gives out certain messages based on the age of the user.
# The age will be an input to the the age asked.
# Different age range will have different messages.
# This has to to be done using if, elif and else statements.
# Issue 1: Enhancing Age Range Messages
age = int(input("Enter your age between 0 to 100?"))

if age < 13:
    print("You qualify for a kiddie discount")
elif age == 21:
    print("Congrats on your 21st")
elif age > 100:
    print("Sorry, you are dead")
elif age >= 65:
    print("Enjoy your retirement")
elif age >= 40:
    print("You're over the hill")
elif age >= 25:
    print("You're an adult now")
elif age >= 18:
    print("Welcome to adulthood")
else:
    print("Age is just a number")