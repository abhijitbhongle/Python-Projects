# We need to write a code that gives out certain messages based on the age of the user.
# The age will be an input to the the age asked.
# Different age range will have different messages.
# This has to to be done using if, elif and else statements.

<<<<<<< HEAD
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

# Issue 2: Input Validation
while True:
    try:
        age = int(input("Enter your age between 0 to 100? "))
        if 0 <= age <= 100:
            break
        else:
            print("Please enter a valid age between 0 and 100.")
    except ValueError:
        print("Please enter a valid integer age.")
=======
age=int(input("Enter you age between 0 to 100?"))
if age<13:
  print("You qualify for a kiddie discount ")
elif age==21:
  print("Congrats on your 21st")
#Next we will use the highest age range as the code will look at each line to give an ouput.
#e.g. if we were to use age range 40, the code will answer that if true and ignore the rest.
elif age> 100:
  print("Sorry, you are dead")
#The age logic applies here and we use the next highest age range i.e. 65+
elif age>= 65:
  print("Enjoy your retirement")
elif age>= 40:
 print(" You're over the hill")
else:
  print("Age is just a number")
>>>>>>> 2e18307164b32ed7472781b3364814ed51b293e1
