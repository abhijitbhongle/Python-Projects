print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is your name?") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
Name= name1+ name2
Name=Name.lower()
t=Name.count("t")
r=Name.count("r")
u=Name.count("u")
e=Name.count("e")
first_digit=t+r+u+e
l=Name.count("l")
o=Name.count("o")
v=Name.count("v")
e=Name.count("e")
second_digit=l+o+v+e
Love_score=str(first_digit)+str(second_digit)
print(f"Your love score is{Love_score}")
if Love_score >="40" and Love_score <="50":
  print(f"Your score is  {Love_score}, you are alright together")

else:
  print(f"Your score is {Love_score}")
