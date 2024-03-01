line1 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️","⬜️","️⬜️","️⬜️"]
line4 = ["⬜️️","⬜️️","⬜️️","⬜️","️⬜️","️⬜️"]
line5 = ["⬜️️","⬜️️","⬜️️","⬜️","️⬜️","️⬜️"]
map = [line1, line2, line3, line4, line5]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a","b","c","d","e"]
letter_index = abc.index(letter)
number_index = int(position[1])-1
map[letter_index][number_index]= " x"



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}")
