game_images = [rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >=3:
  print("You typed an invalid number, you lose")
else:  
  print (game_images[user_choice])
  computer_choice= random.randint(0,2)
  print("Computer chose:")
  print(game_images[computer_choice])
  if user_choice == computer_choice:
    print("Its a draw")
  elif user_choice==0 and computer_choice == 1:
    print("You lose ")
  elif user_choice==0 and computer_choice == 2:
    print("You win")
  elif user_choice ==1 and computer_choice == 0 : 
    print ("You win")  
  elif user_choice ==1 and computer_choice == 2 :
    print("You win")
  elif user_choice == 2 and computer_choice == 0 :
    print("You lose")
  elif user_choice == 2 and computer_choice == 1 :
    print("You win")
